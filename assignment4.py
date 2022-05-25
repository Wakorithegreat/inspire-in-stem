# write a program to withdraw ksh 25000 if account balance is between ksh 100000 to 200000 30% if account balance btw 500000and 1m above 1m deduct 15000
acc_bal = input("enter your account balance")

if(int(acc_bal) > 100000 and int(acc_bal) < 200000):
    acc_bal = int(acc_bal) - 25000
    print("we have deducted 25000")
elif(int(acc_bal) > 500000 and int(acc_bal) < 1000000):
         acc_bal = float(acc_bal) - (0.3* float(acc_bal))
         print("we have deducted 30 percent from your account")
elif(int(acc_bal) > 1000000):
     acc_bal = int(acc_bal) - 15000
     print("we have deducted 15000")
else:
    print("no deduction done")

       