def main(x,y):
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """

    answer='('+str(x)+'+'+str(y)+')'+'*'+'2'+'='+'{'+'answer'+'}'

    return answer
print(main(1,2))