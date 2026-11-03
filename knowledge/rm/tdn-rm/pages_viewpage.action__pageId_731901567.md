---
content_hash: e6fc91b35e429786ebda927aa4dbf2d6969027ea4f9f1f487c2dbb9ef3c9519b
fetched_at: '2026-06-29T00:11:28.536656+00:00'
page_id: '731901567'
product: rm
source: tdn-rm
title: DT - Integração RM x TAE - Monitor de Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=731901567
version: 4
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | TAE - Assinatura Eletrônica |
| País: | Brasil |
| Releases: | a partir da 12.1.2205 |
| Issue: | [DRHCALCRM-3261](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3261) |

## **02. SITUAÇÃO/REQUISITO**

Para otimização no uso do jobs no Monitor de Relatórios do TAE,  será necessário criar as colunas **"IDMONITOR"** e **"CODSISTEMA"** nas tabelas de monitoramento do TAE **"GTOTVSSIGNMONITOR"** e **"GTOTVSSIGNMONITORSUBSCRIBERS".**

## **03. SOLUÇÃO**

Foi realizada uma otimização no uso do jobs e acrescentada uma mensagem de aviso para informar aos usuários a necessidade de atualização da base através do atualizador, com o script criado para inserir as novas colunas **"IDMONITOR"** e **"CODSISTEMA"** e adequar os demais campos das tabelas **"GTOTVSSIGNMONITOR"** e **"GTOTVSSIGNMONITORSUBSCRIBERS".**

## **04. DEMAIS INFORMAÇÕES**

[TOTVS Assinatura Eletrônica - Monitor de relatórios](https://tdn.totvs.com.br/pages/viewpage.action?pageId=607590599)
