import pdfplumber
import pandas as pd
import json

Answer = {}
for year in range(100, 111):
    file_path= "./data/" + str(year) + "_A.pdf" 
    pdf = pdfplumber.open(file_path)
    p1 = pdf.pages[0]
    text= p1.extract_table()
    del text[0]
    df = pd.DataFrame (text, columns = ['Question1', 'Answer1', 'Question2', 'Answer2', 'Question3', 'Answer3'])
    df1 = df[['Question1', 'Answer1']]
    df1.columns = ['Question', 'Answer']
    df2 = df[['Question2', 'Answer2']]
    df2.columns = ['Question', 'Answer']
    df3 = df[['Question3', 'Answer3']]
    df3.columns = ['Question', 'Answer']
    all_ans = pd.concat([df1,df2,df3], axis=0)
    all_ans.reset_index(drop = True, inplace = True)
    ans = list(all_ans['Answer'])
    topic_1, topic_3, topic_4 = ans[0:15], ans[30:40], ans[40:56]
    assert len(topic_1) == 15 and len(topic_3) == 10 and len(topic_4) == 16
    Answer[year] = {}
    Answer[year]['Topic_1'] = topic_1
    Answer[year]['Topic_3'] = topic_3
    Answer[year]['Topic_4'] = topic_4

with open("./result/answer.json", "w") as outfile:
    json.dump(Answer, outfile, indent = 2)