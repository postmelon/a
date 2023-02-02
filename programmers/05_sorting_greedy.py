gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

def solution(gems):
    list = []
    item = 0
    # 서로 다른 종류 계산
    for i in range(len(gems)):
        if gems[i] not in list:
            list.append(gems[i])
            item += 1

    for i in range(len(gems)):
        if len(list) == item:






    answer = []
    return answer

print(solution(gems))