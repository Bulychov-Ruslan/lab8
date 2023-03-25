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



#2esep
commentators = {}
while True:
    comments = input()
    if not comments:
        break
    name, comment = comments.split(': ')
    if name not in commentators:
        commentators[name] = 1
    else:
        commentators[name] += 1
print(len(commentators))


#4esep
n = int(input())
vacation_dict = {}
for i in range(n):
    name, day, month = input().split()
    if month not in vacation_dict:
        vacation_dict[month] = []
    vacation_dict[month].append(name)
requested_month = input()
if requested_month in vacation_dict:
    print(" ".join(vacation_dict[requested_month]))
else:
    print(" ")
