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

