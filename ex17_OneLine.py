# $ python ex17_OneLine.py ex17_test.txt ex17_test_new.txt

from sys import argv
from os.path import exists

script, from_file, to_file = argv

open(to_file,'w', encoding='UTF-16 LE').write(open(from_file, encoding='UTF-16 LE').read())