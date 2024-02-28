print(
    "Привет,напиши имя, фамилию, отчество и дата рождения для записи в мед-кабинет."
)
a = input("Нажмите ENTER для продолжения")
name = []
surname = []
patronymic = []
date_of_birth = []
name.append(input("Имя:"))
surname.append(input("Фамилия:"))
patronymic.append(input("Отчество:"))
date_of_birth.append(input("Дата рождения:"))
print(
    "Спасибо,нужен ли вывод информации? Если да напишите Да, Если нет напишите любое слово"
)
b = input()
if b == "Да":
  print(name[0]), print(surname[0]), print(patronymic[0]), print(
      date_of_birth[0])
if b != "Да":
  print("Спасибо")
input(
    "Нажмите любую клавишу для выхода"
)  #Данная строка ни на что не влияет, ни к чему не присоединена и не связана,нужна если вы открываете программу в Microsoft Terminale
exit(0)
