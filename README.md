# Financial Behavior Test
#### Video Demo: https://youtu.be/evaZgeVd_zw
#### Description: 



## CS50 Python - Final Project
## Introduction

Hi, my name is Felipe Pereira Heitmann, and I'm a Calculus teacher at Anhanguera College in Belo Horizonte, Minas Gerais, Brazil. I took the CS50’s Introduction to Programming with Python right after completed CS50’s Introduction to Computer Science last month. 

When I was heading to the last week on the CS50 Python, a fellow teacher here at the Anhanguera College asked for my help in a project about the Financial Behavior of our students. I merged this demand with the final project for this course. 

The main struggle of the project was that the form given to the students to fill was based on a methodology that required to assign a number of points to each answer of a given question and not simply check if the answer was right or wrong. Because of this issue we could not use a simple form generator like a Google Forms or Microsoft Forms to collect the students' data.

So I decided to build an interactive form from ground up using Python as my Final Project.

## Project Design

We needed a form that was able to record the user's selection among options in multiple choice questions and assign to each answer a value and present a final score of using these values.

- User Interface:
    - User read a question.
    - User read the options for a given question.
    - User selects an option as their answer.
    - User repeats it to 10 questions.
    - User informs age, instruction level and monthly wage.
    - User submit the form.
    - User receive a message with a profile.
    - User can download a financial spreadsheet to use.
    - User can download a financial behavior article to read.

- Data Processing:
    - The questions, answers and profiles are loaded from a .json file into a dictionary.
    - A form is created to hold the questions and answers.
    - Inside this form the questions and answers are loaded from the dictionary.
    - The score of the answers is computed after every user option choice.
    - The user profile is set given the final score.
    - The user identification data (age, instruction level and monthly wage) is inputted.
    - The form button sets an end to the inputs.
    - A dictionary with profile, score, instruction level and monthly wage is created.
    - This dictionary is saved into a .csv file
    - This file is read into a data frame.


## Tools and Methods

To implement this project I used many tools, these are some of them:

- Streamlit Cloud
    - Used to host the app [https://perfil-financeiro-22.streamlit.app/](https://perfil-financeiro-22.streamlit.app/)
- Streamlit
    - Framework to generate React web apps using Python
        - `st.title()` to create the page title.
        - `st.form()` to create the form itself
        - `st.subheader()` to create the questions.
        - `st.radio()` to present the options for the answers.
        - `st.number_input()` to input the number of the user's age.
        - `st.form_submit_button` to submit the form
        - `st.write()` to write the description texts.
        - `st.download_button` to create the buttons to download the files.
        - `st.dataframe()` to show the data frame.
- Datetime package
    - Used to get the timestamp of the users form submission.
        - `datime.now()` to get the timestamp.
- csv package
    - Used to create a .csv file with the users answers to the form and save it.
        - `csv.DictWriter()` to write a dictionary into a .csv file.
        - `.writerow()` to insert the row into the .csv file.
- json package
    - Use to read a .json file into a dictionary with the questions and options of the form.
        - `json.load()` to load the .json file into a dictionary
- pandas package
    - Used to read the .csv into a data frame for posterior analysis.
        - `pd.read_csv` to read the csv into dataframe.

## Timeline

1. 2022/11/04 - First Version:
    1. Created the repository at GitHub.
    2. Created an empty StreamLit project.
    3. All the questions and answers as standalone variables.
    4. All the calculations and searches in the main function.
    5. Hardcoded scores and profiles for the user.
    6. No data saving, only user's response given.
2. 2022/11/06 - Second Version:
    1. Users data saved into a .csv after each submission.
    2. Pandas data frame to show the data.
    3. Getting user identification into the .csv file.
3. 2022/11/09 - Third Version:
    1. Putting the questions and options in a .json file.
    2. Making the form get the info from the .json file.
4. 2022/11/10 - Fourth Version:
    1. Isolating the backend and frontend
    2. `project.py` as backend with all the functions.
    3. `app.py` as frontend with all the interface.
    4. Creating and running the tests.
    5. Writing the documentation.

## Improvements for the next version
- Save the user's answers to the form outside of the StreamLit Cloud.
- Use an external database to save the user's answers.
- Create an automatic descriptive statistical analysis of the user's answers.
- 

## What I learned from this project
- Refactor my code until it gets suited to a given demand.
- Read and write JSON files to save dictionaries in a persistent way.
- Navigating nested dictionaries and lists to get some info.
- Segmentation of frontend and backend in a streamlit project.
- Saving user's data in a CSV file for posterior analysis.
- Making download buttons in streamlit to download user's data and other files.
- Using pandas to read csv and present it in data frames.

## Presentation Script

### CS50 Python: Final Project
### Financial Behavior Test
### Felipe Pereira Heitmann
### felipeph@gmail.com

Hi, I’m Felipe Heitmann from Belo Horizonte, Brazil and this is CS50 Python.

### Google Forms
When planning a survey the first platform we think about is Google Forms or something like that. 

### Not simply right or wrong?
But what if your survey needs to assign different values to each of user's answers and not only check if they are right or wrong?

### CS50's: Introduction to Programming with Python
This is why I created this final project for CS50’s Introduction to Programming with Python.

### Financial Behavior Test
The Financial Behavior Test has 10 different questions with 3 answers each.

### 10 points to the first option
When the user selects the first option it adds 10 points to the final score.

### 5 points to the second option
The second option adds 5 points to the final score.

### 0 points to the third option
And the third option adds 0 points to the final score.

### 10 questions
With all the answers from the user, the app computes a final score and assign a Financial Behavior Profile to the user.

### Score greater than or equal to 80
If the score is above 80, the profile is "Investor"

### Score between 50 and 75 
If the score is between 50 and 75, the profile is "Financially Balanced"

### Score between 20 and 45
If the score is between 20 and 45, the profile is "Indebted"

### Score below 15
And if it is below 15, the profile is "Over-indebted"
For each profile there is text with a commentary and orientation for the user in that profile.

### Downloads
After that the user is presented with a Financial Spreadsheet and an article about the methodology used in this survey.

### Technical Review
### StreamLit
The Financial Behavior Test is hosted at StreamLit Cloud and was created using StreamLit library for the user interface. 

### JSON 
The questions, answers and texts are loaded from a JSON file using the json library. 

### Python elements
The logic of computing the score and getting the user profile was created in python using lists, dictionaries and tuples, "for" loops and if conditional statements. 

### CSV
The user's score, profile, instruction level, age and monthly wage are recorded into a CSV file.