# python3
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    answer = 0
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                answer = i + 1
                break
            pop_bracket = opening_brackets_stack.pop()[0]
            if are_matching(pop_bracket, next):
                continue
            else:
                answer = i + 1
                break

    if answer != 0:
          return answer
    elif (len(opening_brackets_stack)):
          return opening_brackets_stack.pop()[1] + 1
    else:
          return 'Success'

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
