---
article_id: 35487156124567
category: Materiais - Compras (SIGACOM)
content_hash: 152e81e11cc3f63524fd65d790475628295d507d82dde6cc805a044719fa82ac
fetched_at: '2026-06-28T22:41:17.370545+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de entrada
  - tipos de nota e como utilizar
type: support-article
updated_at: '2025-10-08T16:40:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35487156124567-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-entrada-tipos-de-nota-e-como-utilizar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35487156107671) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Dúvida**  
**Quais são os tipos de notas de entrada e em que processo utilizar cada um deles ?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Todas as versões  
  
**Solução**  
Dentro do documento de entrada, temos os tipos de nota :

**Normal**

**Devolução**

**Beneficiamento**

**Compl. ICMS**

**Compl. IPI**

**Complemento que pode ser ( opções do campo Tipo de complemento ) :**

**1- Preço**

**2- Quantidade**

**3- Frete**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35487211395095)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35487211395479)

**Os tipos Compl.ICMS e Compl. IP**I são referentes aos complementos dos impostos, referentes a notas de entrada. E esses tipos são atendidos pela equipe de suporte do fiscal, que atua nos impostos no documento de entrada. Quaisquer dúvida sobre eles, podem ser sanadas mediante abertura de ticket para a equipe de suporte do fiscal.

**TIPO NORMAL :**

***Esse tipo de nota é utilizado em entradas nos processos de compras e que envolvem fornecedores.***

***É utilizado também, em processos de retorno, utilizando ou não poder de terceiros no TES, porém onde a remessa  ( Pedido de Vendas), foi efetuada utilizando um fornecedor também.***

Exemplo : Pedido de vendas utilizado para efetuar a nota de remessa/saída.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35492723600023)

Na entrada/retorno :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35492723604247)

**Nesse cenário, pode ou não haver o controle de poder de terceiros nos TES utilizados**, na saída e na entrada. Lembrando que, se na saída foi utilizado um TES com controle de poder de terceiros como remessa, o da entrada, precisa estar configurado com Devolução.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35492723604887)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35492732471959)

**TIPO DEVOLUÇÃO :**

***Este tipo de nota é utilizado somente em processos de entrada de nota, referente a devolução de operações de saída referentes a vendas, sem o controle de poder de terceiros configurados nos TES.***

***É um tipo de nota onde, quando preenchido o sistema já altera o campo de fornecedor para cliente, no cabeçalho da nota de entrada.***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35492723608215)

**TIPO BENEFICIAMENTO :**

Este tipo de nota de entrada, também é utilizado para entradas envolvendo clientes.

E podemos ter dois cenários :

***1-) Quando a sua empresa é um industrializador e por exemplo, recebe um produto para beneficiar de um cliente seu. Nesse cenário o TES utilizado na entrada, pode ou não conter o controle de poder de terceiros configurado.***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35492732473751)

***2-) Quando foi feita uma remessa para um cliente, seja consignação, demonstração, etc. E no Pedido de vendas, foi utilizado um cliente. E no TES da saída está configurado o controle de poder de terceiros como Remessa.***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35492723610775)

***No retorno dessa remessa deve-se utilizar o tipo da nota de entrada como B. E o Tes de retorno configurado com o campo de controle de poder de terceiros como Devolução.***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35492723612439)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35492723604887)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35492732471959)

**TIPO COMPLEMENTO :**

**Os tipos de nota de complemento são sempre gerados, considerando notas de entrada como origem, e, utilizando fornecedores.**

**Importante : Notas do tipo Complemento, não são passíveis de terem pedido de compras vinculado, pois é necessário vincular a nota de origem ( entrada ).**

**1-Preço :**

**Com essa opção é possível complementar o preço de uma nota de origem/compra utilizando um fornecedor e vinculando com a nota de origem.**

**Por exemplo:**

Foi feita uma compra, pelo valor unitário de 500,00, porém no momento de se faturar, o seu fornecedor emitiu a nota de por 450,00. Depois ele percebeu o erro, e emitiu uma nota de complemento de preços com a diferença. Essa nota da diferença, deve ser incluída com o tipo Complemento, o tipo do complemento preço e, após o preenchimento das informações no cabeçalho e no item da nota, deve-se vincular através da opção Origem em outras ações, a nota de compra, a origem, que foi incluída com o valor a menor.

Com esse procedimento, o custo do produto será alterado, considerando a nota de origem ( a compra efetiva ) e a nota de complemento de preços.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35493309766935)

Baseado no produto e no fornecedor na opção Origem serão apresentadas as notas de compra/origem. Basta posicionar em cima da nota a ser complementada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35493309767447)

**2-Quantidade :**

**Com essa opção é possível complementar as quantidades de uma nota de origem/compra utilizando um fornecedor e vinculando com a nota de origem.**

O processo é semelhante ao do item 1, complemento de preços, só que considerando a quantidade. Considerando o mesmo cenário do item 1.

**3-Frete :**

**O tipo de complemento de frete normalmente é utilizado para as entradas dos CTE´s ( conhecimentos de frete ).**

Onde há a possibilidade de se utilizar a MATA103 ( documento de entrada ) ou a MATA116 ( Nf Conhec Frete ).

A diferença em como utilizar uma ou outra rotina, está no fornecedor do CTE. 

Se ele é o mesmo para as duas notas, compra e CTE, pode-se usar a rotina do documento de entrada. Se são fornecedores diferentes, ou seja, a compra foi com um fornecedor e o CTE com outro, aí deve-ser utilizar a rotina Nf Conhec de Frete.

[Entrada de CTE qual rotina utilizar ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22672045330327-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Inclus%C3%A3o-de-CTE-qual-rotina-utilizar)

**Importante: As rotinas do compras só vinculam CTE´s com notas de origem, entrada.**

**Não vinculamos CTE´s quando a origem é uma nota de saída. Para este cenário temos no módulo do Gestão de Frete Embarcador( GFE ) rotinas que propiciam esse vínculo. Quaisquer dúvidas, acionar a equipe do GFE mediante ticket**.

**Sáiba Mais :**

[**Para ter o controle correto do saldo de poder de terceiros**](https://tdn.totvs.com/pages/releaseview.action?pageId=285642640)

[**Incluir nota de complemento de preços**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028648592-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-incluir-uma-nota-de-entrada-tipo-complemento-de-pre%C3%A7o)

[**Como incluir uma nota de devolução de vendas**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010638982-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-uma-Devolu%C3%A7%C3%A3o-de-Vendas-na-rotina-de-Documento-de-Entrada)
