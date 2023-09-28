import csv
import matplotlib.pyplot as plt
import time
import re

filename = 'pricesAids.csv'

# initializing the titles and rows list
fields = []
rows = []
extraRows = []
pattern1 = r'[A-K]'

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)



    # extracting each data row one by one
    for row in csvreader:
        # Секционирование по кол-ву производителей(но тогда круговая диаграмма для второй секции не будет построена)
       # if (int(row[2]) > 5):
          #  rows.append(row)
       # else:
        #    extraRows.append(row)
    # Секционирование по суммарной трате на лекарства за 2021 год
        #if (float(row[28]) > 500000):
    # Секционирование по средней цене на лекарства за 2021 год
        if (float(row[32]) > 100):
            rows.append(row)
        else:
            extraRows.append(row)
        # Секционирование по алфавиту
        # if (re.fullmatch(pattern1, row[0][0])):
        #     rows.append(row)
        # else:
        #     extraRows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
# print('Field names are:' + ', '.join(field for field in fields))

# print(fields[22]) - Tot_Spndng_2020
# print(float(rows[800][22]))

# printing first 5 rows
# print('\nFirst 5 rows are:\n')
# for row in rows[:2]:
    # parsing each column of a row
    # for col in row:
    #      print("%10s" % col, end=" "),
    # print('\n')
print(fields[32]) # суммарная трата / кол-во выписанных рецептов = средняя цена
print(rows[1][32])
print(rows[1][30])
print(rows[1][28])

a = ['a', 'b', 'c', 'd']

b = 'f' in a
print(b)

a.append('g')

print(fields[23]) # used aids
print(fields[24]) # created recipes

countUsedAidsTwentyYear = []
countCreatedRecipesTwentyYear = []
countOfProducersMoreTwentyFive = []
brandsNameArray = []
countTotalProducersMoreOne = []
countUsedAidsTwOneYear = []



countUsedAidsTwentyYear2 = []
countCreatedRecipesTwentyYear2 = []
countOfProducersMoreTwentyFive2 = []
brandsNameArray2 = []
countTotalProducersMoreOne2 = []
countUsedAidsTwOneYear2 = []


print(float(rows[1][23]))

print(fields[2]) # countOfProducers
print(fields[0]) # brandsName

st = time.time()
for i in range(0, len(rows), 1):

    if ((not (rows[i][0] in brandsNameArray)) & (int(rows[i][2]) > 20)):
        brandsNameArray.append(rows[i][0])
        #countOfProducersMoreTwentyFive.append(int(rows[i][2]))
        countUsedAidsTwOneYear.append(float(rows[i][29]))




    if (not ((rows[i][23] == '') | (rows[i][24] == ''))):
        countUsedAidsTwentyYear.append(float(rows[i][23]))
        countCreatedRecipesTwentyYear.append(float(rows[i][24]))


    if (int(rows[i][2]) > 1):
        countTotalProducersMoreOne.append(int(rows[i][2]))


print('Время в первой секции')
print(time.time()-st)
et = time.time()
for i in range(0, len(extraRows), 1):

    if ((not (extraRows[i][0] in brandsNameArray2)) & (int(extraRows[i][2]) > 20)):
        brandsNameArray2.append(extraRows[i][0])
       # countOfProducersMoreTwentyFive2.append(int(extraRows[i][2]))
        countUsedAidsTwOneYear2.append(float(extraRows[i][29]))


    if (not ((extraRows[i][23] == '') | (extraRows[i][24] == ''))):
        countUsedAidsTwentyYear2.append(float(extraRows[i][23]))
        countCreatedRecipesTwentyYear2.append(float(extraRows[i][24]))


    if (int(extraRows[i][2]) > 1):
        countTotalProducersMoreOne2.append(int(extraRows[i][2]))

print('Время во второй секции')
print(time.time()-et)


print(len(brandsNameArray))

plt.figure()

ax = plt.subplot()
ax.scatter(countCreatedRecipesTwentyYear, countUsedAidsTwentyYear)


plt.figure()
ac = plt.subplot()
#ac.pie(countOfProducersMoreTwentyFive, labels=brandsNameArray)
ac.pie(countUsedAidsTwOneYear, labels=brandsNameArray)


plt.figure()
ab = plt.subplot()
ab.hist(countTotalProducersMoreOne, max(countTotalProducersMoreOne)-1)


#print(countOfProducersMoreTwentyFive2[1])

if (len(extraRows) > 0):
    plt.figure()

    ax2 = plt.subplot()
    ax2.scatter(countCreatedRecipesTwentyYear2, countUsedAidsTwentyYear2)

    plt.figure()
    ac2 = plt.subplot()
    #ac2.pie(countOfProducersMoreTwentyFive2, labels=brandsNameArray2)
    ac2.pie(countUsedAidsTwOneYear2, labels=brandsNameArray2)

    plt.figure()
    ab2 = plt.subplot()
    ab2.hist(countTotalProducersMoreOne2, max(countTotalProducersMoreOne2)-1)


plt.show()
