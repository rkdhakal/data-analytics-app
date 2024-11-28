import pandas as pd

def run_analysis():
    # Load data
    data = pd.read_csv('data/sample.csv')

    # Handle missing or invalid values (e.g., fill with 0 or drop them)
    data.fillna(0, inplace=True)

    # Perform analysis (e.g., calculate mean)
    avg_height_male = data[data['gender'] == 'male']['height'].mean()
    avg_height_female = data[data['gender'] == 'female']['height'].mean()
    avg_weight_male = data[data['gender'] == 'male']['weight'].mean()
    avg_weight_female = data[data['gender'] == 'female']['weight'].mean()

    # Ensure no NaN is returned
    return {
        "avg_height_male": avg_height_male if not pd.isna(avg_height_male) else 0,
        "avg_height_female": avg_height_female if not pd.isna(avg_height_female) else 0,
        "avg_weight_male": avg_weight_male if not pd.isna(avg_weight_male) else 0,
        "avg_weight_female": avg_weight_female if not pd.isna(avg_weight_female) else 0,
    }

