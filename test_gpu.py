import torch
import torch.nn as nn

tensor = torch.randn(10,10,10)
tensor = tensor.to('cuda')
import IPython;IPython.embed();exit()