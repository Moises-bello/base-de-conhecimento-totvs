---
article_id: 25144803768215
category: Financeiro
content_hash: f16ed641c6739d7f67081e736052557664d87e9491b44f9c2f6c1e07292c559c
fetched_at: '2026-06-28T22:38:03.038095+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA450 - É possível
  compensar um título do contas a receber com um título do contas a pagar
type: support-article
updated_at: '2026-04-14T18:34:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25144803768215-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA450-%C3%89-poss%C3%ADvel-compensar-um-t%C3%ADtulo-do-contas-a-receber-com-um-t%C3%ADtulo-do-contas-a-pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25191503805591) Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**  
É possível compensar um título do contas a receber com um título do contas a pagar?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

Essa funcionalidade permite realizar a compensação entre títulos a pagar e títulos a receber, desde que sejam do mesmo tipo.

Ou seja, possibilita a compensação entre títulos de débito do contas a pagar com títulos de débito do contas a receber, bem como entre títulos de crédito do contas a pagar com títulos de crédito do contas a receber.

Dessa forma, facilita o encontro de contas entre fornecedor e cliente, permitindo a baixa simultânea dos títulos a pagar e a receber.

Os tipos de títulos

* **Títulos de débito:** exemplos incluem **NF (Nota Fiscal), BOL (Boleto)**, entre outros documentos de débito.
* **Títulos de crédito:** incluem **PA (Pagamento Antecipado), RA (Recebimento Antecipado)**, além de títulos de devolução como **NDF (Nota de Débito Fiscal)** e **NCC (Nota de Crédito Comercial).**

Essa rotina possibilita que esses diferentes tipos de títulos sejam compensados de maneira eficiente, promovendo o acerto de contas entre as partes envolvidas.

![Gravar_2024_07_24_17_55_11_459.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25144803722647)

Na **SE5** será gerado o registro para cada **NF** com o tipo **BA (não gera movimentação bancária)** no campo **E5\_TIPODOC**

**Importante**

Não é permitido realizar a compensação entre títulos de tipos diferentes. Ou seja, não é possível compensar uma nota de débito a receber com uma nota de crédito a pagar.

* **Notas de débito**: representam valores a receber.
* **Notas de crédito**: representam valores já recebidos.

Por esse motivo, não é possível compensar um valor já recebido com um valor que ainda precisa ser pago, e vice-versa.

Essa rotina tem como objetivo realizar a compensação entre registros equivalentes, eliminando os valores entre as notas, de modo que não haja geração de movimentação bancária.

**Saiba mais**  
[Compensação entre carteiras - FINA450](https://tdn.totvs.com/pages/releaseview.action?pageId=516194467)

[Descrições dos tipos de movimentações do campo E5\_TIPODOC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022538171-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Descri%C3%A7%C3%B5es-dos-tipos-de-movimenta%C3%A7%C3%B5es-do-campo-E5-TIPODOC)

[Relatório de títulos compensados por compensação entre carteiras - FINR520](Cross%20Segmentos%20-%20Backoffice%20Linha%20Protheus%20-%20SIGAFIN%20-%20%20FINA450%20-%20Qual%20relat%C3%B3rio%20visualiza%20t%C3%ADtulos%20compensados)
