import requests
import pandas as pd
import os

def extrair_dados_api(endpoint):
    """Faz a requisição na Fake Store API e retorna um DataFrame do Pandas."""
    url = f"https://fakestoreapi.com/{endpoint}"
    print(f"Buscando dados de: {url}...")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API no endpoint '{endpoint}': {e}")
        return None

def main():
    os.makedirs('data', exist_ok=True)
    
    endpoints = ['products', 'carts', 'users']
    
    for ep in endpoints:
        df = extrair_dados_api(ep)
        if df is not None and not df.empty:
            caminho_salvamento = f"data/{ep}_raw.csv"
            df.to_csv(caminho_salvamento, index=False)
            print(f"Sucesso! Salvo em: {caminho_salvamento}\n")
        else:
            print(f"Falha ao gerar dados para o endpoint: {ep}\n")

if __name__ == "__main__":
    main()