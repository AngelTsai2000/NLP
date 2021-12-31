import pdfplumber
import json

topic_1 = {}
for year in range(100, 111):
    file_path= "./data/" + str(year) + "_Q.pdf" 
    pdf = pdfplumber.open(file_path)
    page = 1
    p1 = pdf.pages[page]
    text= p1.extract_text()      

    paragraphs= text.split('\n')
    text_list, Q1, A1 = [], [], []
    tmp_str = ''
    for num, paragraph in enumerate(paragraphs):
        if num >= 7 and num < len(paragraphs)-1:
            if paragraph[0] in ['(', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if num > 7:
                    text_list.append(tmp_str)
                tmp_str = ''
                tmp_str = paragraph.strip()
            else:
                tmp_str += ' ' + paragraph.strip()
    text_list.append(tmp_str)
    for s in range(0, 30, 2):
        tmp = s // 2 + 1
        Q1.append(text_list[s].replace(str(tmp)+'.', '').strip())
        A1.append(text_list[s+1])
    
    assert len(Q1) == 15
    assert len(A1) == 15
    topic_1[year] = {}
    topic_1[year]["Question"] = Q1
    topic_1[year]["Choice"] = A1

with open("./result/topic_1.json", "w") as outfile:
    json.dump(topic_1, outfile, indent = 2)