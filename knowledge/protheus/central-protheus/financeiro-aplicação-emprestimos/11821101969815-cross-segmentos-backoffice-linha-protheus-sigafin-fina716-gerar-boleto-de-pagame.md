---
article_id: 11821101969815
category: Financeiro - Aplicação / Emprestimos
content_hash: a979aff79144a2e73a7e2c934e91fe91736f540dc943ab1d34f512b346acb015
fetched_at: '2026-06-28T22:37:59.528519+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA716 - Gerar boleto
  de pagamento para empréstimos
type: support-article
updated_at: '2024-06-12T14:58:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11821101969815-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Gerar-boleto-de-pagamento-para-empr%C3%A9stimos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:08:00 min****Dúvida**Como gerar Boletos de Pagamento de parcelas de empréstimos para efetuar por outras rotinas e não pela FINA716, exemplos: enviar ao banco via CNAB, ou gerar uma fatura para pagamento e negociação.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**Ao gerar as parcelas de pagamento de empréstimos, irá habilitar o campo "**Gerar Parcela**" e mudará o status da parcela para "**Efetivo**"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11820980410007)

Após confirmação, o título "**PR**" da parcela, será baixado e será gerado um título no **Contas a Pagar** do tipo "**BOL**"

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11821022215191)

Neste tipo de título, diferente da rotina antiga **FINA171** onde não era possível enviar parcelas de empréstimo no **Borderô de pagamentos**, poderá ser enviado para pagamento ou ser baixado manualmente no Financeiro via baixas normais.   
  
**Saiba mais**  
[Aplicações e empréstimos - FINA716 - Financeiro P12](https://tdn.totvs.com/pages/viewpage.action?pageId=680254799)
