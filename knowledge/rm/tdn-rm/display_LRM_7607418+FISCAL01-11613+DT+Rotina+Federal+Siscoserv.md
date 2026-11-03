---
content_hash: 1afa88383a2042c8e227cd524b5b3195ff7bf651ee5d505e8412d3635795b623
fetched_at: '2026-06-29T00:10:32.451333+00:00'
page_id: '525817665'
product: rm
source: tdn-rm
title: 7607418 FISCAL01-11613 DT Rotina Federal Siscoserv
type: documentation
url: https://tdn.totvs.com/display/LRM/7607418+FISCAL01-11613+DT+Rotina+Federal+Siscoserv
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Siscoserv |
| Ticket: | 7607418 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11613 |

## **02. SITUAÇÃO/REQUISITO**

Na geração da rotina SISCOSERV, para o arquivo tipo RAS, registro do xml Tag  <NumeroOperacaoEmpresa>. O sistema está gerando o conteúdo do campo "NumeroOperacaoEmpresa" com 13 caracteres, porém o tamanho estabelecido  pelo manual da rotina são 10 caracteres. Com isso está sendo apresentado  erro, na importação do arquivo.

## **03. SOLUÇÃO**

Ajuste na geração da tag <NumeroOperacaoEmpresa> para que quando a soma da concatenação dos caracteres dos campos Coligada, IdLaf e IdPrd do Lançamento for maior que 10

a tag seja gerado com os 10 primeiros caracteres do código MD5. Caso contrario será gerado através dos campos Coligada, IdLaf, IdPrd e NumItem.
