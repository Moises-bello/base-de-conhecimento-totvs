---
article_id: 21508586743063
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 655f3676bf77e8b5b797d569900199d3a6f9db00253eeb320638f6d28c8200cd
fetched_at: '2026-06-28T22:39:44.473854+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ao associar adiantamento
  ao fornecedor na invoice, é apresentado o Help  M020VALID
type: support-article
updated_at: '2024-02-21T19:32:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21508586743063-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ao-associar-adiantamento-ao-fornecedor-na-invoice-%C3%A9-apresentado-o-Help-M020VALID
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21508594989335) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao associar adiantamento ao fornecedor na invoice, é apresentado o **Help M020VALID.**

![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21508594989591)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Import Control – A partir da versão 12.1.33  
  
**Solução**

O Help é apresentado, pois, o campo **FK2\_NATURE** está sendo buscado na tabela **SED - Naturezas** e não está sendo localizado.

Nesse caso, é necessário confirmar o cadastro da Natureza na rotina **FINA010** e certificar que o registro da natureza não está bloqueado (**ED\_MSBLQL = '2 - Nao'** significa que não está bloqueado).  
  
**Saiba mais:**

[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Adiantamento por Fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025754692-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Adiantamento-por-Fornecedor)

[Pagamento antecipado para a purchase order](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000091867-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Pagamento-antecipado-para-a-purchase-order)  
[Naturezas - FINA010 - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Naturezas+-+FINA010+-+Financeiro+-+P12)
