---
article_id: 360024655932
category: Materiais - Compras (SIGACOM)
content_hash: 1e0f92896f9a2ee55b856db710ecacc7a0ff9a8c135441a7b229ff9b2bf17bac
fetched_at: '2026-06-28T22:41:10.368604+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a finalidade do
  parâmetro MV_RATDESP ?
type: support-article
updated_at: '2023-06-21T15:05:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024655932-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-finalidade-do-par%C3%A2metro-MV-RATDESP
---

**Dúvida**Qual a finalidade do parâmetro MV\_RATDESP ?

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução***Indica se o Rateio do Frete/Despesas/Seguro será efetuado por Valor(1) ou Peso(2) nas NF de Entrada e Saída.*Considerando NF de Entrada, para Despesas, Frete e Seguro é possível realizar o rateio por valor ou por peso, sendo que o tratamento é definido pelo parâmetro MV\_RATDESP.   
  
O campo utilizado para o rateio por peso é o D1\_PESO, ele deve ser preenchido manualmente, ou pode-se utilizar gatilhos ou customizações para faze-lo.   
Para verificar melhor o tratamento marcar os campos D1\_DESPESA, D1\_VALFRE e D1\_SEGURO como usado via configurador.

Se informarmos os valores manualmente em cada item a rotina soma os valores e apresenta no folder de Descontos/Frete/Despesas.

Observação: Este tratamento é realizado independente de a TES gerar ou não duplicata. Caso possua algum item na nota que não gere duplicata e não desejar que os valores de Desconto, Despesa, Frete e Seguro sejam rateados automaticamente, deve-se informar os valor   
individualmente (item a item).

***Saiba Mais :***

* [MV\_RATDESP - Conceito do parâmetro (Rateio das Despesas Acessórias)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=284355064)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
