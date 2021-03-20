import random 
from math import sqrt
  
N = int(input("Ingresa tamaño array random N")) 
D_plus =[] 
D_minus =[] 
_random =[] 
  
for i in range(0, N): 
    _random.append(random.random()) 
    _random.sort() 
  
# Calcular max(i/N-Ri) 
for i in range(1, N + 1): 
    x = i / N - _random[i-1] 
    D_plus.append(x) 
  
# Calcular max(Ri-((i-1)/N)) 
for i in range(1, N + 1): 
    y =(i-1)/N 
    y =_random[i-1]-y 
    D_minus.append(y) 
  
# Calcular max(D+, D-) 
n1=sqrt(N) * D_plus
n2=sqrt(N) * D_minus
ans = max(n1, n2) 
print("Valor de D es :") 
print(ans)