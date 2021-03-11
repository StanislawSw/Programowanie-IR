m = float(input("podaj macę ciałą (w kilogramach)"))
w5
g = float(input("Podaj wzrost (w metrach)"))
print()
bmi = m / (w**2)
print(f"BMI = {bmi:.2f}")
if bmi < 18.5:
    print("Niedowaga")
elif bmi >= 18.5 and bmi < 25:
    print("Waga prawidłowa")
elif bmi >= 25 and bmi < 30:
    print("Nadwaga")
else:
    print("Otyłość")


