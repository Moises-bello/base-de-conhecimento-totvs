---
content_hash: c9c9ab9bd0a4bee95ac5906adf33270f410840a3643413b0bd6cd44fded7caee
fetched_at: '2026-06-29T00:10:53.753678+00:00'
page_id: '579458941'
product: rm
source: tdn-rm
title: FISCAL01-14303 DT Campo Complementar para tag <CodMotCanc>
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=579458941
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: |  |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cancelar NFS-e |
| País: | Brasil |
| Ticket: | 10221340 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14303 |

## **02. SITUAÇÃO/REQUISITO**

Carregar valor na tag <codmotcanc> a fim de que o TSS não reporte erros de transmissão

## **03. SOLUÇÃO**

Foi feita a adequação do código para que no cancelamento de uma NFS-e, a tag <codmotcanc> seja carregada   
com o valor definido no campo complementar CODMOTCANC, no Movimento.

## **04. DEMAIS INFORMAÇÕES**

O cliente deverá parametrizar o campo complementar no movimento para que esta funcionalidade tenha efeito.
