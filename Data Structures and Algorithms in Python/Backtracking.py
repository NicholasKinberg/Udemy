# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
# example of backtracking
# backtracking is a form of recursion
def permute(list, s):
    if list == 1:
        return s
    else:
        return [
            y + x
            for y in permute(1, s)
            for x in permute(list - 1, s)
        ]