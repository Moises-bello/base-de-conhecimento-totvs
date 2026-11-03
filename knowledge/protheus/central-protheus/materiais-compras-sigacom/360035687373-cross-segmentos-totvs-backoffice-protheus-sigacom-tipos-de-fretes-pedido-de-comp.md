---
article_id: 360035687373
category: Materiais - Compras (SIGACOM)
content_hash: 77dcb9333d92b792fad2fc35409895cc6285b73eecb354b91241b295219a2338
fetched_at: '2026-06-28T22:41:25.359364+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Tipos de Fretes Pedido
  de Compra
type: support-article
updated_at: '2024-03-05T19:49:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035687373-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Tipos-de-Fretes-Pedido-de-Compra
---

**Dúvida**

Tipos de Fretes - Pedido de Compra  
  
**Ambiente**

Protheus - Compras - A partir da versão 12.1.17  
  
**Solução**

Tipos de Fretes - Definições

* ***CIF***: Cost, Insurance and Freight

O remetente (fornecedor) se responsabiliza pelo pagamento do frete quando a operação for contratada sob a cláusula CIF. Neste caso o estabelecimento vendedor (fornecedor) responde pelo transporte da mercadoria até o estabelecimento destinatário, mediante contratação do serviço de transporte. O valor de frete será destacado na NF e fará parte do valor desta. A contratação e o pagamento do frete ficarão a cargo do estabelecimento vendedor (fornecedor). resumindo é o comprador quem paga o frete, o fornecedor só menciona na nota de saída para o comprador dar entrada na nota com o valor total, ou seja, total de mercadoria + frete.

* ***FOB***: Free On Board

O destinatário (comprador) se responsabiliza pelo pagamento do frete quando a operação for contratada sob a cláusula FOB. Caso em que o estabelecimento comprador (destinatário) assume a responsabilidade pela retirada da mercadoria adquirida, mediante contratação do serviço de transporte. Neste caso o  
estabelecimento comprador irá contratar uma transportadora para execução do serviço de transporte, que não será destacado na NF. Posteriormente esta transportadora enviará uma NF de Conhecimento de frete, que poderá ser vinculada a NF da compra que foi transportada.

* ***POR CONTA DE TERCEIROS***:

Modalidade de frete utilizada quando o custo e responsabilidade sobre frete não é por conta do Emitente, nem do Destinatário/Remetente.

* ***POR CONTA DO DESTINATÁRIO/REMETENTE***:

Modalidade conhecida como FOB (Free on Board – “Livre a bordo”). Nesta opção todo o custo e responsabilidade sobre o frete *estão por conta do Destinatário da Mercadoria*.

* ***REMETENTE***:

Em casos de devolução de mercadoria, quem remete a mercadoria à empresa emissora da nota fiscal é denominando Remetente. Não deve ser confundindo com Emitente (que é o responsável pela Emissão da Nota Fiscal).

* ***SEM FRETE***:

Modalidade utilizada quando não há frete na operação.

***Observações***:

**->** Se o fornecedor informa ao comprador que irá pagar o frete, deverá mencionar na nota de saída para que ao dar entrada o comprador pague o valor do transporte (CIF) mencionada no pedido.

**->** Se o fornecedor informar que não irá cobrar o frete e que é sua a responsabilidade da contratação de uma transportadora e do pagamento do transporte, neste caso após a contratação e recebimento da mercadoria ira receber uma nota de conhecimento de frete que será agregada a nota de entrada origem (FOB) que ficara destacada na nota de conhecimento de frete.

**->** Não temos como incluir um novo tipo de Frete ( **campo C7\_TPFRETE** ), visto que é o fonte MATXFUNA quem cria esse combo dos tipos e nele não há Ponto de entrada disponível para essa situação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21832811234967)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21832831307671)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
