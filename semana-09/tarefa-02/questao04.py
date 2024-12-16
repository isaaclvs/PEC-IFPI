morango_kg = float(input())
maca_kg = float(input())

if morango_kg <= 5:
    preco_morango = morango_kg * 2.50
else:
    preco_morango = morango_kg * 2.20

if maca_kg <= 5:
    preco_maca = maca_kg * 1.80
else:
    preco_maca = maca_kg * 1.50

total = preco_morango + preco_maca

if (morango_kg + maca_kg > 8) or (total > 25):
    total -= total * 0.10

print(f"{total:.2f}")

