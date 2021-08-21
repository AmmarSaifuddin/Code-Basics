# Define Function to calculate total expense.
Monthly_Expense=[2100,3500,3400]
def calculate(exp):
    total=0
    for i in exp:
        total = i + total
    return total

total_expense=calculate(Monthly_Expense)
print (total_expense)

# Define Function to sum 2 numbers.
def sum(a,b):
    sum=a+b
    print (sum)
sum(5,7)
