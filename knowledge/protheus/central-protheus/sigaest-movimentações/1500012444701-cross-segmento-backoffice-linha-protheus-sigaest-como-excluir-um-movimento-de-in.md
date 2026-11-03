---
article_id: 1500012444701
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 20592a11f149caccaa1603e90ac0d413da0fa0147d5720217c9ca6bd003130de
fetched_at: '2026-06-28T22:38:54.404179+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como excluir um movimento
  de Inventário feito indevidamente?
type: support-article
updated_at: '2021-05-27T12:02:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012444701-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-excluir-um-movimento-de-Invent%C3%A1rio-feito-indevidamente
---

**Dúvida**É possível estornar ou excluir um movimento de acerto de inventário feito indevidamente?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**São bem comuns os casos onde por erro de digitação ou outros motivos acabamos efetuando uma digitação e acerto de inventário de maneira incorreta durante o Processo de Inventário. Neste artigo mostraremos qual a maneira padrão do *Protheus* para poder estornar um movimento de acerto de inventário.

Cenário Prático:

Produto: PA105

Quantidade antes de inventariar: 48

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019508002/mceclip0.png)

Quantidade contada (erroneamente): 53

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019508282/mceclip3.png)

Após o acerto, o saldo passou a ser 53 (por erro de digitação):

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019777261/mceclip2.png)

**Estornando o Acerto**

Todo acerto de inventário, **quando há uma diferença entre o que digitou e o que tinha no estoque no momento da digitação**, o Protheus gera automaticamente movimentos do tipo DE0/RE0 na tabela de Movimentações Internas (SD3), com o valor da diferença, que no nosso caso foi 5 a mais (48 -> 53).

**Observação importante**: Só será possível fazer o estorno/exclusão do acerto caso a movimentação for de um período que **não** **foi** **efetuada** **a virada de saldos**.

Desta forma, basta acessarmos a rotina de Movimentos Internos Múltiplos (MATA241) para estornarmos o movimento. Caminho: **Modulo 04 - Estoque/Custos > Atualizações > Movimentações > Internas > Movimentação Múltipla.** Veja:

![ESTORNO_INV.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019777761/ESTORNO_INV.gif)

Com isso, nosso saldo volta para 48:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019777821/mceclip4.png)

Para deletar do ambiente os movimentos estornados, basta parametrizar, no Recálculo do Custo Médio, a pergunta "Apagar Estornos?" = "Sim":

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019508882/mceclip5.png)

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Processo padrão para Inventariar produtos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-MP-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
