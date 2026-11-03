---
content_hash: 74341c9835357ced0e84a21e19b6f992be0ff2f96e1237ac51c1c0918bc620bf
fetched_at: '2026-06-29T00:10:44.441973+00:00'
page_id: '552580024'
product: rm
source: tdn-rm
title: 8743063 FISCAL01-12965 DT Implementação dos motivos 3 e 6, conforme manual
  da DAPI.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552580024
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DAPI - Minas Gerais |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12965 |

## **02. SITUAÇÃO/REQUISITO**

Cliente precisa gerar a DAPI, no detalhamento 22, com o motivo 6. Atualmente o sistema só permite que seja   
gerado com os motivos "1" (outros) e "2" (estorno), mas de acordo com o manual da DAPI existem outros motivos,   
como o "6", solicitado pelo cliente.

## **03. SOLUÇÃO**

Alterada a geração do Detalhamento do Campo 90 (Linha 22)

Se a string for “Outros” ou "1" gerar com o Motivo = 1.  
Se a string for “Estorno” ou "2" gerar com Motivo = 2.  
Se a string for "3", gerar com Motivo = 3.  
Se a string for "6", gerar com Motivo = 6.
