---
article_id: 6911686492311
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 05000c36e635046413744d062cbac20ef9bc4155515ef051f1c054a060c66329
fetched_at: '2026-06-28T22:38:29.896454+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus - SIGAFAT - Funcionamento
  do parâmetro MV_TPRTDSP no rateio das Despesas Acessórias
type: support-article
updated_at: '2026-03-26T13:47:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6911686492311-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Funcionamento-do-par%C3%A2metro-MV-TPRTDSP-no-rateio-das-Despesas-Acess%C3%B3rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16290290449047) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual o funcionamento do parâmetro MV\_TPRTDSP no rateio das despesas acessórias (Frete/Seguro/Despesas)?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**  
O parâmetro MV\_TPRTDSP define se o valor das despesas acessórias (Frete/Seguro/Despesa) e do [Desconto por indenização](https://totvssuporte.zendesk.com/knowledge/articles/360052217534/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F360052217534) informados no pedido de venda serão considerados na liberação do pedido ou se serão rateados entre os itens independente da liberação.

* MV\_TPRTDSP = 1 - "POR PEDIDO" : Sistema executa o rateio para cada nota fiscal gerada, por quantidade (registros na tabela SC6), ou seja, cada item da SC6 fará parte do rateio, independente dos itens que foram liberados.
* MV\_TPRTDSP = 2 - "POR LIBERAÇÃO" : Irá ratear pelo número de liberações (número de registros na SC9), o sistema rateia as despesas acessórias pelo numero de linhas gravadas na SC9, ou seja, pelos itens liberados, ainda que estes possuam bloqueio de Crédito ou Estoque.

**Saiba mais**:

[Cálculo do Rateio das Despesas Acessórias (Frete/Seguro/Despesa)](https://tdn.totvs.com/x/mDc-Dg)
