---
content_hash: 8817ae3387afbb654548d6ae6feffd527997a2a1955571831ed180abfdf4a5f4
fetched_at: '2026-06-29T00:09:19.468842+00:00'
page_id: '422543546'
product: rm
source: tdn-rm
title: 913107 FISCAL01-6716 DT Envio da NFS-e do Município de Ponta Grossa PR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422543546
version: 1
---

Tempo aproximado para leitura:**01 min**

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Envio da NFS-e |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar o envio de NFS-e para o município de Ponta Grossa/PR está ocorrendo a seguinte mensagem de rejeição: *S23 - Valor total não corresponde a soma dos itens.*

## **03. SOLUÇÃO**

Foi alterado a geração do XML único do TSS na tag valtotal (valor do documento) que será igual a tag valliq (valor líquido), somente para o município de Ponta Grossa.
