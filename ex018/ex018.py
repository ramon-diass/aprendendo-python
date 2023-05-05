from math import sin, cos, tan, radians

a = float(input('Digite o valor do ângulo em graus: '))
rad = radians(a)
print(f'Seu seno é {sin(rad):.3f}, seu cosseno {cos(rad):.3f} e o valor de sua tangente é {tan(rad):.3f}.')
