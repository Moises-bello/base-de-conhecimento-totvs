---
article_id: 9129246051479
category: SIGAEST - LEGAIS
content_hash: 97e64865014b2e57825ecc253e71ad629dea01518c166347c9dad02370d071a5
fetched_at: '2026-06-28T22:38:51.670954+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI - Como interpretar
  o cálculo do Valor Importado (A8_VLRVI) em Produções?
type: support-article
updated_at: '2025-02-17T13:28:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9129246051479-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-FCI-Como-interpretar-o-c%C3%A1lculo-do-Valor-Importado-A8-VLRVI-em-Produ%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:06:35 min** **Dúvida**Como interpretar o cálculo do Valor Importado(A8\_VLRVI) em Produções?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Nesta documentação abordaremos a explicação de como é composto o campo A8\_VLRVI a partir do ponto de vista das Produções.

Recomendamos que, para ler esta documentação, o leitor tenha ciência de como é montado o Valor Importado com base nas Compras. Caso tenha dúvida em como ele é composto em Importações

(Compras), por gentileza verifique a Documentação abaixo:

|  |
| --- |
| [**Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI - Como interpretar o cálculo do Valor Importado (A8\_VLRVI) em Importações?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9121923559959) |

**Definição dos Produtos da Exemplificação**

Para exemplificar a maneira de se analisar, vamos usar os seguintes produtos:

**◼ MPIMPORTADO01**

**◼ MPIMPORTADO02**

**◼ MPNACIONAL01**

**◼ PI01**

**◼ PI02**

**◼ PA01**

**Observação**: **MP****= Matéria Prima, PI = Produto Intermediário e PA = Produto Acabado**

Eles ficarão depostos na seguinte estrutura:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9127276596247/mceclip0.png)

Os produtos destacados em vermelho passarão por Importação, sendo que ambos terão origem 1. Esta documentação é uma continuação. Todos os produtos têm relação 1:1, ou seja, para Produzir 10 itens do produto pai, são consumidos 10 itens do produto filho.

**Efetivando a Importação Direta**

Vamos entrar com a Nota via MATA103 (***Módulo 02 - Compras -> Atualizações -> Movimentos -> Documento de Entrada***). Note que os produtos terão a mesma quantidade, porém valores diferentes. O Frete será de R$ 300,00 que será rateado proporcionalmente para cada item da NF.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9127654169879/mceclip5.png)

**Aplicando o Cálculo do Valor Importado (A8\_VLRVI) do MPIMPORTADO01 e MPIMPORTADO02**

Vamos aplicar de forma resumida a fórmula.

**VI = VL \* FST**.

**A8\_VLRVI = Soma das VI's  / Soma das Quantidades do item nas NFs de Importação dentro do período.**

**MPIMPORTADO01:**

VI = VL \* FST

VI = 3591,3 \* 1

VI = 3591,3

A8\_VLRVI = VI / Quantidade

Taxa Unitária = 3591,3 / 100

Taxa Unitária  =  35,91

**MPIMPORTADO02:**

VI = VL \* FST

VI = 8208,7 \* 1

VI = 8208,7

A8\_VLRVI = VI / Quantidade

A8\_VLRVI = 8208,7 / 100

A8\_VLRVI  =  82,09

**Ordem de Produção e Apontamento do 3° Nivel da Estrutura (PI02 : MPIMPORTADO02)**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128535927447/mceclip0.png)

Vamos criar a Ordem de Produção (MATA650) via ***Módulo 04 - Estoque/Custos -> Atualizações -> Movimentações -> Internas -> Produção -> Ordens de Produção***.

Será uma OP de **quantidade 70.** Lembrando novamente que a relação entre o PI02 e MPIMPORTADO02 é 1:1.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128584130967/mceclip1.png)

Agora vamos Apontar a Produção (MATA250) via ***Módulo 04 - Estoque/Custos -> Atualizações -> Movimentações -> Internas -> Produção -> Apontar Produção***.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128611088791/mceclip2.png)

**Apuração do Valor Importado do PI02**

Através do relatório FCIR003 é possível analisar. Mas um detalhe importante é que **ele só trará os valores no produto produzido (PI02) após o processamento da rotina FISA061**.

