
# This program is used to create users and assign taks to each user in a company

# Open file containing users and store in string variable users
# Import datetime module to keep track of deadlines and sys module to logout

from datetime import datetime



import sys




# Define separate functions to perform different aspects of the program

# Statistics function, outputs the total number of users in the system and total
# number of tasks assigned. Users assigned is equal to number of lines in, this
# dictionary is created to store values from task_overview and printed out to the
# the user when function 

def stats():
    
    document = open('task_overview.txt','r')
    

    task_stats_dict = {}

    for elements in document.readlines():
        lines = elements.strip().split(', ')
        task_stats_dict['Total tasks'] = lines[0]
        task_stats_dict['Total tasks completed'] = lines[1]
        task_stats_dict['Total tasks uncompleted'] = lines[2]
        task_stats_dict['Total tasks overdue'] = lines[3]
        task_stats_dict['Percentage incomplete'] = lines[4]
        task_stats_dict['Percentage overdue'] = lines[5]

        for k, v in task_stats_dict.items():
            print(k + ': ',v)
    document.close()
    admin_menu()
    return

# This function is for generating reports 

def reports():

    tasks = open('tasks.txt', 'r').readlines()

    task_detail = {}
    new_dict ={}
    index = 0

    for line in tasks:
        
        task_list = line.strip().split(", ")
        index += 1
        task_detail = {index:{}}
        task_number                            = index
        task_detail[index]["Assigned to"]      = task_list[0]
        task_detail[index]["Task name"]        = task_list[1]
        task_detail[index]["Task Description"] = task_list[2]
        task_detail[index]["Date assigned"]    = task_list[3]
        task_detail[index]["Due date"]         = task_list[4]
        task_detail[index]["Task Complete"]    = task_list[5]
        new_dict.update(task_detail)

    total_tasks = len(new_dict)
    completed   = 0
    overdue     = 0
    today       = datetime.today()
    
    for task in new_dict.values():
        
        if task['Task Complete'] == 'Yes':
            completed += 1
        
    total_incompl = total_tasks - completed
    perc_incom    = int((total_incompl/total_tasks)*100)

    for task in new_dict.values():
        due_date = task['Due date']
        task_due = datetime.strptime(due_date,'%d %b %Y' )

        if task_due < today:
            overdue += 1
            
    perc_overdue = int((overdue/total_tasks)*100)

    task_overview = open('task_overview.txt','w')
    task_overview.write(str(total_tasks) +', ' + str(completed) +', '+
                        str(total_incompl) + ', '+ str(overdue) + ', ' +
                        str(perc_incom) + ', ' + str(perc_overdue))
    task_overview.close()


    def user_stats():
        
        # This is the number of tasks assigned to a particular user,this checks how many times
        # the username appears in task_list by looping through all the tasks in task.txt
        # create dictionary with usernames as keys value associated with username key is
        # incremented by 1 each time condtions in loop is met for each user
        
        user_overview = open('user_overview.txt', 'w')
        users = open('user.txt', 'r')
        lines = users.readlines()
        num_users = len(lines)


        user_dict = dict()
        user_task_compl = dict()
        user_overdue = dict()

        for line in tasks:
        
            task_list = line.strip().split(", ")

            for person in task_list:
                if person == task_list[0]:

                    if person in user_dict :
                
                        user_dict[person] = user_dict[person] + 1
                    else:
                        user_dict[person] = 1

                    for key in user_dict.keys():
            
                         user_overview.write(str(key) + ', ' +  str(user_dict[key]) + ', ' +  str(user_dict[key]/total_tasks*100) + '\n')

                if person == task_list[0] and task_list[5] =='Yes':

                    if person in user_task_compl :
                
                        user_task_compl[person] = user_task_compl[person] + 1
                    else:
                        user_task_compl[person] = 1
                        
                    for k in user_task_compl.keys():
            
                       user_overview.write(str(k) + ', ' + str(user_task_compl[k]/user_dict[key]*100) + ', ' + str(100-(user_task_compl[k]/user_dict[key]*100)))
            

                if person == task_list[0] and task_list[5] =='No':
                    
                    if datetime.strptime(task_list[4],'%d %b %Y') < today:

                        if person in user_overdue :
                
                            user_overdue[person] = user_overdue[person] + 1
                        else:
                            user_overdue[person] = 1
           
        

      
            
        

