# Богданов Алексей Максимович Ум-222
# Практическая работа 6. Вариант 4.
n = int(input("Введите кол-во элементов массива: "))
a = 0
arr=[]
max=0
pnomer=0 #Порядковый номер максимального элемента
clv = 0 #Кол-во нечетных элементов исходного массива
#Заполнение массива целыми числами
while a < n:
    string = "Введите " + str(a+1) + " элемент массива (целое число): "
    arr.append(int(input(string)))
    #Подсчет кол-ва нечетных элементов исходного массива
    if arr[a]%2!=0:
        clv+=1
    #Нахождение максимального эл-та в исходном массиве и запоминание его порядкового номера
    if max<arr[a]:
        max=arr[a]
        pnomer=a
    a+=1

print("Введённый массив:", arr)
print("Максимально число исходного массива:", max, "\nПорядковый номер максимального числа:",pnomer)

#Проверка на то, есть ли в исходном массиве нечетные числа
if clv == 0:
    print("В исходном массиве нет нечетных чисел!")
#Формирование и вывод массива с нечетными числами в обратном порядке
else:
    a = 0
    arr2 = []
    while a < n:
        if arr[a]%2!=0:
            arr2.append(arr[a])
        a+=1
    arr2.sort(reverse=True)
    print("Массив нечетных чисел, полученный из исходного массива(эл-ты выведены в порядке убывания):", arr2)


