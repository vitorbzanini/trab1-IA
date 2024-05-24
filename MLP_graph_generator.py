import pandas as pd
from sklearn.neural_network import MLPClassifier
import math
from sklearn.metrics import accuracy_score as acc_score
import matplotlib.pyplot as plt

x_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_attributes.csv")
x_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_attributes.csv")
y_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_classes.csv")
y_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_classes.csv")

size_of_entry = len(x_train.columns)
size_of_output = 4

guess_hidden_layer = math.ceil(math.sqrt(size_of_entry * size_of_output))

score = []
plt_hidden_layer = []

for i in range(2, 22, 2):
    clf = MLPClassifier(max_iter=3000,activation='tanh',solver='adam', hidden_layer_sizes=(guess_hidden_layer*i,), learning_rate_init=0.0005, momentum=0.2, verbose=False)
    clf.fit(x_train.values, y_train.values.ravel()) 

    teste_pred_y = clf.predict(x_test.values)
    
    score_value = acc_score(y_test.values, teste_pred_y)
    score.append(score_value)
    plt_hidden_layer.append(guess_hidden_layer*i)

plt.xlabel("Guess hidden layer:")
plt.ylabel("acurácia")
plt.plot(plt_hidden_layer,score)
plt.savefig('MLP_guess_hidden_layer.png', dpi=300, bbox_inches='tight')
plt.show()