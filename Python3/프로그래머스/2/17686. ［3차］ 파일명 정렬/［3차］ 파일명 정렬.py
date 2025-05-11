import re

def decomp(file:str):
    number = re.findall(r'\d+', file)
    numind = file.index(number[0])
    
    # head, numb, tail
    return file[:numind].lower(), number[0], file[numind+len(number[0]):]
    
    
    

def solution(files):

    li = []
    for file in files:
        head, num, tail = decomp(file)
        li.append([file, head, num, tail])
    
    
    li.sort(key=lambda x: (x[1], int(x[2])))
    answer = [x[0] for x in li]
    
    return answer

