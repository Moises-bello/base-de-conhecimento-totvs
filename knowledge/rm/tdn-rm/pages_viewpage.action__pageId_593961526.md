---
content_hash: f52c8a46b6ee50f23f9ded9db08c2805bc033f751c7b3e0353079cf971da58d0
fetched_at: '2026-06-29T00:10:56.998526+00:00'
page_id: '593961526'
product: rm
source: tdn-rm
title: 10646352 FISCAL01-14778 - DT NFS-e Anápolis - Cancelamento - Arquivo enviado
  fora da estrutura do arquivo xml
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593961526
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cancelamento de NFS-e |
| Ticket: | 10646352 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14778 |

## **02. SITUAÇÃO/REQUISITO**

Rejeição apresentada ao consultar o cancelamento da NFS-e da prefeitura de Anápolis:  
E160 - Arquivo enviado fora da estrutura do arquivo XML de entrada

Foi verificado que no arquivo **cancelanfse001\_in.xml**  o RM não está enviando o código de cancelamento, com isto a prefeitura não realiza o cancelamento da NFS-e.

## **03. SOLUÇÃO**

Ajuste no processo de cancelamento para possibilitar ao usuário a informar o motivo de cancelamento da NFS-e no município de Anápolis.
