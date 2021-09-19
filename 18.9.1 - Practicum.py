nums = None
n = None


def get_nums():
    try:
        global nums
        nums = list(map(int, str(input(f'Введите несколько чисел через пробел:\n')).split()))
        if nums == []:
            print('Вы ничего не ввели')
            get_nums()
    except ValueError:
        print('Это не число')
        get_nums()


def get_n():
    try:
        global n
        n = int(input(f'Введите дополнительное число:\n'))
    except ValueError:
        print('Это не число')
        get_n()

print('Программа ищет в списке чисел индекс числа, которое меньше дополнительного числа, а следующее за ним число больше или равно ему')
get_nums()
get_n()


def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


def binary_search(array, element, left, right):
    if left > right:
        return right
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


try:
    idn = binary_search(sort(nums), n, 1, len(sort(nums)) - 1)

    if sort(nums).count(n) == len(sort(nums)):
        print(f'В списке все числа равны дополнительному числу')
    elif n < sort(nums)[0]:
        print(f'Введённое число меньше самого маленького числа из списка: {sort(nums)[0]} (индекс: 0)')
    elif n > sort(nums)[-1]:
        print(f'Введённое число больше самого большого числа из списка: {sort(nums)[-1]} (индекс: {len(sort(nums)) - 1})')
    elif sort(nums).count(n) > 1:
        print(f'В списке есть несколько таких чисел: {sort(nums).count(n)}')
        if sort(nums).index(n) == 0:
            print(f'И они являются самыми маленькими в списке: индекс первого такого числа равен 0')
        else:
            if n == sort(nums)[-1]:
                print('И они являются самыми большими в списке')
            print(f'Индекс первого такого числа равен: {sort(nums).index(n)}')
            print(f'Число в списке, которое меньше введённого равно {sort(nums)[sort(nums).index(n) - 1]} (индекс {sort(nums).index(n) - 1})')
            print(f'А следующее число в списке равно {sort(nums)[sort(nums).index(n) + 1]} (индекс {sort(nums).index(n) + 1})')
    elif n == sort(nums)[0]:
        print(f'Введённое число является минимальным из списка, его индекс равен: {idn}')
    elif n == sort(nums)[-1]:
        print(f'Введённое число является максимальным из списка, его индекс равен: {idn}')
        print(f'Число в списке, которое меньше введённого равно {sort(nums)[idn - 1]} (индекс {idn - 1})')
    elif n == sort(nums)[idn]:
        print(f'Число {n} есть в списке, его индекс равен: {idn}')
        print(f'Число в списке, которое меньше введённого равно {sort(nums)[idn-1]} (индекс {idn-1})')
        print(f'А следующее число в списке равно {sort(nums)[idn + 1]} (индекс {idn + 1})')
    else:
        print(f'Число в списке, которое меньше введённого равно {sort(nums)[idn]} (индекс {idn})')
        print(f'А следующее число в списке равно {sort(nums)[idn + 1]} (индекс {idn + 1})')

except NameError:
    print('ошибка NameError')