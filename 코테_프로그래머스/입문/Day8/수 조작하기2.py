def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        num = numLog[i] - numLog[i-1]
        if num == 1:
            answer += 'w'
        elif num == -1:
            answer += 's'
        elif num == 10:
            answer += 'd'
        elif num == -10:
            answer += 'a'
        
    return answer

result = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
print(solution(result))



# 다른사람풀이

def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        if numLog[i]-numLog[i-1]==1:
            answer+='w'
        elif numLog[i]-numLog[i-1]==-1:
            answer+='s'
        elif numLog[i]-numLog[i-1]==10:
            answer+='d'
        elif numLog[i]-numLog[i-1]==-10:
            answer+='a'
    return answer
