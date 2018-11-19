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
```

#### 列子

```
    class ListMeta(type):
		def __new__(cls, name, bases, attrs):
			attrs["add"] = lambda self. value:self.append(value)
			return type.__new__(cla, name, bases, attrs)

	class MyList(list, metaclass=ListMeta)
		pass
	
    l = MyList()
	l.add(1)
	// [1]
```
