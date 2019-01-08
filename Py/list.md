#### 列表数据类型


>

    列表包含多个字构成的序列

    术语”列表值“ 指的是列表本身(他作为一个值，可以保存在变量中，或传递给函数，像所有其他值一样)

    li = [1, 3, 4, 5, 6, 7]

    用下标取得列表中的单个值

    li[-1]

    li[:2]

    li[1:4]

    用len()取得列表的长度和用下标改变列表中的值

    length = len(li)

    li[2] = 223

    列表连接和列表复制和用del语句从列表中删除值

    使用 + 进行两个或多个列表的连接

    [1, 2, 3, 4, 5] + [6, 7, 8, 9]

    使用*进行列表的复制

    [1, 2, 3, 4, 5] * 2

    del语句将删除列表中下标处的值，表中被删除值后面的所有值，都将向前移动一个下标

    spam = [1, 3, 5, 7, 9]

    del spam[2]

    列表用于循环

    for i range(12):
        print(i)

    for i in [1, 2, 3, 4, 5, 6]:
        print(i)

    in 和 not in操作符，可以确定一个值是否在列表中

    "123" in [1, 3, 4, 5]

    1 not in [2, 3, 5, 5, 6]

    用index()方法在列表中查找值
       可以传入一个值，如果该值存在于列表中，就返回巴德下标

       spam = ["index", "foo", "bar"]

       spam.index("index")

       note: 如果列表中存在重复的值，就返回它第一次出现的下标

    用append()和insert()方法在列表中添加值
       append()方法将参数添加到列表末尾
       insert()方法可以在列表任意下标处插入一个值，
       insert()方法的第一个参数是新值的小标，第二个参数是要插入的新值

       spam = [1, 2, 3, 4]

       sapm.append(5)
       spam.insert(1, "spam")

    用remove()方法从列表中删除值
       给remove()方法传入一个值，他将从被调用的列表中删除

       spam = ["cat", "bat", "rat", "elephant"]

       spam.remove("cat")

       note：试图删除列表中不存在的值，将导致valueError错误

    用sort()方法将列表中的值排序

       spam = [1, 2, 3, 4, 5,332, 7, 0]

       spam.sort()

       span.sort(reverse=True)

       指定reverse关键字参数为True，让sort()按逆序排序


#### copy模块的copy()和deepcopy()函数

>

    在处理列表和字典时，尽管传递引用常常是最方便的方法，但是如果函数修改了传入的列表或者字典，
    你可能不希望这些变动影响原来的列表和字典

    import copy
    spam = ['a', 'ad', 'c', 'd']
    cheese = copy.copy(spam)

    cheese[1] = 'b'

    print(cheese)
    print(spam)

    copy()函数创建了第二个列表，能独立于第一个列表修改

    deepcopy()函数将同时复制他们内部的列表
