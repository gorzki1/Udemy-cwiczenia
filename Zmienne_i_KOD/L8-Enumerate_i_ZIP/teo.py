workDays = [19, 21, 22, 21, 20,22]

print(workDays)
print(workDays[2])  # wydrukowało 22 bo liczymy od "0"


enumeratedDays = list(enumerate(workDays))
print(enumeratedDays)

for pos, value in enumeratedDays:
    print('Position', pos, 'value', value) 

months = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthsDays = list(zip(months,workDays))
print(monthsDays)
#for m, d in monthsDays:
#    print('Month', m, 'days', d) 

print('*'*63)
for pos, (m, d) in enumerate(zip(months, workDays)):
    print('Position', pos, 'month', m, 'days', d)
