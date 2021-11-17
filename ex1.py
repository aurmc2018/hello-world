bill = float(input("What is your bill amount?"))

tip = int(input("What is your tip%?"))

persons = int(input("How many persons?"))

bill_amount = bill + ((tip/100) * bill)

bill_amount_person = bill_amount/persons

final_amount = "{:.2f}".format(bill_amount_person)

print("Amount per sperson is computed as "+final_amount)




