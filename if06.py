def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1= n%10
    x2= n%100//10
    x3= n%1000//100
    x4= n%10000//1000
    x5= n//10000
    if x1>x2:
        if x1>x3:
            if x1>x4:
                if x1>x5:
                    return 1
                else: return 5

    if x2>x3:
        if x2>x4:
            if x2>x5:
                return 2
            else: return 5
    if x3>x4:
        if x3>x5:
            return 3
        else: return 5
    if x4>x5:
        return 4
    else: return 5

print (main(17345))