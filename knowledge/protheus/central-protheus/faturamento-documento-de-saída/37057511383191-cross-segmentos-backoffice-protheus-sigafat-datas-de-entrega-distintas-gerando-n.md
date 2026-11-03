---
article_id: 37057511383191
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 7bd28a8944be45b7b2e0e054d37270b3457665fbd5161dab38ddaae31196d09f
fetched_at: '2026-06-28T22:38:44.027808+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Datas de entrega distintas
  gerando notas fiscais diferentes ao faturar
type: support-article
updated_at: '2025-12-16T14:59:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37057511383191-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Datas-de-entrega-distintas-gerando-notas-fiscais-diferentes-ao-faturar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37057504897559) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Por que datas de entrega distintas estão gerando notas fiscais diferentes ao faturar?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**  
De acordo com a lei **NT 2025.002, itens do pedido de venda com data de entrega (C6\_ENTREG) diferente entre si, serão repartidos e gerarão novas notas fiscais ao faturar, mesmo que todos os campos abaixo estejam de acordo.**

Assim, cada entrega diferente no item (campo C6\_ENTREG), será colocado em uma nova nota fiscal, onde levarão esse valor a data de entrega do cabeçalho da nota fiscal de saída (campo F2\_DTENTR)

**Mesmo em um mesmo pedido, caso as linhas tenham datas distintas de entrega serão geradas múltiplas notas, de acordo com as datas.**

**Fluxograma do valor 1:**

Entrega do cabeçalho do pedido de venda (Campo C5\_FECENT) pode ou não passar o dado para o campo C6\_ENTREG, que passa para o campo da liberação do pedido de venda (campo C9\_DATENT), que ao faturar leva ao campo do cabeçalho da nota fiscal (campo F2\_DTENTR) que ao transmitir gera a tag dPrevEntrega.

**Fluxograma do valor 2:**

Antes faturar, na tela de perguntes onde, por exemplo, fica o pergunte "Aglutina pedidos iguais", agora há o pergunte (MV\_PAR28) "Dt. Entreg" onde se preenchido, é levado diretamente ao cabeçalho da nota fiscal (campo F2\_DTENTR), não interferindo nos demais campos C6\_ENTREG e C9\_DATENT, porém não serão respeitados e podem ficar diferentes do campo F2\_DTENTR.

**Saiba mais:**

[**Data prevista de entrega**](https://tdn.totvs.com/x/flCZP)

[**Notas de Débito (NF-e: finNFe = 6 - NT 2025.002)**](https://tdn.totvs.com/x/MZ5qP)
