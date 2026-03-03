print("Bill Split Calculator")
bill = float(input("Enter the bill amount: $"))
tip = float(input("enter the tip percentage: $")) 
tip_amount = (tip/100)*bill
total = tip_amount + bill
people = int(input())
amount_per_person = total/people
print(f"Total (including tip): ${total}")
print(f"Each person pays: ${amount_per_person}")