import json


filename = input("Enter the name of the json file with questions and answers: ")
grade=0
with open ("questions.json","r") as file:
   s=json.load(file)
name = input("Enter your name: ")
for i in range (1,21):
    user_answer = input( f" {i} : {s[str(i)][0]} : ")
    if user_answer == s[str(i)][1]:
        grade+=1
print(f"the deserved grade is {grade}")
try:
    with open('results.json', 'a', newline='') as file:
       file.write(user_answer+" : " + str(grade)+"/n")
except IOError:
    print("Error: Could not write to results.json file.")