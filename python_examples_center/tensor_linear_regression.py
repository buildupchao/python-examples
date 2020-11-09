import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob
import unicodedata
import string
import random
from torch.autograd import Variable

x = np.loadtxt('../data/data1/data1_x.txt')
y = np.loadtxt('../data/data1/data1_y.txt')

plt.scatter(x, y)
plt.show()

x = torch.tensor(x, dtype=torch.float32)
x = torch.unsqueeze(x, dim=1)
y = torch.tensor(y, dtype=torch.float32)
y = torch.unsqueeze(y, dim=1)


class LinearRegression(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        out = self.linear(x)
        return out

EPOCH_SIZE = 2000
model = LinearRegression()
# 损失函数设置为均方误差损失函数
loss_function = torch.nn.MSELoss()
# 设置学习率
learning_rate = 0.005
# 随机梯度下降法
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
# 记录loss
loss_history = []

for epoch in range(EPOCH_SIZE):
    prediction = model(x)
    loss = loss_function(prediction, y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
    loss_history.append(loss.item())

    if epoch % 100 == 0:
        print("Epoch{}:loss:{}".format(epoch, loss.item()))
        plt.scatter(x.numpy(), y.numpy())
        plt.scatter(x.numpy(), prediction.detach().numpy(), color='r')
        plt.show()

history_x = []
for i in range(len(loss_history)):
    history_x.append(i)
plt.plot(np.array(history_x), np.array(loss_history))
plt.show()
