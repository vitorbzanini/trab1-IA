import pandas as pd
from sklearn import neighbors
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score as acc_score

x_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_attributes.csv")
x_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_attributes.csv")
x_validation = pd.read_csv(r"/home/vitor/IA/T1/Validation_dataset_attributes.csv")
y_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_classes.csv")
y_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_classes.csv")
y_validation = pd.read_csv(r"/home/vitor/IA/T1/Validation_dataset_classes.csv")

score = []
begin_knn = 1
end_knn = 35

for i in range(begin_knn,end_knn):
    clf = neighbors.KNeighborsClassifier(n_neighbors=i)
    clf.fit(x_train.values, y_train.values.ravel()) 

    teste_pred_y = clf.predict(x_test.values)
    
    score_value = acc_score(y_test.values, teste_pred_y)
    score.append(score_value)

plt.xlabel("número de vizinhos")
plt.ylabel("acurácia")
plt.plot(range(begin_knn, end_knn),score)
plt.savefig('k_neighbors.png', dpi=300, bbox_inches='tight')
plt.show()