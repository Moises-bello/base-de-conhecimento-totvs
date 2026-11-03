---
content_hash: ae809df658497b9dbace3f5dd3ae534bf535a3bba585c78bbcec48d6f7ad8181
fetched_at: '2026-06-29T00:11:12.202423+00:00'
page_id: '651296494'
product: rm
source: tdn-rm
title: DT- eSocial - S-1200 - Recibo de Férias - Antecipação Salário Família nas Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=651296494
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | **Linha RM** |
| Segmento: | **RH** |
| Módulo: | **Totvs Folha de Pagamento** |
| Função: | S-1200 - Recibo de férias - Antecipação Salário Família nas Férias |
| País: | Brasil |
| Ticket: | 12890714 |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHROTRM-2024 |

## **02. SITUAÇÃO/REQUISITO**

Quando é pago o salário família nas férias o sistema está duplicando a base de salário família, devido está considerando o evento do envelope e do recibo de férias.

## **03. SOLUÇÃO**

Criado no parametrizador em configurações gerais 7/7 um campo para informar o evento de antecipação salário família nas férias.

Ao gerar o XML do evento S-1200 o evento com código de cálculo 149 será substituído pelo evento informado no parametrizador na parte do XML referente a antecipação de férias.

## **04. DEMAIS INFORMAÇÕES**
