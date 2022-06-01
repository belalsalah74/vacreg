import datetime

now = datetime.datetime.now().date()

delta = datetime.timedelta(days=30)

date = f'{now+delta}'

print(datetime.datetime('2022-05-31'))
