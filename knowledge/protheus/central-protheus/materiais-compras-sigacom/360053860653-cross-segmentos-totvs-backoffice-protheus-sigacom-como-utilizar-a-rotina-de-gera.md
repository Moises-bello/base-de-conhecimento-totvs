---
article_id: 360053860653
category: Materiais - Compras (SIGACOM)
content_hash: d67e61067602049580f3ec54758f24d46e0ec1b91a4b984e96357224b0710bd9
fetched_at: '2026-06-28T22:41:16.077786+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como utilizar a rotina
  de Gerar Demanda MATA295 ?
type: support-article
updated_at: '2022-05-16T21:25:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053860653-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-utilizar-a-rotina-de-Gerar-Demanda-MATA295
---

**Dúvida**

Como utilizar a rotina de Gerar Demanda MATA295 ?  
  
**Ambiente**

Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Esta rotina gera a demanda do mês anterior, efetua a classificação ABC de venda e de custo, classifica tipo de preço e grava a fórmula do cálculo da demanda para cada produto, de acordo com as perguntas respondidas na janela "Parâmetros". Este processo deve ser executado todo início de mês, antes da geração da Sugestão de Compras.

*Durante o processamento, é atualizada a nova tabela Arquivo de Consumo (SBL) em 7 processos internos. São eles:*

*- Geração e atualização do SBL (Arquivo de Consumo) mês a mês.*

*- Acumulação de Entradas - SD1 (Arquivo de Itens das NFs de Entradas).*

*- Acumulação de Saídas - SD2 (Arquivo de Itens das NFs de Saídas).*

*- Acumulação de Requisições - SD3 (Arquivo de Requisições).*

*- Classificação ABC de Venda.*

*- Classificação ABC de Custo (Standard).*

*- Gravação* *da fórmula de demanda escolhida no mês para cada produto.*

**Parâmetros:**

***Mês p/ Avaliação?***

-Informe a quantidade de meses para avaliação da demanda.

***Estabilidade?***

Informe se o Sistema deve considerar fórmula de estabilidade no cálculo da demanda. Ao selecionar "Não"", esta fórmula não fará parte das fórmulas que poderão ser eleitas pela rotina.

**Obs**: *Caso esta fórmula seja eleita como a mais adequada, será necessário, no mínimo, dois meses de demanda do produto para gerar a sugestão de compras corretamente.*

***Médias 3 meses?***

Informe se o Sistema deve considerar a fórmula de média de três meses no cálculo da demanda. Ao selecionar "Não", esta fórmula não fará parte das fórmulas que poderão ser eleitas pela rotina.

**Obs**: *Caso esta fórmula seja eleita como a mais adequada,  será necessário, no mínimo, quatro meses de demanda do produto para gerar a sugestão de compras corretamente.*

***Tendência?***

Informe se o Sistema deve considerar a fórmula de tendência no cálculo da demanda. Ao selecionar "Não", esta fórmula não fará parte das fórmulas que poderão ser eleitas pela rotina.

**Obs:***Caso esta fórmula seja eleita como a mais adequada, será necessário, no mínimo, três meses de demanda do produto para gerar a sugestão de compras corretamente.*

***Sazonalidade?***

Informe se o Sistema deve considerar a fórmula de sazonalidade no cálculo da demanda. Ao selecionar "Não", esta fórmula não fará parte das fórmulas que poderão ser eleitas pela rotina.

**Obs**: *Caso esta fórmula seja eleita como a mais adequada, será necessário, no mínimo, dezesseis meses de demanda do produto para gerar a sugestão de compras corretamente.*

***Códigos das Fórmulas?***

Informe o código das fórmulas, criadas pelo usuário, a serem consideradas no cálculo da demanda. Os códigos devem estar separados ";" (ponto e vírgula).

***% Class. "A" Venda?***Informe a porcentagem para classificação de venda "A" dos produtos.

***% Class. "B" Vendas?***Informe a porcentagem para classificação de venda "B" dos produtos.

***% Class. "A" Custo?***Informe a porcentagem para classificação de custo "A" dos produtos.

***% Class. "B" Custo?***Informe a porcentagem para classificação de custo "B" dos produtos.

***Class. Custo Médio de? / Class. Custo Médio Até?***

Informe o intervalo de valores,  mínimo e máximo, para classificação do custo standart.

Exemplo: Class. Custo Médio de? 0

Class. Custo Médio Até? 999999999

***Considerar Movimento?***

Informe o tipo de movimento a ser considerado para geração da demanda. Para que os movimentos internos sejam considerados no cálculo da demanda, este parâmetro deve estar configurado com conteúdo igual a "Todos"

***Tipo?***

Informe o código do tipo de produto a ser considerado,  ou deixe em branco para considerar todos os tipos.

***Exceto?***

Informe o código do tipo de produto(s) que não será(ão) considerados para a geração da demanda.

***Qto ao Faturamento?***

Informe se o processamento deve considerar os documentos que geram duplicatas, os que não geram ou todos os documentos.

***Qto ao Estoque (TES)?***

Informe se o processamento deve considerar os documentos que possuem TES que movimentam o estoque, os que não movimentam ou todos os documentos.

***Saiba Mais :***

[MP - SIGACOM - Configuração dos parâmetros da Sugestão de Compras MATA297](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053817373)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
