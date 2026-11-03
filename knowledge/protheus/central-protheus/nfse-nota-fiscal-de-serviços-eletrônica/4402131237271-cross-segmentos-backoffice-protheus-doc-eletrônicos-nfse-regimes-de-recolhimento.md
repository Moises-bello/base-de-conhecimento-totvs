---
article_id: 4402131237271
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: a7f36f9b90629ea1e49dda7f1b27801ab465f870ff7f31085647a7e3c2a0e6bf
fetched_at: '2026-06-28T22:39:58.417455+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Regimes de
  Recolhimento - Araxá-MG
type: support-article
updated_at: '2025-06-25T13:20:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402131237271-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Regimes-de-Recolhimento-Arax%C3%A1-MG
---

**Dúvida**Regra de preenchimento do Regime de Recolhimento para NFSE de Araxá-MG.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Documentos Eletrônicos - Todas as versões.  
  
**Solução**O campo no Protheus responsável por alimentar a tag <tsRegRec> no XML é o campo F4\_ISSST (Pagto Imposto) no TES e dependendo do regime, os parâmetros MV\_OPTSIMP e MV\_REGIESP também são usados:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402131111831/mceclip0.png)

Códigos definidos pela prefeitura de acordo com o manual de integração webservice:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402132360855/mceclip1.png)

**De/Para entre Protheus e XML gerado no layout da prefeitura:**

**F4\_ISSST=1** <tsRegRec>00<tsRegRec/>  
**F4\_ISSST=3** <tsRegRec>03<tsRegRec/>  
**F4\_ISSST=4** <tsRegRec>04<tsRegRec/>  
**F4\_ISSST=2** <tsRegRec>07<tsRegRec/>  
**MV\_REGIESP=2** <tsRegRec>08<tsRegRec/>  
**MV\_REGIESP=3** <tsRegRec>09<tsRegRec/>  
**MV\_OPTSIMP=1** <tsRegRec>11<tsRegRec/>  
**MV\_REGIESP=5** <tsRegRec>12<tsRegRec/>
