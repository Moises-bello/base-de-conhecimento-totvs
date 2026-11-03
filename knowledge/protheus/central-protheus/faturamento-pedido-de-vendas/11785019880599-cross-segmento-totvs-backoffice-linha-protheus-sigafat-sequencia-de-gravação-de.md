---
article_id: 11785019880599
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d1fccdceed9dec99d5dfcd4b6283a7bbeefa004e69efe90532acbcabebaafe1f
fetched_at: '2026-06-28T22:38:42.449343+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Sequencia de
  gravação de ítens do Adapter EAI MATA410 / MATI410
type: support-article
updated_at: '2023-01-19T20:31:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11785019880599-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Sequencia-de-grava%C3%A7%C3%A3o-de-%C3%ADtens-do-Adapter-EAI-MATA410-MATI410
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Como é gravado a sequencia de itens de um Pedido de Vendas em uma integração EAI.   
O sistema respeita a sequencia da TAG OrderItem enviada no JSON ou XML ou a sequencia que o item aparece registrada no arquivo ?  
  
Abaixo um exemplo, em um XML/JSON temos as ordens abaixo gravadas nesta sequencia  
  
OrderItem: 3  
OrderItem: 2  
  
Qual sequencia será gravado no Pedido de Vendas ?  
  
**Ambiente**Microsiga Protheus -  todas as versões.  
  
**Solução**

Em nosso fluxo sempre gravamos os itens na ordem que os recebemos seja via XML ou JSON, isto é, pelo exemplo acima será gravado nesta sequencia   
  
Em primeiro o OrderItem: 3 e depois OrderItem: 2

A tag OrderItem não tem o objetivo de ordenar os itens do pedido de venda recebidos pelo arquivo XML/JSON. Neste caso é utilizado apenas para associar os valores recebidos com os valores internos do Protheus. Justamente pois na integração entre sistemas é comum as soluções terem controles diferentes, e devido a este cenário é realizado o mapeamento através do cadastro de De/Para (APCFG070).  
  
**Dica** : Caso perceba mudança de comportamento na gravação dos ítens  
  
Considerando que não houve mudança de comportamento do Protheus, aconselhamos a verificar se houve alguma mudança na geração do Json que foi enviado para integração (pois conforme dissemos, o fluxo irá executar o processamento na ordem de recebimento).

Segue o link de documentação complementar  
<https://tdn.totvs.com/display/PROT/Adapter+EAI+-+Order>
