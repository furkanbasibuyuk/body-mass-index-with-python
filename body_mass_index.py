print("""**************************

BODY MASS INDEX CALCULATOR

***************************
""")

user_Height = float(input("Please enter the height(m) : "))
user_Weight = float(input("Please enter the weight : "))

bmic = user_Weight / (user_Height ** 2)

if (bmic < 18.5):
    print(bmic,"U R SO SKINNNYYYYYYYY... l i k e  a  p a p e r . . .")
elif (bmic >= 18.5 and bmic < 25):
    print(bmic,"HIGH FIVE !!!!.. You are okayy..")
elif (bmic >= 25 and bmic < 30):
    print(bmic,"You are a little bit fat. If u do more workout, its gonna be fine for you")
else:
    print("You are too fat bitch. Even i couldnt find the answer. Get your ass up!!!!")
