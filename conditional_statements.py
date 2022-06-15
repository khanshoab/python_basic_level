# ################## CONDITIONAL STATEMENT ####################
# key points 1>if statement, 2>if else statement, 3>if elif else statement.

# ###################### IF STATEMENT ####################3

# for the check odd number.
a = int(input("please Enter the integer value:"))

if a != 0:
    print(a, "YES CORRECT THIS IS INTEGER VALUE")

# for the check even number.
b = int(input("please enter the only odd number::"))

if b % 2 != 0:
    print(b, "yes this is the even number")

# ######################## IF ELSE ######################

# for the check odd and even number.
a = int(input("please Enter the integer value:"))

if a % 2 == 0:
    print(a, "yes this is even number")
else:
    print(a, "it is not even number")

# for the check odd  number.
b = int(input("please enter the number::"))

if b % 2 != 0:
    print(b, "yes this is the odd number")
else:
    print(b, "it is not odd number")

# ###################### IF ELIF ELSE STATEMENT ####################

per = int(input("please enter the student marks::"))
if per == 32 or per <= 59:
    print(per, "Student is grade 'E' pass")
elif per == 60 or per <= 69:
    print(per, "Student is grade 'D' pass")
elif per == 70 or per <= 79:
    print(per, "Student is grade 'C' pass")
elif per == 80 or per <= 89:
    print(per, "Student is grade 'B' pass")
elif per == 90 or per <= 100:
    print(per, "Student is grade 'A' pass")
else:
    print(per, "Student is fail")
