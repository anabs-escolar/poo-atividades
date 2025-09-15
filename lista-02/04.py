
from multiprocessing import reduction


i = input("Digite uma data no formato dd/mm/aaaa\n")


def check_valid_date(date: str) -> bool:
    """_summary_

    Args:
        date (str): Date in format "dd/mm/yyyy"
    Returns:
        bool: True for valid dates
    """
    date = list(map(int, date.split(sep="/")))
    
    three_values = True if len(date) <= 3 else False
    days = True if date[0] <= 31 and date[0] > 0 else False
    month = True if date[1] <= 12 and date[1] > 0 else False
    
    if three_values and days and month :
        return True
    return False


if check_valid_date(i):
    print("A data informada é válida")
else:
    print("A data informada não é válida")
    