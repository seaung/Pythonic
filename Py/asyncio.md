#### python asyncio
>

    1. event_loop事件循环：程序开启一个无限的循环，
       程序员会把一些函数注册到事件循环上，
       当满足事件发生的时候，调用相应的协程函数

    2. coroutine协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行
       而是会返回一个协程对象。协程对象需要注册到事件循化，由事件循环调用

    3. future：代表将来执行或没有执行的任务的结果，它和task没有本质区别

    4. async/await关键字：python3.5用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口

#### 定义一个协程
>
    定义一个协程很简单，使用async关键字，就像定义普通函数一样

    import time
    import asyncio

    now = lambda : time.time()

    async def do_some_work(x):
        print("Waiting : ", x)

    start = now()

    coroutine = do_some_work(2)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(coroutine)
    print("TIME : ", now() - start)

    result: Waiting :  2
            TIME:  0.0004658699035644531

    通过async关键字定义一个协程，协程也是一种对象，协程不能直接运行，
    需要把协程加入事件循环，由后者在适当的时候调用协程，asyncio.get_event_loop方法
    可以创建一个事件循环，然后使用run_until_complete将协程注册到事件循环，并启动事件循环
