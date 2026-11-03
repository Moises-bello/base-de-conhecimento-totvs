---
article_id: 20432151534103
category: Materiais - Compras (SIGACOM)
content_hash: a9873ebecf07e9f98ca8a7ebf159738bd07720a6ffc4bcea7b9679b9ce5a301d
fetched_at: '2026-06-28T22:41:20.147582+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA121 - O sistema
  rateia o valor do frete para um item que foi Eliminado Resíduo?
type: support-article
updated_at: '2024-01-09T11:56:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20432151534103-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA121-O-sistema-rateia-o-valor-do-frete-para-um-item-que-foi-Eliminado-Res%C3%ADduo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20432137953303) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao informar o valor total do frete (C7\_FRETE) no pedido de compras, o sistema rateia o valor do frete (C7\_VLRFRET) em item que foi eliminado o resíduo (C7\_RESIDUO=S)?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Protheus Compras - A partir da versão 33  
  
**Solução**Sim, uma vez que o item faz parte do pedido, ele constitui o valor total desse pedido. Dessa forma, mesmo que seja eliminado resíduo desse item, ele continuará constituindo o valor total do pedido. Sendo assim, o valor do frete será rateado proporcionalmente ao valores unitários.

* O valor de frete informado no pedido de compras sempre será baseado no **TOTAL** do pedido
  + Pedido de Compras (PC001) com 3 itens e valor do frete R$ 120,00

| Item | Quantidade | Valor | Total | Vlr Frete |
| --- | --- | --- | --- | --- |
| 0001 | 1 | 140,00 | 140,00 | (70%) = 84,00 |
| 0002 | 1 | 40,00 | 40,00 | (20%) = 24,00 |
| 0003 | 1 | 20,00 | 20,00 | (10%) = 12,00 |

* Documento de Entrada (Proporcional será calculado conforme configurado parâmetro MV\_FRT103E)
  + Vincular apenas item 0001 / 0002 com uma quantidade menor

| Item NF | PC | Item PC | Quantidade | Valor | Total | Vlr Frete |
| --- | --- | --- | --- | --- | --- | --- |
| 0001 | PC001 | 0001 | 0,5 | 140,00 | 70,00 | * Se MV\_FRT103E = .T.   + 42,00 |
| 0002 | PC001 | 0002 | 0,5 | 40,00 | 20,00 | * Se MV\_FRT103E = .T.   + 12,00 |

* + Com o MV\_FRT103E = T totalizou no documento R$ 54,00 dos R$ 120,00 no PC001

* Pedido de Compras (PC001) atualizado

| Item | Qtd Atendida | Quantidade | Valor | Total | Vlr Frete |
| --- | --- | --- | --- | --- | --- |
| 0001 | 0,5 | 1 | 140,00 | 140,00 | 84,00 |
| 0002 | 0,5 | 1 | 40,00 | 40,00 | 24,00 |
| 0003 | 0 | 1 | 20,00 | 20,00 | 12,00 |

* Eliminação de Resíduo (PC001 / Item 0001)

| Item | Qtd Atendida | Quantidade | Valor | Total | Vlr Frete | Encerrado/Resíduo |
| --- | --- | --- | --- | --- | --- | --- |
| 0001 | 0,5 | 1 | 140,00 | 140,00 | 84,00 | S |

* Novo Documento de Entrada, vinculando os 2 itens restantes do PC001

| Item NF | PC | Item PC | Quantidade | Valor | Total | Vlr Frete |
| --- | --- | --- | --- | --- | --- | --- |
| 0001 | PC001 | 0002 | 0,5 | 40,00 | 20,00 | * Se MV\_FRT103E = .T.   + 12,00 |
| 0002 | PC001 | 0003 | 1 | 20,00 | 20,00 | * Se MV\_FRT103E = .T.   + 12,00 |

* + Com o MV\_FRT103E = T totalizou no documento R$ 78,00 dos R$ 120,00 no PC001

**Obs: Frete nos 2 documentos totalizou os R$ 78,00 dos R$120,00, os R$ 42,00 restantes foram eliminado, via eliminação de resíduo.**

**Parâmetro: MV\_FRT103E**

* Se MV\_FRT103E = .T. (default), Sempre irá proporcionalizar o frete ao alterar o item.  
  **Exemplo**: Quantidade do item: 1000 unidades, Frete: 100. Ao alterar a quantidade para 900, frete será proporcionalizado para 90.
* Se MV\_FRT103E = .F., não irá proporcionalizar o frete ao alterar o item.  
  **Exemplo**: Quantidade do item: 1000 unidades, Frete: 100. Ao alterar a quantidade para 900, frete continuará 100.

Para habilitar o valor do frete na linha do item do pedido de compras, será necessário seguir a documentação abaixo.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como informar o valor do frete item a item no pedido de compra](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035974093-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-informar-o-valor-do-frete-item-a-item-no-pedido-de-compra)

**Saiba Mais:**

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [PCOM04031 - Pedido de Compras - Rateio Valor de Frete](https://tdn.totvs.com.br/display/public/PROT/PCOM04031+-+Pedido+de+Compras+-+Rateio+Valor+de+Frete)
* [MV\_FRT103E](https://tdn.totvs.com.br/pages/viewpage.action?pageId=668182088)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como informar o valor do frete item a item no pedido de compra](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035974093-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-informar-o-valor-do-frete-item-a-item-no-pedido-de-compra)
