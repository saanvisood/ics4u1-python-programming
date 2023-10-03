# Exercise 1

grade9 = []
grade10 = []
grade11 = []
grade12 = []

def convertPascalCase(str):
    if str == None:
        return str
    
    return str.title()

def processStudents():

    students_file = open('all-students.txt', 'r')

    for line in students_file:
        record = line.strip().split('\t')
        name = convertPascalCase(record[1].lower()+' '+record[2].lower())

        if record[0] == '09':
            grade9.append(name)
        elif record[0] == '10':
            grade10.append(name)
        elif record[0] == '11':
            grade11.append(name)
        else:
            grade12.append(name)

    students_file.close()

    print (grade9)
    print (grade10)
    print (grade11)
    print (grade12)

processStudents()

# Exercise 2

yahoo = []
hotmail = []
gmail = []
hdsb = []

def processEmails():
    emails_file = open('email-addresses.txt', 'r')

    for line in emails_file:

        new_line= line.strip()

        if 'yahoo' in new_line:
            yahoo.append(new_line)
        elif 'hotmail' in new_line:
            hotmail.append(new_line)
        elif 'gmail' in new_line:
            gmail.append(new_line)
        elif 'hdsb' in new_line:
            hdsb.append(new_line)

    emails_file.close()

    print (yahoo)
    print (hotmail)
    print (gmail)
    print (hdsb)

processEmails()

# Exercise 3

def processContra():

    message = ''

    contra_file = open('contracrostipunctus.txt', 'r')

    for line in contra_file:
        delimeter = line.strip().split(': ')
        
        char_line = delimeter[1]

        message += (char_line[0])

    contra_file.close()

    print (message)

processContra()
