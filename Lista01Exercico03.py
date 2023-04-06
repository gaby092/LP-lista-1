custodefabrica=int(input('digite o custo de fabrica: '))
distribuidor= custodefabrica * 28 / 100
impostos= custodefabrica * 45 / 100
consumidor= custodefabrica + distribuidor + impostos
print(f'o custo ao consumidor é {consumidor}')