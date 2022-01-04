def main(x1,x2,x3):
    """
    Given three integers, x1, x2, and x3, return the "[x1, x2, x3]" string.
    Args:
        x1: int
        x2: int
        x3: int
    Returns:
        str: return answer.
    """
    answer='['+x1+','+x2+','+x3+']'
    return answer
print(main(x1='Name',x2='Last name',x3='Father\'s name'))