#   제 1고지 미분 자동 계산

#   1. 상자로서의 변수

##  1.1 변수란

    상자에 데이터를 넣을때 상자를 변수라고 한다.

## 1.2 Variable 클래스 구현

    DeZero에서 사용하는 변수라는 개념을 Variable 이라는 이름의 클래스로 구현

    상자 안에 넣는 데이터로는 넘파이의 다차원 배열을 사용
    머신러닝 시스템은 기본 데이터 구조로 다차원 배열을 사용하기 때문에 Dezero의 Variable 클래스는 넘파이의 다차원 배열만 취급한다.
    이 책에서는 앞으로 numpy.ndarray 인스턴스를 단순히 ndarray 인스턴스라고 부른다.

## 1.3. 넘파이의 다차원 배열

    다차원 배열에서 원소에서 순서에는 방향이 있고 이 방향을 차원 혹은 축 이라고 한다.

![그림1-2](./img/그림%201-2.png)
    
    넘파이의 ndarray 인스턴스에는 ndim 이라는 인스턴스 변수가 있습니다.
    ndim은 number of dimenstions의 약자이다.

#   2. 변수를 낳는 함수

    
##  2.1 함수란

    함수는 입력한 변수를 다를 변수로의 대응 관계를 정한 것 이다.

![그림2-1](./img/그림%202-1.png)

##  2.2 Function 클래스 구현

    Function 클래스는 Variable 인스턴스를 입력받아 variable 인스턴스를 출력
    variable 인스턴스의 실제 데이터는 인스턴스 변수인 data에 있다.

## 2.3 Function 클래스 이용

    앞으로는 다양한 함수가 필요하다ㅡㄴ 점을 고려하면 Function 클래스는 기반 클래스로 두고 DeZero의 모든 함수가 공통적으로 제공하는 기능만 담아두는 것이 좋을거 같다.


#   3. 함수연결

    DeZero의 변수와 함수를 만들었다. 2단계에서 Square라는 제곱계산용 함수 클래스를 구현했다.

    이장에서는 다른 함수를 구현하고 여러 함수를 조합해 계산한다.

# 3.1 exp 함수 구현

    함수를 구현했다!

# 3.2 함수 연결

    DeZero 함수들을 연이어 사용이 가능하다.    

![그림3-1](./img/그림%203-1.png)


#   4.수치미분

    지금까지 Variable 클래스와 Function 클래스를 구현했다.
    미분을 자동으로 계산하기 위해서!
    수치 미분을 간단한 방법으로 계산해 본다.

##  4.1 미분이란

    미분은 간단히 말하면 변화율이다.

![식4-1](./img/식%204.1.png)
![그림4-1](./img/그림%204-1.png)

    h값을 한없이 0에 가깝게 줄여 x 의 변화 비율을 구하면 그게 미분 값이다.

## 4.2 수치 미분 구현

    컴퓨터는 극한을 취급할 수 없으니 h를 극한과 비슷한 값으로 대체한다.
    매우 작은값을 이용하여 미분 하는 것을 수치 미분이라고 한다.
    이에 오차가 생길수 밖에 없는데 이 근사 오차를 줄이는 방법으로 중앙 차분이 있다.
    중앙 차분은 f(x-h) 와 f(x+h)의 차이를 구한다.

![그림4-2](./img/그림%204-2.png)

    x 와 x+h 사이에서 기울기를 구하는 방법은 전진 차분 이라고 한다.
    중앙 차분 쪽이 오차가 작다.
    중앙 차분을 구현하는 함수를 numerical_diff(f, x, eps=1e-4)로 구현한다.
    f는 미분대상의 함수이며 Function 인스턴스 이다. 두번째 인수 x는 미분을 계산하는 변수, eps는 작은값을 나타낸다.

## 4.3 합성 함수의 미분

    코드로 작성했다.

## 4.4 수치 미분의 문제점

    수치 미분의 결과에는 오차가 포함되어있다. 계산에 따라 커질수도 있다.
    수치 미분의 문제는 계산량이 많다는 점이다. 따라서 역전파가 등장한다.
    역전파를 정확하게 구현했는지 확인하기 위해 수치미분 값을 이용한다. 이를 기울기 확인 gradient checking 이라고 한다.

# 5. 역전파 이론

    수치미분은 계산 비용과 정확도면에서 문제가 있다
    역전파가 구세주로 등장할 시점.
    역전파를 이용하면 미분을 효율적으로 계산 할 수있고 결괏값의 오차도 더 작다.

