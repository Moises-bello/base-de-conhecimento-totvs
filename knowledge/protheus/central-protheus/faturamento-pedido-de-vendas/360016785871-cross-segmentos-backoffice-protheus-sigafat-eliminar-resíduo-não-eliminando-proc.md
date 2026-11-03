---
article_id: 360016785871
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 16767dacdae8483740c26cb9d865e0f24648d4e379912c1a3b3f0915df7a1285
fetched_at: '2026-06-28T22:38:39.779431+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Eliminar resíduo não eliminando
  (processando)
type: support-article
updated_at: '2025-04-30T17:36:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016785871-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Eliminar-res%C3%ADduo-n%C3%A3o-eliminando-processando
---

**Ocorrência:**Ao acionar a eliminação de resíduos de um pedido de vendas o mesmo não encerrado/processado.  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

* Este Pedido já foi parcialmente faturado? É necessário que sim. Se o Pedido não será entregue, por completo recomenda-se excluir o Pedido. Como o nome da própria rotina indica, elimina apenas resíduo, então neste caso não será eliminado.  
  Se houver dúvida, verifique no campo D2\_PEDIDO se é localizado algum registro em Nota já emitida para esse Pedido.
* Este Pedido tem relação com operação para Controle de Poder de Terceiro (TES preenchido com F4\_PODER3 igual a Remessa ou Devolução / Campo C6\_NFORI preenchido com uma Nota que controla Poder de Terceiro)?  
  Neste caso não será eliminado, pois se o produto é de terceiro e em teoria deve ser totalmente retornado (não há opção de eliminar o resíduo de terceiro).]
* Esse pedido é oriundo de integração ( campo "Origem (C5\_ORIG)" preenchido)? Se sim, só pode ser eliminado o resíduo unitariamente por vez, no "Pedidos de venda (MATA410) > "Outras ações" > "Excluir" > "Resíduo".  
  O fluxograma foi desenhado assim, pela necessidade de mitigar demais integrações, onde é importante ter o controle de saldo.

* Este Pedido (esta quantidade que está tentando eliminar) já foi submetido à Liberação (possui registro na Tabela SC9)? Caso já tenha sido liberado para Faturar, **não será eliminado o resíduo**. É necessário estornar a liberação e então, posteriormente, eliminar o resíduo.  
  Certifique-se se há quantidade liberada verificando se há conteúdo no campo C6\_QTDEMP (**Quantidade liberada, porém não faturada**). Também é possível identificar acessando a rotina Documentos de Saída **MATA460A** e verificando se aparece algum registro para esse Pedido com legenda diferente de vermelho (**ou seja, ainda não faturado**). Para estornar a liberação na rotina Docs de Saída **MATA460A > Outras Ações > Estornar liberação** (**ou, no próprio Pedido de vendas** **clique em "Alterar" e em seguida "Confirmar",** pois alteração do Pedido estorna as liberações.
* Os parâmetros de entrada da Rotina estão corretamente preenchidos?  
  Atente-se ao primeiro pergunte que indica o percentual máximo de eliminação do item. Caso a quantidade vendida seja relativamente baixa, de modo que o percentual a ser eliminado é superior ao limite determinado nedde pergunte, o resíduo não será eliminado.  
    
  **OBS:** Nestes casos deve-se ajustar o percentual máximo; ou eliminar o resíduo direto no Pedido de Vendas (*Seleciona Pedido > Outras ações > Excluir > Resíduo*) no qual não é exibida Tela de parâmetros; ou então faturar a quantidade razoável de acordo a cumprir com este limite de eliminação determinado.
* O campo C6\_ENTREG (Data de entrega) do item deve estar preenchido.  
    
    
  **Saiba mais:**  
  [Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - Eliminar resíduo de Pedido de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16286467873047-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Eliminar-res%C3%ADduo-de-Pedido-de-Vendas)
