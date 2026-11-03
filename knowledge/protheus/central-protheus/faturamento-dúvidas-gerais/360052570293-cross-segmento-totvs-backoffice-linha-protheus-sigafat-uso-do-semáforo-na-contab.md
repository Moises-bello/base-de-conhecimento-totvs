---
article_id: 360052570293
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b045d66a77bbc6ecbcca8ce14e9c8691bf3ba128d4bacf7d6d4416b8a9ce13ef
fetched_at: '2026-06-28T22:38:28.681667+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Uso do Semáforo
  na Contabilização Off Line do Faturamento - CTBANFS
type: support-article
updated_at: '2023-05-16T14:37:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052570293-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Uso-do-Sem%C3%A1foro-na-Contabiliza%C3%A7%C3%A3o-Off-Line-do-Faturamento-CTBANFS
---

**Dúvida**

Uso do Semáforo na Contabilização Off Line do Faturamento - **CTBANFS.**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

O sistema grava em um arquivo Ctree na pasta system (mesmo que o dicionário esteja no banco) :

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082572474/mceclip0.png)

Uma linha sempre será atualizada no momento que a rotina for rodada novamente:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083747493/mceclip1.png)  
  
Para desativar essa atualização será necessário alterar o parâmetro **MV\_ CTBNFSE** de conteúdo 1 para 2.
