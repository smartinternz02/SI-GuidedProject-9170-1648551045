import numpy as np

a=np.zeros(10)
print(a)

a=np.ones(10)
print(a)

arr=np.ones(10)*5
print(arr)

arr=np.arange(10,51)
print(arr)

arr=np.arange(10,51,2)
print(arr)

a=np.arange(0,9).reshape(3,3)
print(a)

a=np.eye(3,3)
print(a)

arr=np.random.rand(1)
print(arr)

arr=np.random.rand(1,25)
print(arr)

a=np.arange(0.01,1.01,0.01).reshape(10,10)
print(a)

arr=np.linspace(0,1,20)
print(arr)

t=np.arange(1,26).reshape(5,5)

print(t[2:,1:])

print(t[3][-1])

print(t[:3,1].reshape(3,1))

print(t[-1])

print(t[-2:])

print(t.sum())

print(t.std())

print(t.sum(axis=0))