---
article_id: 28686739061143
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: df5d09f92c0dab88fb6b50459d519139170a0bd25cb88df5e9a84a1b9624c3a8
fetched_at: '2026-06-28T22:38:42.555506+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFAT - Help A410NSALDO
type: support-article
updated_at: '2024-12-20T20:06:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28686739061143-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-Help-A410NSALDO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28686747186711) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Como resolver o Help **A410NSALDO** na Devolução de Compra no Pedido de Venda?

**Ambiente**Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões;  
  
**Causa**O Help verifica se a quantidade informada no campo "Quantidade (**C6\_QTDVEN**)" do pedido de devolução excede a quantidade registrada no campo "Quantidade (**D1\_QUANT**)" da Nota Fiscal de Origem.

**Solução**Isso pode ocorrer devido a devoluções anteriores já realizadas, divergências na padronização das casas decimais que geram inconsistências, ou pela falta de cálculo adequado da quantidade restante em casos de devolução parcial. Portanto, existem essas principais soluções:

* **Para Devoluções Anteriores:**

  Verifique no histórico se já houve devoluções para o mesmo item e ajuste a quantidade solicitada.
* **Para Divergências em Casas Decimais:**

  Certifique-se de que as configurações de casas decimais estão padronizadas no sistema.
* **Para Devoluções Parciais:**

  Subtraia manualmente os valores **D1\_QUANT - D1\_QTDEDEV**, para saber a quantidade que ainda pode ser devolvida.

**Observações**

Em casos de **Exclusão de Notas Faturadas na Rotina MATA521A:**

* Quando uma nota de devolução faturada é excluída pela rotina **MATA521A**, é fundamental excluir também o pedido correspondente (mesmo que esteja em aberto ou liberado).
* O sistema não atualiza automaticamente o campo **D1\_QTDEDEV** ao excluir apenas pela rotina, causando inconsistências nos valores de devolução.
* Após excluir o pedido, refaça o processo de devolução para corrigir os valores.

**Saiba mais**

**[FAT0007 Realizar uma Devolução de Compras](https://tdn.totvs.com/x/g0FtDQ)**

[Cross Segmentos - Backoffice Protheus - SIGAFAT - Como fazer uma devolução de compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022341592-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-fazer-uma-devolu%C3%A7%C3%A3o-de-compras)

[Cross Segmentos - Backoffice Protheus - SIGAFAT - Casas decimais no Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001427308-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Casas-decimais-no-Faturamento?source=search)
