# -------------------------------------1------------------------------------------
rivers = {
    "Ніл": "Египет",
    "Жайық": "Қазақстан",
    "Сырдария": "Қазақстан",
}

print(rivers)

river = input()
if river in rivers:
    print(f"{river} өзен {(rivers[river])} ағып өтеді")
else:
    print(f"{river} бұндай өзен жоқ")

new_country, new_river = input().split()
rivers.update({new_country: new_river})

print(rivers)