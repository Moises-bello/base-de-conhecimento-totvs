---
article_id: 4420658656663
category: SIGAEST - RELATORIOS
content_hash: 0a8c7b436d5df6444bff135ee527aeb3d43e8f9726637b447a690dd855dc8d13
fetched_at: '2026-06-28T22:39:06.046678+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Giro de Estoque -
  Conceito e Informações
type: support-article
updated_at: '2022-01-28T17:25:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420658656663-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Giro-de-Estoque-Conceito-e-Informa%C3%A7%C3%B5es
---

**Dúvida**O que é Giro de Estoque e como obter seu cálculo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**O giro de Estoque tem relação com a quantidade de produção/vendas de um período. Portanto, é uma ferramenta que aponta a circulação das mercadorias, ou seja, quantas vezes elas foram vendidas/consumidas e repostas completamente no armazém. Ele é um indicador muito importante para avaliar se a gestão do estoque é eficiente, mostrando se há equilíbrio entre compras e vendas dos produtos. Quanto mais eles forem vendidos, maior é o giro de estoque. 

**Exemplificação**

Geralmente o cálculo é feito para descobrir o número de giros ao mês, bimestre, timestre ou ano (a depender do tipo de Produto). Para que o estoque tenha um bom giro no mês (por exemplo) é necessário que a compra do Material tenha relação com a necessidade de produção ou previsão de vendas.

**Giro de estoque =** Total de vendas / Volume médio de estoque

O giro de estoque é igual ao total de vendas/consumo produtivo dividido pelo volume médio de estoque.

Por exemplo, se o volume médio mensal no estoque de um supermercado é de 3 mil pacotes de suco, e são vendidos 12 mil deles por ano, o giro de estoque é 4, o que significa que o estoque foi completamente renovado 4 vezes. Caso o número fosse menor do que 1, isso indicaria que o estoque não foi renovado nenhuma vez, ou seja, o estoque ficou parado correndo riscos operacionais (vencimentos, etc).

**Em ambiente Produtivo**

Se, num cenário produtivo, ocorre uma produção de um lote total de 100 KG ao mês, mas esta produção é fracionada em 25 Kg/semana, a compra de matéria prima é feita total (100 KG) na 1ª semana do mês, o giro seria 1 pois a empresa ficou com o estoque parado naquela semana. Mas se a compra é feita conforme necessidade de produção, 25 Kg/Semana, o seu giro de estoque será 4, pois, calculando a necessidade de produção pela quantidade de material em estoque - 100 / 100 = 1 ou 100 / 25 = 4, o estoque girou 4 vezes no mês.

O Protheus disponibiliza do relatório **[Análise de Estoques (MATR290)](https://tdn.totvs.com/pages/releaseview.action?pageId=348295976)**, onde é possível fazer uma análise aproximada ao giro de estoque (não necessariamente o relatório tem este viés).  
  
Exemplo:  
Relatório MATR290 traz as informações de saldo atual, ponto pedido, lote econômico, consumo, etc.  
  
Neste caso, pode-se utilizar o relatório Análise de Estoques (MATR290), com os parâmetros da seguinte forma:

Lst so prod.obsolet ? =Sim

Dt.Limite p/obsolt ? = Indicar o período que deseja que não seja exibido. **[Clique aqui para ver detalhes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021872411-MP-SIGAEST-MATR290-Obsolesc%C3%AAncia-de-Produtos)**

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)*
