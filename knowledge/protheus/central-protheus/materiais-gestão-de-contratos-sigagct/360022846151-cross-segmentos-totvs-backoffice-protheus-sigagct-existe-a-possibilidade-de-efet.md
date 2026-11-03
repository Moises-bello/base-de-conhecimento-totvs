---
article_id: 360022846151
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 958cbbc8e3a8e5703c2192333f0ab5226f66a388b81bcfbeebf51a1fe5b2f3e1
fetched_at: '2026-06-28T22:37:20.047329+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Existe a possibilidade
  de efetuar a Devolução de Saldo da Medição já realizada / encerrada ?
type: support-article
updated_at: '2022-10-06T17:35:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022846151-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Existe-a-possibilidade-de-efetuar-a-Devolu%C3%A7%C3%A3o-de-Saldo-da-Medi%C3%A7%C3%A3o-j%C3%A1-realizada-encerrada
---

**Dúvida**Existe a possibilidade de efetuar a Devolução de Saldo da Medição já realizada / encerrada ?  
  
**Ambiente**Protheus – Gestão de Contratos – A partir da versão 12.17  
  
**Solução**

Esta possibilidade é possível de ser realizada, apenas para Contratos de Compras.

Para efetuar Devolução do Saldo da Medição para o processo de compra, primeiramente o parâmetro **MV\_COMPCDV** precisa estar habilitado, para que, ao realizar a Devolução de Compra feita por um Pedido de Compras gerado pelo SIGAGCT, a quantidade devolvida na NF volte a ficar disponível no Pedido de Compra.

**MV\_COMPCDV** → Altera o status do Pedido de Compra para em aberto após a Devolução.

Mais informações sobre o **MV\_COMPCDV**:  
<https://tdn.totvs.com.br/pages/releaseview.action?pageId=233753468>

Posteriormente, para retornar o Saldo ao Contrato, basta realizar a eliminação de resíduo do pedido de compra, com o parâmetro **MV\_CNRESID** habilitado.

Mais informações sobre o **MV\_CNRESID**:   
<http://tdn.totvs.com.br/pages/releaseview.action?pageId=272417737>

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Retorno do Saldo do Contrato ao Eliminar Resíduo do Pedido de Compras gerado na Medição - MV\_CNRESID](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022848571-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Retorno-do-Saldo-do-Contrato-ao-Eliminar-Res%C3%ADduo-do-Pedido-de-Compras-gerado-na-Medi%C3%A7%C3%A3o-MV-CNRESID?source=search)

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
