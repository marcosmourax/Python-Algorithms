from math import cos, sin, tan, radians
an = int(input(f'Digite o ângulo que você deseja: '))
print(f'O ângulo de {an} tem o Seno de {sin(radians(an)):.2f} \nO ângulo de {an} tem o Cosseno de {cos(radians(an)):.2f} \nO ângulo de {an} tem a tangente de {tan(radians(an)):.2f}')
