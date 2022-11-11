# --------- FINANCIAL BEHAVIOR APP ----------------

# -------------- ROAD MAP ----------------
# - Form with the questions and the answers to that question
# - The from computes the score of the answers
# - Shows to user the output related to that score
# - Does not show the score
# - Questions and answers are in a list of dictionaries
# - The score update is hardcoded in a way that will not be updated
# - Now I can record the the answers into a CSV file



# -------------- IMPROVEMENTS ------------
# - Get the number of questions from the database or csv
# - TITLE, SUBTITLE, DESCRIPTION outside of the code
# - Put the basic info outside this code and import it from outside
# - Texts from the a db or csv
# - Put the questions and answers into a database
# - Break the questions and the answers into different data
# - Write a new score_update function in a more flexible way




# Framework that creates the app
import streamlit as st

import pandas as pd

import project


# ------------ FILES ---------------------------

csv_file = r"./records/scores.csv"
planilha = r"./download/planilha-mensal.xlsx"
artigo = r"./download/artigo-dsop.pdf"
form_file = r"form.json"

# Get the dict with the form info
form_dict = project.get_form_dict(form_file)

# Score starts as zero
score = 0


# ------------ INTERFACE ---------------------------
# Title and subtitle
st.title(form_dict['title'])
st.write(form_dict['subtitle'])

# Form that is immutable before send
with st.form("form_dsop"):
 
    # Description inside the form
    st.markdown(form_dict['description'])    
    
    # Questions and answers as radio buttons
    for row in range(len(form_dict['options'])):
        
        # Get the question and the answers of this row        
        question = project.get_question(form_dict, row)              
        answers_tuple = project.get_options(form_dict, row)
        
        # Line, Question and Options
        st.write("---")
        st.subheader(question) 
        option_selected = st.radio('Select option', answers_tuple, label_visibility='hidden')
        
        # Update score after selecting the option
        score = project.update_score(score, form_dict, row, option_selected)
    
    # Get the user profile given a score
    perfil = project.get_profile(score, form_dict)
        
    # Line, Question about age, Input number to age    
    st.write("---")
    st.subheader(form_dict['age']['question'])
    idade = st.number_input("Digite sua idade", step=1, min_value=14, max_value=99, label_visibility='hidden')

    # Line, Question about instruction level and options
    st.write("---")
    st.subheader(form_dict['instruction_level']['question'])
    escolaridade = st.radio("Selecione uma opção", tuple(form_dict['instruction_level']['answers']), label_visibility='hidden')

    # Line, Question about monthly wage and options
    st.write("---")
    st.subheader(form_dict['monthly_wage']['question'])
    renda = st.radio("Selecione uma opção", tuple(form_dict['monthly_wage']['answers']), label_visibility='hidden')
      
    # Button for the form submit
    dsop_submitted = st.form_submit_button("Enviar")

# After the form is submitted
if dsop_submitted:

    # Add a new record to the csv
    record_added = project.make_new_record(perfil, score, escolaridade, idade, renda, csv_file)
   
    # Title of the score given to the user
    st.title("Seu perfil é:")
        
    # Select the text and what to show to user given a score
    for profile in form_dict['profiles']:
        if  profile["profile"] == perfil:
            if profile["color"] == "green":
                st.success(profile["profile"])
            if profile["color"] == "blue":
                st.info(profile["profile"])
            if profile["color"] == "yellow":
                st.warning(profile["profile"])
            if profile["color"] == "red":
                st.error(profile["profile"])
            
            # Show the text of that given profile
            st.write(profile["text"])

# Button for the user to download the spreadsheet    
with open(planilha, "rb") as file:
    download_spreadsheet = st.download_button(
        label="Baixar Planilha de Orçamento Mensal",
        data=file,
        file_name="dsop-orcamento-mensal.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# Button for the user to download the article
with open(artigo, "rb") as file:
    download_pdf = st.download_button(
        label="Artigo sobre a Metodologia DSOP",
        data=file,
        file_name="artigo-dsop.pdf",
        mime="application/pdf"
        )

for i in range(200):
    st.write("")

df = pd.read_csv(csv_file)

csv_data = df.to_csv(index=False).encode('utf-8')

st.download_button(
   "Baixar csv",
   csv_data,
   "scores.csv",
   "text/csv",
   key='download-csv'
)


st.dataframe(df)
