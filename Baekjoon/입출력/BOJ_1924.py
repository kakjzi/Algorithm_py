import datetime
a, b = map(int,input().split())

# 1월 1일은 월요일.
days = ['TUE','WED','THU','FRI','SAT','SUN','MON']
print(days[datetime.date(2017, a, b).weekday()])