import streamlit as st

################## Model1 ##################
def TestModel1(sentence: str, words: list):
    '''
    Input
    - question sentence
    - words list with four words
    ----------------------------
    output
    - filled sentence (replace _ by right word)
    - the list of different meaning dictionary of the right word (word/prob/E_mean/C_mean/example)
    '''

    result = []         # store all answers
    answer1 = {}        # ex: answer1 dictionary
    answer2 = {}        # ex: answer2 dictionary

    ### predict sentence with four words in words list

    temp = sentence.split()
    for i in range(len(temp)):                          # fill the blank of input question
        if temp[i] == '_':
            temp[i] = 'abort'
            sentence = ' '.join(temp)

    answer1['word'] = 'abort'
    answer1['prob'] = '97.33%'
    answer1['E_mean'] = 'to stop the development of a baby that has not been born, usually by having a medical operation.'
    answer1['C_mean'] = '墮胎，人工流產'
    answer1['example'] = 'The plan/flight had to be aborted at the last minute.'
    result.append(answer1)

    answer2['word'] = 'abort'
    answer2['prob'] = '2.67%'
    answer2['E_mean'] = 'to cause something to stop of fail before it begins or before it is complete.'
    answer2['C_mean'] = '中止；使夭折；使中途失敗'
    answer2['example'] = 'They decided to abort the pregnancy.'
    result.append(answer2)
    
    return sentence, result

################## Model2 ##################
def TestModel2(article: str, words: list):
    '''
    Input
    - question article
    - words list with ten words
    ----------------------------
    output
    - filled article (replace all _ by right words)
    '''

    ### predict and revise the article

    result = article
    
    return result

################## Model3 ##################
def TestModel3(article: str):
    '''
    Input
    - question article
    ----------------------------
    output
    - article with highlight words
    - the list of words meaning dictionary (word/prob/E_mean/C_mean/example)
    '''

    result = []         # store all answers
    keyword1 = {}        # ex: keyword1 dictionary
    keyword2 = {}        # ex: keyword2 dictionary

    ### find and highlight the keywords of the article 

    keyword1['word'] = 'foreign'
    keyword1['pos'] = 'adj.'          # part of speech (詞性)
    keyword1['E_mean'] = 'belonging or connected to a country is not your own.'
    keyword1['C_mean'] = '外國的'
    keyword1['example'] = 'Spain was the first foreign country she had visited.'
    result.append(keyword1)
    
    
    return article, result

################## application1 ##################
def app1():
    st.header("字彙填空")
    st.write("Please entry the question and the options:")
    words = [None] * 4
    with st.form(key='form1'):
        input_question = st.text_input(label="Question")
        col1, col2 = st.columns(2)
        with col1:
            words[0] = st.text_input(label="A")
            words[1] = st.text_input(label="C")
        with col2:
            words[2] = st.text_input(label="B")
            words[3] = st.text_input(label="D")
        submit = st.form_submit_button('Search')

        if submit:
            output_sentence, result = TestModel1(input_question, words)     # the prediction result
            st.header("Answer: %s" %(output_sentence))                      # print the answer
            for answer in result:
                st.subheader("%s: %s" %(answer['word'], answer['prob']))
                st.write("> %s" %(answer['E_mean']))
                st.write("> %s" %(answer['C_mean']))
                st.write("> %s" %(answer['example']))

    #st.subheader("(answer_word): (percentage)")
    #st.write("(English meaning)")
    #st.write("(Chinese meaning)")
    #st.write("(example sentence)")


################## application2 ##################
def app2():
    st.header("克漏字")
    st.write("Please entry the article and the words:")
    words = [None] * 10
    with st.form(key='form2'):
        input_article = st.text_area(label="Article")
        col1, col2 = st.columns(2)
        with col1:
            words[0] = st.text_input(label="word1")
            words[1] = st.text_input(label="word3")
            words[2] = st.text_input(label="word5")
            words[3] = st.text_input(label="word7")
            words[4] = st.text_input(label="word9")
        with col2:
            words[5] = st.text_input(label="word2")
            words[6] = st.text_input(label="word4")
            words[7] = st.text_input(label="word6")
            words[8] = st.text_input(label="word8")
            words[9] = st.text_input(label="word10")
        submit = st.form_submit_button('Search')

        if submit:
            result = TestModel2(input_article, words)           # the prediction result
            st.header("Answer")
            st.write(result)      

    #st.header("Answer")
    #st.write("(Filled Article) ...")


################## application3 ##################
def app3():
    st.header("文章字義查詢")
    st.write("Please enter the article or sentence:")
    with st.form(key='form3'):
        input_article = st.text_area(label="Article or Sentence")
        submit = st.form_submit_button('Search')

        if submit:
            output_article, result = TestModel3(input_article)          # the prediction result
            st.header("Answer")
            st.write(output_article) 
            for keyword in result:
                st.subheader("%s: %s" %(keyword['word'], keyword['pos']))
                st.write("> %s" %(keyword['E_mean']))
                st.write("> %s" %(keyword['C_mean']))
                st.write("> %s" %(keyword['example']))

    #st.subheader("Keywords")
    #st.write("(Original article) ...")
    #st.write("* (word1)")
    #st.write("(English meaning)")
    #st.write("(Chinese meaning)")
    #st.write("(example sentence)")



################## start run app ##################

st.title("English Helper")

selection = st.selectbox("Choose one function", ("字彙填空", "克漏字", "文章字義查詢"))
st.markdown("***")

if selection == "字彙填空":
    app1()
elif selection == "克漏字":
    app2()
else:
    app3()

