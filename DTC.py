import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score as acc_score
import pickle 
from tabulate import tabulate
from sklearn import tree 

x_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_attributes.csv")
x_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_attributes.csv")
x_validation = pd.read_csv(r"/home/vitor/IA/T1/Validation_dataset_attributes.csv")
y_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_classes.csv")
y_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_classes.csv")
y_validation = pd.read_csv(r"/home/vitor/IA/T1/Validation_dataset_classes.csv")

data = []

#entropy == log_loss

f = open("DTC_data.txt", "w")

new_x_train = pd.concat([x_train, x_test], axis=0)
new_y_train = pd.concat([y_train, y_test], axis=0)

clf = DTC(random_state=0
        ,criterion = 'entropy'  # 'gini', 'entropy', 'log_loss'
        ,min_samples_split=2    # default 2
        ,min_samples_leaf=1     # default 1
        ,max_leaf_nodes=None    # default None
        ,class_weight=None      # default None. 'balanced' para equilibrar classes
        ,ccp_alpha=0.0          # default 0.0 Valores na documentação 0.005 0.01 0.015 0.02 0.025 0.03 0.035
        )

clf.fit(new_x_train.values, new_y_train.values.ravel()) 

DTC_model = 'DTC_model.sav'
pickle.dump(clf, open(DTC_model, 'wb'))

teste_pred_y = clf.predict(x_validation.values)

score_value = acc_score(y_validation.values, teste_pred_y)
print("acc_score : ", score_value)

header = ["DTC: ", "entropy",  "ccp_alpha", "0.0"]

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

file_tree = open("tree2.dot", "w")

dot_data = tree.export_graphviz(clf, out_file=None, feature_names = ["c1","c2","c3","c4","c5","c6","c7","c8","c9"],
                                class_names = ["0","1","2","3"], filled=True, rounded=True, special_characters=True)

file_tree.write(dot_data)

#dot -Tx11 tree.dot > output.x11
