import requests
from requests import api, exceptions

def cotacao(nome):
    url = f"https://economia.awesomeapi.com.br/last/{nome}"
    resultado = requests.get(url)
    if resultado.status_code == 404:
        print('\n------------------------------------------\n')
        print("Moeda não encontrada")
        print('\n------------------------------------------\n')
    else:
        dicionario = resultado.json()
        print('\n------------------------------------------\n')
        print("Seguem cotações da moeda", nome.upper(), ": \n")
        if nome == "usd" or nome == "USD":
            compra = dicionario['USDBRL']['bid']
            venda = dicionario['USDBRL']['ask']
            variacao = dicionario['USDBRL']['varBid']
        elif nome == "eur" or nome == "EUR":
            compra = dicionario['EURBRL']['bid']
            venda = dicionario['EURBRL']['ask']
            variacao = dicionario['EURBRL']['varBid']
        elif nome == "btc" or nome == "BTC":
            compra = dicionario['BTCBRL']['bid']
            venda = dicionario['BTCBRL']['ask']
            variacao = dicionario['BTCBRL']['varBid']
        print("Valor de compra: ", compra)
        print("Valor de venda: ", venda)
        print("Variação: ", variacao)
        print('\n------------------------------------------')

print('\n------------------------------------------\n')
print("Digite usd ou USD para Dólar Americano; ")
print("Digite eur ou EUR para EURO; ")
print("Digite btc ou BTC para BICOIN")

print('\n------------------------------------------\n')
cotacao(input("Digite: "))