import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score as acc_score

x_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_attributes.csv")
x_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_attributes.csv")
x_validation = pd.read_csv(r"/home/vitor/IA/T1/Validation_dataset_attributes.csv")
y_train = pd.read_csv(r"/home/vitor/IA/T1/Train_dataset_classes.csv")
y_test = pd.read_csv(r"/home/vitor/IA/T1/Test_dataset_classes.csv")
y_validation = pd.read_csv(r"/home/vitor/IA/T1/Validation_dataset_classes.csv")

score = []
header = []
data = []
begin_knn = 1
end_knn = 35

criterion = ['gini', 'entropy', 'log_loss']

for i in criterion:
    clf = DTC(random_state=0
            ,criterion = i        # 'gini', 'entropy', 'log_loss'
            ,min_samples_split=2  # default 2
            ,min_samples_leaf=1   # default 1
            ,max_leaf_nodes=None  # default None
            ,class_weight=None    # default None. 'balanced' para equilibrar classes
            ,ccp_alpha=0.0        # default 0.0 Valores na documentação 0.005 0.01 0.015 0.02 0.025 0.03 0.035
            )
    clf.fit(x_train.values, y_train.values.ravel()) 

    teste_pred_y = clf.predict(x_test.values)
    
    score_value = acc_score(y_test.values, teste_pred_y)
    score.append(score_value)

plt.xlabel("criterion: ")
plt.ylabel("acurácia")
plt.plot(criterion,score)
plt.savefig('criterion.png', dpi=300, bbox_inches='tight')
plt.show()

#two better criterions: entropy and log_loss
score.clear()
ccp_alpha_values = [0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035]

for i in ccp_alpha_values:
    clf = DTC(random_state=0
            ,criterion = 'log_loss'  # 'gini', 'entropy', 'log_loss'
            ,min_samples_split=2     # default 2
            ,min_samples_leaf=1      # default 1
            ,max_leaf_nodes=None     # default None
            ,class_weight=None       # default None. 'balanced' para equilibrar classes
            ,ccp_alpha=i             # default 0.0 Valores na documentação 0.005 0.01 0.015 0.02 0.025 0.03 0.035
            )
    clf.fit(x_train.values, y_train.values.ravel()) 

    teste_pred_y = clf.predict(x_test.values)
    
    score_value = acc_score(y_test.values, teste_pred_y)
    score.append(score_value)

plt.xlabel("log_loss -> ccp_alpha: ")
plt.ylabel("acurácia")
plt.plot(ccp_alpha_values,score)
plt.savefig('log_loss-ccp_alpha.png', dpi=300, bbox_inches='tight')
plt.show()

score.clear()
ccp_alpha_values = [0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035]

for i in ccp_alpha_values:
    clf = DTC(random_state=0
            ,criterion = 'entropy'  # 'gini', 'entropy', 'log_loss'
            ,min_samples_split=2    # default 2
            ,min_samples_leaf=1     # default 1
            ,max_leaf_nodes=None    # default None
            ,class_weight=None      # default None. 'balanced' para equilibrar classes
            ,ccp_alpha=i            # default 0.0 Valores na documentação 0.005 0.01 0.015 0.02 0.025 0.03 0.035
            )
    clf.fit(x_train.values, y_train.values.ravel()) 

    teste_pred_y = clf.predict(x_test.values)
    
    score_value = acc_score(y_test.values, teste_pred_y)
    score.append(score_value)

plt.xlabel("entropy -> ccp_alpha: ")
plt.ylabel("acurácia")
plt.plot(ccp_alpha_values,score)
plt.savefig('entropy-ccp_alpha.png', dpi=300, bbox_inches='tight')
plt.show()



