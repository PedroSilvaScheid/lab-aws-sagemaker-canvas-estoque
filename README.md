# Entrega do Lab de previsão de Estoque Inteligente na AWS com [SageMaker Canvas](https://aws.amazon.com/pt/sagemaker/canvas/)

Neste Lab segui os passos para a criação de um modelo preditivo descritos no curso. Como dataset decidi desenvolver um script python para gerar modelos de estoque, criei um cenário imaginário de um loja de produtos Gaúchos na Itália. Dessa forma para testar os modelos da pra gerar diferentes datasets a partir do código que está na pasta datasets desse repositório.

Escolhi prever a quantidade de cada produto numa previsão de 7 dias em uma variedade de 20 produtos. Caso utiliza-se de dados reais acredito que as predições seriam muito mais eficientes e uteis também. 

Analisando as métricas do modelo, pode-se dizer que:

- Avg. wQL: 0.129
- MAPE: 0.242
- WAPE: 0.203
- RMSE: 6.699
- MASE: 1.118

- Desempenho Geral: 
O modelo parece ter uma perda relativamente baixa e um erro percentuais moderado (MAPE e WAPE), sugerindo uma previsão razoável. No entanto, o RMSE é um pouco alto, indicando que há uma quantidade significativa de erro absoluto.

- Comparação com Modelo de Referência: 
O MASE próximo de 1 sugere que o modelo não está significativamente melhor do que um modelo de referência simples. Isso pode indicar que o modelo pode se beneficiar de mais ajustes ou de uma análise mais profunda para melhorar a precisão.
