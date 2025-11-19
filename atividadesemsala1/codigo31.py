results = []
printer = []
m = n = 1
while True:
    m, n = map(int, input('Insira os valores: ').split())
    print(f"DEBUG: m={m}, n={n}")
    if n > m:
        n, m = m, n
    if m <= 0 or n <= 0:
        break

    n -= 1

    for i in range(m - n):
        n += 1
        printer.append(n)
    soma = sum(printer)
    results.append(printer)
    printer = []
    results.append(f'sum={soma}')

for i in results:
    printer.append(i)
    if isinstance(i, str):
        print(*printer)
        printer = []