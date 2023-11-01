# 58. 대표적인 CNN (VGG16)

- 이전 단계에서 구현한 Conv2d 계층과 Pooling 함수를 이용하여 유명한 모델인 VGG16을 구현하려 한다.

## 58.1 VGG16 구현

- VGG는 2014년 ILSVRC 대회에서 준우승한 모델이다.
- "Very deep convolutional networks for large-scale image recognition" 라는 논문에서는 계층 수에 따라 여러 종류의 모델을 제안하고 있다.
- 우리는 그중 하나인 VGG16 모델을 구현한다.


![pic58-1](./img/그림%2058-1.png)

- 위의 그림은 VGG16의 신경망 구성이다.
- ConV 레이어의 앞의 숫자는 커널 크기, 뒤의 숫자는 채널의 갯수 이다.
- pool/2 는 2*2 풀링을, Linear 4096은 출력 크기가 4096인 완전연결계층을 가리킨다.
- VGG16의 특징은 다음과 같다.
    * 3 * 3 합성곱층 사용(패딩은 1*1)
    * 함성 곱층의 채널 수는 풀링하면 2배로 증가
    * 완전연결계층에서는 드롭아웃 사용
    * 활성화 함수로 ReLU 사용

- 이 특징을 이용하여 코드로 구현하면 다음과 같이 나온다.
```python
    def __init__(self, pretrained=False):
        #출력 채널 수 만큼 지정
        super().__init__()
        self.conv1_1 = L.Conv2d(64, kernel_size=3, stride=1, pad=1)
        self.conv1_2 = L.Conv2d(64, kernel_size=3, stride=1, pad=1)
        self.conv2_1 = L.Conv2d(128, kernel_size=3, stride=1, pad=1)
        self.conv2_2 = L.Conv2d(128, kernel_size=3, stride=1, pad=1)
        self.conv3_1 = L.Conv2d(256, kernel_size=3, stride=1, pad=1)
        self.conv3_2 = L.Conv2d(256, kernel_size=3, stride=1, pad=1)
        self.conv3_3 = L.Conv2d(256, kernel_size=3, stride=1, pad=1)
        self.conv4_1 = L.Conv2d(512, kernel_size=3, stride=1, pad=1)
        self.conv4_2 = L.Conv2d(512, kernel_size=3, stride=1, pad=1)
        self.conv4_3 = L.Conv2d(512, kernel_size=3, stride=1, pad=1)
        self.conv5_1 = L.Conv2d(512, kernel_size=3, stride=1, pad=1)
        self.conv5_2 = L.Conv2d(512, kernel_size=3, stride=1, pad=1)
        self.conv5_3 = L.Conv2d(512, kernel_size=3, stride=1, pad=1)
        self.fc6 = L.Linear(4096) # 출력 크기만 지정
        self.fc7 = L.Linear(4096)
        self.fc8 = L.Linear(1000)

    def forward(self, x):
        x = F.relu(self.conv1_1(x))
        x = F.relu(self.conv1_2(x))
        x = F.pooling(x, 2, 2)
        x = F.relu(self.conv2_1(x))
        x = F.relu(self.conv2_2(x))
        x = F.pooling(x, 2, 2)
        x = F.relu(self.conv3_1(x))
        x = F.relu(self.conv3_2(x))
        x = F.relu(self.conv3_3(x))
        x = F.pooling(x, 2, 2)
        x = F.relu(self.conv4_1(x))
        x = F.relu(self.conv4_2(x))
        x = F.relu(self.conv4_3(x))
        x = F.pooling(x, 2, 2)
        x = F.relu(self.conv5_1(x))
        x = F.relu(self.conv5_2(x))
        x = F.relu(self.conv5_3(x))
        x = F.pooling(x, 2, 2)
        x = F.reshape(x, (x.shape[0], -1))#합성 곱층에서 완전 연결 계층으로 전환 하기위해 데이터의 형상  변환 4차원에서 2차원으로 변환
        x = F.dropout(F.relu(self.fc6(x)))
        x = F.dropout(F.relu(self.fc7(x)))
        x = self.fc8(x)
        return x
```

## 58.2 학습된 가중치 데이터

- VGG16은 이미지넷 이라고 하는 거대한 데이터셋으로 학습한다.
- 그리고 학습이 완료된 가중치 데이터가 공개되어있어 따로 학습을 진행하지 않아도 된다!!(해야 알겠죠?)
- 이번 절에서는 학습된 가중치 데이터를 읽어오는 기능을 VGG16 클래스에 추가한다.

```python
class VGG16(Model):
    WEIGHTS_PATH = 'https://github.com/koki0702/dezero-models/releases/download/v0.1/vgg16.npz'

    def __init__(self, pretrained=False):
        super().__init__()
```

- pretrained=False 를 True 로 바꾸면 가중치 파일을 받아 읽어올수 있다!
- 아래의 그림은 VGG16의 계산 그래프를 나타낸 것이다.
![pic58-2](./img/그림%2058-2.png)

## 58.3 학습된 VGG16 사용하기

```python

url = 'https://github.com/oreilly-japan/deep-learning-from-scratch-3/raw/images/zebra.jpg'
img_path = dezero.utils.get_file(url)
img = Image.open(img_path)
img.show()
```

- 위의 코드를 실행하면 얼룩말 이미지가 나온다

![Alt text](image-8.png)

- 이미지의 타입은 PIL.Image 즉 ndarray가 아니기 때문에 ndarray로 바꿔야 한다.
- 이때 preprocess를 사용한다.

![Alt text](image-9.png)

- 변환을 마쳤으면 다음의 코드로 학습을 진행한다
```python
if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from PIL import Image
import dezero
from dezero.models import VGG16



url = 'https://github.com/oreilly-japan/deep-learning-from-scratch-3/raw/images/zebra.jpg'
img_path = dezero.utils.get_file(url)
img = Image.open(img_path)

x = VGG16.preprocess(img)
x = x[np.newaxis]

model = VGG16(pretrained=True)
with dezero.test_mode():
    y = model(x)
predict_id = np.argmax(y.data)

model.plot(x, to_file='vgg.pdf')
labels = dezero.datasets.ImageNet.labels()
print(labels[predict_id])
```

- 실행 결과는 다음과 같이 잘 나온다.

![Alt text](image-10.png)


