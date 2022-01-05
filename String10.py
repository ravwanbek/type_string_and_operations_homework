def main(x,y):
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    a=str((x+y)*2)
    answer='"'+'('+str(x)+'+'+str(y)+')'+'*'+'2'+'='+a+'"'

    return answer
print(main(1,2))