lietotaja_skaitlis = int(input("Ievadiet skaitli: "))

faktorials = 1

for i in range(1, lietotaja_skaitlis + 1):
    faktorials *= i

print(f"{lietotaja_skaitlis}! ir {faktorials}.")