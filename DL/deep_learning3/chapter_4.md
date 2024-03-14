# 34.  sin 함수 고차 미분

    이번 장에서는 sin 과 cos을 구현하고 고차원의 sin 함수를 미분해본다.


## 34.1 sin 함수 구녛ㄴ

```python
    class Sin(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        y = xp.sin(x)
        return y

    def backward(self, gy):
        x, = self.inputs
        gx = gy * cos(x)
        return gx


def sin(x):
    return Sin()(x)
```

    forward 안쪽의 변수들은 모두 ndarray
    backward 안쪽의 변수들은 Variable 이다
    따라서 backward를 쓸때는 무조건 Dezero 함수를 사용해야하고 함수가 없다면 구현해야한다.

    sin함수의 미분 값은 cos이기 때문에 backward에서는 cos 값이 필요하다


## 34.2 cos 함수 구현

    cos함수의 미분값은 -sin

```python
class Cos(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        y = xp.cos(x)
        return y

    def backward(self, gy):
        x, = self.inputs
        gx = gy * -sin(x)
        return gx


def cos(x):
    return Cos()(x)


```

    sin 과 비슷하게 굴러감


## 34.3  sin 함수 고차 미분

    sin 함수의 2차 3차 4차 미분도 계산

```python

import numpy as np
from dezero import Variable
import dezero.functions as F

x = Variable(np.array(1.0))
y = F.sin(x)
y.backward(create_graph=True)

for i in range(3):
    gx = x.grad
    x.cleargrad()
    gx.backward(create_graph=true)
    print(x.grad)
```

    결과값
    variable(-0.8414709848078965)
    variable(-0.5403023058681398)
    variable(0.8414709848078965)


----

    앞의 코드를 조금 확장하여 그래프로 그려본다

```python
import numpy as np
import matplotlib.pyplot as plt
from dezero import Variable
import dezero.functions as F

x = Variable(np.linspace(-7, 7, 200))
y = F.sin(x)
y.backward(create_graph=True)

logs = [y.data]

for i in range(3):
    logs.append(x.grad.data)
    gx = x.grad
    x.cleargrad()
    gx.backward(create_graph=True)

labels = ["y=sin(x)", "y'", "y''", "y'''"]
for i, v in enumerate(logs):
    plt.plot(x.data, logs[i], label=labels[i])
plt.legend(loc='lower right')
plt.show()
```

    이 그래프는 -7부터 7까지 사이를 200등분한 것을 x 축으로 나타낸다.

![그림34-1](./img/그림%2034-1.png)

    그래프들이 유사한것을 볼수 있다.
    sin() -> cos() -> -sin() -> -cos() -> sin()
    순으로 미분이 진행되서 유사하다.