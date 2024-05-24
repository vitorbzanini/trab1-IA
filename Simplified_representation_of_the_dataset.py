import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_attributes.csv")
x_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_attributes.csv")
x_validation = pd.read_csv(r"/home/vitor/IA/T1/Validation_dataset_attributes.csv")
y_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_classes.csv")
y_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_classes.csv")
y_validation = pd.read_csv(r"/home/vitor/IA/T1/Validation_dataset_classes.csv")

x_plot = x_train.replace(-1, 2)
value_for_normalization = len(x_train.columns) * x_plot['c1'].max() 


"""sum_values_dataset = []
for i in range(0, len(x_plot)):
    media = sum(abs(x_plot.iloc[i].values))/(value_for_normalization) + y_train.values.ravel()[i]  
    sum_values_dataset.append(media)
    print(media)
    a = input('').split(" ")[0]
    print(a)"""

column_0, column_1, column_2, column_3 = [], [], [], []

for i in range(0, len(x_train)):
    linear_sum=0
    #print(x_plot.iloc[i].values.ravel()[i])
    for j in range(1, 10):
        linear_sum += x_plot.iloc[i].values.ravel()[j-1] * j
        """print(x_plot.iloc[i].values.ravel()[j-1])
        a = input('').split(" ")[0]
        print(a)"""    
    
    media = linear_sum #* (y_train.values.ravel()[i]) 
    """print(linear_sum)
    print(media)
    a = input('').split(" ")[0]
    print(a)"""

    if y_train.values.ravel()[i] == 0:
        column_0.append(media)
    elif y_train.values.ravel()[i] == 1:
        column_1.append(media)
    elif y_train.values.ravel()[i] == 2:
        column_2.append(media)
    else:  
        column_3.append(media)

plt.plot(column_0, 'ko', label="X Venceu")
plt.plot(column_1, 'ro', label="O venceu")
plt.plot(column_2, 'go', label="Tem jogo")
plt.plot(column_3, 'bo', label="Empate")

print(len(column_0))
print(len(column_1))
print(len(column_2))
print(len(column_3))

plt.yticks(np.arange(0, 100, step=2))
plt.xticks(np.arange(0, 8000, step=100))
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Faces Features")
plt.legend()
plt.show()

# Eixo x corresponde a todos os objetos do dataset (que são visualizados 0-8000)
# Eixo y corresponde a soma linear dos valores de cada objeto do dataset

"""y_train_norm = y_train/y_train.max() # Normalize the data to plot using max value of the column 
x_plot = x_train.replace(-1, 2) # Replace -1 by 2 to implement the normalization for visualize
                                # some simplification of the data in the plot
                                # and find the relation of the errors in the prediction 

value_for_normalization = len(x_train.columns) * x_plot['c1'].max() 
                              # 18 (9 n_attributes * 2 max_value_column) is the maximum sum of values in a row because 
                              # the values are 0(x), 1(o) or 2(b) and the maximum of sum
                              # will be 'b' in all columns

print(y_train.max())

sum_values_dataset = []
for i in range(0, len(x_plot)):
    media = sum(abs(x_plot.iloc[i].values))/(value_for_normalization) + y_train.values.ravel()[i]  
    sum_values_dataset.append(media)
    print(media)
    a = input('').split(" ")[0]
    print(a)

plt.xticks(np.arange(0, 5, step=0.2))
plt.yticks(np.arange(0, 1, step=0.2))
plt.scatter(sum_values_dataset, y_train_norm.values.ravel())
plt.show()"""