def dayOfProgrammer(year):
    feb = 28
    total_days = total_days = 31+feb+31+30+31+30+31+31
    if year < 1918:
        if year % 4 == 0:
            feb = 29
            total_days = 31+feb+31+30+31+30+31+31
    elif year == 1918:
        feb = 15
        total_days = 31+feb+31+30+31+30+31+31
    elif year > 1919:
        if year % 400 == 0 or (year %4 ==0 and year % 100 != 0):
            feb = 29
            total_days = 31+feb+31+30+31+30+31+31
    dd = 256 - total_days
    return str(dd) +'.'+'09'+'.'+str(year)



if __name__ == '__main__':
    #year = int(input().strip())
    year = 1918
    result = dayOfProgrammer(year)
    print(result + '\n')
