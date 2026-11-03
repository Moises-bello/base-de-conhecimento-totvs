---
content_hash: 264e73eb044368133bdd2c37558076b6dfdf1df1147b375f6fca504f4bfe9051
fetched_at: '2026-06-29T00:10:51.371153+00:00'
page_id: '566492830'
product: rm
source: tdn-rm
title: 9284800 FISCAL01-13954 - DT NFS-e - Implementação do município de Itupeva-SP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=566492830
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio de NFS-e |
| Ticket: | 9284800 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13954 |

## **02. SITUAÇÃO/REQUISITO**

Alterar o comportamento da tag codverificacao, a mesma deverá ser gerada para todos os municípios caso seja preenchida nos campos complementares do movimento.

## **03. SOLUÇÃO**

Foi implementado uma alteração no envio da Nota Fiscal de Serviço eletrônica para garantir que a tag codverificacao, caso preenchida no movimento, seja gerada em todos os munícipios, independentemente se o campo for obrigatório ou não.
