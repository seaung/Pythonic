#### 列表


###### 使用[]或list()创建列表
>>>

   >>> empty_list = []
   >>> weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
   >>> big_birds = ['emu', 'ostrich', 'cassowary']
   >>> first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']

   >>> another_empty_list = list()
   >>> another_empty_list
   >>> []

   list是有序的，元素允许重复

###### 使用list()将其他数据类型转换成列表
>>>

    python的list()函数可以将其他数据类型转换成列表类型

    >>> list('cat')
    >>> ['c', 'a', 't']

    >>> a_tuple = ('ready', 'fire', 'aim')
    >>> list(a_tuple)

    >>> birthday = '1/6/1952'
    >>> birthday.split('/')
    >>> ['1', '6', '1952']

    >>> splitme = 'a/b/c//d///e'
    >>> splitme.split('/')
    >>> ['a', 'b', '', 'c', 'd', '', '', 'e']

    >>> splitme.split('//')
    >>> ['a/b', 'c/d', '/e']

###### 使用[offset]获取元素
>>>

    >>> marxes = ['groucho', 'chico', 'harpo']
    >>> marxes[0]
    >>> grouncho

    >>> marxes[-1]
    >>> harpo

###### 包含列表的列表
>>>

   >>> small_birds = ['hummingbird', 'finch']
   >>> extinct_birds = ['dodo', 'passenger pigeon', 'norwegian blue']
   >>> carol_birds = [3, 'french hens', 2, 'turtledoves']
   >>> all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
   >>> all_birds
   [['hummingbird', 'finch'], ['dodo', 'passenger pigeon', 'norwegian blue'], 'macaw', [3, 'french hens', 2, 'turtledoves']]

   >>> all_birds[1]
   ['dodo', 'passenger pigeon', 'norwegian blue']

###### 使用[offset]修改元素
>>>

    >>> marxes = ['groucho', 'chico', 'harpo']
    >>> marxes[2] = 'wanda'
    >>> marxes
    ['groucho', 'chico', 'wanda']

###### 指定范围并使用切片提取元素
>>>

    >>> marxes = ['groucho', 'chico', 'harpo']
    >>> marxes[0:2]
    ['groucho', 'chico']

    >>> marxes[::2]
    ['groucho', 'harpo']

    >>> marxes[::-2]
    ['harpo', 'groucho']

    >>> marxes[::-1]
    ['harpo', 'chico', 'groucho']

###### 使用append()添加元素至尾部
>>>

    >>> marxes.append('zeppo')
    >>> marxes
    ['groucho', 'chico', 'harpo', 'zeppo']

###### 使用extend()或+=合并列表
>>>

    >>> marxes = ['groucho', 'chico', 'harpo', 'zeppo']
    >>> others = ['gummo', 'karl']
    >>> marxes.extend(others)
    >>> marxes
    ['groucho', 'chico', 'harpo', 'zeppo', 'gummo', 'karl']

    >>> marxes += ['gummo', 'karl']
    >>> marxes
    ['groucho', 'chico', 'harpo', 'gummo', 'karl']

#### 使用insert()在指定位置插入元素
>>>

   >>> marxes.insert(3, 'gummo')
   >>> marxes
   ['groucho', 'chico', 'harpo', 'gummo', 'zeppo']
   >>> marxes.insert(10, 'karl')
   >>> marxes
   ['groucho', 'chico', 'harpo', 'gummo', 'zeppo', 'karl']

###### 使用del删除指定位置的元素
>>>>

    >>> del marxes[-1]
    >>> marxes
    ['groucho', 'chico', 'harpo', 'gummo', 'zeppo']

###### 使用remove()删除具有指定值的元素
>>>

    >>> marxes = ['groucho', 'chico', 'harpo', 'gummo', 'zeppo']
    >>> marxes.remove('gummo')
    >>> marxes
    ['groucho', 'chico', 'harpo', 'zeppo']

###### 使用pop()获取并删除指定位置的元素
>>>

    >>> marxes = ['groucho', 'chico', 'harpo', 'zeppo']
    >>> marxes.pop()
    'zeppo'
    >>> marxes
    ['groucho', 'chico', 'harpo']
    >>> marxes.pop(1)
    ['groucho', 'harpo']

###### 使用index()查询具有特定值的元素位置
>>>

    >>> marxes = ['groucho', 'chico', 'zeppo']
    >>> marxes.index('chico')
    1

###### 使用in判断值是否存在
>>>

    >>> marxes = ['groucho', 'chico', 'harpo', 'zeppo']
    >>> 'groucho' in marxes
    True
    >>> 'bob' in marxes
    False

###### 使用count()记录特定值出现的次数
>>>

    >>> marxes = ['groucho', 'chico', 'harpo']
    >>> marxes.count('harpo')
    1
    >>> marxes.count('bob')
    0

###### 使用join()转换为字符串
>>>

    marxes = ['groucho', 'chico', 'harpo']
    >>> ','.join(marxes)
    'groucho, chico, harpo'

###### 使用sort()重新排序元素
>>>

    1. 列表方法sort()会对源列表进行排序，改变源列表内容
    2. 通用函数sorted()则会返回排好序的列表副本，源列表内容不变

    note: 如果列表中的元素都是数字，他们会默认的排序成从小到大的升序
          如果元素都是字符串，则会按照字母表顺序排列

    >>> marxes = ['groucho', 'chico', 'harpo']
    >>> sorted_marxes = sorted(marxes)
    >>> sorted_marxes
    ['chico', 'groucho', 'harpo']

