def main(s,n):
    """
    s string is given. repeat it n times and return the resulting string.
    Args:
        s: str
        n: int
    Returns:
        str: return answer.
    """
    answer=s*n
    return answer
s='Salom'
n=5
print(main(s,n))