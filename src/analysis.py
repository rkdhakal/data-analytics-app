import pandas as pd

def run_analysis():
    # Load the dataset
    data = pd.read_csv('data/sample.csv')
    
    # Clean the column names
    data.columns = data.columns.str.replace('"', '').str.strip()

    # Calculate average height and weight by gender
    avg_height_male = data.loc[data['Sex'] == 'M', "Height (in)"].mean()
    avg_height_female = data.loc[data['Sex'] == 'F', "Height (in)"].mean()
    avg_weight_male = data.loc[data['Sex'] == 'M', "Weight (lbs)"].mean()
    avg_weight_female = data.loc[data['Sex'] == 'F', "Weight (lbs)"].mean()
    
    return {
        "avg_height_male": avg_height_male,
        "avg_height_female": avg_height_female,
        "avg_weight_male": avg_weight_male,
        "avg_weight_female": avg_weight_female
        }