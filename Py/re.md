#### 正则表达式


>
    1. import re
    2. re.compile()创建正则表达式对象
    3. 向Regex对象的search()方法传入要匹配的字符串，它返回一个Math对象
    4. 调用Match对象的group()方法，返回实际匹配到的文本字符串


#### findall()方法


>

    1. 返回一组字符串，包含被查找字符串中的所有匹配
    2. findall()方法不是返回一个Match对象，而是返回一个字符串列表


#### 正则表达式符号


>

    ? 匹配零次或者一次前面的分组

    * 匹配零次或者多次前面的分组

    + 匹配一次或者多次前面的分组

    {n} 匹配n次前面的分组

    {n, } 匹配n次或者跟多前面的分组

    {, m} 匹配零次到m次前面的分组

    {n, m} 匹配至少n次，至多m次前面的分组

    {n, m}?或者*?或+？对前面的分组进行非贪心匹配

    ^spam意味着字符串必须以spam开始

    spam$意味着字符串必须以spam结束

    . 匹配所有字符，换行符除外

    \d, \d, \s 分别匹配数字，单词和空格

    \D, \W, \S 分别匹配数字，单词和空格之外的所有字符

    [abc]匹配方括号内的任意字符

    [^abc]匹配不在方括号内的任意字符串


#### 不区分大小写的匹配


>

   向re.compile()中传入第二个参数
   re.IGNORECASE或者re.I


#### 用sub()方法替换字符串


>

    sub()方法需要传入两个参数

    1. 字符串，用于取代发现的匹配
    2. 一个字符串，即正则表达式
    sub()方法返回替换完成后的字符串

    example:
        import re

        nameRegx = re.compile(r"Agent \w+")
        nameRegx.sub("GREETE", "Agent Alice gave")


#### 组合使用re.IGNORECASE,re.DOTALL和re.VERBOSE(忽略空白和注释)


>

    re.compile()只接受一个值作为他的第二个参数
    可以使用管道字符串将变量组合起来，从而绕过这个限制
