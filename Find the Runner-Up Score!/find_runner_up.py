
def find_runner_up(n, a):
    """_summary_

    Args:
        n (_type_): 5
        a (_type_): 2 3 6 6 5
    """
    score_array = list(a)
    
    if score_array.__len__() == int(n):
        runner_up = min(score_array)
        for i in score_array:
            if i > runner_up and i < max(score_array):
                runner_up = i

        return runner_up


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(find_runner_up(n, arr))
