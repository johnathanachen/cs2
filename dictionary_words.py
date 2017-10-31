import os
import sys
import random
import re


with open("/usr/share/dict/words", "r") as directory:
    file_content = directory.read()

num = 5
print("uhhh")

def randomize(num):
    print("hi")
    string_list = list(file_content)
    print(string_list)
    word_list = random.choice(file_content)
    m = re.search('(*\n$)', file_content)s
    for word in file_content:
        word_list.append(file_content)
    print(string_list)
    print(word_list)
    randomize = ' '.join(random.choice(word_list) for i in range(num))
    print(randomize)
    return randomize

randomize(num)

# if __name__ == '__main__':
#     num = sys.argv[1:]
#     randomize(num)
