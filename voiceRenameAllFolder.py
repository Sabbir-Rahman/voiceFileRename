#rename all folder and its under voices if
#name_gender_age convention followed

import os



#write your root folder name
path = "C:\\Users\\User\\Desktop\\voice"

path_dir_root = os.chdir(path)
for path_name in os.listdir(path_dir_root):

    path_name_list = []
    path_dir_sub = os.chdir(str(path) + '\\' + str(path_name))

    path_name_list = path_name.split("_")
    print(path_name_list[0])
    c=1
    v=1
    total = 0
    name = path_name_list[0]
    gender = path_name_list[1]
    age = path_name_list[2]

    def correct_order():
        for file in os.listdir(path_dir_sub):
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

    for file1 in os.listdir(path_dir_sub):
        if total%5 ==0 and total <50 and total>0:
            v = 1
            c = c + 1
        if total ==50:
            v = 1
            c = c + 1

        new_file_name = "c00{}v00{}{}{}{}.wav".format(c,v,gender,age,name)

        os.rename(file1,new_file_name)
        print(file1)
        v = v+1
        total = total + 1