## 5.1 연쇄 법칙

    역전파를 이해하는 열쇠는 연쇄법칙 이다.
    합성 함수의 미분은 구성함수 각각을 미분한후 곱한것과 같다.

![그림5-1](./img/그림%205-1.png)

    x에 대한 y의 미분은 다음과 같다.

![식5-1](./img/식%205.1.png)

    각각 함수의 미분값을 모두 곱한것과 같다!

## 5.2 역전파 원리 도출

![식5-3](./img/식%205.3.png)
![그림5-2](./img/그림%205-2.png)
![그림5-3](./img/그림%205-3.png)
![그림5-4](./img/그림%205-4.png)

    y의 입력값에 대한 미분값이 전파된다!
    머신러닝은 주로 대량의 매개변수를 입력받아서 마지막에 손실함수를 거쳐 출력을 내는 형태로 진행
    손실 함수의 각 매개변수에 대한 미분을 졔산해야된다.

## 5.3 계산 그래프로 살펴보기

![그림5-5](./img/그림%205-5.png)

    역전파 시에는 순전파일때 사용한 데이터가 필요하다.
    따라서 순전파를 하고 앞의 데이터값들을 기억해야한다.

# 6. 수동 역전파

    Variable 과 Function 클래스를 확장하여 역전파를 이용한 미분을 구현

##   6.1 Variable 클래스 추가 구현

    미분 값을 저장하도록 구현

##  6.2 Function 클래스 추가 구현

    미분을 계산하는 역전파 backward 메서드 구현
    forward 메서드 호출 시 건네받은 Variable 인스턴스 유지

## 6.3 Square 와 Exp 클래스 추가 구현
    
    제곱과 exp를 계산할 클래스를 추가로 구현한다.

## 6.4 역전파 구현

![그림6-1](./img/그림%206-1.png)

    순전파를 보내고 역전파로 y를 미분한다.

![그림6-2](./img/그림%206-2.png)


# 7. 역전파 자동화

    이전 단계에서는 수동으로 조합해야 했다.
    이번 단계에서는 자동으로 시켜본다.

![그림7-1](./img/그림%207-1.png)

    일반적인 순전파를 한번만 하면 자동으로 역전파가 되게 만든다!

##  7.1 역전파 자동화의 시작

    함수 입장에서는 변수는 입력과 출력에 쓰인다
    변수 입장에서는 함수에 의해 만들어 진다.
![그림7-2](./img/그림%207-2.png)

    assert 부분에서 에러가 발생하는데 예제 코드를 그대로 가져다 쓰면 작동함 왜..?

![그림7-3](./img/그림%207-3.png)

    이렇게 보면 링크드 리스트 형태를 띄운다.

## 7.2 역전파 도전!

    단계별로 코드 구현!

    함수를 가져오고 함수의 입력을 가져온다 함수의 backward 메서드를 호출한다.
    함수를 가져온다.
    함수의 입력을 가져온다.
    함수의 backward 메서드를 호출한다.

## 7.3 backward 메서드 추가

    아까 보여준 코드에는 앞의 변수로 거슬러 올라가는 로직을 보여줬다.
    이제 자동화 해서 보여준다.

#   8. 재귀에서 반복문으로


## 8.1 현재의 Variable 클래스

    처리 효율을 개선하고 앞으로의 확장을 대비해 backward 메서드의 구현 방식을 바꿔본다.

    이전장에서 우리는 variable 클래스의 backward 메서드를 다음과 같이 구현했다.

```python
    class Variable:
        #생략

        def backward(self):
            f = self.creator
            if f is not None:
                x = f.input
                x.grad = f.backward(self.grad)
                x.backward()
```

    이부분에서 backward() 메서드를 계속해서 호출하는 재귀 형식이 계속 나온다.

## 8.2 반복문을 이용한 구현

    재귀를 사용한 구현을 반복문을 이용한 구현으로 바꿔본다.

``` python

    class Variable:


        def backward(self):
            funcs = [self.creator]

            while funcs:
                f = funcs.pop()
                x,y = f.input. f.output
                x.grad = f.backward(y.grad)

                if x.creator is not Non:
                    funcs.append(x.creator)
    
```

    반복문을 이용해 구현하였다.
    funcs 라는 리스트에 차례로 집어넣는다.

## 8.3 동작 확인

    코드는 잘 동작 한다.

