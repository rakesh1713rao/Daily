# l = [1,2,3,4]

# number=input("Enter the number ")
# def rem(number):
#     try:
#         number = int(number)
#     except:
#         return "Enter a valid number"
#     if number not in l:
#         return "not found"
#     l.remove(number)
#     return l
    
# l2 =[]
# num=input("Enter the Number")


# def add(n):
#     try:
#         n=int(n)
#         return "Enter strings only"
#     except:
#         l2.append(n)
#         return l2
  

# var= add(num)
# print(var)



height = input("Enter you height:\n")
weight= input("Enter your weight:\n")

def bmi(h,w):
    bmi = int(w)/eval(h)**2
    return bmi

bodymass=bmi(height,weight)

print(round(bodymass))


print("Welcome to the tip calculator!")

bill_amount = float(input("Enter your bill amount $"))
tip = int(input("How much Tip you would like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill? "))

# total_bill_amt = bill_amount * (1 + tip / 100)
# per_person = total_bill_amt / people
# final_amt = round(per_person, 2)

# print(f"Each person should pay: $ {final_amt}")

def final_amt(b,t,p):
    total_bill_amt = b * (1+t/100)
    per_person = total_bill_amt / p
    final_amt = round(per_person,2)
    return f"Each person should pay: ${final_amt}"

ans=final_amt(bill_amount,tip,people)

print(ans)