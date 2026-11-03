---
article_id: 360057292614
category: SIGAEST - CUSTOS
content_hash: 1c581c985e1807ee470d32100692e5bd7bc268198bd73b4851e7e5c378fb236b
fetched_at: '2026-06-28T22:39:00.284505+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Acerto de Custo dos
  Produtos em Estoque
type: support-article
updated_at: '2025-10-08T12:11:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Acerto-de-Custo-dos-Produtos-em-Estoque
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29303055841303)** Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Como ajustar o custo dos Produtos em Estoque?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Neste artigo abordaremos como acertar o custo de um produto em nosso Estoque.

Normalmente ele é feito quando o **custo médio atual** do produto não está no valor financeiro correto no entendimento da empresa, **o acerto de custo deve ser efetivado somente se você ja tiver processado o custo médio e refaz saldos** para o periodo atual.

**Caso você valide em Kardex, a existencia de uma nota de entrada, você deve usar como base, a QUANTIDADE e VALOR após essa nota**, pois o movimento valorizado fica APÓS a Nota de entrada (Em conformidade com o processamento de custo médio com o pergunte ANTES ou DEPOIS para os movimentos INTERNOS), **se acaso não houver nota de entrada, tenha como base o "SALDO ATUAL ou INICIAL, dependendo de onde voce quer o acerto ANTES ou DEPOIS".**

**E se o meu saldo inicial for ZERO, e as movimentações inciais forem internas sem CUSTO apenas com SALDO FISICO, como fica meu acerto valorizado para calculo inicial desses movimentos?**

Voce precisara nesse caso, efetuar um acerto de custo com QUANTIDADE, e considerar o calculo valorizado como ANTES, porque as movimentações SD2 e SD3 são com base no B2\_CM1, se voce incluir um movimento de apenas VALOR, ele não tera referencia para formar o médio, logo (valor / zero = zero B2\_CM1), portanto precisa de saldo para formar o médio (valor / saldo = B2\_CM1), essa é uma questão matematica.

**ANTES DO ACERTO:**

**![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32940617853463)**

**DEPOIS DO ACERTO:**

![Screenshot_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32940643213975)

***(Importante: Acerto de custo não deve ser realizado no armazem segregado de qualidade, armazem configurado como armazem CQ, porque não havera como liberar CUSTO sem saldo, portanto não realizar acerto de custo no armazem de qualidade.)***

**Simulando um acerto de custo:**

Vamos usar como base o produto de codigo **PROD001**, se baseando no relatorio Kardex Fisico Financeiro ([ESTSV023](https://tdn.totvs.com/x/VyueLQ)) onde o produto possui um saldo inicial de **1.500 | Custo médio: 25,5000 e | Valor 38.250,00.**

Essas movimentações apresentadas, ja foram processadas pelo recalculo de custo médio e refaz saldos, e a empresa informa que as movimentações "Internas" **precisam ser ajustadas para um custo médio de R$ 35,00 reias**.

Perceba que existe 3 movimentações, **onde a primeira de se trata de uma nota de entrada**, as demais se tratam de duas movimentações internas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29303055843607)

**Realizando o calculo para o ajuste de custo:**

Sabendo que a movimentação valorizada de acerto de custo, é ordenada entre as movimentações internas, e classificada seu posicionamento de acordo processamento do recalculo de custo médio, sob o pergunte "[Mov interno valorizado = Antes ou Depois](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)", **o seu objetivo é que as movimentações apresentadas tenham o custo médio de 35,00 ao inves do atual de 25,3960**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29303047351447)

Primeiro precisamos descobrir o total com o meu novo médio desejado, para isso você deve multiplicar o seu médio desejado (35,00) multiplicado com o saldo fisico "**após a ultima nota de entrada**", que é de **1.515,00**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29303055845527)

Então teremos **35,00 \* 1.515,00 = 53.025 (esse é o total descoberto).**

Agora precisamos creditar o total descoberto - o total disponivel após a ultima nota de entrada, que é de **38.475,00**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29303055846423)**

Então teremos **53.025 - 38.475,00 = 14.550** (valor positivo).

Dessa forma conseguimos saber que o movimento valorizado que precisa ser realizado, é uma entrada DE6 com o valor de **14.550**, para que nossas movimentações após esse movimento valorizado calculado com o pergunte "**Mov valorizado = Antes**", custeie os demais movimentos com o nosso novo médio desejado de **35,00.**

**Como cadastrar a TM(Tipo de movimento) para ser valorizado?**

Vamos usar como base o **TM 300**, basta você considerar o campo "**Valorizado = Sim**" e "**Qtd Zero = Sim**", pois dessa forma, voce consegue efetuar a movimentação apenas com a digitação de valor, sem quantidade. A mesma configuração se aplica para vocês considerar uma Requisição Valorizada.

**SIGAEST > ATUALIZAÇÕES > CADASTROS > MOVIMENTAÇÕES > INTERNAS (MATA230)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29303055847447)

Cadastrado a TM valorizada, basta realizar a movimentação para o produto, via rotina **"Movimentação Multipla - MATA241"**.

**SIGAEST > ATUALIZAÇÕES > MOVIMENTAÇÕES > INTERNAS > MOVIMENTAÇÃO MULTIPLA (MATA241)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29303047355927)

Realizado a movimentação valorizada, e processado o custo médio, esse é o cenario esperado na validação de suas movimentações no kardex:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29303055850903)

**Mas na validação do saldo atual o custo médio ainda não esta ajustado, oque fazer?**

Caso seu custo médio(B2\_CM1) não esteja atualizado com 35,00 basta processar o refaz saldos para o produto, pois o refaz saldos é o responsavel pela atualização do B2\_CM1, enquanto o custo médio é responsavel pela atualização do custo médio final(B2\_CMFIM1).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29303047358743)

Ao final desse artigo, esta sendo disponbilizado uma planilha, que pode ajudar você na hora de efetuar o calculo do custo médio desejado. Basta efetuar o preenchimento dos campos em amarelo, que a planilha ira montar para voce na coluna G12 o valor necessario para o ajuste, e na coluna H12 qual é o tipo de movimento que deve ser realizado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29303047359511)

**Saiba mais:**

*[MP - SIGAEST - MATR900 - Interpretando o Custo no Kardex antes e depois do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005781102)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
