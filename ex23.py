#languages.txt needed!  (https://learnpythonthehardway.org/python3/languages.txt)
# $ python ex23.py utf-8 strict
# $ python ex23.py big5 strict
# $ python ex23.py big5 replace
import sys
script, encoding, error =sys.argv


def main(lauguage_file, encoding, errors):
    line = lauguage_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(lauguage_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip() # delete /n
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)