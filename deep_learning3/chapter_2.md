# 11. 가변 길이 인수(순전파 편)

    지금까지 우리는 함수에 입출력 변수가 하나씩인 경우만 생각했다.
    하지만 함수에 따라서 여러개의 변수를 입력받기도 한다.

![그림11-1](./img/그림%2011-1.png)

    출력이 여러개인 계산 그래프도 있다.
![그림11-2](./img/그림%2011-2.png)

이상을 고려하여 가변 길이 입출력을 처리할 수 있도록 확장하려 한다.

## 11.1 Function 클래스 수정

    가변 길이 입출력을 표현하려면 변수들을 리스트에 넣는것이 편리할 것 같다.




# 12. 가변길이 인수(개선편)

    Add 클래스를 사용하는 사람을 위한 개선
    Add 클래스를 구현하는 사람을 위한 개선


## 12.1 첫번째 개선 : 함수를 사용하기 쉽게

![그림12-1](./img/그림%2012-1.png)

    왼쪽에서는 인수를 리스트에 넣고 튜플로 반환한다
    오른쪽은 리스트나 튜플을 거치지 않고 인수와 결과를 주고받는다.

```python
    class Function:

        def __call__(self,*inputs):
            ---
            ---

            return outputs if len(outputs)>1 else outputs[0]

```
    함수의 입력부분에 * 을 붙혀서 가변 길이를 준다고 표시하고 반환할 크기가 1이면 그값만을 아니면 리스트를 반환하게 한다.

## 12.2 두번째 개선 : 함수를 구현하기 쉽도록

    Add 클래스를 구현하려면 왼쪽과 같이 짜야하지만 오른쪽으로도 변환을 할수있다.

![그림12-2](./img/그림%2012-2.png)

```python
    class Function:
        def __call__(self,*inputs):

            ---
            ---
            ys = self.forward(*xs)
            if not isinstance(ys,tuple):
                ys=(ys,)
```
    함수 입력 부분에 *를 붙혀 언팩 리스트 푸는것 을 진행
    튜플이 아닌경우 튜플로 변환

## 12.3 add 함수 구현

    구현을 진행하면 된다!


# 13 가변 길이 변수(역전파 편)

    순전파 다음은 역전파이니 역전파를 구현해본다!

## 13.1 가변 길이 인수에 대응한 Add 클래스의 역전파

![그림13-1](./img/그림%2013-1.png)

    그림을 보면 덧셈의 순전파는 입력이 2개 출력은 1개이다.
    이것은 역전파는 입력이 1개 출력이 2개 라는 뜻이다.

    덧셈의 역전파는 출력 쪽에서 전해지는 미분값에 1을 곱한 값이 입력 변수의 미분이다.
    즉 상류에서 흘러오는 미분을 그대로 보내는 것이다.

```python
    class Add(Function):
        def forward(self, x0, x1):
            y = x0 + x1
            return y

        def backward(self,gy):
            return gy, gy
```

## 13.2 Variable클래스 수정

```python
class Variable:
    ---
    ---
    ---

    x,y = f.input, f.output
    x.grad = f.backward(y.grad)
```

    위 클래스 정의에서는 함수의 입출력 갯수가 하나라고 생각했다.
    이부분을 여러개가 들어가도록 바꿔본다.

```python
class Variable:
    ---
    ---
    ---

    while funcs:
        f = funcs.pop()
        gys = [output.grad for output in f.outputs]
        gxs = f.backward(*gys)
        if not isinstance(gxs,tuple):
            gxs = (gxs,)

        for x, gx in zip(f.inpuits, gxs):
            x.grad = gx

            if x.creator is not None:
                funcs.append(x.creator)
```

    outputs에 담겨있는 미분값들을 리스트에 담고
    f의 역전파를 호출한다.
    gxs가 튜플이 아니면 튜플로 변환하고
    역전파로 전파되는 미분값을 인스턴스 변수 grad 에 저장한다.

