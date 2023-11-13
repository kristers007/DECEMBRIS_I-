lietotāja_skaitlis=input(input("Ievadiet skaitli: "))

summa=0

for i in range(1, lietotāja_skaitlis + 1):
    summa += i

print(f"Summa no 1 līdz {lietotāja_skaitlis} ir {summa}")