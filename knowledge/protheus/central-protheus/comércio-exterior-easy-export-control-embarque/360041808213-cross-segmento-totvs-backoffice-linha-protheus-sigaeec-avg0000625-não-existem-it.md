---
article_id: 360041808213
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 21ab1cc8b47d383e55f965ed24001875209255e860567f069e38aff471f67137
fetched_at: '2026-06-28T22:36:39.102285+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - AVG0000625 -
  Não existem itens disponiveis para este processo. '
type: support-article
updated_at: '2021-10-04T12:49:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041808213-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-AVG0000625-N%C3%A3o-existem-itens-disponiveis-para-este-processo
---

**Dúvida**Ao incluir o embarque apresenta a mensagem: AVG0000625 - Não existem itens disponíveis para este processo.?  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055095654/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**

1. Acesse o módulo SIGACFG em Ambiente, selecione Cadastros/Parâmetros.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026597812/mceclip2.png)

2. Selecione ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026592931/mceclip3.png) Pesquisar e Procurar Por: MV\_AVG0067

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410001829015/mceclip0.png)

Com o parâmetro MV\_AVG0067 desabilitado .F. e os itens não faturados, ou seja sem a nota fiscal gerada, a mensagem será apresentada.

Caso o parâmetro MV\_AVG0067 esteja habilitado .T., verifique na EE9 se o item do pedido de exportação encontra-se vinculado a um embarque, pois neste caso o item não possui saldo a ser vinculado a um novo embarque.
