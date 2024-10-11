import random

def numbers():
    for i in range(5):
        operations = input("Select an operator: +, -, /, *")
        rand = random.randrange(-100,100,1) 
        rands = random.randrange(-100, 100, 1)
        answer = f"{rand}{operations}{rands}="
        print (answer)
        player = str(float(input()))
        answers = answer + player
        print (answers)
        
    count = 0
    for i in range(5):
        if "=" in answers:
            answers = answers.split("=")
            left = eval(answers[0]) 
            right = eval(answers[1])
        if left == right:
            count+=1 
            # print(count)
        #     print (f"You have {count} correct.")
        # else:
        #     print ("This is incorrect.")
    
    if count <=2:
        print(f"You have {count}. Do better!")
    elif count > 2:
        print(f"You have {count} and have done well. Keep going!")
     
    
print(numbers())

# def correct( workout):
#     if '=' in workout:
        

