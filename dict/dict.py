"""
 Prerequisites:
    sudo apt install sdcv
    tar xvfj stardict-babylon-collins4-2.4.2.tar.bz2 -C/home/ubuntu/.stardict/dic/

 Usage: python3 dict.py

 Input: words.txt
 Output: output.csv

    Input: one word per line
    Output: a csv separated by , with
        1st column: word
        2nd column: definition

Download dictionary files: http://download.huzheng.org/babylon/english/

"""

import subprocess
import json
import csv

d = 'MacMillan English Dictionary -American'
d = "Collins COBUILD Advanced Learner's English Dictionary"
d = "Oxford Advanced Learner's Dictionary 7th"

def executeShell(command):
    try:
        output = subprocess.check_output(command, shell=True)
        status = 0
    except subprocess.CalledProcessError:
        output = ""
        status = 1
    return (status, output)


class DictionaryCSV():
    def __init__(self):
        pass

    def translate_word(self, word):
        (e,o) = executeShell('sdcv -j -u "' + d + '" "' + word + '"')
        # print(o)
        # two problems here
        # 1. wade through output = [wade..][through...]
        # 2. "wade through" output = []
        l = json.loads( o.decode("utf-8") )
        if len(l) > 0:
            return [word, l[0]['definition']]

    def translate_file(self, words_file, output_file):
        table = []
        lines = [line.rstrip('\n') for line in open(words_file)]
        #print(lines)
        for word in lines:
            print(word)
            result = self.translate_word(word)
            if result is not None:
                table.append(result)

        #print(table)
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(table)

if __name__ == '__main__':
    dcsv = DictionaryCSV()
    dcsv.translate_file("words.txt", "output.csv")
