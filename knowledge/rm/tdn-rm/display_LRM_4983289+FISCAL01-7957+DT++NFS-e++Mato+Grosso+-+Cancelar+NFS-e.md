---
content_hash: fe38b4f2b2d9f9cd2582ffba59567e0db7ea78bdbda95386606641932fdf567f
fetched_at: '2026-06-29T00:10:15.847755+00:00'
page_id: '465379097'
product: rm
source: tdn-rm
title: 4983289 FISCAL01-7957 DT  NFS-e  Mato Grosso - Cancelar NFS-e
type: documentation
url: https://tdn.totvs.com/display/LRM/4983289+FISCAL01-7957+DT++NFS-e++Mato+Grosso+-+Cancelar+NFS-e
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Cancelamento da NFS-e |
| Ticket: | 4983289 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-7957 |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar o cancelamento de uma NFS-e para o município Campo Grande, o sistema não está removendo os caracteres especiais da solicitação de cancelamento da NFS-e, sendo que o parâmetro para remover os caracteres especiais está devidamente marcado.  
Devido a não remoção destes caracteres especiais, estava causando a mensagem de rejeição da solicitação de cancelamento:  
" ASSINATURA DIGITAL INVALIDA ".

## **03. SOLUÇÃO**

Foi retirado os caracteres especiais do motivo de cancelamento da NFS-e.
