



def file_wr(str,file_name):

    file = open(file_name, 'a', encoding='UTF-8')
    file.write(str+"\n")
    file.close()
    
file_wr("pokes", "haha.txt")