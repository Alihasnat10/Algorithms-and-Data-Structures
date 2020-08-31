def timeConversion(s):
    hh = s[0:2]
    mm = s[3:5]
    ss = s[6:8]
    t = s[8:11]
    if t == 'AM' and hh == '12':
        hh = '00'
    if t == 'PM' and hh != '12':
        hh = int(hh)
        hh += 12
    print(str(hh)+':'+mm+':'+ss)

#s='07:05:45PM'
#s='12:00:00AM'
s='07:05:45PM'
timeConversion(s)
