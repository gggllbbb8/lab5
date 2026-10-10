n=int(input(Эвведите количество целых чисел N"))
print(f"введите {n} целх чисел")
numbers=[]
for _ in range(n):
    numbers.append(int(input))
negativ=[x for x in numbers if x<0]
pozitiv=[x for x in numbers if x>0]
if not negativ:
    print("нет отрицательных чисел")
elif not pozitiv:
    print("нет положительных чисел")
min_abs_negativ=min(negatiiv,key=abs)
min_pozitiv=min(pozitiv)
product=min_abs_negativ*min_pozitiv
print("-"*30)
print(f,"наим по модулю отриц элемент:"min_abs_negative)
print(f,"наим положительный элемент:"min_pozitiv)
print(f,"их произведение:"product)