## 13.3 Square 클래스 구현

    Square 클래스에서 수정할 곳은 한곳뿐이 없다.

```python
    class Square(Function):

        def backward(self,gy):
            x = self.inputs[0].data
```

    Function 클래스의 인스턴스 변수 이름이 단수형인 input에서 inputs로 바꼇다.

# 14. 같은 변수 반복 사용

    현재의 DeZero 에는 문제가 있다 같은 변수를 반복해서 사용할 경우 의도대로 동작하지 않을수 있다!

![그림14-1](./img/그림%2014-1.png)

```python
    x = Variable(np.array(3.0))
    y = add(x,x)

    print('y',y.data)

    y.backward()
    print('x.grad',x.grad)
```
    이걸 미분하면 2가 나와야 하지만 1이나온다 이 문제를 해결해 보자

```python


    class Variable:

        def backward(self):
            for x, gx in zip(f.input, gxs):
                xgrad = gx # 이게 실수이다.
```

    미분값이 그대로 덮어 씌워지기 때문에 그렇다.

![그림14-2](./img/그림%2014-2.png)


##  14.2 해결책

    해결책은 간단하다

```python

    if x.grad is None:
        x.grad = gx
    else:
        x.grad = x.grad + gx

```

    앞서 시행했던 코드를 다시 실행하면 2가 나오는 것을 보여준다.


## 14.3 미분값 재설정

    위의 변경으로 인해 다른 문제가 발생할수도 있다

``` python
    x = Variable(np.array(3.0))
    y = add(x,x)
    y.backward()
    print(x.grad)

    y = add(add(x,x),x)
    y.backward()
    print(x.grad)
```

    위의 코드를 계산하면 2.0 과 5.0이 나온다 이것은 variable 안의 x 를 재사용하기 때문이다. 따라서 Variable 안에 미분 값을 초기화 시켜주는 메서드를 추가한다.

``` python

    class Variable:

        def cleargrad(self):
            self.grad = None
```

    이상으로 단계를 마무리 한다.


# 15. 복잡한 계산 그래프(이론편)

    지금까지 우리는 아래의 그림처럼 한줄로 늘어선 계산 그래프를 다뤘다

![그림15-1](./img/그림%2015-1.png)

    그러나 계산이 이렇게 한줄로 될 필요는 없다.

![그림15-2](./img/그림%2015-2.png)

    이렇게도 만들수 있으나 우리의 DeZero는 이런 복잡한 연결의 역전파를 제대로 할수가 없다.

## 15.1 역전파의 올바른 순서

![그림15-3](./img/그림%2015-3.png)

    DeZero는 위 그림을 제대로 미분하지 못한다

![그림15-4](./img/그림%2015-4.png)

    위 그림처럼 역전파가 진행되야 한다.

## 15.2 현재의 DeZero

```python
class Variable:

    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)

        funcs = [self.creator]

        while funcs:
            f = funcs.pop()
            gys = [output.grad for output in f.outputs]
            gxs = f.backward(*gys)

            if not isinstance(gxs, tuple):
                gxs = (gxs,)

            for x,gx in zip(f.input, gxs):
                if x.grad is None:
                    x.grad = gx
                else:
                    x.grad = x.grad + gx

                if x. creator is not None:
                    func.append(x.creator)
```

    위의 코드대로라면 흐름은 다음과 같이 나타날 것입니다.

![그림15-5](./img/그림%2015-5.png)

    순서가 D C A B A 가 되버린다.
    C에서 바로 A로 이어지고 A의 역전파도 2번 일어나서 문제가된다.


![그림15-6](./img/그림%2015-6.png)

    가장먼저 func 리스트에 D가 추가되어 [D] 상태로 시작한다 여기서 D의 입력 변수 B,C가 추가된다.

