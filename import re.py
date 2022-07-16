import re

len_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 65536]

def parse(stringinput):
    date, len_weeks = stringinput.split(',')
    len_weeks = int(len_weeks)
    date = date[1:-1]
    month, date = map(int,date.split("/"))
    if(date > len_month[month]):
        date = len_month[month]
    return month, date, len_weeks

def mdtoi(month, date):
    result = 0
    for i in range(1, month):
        result += len_month[i]
    result += date
    return result

def get_first_day_of_week(i):
    i = (i // 7) * 7 + 1
    return i

def itomd(i):
    if(i > 365):
        return 13, 1
    month = 1
    day = 0
    while(day + len_month[month] < i):
        day += len_month[month]
        month += 1
    date = i - day
    return month, date

def solve(stringinput):
    month, date, len_weeks = parse(stringinput)
    print("month", month)
    print("date", date)
    print("len_weeks", len_weeks, "\n\n\n")
    result = []
    day = mdtoi(month, date)
    first_day = get_first_day_of_week(day)
    last_written_month = None
    for _ in range(len_weeks):
        week = []
        if(first_day > 365):
            break
        for i in range(7):
            if(first_day + i > 365):
                break
            m, d = itomd(first_day + i)
            if(last_written_month != m):
                week.append(str(m) + "/" + str(d))
                last_written_month = m
            else:
                week.append(str(d))
        first_day += 7
        result.append(week)
    return result

if __name__ == '__main__':
    print(solve(input()))
    assert(mdtoi(1, 1) == 1)
    assert(mdtoi(1, 7) == 7)
    assert(mdtoi(2, 1) == 32)
    assert(mdtoi(12,31) == 365)
    assert(itomd(1) == (1, 1))
    assert(itomd(7) == (1, 7))
    assert(itomd(32) == (2, 1))