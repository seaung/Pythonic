#### __future__模块
>

    1. absolute_import模块

       from __future__ import absolute_import

       在python2.4以前，默认是相对导入，程序会首先在当前目录下查找目标模块，
       如果赵不到才会去系统的默认目录中查找

    2. print_function模块

       在python2.x中print只是python2中的一个类似关键字一样存在的函数
       而在python3.x中print是一个打印函数

       print_function模块统一了print方法只能像函数一样调用

   3. unicode_literals模块

      在python中有些库的接口要求必须是str类型字符串，有些接口要求必须是unicode类型
      的字符串
      unicode_literals模块统一了将模块中显示出现的所有字符串转为unicode类型

   4. division模块

      在python2.x中除法有两种情况，如果整数相除结果热是整数，余数会被去掉
      这种除法叫地板除，想要做到整除，必须把其中的一个数变成浮点数

      而在python3.x中所有的除法都是精确除法

      想要在python2.x中直接使用python3.x的除法，就可以导入__future__模块的division
