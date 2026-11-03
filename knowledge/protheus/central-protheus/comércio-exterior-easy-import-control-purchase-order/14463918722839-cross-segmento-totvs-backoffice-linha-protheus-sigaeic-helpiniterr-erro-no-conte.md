---
article_id: 14463918722839
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 5af2584810a449e27a9ef3bf360b02eb9fc93dc03e588a53a6a368f0c910a779
fetched_at: '2026-06-28T22:39:41.216486+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - HELP:INITERR Erro
  no conteúdo do inicializador padrão. Campo : W2_PARID_U'
type: support-article
updated_at: '2023-05-09T15:07:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14463918722839-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-HELP-INITERR-Erro-no-conte%C3%BAdo-do-inicializador-padr%C3%A3o-Campo-W2-PARID-U
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**

Na rotina Purchase Order ( **EICPO400** ) para incluir ou alterar, o sistema exibe uma mensagem de

HELP:INITERR Erro no conteúdo do inicializador padrão. Campo : W2\_PARID\_U .

![Imagem3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14463321926423)![Imagem2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14463335036823)![Imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14463321855127)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**

A causa raiz deste problema é desposcionamento dos campos da tabela **SW2** ou no Dicionário de dados da **SX3**. Verificar como esta o posicionamento dos campos **W2\_DT\_PAR** , **W2\_PARID\_U** e **W2\_MOEDA.**
