---
article_id: 12658027235223
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 8c3038fc34e44ebd216ef35fe35118ec6ebe8b69afde7c377daf16f203f2d1ca
fetched_at: '2026-06-28T22:38:42.748203+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help: A410VTDNO
  no faturamento'
type: support-article
updated_at: '2023-06-21T18:57:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12658027235223-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-A410VTDNO-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15482117182359) Tempo aproximado para leitura: **00:04:30 min****Ocorrência**Ao devolver uma compra aparece o Help: A410VTDNO, como retornar o item pelo pedido de venda?  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões  
  
**Causas**

1 - As devoluções parciais do pedido de venda tiveram ITENS com preços maiores que o preço do item no documento de entrada.

2 - O Help ocorre quando a multiplicação que incide no C6\_VALOR (C6\_QTDVEN \* C6\_PRCVEN) dá um valor maior ou menor do que o exato valor total do documento de entrada restante a devolver.

**OBS:** O Help só ocorre quando já foi anteriormente devolvido parte do saldo da entrada, porém na nova tentativa de devolução, está no campo C6\_QTDVEN para ser retornado, toda a quantidade que falta devolver (D1\_QUANT - D1\_QTDEDEV).

O sistema verifica o total da entrada (D1\_TOTAL) do documento de entrada. Exemplo:

**Documento de entrada (MATA103):**

Quantidade: D1\_QUANT = 2

Preço unitário: D1\_VUNIT = 2

Resultado: D1\_TOTAL = 4

**Primeira devolução ao documento de entrada (MATA410):**

Quantidade: C6\_QTDVEN = 1 (Ao entrar na rotina estava "2", porém nessa devolução alteramos para um para devolver apenas um)

Preço de venda: C6\_PRCVEN = 2 (Encontrado pelo C6\_VALOR dividido pelo C6\_QTDVEN [2 / 1 = 1])

Preço de lista: C6\_PRUNIT = 2 (Vem do campo D1\_VUNIT)

Resultado: C6\_VALOR = 2 (Resultado do C6\_QTDVEN \* C6\_PRCVEN)

**Segunda devolução ao documento de entrada (MATA410):**

1 - Ao retornar pela funcionalidade Retornar, o sistema irá validar:

* Do total da entrada, falta devolver R$ 2 ao todo.
* Do total da entrada, falta devolver uma quantidade do item.

Logo, o sistema achará o preço de venda (C6\_PRCVEN), dividindo o total (C6\_VALOR) pela quantidade (C6\_QTDVEN): (2 / 1 = 1)

Ao retornar pela funcionalidade Retornar (segunda devolução):

Quantidade: C6\_QTDVEN = 1

Preço de venda: C6\_PRCVEN = 2

Preço de lista: C6\_PRUNIT = 2

Resultado: C6\_VALOR = 2

**Da maneira que a segunda devolução está acima, será possível devolver, pois atende:**

* 1 - A quantidade que resta devolver (1)
* 2 - O total em relação ao documento de entrada que resta devolver (R$2)

2 - Ao alterar o preço de venda (C6\_PRCVEN), para um valor que a multiplicação dele com a quantidade, seja menor ou maior que o valor exato do documento de entrada a devolver, o erro ocorre:

Exemplo 1: Ao retornar pela funcionalidade Retornar (segunda devolução):

Quantidade: C6\_QTDVEN = 1

**Preço de venda: C6\_PRCVEN = 3**

Preço de lista: C6\_PRUNIT = 2

Resultado: C6\_VALOR = 3

**Da maneira que a segunda devolução está acima, o erro "A410VTDNO" ocorre pois:**

* 1 - A quantidade que resta devolver (1) está correta
* 2 - O total em relação ao documento de entrada que resta devolver está incorreto, está (R$ 3) e não (R$ 2), um real a mais que o correto.

Exemplo 2: Ao retornar pela funcionalidade Retornar (segunda devolução):

Quantidade: C6\_QTDVEN = 1

**Preço de venda: C6\_PRCVEN = 1**

Preço de lista: C6\_PRUNIT = 2

Resultado: C6\_VALOR = 1

**Da maneira que a segunda devolução está acima, o erro "A410VTDNO" ocorre pois:**

* 1 - A quantidade que resta devolver (1) está correta
* 2 - O total em relação ao documento de entrada que resta devolver está incorreto, está (R$ 1) e não (R$ 2), um real a menos que o correto.

**Solução:**

1 - Inserir no C6\_PRCVEN uma quantidade que, ao ser feita a multiplicação (C6\_QTDVEN \* C6\_PRCVEN), o valor total (C6\_VALOR) seja exatamente o valor que falta retornar, para ficar igual ao documento de entrada.

2 - Identificar nos pedidos de venda devolvidos anteriormente (referenciando o documento de entrada), quais deles estão sendo devolvidos com o valor maior (C6\_VALOR) fazendo com que fique desregulado as próximas devoluções parciais, pois a quantidade a ser devolvida nem foi completa porém o valor total a ser devolvido sim.
