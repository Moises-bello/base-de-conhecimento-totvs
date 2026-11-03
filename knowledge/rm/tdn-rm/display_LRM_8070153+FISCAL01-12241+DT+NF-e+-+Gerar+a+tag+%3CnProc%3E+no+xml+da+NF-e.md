---
content_hash: 23673362bd87434ba4bda6e56335008a159486b6445378584020c6334f4531e2
fetched_at: '2026-06-29T00:10:37.004818+00:00'
page_id: '533743832'
product: rm
source: tdn-rm
title: 8070153 FISCAL01-12241 DT NF-e - Gerar a tag <nProc> no xml da NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/8070153+FISCAL01-12241+DT+NF-e+-+Gerar+a+tag+%3CnProc%3E+no+xml+da+NF-e
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Envio de NF-e |
| Ticket: | 8070153 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12241 |

## **02. SITUAÇÃO/REQUISITO**

Gerar a tag <nProc> no xml da NF-eGerar a tag <nProc> no xml da NF-e

## **03. SOLUÇÃO**

**Funcionalidade: Envio da NF-e**  
**Cenário I: Movimento com processo judicial**

Dado que um movimento possui processo judicial  
e a origem é 0,1,2,3 ou 9  
Ao enviar a NF-e  
A tag procRef deve ser preenchida com as subtags nProc (número do processo) e indProc (origem do processo)
