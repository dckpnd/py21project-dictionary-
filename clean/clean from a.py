import re

with open("slovar_new.txt", "r", encoding="utf-8") as file:
    data = file.read()
newnew_slovar = re.sub("a", "а" , data)

with open ('newnew_slovar.txt', 'w', encoding ='utf-8') as filik:
    for i in newnew_slovar:
        filik.write(i)