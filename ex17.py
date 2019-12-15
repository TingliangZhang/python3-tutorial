#Make a Samle file
# $ echo "this is a test file." > ex17_test.txt
#Look at it
# $ cat test.txt
#Now Run
# $ python ex17.py ex17_test.txt ex17_test_new.txt

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copy from {from_file} to {to_file}.")

# in_file=open(from_file)
# Error!
# UnicodeDecodeError: 'gbk' codec can't decode byte 0xff in position 0: illegal multibyte sequence

# 原因：在Windows下echo进去的文件格式默认为 UTF-16 LE ！

# Trying to solve this problem
# in_file=open(from_file, encoding='gbk')
# in_file=open(from_file, encoding='gb18030', errors='ignore')
# in_file=open(from_file, encoding='UTF-8', errors='ignore')
in_file=open(from_file, encoding='UTF-16 LE')
indata=in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"The output file exist? {exists(to_file)}")

input()


# out_file=open(to_file,'w')
# Error!
# UnicodeEncodeError: 'gbk' codec can't encode character '\u2eb6' in position 0: illegal multibyte sequence
out_file=open(to_file,'w', encoding='UTF-16 LE')
out_file.write(indata)

print("done")
out_file.close()
in_file.close()