###### 使用len()获取长度
>>>

    >>> marxes = ['groucho', 'chico', 'harpo']
    >>> len(marxes)
    3

#### 元组


###### 使用()创建元组
>>>

    >>> empty_tuple = ()
    >>> empty_tuple
    ()

    note: 创建包含一个或多个元素的元组时，每一个元素后面都需要跟着一个逗号，即使只包含一个元素也不能省

    >>> one_marx = 'groucho',
    >>> one_marx
    ('groucho', )

###### 元组和列表
>>>

    在许多地方都可以用元组代替列表，但是元组的方法函数与列表相比要少一些
    元组没有append(),insert()等等，因为一旦创建便无法修改

    1. 元组占用的空间较小
    2. 不会意外修改ia元组的值
    3. 可以将元组作用于字典的键值
    4. 命名元组可以作为对象的替代
    5. 函数的参数是以元组的形式传递的

#### 字典
>>>>

    字典与列表类似，但其中元素的顺序无关紧要，因为它们不是通过像 0 或 1
    的偏移量访问的。取而代之,每个元素拥有与之对应的互不相同的键(key)
    ,需要通过键来访问元素。键通常是字符串,但它还可以是 Python 中其他任意的不可变类型:布尔型、
    整型、浮点型、元组、字符串,以及其他一些在后面的内容中会见到的类型。字典是可变
    的,因此你可以增加、删除或修改其中的键值对

###### 使用{}创建字典
>>>

    >>> empty_dict = {}
    >>> empty_dict
    {}

    >>> bierce = {"day": 'a period of twenty-four hours, mostly misspent'}

###### 使用dict()转换为字典
>>>

    >>> lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    >>> dict(lol)
    {'c': 'd', 'a': 'b', 'e': 'f'}

    >>> lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
    >>> dict(lot)
    {'c': 'd', 'a': 'b', 'e': 'f'}

    >>> tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
    >>> dict(tol)
    {'c': 'd', 'a': 'b', 'e': 'f'}

    >>> los = ['ab', 'cd', 'ef']
    >>> dict(los)
    {'c': 'd', 'a': 'b', 'e': 'f'}

###### 使用[key]添加或修改元素
>>>

    >>> python = {'chapman': 'graham', 'cleese': 'john', 'idle': 'eric'}

    >>> python['chapman'] = 'pycharm'

    >>> python['author'] = 'govaos'

###### 使用update()合并字典
>>>

    使用update()可以将一个字典的键值对复制到另一个字典中去

    note:如果待添加的字典与待扩充的字典包含同样的键，那么新归入的字典的值会取代原有的值

    >>> first = {'a': 1, 'b': 2}
    >>> second = {'b': 'platypus'}
    >>> first.update(second)
    {'b': 'platypus', 'a': 1}

###### 使用del删除具有指定键的元素
>>>

    >>> del pythons['marx']

###### 使用clear()删除所有元素
>>>

    使用clear()或者给字典变量重新赋值一个空字典({})可以将字典中所有元素删除

    >>> pythons.clear()
    >>> pythons
    {}
    >>> pythons = {}
    >>> pythons
    {}

###### 使用in判断是否存在
>>>

    判断某一个字典存在于一个字典中，可以使用in

    >>> 'chapman' in pythons
    True
    >>> 'tor' in pythons
    False

###### 使用[key]获取元素
>>>

    >>> pythons['cleese']
    'john'

###### 使用keys()获取所有键
>>>

   >>> signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
   >>> signals.keys()
   dict_keys(['green', 'yellow', 'red'])

###### 使用values()获取所有值
>>>

    >>> list(signals.values())
    ['go', 'smile for the camera', 'go faster']

###### 使用items()获取所有键值对
>>>

    >>> list(signals.items())
    [('green', 'go'), ('red', 'smile for the camera'), ('yellow', 'go faster')]

    每一个键值对以元组的形式返回,例如('green', 'go')

###### 使用=赋值，使用copy()复制
>>>

    >>> signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
    >>> save_signals - signals
    >>> signals['blue'] = 'confuse everyone'
    >>> save_signals
    {'blue': 'confuse everyone', 'green': 'go', 'red': 'smile for the camera', 'yellow': 'go faster'}

#### 集合
>>>

    集合就像舍弃了值,仅剩下键的字典一样。键与键之间也不允许重复。如果你仅仅想知道
    某一个元素是否存在而不关心其他的,使用集合是个非常好的选择。如果需要为键附加其
    他信息的话,建议使用字典

###### 使用set()见其他类型转换为集合
>>>

    >>> set('letters')
    {'l', 'e', 't', 'r', 's'}

    >>> set(['dasher', 'dancer', 'prancer', 'mason-dixon'])
    {'dasher', 'dancer', 'prancer', 'mason-dixon'}

    >>> set(('ummagumma', 'echoes', 'atom heart mother'))
    {'ummagumma', 'echoes', 'atom heart mother'}

    当字典作为参数传入set()函数时，只有键会被使用

    >>> set({'apple': 'red', 'orange': 'norwegian', 'cherry': 'red'})
    {'apple', 'orange', 'cherry'}

###### 使用in测试是否存在
>>>

   >>> 1 in set
