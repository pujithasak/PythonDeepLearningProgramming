import pandas as pd

train_df = pd.read_csv('./train.csv')

# Finding correlation between survived and sex column
train_df['Sex'] = train_df['Sex'].map({'female': 1, 'male': 0}).astype(int)
print(train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))

