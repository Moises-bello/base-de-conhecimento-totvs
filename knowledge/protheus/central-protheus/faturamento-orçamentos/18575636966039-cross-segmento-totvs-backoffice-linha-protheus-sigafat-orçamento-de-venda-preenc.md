---
article_id: 18575636966039
category: Faturamento - Orçamentos
content_hash: a8383692195bc95611fa25a43a09511ae0402a98cf628603b04790f7fd7b08a0
fetched_at: '2026-06-28T22:38:25.024898+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Orçamento de
  Venda preenchendo TES automaticamente - MATA415
type: support-article
updated_at: '2023-10-26T12:53:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18575636966039-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Or%C3%A7amento-de-Venda-preenchendo-TES-automaticamente-MATA415
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18575620250007) Tempo aproximado para leitura: **00:05:00 min****Dúvida:**Orçamento de venda preenchendo o campo **CK\_TES** automaticamente:

**Ambiente:**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução:**Caso não haja um TES informado no campo "**TS Padrão**" (**B1\_TS**) no **Cadastro de Produtos** (**MATA010**) será assumido o código que está no parâmetro **MV\_TESSAI.**

Para que o campo CK\_TES não seja preenchido automaticamente, limpe o conteúdo do parâmetro MV\_TESSAI e o campo não será mais preenchido automaticamente.

![tessai.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/18575614332311)

**Veja Também:**

**[Configurações e Campos para uso da Rotina Orçamento de Vendas (MATA415).](https://tdn.totvs.com/pages/releaseview.action?pageId=271168172)**
