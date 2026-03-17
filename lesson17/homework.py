# Customer Due Amount Calculator

# Taking input from user
total_bill = float(input("Enter total bill amount: "))
amount_paid = float(input("Enter amount paid by customer: "))

# Calculating due or change
if amount_paid < total_bill:
    due = total_bill - amount_paid
    print("Customer still has to pay:", due)

elif amount_paid > total_bill:
    change = amount_paid - total_bill
    print("Return change to customer:", change)

else:
    print("Payment complete. No due amount.")