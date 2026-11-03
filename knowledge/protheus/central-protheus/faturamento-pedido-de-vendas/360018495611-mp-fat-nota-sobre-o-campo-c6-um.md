---
article_id: 360018495611
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 16fbbd805301f5317fefc5caf0e167cb43256ae80b6d617b99488aaf61f58b0d
fetched_at: '2026-06-28T22:38:42.801875+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP-FAT- Nota sobre o campo C6_UM
type: support-article
updated_at: '2021-04-28T15:51:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018495611-MP-FAT-Nota-sobre-o-campo-C6-UM
---

**Dúvida**Ao alterar o campo unidade do produto, não altera o campo de unidade no pedido de venda.  
   
 **Ambiente**Microsiga Protheus- desde versões anteriores à 12.  
  
**Solução**

Trata-se de conceito da rotina.

Por padrão da rotina de Pedido de Venda, as informações do produto não serão atualizadas na linha do item quando o usuário tentar digitar o mesmo código, ou teclar <ENTER> sobre o código do produto ou efetuar a busca via <F3> do mesmo produto. As informações não são atualizadas para garantir a integridade dos dados que foram eventualmente alterados pelo usuário.

Para ver exemplo de uso, consulte a FAQ: **[Nota sobre o campo C6\_UM](http://tdn.totvs.com/display/PROT/FAT0277+-+Nota+sobre+o+campo+C6_UM)**
