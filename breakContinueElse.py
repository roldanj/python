# break
for number in range(1, 11):
    if number == 5:
        break
    else:
        print(number)

# continue print 1 - 10 and skip 5
for number in range(1, 11):
    if number == 5:
        continue
    else:
        print(number)

# Else with loop checks for break
for number in range(1, 11):
    if number == 15:
        break
    else:
        print(number)
else:
    print("All the numbers were printed without breaking the loop!")

for number in range(1, 11):
    if number == 5:
        break
    else:
        print(number)
else:
    print("All the numbers were printed without breaking the loop!")