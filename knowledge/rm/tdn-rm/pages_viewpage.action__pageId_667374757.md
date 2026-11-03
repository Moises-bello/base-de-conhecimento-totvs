---
content_hash: f3d5c14859ade4cee3c2c095daa99a57eb4107b783b059d9bf2a2ac9853617dc
fetched_at: '2026-06-29T00:11:16.405069+00:00'
page_id: '667374757'
product: rm
source: tdn-rm
title: FISCAL01-17543 - DT - Tratar campo Código da Guia de Apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=667374757
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Guias Apuração |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17543 |

## **02. SITUAÇÃO/REQUISITO**

Ao tentar realizar a geração de guia de ICMS foi apresentada a seguinte mensagem: **Erro no processo: A cadeia de caracteres de entrada não estava em um formato correto.**

Obs.: o erro ocorria, pois, o cliente inseriu a guia manualmente e o código da guia possuía caracteres não numéricos

## **03. SOLUÇÃO**

Foi adicionada validação para que o campo Código da Guia aceite apenas números ao ser criada manualmente.

Disponível a partir da versão 12.1.2205
