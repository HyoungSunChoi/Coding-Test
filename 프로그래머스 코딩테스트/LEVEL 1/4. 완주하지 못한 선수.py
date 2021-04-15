import collections
participant=["mislav", "stanko", "mislav", 'john',"ana"]
completion=["stanko", "ana", "mislav"]
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys()))
    return list(answer.keys())[0]
print(solution(participant,completion))

