---
article_id: 360039486594
category: Faturamento - Orçamentos
content_hash: 018508d50c765bcb112dc8f8a0550e6d7ec9656d9c97ce76aaa558e61c931eae
fetched_at: '2026-06-28T22:38:24.960703+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Funcionamento do parâmetro
  MV_ORCLIPD
type: support-article
updated_at: '2025-02-14T19:11:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039486594-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Funcionamento-do-par%C3%A2metro-MV-ORCLIPD
---

**Dúvida**

Quando o Orçamento de vendas (**MATA415**) é incluído, o sistema insere por padrão, o código do cliente como "000001" e loja como  "01", como alterar?   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

O parâmetro **MV\_ORCLIPD** é o responsável por carregar o código do cliente e loja padrão para o orçamento.

Caso seja necessário trocar o código e a loja do cliente, ajuste o parâmetro via configurador.

O código do cliente e loja são colocados em seguida, exemplo: 00000101
