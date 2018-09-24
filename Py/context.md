#### 上下文管理器

>
    写代码时，希望把一些操作放置到代码模块中，这样在代码块中执行时就可以保持
    某种运行状态，而离开代码块时就执行另外的一种操作，结束当前状态
    即上下文管理器的目的就是实现对象的使用范围，如果超出范围就采取处理

    需要实现
           __enter__和__exit__方法

           __enter__：负责进入代码块的准备工作， 进入时被调用

           __exit__： 负责执行代码离开的善后工作，离开被调用


```
    class TestManager(object):
        def __init__(self, text):
            self.text = text

        def __enter__(self):
            return self.text + "..."

        def __exit__(self, exc_type, exc_value, trace_back):
            self.text = self.text + "oooo"

    
    with TestManager("test") as tm:
        print(tm.text)
```