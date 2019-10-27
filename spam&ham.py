import csv, re
with open('spam.csv', newline='') as File:
    #spam, ham, spamham = 0, 0, 0
    reader = csv.reader(File)
    for x in reader:
        for c in str(x).split():
            txt = re.sub('[^A-Za-z0-9]+', '', c)
            if txt != '':
                print(txt.lower())
    '''for row in csv.reader(File):
        if row[0] == 'spam':
            spam += 1
        else:
            ham += 1
        spamham += 1
    print('spam =>', spam , '\nham =>', ham, '\nsum =>', spamham'''
    
