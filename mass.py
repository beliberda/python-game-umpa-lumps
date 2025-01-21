
listEnemy = ["Пупа","Лупа","За","Зарплатой", "Пришли"]
print("Последний элеменет",listEnemy[len(listEnemy) - 1])
print("Длина массива",len(listEnemy))

print(listEnemy[-1])


print(listEnemy)

listEnemy.append("Медведь")

print("После append",listEnemy)

listEnemy.insert(4, "Вставил элемент")
print("После insert",listEnemy)

listEnemy.pop(4)
print("После pop",listEnemy)

listEnemy.remove("Лупа")
print("После remove",listEnemy)

index = listEnemy.index("За")
print("Результат index",index)

count = listEnemy.count(20)
print("Результат count 20",count)

listEnemy.reverse()
print("После reverse",listEnemy)

listEnemy.sort(reverse=True)
print("После reverse",listEnemy)

# Создать список противников, в него добавить объекты класса, им задать свойства и т.д.