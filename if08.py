def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    a=number
    if a==1:
        return "Monday"
    elif a==2:
        return "Tuesday"
    elif a==3:
        return "Wednesday"
    elif a==4:
        return "Thursday"
    elif a==5:
        return "Friday"
    elif a==6:
        return "Saturday"
    elif a==7:
        return "Sunday"


print (main(5))