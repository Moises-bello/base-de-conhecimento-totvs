---
content_hash: 017bfa1456476af23b9665f07584f560efddb4bf5cda28f2177e73ea1a888b5c
fetched_at: '2026-06-29T00:10:38.681137+00:00'
page_id: '544709750'
product: rm
source: tdn-rm
title: 8389570 FISCAL01-12676 DT DIEF - PA
type: documentation
url: https://tdn.totvs.com/display/LRM/8389570+FISCAL01-12676+DT+DIEF+-+PA
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DIEF - PA |
| Ticket: | 8389570 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12676 |

## **02. SITUAÇÃO/REQUISITO**

Atualmente no ANEXO II - SUBSTITUIÇÃO TRIBUTÁRIA - Sub Tipo 23, estamos gerado o Código do   
Município para Lançamentos de Entrada e Saída com ST.  
Segundo o manual o Código do Município só deve ser informado para Lançamentos de Saída com ST.

## **03. SOLUÇÃO**

Foi ajustado no sistema para que o Código de Município só será gerado para Lançamentos de Saída, para Lançamentos de Entrada

será gerado o campo com valor 0 Zero
