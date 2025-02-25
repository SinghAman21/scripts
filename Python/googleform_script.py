import requests
import random
import time

# Google Form URL (REPLACE WITH YOUR SUBMISSION URL)
FORM_URL = 'https://docs.google.com/forms/d/e/UNIQUE_FORM_ID/formResponse'  # Corrected URL

# Headers to mimic a browser request (OPTIONAL)
headers = {
    'Origin': 'https://docs.google.com',
    'Referer': 'https://docs.google.com/forms/d/e/UNIQUE_FORM_ID/viewform',
    'Content-Type': 'application/x-www-form-urlencoded',
}

# Define possible answers for each question
# If open ended create a txt,json or array link it accordingly
answers = {
    "trend": ["De globalisation", "Decarbonisation", "Demographics", "Digitalization"],
    "familiarity": ["Very familiar", "Somewhat familiar", "Not very familiar", "Not at all familiar"],
    "sustainable_investing": ["Yes", "No", "Uncertain"],
    "ai_importance": ["Very important", "Somewhat important", "Not very important", "Not at all important"],
    "crypto_investment": ["Yes", "No"],
    "information_source": ["Social media", "News articles", "Financial advisor", "Online forums"],
    "cyber_security_concern": ["Very concerned", "Somewhat concerned", "Not very concerned", "Not at all concerned"],
    "future_trend": ["Fintech innovations", "Sustainable investing", "Cryptocurrencies", "Artificial intelligence in finance"]
}

def read_names(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
        
def read_emails(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def fill_form(name, email):
    data = {
        'entry.723878051': email,  
        'entry.723878051': name,  #
        'entry.162341043': random.choice(answers['trend']), 
        'entry.2064448238': random.choice(answers['familiarity']),
        'entry.1127301049': random.choice(answers['sustainable_investing']),  
        'entry.610390207': random.choice(answers['ai_importance']),  
        'entry.253333483': random.choice(answers['crypto_investment']),  
        'entry.849586231': random.choice(answers['information_source']),  
        'entry.1223972859': random.choice(answers['cyber_security_concern']),  
        'entry.1584534532': random.choice(answers['future_trend'])  
    }
    
    response = requests.post(FORM_URL, data=data, headers=headers)  
    return response.status_code

def main():
    emails = read_emails('emails.txt')
    names = read_names('names.txt')
    n = int(input("How many times do you want to submit the form? "))
    
    for _ in range(n):
        for name, email in zip(names, emails):
            status = fill_form(name, email)
            print(f"Submitted form for {name}, Status Code: {status}")
            time.sleep(1)  
    print("Form submissions completed.")

if __name__ == "__main__":
    main()