Para acessar o relatório, entre no ***Módulo 04 - Estoque/Custos -> Relatórios -> Genéricos -> Relação FCI An. Prod***

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128689577879/mceclip4.png)

Em linhas gerais, o que ocorre:

▻ O PI02 teve uma produção de 70 itens;

▻ Ele se apropria da taxa do produto filho (MPIMPORTADO02) que é de 82,09;

▻ 70 (qtde) \* 82,09 (taxa) = 5.746,30 (Valor Total Importado)

▻ Se lermos de forma a saber a taxa unitária importada, ficaria: 5.746,30 / 70 = 82,09

**Ordem de Produção e Apontamento do 2° Nivel da Estrutura (PI01 : PI02 e MPIMPORTADO01)**

**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128918997143/mceclip8.png)**

Vamos criar a Ordem de Produção (MATA650) via ***Módulo 04 - Estoque/Custos -> Atualizações -> Movimentações -> Internas -> Produção -> Ordens de Produção***.

Será uma OP de **quantidade 50.** Lembrando novamente que a relação entre o PI01 com o PI02 e MPIMPORTADO01 é de 1:1.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128814106007/mceclip5.png)

Agora vamos Apontar a Produção (MATA250) via ***Módulo 04 - Estoque/Custos -> Atualizações -> Movimentações -> Internas -> Produção -> Apontar Produção***.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128817879703/mceclip6.png)

**Apuração do Valor Importado do PI01**

Através do relatório FCIR003 é possível analisar. Mas um detalhe importante é que **ele só trará os valores no produto produzido (PI01) após o processamento da rotina FISA061**.

Para acessar o relatório, entre no ***Módulo 04 - Estoque/Custos -> Relatórios -> Genéricos -> Relação FCI An. Prod***

***![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128864119703/mceclip7.png)***

Em linhas gerais, o que ocorre:

▻ O PI01 teve uma produção de 50 itens;

▻ Ele se apropria da taxa dos produtos filhos (MPIMPORTADO01 e PI02 ) que é, respectivamente, 35,91 e 82,09;

▻ Uma maneira resumida de pra vermos o Valor Unitário Importado do PI01 é: 35,91 + 82,09 = 118,00

▻ Com isso, 50 \* 118,00 = 5.900,00 (Valor Total Importado).

**Ordem de Produção e Apontamento do 1° Nivel da Estrutura (PA01 :  PI01 e MPNACIONAL01)**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128962928023/mceclip9.png)

Não temos saldo físico do produto **MPNACIONAL01**. Vamos entrar com uma Nota via MATA103 (***Módulo 02 - Compras -> Atualizações -> Movimentos -> Documento de Entrada***)

A entrada será de quantidade 20 (que será a quantidade da Ordem de Produção do PA01)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128965441815/mceclip10.png)

Vamos criar a Ordem de Produção (MATA650) via ***Módulo 04 - Estoque/Custos -> Atualizações -> Movimentações -> Internas -> Produção -> Ordens de Produção***.

Será uma OP de **quantidade 20.** Lembrando novamente que a relação entre o PI01 com o PI02 e MPIMPORTADO01 é de 1:1.

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9129062072855/mceclip11.png)

Agora vamos Apontar a Produção (MATA250) via ***Módulo 04 - Estoque/Custos -> Atualizações -> Movimentações -> Internas -> Produção -> Apontar Produção***.

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9129090444311/mceclip12.png)

**Apuração do Valor Importado do PA01**

Através do relatório FCIR003 é possível analisar. Mas um detalhe importante é que **ele só trará os valores no produto produzido (PA01) após o processamento da rotina FISA061**.

Para acessar o relatório, entre no ***Módulo 04 - Estoque/Custos -> Relatórios -> Genéricos -> Relação FCI An. Prod***

***![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9129215557527/mceclip13.png)***

Em linhas gerais, o que ocorre:

▻ O PA01 teve uma produção de 20 itens;

▻ Ele se apropria da taxa do único produto filho que tem resquício de taxa importada (PI01) que é de 118,00;

▻ O MPNACIONAL01 não é um produto importado, logo os valores de taxa unitária e total são zerados;

▻ Com isso, 20 \* 118,00 = 2.360,00

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI - Como interpretar o cálculo do Valor Importado (A8\_VLRVI) em Importações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9121923559959)*

[*Clique aqui e veja mais artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
