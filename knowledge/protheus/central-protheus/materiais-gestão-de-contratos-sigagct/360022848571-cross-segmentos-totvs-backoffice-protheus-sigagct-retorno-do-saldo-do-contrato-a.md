---
article_id: 360022848571
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 37a6cfed607509e84aba70727b0e6bbe5eb17e862b3994b5185892fce9302cef
fetched_at: '2026-06-28T22:37:20.160321+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Retorno do Saldo do
  Contrato ao Eliminar Resíduo do Pedido de Compras gerado na Medição - MV_CNRESID
type: support-article
updated_at: '2026-03-03T17:59:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022848571-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Retorno-do-Saldo-do-Contrato-ao-Eliminar-Res%C3%ADduo-do-Pedido-de-Compras-gerado-na-Medi%C3%A7%C3%A3o-MV-CNRESID
---

**Dúvida**

Como efetuar a eliminação de resíduo de quantidades que sobram ou que não foram atendidas do Pedido de Compras gerado na Medição - MV\_CNRESID

**Ambiente**  
Protheus - Gestão de Contratos – A partir da versão 12.17

**Solução**

A rotina **Eliminar Resíduos (MATA235)**permite o estorno das quantidades ainda não entregues dos Saldos das Planilhas, Cronogramas e Contratos relacionados ao pedido de compras, selecionados para Eliminação do Resíduo.

A Eliminação de Resíduos funciona no momento em que a empresa recebe entradas parciais de materiais, muitas vezes os registros pedidos de compras ficam em aberto por quantidades muito pequenas, insuficientes para que se faça uma nova entrega.

A eliminação de resíduos é um cancelamento das pequenas quantidades que sobram nos pedidos de compras, autorizações de entrega, contratos de parceria e solicitações de compras.

Para que se consiga realizar o retorno do Saldo do Contrato ao Eliminar Resíduo do Pedido de Compras Gerado na Medição vejamos o conceito do parâmetro **MV\_CNRESID.**

**Importante:** O conceito de Eliminação de Resíduos é válido somente para **Contratos do Tipo Compra.**

Parâmetro: **MV\_CNRESID**= S

Configura o sistema para permitir o estorno com as quantidades ainda não entregues dos Saldos das Planilhas, Cronogramas e Contratos relacionados ao pedido de compras, selecionados para Eliminação do Resíduo ou não.

Ao realizar a eliminação de resíduos:

* o saldo eliminado voltará ao contrato na parcela correspondente e o título provisório será recriado no financeiro, com o valor que foi eliminado;
* se o pedido foi parcialmente atendido, a quantidade do pedido (C7\_QUANT) é alterada para a quantidade atendida (C7\_QUJE), para não dar margem para que a nota fiscal seja cancelada e uma nova nota fiscal seja lançada com um valor superior ao saldo consumido do contrato;
* se o pedido não foi atendido (C7\_QUANT), a quantidade do pedido permanece a mesma, mas ele fica com a situação resíduo eliminado.

Caso o ***MV\_CNRESID= N***, não "devolve" o saldo para o contrato.

***Obs1:***

Temos um pedido de compra gerado através de medição, esse pedido foi dado entrada parcialmente, restando um valor que não será utilizado. A duvida é, seria possível voltar esse saldo para o contrato sem estornar o pedido?

***R:*** Com o parâmetro habilitado, ao se Eliminar o Residuo do Pedido gerado na medição, ele tem a funcionalidade retornar o saldo para o contrato, e estornando também a quantidade para o item da planilha e o valor para a competência do Cronograma Financeiro referente a medição que gerou o pedido eliminado resíduo.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Existe a possibilidade de efetuar a Devolução de Saldo da Medição já realizada / encerrada ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022846151-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Existe-a-possibilidade-de-efetuar-a-Devolu%C3%A7%C3%A3o-de-Saldo-da-Medi%C3%A7%C3%A3o-j%C3%A1-realizada-encerrada-?source=search)

[GCT0075\_Eliminação\_Resíduo\_GCT (Parâmetro MV\_CNRESID)](http://tdn.totvs.com/pages/viewpage.action?pageId=272417737)

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
