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

from datetime import datetime

import csv

import form

# Score starts as zero
score = 0

# Function to update the score given the points of each answer
def update_score(score, radio_selected, high_points_answer, high_points_value, low_points_answer, low_points_value):
    if radio_selected == high_points_answer:
        score += int(high_points_value)
    elif radio_selected == low_points_answer:
        score += int(low_points_value)
    else:
        score += 0
        
    return score

def get_perfil(score):
    for profile in form.profiles:
        if  profile["min_score"] <= score <= profile["max_score"]:
            perfil = profile["profile"]    
    return perfil
    


# ------------ INTERFACE ---------------------------
# Title and subtitle
st.title(form.TITLE)
st.markdown(form.SUBTITLE)

# Form that is immutable before send
with st.form("form_dsop"):
    
    # Description inside the form
    st.markdown(form.DESCRIPTION)    
    
    # Questions and answers as radio buttons
    for i in range(form.N_QUESTIONS):
        
        # Horizontal line as a separator
        st.write("---")
        
        # Radio selection for the answers of each question
        # First arg is the question (but prints small)
        # Second arg is a tuple of options for answers
        radio_selected = st.radio(form.answers[i]["question"], 
                                  (form.answers[i][10], 
                                   form.answers[i][5], 
                                   form.answers[i][0]))
        
        # Update the score 
        # First arg is the actual score
        # Second arg is the option selected
        # Third argument is the high score answer
        # Fourth arg is the value of the high score answer
        # Fifth arg is the low score answer
        # Sixth arg is the value of the low score answer
        score = update_score(score,
                             radio_selected, 
                             form.answers[i][10],
                             list(form.answers[i].keys())[1],
                             form.answers[i][5],
                             list(form.answers[i].keys())[2])
    
    
    st.write("---")
    
    idade = st.number_input("Idade", step=1, min_value=14, max_value=99)

    
    st.write("---")
    
    escolaridade = st.radio("Último Nível de Escolaridade Completo",
                            ("Sem instrução",
                             "Ensino Fundamental",
                             "Ensino Médio",
                             "Ensino Superior"))

    
    st.write("---")
    
    renda = st.radio("Renda Pessoal Mensal (aproximadamente)",
                     ("Sem Rendimentos",
                      "Até 1 salário mínimo",
                      "Até 2 salários mínimos",
                      "Até 5 salários mínimos",
                      "Até 10 salários mínimos",
                      "Até 20 salários mínimos",
                      "Mais de 20 salários mínimos"))
    
    perfil = get_perfil(score)
    
    # Button for the form submit
    dsop_submitted = st.form_submit_button("Enviar")

# After the form is submitted
if dsop_submitted:
  
 
    # Dictionary to create a new record
    new_record = {"timestamp": datetime.now(), 
                  "perfil" : perfil,
                  "score" : score,
                  "escolaridade" : escolaridade,
                  "idade" : idade,
                  "renda" : renda}
    
    # Header of the csv file
    header = list(new_record.keys())
    
    # Open the csv file with timestamp and score
    with open("scores.csv", "a", newline="", encoding="UTF-8") as records:
        
        # 
        writer = csv.DictWriter(records, fieldnames=header)
        
        # Append a new row to the csv file    
        writer.writerow(new_record)
    
  
    
    # Title of the score given to the user
    st.title("Seu perfil é:")
    
    # Select the text and what to show to user given a score
    for profile in form.profiles:
        if  profile["min_score"] <= score <= profile["max_score"]:
            if profile["color"] == "green":
                st.success(profile["profile"])
            if profile["color"] == "blue":
                st.info(profile["profile"])
            if profile["color"] == "yellow":
                st.warning(profile["profile"])
            if profile["color"] == "red":
                st.error(profile["profile"])
            
            st.write(profile["text"])

# Button for the user to download the spreadsheet    
with open("planilha-mensal.xlsx", "rb") as file:
    download_spreadsheet = st.download_button(
        label="Baixar Planilha de Orçamento Mensal",
        data=file,
        file_name="dsop-orcamento-mensal.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# Button for the user to download the article
with open("artigo-dsop.pdf", "rb") as file:
    download_pdf = st.download_button(
        label="Artigo sobre a Metodologia DSOP",
        data=file,
        file_name="artigo-dsop.pdf",
        mime="application/pdf"
        )
    
with open("scores.csv", "rb") as file:
    download_csv = st.download_button(
        label="Baixar csv",
        data=file,
        file_name="scores.csv",
        mime="text/csv"
    )

df = pd.read_csv("scores.csv")

st.write(df)