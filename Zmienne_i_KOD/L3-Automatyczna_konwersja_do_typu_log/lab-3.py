
def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(i+1, options[i]))

    choice = input(" Select option above or press enter to exit: ")
    return choice

choice='x'
options = ['load data', "export data", 'analyze & predict']

while choice:
    choice = DisplayOptions(options)

    if choice:
        try:
            choice_num = int(choice)-1
            if choice_num >=0 and choice_num < len(options):
                print((" U have selected {} - {} ").format(choice_num+1, options[choice_num]))
            else:
                print("choose a value froma list or pres ENTER")
        except:
            print("U need to enter a number")
    else:
        print("-----END-----")






