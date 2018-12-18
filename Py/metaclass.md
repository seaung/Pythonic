#### Python Metaclass

```
    class Hello():
		    def say_hello(self, name="world"):
		        print("hello, %s" %name)

	hello = Hello()
	hello.say_hello()

	>>> hello world
```

#### 把上面代码进行改写

```
    def f(self, name="world"):
	    print("hello %s" %name)

	Hello = type('Hello', (object,), dict(say_hello=f))

	hello = Hello()
	hello.say_hello()

	//  hello world

  type()参数详解

  口诀：
       我是谁，我从哪里来，我要到哪里去

  1. 第一个参数: 我是谁。在这需要一个区分与其他一切的命名，上面的实例将命名为Hello

  2. 第二个参数： 我从哪里来，也就是父类，以上的实例的父类是object---python一种非常低级的类

  3. 第三个参数： 我要到哪里去，将需要调用的方法和属性包含到一个字典里，再作为参数传入
```

#### 使用元类编程

```
    class SayMetaclass(type):
		def __new__(cls, name, bases, attrs):
			attrs["say_"+name] = lambda self,value,saying=name:print(saying+","+value+"!")
			return type.__new__(cls, name, bases, attrs)

	class Hello(object, SayMetaclass):
		pass

	hello = Hello()
	hello.say_Hello("world")

	// hello world

  1. 元类使用type衍生而出的，所以父类需要传入type[道生一，所以一必须包含道]

  2. 元类的操作都在__new__中完成，它的第一个参数是将创建的类，之后的参数既是
     三大永恒的命题，我是谁，我从哪里来，我将到哪里去。他返回的对象也是三大永恒命题
```

#### 列子

```
    class ListMeta(type):
		def __new__(cls, name, bases, attrs):
			attrs["add"] = lambda self, value:self.append(value)
			return type.__new__(cls, name, bases, attrs)

	class MyList(list, metaclass=ListMeta)
		pass

    l = MyList()
	l.add(1)
	// [1]
```

#### 口诀
>>>

    道生一，一生二，而生三，三生万物

    1. 道既是type

    2. 一既是metaclass(元类，或者叫类生成器)

    3. 二既是class(类，或者叫实例生成器)

    4. 三既是instance(实例)

    5. 万物既是实例的各种属性与方法
