---
article_id: 16286467873047
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e11e379318980ed5241a78f72712b66215069151822a41b59330dd84b54947a7
fetched_at: '2026-06-28T22:38:33.100395+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - Eliminar resíduo
  de Pedido de Vendas
type: support-article
updated_at: '2025-05-20T14:47:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16286467873047-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Eliminar-res%C3%ADduo-de-Pedido-de-Vendas
---

**Dúvida:**

Eliminar resíduo de Pedido de Vendas  
  
**Ambiente:**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - todas as versões.  
  
**Solução:**

Quando um Pedido de Vendas é faturado parcialmente, ou seja, a nota fiscal é emitida com referência a apenas alguns produtos ou quantidade parcial dos pedidos, seu saldo é chamado de resíduo, significando que não foi entregue ao cliente.

Este faturamento parcial ocasiona valores mínimos que não compensam ser faturados. Os limites mínimos são variáveis de região para região, pois devem ser levados em consideração os custos do transporte para que sejam compensadores.

O sistema grava o código de bloqueio "**R**" no campo "**Status Blq" (****C6\_BLQ)** indicando que o item está bloqueado - não será mais faturado devido à eliminação de resíduo.

A Eliminação de Resíduo pode ser realizada  de duas formas:

1-) Individualmente  pela rotina MATA410  selecionando o Pedido de Venda e clicando no  Botão Outras Ações > Excluir> Resíduos ;

2-) Através da rotina MATA500, preenchendo os Parâmetros, clicando no checkbox dos Pedidos de Venda > Botão Selecionar> Ok

![resi.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/16286440195351)

***OBSERVAÇÕES:***

* **Status:** Quando o Pedido é encerrado por ter sido parcialmente faturado e o restante eliminado resíduo (ou por ter sido totalmente faturado) o Pedido recebe o Status Vermelho - Encerrado com base no campo **C5\_NOTA**.  
  Se faturado 100% o **C5\_NOTA** recebe o número da última Nota Faturada. Se eliminado resíduo, recebe o conteúdo XXXXXX (6 ou 9 dígitos).
* Detalhes em:   
  [Legendas exibidas na rotina MATA410 - Pedido de Vendas](https://tdn.totvs.com/display/PROT/FAT0121_Legendas_Status_do_Pedido_de_Vendas)

* **Cancelar a Eliminação de resíduo:** Se a eliminação de resíduo foi executada indevidamente para o Pedido, é possível "desfazer" alterando o campo "**Status Blq" (C6\_BLQ)** no Pedido de Vendas, de "**R**" para "**N**".  
  **Obs.**: Para isto é necessário que o sistema esteja configurado de modo a permitir aproveitar itens eliminados por resíduo através do parâmetro (**MV\_RSDOFAT)**e edição de Pedido de Vendas encerrado no parâmetro  **(MV\_ALTPED).**
* Para isto é necessário que o sistema esteja configurado de modo a permitir edição de Pedido de Vendas encerrado (MV\_ALTPED).
* **Valores / Quantidades do Pedido:** Ao eliminar resíduo, os valores (assim como as quantidades) não são alterados ou subtraídos do Total do Pedido. Apenas registra-se o campo de Bloqueio para que aquele resíduo não seja mais liberado/faturado.
* **Rotina Automática:** A rotina de eliminação de resíduos não permite execução via rotina automática, pois depende da ação do usuário.

**Veja mais:**

**[FAT0227\_Eliminar Resíduo de Pedido de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=285655735)**
