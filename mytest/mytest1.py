import torch

x = torch.tensor([1, 2, 3, 4])
new_x = torch.view_as_complex(x.float().reshape(*x.shape[:-1], -1, 2))
print(f'x = {x}')
print(f'new_x = {new_x}')
