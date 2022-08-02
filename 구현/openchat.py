def solution(record):
    answer = []
    id_nickname = {}
    print_out = []
    
    for i in record:
        mode = i.split()[0]
        
        if mode == 'Enter':
            id_code = i.split()[1]
            nickname = i.split()[2]
            id_nickname[id_code] = nickname
            print_out.append([id_code,'님이 들어왔습니다.'])
            
        elif mode == 'Leave':
            id_code = i.split()[1]
            print_out.append([id_code,'님이 나갔습니다.'])
            
        elif mode == 'Change':
            id_code = i.split()[1]
            nickname = i.split()[2]
            id_nickname[id_code] = nickname
            
            
    for j in print_out:
        k = id_nickname.get(j[0])+j[1]
        answer.append(k)
    
    return answer