from forex_python.converter import CurrencyRates

c = CurrencyRates()
valor_dolar = c.get_rate('USD', 'BRL')
print("A cotação atual do dólar em relação ao real é {:.3f}".format(valor_dolar))
