---
article_id: 4412251756183
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 78f5b2cfe0dd2b785d96ce66f3ca478f169705cfee77a09094a089c8183d2c58
fetched_at: '2026-06-28T22:36:39.221096+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Ponto de entrada
  para modificar o pedido de exportação ao realizar alterações no embarque de exportação
type: support-article
updated_at: '2022-06-09T20:58:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412251756183-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Ponto-de-entrada-para-modificar-o-pedido-de-exporta%C3%A7%C3%A3o-ao-realizar-altera%C3%A7%C3%B5es-no-embarque-de-exporta%C3%A7%C3%A3o
---

**Dúvida**Precisamos de um Ponto de Entrada para modificar o pedido de exportação (**EECAP100**) ao realizarmos qualquer modificação no embarque (**EECAE100**).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Pode ser utilizado o ponto de entrada **FECHAMENTO\_EMBARQUE**no momento que passar por ele:

1. EE7 = Estará posicionada na ordem 1 (**EE7\_FILIAL+EE7\_PEDIDO**) e no pedido que originou o embarque.
2. EE8 = Estará posicionada na ordem 1 (**EE8\_FILIAL+EE8\_PEDIDO+EE8\_SEQUEN+EE8\_COD\_I**) e no primeiro item do pedido que originou o embarque.

Para replicar os dados alterado no embarque para o pedido, será necessário utilziar as variávies de memória, exemplo:

1. Foi modificado o campo **EEC\_FORN** na alteração do embarque de exportação.
2. Para replicar para o Pedido de exportação (**EE7**) será necessário realizar a seguinte atribuição -(**EE7\_FORN := M->EEC\_FORN**).

**Saiba mais**[PE EECAE100 Embarque](https://tdn.totvs.com/display/public/PROT/DT+PE+EECAE100+Embarque)
