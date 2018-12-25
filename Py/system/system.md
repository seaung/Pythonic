#### 文件


###### 用open()创建文件
>>>

    >>> fout = open('oops.txt', 'wt')
    >>> print('oops i created a file.', file=fout)
    >>> fout.close()

###### 使用exists()检查文件是否存在
>>>

    >>> import os
    >>> os.path.exists('oops.txt')
    True
    >>> os.path.exists('./oops.txt')
    True
    >>> os.path.exists('waffles')
    False

###### 用isfile()检查是否为文件
>>>

    >>> name = 'oops.txt'
    >>> os.path.isfile(name)
    True

    判断是否为目录的方法

    >>> os.path.isdir(name)
    False

    判断是否为绝对路径

    >>> os.path.isabs(name)
    False

###### 用copy()复制文件
>>>

    copy()函数来自模块shutil

    >>> import shutil
    >>> shutil.copy('oops.txt', 'ohno.txt')

    shutil.move()函数会复制一个文件并删除原始文件

###### 用rename()重命名文件
>>>

    >>> import os
    >>> os.rename('ohno.txt', 'ohwell.txt')

###### 用link()或者symlink()创建链接
>>>

    >>> os.link('oops.txt', 'yikes.txt')
    >>> os.path.isfile('yikes.txt')
    True

###### 用chmod()修改权限
>>>

    os.chmod('oops.txt', 0o400)

###### 用chown()修改所有者
>>>

    os.chown('oops', uid, gid)

###### 用abspath()获取路径名
>>>

    >>> os.path.abspath('oops.txt')
    ‘/usr/gaberlunzie/oops.txt’

###### realpath()获取符号的路径名
>>>

    >>> os.path.realpath('jeepers.txt')
    '/usr/gaberlunzie/oops.txt'

###### 用remove()删除文件
>>>

    >>> os.remove('oops.txt')

#### 目录


###### 使用mkdir()创建目录
>>>

    >>> os.mkdir('poens')
    >>> os.path.exists('poens')

    True

###### 使用rmdir()删除目录
>>>

    >>> os.rmdir('poens')
    >>> os.path.exists('poens')
    False

###### 使用listdir()列出目录内容
>>>

    >>> os.listdir('poens')
    []

###### 使用chdir()修改当前目录
>>>

    >>> import os
    >>> os.chdir('opems')
    >>> os.listdir('.')
    ['mcintyre']

###### 使用glob()列出匹配文件
>>>

    note:glob()函数会使用unix shell的规则来匹配文件或者目录，而不是更复杂的正则表达式

    1. * 会匹配任意名称
    2. ? 会匹配一个字符
    3. [abc] 会匹配字符a，b和c
    4. [!abc] 会匹配除了a，b和c之外的所有字符

    >>> import glob
    >>> glob.glob('m*')
    ['mcintyre']
