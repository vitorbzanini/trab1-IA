import pandas as pd
from sklearn import neighbors
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score as acc_score
import pickle 
from tabulate import tabulate

x_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_attributes.csv")
x_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_attributes.csv")
x_validation = pd.read_csv(r"/home/vitor/IA/T1/Validation_dataset_attributes.csv")
y_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_classes.csv")
y_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_classes.csv")
y_validation = pd.read_csv(r"/home/vitor/IA/T1/Validation_dataset_classes.csv")

f = open("KNN_data.txt", "w")

new_x_train = pd.concat([x_train, x_test], axis=0)
new_y_train = pd.concat([y_train, y_test], axis=0)

clf = neighbors.KNeighborsClassifier(n_neighbors=10)
clf.fit(new_x_train.values, new_y_train.values.ravel()) 

KNN_model = 'KNN_model.sav'
pickle.dump(clf, open(KNN_model, 'wb'))

teste_pred_y = clf.predict(x_validation.values)

score_value = acc_score(y_validation.values, teste_pred_y)
print("acc_score : ", score_value)

header = ["KNN: ", "k",  "value", str(10)]
data = []

for i in range(0, len(y_validation)):
    if y_validation.iloc[i].values != teste_pred_y[i]:
        new_data = []
        for j in range(0, len(x_validation.iloc[i].values)):
            if x_validation.iloc[i].values[j] == 0:
                new_data = new_data + ["x"]
            elif x_validation.iloc[i].values[j] == 1:
                new_data = new_data + ["o"]
            else:
                new_data = new_data + ["b"]
        data.append([','.join(new_data), "correct value vs prediction", str(y_validation.iloc[i].values), str(teste_pred_y[i])])
       
f.write(tabulate(data, headers=header, tablefmt='grid'))
f.write("\n\n\n")
data.clear()

