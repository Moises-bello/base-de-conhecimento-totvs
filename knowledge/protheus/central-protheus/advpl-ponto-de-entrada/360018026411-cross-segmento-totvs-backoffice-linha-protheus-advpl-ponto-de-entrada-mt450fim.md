---
article_id: 360018026411
category: ADVPL - Ponto de Entrada
content_hash: f9dbb794d55b47137e082194da492ef9642afc3de832a821cc7da5a6f1ad727a
fetched_at: '2026-06-28T22:40:12.685714+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MT450FIM
type: support-article
updated_at: '2022-06-03T13:21:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018026411-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MT450FIM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Ao utilizar a Liberação Manual da rotina **MATA450** e clicar no botão "**OK**" o PE **MT450FIM** não é chamado, como corrigir?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**O ponto **MT450FIM** , atua ao clicar no botão "Lib Todos" , neste caso, utilize o Ponto de entrada  **MTA450LIB .**

Este ponto pertence à rotina de liberação de crédito, **MATA450**(). Está localizado na liberação manual, **A450LIBMAN**(). Permite que o item a ser processado seja validado, permitindo ou não seu processamento.

**Saiba mais**[MTA450LIB - Validar item na liberação manual](http://tdn.totvs.com/pages/releaseview.action?pageId=6784404)  
[MT450FIM](http://tdn.totvs.com/display/public/PROT/MT450FIM)
