from datetime import datetime


def get_previous_quarter() -> tuple[int, int]:
    current_year = datetime.now().year
    current_quarter = (datetime.now().month - 1) // 3 + 1

    if current_quarter == 1:
        return current_year - 1, 4
    else:
        return current_year, current_quarter - 1
