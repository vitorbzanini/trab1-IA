import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score as acc_score
from sklearn.metrics import confusion_matrix as cm
from sklearn.linear_model import Perceptron
from sklearn.datasets import load_digits

# Dados de entrada


x_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_attributes.csv")
x_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_attributes.csv")
y_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_classes.csv")
y_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_classes.csv")

#train = pd.concat([x_train, y_train], axis=1)
#print(train)
#test  = pd.concat([x_test, y_test], axis=1)
#print(test)

clf = Perceptron(tol=1e-3, random_state=1, max_iter=5000).fit(x_train.values, y_train.values.ravel())

teste_pred_y = clf.predict(x_test.values)

acuracia = acc_score(y_test.values, teste_pred_y)
#acuracia = modelo.score(y_test.values, teste_pred_y)
resultado = cm(y_test.values, teste_pred_y)

#cm_display = CMD(resultado).plot()
print('Alpha=', 0.0,' Acuracia=', acuracia)
