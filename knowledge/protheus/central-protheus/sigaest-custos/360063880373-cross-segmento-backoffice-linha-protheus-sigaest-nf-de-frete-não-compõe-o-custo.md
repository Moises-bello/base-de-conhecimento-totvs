---
article_id: 360063880373
category: SIGAEST - CUSTOS
content_hash: 9ce8b48e5f039f77d6886d5dc1044147e912710454df5425f439151ced514815
fetched_at: '2026-06-28T22:39:02.268857+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - NF de frete não compõe
  o custo do produto rejeitado no Armazém de CQ após devolver ao fornecedor
type: support-article
updated_at: '2023-07-03T17:53:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063880373-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-NF-de-frete-n%C3%A3o-comp%C3%B5e-o-custo-do-produto-rejeitado-no-Armaz%C3%A9m-de-CQ-ap%C3%B3s-devolver-ao-fornecedor
---

**Dúvida**Ao efetuar um Documento de Entrada de Qtde 1 e Custo de 10,00 com Conhecimento de Frete de 50,00, após o produto ser rejeitado pelo CQ (MV\_CQ) e devolvido ao fornecedor, o Saldo do Frete (50,00) fica preso no CQ, conforme mostrado no Kardex:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102454754)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102454774)

Como resolver esta questão?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Este cenário acima não se trata de um erro. Abaixo daremos uma sugestão de como tratar este problema.

**Recomendação para o Custo agregado à NF de Entrada não ficar preso no C.Q**

É recomendado que seja criado um local (armazém) de rejeição, que pode ser um local físico onde a qualidade retira da área de qualidade e move para o setor de rejeições e devoluções ou mesmo um local fictício em que a qualidade rejeita naquele local mas fisicamente fica na área da qualidade para ser devolvido.

No caso de produtos que foram para a qualidade e **não tiverem nenhum custo agregado**, como valor de frete, **a rejeição pode ser mantida no local de CQ e ser feita a devolução diretamente do local de CQ**, isto porque no pedido de devolução será feita a amarração com a nota de entrada e o custo será referente somente a nota de entrada.

No Caso de produtos **que tenham custos agregados**, como valor de frete, este custo não pode ser devolvido e deverá ser pago, então este custo precisa fazer parte do custo do estoque. Para tanto **deve ser rejeitado para um local diferente de CQ** assim todo o custo passa a fazer parte do custo de estoque, tanto o custo do produto como o custo de frete, e ao devolver o produto o custo será referente a nota de entrada na amarração do pedido de devolução, mantendo o custo do frete no estoque.

Em ambos os casos o mais interessante seria ter um armazém (local) de rejeição e a partir dele ser devolvido ou até mesmo requisitado para refugo.

**Saiba mais:**

*[MP - SIGAEST - Agregando o Custo ao Conhecimento de Frete](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053013934-MP-SIGAEST-Agregando-o-Custo-ao-Conhecimento-de-Frete-)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)*
