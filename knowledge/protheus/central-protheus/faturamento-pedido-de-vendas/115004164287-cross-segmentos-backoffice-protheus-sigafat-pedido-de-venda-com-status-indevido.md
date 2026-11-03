---
article_id: 115004164287
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 78e61df299c9fcc2f9d805a8d3bdb822a34f0c526b07789ee4493ba55632cd65
fetched_at: '2026-06-28T22:38:39.935399+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Pedido de Venda com status
  indevido de bloqueado (ou indevidamente liberado) por Estoque
type: support-article
updated_at: '2026-03-10T11:35:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004164287-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pedido-de-Venda-com-status-indevido-de-bloqueado-ou-indevidamente-liberado-por-Estoque
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16372917207703)** Tempo aproximado para leitura: **00:03:30 min**  
  
**Dúvida**  
Por que meu Pedido de Venda foi bloqueado (ou liberado) indevidamente por Estoque e como posso verificar a causa?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**  
O status de bloqueio ou liberação de um Pedido de Venda por Estoque é regido por algumas validações de parâmetros, saldos e configurações da operação. As principais para identificar a causa, podem ser verificadas a partir das seguintes etapas:

|  |
| --- |
| Assista nosso vídeo How To com mais detalhes do passo a passo abaixo:  [How To | MP - SIGAFAT - Bloqueio indevido de estoque](https://www.youtube.com/watch?v=Hzlg--lGieg&t=57s) |

1 - Confirmação do Bloqueio e Causa Raiz:

| **Campo/Validação** | **Descrição** |
| --- | --- |
| **C9\_BLEST = 02** | Confirme se o Item do Pedido de Venda (MATA410) está realmente bloqueado por **Estoque**. |
| **C9\_BLWMS** | Se este campo tiver conteúdo, o bloqueio é gerado pelo módulo **SIGAWMS** (Gestão de Armazenagem). |
| **Liberação Manual** | Se a Liberação do Estoque foi realizada pela opção Manual, o sistema desconsidera o saldo e pode Liberar o Pedido, deixando o saldo Negativo (causa de *liberação indevida*). |

2 - Avaliação de Parâmetro:

| **Parâmetro e Conteúdo** | **Efeito (Bloqueio / Liberação Indevida)** |
| --- | --- |
| **MV\_AVALEST =** **3** | Bloqueia **todos** os faturamentos por **Estoque**, obrigando a liberação pela rotina (MATA330). (Bloqueio esperado). |
| **MV\_QEMPV =** **.F.** | O saldo empenhado para Ordem de Produção (OP) é considerado Disponível, o que pode evitar o bloqueio mesmo com OP aberta. (Pode gerar *liberação indevida*). |
| **MV\_GERABLQ =** **N** | O bloqueio de **Estoque** é desconsiderado para produtos que controlam Rastro/Localização. (Pode gerar *liberação indevida*). |

3. Validação do Saldo e Tipo de Liberação Local:

| **Configuração** | **Checagem** | **Efeito (Bloqueio / Liberação Indevida)** |
| --- | --- | --- |
| **Saldo Disponível** | A quantidade disponível deve ser maior que a Qtd. Reservada (**B2\_RESERVA**) | O saldo reservado é considerado indisponível para novos pedidos. |
| **Qt. Ter. Ns. Pd. (B2\_QTNP)** | Se este campo tiver valor, este saldo não está disponível para venda, pois pertence a terceiros. | Se for maior que a Qtd. Disponível, causará o bloqueio. |
| **C5\_TIPLIB** | Se o campo "Tipo de Liberação" for 2 - Por Pedido | A falta de Estoque em apenas um item bloqueará o pedido inteiro. (Bloqueio esperado). |
| **Lote/Endereço** | Se o produto controla Lote (B1\_RASTRO) ou Endereço (B1\_LOCALIZ). | O saldo deve ser validado no Lote/Endereço específico, conforme registrado em C6\_LOTECTL ou C6\_LOCALIZ. |
| **TES (F4\_ESTOQUE)** | O TES no Pedido de Venda deve ter F4\_ESTOQUE = S - Sim. | Se for N, o Estoque não será atualizado/validado. |
| **F4\_SLDNPT** | Se o campo Saldo em Poder de Terceiros for 1 - Disponível para faturamento. | O sistema utiliza Saldo Nosso em Poder de Terceiro, o que pode evitar o bloqueio mesmo sem saldo em Estoque. (Pode gerar *liberação indevida*). |
| **F4\_PODER3** | Para pedidos de Retorno de Saldo de Terceiros. | O TES deve ter Poder Terc. (F4\_PODER3) = D - Devolução. |

**Saiba mais:**

* Consulte mais detalhes no *link*: [Liberação / Bloqueio “indevido” de Estoque](https://tdn.totvs.com/x/zGk-Dg)
* Webinar: [Análise e Bloqueio de Estoque no Faturamento (SIGAFAT)](https://youtu.be/6XfctVxULuY)
* [Cross Segmentos - Backoffice Protheus - SIGAFAT - Como identificar e liberar bloqueios do Pedido de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014207291-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-identificar-e-liberar-bloqueios-do-Pedido-de-Vendas)
