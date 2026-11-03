---
article_id: 38170459549719
category: Financeiro - Contas a Receber - PIX
content_hash: 8a6ceb0004f22d026af20002e1811bd1491ef24a697ff7dc9c1ea09600ff5d42
fetched_at: '2026-06-28T22:38:16.458661+00:00'
product: protheus
section_id: 1500001539301
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - Ao incluir
  título no contas a receber está ficando com a legenda laranja
type: support-article
updated_at: '2026-02-04T20:03:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38170459549719-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Ao-incluir-t%C3%ADtulo-no-contas-a-receber-est%C3%A1-ficando-com-a-legenda-laranja
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38170459525655) Tempo aproximado para leitura: **00:03 min**  
  
**Dúvida**  
Por que, ao incluir um título no contas a receber, o mesmo está ficando com legenda laranja ao invés de verde?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Este cenário ocorre porque, no momento da inclusão, está configurado no **complemento do título**, conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38170445606295)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38170445607447)

O título será gerado conforme a imagem a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38170459531159)

Caso seja necessário alterar a legenda após a inclusão do registro, uma vez que o recebimento não ocorrerá via PIX, é possível ajustar o título por meio do **complemento do título**, atualizando o campo **“Gera PIX”** para a opção **“2 – NÃO”**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38170459532695)

**Saiba mais**

[Pagamentos instantâneos - PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)
