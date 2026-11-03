---
content_hash: 855d4cf6cc188b571ce43c5e908402a6e068c885ae428dc67d2d3bf46e03ddc9
fetched_at: '2026-07-02T19:24:24.796477+00:00'
page_id: '489764691'
product: protheus
source: tdn-tec
title: Application Server - 17.3.0.11
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.11
version: 5
---

GreenEXPEDIDO

# Implementação

SQLite como base principal para aplicações AdvPL

Requisito:  
Suportar o SQLite como base principal para aplicações AdvPL que sejam concebidas com as premissas de ser single-user ou single-process.  
  
Solução:  
Implementação das funções da RDD TOPCONN para a RDD SQLITE\_SYS, meditante configuração (RPODB=SQLITE).

# Melhoria

Registrar hora de aplicação de patch no console.log do Appserver

Solução: Implementação de API para ambiente Cloud

Referente ao chamado: [TTEC-3174](http://jiraproducao.totvs.com.br/browse/TTEC-3174)

# Correção

Função FListZip falha quando o arquivo passado por parâmetro não existe

Problema: Quando arquivo passado como parâmetro para função FListZip não existe, a função estava apresentando retorno inesperado.  
  
Solução: Correção no tratamento de parâmetros da função.

Referente ao chamado: TTEC-3155
