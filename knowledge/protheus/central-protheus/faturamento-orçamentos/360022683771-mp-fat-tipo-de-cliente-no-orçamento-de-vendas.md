---
article_id: 360022683771
category: Faturamento - Orçamentos
content_hash: aebb2d4a5114338b3808ef7b9ea9777bef89497fb55a1a573932454e613bc4f7
fetched_at: '2026-06-28T22:38:24.986154+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: MP - FAT- Tipo de Cliente no Orçamento de Vendas
type: support-article
updated_at: '2021-04-28T15:15:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022683771-MP-FAT-Tipo-de-Cliente-no-Or%C3%A7amento-de-Vendas
---

**Dúvida**

Existe a possibilidade por padrão de incluir o campo Tipo de Cliente no ORÇAMENTO SCJ, e o mesmo ao ser efetivado, na SC5 ,manter essa informação?

**Ambiente**

Microsiga Protheus - A partir da versão 12.  
  
   
**Solução**

Criado o **Tipo do Cliente** (**CJ\_TIPOCLI**). Ele será inicializado com o conteúdo do campo **Tipo do Cliente** (**A1\_TIPO**) no momento de informar o Código/Loja do Cliente na rotina de Orçamento de Vendas. O usuário poderá, a seu critério, alterar o seu conteúdo. Ao executar a rotina de Aprovação de Vendas para transformar o Orçamento em Pedido de Venda, o conteúdo vigente no campo **Tipo do Cliente** (**CJ\_TIPOCLI**) será considerado no campo correspondente do Pedido de Vendas.

Detalhes em : <http://tdn.totvs.com/pages/viewpage.action?pageId=359471576>
