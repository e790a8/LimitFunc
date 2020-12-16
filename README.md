# LimitFunc：限制函数
Limit function args type

限制函数参数类型

# method of application：使用方法

annotation：The parameters are ordered in the default order

注：参数顺序按默认顺序

```python
from LimitFunc import limit_func
# No default values
# 没有默认值
@check_args(checks={'a': int, 'b': str})
def test(a, b):
    pass
```



```python
from LimitFunc import limit_func
# Have default values
# 有默认值
@check_args(checks={'a': int, 'b': str}, defaults={'b': 'test'})
def test(a, b):
    pass
```

