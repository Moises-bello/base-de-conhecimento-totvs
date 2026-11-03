---
article_id: 360019811032
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: de62130bccd86c129a8a11b7434f97b949a01cd557e1f4d05d0e7bda34b5364f
fetched_at: '2026-06-28T22:38:41.092082+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Array out of
  bounds na função A410REMBEN
type: support-article
updated_at: '2021-09-21T20:26:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019811032-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Array-out-of-bounds-na-fun%C3%A7%C3%A3o-A410REMBEN
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**

Ao vincular um item que vai para beneficiamento com a OP usando o botão **Beneficia** do pedido de vendas é gerado errorlog: **array out of bounds ( 0 of 101 ) on A410REMBEN(MATN410A.PRW).**

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGAFAT - a partir da versão 12.

**Causa**

O erro ocorre por o campo **C6\_QTDLIB2** está com o uso desmarcado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409098926103/mceclip0.png)

O erro também pode ocorrer com os campos **C6\_PRODUTO, C6\_TES, C6\_LOCAL, C6\_ITEM, C6\_QTDVEN, C6\_UNSVEN, C6\_LOTECTL, C6\_NUMLOTE, C6\_DTVALID,  C6\_LOCALIZ,  C6\_NUMSERI,  C6\_QTDLIB,  C6\_QTDLIB2, C6\_PRCVEN e C6\_VALOR,** pois todos estes campos fazem parte do array da rotina **A410REMBEN**.

Se o **nível de campo** dos campos que compõem o array ,estiver diferente do padrão que é 1, ou a houver **falta** de um dos campos que fazem parte do array, no Dicionários de Dados,  também gerará o erro de array da função **A410REMBEN**,

**Solução**

Via configurador, Dicionário de Dados, alteração da tabela SC6 - itens de pedido de vendas, localize o campo em questão, marque-o como usado e valide se o nível do campo está igual a 1, não estando, ajuste-o também.

Salve a alteração do campo e da tabela, atualize o dicionário de dados, reinicie o smartclient e efetue o pedido novamente.

Para o caso de falta de campo no Dicionário de Dados, é necessário efetuar o download do **Dicionário de Dados** no portal do cliente, conforme a sua release de uso e posteriormente, processar o **UPDDISTR** para que o ambiente assuma a atualização de Dicionário de Dados.

Feito o procedimento, reinicie o Protheus e efetue o processo novamente.