# 9. 함수를 더 편리하게

    DeZero가 역전파를 할수 있게 되었다.
    Define by run 이라고 하는 전체 계산의 각 조각들을 런타임에 연결 해내는 능력도 갖췄다.
    하지만 사용하기 조금 불편한 부분이 있어서 이번 단계에서는 DeZero의 함수에 세가지 개선을 추가하겠습니다.

## 9.1 파이썬 함수로 이용하기

    지금까지 DeZero는 함수를 파이썬 클래스로 정의했지만 함수로도 정의가 가능하다.

```python
    def square(x):
        f = Square()
        return f(x)

    def exp(x):
        f = Exp()
        return f(x)
```
    혹은 다음과 같이 구현이 가능하다.

```python
    def square(x):
        return Square()(x)

    def exp(x):
        return Exp()(x)
```
    이렇게 구현을 했을때도 잘 동작을 한다.

## 9.2 backward 메서드 간소화

    역전파 시 사용자의 번거로움을 줄이기 위한 것이다.
    y.grad = np.array(1.0) 부분을 생략한다.
    이 코드를 생략할수 있도록 다음과 같이 코드를 추가한다

```python
    class Variable:

        def backwawrd(self):
            if self.grad is None:
                self.grad = np.ones_like(self.data)
```
    grad 값이 non이면 자동으로 미분값을 생성한다.
    이제 계산을 하고 난뒤 backward를 호출하는 것만으로 미분 값이 구해진다.

## 9.3 ndarray 만 취급하기

    ndarray인스턴스만 취급하게 다른 데이터형을 입력할 경우 에러가 출력하게 한다.

```python
    x = np.array(1.0)
    y = x ** 2
    print(type(x),x.ndim)
    print(type(y))
```
    위 코드는 numpy.float64나 numpy.float32등으로 달라진다
    따라서 np.isscalar함수를 사용한다. 스칼라인지 여부를 확인한후 as_array를 이용하여 ndarray 인스턴스로 변환해 준다.

# 10. 테스트

    소프트 웨어 개발에서는 테스트를 빼놓을수 없습니다.
    이번 단계에선 테스트 방법 특히 딥러닝 프레임 워크의 테스트 방법에 대해 설명 한다.

## 10.1 파이썬 단위 테스트

    파이썬으로 테스트할때는 표준 라이브러리에 포함된 unittest를 이용하면 편한다.
    여기에서는 이전 단계에서 구현한 square 함수를 테스트 해본다.

```python
class SquareTest(unittest.TestCase):
    def test_forward(self):
        x = Variable(np.array(2.0))
        y = square(x)
        expected = np.array(4.0)
        self.assertEqual(y.data, expected)
```
    unittest를 임포트 하고 unittest.TestCase를 상속한 SquareTest 클래스를 구현한다.
    테스트할 때는 이름이 test로 시작하는 메서드를 만들고 그 안에 테스트할 내용을 적는다.
    앞의 테스트는 square 함수의 출력이 기댓값과 같은지 확인한다.
    따라서 입력이 2.0일때 출력이 4.0이 맞는지 확인한다.

## 10.2 square 함수의 역전파 테스트

    방금 구현한 Square test 클래스에 다음 코드를 추가한다.

```python
    def test_backward(self):
        x = Variable(np.array(3.0))
        y = square(x)
        y.backward()
        expected = np.array(6.0)
        self.assertEqual(x.grad, expected)
```

    테스트를 돌려보면 결과가 일치하는지 확인합니다.

### 10.3 기울기 확인을 이용한 자동 테스트

    기울기 확인 이라는 방법을 이용하면 자동화가 가능하다.
    수치미분으로 구한 결과와 역전파로 구한 결과를 비교하여 그 차이가 크면 역전파 구현이 문제가 있다고 판단하는 검증 기법입니다.

```python
def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2 * eps)

    def test_gradient_check(self):
        x = Variable(np.random.rand(1))
        y = square(x)
        y.backward()
        num_grad = numerical_diff(square, x)
        flg = np.allclose(x.grad, num_grad)
        self.assertTrue(flg)
```

기울기 확인을 할때 무작위 입력값을 하나 생성하고 이를 역전파로 미분값을 구하고 numerical_diff 함수를 사용해서 수치 미분으로 계산해본다.
그리고 np.allclose(a,b)를 이용해 값이 가까운지 아닌지를 판단한다.
얼마나 가까운지에 대한 기준값은 rtol,atol로 정할수 있다.