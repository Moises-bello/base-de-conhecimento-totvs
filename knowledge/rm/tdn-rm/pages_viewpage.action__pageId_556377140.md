---
content_hash: 88aebb7ac1319c56ad60dc4f7647764bcbc1ade8e1747de0fffbd3a8a590df50
fetched_at: '2026-06-29T00:10:46.816452+00:00'
page_id: '556377140'
product: rm
source: tdn-rm
title: 5513092 FISCAL01-8771 DT Integração RM TAF - T015 Campo 45 (R-2050 Indicativo
  de comercialização)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=556377140
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Reinf |
| Ticket: | 5513092 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8771 |

## **02. SITUAÇÃO/REQUISITO**

Implementação do campo IndCom (com o código 7) no registro R-2050

## **03. SOLUÇÃO**

SE for uma operação para o exterior (CFOP 7xxx) ENTÃO o indicador será "9"

SENÃO

SE o campo FCFO.ENTIDADEEXECUTORAPAA do Cliente/Fornecedor estiver marcado

ENTÃO o indicador será "8"

SENÃO

SE o item do movimento for um produto isento de tributação FUNRURAL TPRODUTODEF.PRDISENTOFUNRURAL = 1 

ENTÃO o indicador será **“7”**

SENÃO o indicador será "1".
