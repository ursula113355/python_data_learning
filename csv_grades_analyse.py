import pandas as pd
file_path = 'student_scores.csv'
df = pd.read_csv(file_path)
stats = df.describe().loc[['mean','max','min']]
print(stats)

