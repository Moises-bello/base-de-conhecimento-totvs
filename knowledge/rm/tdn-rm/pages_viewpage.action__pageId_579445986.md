---
content_hash: 2548e1f54808fbe1e1c90af4665856ee4ff25c0ff3e23ea689e57947abda63d9
fetched_at: '2026-06-29T00:10:53.747043+00:00'
page_id: '579445986'
product: rm
source: tdn-rm
title: 10227598 FISCAL01-14411 DT NFSE - CNAE secundário não está sendo gerado para
  o município de Aparecida de Goiânia/GO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=579445986
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio de NFS-e |
| País: | Brasil |
| Ticket: | 10227598 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14411 |

## **02. SITUAÇÃO/REQUISITO**

Cliente relata que ao enviar uma NFSE para o município de Aparecida de Goiânia/GO, o código do CNAE secundário não está sendo levado para o XML.

Campo: Código na Receita Federal dos dados fiscais do Produto/Serviço.

## **03. SOLUÇÃO**

No munícipio Aparecida de Goiânia, quando o campo “Código na Receita Federal” não for vazio a Tag “CodigoCnae” do XML será preenchida com esta informação. Caso contrário será preenchido com o Código CNAE do prestador.

Possuindo o mesmo comportamento que outros municípios.
