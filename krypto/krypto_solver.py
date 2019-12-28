"""
Christian Felt
December 2019
Solves Krypto problems.
"""

OPS = {'+', '-', '*', '/'}


def solve(cards, target):
    for op1 in OPS:
        for op2 in OPS:
            for op3 in OPS:
                for op4 in OPS:
                    this_answer = str(cards[0]) + " " + op1 + " " + str(cards[1]) + " " + op2 + " " + \
                                  str(cards[2]) + " " + op3 + " " + str(cards[3]) + " " + op4 + " " + str(cards[4])
                    if eval(this_answer) == target:
                        return this_answer + " = " + str(target)
    return "There is no solution."


if __name__ == "__main__":
    print(solve([2, 3, 4, 5, 6], 4))
