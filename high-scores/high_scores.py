from heapq import nlargest


def latest(scores):
    if len(scores) == 0:
        return None

    return scores[len(scores)-1]


def personal_best(scores):
    high_score = 0
    for num in scores:
        if num > high_score:
            high_score = num
    
    return high_score


def personal_top_three(scores):
    return nlargest(3, scores)


        