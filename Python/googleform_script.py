import requests
import random
import time

# Google Form URL (REPLACE WITH YOUR SUBMISSION URL)
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLScB3QkpCiI2wocdlkRpLo_3bTSFhkjD8kEiCoKPW7dhFv1aQA/formResponse'  # Corrected URL

# Headers to mimic a browser request (OPTIONAL)
headers = {
    'Origin': 'https://docs.google.com',
    'Referer': 'https://docs.google.com/forms/d/e/1FAIpQLScB3QkpCiI2wocdlkRpLo_3bTSFhkjD8kEiCoKPW7dhFv1aQA/viewform',
    'Content-Type': 'application/x-www-form-urlencoded',
}

# Define possible answers for each question
# If open ended create a txt,json or array link it accordingly
answers = {
    
    # New questions
    "age_group": ["18-24", "25-34", "35-44", "45-54", "55+"],
    "profession": ["Investor", "Trader", "Student", "Data Scientist", "Other"],
    "stock_market_familiarity": ["Beginner", "Intermediate", "Expert"],
    "ml_tool_usage": ["Yes", "No"],
    "ml_prediction_improvement": ["Yes", "No", "Not sure"],
    "ml_trust": ["1", "2", "3", "4", "5"],
    "ml_accuracy": ["Yes", "No", "Maybe"],
    "ml_advantage": ["Speed", "Accuracy", "Ability to handle large datasets", "Other"],
    "ml_risk": ["Overfitting", "Data quality issues", "Lack of interpretability", "Other"],
    "ml_bot_usage": ["Yes", "No"],
    "ml_bot_effectiveness": ["1", "2", "3", "4", "5"],
    "ml_crash_prediction": ["Yes", "No", "Maybe"],
    "ml_forecast_reliability": ["1", "2", "3", "4", "5"],
    "ml_retail_investor": ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"],
    "ml_regulation": ["Yes", "No", "Not sure"],
    "ml_manipulation_concern": ["Yes", "No"],
    "ml_accessibility": ["Accessible to everyone", "Restricted to professionals"],
    "ml_replace_human": ["Yes", "No", "Maybe"],
    "ml_transparency_importance": ["1", "2", "3", "4", "5"],
    "ml_dominant_force": ["Yes", "No", "Not sure"],
    "ml_trading_percentage": ["Less than 25%", "25-50%", "50-75%", "More than 75%"],
    "ml_investment_willingness": ["Yes", "No", "Maybe"],
    "ml_volatility_impact": ["Increase", "Decrease", "Not Sure"],
    "ml_integration": ["Integrated", "Separate"],
    "ml_biggest_concern": ["Other", " idk", "skip" ,".." ,"."]  # This can be customized based on specific concerns
}


def read_names(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
        
def read_emails(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# def fill_form(name, email):
def fill_form(name):
    data = {
        'entry.1303826610': name
        'entry.136379921': random.choice(answers['age_group']),
        'entry.1033703970': random.choice(answers['profession']),
        'entry.421065018': random.choice(answers['stock_market_familiarity']),
        'entry.795132544': random.choice(answers['ml_tool_usage']),
        'entry.1973458144': random.choice(answers['ml_prediction_improvement']),
        'entry.1482310851': random.choice(answers['ml_trust']),
        'entry.203536161': random.choice(answers['ml_accuracy']),
        'entry.94130541': random.choice(answers['ml_advantage']),
        'entry.672645319': random.choice(answers['ml_risk']),

        'entry.1511261723': random.choice(answers['ml_bot_usage']),
        'entry.902553014': random.choice(answers['ml_bot_effectiveness']),
        'entry.1797295609': random.choice(answers['ml_crash_prediction']),
        'entry.1016762150': random.choice(answers['ml_forecast_reliability']),
        'entry.291175138': random.choice(answers['ml_retail_investor']),
        'entry.694976896': random.choice(answers['ml_regulation']),
        'entry.352232777': random.choice(answers['ml_manipulation_concern']),
        'entry.1910328037': random.choice(answers['ml_accessibility']),
        'entry.1156343802': random.choice(answers['ml_replace_human']),
        'entry.1860764607': random.choice(answers['ml_transparency_importance']),

        'entry.1339017678': random.choice(answers['ml_dominant_force']),
        'entry.717996384': random.choice(answers['ml_trading_percentage']),
        'entry.1771355341': random.choice(answers['ml_investment_willingness']),
        'entry.1000840126': random.choice(answers['ml_volatility_impact']),
        'entry.1756348025': random.choice(answers['ml_integration']),
        'entry.1763827264': random.choice(answers['ml_biggest_concern'])
    
    }
    
    response = requests.post(FORM_URL, data=data, headers=headers)  
    return response.status_code

def main():
    # emails = read_emails('emails.txt')
    names = read_names('name.txt')
    n = int(input("How many times do you want to submit the form? "))
    
    for _ in range(n):
        # for name, email in zip(names, emails):
        for name in names:
            # status = fill_form(name, email)
            status = fill_form(name)
            print(f"Submitted form for {name}, Status Code: {status}")
            time.sleep(1)  
    print("Form submissions completed.")

if __name__ == "__main__":
    main()
