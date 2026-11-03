---
article_id: 7944057447575
category: Financeiro
content_hash: 8a24fabdff19915977da7322f57577ed4448681357dfcbe3892ff2b7581a9f43
fetched_at: '2026-06-28T22:38:03.258045+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Help TITPGPIXCART  '
type: support-article
updated_at: '2022-10-19T20:55:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7944057447575-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Help-TITPGPIXCART
---

**Ocorrência**No módulo Financeiro, ao tentar realizar alterações na natureza, descrição ou vencimento do título o sistema apresenta o Help TITPGPXCART  
Conforme print abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7927332370199/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
 **Causa**É apresentado este Help, pois o título não pode ser alterado e foi originado pela rotina de Venda Assistida, vinculado aos pagamentos de PIX, Cartão de crédito ou débito.

Importante: é possível visualizar a origem do título através da tabela SE1 campo E2\_ORIGEM.

**Solução**Por regra de negócio e integridade não pode ser alterado nenhuma informação dos títulos gerados pela Venda Assistida.

**Saiba mais:**[DT Alteração de títulos originados pela rotina LOJA701 e pago com PIX ou cartões de crédito e débito](https://tdn.totvs.com/pages/releaseview.action?pageId=696692341)
