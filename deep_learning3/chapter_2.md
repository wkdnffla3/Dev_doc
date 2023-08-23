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