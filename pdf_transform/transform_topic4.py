import pdfplumber
import json

def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

topic_4 = {}
for year in range(100, 111):
    file_path= "./data/" + str(year) + "_Q.pdf"
    pdf = pdfplumber.open(file_path)
    p4 = pdf.pages[3:]
    text = ''
    for p in p4:
        tmp = p.extract_text()
        text += ' ' + tmp
    paragraphs= text.split('\n')

    topic4, topic5 = None, None
    for paragraph in paragraphs:
        if '四' in paragraph:
            topic4 = paragraphs.index(paragraph)
        elif '貳' in paragraph:
            topic5 = paragraphs.index(paragraph)
            break

    result = {}
    start, ans, ques, i, count = 0, 0, 0, 0, 0
    q_nums = ['41.', '42.', '43.', '44.', '45.', '46.', '47.', '48.', '49.', '50.', '51.', '52.', '53.', '54.', '55.', '56.']
    ans_mark = ['(A)', '(B)', '(C)', '(D)']
    for paragraph in paragraphs[topic4 + 1 : topic5]:
        if '題組' in paragraph:
            if start:
                result[i] = {}
                result[i]['Text'] = tmp_text.strip()
                result[i]['Question'] = tmp_q.strip()
                result[i]['Choice'] = tmp_ans.strip()
            i += 1
            tmp_text, tmp_q, tmp_ans = '', '', ''
            start = 1
        elif start and (paragraph[0:3] in q_nums or paragraph[0:3] in ans_mark or is_contains_chinese(paragraph) == 0):
            tmp = paragraph.strip()
            if paragraph[0:3] not in q_nums and paragraph[0:3] not in ans_mark:
                ques = 0
                ans = 0
                tmp_text += ' ' + tmp
            elif (paragraph[0:3] in q_nums or ques) and paragraph[0:3] not in ans_mark:
                if paragraph[0:3] in q_nums:
                    tmp_q += '\n' + tmp
                else:
                    tmp_q += ' ' + tmp
                ques = 1
                ans = 0
            elif (paragraph[0:3] in ans_mark or ans) and paragraph[0:3] not in q_nums:
                if paragraph[0:3] in ans_mark:
                    tmp_ans += ' ' + tmp
                else:
                    tmp_ans += ' ' + tmp
                ques = 0
                ans = 1

    result[i] = {}
    result[i]['Text'] = tmp_text.strip()
    result[i]['Question'] = tmp_q.strip()
    result[i]['Choice'] = tmp_ans.strip()
    assert len(result) == 4

    topic_4[year] = result

ans_mark = ['(A)', '(B)', '(C)', '(D)']
topic_4_final = {}
for year in topic_4.keys():
    topic_4_final[year] = {}
    for i in range(1, 5):
        topic_4_final[year][i] = {}
        topic_4_final[year][i]['Text'] = topic_4[year][i]['Text']

        q_tmp = topic_4[year][i]['Question'].split('\n')
        topic_4_final[year][i]['Question'] = {}
        for tmp in q_tmp:
            tmp_2 = tmp.split('. ')[1]
            topic_4_final[year][i]['Question']['Q' + str(q_tmp.index(tmp) + 1) + '.'] = tmp_2
        assert len(topic_4_final[year][i]['Question']) == 4

        a_tmp = topic_4[year][i]['Choice'].split(' (')
        topic_4_final[year][i]['Choice'] = {}
        count, tmp_2, n = 0, '', 1
        for tmp in a_tmp:
            if tmp[0] == '(':
                tmp_2 += ' ' + tmp
            else:
                tmp_2 += ' (' + tmp
            count += 1
            if count == 4:
                # print(tmp_2.strip())
                topic_4_final[year][i]['Choice']['Q' + str(n) + '.'] = tmp_2.strip()
                count = 0
                tmp_2 = ''
                n += 1
        # print(topic_4_final[year][i]['Choice'])
        assert len(topic_4_final[year][i]['Choice']) == 4
        
with open("./result/topic_4.json", "w", encoding = 'utf-8') as outfile:
    json.dump(topic_4_final, outfile, ensure_ascii = False, indent = 2)