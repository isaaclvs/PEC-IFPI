PI = 3.141592

raio = float(input("Digite o raio do círculo: "))

circunferencia = 2 * PI * raio
areaCirculo = PI * raio ** 2
areaEsfera = 4 * PI * raio ** 2
volumeEsfera = (4 * PI * raio ** 3) / 3

print(f"Esse é o comprimento da circunferencia: {circunferencia:.6f}")
print(f"Essa é a área do círculo: {areaCirculo:.6f}")
print(f"Essa é a área da esfera: {areaEsfera:.6f}")
print(f"Esse e o volume da esfera: {volumeEsfera:.6f}")
