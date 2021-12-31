import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time

# read data to list
df = pd.read_csv('./data/vocabulary_preprocessed.csv', names=['vocab'], header=None)
vocabs = df['vocab'].tolist()
tmp_set = set(vocabs)
vocabs = list(tmp_set)
vocabs.sort()
# vocabs = ['in']
print(len(vocabs))
vocabs_dic = {}

'''class Vocab:
    def __init__(self, num, pos, eng_def, chi_def, eg):
        self.num = num
        self.pos = pos
        self.eng_def = eng_def
        self.chi_def = chi_def
        self.eg = eg'''

url_pre = "https://dictionary.cambridge.org/dictionary/english-chinese-traditional/"
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
for vocab in vocabs[6000:]:
    # time.sleep(1)
    print(vocab, vocabs.index(vocab))
    url = requests.get(url_pre + vocab, headers = headers)
    url.encoding = 'UTF-8'
    soup = BeautifulSoup(url.text,'html.parser')

    vocabs_dic[vocab] = []
    # print('\033[44m {} \033[0m'.format(vocab))
    words = soup.find_all(class_ = "pr entry-body__el")
    num = 0
    for word in words:
        pos = word.find(class_ = "pos dpos")
        try:
            pos = pos.text
        except:
            pos = None
        def_blocks = word.find_all(class_ = "def-block ddef_block")
        for def_block in def_blocks:
            '''print('\033[42m {} \033[0m'.format(pos.text))
            print('\033[36m Def {} \033[0m'.format(def_blocks.index(def_block) + 1))'''
            num += 1
            eng_def = def_block.find(class_ = "def ddef_d db")
            eng_def = eng_def.text.replace('\n',' ')
            chi_def = def_block.find(class_ = "trans dtrans dtrans-se break-cj")
            try:
                chi_def = chi_def.text.replace('\n',' ')
            except:
                chi_def = None
            eg_sents = def_block.find_all(class_ = "eg deg")
            '''print(eng_def)
            print(chi_def)
            for sent in eg_sents:
                print(sent.text.replace('\n',' '))'''
            try:
                eg_sent = eg_sents[0].text.replace('\n',' ')
            except:
                eg_sent = None
            # tmp = Vocab(num, pos.text, eng_def, chi_def, eg_sent)
            tmp = {'num': num, 'pos': pos, 'eng_def': eng_def, 'chi_def': chi_def, 'eg': eg_sent}
            vocabs_dic[vocab].append(tmp)

with open("vocabulary_7.json", "w", encoding = 'utf-8') as outfile:
    json.dump(vocabs_dic, outfile, ensure_ascii = False, indent = 2)