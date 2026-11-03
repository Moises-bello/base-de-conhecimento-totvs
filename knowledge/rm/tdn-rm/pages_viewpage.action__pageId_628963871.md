---
content_hash: 33bc4fac70de8662dd22c82aeef9a232d22f050484de1b40e33d28e6c7b732ab
fetched_at: '2026-06-29T00:11:05.316413+00:00'
page_id: '628963871'
product: rm
source: tdn-rm
title: FISCAL01-14216 - DT NFS-e Florianópolis - Gerar a tag CST de acordo com o manual
  da prefeitura
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628963871
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Transmissão de NFSe |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14216 |

## **02. SITUAÇÃO/REQUISITO**

O cliente está realizando um envio de NFS-e para a Prefeitura de Florianópolis/SC, esta operação é isenta de ISS, porém o cliente está tendo que enviar o valor de ISS pois a Prefeitura consiste o valor da alíquota e ocorre a rejeição abaixo:

0000 - Alíquota inválida do item 1.

De acordo com a Tabela de CST do manual da prefeitura de Florianópolis, quando a operação é Isenta de ISS deve ser gerado o CST 12 no XML.

Analisando o arquivo remessanfse001\_in, não possuía a TAG <cst>. A mesma esta disponível no Manual do XML Único do TSS:

Necessário alterar a transmissão da NFS-e pelo RM para gerar a tag <cst> no xml da nota.

## **03. SOLUÇÃO**

Realizada a alteração no processo de envio de NFS-e para gerar a tag cst.

Será gerado na tag cst a informação preenchida no campo Situação Tributária da linha do tributo ISS.

Independentemente do município, caso o campo seja preenchido a tag será gerada no xml.