![그림15-7](./img/그림%2015-7.png)

    다음 리스트인 C가 꺼내진다 그리고 A가 추가되어 리스트가 B,A가 되고 A가 꺼내지게 되는데 여기서 문제가 발생한다.
    B를 꺼내야 하는데 A를 꺼내게 된것

## 15.3 함수 우선순위

    funcs 리스트에는 다음에 처리할 함수들의 후보 들이있다.
    지금까지는 마지막 원소만 꺼냈지만 이젠 아니다
    따라서 함수에 우선순위를 줄 수 있어야 한다.

    해결방법으로는 계산 그래프를 분석 하여 알아내는 방법이 있다.
    ex) 위상정렬 알고리즘을 사용하면 연결 방법을 기초로 노드를 정렬 가능

    하지만 더 좋은 방법을 이미 알고있다.
    함수가 어떤 변수를 만들어내는가 하는 '창조자 - 피조물 관계' , '부모 자식 관계' 를 이미 알고있다.
    따라서 아래 그림처럼 변수의 세대를 기록할수 있다.

![그림15-8](./img/그림%2015-8.png)

# 16. 복잡한 계산 그래프(구현편)

    이번 단계에서는 15단계에서 설명한 이론을 코드로 구현한다.
    먼저 순전파 시'세대' 를 설정하는 부분부터 시작하겠습니다.
    그런 다음 역전파 시 최근 세대의 함수부터 꺼내도록 한다.
    이렇게 하면 복잡한 계산 그래프라도 올바른 순서로 역전파가 이루어 진다.

## 16.1 세대 추가.

    먼저 Variable 클래스와 Function 클래스에 인스턴스 변수 generation을 추가.

``` python
class Variable:
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError('{} is not supported'.format(type(data)))

        self.data = data
        self.grad = None
        self.creator = None
        self.generation = 0

    def set_creator(self, func):
        self.creator = func
        self.generation = func.generation + 1 # 세대 설정 부모 +1

```

    variable 클래스는 generation을 0으로 초기화하고
    set_creator 메서드가 부모 세대보다 1만큼 큰 값을 설정한다.

![그림16-1](./img/그림%2016-1.png)

    Function 클래스의 generation은 입력 변수와 같은 값으로 설정한다.

![그림16-2](./img/그림%2016-2.png)

```python
class Function:
    def __call__(self, *inputs):
        xs = [x.data for x in inputs]
        ys = self.forward(*xs)
        if not isinstance(ys, tuple):
            ys = (ys,)
        outputs = [Variable(as_array(y)) for y in ys]

        self.generation = max([x.generation for x in inputs])
        for output in outputs:
            output.set_creator(self)
        self.inputs = inputs
        self.outputs = outputs
        return outputs if len(outputs) > 1 else outputs[0]
```

## 16.2 세대 순으로 꺼내기

![그림16-3](./img/그림%2016-3.png)

    위의 그림을 기반으로 세대를 큰곳부터 꺼내면 됩니다.

## 16.3 Variable 클래스의 backward

```python
def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)

        funcs = []
        seen_set = set()

        def add_func(f):
            if f not in seen_set:
                funcs.append(f)
                seen_set.add(f)
                funcs.sort(key=lambda x: x.generation)

        add_func(self.creator)

        while funcs:
            f = funcs.pop()
            gys = [output.grad for output in f.outputs]
            gxs = f.backward(*gys)
            if not isinstance(gxs, tuple):
                gxs = (gxs,)

            for x, gx in zip(f.inputs, gxs):
                if x.grad is None:
                    x.grad = gx
                else:
                    x.grad = x.grad + gx

                if x.creator is not None:
                    add_func(x.creator)
```

    add_func 함수가 DeZero 함수 리스트를 세대 순으로 정렬한다.

## 16.4 동작확인

    이제 세대가 큰 함수를 꺼낼 수 있으니 그래프와 역전파도 올바른 순서로 진행이 가능할 것이다!

![그림16-4](./img/그림%2016-4.png)

