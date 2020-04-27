'''
High Schore
-------
Write methods that return the highest score from the list, the last added score and the three highest scores.

You may assume: - scores is a list of unorderd integer values 
                - There are no negative numbers

RESTATE
From a list of positive integers, return the highest num, last adderd num and the three highest nums in the list.

ASSUMPTIONS
We'll assume that input contains positive integers 0-n. 

BRAINSTORM
My initial idea is return the value at the last index, loop over scores and return the highest score, 
then create three score variables, loop over score list and update scores accordinly. 

EXPLAIN
Last score: Here we have a 0(n) solution in which return the score at the last index.
Highest score: Here we have  o(n^2) loop that checks if the score is greater than the high score. 

TRADEOFFS
Overall it's less memory efficient but is more time efficient.
'''



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


        