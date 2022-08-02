import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0
#print(len(word))
while i < len(word):
    if word[i] == "<":       #열린괄호 인지
        i += 1 
        while word[i] != ">":  #닫힌괄호 인지
            i += 1 
        i += 1              
    elif word[i].isalnum(): # num or alpha
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        word[start:i]=reversed(word[start:i]) # 괄호아닌 부분뒤집기
    else:           # blank일때    
        i+=1                

print("".join(word)) #list합쳐서 내보내기
