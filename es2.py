A = []
B = []
while True:
    a = input("inserire una parola,per stoppare scrivi 0.")
    if a == "0":
        break
    else:
        A.append(a)
        B.append(len(a))
print(A)
print(B)    
