---
content_hash: 4567b37a74ad878edf1f616f5d87ae86a95700c9a95f571238c61670b1db8801
fetched_at: '2026-06-29T00:11:22.102528+00:00'
page_id: '698615896'
product: rm
source: tdn-rm
title: FISCAL01-18304 - DT - NFS-E - SALVAR XML - Verificar e-mail Fiscal.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=698615896
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFS-e |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18304 |

## **02. SITUAÇÃO/REQUISITO**

Alterar o processo de envio de e-mail da NFS-e para considerar o e-mail Fiscal do Cli/For e caso este esteja em branco, então considerar o e-mail principal. Além disso, verificar outras diferenças no processo.

## **03. SOLUÇÃO**

Envio de XML por e-mail da NFS-e agora envia para o e-mail fiscal, caso vazio envia para o e-mail principal.

Disponível a partir da versão 12.1.2205
