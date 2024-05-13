import torch

x = torch.tensor([1, 2, 3, 4])
new_x = torch.view_as_complex(x.float().reshape(*x.shape[:-1], -1, 2))
print(f'x = {x}')
print(f'complex_x = {new_x}')
print(f'real_x = {torch.view_as_real(new_x).flatten(0)}')
