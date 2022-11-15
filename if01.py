def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b:
        if a>c:
            return a
        else: return c
    if b>a:
        if b>c:
            return b
        else: return c

print (main(15,9,48))