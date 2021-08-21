# exp = [2340, 2500, 2100, 3100, 2980]
# total=0
# for item in exp:
#     total = total + item
# print(total)

# exp = [2340, 2500, 2100, 3100, 2980]
# total=0
# for item in exp:
#     total=item+total
# print (total)

# for i in range(1,11):
#     print (i*i)

# exp = [2340, 2500, 2100, 3100, 2980]
# total=0
# for i in range(len(exp)):
#     total=total+exp[i]
#     print('Month', i+1,'=',exp[i] )
# print ('My total expense is ',total)

exp = [2340, 2500, 2100, 3100, 2980]
total=0
for i in range(len(exp)):
    print ('Month',i+1,'=',exp[i])
    total=exp[i]+total
print('Total Expense =',total)

# key_location='chair'
# locations=['garage','car','bedroom','chair','closet']
# for i in locations:
#     if i==key_location:
#         print ('The key is found in ',i)
#         break
#     else:
#         print('The key is not found in ',i)

key_location='chair'
locations=['garage','car','bedroom','chair','closet']
for i in locations:
    if i==key_location:
        print ('The key is found in ',i)
        break
    else:
        print ('The key is not found in ',i)

for i in range(1,11):
    if i%2==0:
        continue
    print(i*i)

i=1
while i<=5:
    print(i)
    i=i+1

# Vid 9 Exercise













