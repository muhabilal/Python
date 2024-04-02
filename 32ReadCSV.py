import pandas as pd
data = pd.read_csv('data.csv')
#print(data['Smoking'].dtype)

# Find null data
null_data = data.isnull().sum()
#print(null_data)

# Find duplicate rows
duplicate_rows = data.duplicated()
#print(duplicate_rows)
print(data['HeartDisease'])
#data['HeartDisease'] = data['HeartDisease'].str.strip().replace({'No': 0, 'Yes':1}) 
replacements = {
    'HeartDisease': {'No': 0, 'Yes': 1},
    'Smoking': {'No': 0, 'Yes': 1},
    'AlcoholDrinking': {'No': 0, 'Yes': 1},
    'Stroke':{'No': 0, 'Yes': 1},
    'DiffWalking':{'No': 0, 'Yes': 1},
    'Sex':{'Female': 0, 'Male': 1},
}
data.replace(replacements, inplace=True)
data['BMI']=data['BMI'].astype(int)
data.to_csv('preprocessed_data.csv', index=False)