```python
x = Variable(np.array(2.0))
a = square(x)
y = add(square(a), square(a))
y.backward()

print(y.data)
print(x.grad)
```


# 17 메모리 관리와 순환 참조

    DeZero는 교육적인 면을 중시해서 이해하기 쉽도록 제작
    따라서 성능은 다소 낮음
    따라서 성능을 개선 가능할 대체기술을 DeZero에 도입할 계획
    시작에 앞서 파이썬의 메모리 관리에 대해 알아본다

## 17.1 메모리 관리

    파이썬은 필요 없어진 객체를 메모리에서 자동으로 삭제한다.
    불필요한 객체는 파이썬 인터프리터가 제거
    코드를 제대로 작성하지 않으면 메모리 누수 메모리 부족등의 문제가 발생
    신경망에서는 큰데이터를 다루는 경우가 많아 메모리 관리가 필수이다.

    파이썬은 2가지의 메모리 관리 방식을 가지고 있다.
    1. 참조의 수를 세는 방법 (참조 카운트)
    2. 세대를 기준으로 쓸모없어진 객체를 회수하는 방법(GC)

## 17.2 참조 카운트 방식의 메모리 관리

    모든 객체는 참조 카운트가 0인 상태로 생성되고 다른 객체가 참조 할대마다 1씩 증가
    참조가 끊길 때마다 1씩 감소한다.

    ex)
    대입 연산자를 사용할때
    함수에 인수로 전달할 때
    컨테이너 타입 객체에 추가할때

```python
a=obj()
b=obj()
c=obj()

a.b = b
b.c = c

a=b=c=None
```

    a,b,c, 라는 객체를 생성하고 a가 b를 참조하고 b가 c를 참조한다

![그림17-1](./img/그림%2017-1.png)

    None을 할당하게 되면 a는 참조 하던 것이 없어져 0이 되고 b와 c는 1이 될것이다.
    a 는 0이 되어 삭제되고 b는 0 이될것이다 이것이 줄줄히 이어져 다 삭제가 된다.

    참조 카운트로 많은 메모리 관리 문제를 해결이 가능하나 순환 참조는 해결하지 못한다.

## 17.3 순환 참조

```python
a=obj()
b=obj()
c=obj()

a.b = b
b.c = c
c.a = a

a=b=c=None
```
![그림17-2](./img/그림%2017-2.png)

    a b c 3개의 객체가 원 모양을 이루며 서로를 참조하게 되는데 이게 순환 참조이다.

    3객체 의 참조카운트는 모두 1이지만 사용자는 이들 3개의 객체중 아무것에도 접근이 불가능하다.
    None을 하는 것으로는 순환 참조의 참조 카운트가 0이 되지 않는다.
    따라서 GC(세대별 가비지 컬렉션)가 등장하게 된다.

    gc는 참조 카운트보다 영리한 방법으로 불필요한 객체를 찾아낸다
    gc의 구조는 따로 알아본다.
    gc는 메모리가 부족해지는 시점에 파이썬 인터프리터에 의해 자동으로 호출

    DeZero에는 순환 참조가 존재한다.

![그림17-3](./img/그림%2017-3.png)
    
    이것은 파이썬 모듈인 weakref로 해결이 가능하다.


## 17.4 weakref 모듈

    파이썬에서는 weakref.ref함수를 사용하여 약한 참조를 만들수 있다.
    약한 참조란 다른 객체를 참조하되 참조 카운드트는 증가시키지 않는 기능이다.

    데이터엔 접근이 가능하지만 참조 카운트는 증가하지 않는다.

    이것을 DeZero에도 추가해 보자

