import pdfplumber
import json

topic_3 = {}
for year in range(100, 111):
    file_path= "./data/" + str(year) + "_Q.pdf"
    pdf = pdfplumber.open(file_path)
    p3 = pdf.pages[3]
    text= p3.extract_text()

    paragraphs= text.split('\n')

    tmp_text = ''
    tmp_ans = ''
    flag, start, topic3 = 0, 0, None
    # print(paragraphs)
    for paragraph in paragraphs:
        # print(paragraph)
        if '三' in paragraph:
            topic3 = paragraphs.index(paragraph)
            break

    for i in range(topic3 + 1, len(paragraphs)):
        if paragraphs[i][0].istitle():
            start = 1
        if start:
            tmp = paragraphs[i].strip()
            if paragraphs[i][0:3] not in ['(A)', '(F)']:
                if tmp_text == '':
                    tmp_text += tmp
                else:
                    tmp_text += ' ' + tmp
            else:
                flag += 1
                if flag == 1:
                    tmp_ans += tmp
                else:
                    tmp_ans += ' ' + tmp
            if flag == 2:
                break
    
    topic_3[year] = {}
    topic_3[year]["Question"] = tmp_text
    topic_3[year]["Choice"] = tmp_ans

with open("./result/topic_3.json", "w", encoding = 'utf-8') as outfile:
    json.dump(topic_3, outfile, ensure_ascii = False, indent = 2)