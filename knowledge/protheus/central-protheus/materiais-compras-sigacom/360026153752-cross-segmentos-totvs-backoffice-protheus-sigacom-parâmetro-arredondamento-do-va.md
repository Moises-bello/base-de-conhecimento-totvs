---
article_id: 360026153752
category: Materiais - Compras (SIGACOM)
content_hash: da9e2caa72cc5003f9336c7f1f1a1f03c198714f90d07178889b810e916edc20
fetched_at: '2026-06-28T22:41:10.141282+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Parâmetro arredondamento
  do Valor Total do Pedido de Compras - MV_ARRPEDC
type: support-article
updated_at: '2022-09-26T16:44:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026153752-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Par%C3%A2metro-arredondamento-do-Valor-Total-do-Pedido-de-Compras-MV-ARRPEDC
---

**Dúvida**Parâmetro arredondamento do Valor Total do Pedido de Compras - MV\_ARRPEDC

**Ambiente**Protheus - Compras - A partir da versão 11  
  
**Solução**Parâmetro MV\_ARRPEDC define o arredondamento do valor total do item do Pedido de Compras (MATA120)

* O cálculo efetuado utiliza a regra definida neste parâmetro e sobrepõe a contagem realizada   
  pelo gatilho padrão do sistema. As opções disponíveis para o parâmetro são:  
    
  • **ROUND** --> Efetua o arredondamento do valor total, de acordo com a quantidade de casas decimais do campo Vlr. Total (C7\_TOTAL)  
    
  • **NOROUND -**-> Não efetua o arredondamento do valor total. Se o conteúdo do parâmetro estiver em branco ou for inválido, o cálculo do valor total continuará sendo efetuado pelo gatilho padrão do sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025617812/mceclip0.png)

Saiba Mais:

[MV\_ARRPEDC - Arredondamento do valor total do Pedido de Compras](https://tdn.totvs.com/display/public/PROT/MV_ARRPEDC+-+Arredondamento+do+valor+total+do+Pedido+de+Compras)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
