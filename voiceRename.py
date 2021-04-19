#name single file voices
#have to change name,age, gender everytime

import os

path = os.chdir("C:\\Users\\User\\Desktop\\sabbir")

c=1
v=1
total = 0
name = 'sabbir'
gender = 'm'
age = '21'

def correct_order():
    for file in os.listdir(path):
        if file == 'Recording_1.wav':
            print(file)
            os.rename(file, 'Recording_01.wav')
        if file == 'Recording_2.wav':
            print(file)
            os.rename(file, 'Recording_02.wav')
        if file == 'Recording_2.wav':
            print(file)
            os.rename(file, 'Recording_02.wav')
        if file == 'Recording_3.wav':
            print(file)
            os.rename(file, 'Recording_03.wav')
        if file == 'Recording_4.wav':
            print(file)
            os.rename(file, 'Recording_04.wav')
        if file == 'Recording_5.wav':
            print(file)
            os.rename(file, 'Recording_05.wav')
        if file == 'Recording_6.wav':
            print(file)
            os.rename(file, 'Recording_06.wav')
        if file == 'Recording_7.wav':
            print(file)
            os.rename(file, 'Recording_07.wav')
        if file == 'Recording_8.wav':
            print(file)
            os.rename(file, 'Recording_08.wav')
        if file == 'Recording_9.wav':
            print(file)
            os.rename(file, 'Recording_09.wav')

correct_order()

for file in os.listdir(path):
    if total%5 ==0 and total <50 and total>0:
        v = 1
        c = c + 1
    if total ==50:
        v = 1
        c = c + 1

    new_file_name = "c00{}v00{}{}{}{}.wav".format(c,v,gender,age,name)

    # os.rename(file,new_file_name)
    print(file)
    v = v+1
    total = total + 1
