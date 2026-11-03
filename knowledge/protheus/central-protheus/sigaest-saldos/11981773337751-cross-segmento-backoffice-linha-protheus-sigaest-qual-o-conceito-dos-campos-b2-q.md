---
article_id: 11981773337751
category: SIGAEST - SALDOS
content_hash: db6adb95fcce9a89d50443513299640ef7809628c35c4f3b070b697722522dd2
fetched_at: '2026-06-28T22:39:14.924950+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Qual o conceito dos
  campos B2_QACLASS e B2_NAOCLAS?
type: support-article
updated_at: '2023-01-27T14:50:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11981773337751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-o-conceito-dos-campos-B2-QACLASS-e-B2-NAOCLAS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual o conceito e utilização dos campos **B2\_QACLASS** e **B2\_NAOCLAS** no Protheus?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**O campo **B2\_QACLASS** é populado quando utiliza produto com controle de endereço **(B1\_LOCALIZ=S)**, e o saldo ainda não foi endereçado. Ou seja esta aguardando a destinação do saldo pela rotina MATA265.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11982446865943)

O campo **B2\_NAOCLAS** é populado quando quando incluir uma pré-nota de entrada (MATA140) e a mesma ainda não foi classificada. Ou seja, esta aguardando a classificação da nota para inclusão do saldo no Estoque. 

Obs.: Na [consulta F4 de Saldos em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto-) não tem um campo referenciando a pré-nota. 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11982859994775)

***Saiba Mais:***

*[SIGAEST - Como descobrir a origem dos saldos na consulta com comando [F4] no Produto?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto-)*

*[Clique aqui e veja mais artigos sobre Saldos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)*
