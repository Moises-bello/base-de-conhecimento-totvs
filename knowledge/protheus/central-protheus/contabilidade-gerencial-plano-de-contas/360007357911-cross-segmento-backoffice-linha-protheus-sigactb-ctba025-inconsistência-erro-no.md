---
article_id: 360007357911
category: Contabilidade Gerencial - Plano de Contas
content_hash: a55939c584c7c9ab4e46ff945ba3e7541ad42c5e25c1d3b7887d2dca76faec58
fetched_at: '2026-06-28T22:40:33.362339+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA025 - Inconsistência:
  Erro no gatilho  CVD_CODPLA  sec003'
type: support-article
updated_at: '2021-08-20T21:20:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007357911-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA025-Inconsist%C3%AAncia-Erro-no-gatilho-CVD-CODPLA-sec003
---

**Dúvida**Ao vincular uma conta contábil referencial, o sistema está apresentando a inconsistência abaixo:

Inconsistência: Erro no gatilho CVD\_CODPLA sec003

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007641952/mceclip0.png)  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 12.1.17  
  
**Solução**Avaliar as configurações do gatilho CVD\_CODPLA 003 se o mesmo está com a validação conforme ambiente padrão abaixo. Caso esteja diferente, efetue o ajuste do mesmo.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007642152/mceclip2.png)

Antes de realizar o ajuste recomenda-se atualizar o dicionario de dados (SDF.BRA) e UPDDISTR e o geral acumulado

Após atualizar o dicionário ps **Gatilhos** no arquivo **SX7** serão alterados conforme descrito na documentação:[Conversão do Plano de Contas (CTBA020) para MVC](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763)

**Veja mais:**

[Correção no gatilho do campo versão plano contas referencial](http://tdn.totvs.com/pages/releaseview.action?pageId=329030200)
