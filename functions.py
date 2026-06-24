# Function 1
from datetime import date

def write_bug_log(filename, bug_id, severity, status):
    with open(filename,'a') as bl:
        today=date.today()

        bl.write(
             f'Date: {today} | '
             f'Bug ID: {bug_id} | '
             f'Severity: {severity} | '
             f'Status: {status}\n'
        )

        print("Bug logged success")



# Function 2
def read_bug_log(filename):
    with open(filename,'r') as rb:
        for index,line in enumerate(rb,start=1):
            if line.strip():
                print(f'{index}. {line}', end=' ')

# Function 3
def search_bug_log(filename, keyword):
    with open(filename,'r') as sd:
        print(f'Bugs containing : {keyword}\n')
        for line in sd:
            if keyword.lower() in line.lower():
                print(line, end=' ')