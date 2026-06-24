# 📈 E-commerce Analytics & SQL Architecture

Este projeto implementa um pipeline ponta a ponta (*end-to-end*) de engenharia e análise de dados de e-commerce. O fluxo engloba desde a ingestão automatizada de dados brutos de uma API externa até a modelagem relacional, limpeza de estruturas semiestruturadas em SQL (via DuckDB) e geração de indicadores de negócios (KPIs) com storytelling visual.

## 🛠️ Tecnologias e Ferramentas
* **Linguagem Principal:** Python 3.14+
* **Banco de Dados:** DuckDB
* **Manipulação e Visualização dos Dados:** Pandas, Matplotlib e Seaborn

## 🏗️ Arquitetura do Pipeline de Dados

O projeto adota uma variação simplificada da Arquitetura Medalhão localmente:

1. **Camada de Ingestão:** O script modular `ingestao_api.py` consome os endpoints `/products`, `/carts` e `/users`, salvando as respostas em arquivos CSV brutos na pasta `data/`.
2. **Camada de Modelagem e Transformação:** Através do DuckDB em ambiente Jupyter Notebook, os arquivos brutos são mapeados como Views SQL. Estruturas complexas de arrays e dicionários JSON aninhados são normalizadas.
3. **Camada de Produção e Análise:** Os dados limpos são persistidos de volta ao disco e consumidos para a geração de queries analíticas avançadas e gráficos executivos.

```txt
[API Externa] ──(requests)──> [data/*_raw.csv] ──(DuckDB/SQL)──> [data/*_clean.csv] ──> [Visualizações]
```
## ⚙️ Engenharia de Dados
Durante o processamento dos dados brutos da API, identificou-se um problema crítico de governança e formatação nas colunas contendo dicionários e listas.

O problema foi solucionado de forma performática diretamente na camada de computação do banco de dados, utilizando funções de tratamento de string combinadas com extratores JSONPath nativos do DuckDB:

```
-- Exemplo de extração de campos aninhados corrigindo o padrão de aspas
CAST(json_extract(REPLACE(rating, '''', '"'), '$.rate') AS DECIMAL(3,1))
```

Para a tabela fato de vendas, aplicou-se a função de tabela UNNEST para "explodir" as listas aninhadas de produtos adquiridos, transformando registros agrupados em linhas relacionais atômicas.

## 🚀 Storytelling

* **Concentração de Faturamento:** A categoria Men's Clothing lidera massivamente a receita do e-commerce, indicando a necessidade de priorização de capital de giro para este inventário. Em contrapartida, Women's Clothing performa abaixo do esperado, exigindo revisão urgente de catálogo ou marketing.

* **Gargalo de Churn:** O diagnóstico de comportamento revelou que a maior parte da base de clientes realiza apenas uma única compra e não retorna. Recomenda-se a implementação imediata de réguas de relacionamento pós-venda (cupons para 2ª compra) para mitigar o Custo de Aquisição de Clientes (CAC) ineficiente.

* **Análise de Afinidade:** O cruzamento matricial via Self-Join mapeou que o maior padrão de afinidade está na venda cruzada de moda masculina básica (Mochila Fjallraven e Camiseta Mens Casual Premium compradas juntas). Fornece insumos para a implementação de motores de Cross-Selling no checkout.

* **Dispersão Territorial Global:** A distribuição geográfica revela que o e-commerce atende uma base de clientes altamente fragmentada entre o Hemisfério Norte (EUA) e Hemisfério Sul. Operar centralizado destrói a margem com frete internacional; exige-se parcerias com operadoras logísticas de entrega capilar e uso de precificação dinâmica por geolocalização.

## 💾 Como Executar o Projeto
1 - Certifique-se de ter o [Python](https://www.python.org) instalado.

2 - Ative o ambiente virtual, de acordo com o seu [sistema operacional](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv):

```
# Se for Linux ou macOS
source /venv/bin/activate

# Se for Windows
.\venv\Scripts\Activate.ps1
```

3 - Instale as dependências listadas:

```
pip install -r requirements.txt
```

4 - Execute o script de ingestão para atualizar os dados brutos:

```
python .\src\ingestao_api.py
```

5 - Abra o notebook notebooks/01_eda_limpeza.ipynb no VS Code, selecione o Kernel da venv e execute as células.

```
---

Salve o arquivo após colar o conteúdo. Com esse `README.md` finalizado na raiz do repositório, o seu portfólio está completo e pronto para ser apresentado.
```