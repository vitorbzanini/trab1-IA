import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit


df = pd.read_csv(r"/home/vitor/IA/T1/new_tic-tac-toe_n.csv")
df_class = df["state"]
del df["state"]

size_test_validation = 0.3 # 30% of the dataset goes to test and validation

stratSplit = StratifiedShuffleSplit(n_splits=1, test_size=size_test_validation, random_state=0)

for train_index, test_valid_index in stratSplit.split(df, df_class):
    
    x_train, x_test_validation = df.iloc[train_index], df.iloc[test_valid_index]
    y_train, y_test_validation = df_class.iloc[train_index], df_class.iloc[test_valid_index]

size_test_validation = 0.5 #The half of 30% of the dataset goes to test and the other half goes to validation

stratSplit2 = StratifiedShuffleSplit(n_splits=1, test_size=size_test_validation, random_state=0)

for test_index, validation_index in stratSplit2.split(x_test_validation, y_test_validation):
    
    x_test, x_validation = x_test_validation.iloc[test_index], x_test_validation.iloc[validation_index]
    y_test, y_validation = y_test_validation.iloc[test_index], y_test_validation.iloc[validation_index]

x_train.to_csv("Train_dataset_attributes.csv", index=False)
x_test.to_csv("Test_dataset_attributes.csv", index=False)
y_train.to_csv("Train_dataset_classes.csv", index=False)
y_test.to_csv("Test_dataset_classes.csv", index=False)
x_validation.to_csv("Validation_dataset_attributes.csv", index=False)
y_validation.to_csv("Validation_dataset_classes.csv", index=False)