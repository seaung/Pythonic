#### python 面向对象编程


>>>

    对象是代表现实世界中可以明确辨识的实体

    他可以是一个人，一张桌子，一只狗等

    一个对象有独特的特性，状态和行为

        1. 特性就像是人的身份号，python会在运行时自动对每个对象赋予一个独特的id来标识这个对象

        2. 对象的状态也称为属性或者特征使用变量表示，称之为数据域

        3. python使用方法来定义类的行为
    
    对象是类的一个实例，你可以创建一个类的多个对象

    创建类的一个实例的过程被称为实例化

    术语对象和实例经常是可以互换的，对象就是实例，而实例就是对象


#### 定义类

>>>
    除了使用变量存储数据域和定义方法，一个类还提供了一种特殊的方法: __init__

    这个方法被称为初始化程序，它是在创建和初始化这个新对象时被调用

    python 使用下面的语法定义一个类:
        class ClassName:
            initializer
            methods


#### 构造对象

>>>
    
    一旦定义了一个类，你就可以使用构造方法由类来创建对象，构造方法完成两个任务
    1. 在内存中为类创建一个对象

    2. 调用类的__init__方法初始化对象

    包括初始化程序的所有方法，都有第一个参数self.这个参数指向调用方法的对象

    __init__方法中的self参数被自动地设置为引用刚被创建的对象


#### 访问对象成员


>>>
    
    对象成员是指它的数据域和方法。数据域也称为实例变量
    因为每个对象(实例)调用来完成对象上的动作，例如，改变对象数据域中的值

    为了访问一个对象的数据域以及调用对象的方法，需要将对象赋给一个变量

    objectRefVar = ClassName(arguments)

    可以使用圆点运算符(.)访问对象的数据域并调用它的方法，它也被称为对象成员访问运算符

    objectRefVar.datafield
    objectRefVar.method(args)


#### self参数


>>>
    
    self是指向对象本身的参数。你可以使用self访问在类定义中的对象成员

    一旦一个实例变量被创建、那么它的作用于就是整个类