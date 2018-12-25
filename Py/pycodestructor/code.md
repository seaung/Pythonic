#### 使用#注释
>>>

    注释是程序中会被python解释器忽略的一段文本

###### 使用`\`连接
>>>

    >>> aplhabet = 'acffdfdsfsfsfs' + \
    ...             'jjsldfjlsdjfl' + \
    ...             'jsldjflsjlf'

###### 使用if，elif和else进行比较
>>>

    >>> disater = True
    >>> if disater:
    ...    print('woe!')
    ... else:
    ...    print('whee!')
    ...
    woe!
    >>>

###### 使用while进行循环
>>>

    >>> count = 1
    >>> while count <= 5"
    ...    print(count)
    ...    count += 1
    ...
    1
    2
    3
    4
    5
    >>>

###### 使用break跳出循环
>>>

    >>> while True:
    ...    stuff = input(':')
    ...    if stuff == 'q':
    ...        break
    ...    print(stuff.capitalize())
    : test
    Test
    : q
    >>>

###### 使用continue跳出循环开始
>>>

    >>> while True:
    ...     value = input('integer, please [q to quit]: ')
    ...     if value == 'q':
    ...         break
    ...     number = int(value)
    ...     if number % 2 == 0:
    ...         continue
    ...     print(number, 'squared is', number*number)
    integer, please [q to quit] : 1
    1 squared is 1
    integer, please [q to quit]: q
    >>>

###### 循环外使用else
>>>

    >>> numbers = [1, 3, 5]
    >>> position = 0
    >>> while position < len(numbers):
    ...     number = numbers[position]
    ...     if number % 2 == 0:
    ...         print('found even number', number)
    ...         break
    ...     position += 1
    ... else:
    ...     print('no even number found')
    ...
    no even number found

###### 使用for迭代
>>>>

     >>> rabbits = ['flopsy', 'mopsy', 'conttontail', 'peter']
     >>> current = 0
     >>> while current < len(rabbits):
     ...     print(rabbits[current])
     ...     current += 1
     ...
     flopsy
     mopsy
     conttontail
     peter

     >>> for rabbit ini rabbits:
     ...     print(rabbit)
     ...
     flopsy
     mopsy
     conttontail
     peter

###### 使用zip()并行迭代
>>>

    >>> days = ['monday', 'tuesday', 'wednesday']
    >>> fruits = ['banana', 'orange', 'peach']
    >>> drinks = []'coffee', 'tea', 'beer']
    >>> desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
    >>> for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    ....    print(day, drink, fruit, dessert)
    ....

###### 推导式


###### 列表推导
>>>

    [ expression for item in iterable ]

    >>> number_list = [number for number in range(1, 6)]
    >>> number_list
    [1, 2, 3, 4, 5]

    >>> a_list = [number for number in range(1,6) if number % 2 == 1]
    >>> a_list
    [1, 3, 5]

###### 字典推导
>>>

    { key_expression: value_expression for expression in iterable }

    >>> word = 'letters'
    >>> letter_counts = { letter: word.count(letter) for letter in word}
    >>> letter_counts
    {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

###### 集合推导
>>>

    { expression for expression in iterable }

    >>> a_set = { number for number in range(1, 6) if number % 3 == 1}
    >> a_set
    {1, 4}

###### 生成器推导
>>>

    >>> number_thing = (number for number in range(1, 6))
