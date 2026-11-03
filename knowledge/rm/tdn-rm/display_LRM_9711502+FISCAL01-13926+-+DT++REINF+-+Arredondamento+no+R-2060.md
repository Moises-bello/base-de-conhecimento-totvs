---
content_hash: 8bfcd78cc21350bf31bf687cb03c05e33d5a41d61ea63ee0eec9f61d2a230953
fetched_at: '2026-06-29T00:10:51.329289+00:00'
page_id: '566474146'
product: rm
source: tdn-rm
title: 9711502 FISCAL01-13926 - DT  REINF - Arredondamento no R-2060
type: documentation
url: https://tdn.totvs.com/display/LRM/9711502+FISCAL01-13926+-+DT++REINF+-+Arredondamento+no+R-2060
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Período de Apuração CPRB |
| Ticket: | 9711502 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13926 |

## **02. SITUAÇÃO/REQUISITO**

Ao encerrar o período de apuração do tributo CPRB, verificou-se que em alguns casos o valor da contribuição estava com diferença de centavos. 

## **03. SOLUÇÃO**

Foi realizado um ajuste na apuração do CPRB para que o mesmo arredonde em casos de diferença positiva de 0,05 centavos. Este ajuste visa-se necessário para rotinas legais onde o valor da base de calculo \* alíquota deve ser exato.

Informações

Quando no valor do imposto da receita houver uma diferença de 0,05 centavos em relação ao imposto total dos itens, o valor de imposto considerado será dos itens.
