#https://pypi.python.org/pypi/stop-words
import json
from pathlib import Path
import collections
def convertFile():
    file = open('stop_words.txt', 'r')
    stop_words = file.read().split("\n")
    file.close()
    stop_words.append("->")
    stop_words.append("(Current")
    stop_words.append("Location)")
    directory = Path("Takeout//Searches")
    d = directory.iterdir()
    words = []
    for file in d:
        with open(str(file), 'r') as stuff:
            try:
                data = json.load(stuff)
                for level1 in data:
                    if (isinstance(level1, collections.Iterable)):
                        for level2 in data[level1]:
                            for last in level2:
                                search = level2[last]['query_text'].split(" ")
                                for text in search:
                                    if text not in stop_words:
                                        words.append(text)
                                        '''Can also use "id" to know time'''
                                        '''for s in l[x]:
                                            print(s)
                                            print(l[x][s])'''
            except:
                pass
    file1 = open("searched_words.txt", 'w')
    for line in words:
        file1.write(line)
        file1.write("\n")
    file1.close()
            