```python
class Function:
    def __call__(self, *inputs):
        xs = [x.data for x in inputs]
        ys = self.forward(*xs)
        if not isinstance(ys, tuple):
            ys = (ys,)
        outputs = [Variable(as_array(y)) for y in ys]

        self.generation = max([x.generation for x in inputs])
        for output in outputs:
            output.set_creator(self)
        self.inputs = inputs
        self.outputs = [weakref.ref(output) for output in outputs]
        return outputs if len(outputs) > 1 else outputs[0]

    def forward(self, xs):
        raise NotImplementedError()

    def backward(self, gys):
        raise NotImplementedError()
``` 

    이와 같이 인스턴스 변수 self.outputs가 대상을 약한 참조로 가리키게 변경

## 17.5 동작확인

```python
for i in range(10):
    x = Variable(np.random.randn(10000))  # big data
    y = square(square(square(x)))
```

![그림17-5](./img/그림%2017-5.png)



    for 문을 이용해 다음 그림과 같이 복잡한 참조 구조를 만들어 내게 된다.
    for 문이 2번 반복될때 참조 카운트가 0이 된다.

# 18 메모리 절약 모드

    이전 단계에서는 파이썬의 메모리 관리 방식에 대해 알아 봤다 
    이번 단계에서는 DeZero의 메모리 사용을 개선할 수 있는 구조 두가지를 도입한다.
    첫번째는 역전파시 사용하는 메모리 양을 줄이는 방법으로 불필요한 미분 결과를 보관하지 않고 즉시 삭제한다.
    두번째는 역 전파가 필요없는 경우의 모드 를 제공하는 것이다.
    이 모드는 불필요한 계산을 생략한다.


## 18.1 필요없는 미분값 삭제

    우리는 중간변수의 미분값은 필요없다 따라서 지워준다.

```python
def backward(self, retain_grad=False):
        if self.grad is None:
            self.grad = np.ones_like(self.data)

            if not retain_grad:
                for y in f.outputs:
                    y().grad = None  # y is weakref
```

    메서드의 인수에 retain-grad를 추가 retain-greed가 true 이면 지금처럼 모든 변수가 저장
    false면 중간 변수의 모든 미분값을 None으로 재설정 한다.

## 18.2 Function 클래스 복습

    DeZero 에서 미분을 하려면 순전파를 수행한 뒤 역전파 해주면 된다.
    역전파 시에는 순전파의 계산 결과가 필요하기 때문에 순전파때 결괏값을 기억해 둔다.

    인스턴스 변수 input은 역전파 계산시 사용된다.

## 18.3 config 클래스를 활용한 모드 전환

    순전파만을 할 경우를 위한 개선을 DeZero에 추가한다
    우선 두가지 모드 역전파 활성 모드와 역전파 비활성 모드를 전환하는 구조가 필요하다.


```python
lass Function:
    def __call__(self, *inputs):
        xs = [x.data for x in inputs]
        ys = self.forward(*xs)
        if not isinstance(ys, tuple):
            ys = (ys,)
        outputs = [Variable(as_array(y)) for y in ys]

        if Config.enable_backprop:
            self.generation = max([x.generation for x in inputs])
            for output in outputs:
                output.set_creator(self)
            self.inputs = inputs
            self.outputs = [weakref.ref(output) for output in outputs]


```

## 18.4 모드 전환

    이상으로 역전파 활성 비활성을 구분 짓는 코드가 그려졌다.

## 18.5 with 문을 활용한 모드 전환

    파이썬에는 with이라고 하는 후처리를 자동으로 수행하고자 할 때 사용할 수 있는 구문이 있다. 
    대표적인 예로는 파일의 open과 colose 이다.

    with 에 들어갈때 파일이 열리고 블록을 빠져 나올때 닫힌다.
    이것을 이용해 with 블록에 들어갈 때의 전처리, 블록을 빠져나올때의 후처리로 나눌수 있다.


```python
with using_config('enable_backprop', False):
    x = Variable(np.array(2.0))
    y = square(x)

with no_grad():
    x = Variable(np.array(2.0))
    y = square(x)
```

    with문 안에서만 있으면 역전파 비활성화 모드가 된다.
    이제 with 문을 사용한 모드 전환을 구현해 보자

    


