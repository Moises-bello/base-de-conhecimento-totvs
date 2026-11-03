---
article_id: 7250697863191
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 436207e3748ef04bdb075ee06303c3dfc647bc18bc83ea2ab096569a276df929
fetched_at: '2026-06-28T22:38:41.325435+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) – SIGAFAT – Campos no item do
  pedido de vendas sendo alterados ao modificar certos campos no cabeçalho do pedido
  de vendas.
type: support-article
updated_at: '2026-06-22T21:04:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7250697863191-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFAT-Campos-no-item-do-pedido-de-vendas-sendo-alterados-ao-modificar-certos-campos-no-cabe%C3%A7alho-do-pedido-de-vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

Campos no item do pedido de vendas sendo alterados ao modificar certos campos no cabeçalho do pedido de vendas.

**Causa**

Conforme eu coloco informações em certos campos do cabeçalho dos pedidos de venda alguns itens no cabeçalho dos pedidos de venda são alterados.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da versão 12.  
  
**Solução**

Há alguns tipos de gatilhos no pedidos de venda, seja por funções nativas ou gatilhos, a alteração de campos no cabeçalho do pedido de venda **(SC5)** que contém a função **A410Recalc()** pode mudar algumas informações em campos no item do pedido de venda **(SC6)**.

Alguns campos do cabeçalho do pedido de vendas possuem para evitar inconsistências, uma função nativa chamada **A410Recalc()**. Essa função é responsável ao colocar informações no campo, atualizar novamente as informações dos campos antes colocados nos itens.

Caso seja colocado itens depois de incluir no cabeçalho, um item com a função **A410Recalc()**, a informação não será retirada novamente, isso ocorre quando é preenchido informações nos itens e depois é alterado ou incluído alguma informação em campos do cabeçalho do pedidos de venda.

**Para checar se o campo em questão possui a função de atualização nos itens basta:**

1. Selecionar o campo
2. Apertar F1
3. Ir no botão “Validação”
4. Ver se possui a função A410Recalc()

**Exemplo de verificação:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7250527572503/mceclip0.png)   ----->   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7250515428247/mceclip1.png)

**Exemplo para visualização:**

Incluir um pedido de venda e preencher mais nada além do **TES** na **SC6**, ela gatilhará o **CFOP** no campo **C6\_CF**.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7250551340439/mceclip2.png)

Vamos mudar manualmente agora o **CFOP** no campo **C6\_CF** para um diferente do que veio gatilhado ao incluir apenas a **TES**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7250530902551/mceclip3.png)

Agora, para visualizar a ação da função **A410Recalc()**, vamos preencher um campo que tem a função, como por exemplo o **C5\_CONDPAG** (Condição de Pagamento). Ao incluir uma informação no campo **C5\_CONDPAG**, será ativado a função **A410Recalc()** e será reafirmado os campos obrigatórios do item, ou seja, será reafirmado o campo **C6\_TES** fazendo que seja gatilhado o **CFOP** original no **C6\_CF** (retirando o valor que colocamos manualmente).

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7250585843223/mceclip4.png)

Ela reafirma os itens obrigatórios do item (**SC6**), então na verdade, não está mudando o **CFOP**, está reafirmando a **TES** que por sua vez muda o **CFOP**.

**Campos que tem a função A410Recalc():**

* C5\_CLIENTE (Cliente \*)
* C5\_LOJACLI (Loja \*)
* C5\_CLIENT (Cli.Entrega)
* C5\_CONDPAG (Cond. Pagto \*)
* C5\_TABELA (Tabela)
* C5\_DESC1/2/3/4 (Desconto 1/2/3/4)
* C5\_MOEDA (Moeda)

**Observações:**

* Há campos com funções que podem mudar informações dos itens por validarem pontualmente certos campos, não necessariamente recalculam todos os itens obrigatório dos Itens **(SC6)** como o **A410Recalc()**.
* Também há campos que não possuem funções, mas mudam outros campos por estarem incluídos em gatilhos nativos.