# This is the number of tasks completed by the particular user,this checks
# for the username in task_list and if task has been marked complete in task.txt
#  i.e 'Yes' index[5] in line  and creates dictionary with usernames as keys
# value associated with username key is incremented by 1 each time condtions in loop is met
                

    
              
      # This is the number of tasks that are assigned to each particular user and are
# overdue, works similar to algorithm above with additional control statement which
# checks if task has been complete or not
                
                
            
                            
        
    
        #for k in user_overdue.keys():

            #user_overview.write(str(k) + ',' + str(user_overdue[k]/user_dict[key]*100))

                   
    user_stats()
    print('Your report has been generated!')
    admin_menu()

    return




    
# This menu is accesible to all other the users with control
# statements leading to different menu based on choice made by user
# each function is explained in relevant section.
    
def menu():
    
    print("Please selecet one of the following options")
    choice = input("a  -  add task \nva -  view all tasks \nvm -  view my tasks \ne  -  exit: ")

    if choice.lower()   == "a":
        add_task()
        
    elif choice.lower() == "va":
        view_all()
        
    elif choice.lower() == "vm":
        view_mine()
        
    elif choice.lower() == "e":
        out()
        print('You have been logged out')
    return

    
# This menu is only accesible to the user with username 'admin' with control
# statements leading to different menu based on choice made by user
# each function is explained in relevant section.

def admin_menu():
    print("Please selecet one of the following options")
    choice = input("r  -  register new user \na  -  add task \nva -  view all tasks \nvm -  view my tasks \ngr -  generate reports \nds -  display statistics \ne  -  exit: ")

    if choice.lower()   == "r":
        reg_user()
        
    elif choice.lower() == "a":
        add_task()
        
    elif choice.lower() == "va":
        view_all()
        
    elif choice.lower() == "vm":
        task_info()

    elif choice.lower()   == 'gr':
        reports()
        
    elif choice.lower() == "ds":
        stats()
          
    elif choice.lower() == "e":
        out()
    
        
# This function prints information about each task from the tasks.txt file
    
def task_info():
    tasks = open('tasks.txt', 'r+').read()
    lines = tasks.strip().split(", ")
    for i in lines:
        print(i)
    return


# This function gives information about tasks assigned to a particular user uses
# The details are stored in a dictionary where the task details are stored to



def view_mine():
    
    user_name_confirm = input("Enter user name: ")
    tasks = open('tasks.txt', 'r').readlines()

    task_detail = {}
    new_dict ={}
    index = 0

    for line in tasks:
        
        task_list = line.strip().split(", ")
        index += 1
        task_detail = {index:{}}
        task_number                            = index
        task_detail[index]["Assigned to"]      = task_list[0]
        task_detail[index]["Task name"]        = task_list[1]
        task_detail[index]["Task Description"] = task_list[2]
        task_detail[index]["Date assigned"]    = task_list[3]
        task_detail[index]["Due date"]         = task_list[4]
        task_detail[index]["Task Complete"]    = task_list[5]
        new_dict.update(task_detail)
        
        if user_name_confirm == task_list[0]:
            for numbers, headings in task_detail.items():
                print('Task number: ' + str(index))
                
                for key in headings: 
                    print( key + ':', headings[key])

  # This writes values in the task dictionary tasks.txt
    def rewrite_tasks():
            task_file = open('tasks.txt', 'w')
            for task in new_dict.values():
                for key, value in task.items():
                    task_file.write(str(value ) +', ')
                task_file.write('\n')
            task_file.close()
            
   # This algorithm allows user to change values in the dictionary, the due date
   # and the 'Task Complete'

    def edit_task():

        edit_task_ = input('What would you like to do? \ne - Edit Task \nm - Mark task as complete: ')

        if edit_task_ == 'm':
            
            task_num      = int(input('Enter task number: '))
            task_complete = input('Task complete? Yes/No: ')
            new_dict[task_num]['Task Complete'] = task_complete
            print('The completion has been updated')
            
        if edit_task_ == 'e':

            edit_type = input('1 - Edit user \n2 - Edit completion date: ')

            if edit_type == '1':
                
                task_num = int(input('Enter task number: '))
                change_user = input('Enter new user assigned to task: ')
                new_dict[task_num]['Assigned to'] = change_user

            elif edit_type == '2':
                
                task_num = int(input('Enter task number: '))
                
                if new_dict[task_num]['Task Complete'] == 'Yes':
                    print('Cannot edit task, already marked as completed')
                    view_mine_menu()
                    
                else:
                    new_due_date      = date(int(input('Enter year: ')), int(input('Enter month: ')),int(input('Enter day: ')))
                    new_dict[task_num]['Due date'] = new_due_date.strftime('%d %b %Y')
        rewrite_tasks()
                                 
    # This is menu function inside the view_mine which allows user to navigate around.
    
    def view_mine_menu():

        choice_ = int(input('\nWhat would you like to do next?: \n - Go to task (Enter number) \n - Return to main menu (Enter "-1"):'))

        if choice_      == -1 and user_name_confirm == 'admin':
            admin_menu()
            
        elif choice_    == -1:
            menu()

        else:
            
            for k, v in new_dict[choice_].items():
                print(k + ':', v)
            edit_task()

    view_mine_menu()
    return new_dict



