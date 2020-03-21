def spam(number):
    '''Function should return something like this:
    spam(1);#bulochka
    spam(3);#bulochkabulochkabulochka
    But it is broken. Fix it please!

    Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    '''

    return 'bulochka'*int(number)


def my_sum(list_of_numbers):

    """Function receives a list with integer numbers,
    should return its sum as an integer. Do not use built in summarize functions.
    :param list

    Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
    Не использовать встроенные функции суммирования.
    
    """
    pass

    k = 0
    for i in range(0, len(list_of_numbers)):
        k = k + list_of_numbers[i]
    return k


def shortener(string):
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'


    """
    pass
    string1 = string.split()
    string2 =[]
    for i in string1:
        if len(i) > 6:
            i = i[:6]+'*'
            string2.append(i)
        else:
            string2.append(i)

    return ' '.join(string2)

#print(shortener('Function receives the longest string with many words.'))



def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    pass
    #  ...wite your code here
    k = 0
    for i in words:
        if len(i) > 1 and i[0] == i[len(i)-1]:
            k +=1
    return k

#words = ['Abba ra', 'dfg', 'kfd k','a', 'ad', 'aaaaa gfgfgfg aaa']
#print(compare_ends(words))

