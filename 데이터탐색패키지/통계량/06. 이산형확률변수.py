#!/usr/bin/env python
# coding: utf-8

# ### 확률 분포
# - 확률변수가 어떻게 움직이는지를 나타낸 것

# ### 확률 변수의 구분
# 
# - 이산 확률 변수 : 변수가 취할 수 있는 값의 개수가 유한
#     
# - 연속 확률 변수 : 변수가 취할 수 있는 값의 개수가 무한
#     
# ![image.png](attachment:image.png)

# ### 확률함수
# - 확률변수 X가 특정 실수 값 x를 취할 확률을 X의 함수(f)로 나타낸 것
#     - 확률질량함수(probability mass function: pmf)
#         - 확률변수가 이산형인 경우
#     - 확률밀도함수(probability density function: pdf)
#         - 확률변수가 연속형인 경우

# ### 확률분포의 평균(mean) - 기대값
# 
# - 기대값(expected value)라고 함
# -  확률 변수의 기대값({E})은 각 사건이 벌어졌을 때의 이득과 그 사건이 벌어질 확률을 곱한 것을 전체 사건에 대해 합한 값이다. 
#     - 어떤 확률적 사건에 대한 평균의 의미로 생각할 수 있다.
# 
#     - E(X) 또는 μX 로 표시
#     - 이산확률분포의 기대값 : 확률을 가중값으로 사용한 가중평균
#     - 연속확률분포의 기대값 : 적분개념의 면적
#     
#     ![image.png](attachment:image.png)
#     
# - 모평균
#     - 모 평균(population mean) μ는 모 집단의 평균이다. 모두 더한 후 전체 데이터 수 n으로 나눈다.

# ### 이산형 확률 분포
# 
# - 1차원 이산형 확률 분포

# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# In[3]:


import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('precision', '3')
get_ipython().run_line_magic('matplotlib', 'inline')


# #### 이산형 확률
# - 확률변수 x가 취할 수 있는 값의 집합 {x_1, x_2,..., x_k}
# - x가 x_k라는 값을 취하는 확률
# ![image.png](attachment:image.png)
# - 확률 질량함수(확률함수)-pmf
# ![image-2.png](attachment:image-2.png)

# ## 불공정한 주사위
# ![image.png](attachment:image.png)

# - 위 불공정한 주사위 확률분포의 확률 변수 확인
# ![](불공정한주사위확률변수.png)

# In[7]:


# 위 식을 함수로 구현

def f(x) :
    if x in x_set :
        return x/21
    else : 
        return 0


# In[8]:


# 확률 변수가 취할 수 있는 값의 set
x_set=np.array([1,2,3,4,5,6])


# In[9]:


# 확률변수 X
X=[x_set,f] # 확률분포[x_set,f]에 의해 확률변수 X의 동작이 결정됨


# In[14]:


# 확률 p_k를 구한다
prob = np.array([f(x_k) for x_k in x_set])
x_set
prob
zip(x_set,prob)
# x_k 와 p_k의 대응을 사전식으로 표시
dict(zip(x_set,prob))


# ![image.png](attachment:image.png)

# In[16]:


# 이산형 확률분포 그래프
fig=plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.bar(x_set, prob)
ax.set_xlabel('value')
ax.set_ylabel('probability')

plt.show()


# #### 이산형 확률분포 성질
# 
# - 모든확률은 0보다 크거나 같아야 하고
# - 확률의 합은 1이다
# 
# ![image.png](attachment:image.png)

# In[17]:


prob


# In[18]:


np.sum(prob)
np.all(prob >= 0)


# ### 누적분포함수(분포함수) 𝐹(𝑥)
# - X가 x이하가 될때의 확률을 반환하는 함수
# - 누적분포함수(cdf)는 주어진 확률변수가 특정 값보다 작거나 같은 확률을 나타내는 함수
# ![image.png](attachment:image.png)

# In[21]:


# 작거나 같은 이므로 주어진 x보다 작거나 같은 동안의 확률을 모두 더함 - f(x) 확률함수
def F(x) :
    return np.sum([f(x_k) for x_k in x_set if x_k <= x])


# In[22]:


# 주사위의 눈이 3이하가 될 확률
F(3) # x_set의 원소값이 3보다 작거나 같은때까지의 확률의 합계
f(3) # x_set의 원소값이 3일때 확률


# ### 확률변수의 변환
# 
# - 확률변수에 연산을 적용시켜 변화시킨다고 가정 => 새로운 데이터 집합 => 확률변수가 됨 
# 
# - 확률변수의 변환 연산 : 2X+3 
# - 위 연산을 적용시켜 변환된 확률변수를 Y라고 한다면

# In[24]:


y_set=np.array([2*x_k + 3 for x_k in x_set])

prob = np.array([f(x_k) for x_k in x_set])

dict(zip(y_set, prob))


# #### 1차원 이산형 확률변수의 지표

# In[ ]:


- 확률변수의 평균 : 기댓값
    - 확률변수를 무제한 시행하여 얻은 실험값의 합산


# ![image.png](attachment:image.png)

# - 수식을 함수로 구현
# ![image.png](attachment:image.png)
# 
# - 인수 g가 확률변수에대한 연산을 구현한 함수
#     - g에 아무것도 지정하지 않으면 확률변수 X의 기댓값이 구해짐

# #### 불공정 주사위 확률에 대한 기대값

# In[25]:


# 불공정 주사위에 대한 확률 변수

X =[x_set, f]


# In[26]:


def f(x):
    if x in x_set:
        return x / 21
    else:
        return 0
    
x_set = np.array([1, 2, 3, 4, 5, 6])    


# In[27]:


[x_k * f(x_k) for x_k in x_set]


# In[28]:


np.sum([x_k * f(x_k) for x_k in x_set])


# In[29]:


prob


# In[30]:


# 기댓값확인
1*0.048 + 2*0.095+3*0.143+4*0.19 + 5*0.238+6*0.286


# In[31]:


sample = np.random.choice(x_set, int(1e6), p=prob)
np.mean(sample)


# In[32]:


# 기대값 함수 구현
def E(X, g=lambda x:x) :
    x_set, f = X
    return np.sum([g(x_k) * f(x_k) for x_k in x_set])


# In[33]:


E(X)


# In[40]:


E(X, g=lambda x : 2*x+3)


# In[44]:


2 * E(X) + 3


# ### 분산
# 
# - 확률변수의 각 값에서 기대값을 뺀 편차의 제곱을 계산한후 기대값으로 계산
# 
# ![image.png](attachment:image.png)

# ### 불공정한 주사위의 분산

# In[34]:


### 불공정한 주사위의 기대값 함수 E(X)

mean= E(X)
np.sum([(x_k-mean)**2 * f(x_k) for x_k in x_set])


# In[37]:


def V(X, g=lambda x: x) :
    x_set, f = X
    mean = E(X,g)
    return np.sum([(g(x_k)-mean)**2 * f(x_k) for x_k in x_set])
    


# In[38]:


V(X)


# - 확률변수 X 대한 변환변수 2X+3에 대한 분산 계산

# In[39]:


V(X, lambda x:2*x+3)


# ![](분산의공식.png)

# In[42]:


2**2 * V(X)