# This function is used to add tasks by requesting inputs and saves them to
# tasks.txt

def add_task():
    
    task_assignee = input("Enter the name of user you want to assign a task to: ")
    task_title    = input("Enter the title of the task: ")
    task_descr    = input("Enter a description of the task: ")
    task_ass      = date.today()
    due_year      = int(input("Enter the year task is due: "))
    due_month     = int(input("Enter the month task is due: "))
    due_day       = int(input("Enter the day of the month the task is due: "))
    due_date      = date(due_year, due_month, due_day)
    task_compl    = "No"
    
    tasks = open('tasks.txt', 'a')
    tasks.write("\n" + task_assignee + ", " + task_title + ", " + task_descr + ", " + str(task_ass.strftime('%d-%b-%Y')) + ", "
                +  str(due_date.strftime('%d %b %Y')) + ", " +  task_compl)
    return

# This is the function that logs user out of the system

def out():
    sys.exit
    print("You have been logged out")
    return

    
# This function is used to register new users, which are then written to
# user.txt, the file is opened and bolean variable defined set to false

def reg_user():

    users  = open('user.txt', 'r').readlines()
    new_user_name = input("Enter a username: ")
    new_use = False

    while new_use == False:
        
        for i in users:
        
            l = i.strip().split(", ")

            if new_user_name in l:
    
                print("Username in use already, choose a new username")
                new_user_name = input("Enter a username: ")
                

            else:
                       
                new_user_pass = input("Enter a password: ")
                pass_confirm  = input("Please confirm Password: ")
                
            
            

                if pass_confirm == new_user_pass:
                    new_use == True
                    user = open('user.txt', 'a+')
                    user.write("\n" + new_user_name + ", " + new_user_pass)
                    print("New user registered")
                    user.close()
                    admin_menu()
                    return
    
                    

# This is a login function which checks credentials against usernames and
# passwords stored in user.txt, if user is admin, directed to admin menu
# otherwise user is directed to different menu
# A while loop is used to check login credentials with login_cred used as a
# boolean variable set to False, while loop runs until boolean variable is
# True, each line is manipulated using the split and strip funtion then stored
# as a list, 'l', with username at position l[0] and password at position l[1]
# elif statements used to direct user to the right menu based on credentials

def login():
    
    login_cred = False
    users    = open('user.txt', 'r').readlines()
    username = input("Please enter your useranme: ")
    password = input("Please enter your password: ")
   
    while login_cred == False:
        

        for i in users:

            l = i.strip().split(", ")
            
            if username == l[0] and password == l[1]:
                
                if username == "admin":
                    login_cred == True
                    print("Welcome Admin")
                    admin_menu()
                    return
                    
                elif username == l[0] and password == l[1]:
                    login_cred == True
                    print("Welcome")
                    menu()
                    return

        else:
            print("Username or password is incorrect!")
            username = input("Please enter your usernme: ")
            password = input("Please enter your password: ")
    return

# The calls the login function to start off the program
login()



    
        
        


        
   

  


    
    


