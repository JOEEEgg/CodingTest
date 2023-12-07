def solution(arr, queries):
    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
    
    return arr

result = [0, 1, 2, 3, 4]
quriess = [[0, 3],[1, 2],[1, 4]]

print(solution(result, quriess))