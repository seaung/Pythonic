#### 字符串操作

>

    字符串下标和切片

    字符串像列表一样，使用下标和切片

    spam = "hello world!"
    spam[0]

    字符串的in和not in操作符

    像列表一样，in和not in操作符也可以用于字符串
    用in或者not in连接两个字符串得到的表达式，将求值为布尔值True或False

    "hello" in "hello world"

    "hello," not in "hello world"

    有用的字符串方法

    upper()和lower()返回一个新的字符串，其中原字符串的所有字母都被相应的转换为大写或者小写。
    字符串中非字母字符保持不变

    note这些方法没有改变字符串本身，而是返回一个新字符串

    如果字符串至少有一个字母，并且所有字母都是大写或小写
    isupper()和islower()就会相应的返回布尔值True，否则该方法就返回False

    note: 因为upper()和lower()方法本身返回字符串，所以也可以在“那些”返回的字符串上继续调用字符串方法

    spam = "hello world"

    s = spam.upper().lower()

    print(s)

    isX字符串方法

    isalpha()返回True，如果字符串值包含字母，并且非空

    isalnum()返回True，如果字符串只包含字母和数字，并且非空

    isdecimal()返回True，如果字符串只包含数字字符，并且非空

    isspace()返回True，如果字符串只包含空格，制表符和换行，并且非空

    istitle()返回True，如果字符串仅包含大写字母开头，后面都是小写字母的单词

    字符串方法startswith()和endswith()

    返回True，如果他们所调用的字符串以该方法传入的字符串开始或结束，否则，方法返回False

    字符串方法join()和split()

    如果有一个字符串列表，需要将他们连接起来，成为一个单独的字符串，join()方法就很有用

    ",".join(["u", "json", "some"])

    split()方法他针对一个字符串调用，返回一个字符串列表

    "my name is seaung".split()

    用rjust(), ljust()和center()方法对齐文本

    rjust()和ljust()返回调用他们的字符串的填充版本，通过插入空格来对齐文本
    这两个方法的第一个参数是一个整数长度，用于对齐字符串

    "hello".rjust(10)

    "hello".ljust(10)

    这两个方法的第二个可选参数将指定一个填充字符

    "hello".rjust(12, "*")

    "hello".ljust(12, "=")

    center()方法是让文本居中

    "hello".center(23)

    "hello".center(12, "=")

    用strip(), rstrip()和lstrip()删除空白字符

    这些方法返回一个新的字符串
