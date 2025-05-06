
import torch
print(torch.cuda.is_available())  # True dönüyorsa her şey doğru kurulmuş demektir
print(torch.__version__)  # torch versiyonu
print(torch.cuda.get_device_name(0))  # GPU ismini yazdırır
print(torch.cuda.current_device())  # GPU numarasını yazdırır


