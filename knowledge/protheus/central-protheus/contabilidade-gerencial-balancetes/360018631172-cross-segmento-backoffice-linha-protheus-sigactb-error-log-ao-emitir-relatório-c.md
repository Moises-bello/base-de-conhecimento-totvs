---
article_id: 360018631172
category: Contabilidade Gerencial - Balancetes
content_hash: 1713784b9343b998bd64a22a0e87e1a3e7b7e03f21d55134b1fcb2ceb46fc4ed
fetched_at: '2026-06-28T22:41:04.240257+00:00'
product: protheus
section_id: 1500001537281
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: Error log ao emitir
  relatório CTBR040 (Invalid collation ''Latin1_General_BIN)'
type: support-article
updated_at: '2023-11-10T16:11:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018631172-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Error-log-ao-emitir-relat%C3%B3rio-CTBR040-Invalid-collation-Latin1-General-BIN
---

**Dúvida**Error log ao emitir relatório CTBR040 (Invalid collation 'Latin1\_General\_BIN)

**Ambiente**Protheus – SIGACTB – A partir da versão 11.80  
  
  
**Solução**

Foi implementada uma função FWTEMPORARYTABLE que gera os arquivos temporários na área de arquivo temporário do banco de dados e caso o collation desta área temporária seja diferente do collation do Banco de dados, ocorrerá este erro caso o DBAcess esteja desatualizado.

Para corrigir o erro e necessário, atualizar o DBAcess de acordo com o portal do cliente, pois foi realizada uma correção que complementa a query com a conversão do collation.
