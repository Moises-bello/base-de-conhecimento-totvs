---
article_id: 22049729723543
category: Financeiro
content_hash: 03d84796a7f73737040957966d6736a00bc8778bc20c2bb8fb543b08b0b70ce2
fetched_at: '2026-06-28T22:38:03.162322+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Santander
  - É possível imprimir uma mensagem na impressão do boleto utilizando o campo EE_FORMEN1  para
  o banco Santander?
type: support-article
updated_at: '2025-01-23T20:20:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22049729723543-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Santander-%C3%89-poss%C3%ADvel-imprimir-uma-mensagem-na-impress%C3%A3o-do-boleto-utilizando-o-campo-EE-FORMEN1-para-o-banco-Santander
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22049729671831) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**É possível imprimir uma mensagem na impressão do boleto utilizando o campo EE\_FORMEN1 para comunicação via XML(comunicação bancária online) para o banco Santander?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões acima da 33  
  
**Solução**Atualmente, utilizamos a comunicação bancária online para o Santander via XML e não via JSON como é no Itaú e Banco do Brasil, por exemplo. Dessa forma, hoje não é feito esse tipo de operação de impressão de mensagem no boleto utilizando o campo EE\_FORMEN1 (campo dos Parâmetros de Banco) como é possível nas impressões de boleto do banco ITAÚ para o banco Santander.

A comunicação via XML do banco Santander está sendo descontinuada, e sendo substituída pela comunicação via JSON, onde está sendo estudado a forma de impressão de mensagem no boleto através do campo  EE\_FORMEN1 futuramente.  
  
*Atualmente sem data prevista, pois está em fase de piloto.***Saiba mais:**[Santander - FINA713](https://tdn.totvs.com.br/pages/releaseview.action?pageId=653588365)
