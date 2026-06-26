# 🏠 Previsão de Preços de Imóveis com Regressão Linear

Projeto acadêmico de **Ciência de Dados e Machine Learning** que utiliza **Regressão Linear Múltipla** para prever preços de imóveis com base em suas características.

## 📋 Sobre o Projeto

O mercado imobiliário é um setor de grande relevância econômica. Este projeto aplica técnicas de Machine Learning para estimar o preço de um imóvel utilizando o dataset real **House Sales in King County, USA**, contendo dados de vendas de imóveis na região de Seattle, Washington (EUA).

## 📊 Dataset

O dataset contém **4.601 registros** de vendas de imóveis com **18 variáveis**:

| Variável | Descrição |
|---|---|
| `price` | Preço de venda (USD) — variável-alvo |
| `bedrooms` | Número de quartos |
| `bathrooms` | Número de banheiros |
| `sqft_living` | Área habitável (pés²) |
| `sqft_lot` | Área do terreno (pés²) |
| `floors` | Número de andares |
| `waterfront` | Vista para água (0/1) |
| `view` | Qualidade da vista (0-4) |
| `condition` | Condição do imóvel (1-5) |
| `sqft_above` | Área acima do solo (pés²) |
| `sqft_basement` | Área do porão (pés²) |
| `yr_built` | Ano de construção |
| `yr_renovated` | Ano da última reforma |
| `city` | Cidade |

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** — Manipulação de dados
- **NumPy** — Operações numéricas
- **Matplotlib / Seaborn** — Visualizações gráficas
- **Scikit-Learn** — Modelo de Machine Learning

## 📂 Estrutura do Projeto

```
trabalho-final/
├── projeto_regressao_imoveis.ipynb   # Notebook principal do projeto
├── data.csv                          # Base de dados (King County House Sales)
└── README.md                         # Documentação do projeto
```

## 📓 Estrutura do Notebook

1. **Introdução** — Contextualização do problema e justificativa do modelo
2. **Carregamento da Base de Dados** — Importação e inspeção inicial
3. **Análise Exploratória (EDA)** — Valores nulos, duplicatas, distribuições
4. **Estatísticas Descritivas** — Média, mediana, desvio padrão, assimetria, curtose
5. **Visualizações Gráficas** — Histogramas, boxplots, scatter plots, heatmap de correlação, pairplot
6. **Pré-processamento** — Engenharia de features (idade do imóvel, reforma)
7. **Separação Treino/Teste** — 80% treino, 20% teste
8. **Treinamento do Modelo** — Regressão Linear Múltipla
9. **Avaliação** — MAE, MSE, RMSE e R²
10. **Exemplo de Previsão** — Simulação com imóveis fictícios
11. **Conclusão** — Resultados, insights, limitações e trabalhos futuros

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/previsao-precos-imoveis.git
   cd previsao-precos-imoveis
   ```

2. Instale as dependências:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```

3. Execute o notebook:
   ```bash
   jupyter notebook projeto_regressao_imoveis.ipynb
   ```

## 📈 Resultados

O modelo de Regressão Linear Múltipla foi treinado com 12 features derivadas do dataset original. A área habitável (sqft_living) é a variável com maior impacto positivo no preço, seguida pela presença de waterfront e qualidade da vista.

## 📝 Licença

Projeto desenvolvido para fins acadêmicos — Junho/2026.
