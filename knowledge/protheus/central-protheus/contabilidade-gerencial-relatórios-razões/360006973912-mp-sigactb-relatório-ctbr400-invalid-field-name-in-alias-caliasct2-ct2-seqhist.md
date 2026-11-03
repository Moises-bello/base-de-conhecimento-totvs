---
article_id: 360006973912
category: Contabilidade Gerencial - Relatórios Razões
content_hash: cd459ba75bdea28179d157e8a965f03b1c3f93f64325790d632cef3a38890c37
fetched_at: '2026-06-28T22:40:41.172974+00:00'
product: protheus
section_id: 1500001548782
source: central-protheus
title: 'MP - SIGACTB - RELATÓRIO CTBR400 - "invalid field name in Alias cAliasCT2->CT2_SEQHIST" '
type: support-article
updated_at: '2021-04-28T22:12:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006973912-MP-SIGACTB-RELAT%C3%93RIO-CTBR400-invalid-field-name-in-Alias-cAliasCT2-CT2-SEQHIST
---

**Ocorrência**

Ao imprimir o relatório CTBR400 o sistema apresenta o error log: "invalid field name in Alias cAliasCT2->CT2\_SEQHIST" e finaliza a execução.

**Ambiente**  
Protheus – Contabilidade Gerencial – A partir da versão 12.1.17  
   
**Solução**

Para efetuar a correção da inconsistência apresentada, é necessário aplicar a atualização completa do Binário em sua base de dados.  
  
Segue abaixo, nome dos pacotes que devem ser baixados:  
  
-SmartClient: 18-02-15-P12-SMARTCLIENT\_WINDOWS  
-AppServer: 18-04-03-P12\_APPSERVER\_WINDOWS

Caso o problema persistir, verificar a atualização da LIB.
