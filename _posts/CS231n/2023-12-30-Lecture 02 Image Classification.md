---
layout: single
title: Lecture 02 Image Classification
categories: CS231
tag: [AI, ML,DL,CS231,CS231n]
---

# Lecture 02 Image Classification
**video**  
[Lecture 2 | Image Classification](https://www.youtube.com/watch?v=OoUX-nOEjG0&list=PLC1qU-LWwrF64f4QKQT-Vg5Wr4qEE1Zxk&index=2)  
**subtitle**  
[Lecture 2 Image Classification.ko.srt]({{{site.url}}}/attachment/CS231n/lecture02/Lecture_2___Image_Classification.ko.srt)  
**pdf**  
[cs231n_2017_lecture2.pdf]({{{site.url}}}/attachment\CS231n\lecture02\cs231n_2017_lecture2.pdf)  

---

# Image Classification

**Image Classification**을 한다고 하면 우선 이미지를 입력하고 시스템에는 미리 카테고리 집합을 정해둡니다. 컴퓨터가 해야 할 일은 이미지를 보고 어떤 카테고리에 이미지가 속하는 지를 고르는 것입니다.  우리는 이 작업을 아주 쉽게 할 수 있지만 기계에게는 정말 어려운 작업입니다.

![img1.png]({{site.url}}/images/CS231n/lecture02/img1.png){: .align-center}

 예를 들어 입력데이터로 고양이 사진이 한 장 주어지고 카테고리에는 개, 고양이,트럭, 비행기 등이 주어졌다고 합시다. 컴퓨터가 해야할 일은 고양이 사진을 보고 주어진 카테고리 내에서 고양이를 찾는 것이  될 것입니다.  앞서 말했듯이 이는 우리에게는 아주 쉬운 작업이지만 컴퓨터에게는 어려운 작업입니다.  지금부터 이 작업이 왜 컴퓨터에게는 어려운 작업인지에 대해 알아보겠습니다. 

## The Problem and Challenges

### Semantic Gap

![img2.png]({{site.url}}/images/CS231n/lecture02/img2.png){: .align-center}

우선, 컴퓨터가 입력으로 받은 고양이 이미지를 어떻게 인식하는지를 알아봅시다. 컴퓨터는 이미지를 아주 큰 격자 모양의 숫자 집합으로 인식합니다. 그리고 각 픽셀은 세 개의 숫자로 표현되며 숫자 각각은 red, green, blue를 의미합니다. 이처럼 컴퓨터에게 이미지는 단지 거대한 숫자집합에 불과하기 때문에 고양이 이미지를 인식하는 것은 상당히 어려운 일입니다. <span style="background-color:#fff5b1">**“고양이”라는 레이블은 우리가 이 이미지에 붙힌 의미상의 레이블이고 이는 이 이미지가 고양이 사진이라는 사실과 실제 컴퓨터가 보는 픽셀 값과는 큰 차이가 있습니다.**<\span>  

이것을 **Semantic gap( 의미론적의 차이)**라고 합니다. 

### Viewpoint variation and Illumination

![img3.png]({{site.url}}/images/CS231n/lecture02/img3.png){: .align-center}

![img4.png]({{site.url}}/images/CS231n/lecture02/img4.png){: .align-center}

컴퓨터는 픽셀 값을 통해 이미지를 인식합니다. 그러나 주어진 이미지에 아주 미묘한 변화만 발생한다더라고 픽셀을 값들은 모두 변하게 됩니다. 예를 들어, 카메라 각도를 조금만 변하게 해도 모든 픽셀의 값들은 변할 것입니다. 하지만, 이 경우 픽셀 값이이 바뀌더라도 위 이미지가 고양이라는 사실은 변치 않습니다. 

**View point**뿐만 아니라 i**llumination**(조명) 또한 문제가 될 수도 있습니다. 어떤 장면이냐에 따라 조명은 각양각색일텐데 고양이가 어두운 곳에 있던 밝은 곳에 있던 고양이는 고양이입니다. 이처럼,  **ViewPoint**나 **illumination**가 달라지는 경우도 고려하여 컴퓨터가 이미지를 인식할 수 있어야 할 것입니다.  

### Deformation, Occlusion and Background Clustter

![img5.png]({{site.url}}/images/CS231n/lecture02/img5.png){: .align-center}

![img6.png]({{site.url}}/images/CS231n/lecture02/img6.png){: .align-center}

![img7.png]({{site.url}}/images/CS231n/lecture02/img7.png){: .align-center}

또한, **Deforamtion**(객체 자체의 변화)이 있을 수도 있고 **Occlusion**(가려짐)도 있을 수 있고, **Background clutter**(배경과 비슷한 경우)도 있을 수 있습니다.

고양이의 모습이 변하거나, 고양이가 소파속에 숨어서 꼬리만 보인다던가, 고양이가 배경가 유사하게 생겼어도 고양이란 사실은 변치 않습니다. 

즉, 이러한 경우도 고려하여 컴퓨터가 이미지를 인식 할 수 있어야 할 것 입니다.

### polymorphism

![img8.png]({{site.url}}/images/CS231n/lecture02/img8.png){: .align-center}

마지막으로 하나의 클래스 내에서도 다양한 형태를 지닐 수 있는 **polymorphism(**다형성)을 고려해야 합니다.

“고양이”라는 하나의 개념으로 모든 고양이에 대한 다형성을 전부 소화해내야 합니다. 고양이에 따라 생김새, 크기, 색, 나이가 각양 각색이지만 모두 고양이에 속한다는 것은 변치 않습니다.

따라서,  **polymorphism**도 고려하여  컴퓨터가 이미지를 인식 할 수 있어야 할 것 입니다.

### Conclusion

앞서 살펴본 문제들 뿐만 아니라 컴퓨터가 이미지를 인식하기 위해 해결해야할 문제는 아주 많습니다. 컴퓨터가 이미지를 인식하기 위한 알고리즘을 작성하기 위해서는 이러한 모든 문제들을 고려해야하며 이는 매우 어려운 작업입니다.

하지만, 만약 일부 제한된 상황을 가정한다면 잘 동작하며 인간의 정확도와 유사한 수준의 정확도를 보여주는 프로그램은 존재할 수 있습니다. 앞으로 어떤 요소들이 이러한 것을 가능하게 했는지 살펴보도록 겠습니다.

---

## An image classifier

만약 아래와 같은 Image Classfier API 코드를 작성한다고 생각해봅시다.

```python
def classify_image(imaage):
	# Some magic here?
  return class_label
```

위 코드는 이미지를 입력받고 어떤 놀라운 마법이 일어나고 이 이미지가 어디에 속하는지 분별해줍니다. 하지만 실제로 동작하는 Image Classfier를 구현하는 것은 정말 어려운 일입니다.  숫자 정렬이나 그래프 탐색과 같은 문제는 필요한 알고리즘을 이용하여 해결할 수 있습니다. 그러나, Image Classfier의 경우 직관적이고 명시적인 알고리즘이 존재하지 않습니다. 

### Attempts have been made

지금까지 사람들은 동물들을 인식하기 위해 high-end coded rules를 만들려는 명시적인 시도를 해왔습니다. 

 

![img9.png]({{site.url}}/images/CS231n/lecture02/img9.png){: .align-center}

고양이 인식을 예로 들어 앞서 언급한 시도를 살펴보겠습니다. 우리는 고양이는 두 개의 귀와 하나의 코가 있다는 것을 알고 있습니다. 또한,  Hubel과 Wiesel의 연구 덕분에 Eedges가 대단히 중요하다는 것도 알고 있습니다. 이를 이용하여 “명시적 규칙 집합”을 써내려가면 다음과 같이 쓸 수 있을 것입니다. 우선 이미지에서 edges를 계산합니다.그리고 다양한 Corners와 Edges를 각 카테고리로 분류합니다.가령 세 개의 선이 만나는 지점이면 corner라고 했을 때 오른쪽 귀에도  corner가 있고 왼쪽 귀에도  corner가 있고 이외에도 많은 corner가 있습니다. 하지만 이와 같은 방식으로 고양이를 인식하고자 하면 잘 동작하지 않습니다. **`첫 번째 문제는 이와 같은 알고리즘은 앞서 말한 문제들을 해결하지 못한다`**는 것입니다. **`두 번째는 확장성이 없는 방법이라는 것`**입니다.  만약 트럭이나, 개와 같은 다른 객체를 인식해야 한다면  별도로 새로운 명시적 규칙 집합을 작성해야할 것입니다.

객체 인식을 위해서는 이 세상에 존재하는 다양한 객체들에게 유연하게 적용가능한 확장성 있는 알고리즘을 만들어야 합니다. 이를 가능하게 하는 Insight 중 하나는 **Data-Driven Approch(데이터 중심 접근법)** 입니다.

### Data-Driven Approch

Data-Driven Approch에서는 직접 규칙을 정하는 대신 **`많은 양의 데이터를 수집`**합니다. 이를 이용하여 image dataset과 labels datasets을 만듭니다. 다음으로, 앞서 모은  image dataset과 labels datasets를 활용하여 **`Machine Learning을 진행하여 classifier을 학습`**시킵니다. 마지막으로 **`new images에 대해 classifier를 평가`**합니다. 

![img10.png]({{site.url}}/images/CS231n/lecture02/img10.png){: .align-center}

이제 Image Classifier API를 만들기 위해서는 함수가 하나가 아니라  2개가 필요합니다.

첫 번째는 **train함수**로 **입력은 image와 label**이고 **출력은 학습된 model**입니다.

```python
def train(images, labels):
	# Meachine learning!
	return model
```

두 번쨰는 **predict 함수**로 **입력은 model**이고 **출력은 image의 예측값**입니다. 

```python
def predict(model, test_images):
	# Use model to predict labels
	return test_labels
```

이 두 함수는 Meachine Learning의 key insight이며 지난 10-20년간 아주 잘 작동해왔습니다.

### Neareset Neighbor

더 복잡한 알고리즘을 다루기 전에 조금 더 단순한 Classifier를 살펴보겠습니다.

Nearsest Neighbor(NN)은 아주 단순한 Classifier입니다. 

```python
def train(images, labels):
	# Meachine learning!
	return model
```

train step에서는 모든 데이터와 라벨은 기억합니다.

```python
def predict(model, test_images):
	# Use model to predict labels
	return test_labels
```

predict step에서는 새로운 이미지가 들어오면 새로운 이미지과 기존의 학습 데이터를 비교해서 가장 유사한 이미지로 label을 예측합니다.

NN은 아주 단순한 알고리즘이지만 Data-driven Approch를 활용한 아주 좋은 알고리즘입니다.

![img11.png]({{site.url}}/images/CS231n/lecture02/img10.png){: .align-center}

CIFAR-10을 data set으로 이용한  NN예제를 살펴보겠습니다. 아래 그림의 맨 왼쪽 열은
CIFAR-10 테스트 이미지입니다. 그리고 오른쪽 방향으로는 학습 이미지 중 테스트 이미지와 유사한 순으로 정렬했습니다.  테스트 이미지와 학습 이미지를 비교해 보면, 눈으로 보기에는 상당히 비슷해 보이나 항상 맞는 것은 아님을 알 수 있니다.

![img12.png]({{site.url}}/images/CS231n/lecture02/img12.png){: .align-center}

두 번째 행의 이미지는 개입니다. 그리고 가장 유사하다고 판별된 이미지도 개입니다. 하지만 두 번쨰, 세 번째로 유사하다고 판별된 이미지를 살펴보면 사슴이나 말같아 보이는 이미지들도 보입니다. 개는 아니지만 “중간에 흰색 물체가 있다” 등의 특징이 육안으로 보기에는 test image와 매우 유사해 보입니다. 

이처럼 NN을 적용하면 train set에서 가장 가까운 샘플을 찾게 됩니다. 그렇게 찾은 가까운 샘플의 label을 알 수 있고 이를 통해 test set의 label을 예측합니다.

### Distance Metric to compare images

test image를 train image와 비교할 때 어떤 방식을 사용할 지가 중요합니다. 정확히 말하면 어떤 비교함수를 사용하는 지에 따라 달라집니다. 

![img13.png]({{site.url}}/images/CS231n/lecture02/img13.png){: .align-center}

위의 NN예제에서는 비교함수로 L1 Distance를 사용했습니다. L1 Distnace는 아주 간단한 방법으로 이미지를 **Pixel-wise(픽셀단위)로 비교**합니다.

4x4 테스트 이미지가 있다고 가정해봅시다. **`test image와 training image에서 같은 자리의 픽셀을 서로 빼고 절댓값을 취합니다.`** 이렇게 **`픽셀 간의 차이 값을 계산하고 모든 픽셀의 수행 결과를 모두 더합니다.`**  

### NN python code

```python
import numpy as np

class NearestNeibor:
    def __init__(self):
        pass
    
    def train(self, X, y):
        """X is N x D where each row is an example. Y is 1-dimension of size N"""
        # the nearest neighbor classifier simply remembers all the training data
        self.X_train = X
        self.y_train = y
        
    def predict(self,X):
        """X is N x D where each row is an example we wish to predict label for"""
        num_test = X.shape[0]
        # lets make sure that the output type matches the input type
        Y_pred = np.zeros(num_test, dtype = self.y_train.dtype)
        
        # loop over all test rows
        for i in range(num_test):
            # find the nearest training image to the i'th test image
            # using the L1 distance (sum of absolute value differences)
            distances = np.sum(np.abs(self.X_train - X[i,:]), axis = 1)
            min_index = np.argmin(distances) # get the index with smallest distance
            Y_pred[i] = self.y_train[min_index] # predict the label of the nearest example
            
        return Y_pred
```

train 함수의 역할은 train data를 기억하는 것으로 Trainset의 이미지가 총 N개라면 시간 복잡도는 $O(1)$입니다.

test 함수의 역할은 이미지를 입력으로 받고 L1 Distance로 비교하는 것입니다.  Test time에서는 N개의 train data 전부를 test image와 비교해야만 하기 때문에 $O(N)$의 시간 복잡도를 갖습니다.

즉,  NN은 test time이 train time 보다 느린 것을 알 수 있고 이는 보통의 classifier 가지는 특징과 정 반대입니다.  

**`일반적인 Classifier에서는 Train time은 조금 느려도 되지만 Test time에서는 빠르게 동작`**해야합니다. Classifier의 좋은 성능을 보장하기 위해서 Train Time에는 많은 시간을 쏟을 수도 있습니다. 그러나 Test Time은 적은 시간이 요구 됩니다. 왜냐하면 Classifier모델이 핸드폰이나, 브라우저와 등 Low Power Device에서 동작해야 할 수도 있기 때문입니다. CNN과 같은 대부분의 parametic model들은 이러한 방식으로 동작합니다.

### NN decision regions

![img14.png]({{site.url}}/images/CS231n/lecture02/img14.png){: .align-center}

위 그림은 NN의 decsion regions입니다. 2차원 평면 상의 각 점은 학습데이터이고, 점의 색은 class label입니다. 위 그림을 보면 label이 5개임을 알 수 있습니다.  위 decision resgions가 그려진 과정을 살펴보겠습니다. 우선, 2차원 평면 내의 모든 좌표에서 각 좌표가 어떤 train data와 가장 가까운지 계산합니다. 다음으로, 각 좌표를 해당 label로 칠했습니다. 이처럼 NN Classifier은 공간을 나눠서 각 레이블로 분류합니다. 

하지만 이 Classifier은 그닥 좋지는 않습니다. 위 그림을 살펴보면 NN Classifier에서 발생 가능한 문제들을 살펴볼 수 있습니다. 가령 가운데를 보시면, 대부분이 초록색 점들인데중간에 노란 점이 끼어있습니다. **`NN 알고리즘은 "가장 가까운 이웃" 만을 보기 때문에`**, 녹색 무리 한 가운데 노란색 영역이 생겨 버립니다. 이 영역은 노란색이 아닌 초록색 영역이어야만 합니다. 그리고 유사하게 초록색 영역이 파란색 영역을 침범하고 있습니다. 이 또한 초록색 점이 끼어들어서 그렇습니다. 아마 이 점은 noise이거나 spurious(가짜)일것 입니다.

이러한 문제들이 발생하기 때문에 NN의 조금 더 일반화된 버전인 k-NN 알고리즘이 탄생하였습니다.

### K-NN

K-NN알고리즘은  단순하게 가장 가까운 이웃만 찾기보다는 조금 더 고급진 방법을 도입했습니다. 그 방법은 **`Distance metric을 이용해서 가까운 이웃을 K개의 만큼 찾고, 이웃끼리 투표를 하는 방법`**입니다. 그리고 가장 많은 득표를 획득한 레이블로 예측합니다.  거리별 가중치를 고려하는 등 투표를 하는 다양하고 복잡한 방법들이 있을 수 있지만 `가장 잘 동작하면서도 가장 쉬운 방법은 득표수만 고려하는 방법`입니다.

![img15.png]({{site.url}}/images/CS231n/lecture02/img15.png){: .align-center}

위에 보이는 세 예제는 동일한 데이터를 사용한 K-NN 분류기들입니다.각각 K=1/3/5 에서의 결과입니다. 우선, K=3 의 경우를 살펴봅게습니다. 앞서 초록색 영역에 자리 잡았던 노란색 점 때문에 생긴 노란 지역이 깔끔하게 사라졌습니다. 이제는 중앙은 초록색이 깔끔하게 점령했습니다. 그리고 왼쪽의 빨강/파랑 사이의 뾰족한 경계들도 점차 부드러워지고 있습니다. K=5의 경우를 살펴보겠습니다.
파란/빨간 영역의 경계가 이제는 아주 부드럽고 좋아졌습니다. 대게 **`NN분류기를 사용하면, K는 적어도 1보다는 큰 값으로 사용`**합니다. **`왜냐하면  K가 1보다 커야 결정 경계가 더 부드러워지고
더 좋은 결과를 보이기 때문`**입니다.

위 그림을 살펴보면 labeling이 되지않은 흰색영역이 존재합니다. 즉, 흰색 영역은  K-NN이 "대다수"를 결정할 수 없는 지역입니다. 흰색영역은 어떤 식으로든 추론을 해보거나, 임의로 정할 수도 있습니다.

위의 예제는 단순한 예제라서 가장 가까운 이웃이 존재하지 않으면 단순하게 흰색으로 칠했습니다.

### K-NN Example

이미지를 다루는 문제에서  K-NN을 사용하는 전략은 그닥 좋은 방법이 아닙니다.

![img16.png]({{site.url}}/images/CS231n/lecture02/img16.png){: .align-center}

위 그림은 잘 분류되었는지 아닌지를 초록/빨간색으로 표기했습니다. 성능이 생각보다 좋지 않음을 파악할 수 있습니다. 만약 K값을 높히면 어떨까요? ,가장 가까운 이웃 뿐만 아니라 Top-3/Top-5 혹은 모든 행(Row)을 사용하면 어떨까요? **`더 많은 이웃들이 투표에 참여하면 각종 잡음들에 조금 더 강인해 질 것`**임을 추측할 수 있습니다.

### K-NN: Distance Metric

![img17.png]({{site.url}}/images/CS231n/lecture02/img17.png){: .align-center}

K-NN을 사용할 때 결정해야 할 한 가지 사항이 더 있습니다. 바로 **`서로 다른 점들을 어떻게 비교할 것인지`** 입니다. K-NN에서 서로 다른 점들 비교하는 방법은 크게 두 가지가 있습니다.  

<aside>
📢 K-NN에서 서로 다른 점들 비교하는 방법  <br>
1. NN에서도 사용한 L1 distance 즉, <strong>픽셀 간 차이 절댓값 합</strong>을 이용한다.<br>
2. L2 distance 즉, <strong>제곱 합의 제곱근</strong>을 이용한다.  
</aside>

어떤 distance metric을 선택할지는 아주 흥미로운 주제입니다. 왜냐하면 서로 다른 metric에서는 해당 공간의 근본적인 기하하적 구조가 다르기 때문입니다.  위 그림에서 왼쪽에 보이는 사각형은 사실 L1 Distance의 관점에서는 원입니다. 생긴 모습은 원점을 기준으로 하는 사각형의 모양입니다. L1의 관점에서는 사각형 위의 점들이 모두 원점으로부터 동일한 거리만큼 떨어져 있습니다. 반면 L2의 관점에서는 원입니다. 우리가 예상했던 바로 그 원입니다.

이 두 가지 거리 척도간에는 아주 흥미로운 차이점이 있습니다. L1은 어떤 좌표 시스템이냐에 따라 많은 영향을 받습니다. 가령 기존의 좌표계를 회전시키면 L1 distance가 변합니다. 반면 L2 Distance의 경우에는 좌표계와 아무 연관이 없습니다.

만약 **`특징 벡터의 각각 요소들이 개별적인 의미를 가지고 있다면`**(e.g. 키 몸무게) **`L1 Distance`**가 더 적합할 수도 있습니다. 하지만 **`특징 벡터가 일반적인 벡터이고, 요소들간의 실질적인 의미를 잘 모르는경우`**라면, 아마도 **`L2 Distance`**가 조금은 더 적합할 것입니다.  

여기에서 주목할 점은  K-NN에 다양한 거리 척도를 적용하면 K-NN으로 다양한 종류의 데이터를 다룰 수 있다는 점입니다. ****거리 척도만 정해주면 어떤 종류의 데이터도 다룰 수 있습니다.****  K-NN은 아주 단순한 알고리즘이기 때문에 새로운 문제를 접했을 때  간단히 시도해 볼만한 아주 좋은 알고리즘입니다.

![img18.png]({{site.url}}/images/CS231n/lecture02/img18.png){: .align-center}

자 그러면 어떤 거리 척도를 사용하는지에 따라서 실제 기하학적으로 어떻게 변하는지 알아봅시다.

양 쪽 모두 동일한 데이터입니다. 다만 왼쪽은 L1 Distance를 오른쪽은 L2 Distance를 사용했습니다.결과를 보시면 **`거리 척도에 따라서 결정 경계의 모양자체가 달라짐`**을 알 수 있습니다. 왼쪽의 L1 Distance를 살펴보면 결정 경계가 "좌표 축"에 영향을 받는 경향을 알 수 있습니다. L1 Distance가 좌표 시스템의 영향을 받기 때문입니다. 반면 L2 Distance는 좌표 축의 영향을 받지 않고 결정 경계를 만들기 때문에 조금 더 자연스럽습니다.

이처럼  K-NN을 사용하려고 한다면 반드시 선택해야 하는 몇 가지 항목이 있었습니다. 바로 K값과 L1/L2와 같은 거리 척도입니다. 이러한 K와 거리척도를 "Hyperparameters" 라고 합니다.

### Hyperparameters

![img19.png]({{site.url}}/images/CS231n/lecture02/img19.png){: .align-center}

**Hyperparameters**는 머신 러닝 및 딥러닝 모델에서 사용되는 조절 가능한 매개변수들을 의미합니다. Hyperparmeters는 **`학습에 의해 결정되는 것이 아니기 때문에 반드시 학습 전에 선택`**해야합니다. 그러면 좋은 Hyperparmeters를 정하기 위해서는 어떻게 해야 할까? Hyperparmeters를 정하는 일은 문제의존적(problem-dependent)이기 때문에 가장 간단한 방법은 데이터에 맞게 다양한 하이퍼파라미터 값을 시도해 보고 가장 좋은 값을 찾는 방법밖에 없습니다.

![img20.png]({{site.url}}/images/CS231n/lecture02/img20.png){: .align-center}

"다양한 하이퍼 파라미터를 시도해 보는 것" 과 "그중 최고를 선택하는 것" 이 무슨 뜻일까? 

가장 먼저 떠올릴 수 있는 아이디어는 **train data의 정확도와 성능을 최대화하는 Hyperparmeters를 선택**하는 것입니다. 이는 **`좋은 방법같아보이지만 실제로는 절대 해서는 안되는 방법`**입니다. 예를 들어, NN분류기의 경우 K=1일 경우 train data를 가장 완벽하게 분류합니다. 하지만 앞선 예제에서도 보았듯이, 실제로는 K를 더 큰 값으로 선택하는 것이 train data에서는 몇 개 잘못 분류할 수는 있지만 train data에 없던 test data에 대해서는더 좋은 성능을 보일 수 있습니다. **`궁극적으로 기계학습에서는 학습 데이터를 얼마나 잘 맞추는지는 중요하지 않습니다. 우리가 학습시킨 Classfier이
한번도 보지 못한 데이터를 얼마나 잘 예측하는지가 중요`**하기 때문입니다. 그러므로 학습 데이터에만 신경쓰는 것은 최악의 선택입니다.

또 다른 아이디어가 있습니다. **전체 데이터셋 중 학습 데이터를 쪼개서 일부를 테스트 데이터로 사용**하는 것입니다. **train data로 다양한 Hyperparameter 값들을 학습을 시키고 test data에 적용시켜본 다음,Hyperparameters를 선택하는 방법**입니다. 이 방법이 조금 더 합리적인 것 같지만 이 방법 또한  **`절대 해서는 안되는 방법`**입니다. 다시 한 번 기계학습의 궁극적인 목적을 생각해보면 한번도 보지 못한 데이터에서 잘 동작해야 합니다. 즉, test dataset으로는 한번도 보지 못했던 data에서의 성능을 측정할 수 있어야 합니다. 그런데 만약 학습시킨 모델들 중 test data에 가장 잘 맞는 모델을 선택한다면 우리는 그저 하나의 "test set”에서만 "  잘 동작하는 Hyperparmeters를 고른 것일 수 있습니다. 그렇게 되면,  더이상 테스트 셋에서의 성능은 한번도 보지못한 데이터에서의 성능을 대표할 수는 없습니다.

일반적인 방법은 **데이터의 대부분은 train set으로 나누고 일부는 vaildation set, 그리고 나머지는 test set으로 나누는 것**입니다. 그리고 **다양한 Hyperparameters로 train set을 학습**시킵니다. 그런 다음  **vaildation set으로 검증을 한 후 가장 좋았던 Hyperparameters를 선택**합니다. 그리고 **최종적으로 vaildation set에서 가장 좋았던 model을 가지고 test set을 평가**합니다.  마지막 평가가 여러분의 알고리즘이 한번도 보지 못한 데이터에 얼마나 잘 동작해 주는지를 실질적으로 말해줄 수 있는 것입니다.

또 다른 하이퍼파라미터 선택 전략은 **Cross Validation(교차 검증)**입니다.  **Cross Validation**은 ****다음과 같은 과정으로 진행됩니다. 우선 test data를 정해놓습니다. test data는 아주 마지막에만 사용할 것입니다. 그리고 나머지 data를 train data와 validation data로 딱 나눠 놓는 대신에 train data를 여러 부분으로 나눠줍니다. 그런 다음 여러 부분으로 나누어진 train data를 번갈아 가면서 valid data로 활용합니다.

![img21.png]({{site.url}}/images/CS231n/lecture02/img21.png){: .align-center}

이 예제에서는 5-Fold Cross Validation을 사용하고 있습니다. 처음 4개의 fold에서 하이퍼 파라미터를 학습시키고 남은 한 fold에서 알고리즘을 평가합니다. 그리고 1,2,3,5 fold에서 다시 학습시키고 4 fold로 평가합니다. 이런식으로 모든 fold가 validation data로 이용될 때 까지 반복합니다. 이런 방식으로 최적의 하이퍼파라미터를 확인할 수 있을 것입니다. **Cross Validation**은  실제로는 딥러닝같은 큰 모델을 학습시킬 때는 학습 자체가 계산량이 많기 때문에 실제로는 잘 쓰지 않습니다.

![img22.png]({{site.url}}/images/CS231n/lecture02/img22.png){: .align-center}

cross validation을 수행하고 나면 위와 같은 그래프를 보실 수 있습니다. 그래프의 축을 살펴보면 X축은 K-NN의 K이고 고 Y축은 분류 정확도입니다. 위의 경우에는 5-fold cross validation을 수행하였습니다. 각 K마다 5번의  cross validation을 통해 알고리즘이 얼마나 잘 동작하는지를 알려줍니다. 
또한, 만약 여러 validation folds 별 성능의 분산을 같이 계산하게 되면, 어떤 하이퍼파라미터가 가장
좋은지 뿐만 아니라, 그 성능의 분산도 알 수 있습니다.

보통 기계학습 모델을 학습시키는 경우에 위와 같은 모습의 그래프가 그려질 것입니다. 위 그래프를 보면 hyperparameters에 따른 모델의 정확도와 성능을 평가할 수 있습니다. 그리고이를 이용하여  validation의 성능이 최대인 hyperparameters를 선택할 수 있을 것입니다. 이 예제에서는 K = 7 일 경우에 가장 좋은 성능을 내는 것을 알 수 있습니다.

### k-Nearest Neighbor on images never used.

실제로는 **입력이 이미지인 경우에는 K-NN classifier를 잘 사용하지 않습니다**. 왜나하면, **`우선, K-NN classifier은 너무 느립`**니다. 또한, train time 보다 test time에 더 많은 시간을 사용하기 때문에 image classfier로 적합하지않습니다. 그리고,  또 하나의 문제는 **`L1/L2 Distance가 이미지간의 거리를 측정하기에 적절하지 않다는 것`**입니다.벡터간의 거리 측정 관련 함수들은(L1/L2) 이미지들 간의 "지각적 유사성"을 측정하는 척도로는 적절하지 않습니다.

![img23.png]({{site.url}}/images/CS231n/lecture02/img23.png){: .align-center}

K-NN의 또 다른 문제 중 하나는 바로 **"차원의 저주**" 입니다. K-NN을 다시한번 살펴보면 K-NN이 하는 일은 트레이닝 데이터를 이용해서 공간을 분할하는 일입니다. 이는 K-NN이 잘 동작하려면 전체 공간을 조밀하게 커버할 만큼의 충분한 트레이닝 샘플이 필요하다는 것을 의미합니다. 그렇지 않다면 이웃이 사실은 엄청 멀 수도 있고 그렇게 되면 test image를 제대로 분류할 수 없을 것입니다. 공간을 조밀하게 덮으려면 충분한 양의 train data가 필요하고 그 양은 차원이 증가함에 따라 기하급수적으로 증가합니다.

---

# Linear Classification

Linear Classification은 간단한 알고리즘이지만 NerNetwork(NN)와 CNN의 기반 알고리즘입니다. 앞으로 보게될 다양한 종류의 딥러닝 알고리즘들의 가장 기본이 되는것 중 하나가 바로 **Linear classifier**이기 때문에 Linear Classification이 어떻게 동작하는지 이해하는 것은 아주 중요합니다. 왜냐하면 Linear Classification이 결국 전체 NN을 이루게 되기 때문입니다.

![img24.png]({{site.url}}/images/CS231n/lecture02/img24.png){: .align-center}
CIFAR-10이 50,000여개의 트레이닝 샘플이 있고 각 이미지는 32x32 픽셀을 가진 3채널 컬러 이미지라는 것을 다시 상기시봅시다. 

## parametric Approach

![img25.png]({{site.url}}/images/CS231n/lecture02/img25.png){: .align-center}

Linear classification에서는 K-NN과는 조금은 다른 접근 방법을 이용합니다. Linear classifier는 "parametric model"의 가장 단순한 형태입니다. **parametric model**에는 두 개의 요소가 있는데 **입력 이미지인 x**와 **가중치인 W**입니다.  우리는 이제 어떤 함수를 작성해야합니다. 이 함수는 data X와 parameter W를 가지고 10개의 숫자를 출력합니다. 이 숫자는 CIFAR-10의 각 10개의 카테고리의 스코어입니다. 이 스코어를 해석해 보자면, "고양이"의 스코어가 높다는 건 입력 X가 "고양이"일 확률이 크다는 것을 의미합니다.

![img26.png]({{site.url}}/images/CS231n/lecture02/img26.png){: .align-center}

앞서 살편 본 K-NN은 파라미터가 없었습니다. 그저 전체 트레이닝 셋을 가지고 있었고 모든 트레이닝 셋을 Test time에 사용했습니다. 하지만 **`parametric approach에서는 train data를 요약하여 W에 저장합니다. 이런 방식을 사용하면 Test time에서 더이상 trainning data가 필요하지 않습니다.`** Test time에서는 파라미터 W만 있으면 됩니다. 이 방법은 핸드폰과 같은 작은 디바이스에서 모델을 동작시켜야 할 때 아주 효율적입니다. 그렇기 때문에 딥러닝은 바로 이 함수 F의 구조를 적절하게 잘 설계하는 일이라고 할 수 있습니다. 어떤 식으로 가중치 W와 데이터를 조합할지를 여러가지 복잡한 방법으로 고려해 볼 수 있는데 이 과정들이 모두 다양한 NN 아키텍쳐를 설계하는 과정입니다. **`가중치 W와 데이터 X를 조합하는 가장 쉬운 방법은 그냥 이 둘을 곱하는 것`**입니다. 이 방법이 바로 **`Linear classification`** 입니다.

$\begin{align}{F(x,W) = Wx}\end{align}$

## Parametric Approach: Linear Classifier

![img27.png]({{site.url}}/images/CS231n/lecture02/img27.png){: .align-center}

이제 입력데이터 x와 가중치 w의 차원을 알아보겠습니다. 입력 이미지는  32 x 32 x 3이였습니다. 이 값을 열 벡터로 만들면 3,072 dim 벡터가 됩니다. 3,072 벡터가 10-classes를 가진 score로 출력이 되야하기 때문에 행렬 W는 10 x 3072가 되어야 합니다. 이 둘은 곱하면 10-classes를 의미하는 10 x 1의 하나의 열벡터를 얻게 됩니다.

![img28.png]({{site.url}}/images/CS231n/lecture02/img28.png){: .align-center}

그리고 가끔은 "Bias" 을 보게 될텐데  Bias term도 같이 더해줘야 합니다. 위 그림에서 Bias term은 10-dim 열 벡터입니다. **`Bias term은 입력과 직접 연결되지 않습니다. 대신에 "데이터와 무관하게"
특정 클래스에 "우선권"을 부여`**합니다. 가령 dataset이 분균형한 상황을 생각해 볼 수 있습니다.
예를 들어, 고양이 데이터가 개 데이터보다 훨씬 더 많은 상황입니다. 이 상황에서는 고양이 class에 상응하는 bias가 더 커지게 됩니다.

## Linear Classifier Example

![img29.png]({{site.url}}/images/CS231n/lecture02/img20.png){: .align-center}

함수가 어떻게 동작하는지 위 그림을 통해 알아보겠습니다. 위 그림을 보면 2x2 이미지이고 전체 4픽셀입니다. 이 Linear Classifier는 2x2 이미지를 입력으로 받고 이미지를 4-dim벡터로 쭉 폅니다. class는 고양이, 개, 배 이 세개의 class만 있다고 가정하겠습니다.  입력은 4개의 픽셀이고 class는 총 3개이기 때문입에 가중치 W는 4x3 행렬이 됩니다. 그리고 추가적으로 3-dim bias 벡터가 있습니다. bias는 데이터와 독립적으로 각 카테고리에 연결됩니다. 각각의 스코어 는 입력 이미지의 픽셀 값들과 가중치 행렬을 cross dot한 값에 bias term을 더한 것입니다. 이러한 관점에서 Linear Classifier은 Template Matching와 유사합니다. 가중치 행렬 W의 각 행은 각 이미지에 대한 Template으로 볼 수 있고 그 행 벡터와 이미지의 열벡터 간의 cross dot는 결국 class 간의 Template의 유사도를 측정하는 것이라고 할 수 있습니다. bias는 데이터 독립적으로 각 class에 scailing offsets을 더하는 것입니다. 

<aside>
📖 <b>Template Matching</b>  
<b>Template Matchin</b>은 컴퓨터 비전 분야에서 사용되는 기술로, 이미지에서 특정 Template 또는 패턴과 일치하는 부분을 찾는 작업으로 이미지 내에서 특정한 객체나 패턴을 찾거나, 이미지에서 관심 영역을 추출하는 데 유용하게 사용됩니다.
</aside>

## Interpreting a Linear Classifier

![img30.png]({{site.url}}/images/CS231n/lecture02/img30.png){: .align-center}

template matching 관점에서 Liner Classification을 생각해보겠습니다. 가중치 행렬 W의 한 행을 뽑아서 이를 이미지로 시각화 시켜보면 Linear classifier가 이미지 데이터를 인식하기 위해서 어떤 일을 하는지 짐작할 수 있습니다.

이 예제에서는 Linear classifier가 이미지를 학습합니다. 위 슬라이드 하단의 이미지는 실제로
가중치 행렬이 어떻게 학습되는지를 볼 수 있습니다. CIFAR-10의 각 10개의 카테고리에 해당하는 행 벡터를 시각화시킨 것입니다. 이렇게 시각화된 이미지를 살펴보면 어떤 일이 일어나는지 알아볼 수 있습니다. 

가령 맨 왼쪽의 이미지는 비행기 class에 대한 template image입니다. 이 이미지는 전반적으로 파란 색이며 가운데에는 어떤 물체가 있는 것 같습니다. 이 이미지를 해석해보면 Linear classifier가 비행기를 분류할 때 푸르스름한 것들을 찾고 있는 것 같습니다. 이러한 특징들이 이 Classifier이 비행기를 더 잘 찾도록 도와준다고 해석해 볼 수 있습니다.

**`Linear classifier의 문제 중 하나는 각 클래스에 대해서 단 하나의 템플릿만을 학습한다는 것`**입니다. 한 class 내에 다양한 features가 존재할 수 있지만, 모든 것들을 평균화 시키기 때문에 다양한 모습들이 있더라도 각 카테고리를 인식하기 위한 template은 단 하나밖에 없습니다. 이 문제점은 말(馬)을 분류하는 template을 살펴보면 잘 알 수 있습니다. 바닥은 푸르스름해 보입니다. 보통 말이 풀밭에 서 있으니 템플릿이 바닥을 푸르스름하게 학습한 것입니다. 그런데 유심히 살펴보면 말의 머리가 두 개 입니다. 각 사이드 마다 하나씩 달려 있습니다. 머리 두개 달린 말은 존재하지 않지만 Linear classifier가 클래스 당 하나의 템플릿밖에 허용하지 않으므로 이 방법이 최선입니다.

만약 **클래스 당 하나의 템플릿만 학습 할 수 있다는 것과 같은 제약조건이 없고, Neural Network같은 복잡한 모델을 사용한다면 조금 더 정확도 높은 결과를 볼 수 있을 것**입니다.

![img31.png]({{site.url}}/images/CS231n/lecture02/img31.png){: .align-center}

Linear Classifier은 이미지를 고차원 공간의 한 점으로 보는 또 다른 관점으로도 해석할 수 있습니다. **`각 이미지를 고차원 공간의 한점이라고 생각해보면 Linear classifier는 각 클래스를 구분시켜 주는 선형 결정 경계를 그어주는 역할`**을 합니다.

가령 왼쪽 상단에 비행기의 예를 볼 수 있습니다. Linear classifier는 파란색 선을 학습해서 비행기와 다른 클래스를 구분할 수 있습니다.

## Hard cases for a Linear Classifier

이미지가 고차원 공간의 하나의 점 이라는 관점으로 해석한다면 Linear classification이 직면할 수 있는 문제점을 살펴보겠습니다.

![img32.png]({{site.url}}/images/CS231n/lecture02/img32.png){: .align-center}

위 그림의 맨 왼쪽 그림은 두 개의 클래스를 가진 데이터 셋입니다. 데이터셋에는 파랑/빨강 두 개의 카테고리가 있습니다. 파랑색 카테고리는 0보다 큰 픽셀이 홀수 개 인 경우입니다. (예 : [3,-1] 이면 0보다 큰 수 : 3 (1개, 홀수개) -> 파랑) 반면 0보다 큰 수가 짝수 개면 빨간 카테고리로 classifier합니다.

이 같은 규칙으로 좌표 평면에 그려보면 두 개의 사분면에는 파란 class, 두 사분면에는 빨간색 class로 나타남을 볼 수 있습니다. (예:(1.1):2(짝), (-1,1):1(홀), (-1, -1):0(짝)) 이 데이터를 선 하나로 classifier할 방법은 없기 때문에 Linear classifier로는 풀기 힘든 문제입니다. 이와 같이  홀/짝수를 분류하는 것과 같은 문제를 parity problem(반전성 문제)라고 합니다. **`일반적으로  parity problem은 Linear classification으로 풀기 힘든 문제`**라고 알려져있습니다.

**`Linear classifier로는 풀기 힘든 또 하나는 Multimodal problem`**입니다. 위 이미지에서 맨 오른쪽 이미지를 보면 파란색이 분포하는 세 개의 섬들이 있습니다. 그 밖의 빨간색은 전부 다른 카테고리에 속합니다.  Multimodal problem의 예시로는 앞서 살펴본 머리 두 개 달린 말(馬)을 들 수 있습니다. 이처럼 Multimodal problem은 언제든 실제로 일어날 수 있습니다. 왼쪽 머리가 하나의 섬이 될 수 있고
오른쪽 머리가 또 하나의 섬이 될 수 있습니다. 섬이 두 개인데 선을  하나만 긋는 것은 그다지 좋은 방법이 아닙니다. Multimodal data라면 한 class가 다양한 공간에 분포할 수 있으며 이 문제는 Linear classifier로는 풀 수 없습니다.  

이처럼 Linear classifier에는 문제점이 일부 있긴 하지만 아주 쉽게 이해하고 해석할 수 있는 알고리즘입니다.

## Summary

지금까지  Linear classifier의 수식을 살펴보았습니다.  Linear classifier는 기본적으로 행렬과 벡터 곱의 형태로 나타낼 수 있습니다. 이는 템플릿 매칭과 관련이 있으며, 이 관점에서 선형 분류기는 각 카테고리에 대해 하나의 템플릿을 학습한다고 이해할 수 있습니다. 또한, 이미지를 고차원 공간의 한 점으로 해석할 수 있습니다. 각 이미지는 이 고차원 공간에서 한 점으로 표현되며,  Linear classifier는 각 클래스를 구분하는 선형 결정 경계를 정의하여 이를 분류합니다. 이 관점에서  Linear classifier는 데이터를 고차원 공간에서 적절한 위치로 매핑하고, 각 클래스를 선형 결정 경계를 통해 구분하는 역할을 수행합니다.
