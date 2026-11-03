---
content_hash: 96893f85aae8d9be47f59b6908918f08fbf3b511763e1deb39b669ce9d7b4cc4
fetched_at: '2026-06-29T00:11:11.132880+00:00'
page_id: '645911713'
product: rm
source: tdn-rm
title: DT- eSocial - S-1200 - Recibo de Férias - Antecipação 1º Parcela 13º pago nas
  férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=645911713
version: 11
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | **Linha RM** |
| Segmento: | **RH** |
| Módulo: | **TOTVS Folha de Pagamento** |
| Função: | Eventos de Folha |
| País: | Brasil |
| Ticket: | 12737352 |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-1816](https://jiraproducao.totvs.com.br/browse/DRHROTRM-1816) |

## **02. SITUAÇÃO/REQUISITO**

Quando a primeira parcela do 13º é paga nas férias o sistema está duplicando a base de FGTS 13, devido considerar tanto o evento de 13º do envelope quanto o 13º do recibo de férias.

## **03. SOLUÇÃO**

Criado no parametrizador um campo para informar o evento de antecipação primeira parcela 13º nas férias .Este evento não deverá ter incidências de FGTS13.

Ao gerar o XML do evento S-1200 o evento com código de cálculo 9 será substituído pelo informado no parametrizador na parte do XML referente a antecipação de férias.
