from datetime import datetime

import csv

import json


def main():
    print(get_form_dict('form.json'))

# Load the JSON file with the form data into a dict
# Arg is the filepath of the json file
def get_form_dict(filepath):
    
    # With open works to open and close the file when needed
    # The 'r' mode is read-only
    # encoding='utf8' make possible the use of portuguese char
    with open(filepath, 'r', encoding='utf8') as file:
        
        # json.load loads the file
        form_dict = json.load(file)
        
        # Return the dictionary from the json file
        return form_dict
    

# Update the score given the actual score, the options and selection
# This function is made to work inside a loop through a list of dicts
def update_score(score, form_dict, row, option_selected):
    
    # Find the answer selected by the user and add it's score to the total
    # Loop through the items in the list of answer and value for a given row
    for answer_and_value in form_dict['options'][row]['answers']:
        
        # Get the answer text inside each option
        answer_text = answer_and_value['text']
        
        # If this is the option selected by the user
        if option_selected == answer_text:
            
            # Give this answer value to a new variable
            answer_value = answer_and_value['value']
    
    # Add the value of the answer to the total score
    score += answer_value
    
    # Return the updated score
    return score


# For a given row of questions and answers
# Get the list of answers in a form of a tuple to pass to st.radio
# Args are the form dict itself and the position of the row
def get_options(form_dict, row):
    
    # Start with an empty list
    answers_list = []
    
    # Loop through the answer_value dictionaries
    # In every answer found, append to the answers list
    for answer_and_value in form_dict['options'][row]['answers']:
        
        # New variable to hold the answer text of each round
        answer_text = answer_and_value['text']
        
        # Append the answer of this round to the list
        answers_list.append(answer_text)
    
    # Make a tuple for the st.radio element
    answers_tuple = tuple(answers_list)

    # Return this tuple
    return answers_tuple


# Get the profile given a score
def get_profile(score, form_dict):
    
    # Loop through the profiles in the dict
    for profile in form_dict['profiles']:
        
        # When find a profile that my score is between it's limits
        if profile["min_score"] <= score <= profile["max_score"]:
            
            # This is the found profile
            profile_found = profile["profile"]
            
    # Return the value to the function
    return profile_found


# Create the dict to put in the csv
# Needs all the info in the form and the destination filepath
def make_new_record(perfil, score, escolaridade, idade, renda, filepath):
    
    # Make a dict from the data in the form
    new_record = dict_for_record_data(perfil, score, escolaridade, idade, renda)
    
    # Add the dict as a row into a csv
    record_added = add_record_to_csv(new_record, filepath)
    
    # Return the status of the operation
    return record_added
    

# First step is to create a dict from the data in the form
def dict_for_record_data(perfil, score, escolaridade, idade, renda):
    
    # New dict using timestamp
    new_record = {"timestamp": datetime.now(), 
                  "perfil" : perfil,
                  "score" : score,
                  "escolaridade" : escolaridade,
                  "idade" : idade,
                  "renda" : renda}
    
    # Return this new dict
    return new_record


# Add the record to csv
def add_record_to_csv(new_record, filepath):
    # Header of the csv file
    header = list(new_record.keys())
    
    # Try because I want to catch exceptions
    try:
    
        # Open the csv file with timestamp and score
        with open(filepath, "a", newline="", encoding="UTF-8") as records:
            
            # Writer object to the dictionary writing
            writer = csv.DictWriter(records, fieldnames=header)
            
            # Append a new row to the csv file    
            writer.writerow(new_record)
            
            # Status if it went well
            return True
    
    # Error if the file is not accessible 
    except FileNotFoundError:    
        
        # Return false status
        return False
    
def get_question(form_dict, row):
    
    # Go to the json and find the question of a given row
    question = form_dict['options'][row]['question']
    
    # Return this question
    return question
    

if __name__ == "__main__":
    main()