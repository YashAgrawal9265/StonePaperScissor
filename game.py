import random

def game(user,comp):
    if user == comp:
        return None
    elif user == 's':
        if comp == 'p':
            return False
        else:
            return True
    elif user == 'p':
        if comp == 's':
            return True
        else:
            return False
    elif user == 'x':
        if comp == 'p':
            return True
        else:
            return False


print('''======Welcome To The Stone,Paper,Scissor Game=======''')

while True:
    print('''Your choices are:\n 1)Stone\n 2)Paper\n 3)Scissor\n 4)Exit''')
    user = input('Enter your choice: ')

    if user == '1':
        user = 's'
    elif user == '2':
        user = 'p'
    elif user == '3':
        user = 'x' 
    elif user == '4':
        break
    else:
        print('Please enter valid choice')


    num = random.randint(1,3)
    if num == 1:
        comp = 's'
    elif num ==2:
        comp = 'p'
    else:
        comp = 'x'

    user = 's'
    message = game(user,comp)

    if message:
        if user == 's' and comp == 'x':
            print('******** You choose: Stone ********')
            print('******** Computer choose: Scissor ********')
        elif user == 'p' and comp == 's':
            print('******** You choose: Paper ********')
            print('******** Computer choose: Stone ********')
        else:
            print('******** You choose: Scissor ********')
            print('******** Computer choose: Paper ********')
        print('\n======== Congratulatin You Win ========')

    elif message == None:
        if user == 's' and comp == 's':
            print('******** You choose: Stone ********')
            print('******** Computer choose: Stone ********')
        elif user == 'x' and comp == 'x':
            print('******** You choose: Scissor ********')
            print('******** Computer choose: Scissor ********')
        else:
            print('******** You choose: Paper ********')
            print('******** Computer choose: Paper ********')
          
        print('\n======== Tie ========')
    else:
        if user == 's' and comp == 'p':
            print('******** You choose: Stone ********')
            print('******** Computer choose: Paper ********')
        elif user == 'p' and comp == 'x':
            print('******** You choose: Paper ********')
            print('******** Computer choose: Scissor********')
        else:
            print('******** You choose: Scissor ********')
            print('******** Computer choose: Stone ********')
        
        print('\n======== You Loose ========')


print('Thank you for playing this game')