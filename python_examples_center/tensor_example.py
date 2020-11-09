import torch

a = torch.tensor(1., requires_grad=True)
print(a)

x = torch.tensor(3., requires_grad=True)
y = x**3 + 10 * torch.exp(-x**2/10)

print('%f, %f' % (x, y))

y.backward()
print(x.grad)