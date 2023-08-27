import torch
# torch.manual_seed(1)
# x = torch.rand(3, 3)
# print(x.t() @ x + torch.ones_like(x))
# print(x.int())
# print(torch.relu(x))


import matplotlib.pyplot as plt
x = torch.randn(100, 2, requires_grad=True)
# plt.scatter(x[:, 0], x[:, 1])
plt.scatter(x[:, 0].detach().numpy(), x[:, 1].detach().numpy())
plt.show()