# -------------- ROAD MAP -------------
# - Form with the questions and the answers to that question
# - 



# Framework that creates the app
import streamlit as st

# ----------------- PARAMETERS --------------------
N_QUESTIONS = 10

title = r"Teste de Perfil Financeiro"

subtitle = r'''Metodologia DSOP: Diagnosticar, Sonhar, Orçar e Poupar'''

description = r'''Qual seu perfil? Superendividado, Endividado, Equilibrado Financeiramente ou Investidor?

Responda as perguntas abaixo e descubra:'''

answers = [
    {   "question": r"O que você ganha por mês é suficiente para arcar com os seus gastos.?",
        10 : r"Consigo pagar as minhas contas e ainda guardo mais 10% dos meus ganhos.",
        5 : r"É suficiente, mas não sobra nada.",
        0 : r"Gasto todo o meu dinheiro e ainda uso o limite do cheque especial ou peço emprestado para parentes e amigos"},
    {
        "question" : r"Você tem conseguido pagar as suas despesas em dia e à vista?",
        10 : r"Pago em dia, à vista e, em alguns casos, com bons descontos.",
        5 : r"Quase sempre, mas tenho que parcelar as compras de maior valor.",
        0 : r"Sempre parcelo os meus compromissos e utilizo linhas de crédito como cheque especial, cartão de crédito e crediário."
    },
    {
        "question" : r"Você realiza o seu orçamento financeiro mensalmente?",
        10 : r"Faço periodicamente e comparo o orçado com o realizado.",
        5 : r"Somente registro o realizado, sem analisar os gastos.",
        0 : r"Não faço o meu orçamento financeiro."
    },
    {
        "question" : r"Você consegue fazer algum tipo de investimento?",
        10 : r"Utilizo mais de 10% do meu ganho em linhas de investimentos, que variam de acordo com os meus sonhos.",
        5 : r"Quando sobra dinheiro, invisto, normalmente, na poupança.",
        0 : r"Nunca sobra dinheiro para esse tipo de ação."
    },
    {
        "question" : r"Como você planeja a sua aposentadoria?",
        10 : r"Tenho planos alternativos de previdência privada para garantir a minha segurança financeira.",
        5 : r"Contribuo para a previdência social. Sei que preciso de reserva extra, mas não consigo poupar.",
        0 : r"Não contribuo para a previdência social e nem para a privada."
    },
    {
        "question" : r"O que você entende sobre ser Independente Financeiramente?",
        10 : r"Que posso trabalhar por prazer e não por necessidade.",
        5 : r"Que posso ter dinheiro para viver bem o dia a dia.",
        0 : r"Que posso curtir a vida intensamente e não pensar no futuro."
    },
    {
        "question" : r"Você sabe quais são os seus sonhos e objetivos de curto, médio e longo prazos?",
        10 : r"Sei quais são, quanto custam e por quanto tempo terei que guardar para realizá-los.",
        5 : r"Tenho muitos sonhos e sei quanto custam, mas não sei como realizá-los.",
        0 : r"Não tenho sonhos ou, se tenho, sempre acabo deixando-os para o futuro, porque não consigo guardar dinheiro para eles."
    },
    {
        "question" : r"Se um imprevisto alterasse a sua situação financeira, qual seria a sua reação?",
        10 : r"Faria um bom diagnóstico financeiro, registrando o que ganho e o que gasto, além dos meus investimentos e dívidas, se os tiverem.",
        5 : r"Cortaria despesas e gastos desnecessários.",
        0 : r"Não saberia por onde começar e teria medo de encarar a minha verdadeira situação financeira."
    },
    {
        "question" : r"Se a partir de hoje você não recebesse mais seu ganho, por quanto tempo você conseguiria manter seu atual padrão de vida?",
        10 : r"Conseguiria fazer tudo que faço por 5, 10 ou mais anos.",
        5 : r"Manteria meu padrão de vida por 1 a, no máximo, 4 anos.",
        0 : r"Não conseguiria me manter nem por alguns meses."
    },
    {
        "question" : r"Quando você decide comprar um produto, qual é a sua atitude?",
        10 : r"Planejo uma forma de investimento para comprar à vista e com desconto.",
        5 : r"Parcelo dentro do meu orçamento.",
        0 : r"Compro e depois me preocupo como vou pagar."
    },
]

