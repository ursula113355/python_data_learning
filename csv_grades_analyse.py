import pandas as pd
file_path = r'D:\ruixi\Aria\rw\职业规划\python练习\python_data_learning\student_scores.csv'
df = pd.read_csv(file_path)
stats = df.describe().loc[['mean', 'max', 'min']]
print(stats)