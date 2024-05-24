import pandas as pd
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.metrics import accuracy_score as acc_score
from sklearn.metrics import confusion_matrix as cm
import pickle 


x_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_attributes.csv")
x_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_attributes.csv")
y_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_classes.csv")
y_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_classes.csv")

clf = neighbors.KNeighborsClassifier(n_neighbors=1)
clf.fit(x_train.values, y_train.values.ravel())
pickle.dump(clf, open("KNN", 'wb')) 

"""score = []
for i in range(1, 11):
    clf = neighbors.KNeighborsClassifier(n_neighbors=i)
    clf.fit(x_train.values, y_train.values.ravel())
    pickle.dump(model_clf, open("model_clf_pickle", 'wb')) 

    teste_pred_y = clf.predict(x_test.values)
    
    score_value = acc_score(y_test.values, teste_pred_y)
    score.append(score_value)

    #for i in range(0, len(y_test)):
        #print(X_test.iloc[i],"predicao: ", teste_pred_y[i])
        #if y_test.iloc[i].values != teste_pred_y[i]:
        #    print(y_test.iloc[i].values, "predicao: ", teste_pred_y[i]) 
        #else:
        #    print(y_test.iloc[i].values , "equals", teste_pred_y[i])

plt.xlabel("número de vizinhos")
plt.ylabel("acurácia")
plt.plot(range(1,11),score)
plt.show()"""

# Decision Tree
modelo = DTC(random_state=0
            ,criterion = 'log_loss'  # 'gini', 'entropy', 'log_loss'
            ,min_samples_split=2  # default 2
            ,min_samples_leaf=1   # default 1
            ,max_leaf_nodes=None  # default None
            ,class_weight=None    # default None. 'balanced' para equilibrar classes
            ,ccp_alpha=0.0        # default 0.0 Valores na documentação 0.005 0.01 0.015 0.02 0.025 0.03 0.035
            )


modelo.fit(x_train.values, y_train.values)

pickle.dump(modelo, open("DTC", 'wb'))

"""teste_pred_y = modelo.predict(x_test.values)
for i in range(0, len(y_test)):
    print("x_test values: " , x_test.iloc[i].values)
    if y_test.iloc[i].values != teste_pred_y[i]:
        print(y_test.iloc[i].values, "predicao: ", teste_pred_y[i]) 
    else:
        print(y_test.iloc[i].values , "equals", teste_pred_y[i])

acuracia = acc_score(y_test.values, teste_pred_y)
#acuracia = modelo.score(y_test.values, teste_pred_y)
resultado = cm(y_test.values, teste_pred_y)

#cm_display = CMD(resultado).plot()
print('Alpha=', 0.0,' Acuracia=', acuracia)"""