profiles = [
    {
      "profile": "Investidor",
      "min_score" : 80,
      "max_score" : 100,
      "text" : r"Parabéns! Você está no caminho certo! O habito de poupar é o melhor meio para se tornar uma pessoa sustentável financeiramente. É preciso proteger, poupar e guardar parte do dinheiro que passa em suas mãos, pois é por meio dele que você realizará seus sonhos e objetivos. Atrelar o dinheiro guardado a um sonho é o segredo para que ele se realize. Tenha sempre no mínimo 3 sonhos: curto prazo, médio prazo e longo prazo. É importante que você respeite seu dinheiro, lembrando que ele não aceita desaforo, por isso invista sempre em grandes instituições financeiras, como bancos, corretoras e seguradoras. Reúna a família periodicamente e converse sobre o que pretendem realizar no futuro, incluindo as crianças nessas reuniões, pois elas têm muito a contribuir. Ressalto a importância de inserir como sonho a ser realizado, o da independência financeira ou aposentadoria sustentável. Acredite na beleza dos seus sonhos!",
      "color" : "green"
    },
    {
      "profile": "Equilibrado Financeiramente",
      "min_score" : 50,
      "max_score" : 75,
      "text" : r"Pode parecer que tudo está em plena ordem. O fato de não ter dividas, ou se as tiver, estarem controladas, não pode ser sinônimo de tranquilidade. Isso porque você não criou o habito de guardar parte do dinheiro que ganha e, consequentemente, quase não consegue acumular reservas financeiras. Grande parte da população se encontra nessa situação, que é um grande risco. Se algum imprevisto acontecer, como ser convidado para ser padrinho ou madrinha de casamento, ganhar um afilhado, entre outros, por exemplo, é provável que você não tenha alternativa a não ser se tornar uma pessoa inadimplente junto aos compromissos assumidos. Essa situação é conhecida como zona de conforto, mas você deve assumir uma nova postura em relação a utilização do seu dinheiro. É preciso retomar o comando de sua vida financeira, fazer imediatamente um diagnóstico com a ajuda da família, registrando por 30, 60 ou no máximo 90 dias tudo que gastar até mesmo as pequenas despesas. De acordo com uma pesquisa realizada pela DSOP, as famílias possuem, em média, um acréscimo em suas despesas em torno de 20%, seja em compras, em agua, em luz e inclusive, com compras supérfluas. É preciso definir os sonhos para iniciar o processo, lembrando que para cada sonho, também é necessário saber quanto custa, quanto deve guardar por mês e em quanto tempo o realizará: curto, médio ou longo prazo.",
      "color" : "blue"
    },
    {
      "profile": "Endividado",
      "min_score" : 20,
      "max_score" : 45,
      "text" : r"Estar endividado nem sempre é um problema, você pode estar inadimplente, ou próximo disso. É preciso ter muita atenção e não desanimar, porque chegou o momento de levantar a cabeça e saber que sempre existe um caminho. Recomendo o caminho da educação financeira, por meio da metodologia DSOP. É preciso assumir o controle financeiro da sua vida financeira. Como dito anteriormente, reúna a família, inclusive as crianças para uma conversa franca. Talvez seja a primeira vez que você está fazendo isso. O importante é que todos estejam envolvidos nessa missão e com o sonho de sair dessa situação.",
      "color" : "yellow"
    },
    {
      "profile": "Superendividado",
      "min_score" : 0,
      "max_score" : 15,
      "text" : r"Muita calma nessa hora! Estar superendividado, acredite, é o começo de uma nova história. Não nascemos endividados e nem mesmo investidores. Ganhamos e gastamos o dinheiro, ele é um meio importante, mas não podemos tê-lo como um fim. O verdadeiro fim são nossos sonhos e propósitos, assim como os de nossas famílias. Precisamos compreender o ciclo do endividamento, não podemos criticar as formas de créditos. Quando se chega a essa situação é a certeza que novos caminhos virão pela frente. É um marco de um novo começo, para conquistar um novo fim! A orientação em seu caso é de muita calma e serenidade. Tudo é possível, não tenha dúvida. O caminho será se educar financeiramente e será preciso seguir um jeito de fazer, que vamos chamar de Metodologia DSOP de Educação Financeira. Chegou a hora de assumir as rédeas de sua vida financeira e dar um basta nessa situação.",
      "color" : "red"
    },
]


score = 0


st.title(title)
st.markdown(subtitle)


def update_score(score, radio_selected, high_points_answer, high_points_value, low_points_answer, low_points_value):
    if radio_selected == high_points_answer:
        score += int(high_points_value)
    elif radio_selected == low_points_answer:
        score += int(low_points_value)
    else:
        score += 0
        
    return score

with st.form("form_dsop"):
    st.markdown(description)    
    
    # Questions and answers as radio buttons
    for i in range(N_QUESTIONS):
        
        st.write("---")
        
        radio_selected = st.radio(answers[i]["question"], 
                                  (answers[i][10], 
                                   answers[i][5], 
                                   answers[i][0]))
        
        
        score = update_score(score,
                             radio_selected, 
                             answers[i][10],
                             list(answers[i].keys())[1],
                             answers[i][5],
                             list(answers[i].keys())[2])
    
    dsop_submitted = st.form_submit_button("Calcular")

if dsop_submitted:
    
    st.write("Seu perfil é:")
    
    st.balloons()
    
    for profile in profiles:
        if  profile["min_score"] <= score <= profile["max_score"]:
            
            if profile["color"] == "green":
                st.success(profile["profile"])
            elif profile["color"] == "blue":
                st.info(profile["profile"])
            elif profile["color"] == "yellow":
                st.warning(profile["profile"])
            else:
                st.error(profile["profile"])
            
            st.write(profile["text"])
    
with open("planilha-mensal.xlsx", "rb") as file:
    download_spreadsheet = st.download_button(
        label="Baixar Planilha de Orçamento Mensal",
        data=file,
        file_name="dsop-orcamento-mensal.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

with open("artigo-dsop.pdf", "rb") as file:
    download_pdf = st.download_button(
        label="Artigo sobre a Metodologia DSOP",
        data=file,
        file_name="artigo-dsop.pdf",
        mime="application/pdf"
        )

