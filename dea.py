#-------------------------------------------------------------------------------
# Name:        dea.py
# Purpose:
#
# Author:      James
#
# Created:     22/12/2018
# Copyright:   (c) James 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    #make a regex to search for 'on ...... 2020 from' and then use a list of that to find earliest date
    import re
    import statistics
    from datetime import datetime 
    filename = "D:\\Documents\\PythonProjects\\pythonprojects\\regextests\\deaapril12.txt"
    pattern = re.compile(r"[\£\$\€]{1}[,\d]+.?\d*")
    dates = re.compile(r"on(.*\d\d, 2020 )from")

    moneylist = []
    with open(filename, "rt") as in_file:
        for line in in_file:
            for word in line.split():
                if pattern.search(word) != None:
                    moneylist.append(pattern.findall(line))
    dateslist = []
    for i, line in enumerate(open(filename)):
        for match in re.finditer(dates, line):
            dateslist.append(match.group(1).strip())
    z = []
    for x in moneylist:
        z = x + z
    for x in z:
        z = [s.strip('$') for s in z]
        z = [s.replace(',','') for s in z]
        z = [s.replace('-','') for s in z]
        z = [s.replace("'",'') for s in z]
        z = [s.replace(";",'') for s in z]
        z = [s.replace(" ",'') for s in z]
    moneytotal = 0
    for x in z:
        moneytotal= moneytotal + float(x)
    #print(round(moneytotal,2))
    print("Total siezed in timeframe is: ${0:,.2f}".format(moneytotal))
    mean = moneytotal/len(moneylist)
    print("Average amount per seizure is: ${0:,.2f}".format(mean))
    #add a group for the month to order them and sort the dates better in some way, perhaps find longest possible length of string from 'on' to '
    print(dateslist)
    dateslist.sort(key = lambda date: datetime.strptime(date, '%b %d, %Y')) 
    wait = input("PRESS ENTER TO CONTINUE.\n")

    pass
if __name__ == '__main__':
    main()
