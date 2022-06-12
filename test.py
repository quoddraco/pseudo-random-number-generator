import psutil


def mixing(value,l): # Функция для переворачивания последовательности
                     # (123456 > 654321)
    w=value
    mat=[]

    for i in range(l+1):
        mat.append([0] * l)

    for i in range(l+1):
     mat[i] = w // 10 ** (l - i)
     w = w - ((w // 10 ** (l - i))*(10 ** (l - i)))

    k=0
    for i in range(l):
        k=k+(mat[l-i])*(10**(l-i-1))
    return k


def generator(seed,n):# Функция для генерации слч. послед.

    value = seed ** 10 # генерим seed
    print(len(str(value)))
    l=len(str(value))
    value=mixing(value,l)# Вызываем функцию
    cut1 = value
    # Режим value (достаём внутреннюю последовательность)
    cut2 = cut1 % 10**79
    print(len(str(cut2)))

    return cut2 # Возвращаем сгенерированное число (в последствии будущий seed)


def bits(seed):# переводим seed в двоичный код
    n = seed
    m = n
    p = 1
    d1 = 0
    while m > 0:
        d1 = d1 + m % 2 * p
        p = p * 10
        m = m // 2
    print("Двоичный код",d1)
    return d1
# Начало программы #
seed =psutil.virtual_memory()[3]# С помощью библиотеки (psutil) мы получаем
# число равное использующейся оперативной памяти в байтах
# Это число мы используем в качестве seed (начального значения)

print("Seed:",seed)
n=len(str(seed))*5
l=256*2
print("Количество наборов:",n)
listt = []
r=0
keys = []
for i in range(l):# Создаём массив, в котором будем хранить все "случайные последовательности"
                  # в двоичном виде
    listt.append([0] * l)

for i in range(l):# Создаём массив, в котором будем хранить все "случайные последовательности"
                  # в двоичном виде
    keys.append([0] * l)

for i in range(l):# Цикл для создания слч.послед. количеством(n)
    print("===================================")
    seed=generator(seed,n) # Вызываем функцию генерации
    print('Случайнная последовательность:',seed)
    listt[i]=bits(seed)# Вызываем функцию для перевода чисел в двоичную последовательность
    keys[i]=seed
    r+=1


print(r)
f = open('file.txt', 'wt')
for i in listt:# Здесь мы записываем все последовательности в txt
    s = str(i)
    i+=1
    f.write(s + '')
f.close()

q = open('keys.txt', 'wt')
for i in keys:
    s = str(i)
    i+=1
    q.write(s + '\n')
q.close()

