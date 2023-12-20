import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
import joblib

# Membaca data dari file CSV
df = pd.read_csv('../data/customer_churn_train_preprocessed.csv')

# Menyiapkan data fitur dan target
Y = df['churn']
X = df.drop(['churn'], axis=1)

# Memisahkan data menjadi data latih dan data uji
test_size = 0.2
seed = 123
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)

# Membuat dan melatih model RandomForestClassifier
RForest = RandomForestClassifier()
RForest.fit(X_train, Y_train)

# Menyimpan model RandomForestClassifier() ke dalam file dengan ekstensi .joblib
joblib.dump(RForest, 'random_forest_model.joblib')
