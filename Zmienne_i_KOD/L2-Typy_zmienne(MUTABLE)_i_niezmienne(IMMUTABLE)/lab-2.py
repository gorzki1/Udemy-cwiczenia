days = ['mon', 'tue', 'we', 'thu', 'fri', 'sat', 'sun']
workdays = days.copy()
print('Variable days', days, id(days))
print('Variable workdays', workdays, id(workdays))

del workdays[5:7]
print('Variable workdays', workdays, id(workdays))

print('Variable days', days, id(days))
print('Variable workdays', workdays, id(workdays))
