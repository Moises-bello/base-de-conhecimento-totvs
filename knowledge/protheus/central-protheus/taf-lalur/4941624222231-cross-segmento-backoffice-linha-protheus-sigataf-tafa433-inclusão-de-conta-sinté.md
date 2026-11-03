---
article_id: 4941624222231
category: TAF - Lalur
content_hash: 9e2074c0b59a3cd343355d9b66333590503dedea81aad750f9cff5bab96d576b
fetched_at: '2026-06-28T22:41:31.046111+00:00'
product: protheus
section_id: 4404425263639
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGATAF - TAFA433 - Inclusão de
  Conta Sintética no cadastro de Evento Tributário
type: support-article
updated_at: '2022-03-22T19:22:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4941624222231-Cross-Segmento-Backoffice-Linha-Protheus-SIGATAF-TAFA433-Inclus%C3%A3o-de-Conta-Sint%C3%A9tica-no-cadastro-de-Evento-Tribut%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**É possível incluir contas sintéticas no cadastro de Evento Tributário (TAFA433)?  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - TAF – A partir da versão 12.

**Solução**Para composição da base de calculo do LALUR é necessário possuir os lançamentos contábeis na rotina TAFA331 e as respectivas contas contábeis relacionadas ao evento tributário (rotina TAFA433)

[Passo a Passo do Lalur](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404191850135-Cross-Segmento-Backoffice-Linha-Protheus-TAF-Roteiro-de-cadastros-e-parametriza%C3%A7%C3%B5es-para-apura%C3%A7%C3%A3o-do-LALUR-LACS)

Para facilitar esse mapeamento é possível fazer essa amarração de contas por grupo sintético, da seguinte forma:

1. No Menu:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4941199624215/mceclip0.png)

2. Ao incluir uma conta sintética:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4941387014551/mceclip1.png)

3. Sistema apresenta a mensagem abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4941464325015/mceclip3.png)

4. O sistema gatilha as contas analíticas do grupo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4941506489239/mceclip4.png)

Obs. As fichas da ECF permite apenas movimentações de contas analíticas, por esse motivo ao selecionar uma conta sintética são amarradas apenas as contas analíticas.

Todos os campos serão "copiados" para as contas analíticas do grupo, conforme item posicionado. Podendo ser alterado manualmente, caso necessário.

**Saiba Mais:**

https://tdn.totvs.com/pages/releaseview.action?pageId=666452532
