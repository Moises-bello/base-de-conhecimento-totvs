---
article_id: 4851536569879
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b19a6177c519cbb4fff78ad8d9a49c498f2978ce33c06cfd86e42e01892d3551
fetched_at: '2026-06-28T22:38:38.554608+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Liberação de
  campo de desconto para usuário
type: support-article
updated_at: '2022-03-18T14:42:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4851536569879-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Libera%C3%A7%C3%A3o-de-campo-de-desconto-para-usu%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como liberar o campo de desconto do pedido de venda?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

Por padrão de sistema, os campos de desconto do pedido de venda (**C5\_DESC1...4, C5\_DESCONT, C5\_PDESCAB, C6\_DESCONT, C6\_VALDESC**), não possuem restrição de acesso para os usuários.

Certifique que os campos não estejam, configurados com o modo de edição igual a falso (.F.), neste caso é preciso retirar a validação para uso do campo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4851370734103/mceclip0.png)

Outra coisa que pode ser verificado é se há validação de usuário no campo que possa impedir o usuário de acessar o mesmo, neste caso, também  deve ser retirado para que o usuário possa digitar no campo ou avaliado om a equipe de TI o porque da restrição:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4851399859351/mceclip1.png)
