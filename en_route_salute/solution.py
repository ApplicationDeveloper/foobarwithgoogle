RIGHT_WALKER = '>'
LEFT_WALKER = '<'
EMPTY_SPACE = '-'

def solution(s):
    pathway = s
    pathway_length = len(s)
    no_of_salutes = 0

    for i in range(pathway_length):
        character = s[i]

        if character == RIGHT_WALKER:
            starting_point = i + 1
            for j in range(starting_point, pathway_length):
                if s[j] == LEFT_WALKER:
                    no_of_salutes += 2
    
    return no_of_salutes

assert solution(">----<") == 2
assert solution("--->-><-><-->-") == 10
assert solution("<<>><") == 4
