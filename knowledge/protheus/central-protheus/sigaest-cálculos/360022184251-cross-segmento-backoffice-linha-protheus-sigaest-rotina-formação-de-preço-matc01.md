---
article_id: 360022184251
category: SIGAEST - CÁLCULOS
content_hash: c17cf102a0d60d0806796624d647a86c6d8b8801cfcbe05c024c8f1fb172fd0d
fetched_at: '2026-06-28T22:39:04.031640+00:00'
product: protheus
section_id: 1500001550082
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Rotina Formação de
  Preço (MATC010)
type: support-article
updated_at: '2025-10-17T20:45:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022184251-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-Forma%C3%A7%C3%A3o-de-Pre%C3%A7o-MATC010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503129748247) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**

Como funciona e qual a finalidade da Formação de Preço (MATC010)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

A rotina de Formação de Preços (MATC010) tem como objetivo auxiliar o usuário a formar preços dos produtos com base em critérios em que ele pode escolher, a depender da sua regra de negócio. Formando preços com base nestes critérios, a empresa consegue avaliar o preço mais assertivo para obter o lucro esperado nos produtos.

Abaixo explicaremos de maneira prática uma Formação de Preço simples, de ponta à ponta.

Utilizaremos três produtos: um **PA100**, um **MP100** e uma **MOD000004** (MOD + Centro de Custo).

**1° Passo - Entrada do MP100**

Vamos dar entrada (MATA103) do produto **MP100** com a **quantidade 1** e **valor unitário R$ 50,00**. Nesta entrada, deve-se utilizar TES com o campo **F4\_UPRC = Sim**.

**2° Passo - Estruturar o PA100 com MP100 e MOD000004**

Criaremos uma estrutura (MATA200) para o produto **PA100** contendo os produtos **MP100** com **quantidade 1** e **MOD000004** com **quantidade 1**.

**3° Passo - Formação do Custo Standard do PA100, MP100 e criação manual do Cust. Standard da MOD000004**

Agora formaremos o campo Custo Standard (B1\_CUSTD) dos produtos **PA100** e **MP100**, para isto iremos executar a rotina MATA320, maiores detalhes do funcionamento desta rotina no link abaixo.

[MP - SIGAEST - Conceito de utilização da rotina MATA320 - Custo Standard - B1\_CUSTD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013572791-MP-SIGAEST-Conceito-de-utiliza%C3%A7%C3%A3o-da-rotina-MATA320-Custo-Standard-B1-CUSTD?source=search)

O produto **MOD000004** não possui integração contábil, a sua valorização é baseada no campo B2\_CM1. Então podemos preencher manualmente o campo **B1\_CUSTD** (Custo Standard no Cadastro de Produtos) baseado no campo B2\_CM1. Como exemplo, colocaremos o Custo Standard da **MOD000004** no valor de **R$ 10,00**.

OBS ANTES DO 4° PASSO:

A rotina de formação de preços (MATC010) é customizável e o cliente pode definir o que melhor atende a sua regra de negócio. Então utilizaremos um exemplo simples.

**4° Passo - Formação do Preço do PA100**

Podemos formar o preço baseado no **Custo Standard (B1\_CUSTD)**, **Custo Médio (B2\_CM1)**, **Planilha ou em outras moedas.**

Ao abrir a rotina MATC010, selecionaremos o produto PA100 e clicaremos em "Formar Preço"

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000299721)

**5° Passo -  Seleção do Custo da Formação de Preços**

Utilizaremos o Custo Standard conforme imagem abaixo, basta clicar no botão “CUSTO” e selecionar o custo "STANDARD".

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099166914)

Do lado direito temos os principais botões para utilizarmos na manutenção da planilha, podemos incluir linhas, deletar alterar e em seguida podemos salvar as alterações digitando o nome da planilha que será salva.

OBS: Nas versões mais atuais da rotina formação de preços (MATC010) a planilha “STANDARD.PDV” foi descontinuada sendo migrada para a tabela SCO, maiores detalhes no link abaixo.

[MP - SIGAEST - Formação de preço MATC010 - HELP: Tabela SCO deveria conter dados autocontidos.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013975591-MP-SIGAEST-Forma%C3%A7%C3%A3o-de-pre%C3%A7o-MATC010-HELP-Tabela-SCO-deveria-conter-dados-autocontidos-?source=search)

**6° Passo - Formação do Preço do PA100 baseado no Custo Standard da estrutura.**

Na parte superior temos o PA100 e seus componentes, contendo o Nível da Estrutura (SG1), Quantidade e o Valor Total baseados no campo B1\_CUSTD e a Porcentagem do produto na estrutura do PA100.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000301181)

**7° Passo - Utilizando uma das fórmulas pré-definidas da Formação de Preços**

Já existem fórmulas pré-definidas e no nosso caso para apurar o preço de venda, de forma simplificada, utilizaremos o total de matéria prima somado ao custo da MOD multiplicado por dois, veja a imagem abaixo com estas definições, agora temos o preço de venda do nosso produto, veja imagem abaixo.

![TOTAL.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360019163512)

**8° Passo - Atualizando o Preço de Venda do PA100 para R$ 120,00**

Podemos executar a rotina cadastro de produtos (MATA010), selecionar o produto PA100 e clicar em alterar e inserir no campo B1\_PRV1 o valor do preço de venda apurado anteriormente, no nosso exemplo R$ 120,00.

![PRVENDA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360019027031)

**9° Passo - Fazendo uma venda com o novo preço do produto PA100**

Ao digitarmos um Pedido de Venda (MATA410) e digitarmos o produto PA100 e a quantidade, o campo C6\_PRCVEN é preenchido automaticamente, vaja a imagem abaixo:

![MATA410.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360019163492)

Obs: não se pode utilizar produto com tipo "SE" na formação de preço, o tipo SE é reservado, então caso tenha o tipo cadastrado, devera ser reavaliado, por padrão esse tipo não consta nos cadastros de tipos atuais.

![](https://atendimento.totvs.com/attachments/token/qCUuo0ZCPUSWZ2hbb1YQOHgT5/?name=image001.png)

Nas releases mais atuais podemos definir se será utilizada a planilha STANDARD.PDV ou a tabela SCO conforme documentação abaixo.

<https://tdn.totvs.com/pages/releaseview.action?pageId=458770275>

**Saiba mais:**

*[Clique aqui e saiba mais sobre outros Cálculos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199493-SIGAEST-C%C3%81LCULOS)*
