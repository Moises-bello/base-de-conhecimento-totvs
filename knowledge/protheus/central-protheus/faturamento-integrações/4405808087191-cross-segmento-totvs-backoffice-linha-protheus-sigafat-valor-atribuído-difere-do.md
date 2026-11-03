---
article_id: 4405808087191
category: Faturamento - Integrações
content_hash: e7e7805346e55fa98cf7aa46389abc8eddb83429759df424b6aecd81466e7396
fetched_at: '2026-06-28T22:38:26.449414+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Valor atribuído
  difere do tamanho do campo (Insc ANTT) GU3_ANTT
type: support-article
updated_at: '2021-08-06T19:24:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405808087191-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Insc-ANTT-GU3-ANTT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**

Ao atualizar o cadastro de Transportadora (**MATA050**) gera o Help: Inconsistência com o Frete Embarcador (SIGAGFE) - Valor atribuído difere do tamanho do campo (Insc ANTT) GU3\_ANTT

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405797215383/mceclip0.png)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

A mensagem informa que há divergência no tamanho de campo entre os campos **A4\_ANTT** e **GU3\_ANTT** no GFE, ambos tem estar com o mesmo tamanho, conforme abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405797318039/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405797327639/mceclip2.png)

Efetue o ajuste via **Configurador**, salvar os campos ajustados, salvar as tabelas, atualizar o dicionário de dados e reiniciar o smartclient, posteriormente, efetue o processo novamente.

O ajuste efetuado fará com que a mensagem não ocorra mais.
