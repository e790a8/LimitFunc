# LimitFunc：限制函数
> Limit function args type
>
> 限制函数参数类型
>
> 由于python为动态强类型语言，导致函数的参数可以传入任意类型，在大型复杂程序中，这可能引起一系列莫名其妙BUG；而typing的类型标注只能作为一个提示的作用，并不能阻止任意的传入，因此写了这个装饰器，用来限制传入参数的类型，如传入的参数类型与预设的不一致将会报错。
>
> 各位有任何建议或想法，欢迎共同完善此项目。



# Install

> 正常安装：
>
> pip install LimitFunc
>
> 国内安装（阿里源）：
>
> pip install LimitFunc -i https://mirrors.aliyun.com/pypi/simple



# Method of application：使用方法

> annotation：The parameters are ordered in the default order
>
> 注：参数顺序按默认顺序

```python
from LimitFunc import limit_func
# No default values
# 没有默认值
@limit_func(checks={'a': int, 'b': str})
def test(a, b):
    pass
```



```python
from LimitFunc import limit_func
# Have default values
# 有默认值
@limit_func(checks={'a': int, 'b': str}, defaults={'b': 'test'})
def test(a, b):
    pass
```

