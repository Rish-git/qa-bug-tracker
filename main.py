from functions import write_bug_log, read_bug_log, search_bug_log
while True: 
          print("\n=============================")
          print("     QA Bug Tracker v1.0")
          print("=============================")
          print("1. Log a new bug")
          print("2. View all bugs")
          print("3. Search bugs by keyword")
          print("4. Exit")
          print("=============================")
          choice=input("Enter the choice from the menu: ")

          if choice == "1":
               
               filename = input("Enter filename: ")
               bug_id = input("Enter Bug ID: ")
               severity = input("Enter Severity: ")
               status = input("Enter Status: ")
               write_bug_log(filename, bug_id, severity, status)

          elif choice == "2":

               read_bug_log('Rish.txt')
               
          elif choice == "3":
               print('welcome to the Bug search engine')
               filename = input("Enter filename: ")
               keyword = input("Enter keyword: ")
               search_bug_log(filename,keyword)


          elif choice == "4":
               print("Goodbye")
               break


          else:
               print ('Invalid slection please refer to the menu options listed below:')
               menu_options="""
               1. Log a new bug
               2. View all bugs        
               3. Search bugs by keyword
               4. Exit
               """
               print(menu_options)