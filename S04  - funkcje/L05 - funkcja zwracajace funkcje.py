from datetime import datetime

def generator(time="minutes"):
    dictForFunc = {"minutes": 60, "hours": 3600, "days": 86400}
    unit = dictForFunc[time]
    source = '''
def f_span(date1, date2):
    span = date2 - date1
    duration = span.total_seconds()
    result = divmod(duration, {})[0]
    return result'''.format(unit)
    exec(source, globals())
    return f_span

f_minutes = generator("minutes")
f_hours = generator("hours")
f_days = generator("days")

start = datetime(1997, 9, 14, 0, 0, 0)
stop = datetime(1997, 9, 15, 0, 0, 0)
stop2 = datetime.now()

print(f_minutes(start, stop))
print(f_hours(start, stop))
print(f_days(start, stop2))

