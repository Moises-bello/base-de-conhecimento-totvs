---
content_hash: beb43a93a195b1dad7ebf7219a560c3a39ee0627ec1322ba3303aabd11d46dff
fetched_at: '2026-06-29T00:10:52.215617+00:00'
page_id: '571002861'
product: rm
source: tdn-rm
title: CPRB Regime de Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=571002861
version: 16
---

As empresas no regime de Lucro Real já entregam a EFD Contribuições contendo a escrituração do PIS e COFINS nos Blocos A, C, D e F. Já as empresas do Lucro Presumido só passarão a informar a escrituração de PIS e COFINS a partir da competência julho/2012.

Entretanto, para os dois regimes, Real e Presumido, a obrigação para a escrituração da apuração da contribuição previdência sobre receita é a partir de março/2012.

As empresas do Lucro Real devem informar o Bloco P juntamente com os demais Blocos. As empresas do Lucro Presumido devem informar, até a competência junho/2012, apenas os dados dos Blocos 0, P e 9 e o restante dos blocos A, C, D, F, 1, M vazios.

**Obs.:** Os dados do Registro 2060 da REINF vem diretamente do período de apuração, este qual utilizava o código da conta contábil como chave graças ao obsoleto bloco P da EFD Contribuições.

Este não é o caso da REINF ocasionando erro de cálculo em casos onde houvessem exclusões e saídas com contas contábeis distintas.

Em consequência do defeito e a inutilização do bloco P, todos os períodos de apuração do CPRB com o ano maior ou igual a 2020 a Conta Contábil não será mais chave do Agrupamento.

Para identificarmos as empresas optantes pelo Lucro Presumido, será apresentado na tela de geração da rotina, campo para informação do Regime adotado pela empresa de Lucro Presumido:

* Não se aplica;
* Regime de Caixa;
* **Regime de Competência**.

Caso seja selecionada a opção “Não se aplica”, a geração seguirá o modelo padrão, já gerado atualmente, mais o Bloco P, de acordo com as regras constantes no Item 5 desta especificação.

Se for selecionada a opção Regime de Caixa ou **Regime de Competência** e o período selecionado por anterior a Julho/2012, serão gerados apenas os Blocos 0, P e 9.

falseApuração CPRB

**Para acessar o Período de Apuração da CPRB:**

Selecionar o módulo Gestão Fiscal | Obrigações Principais | Período de Apuração

Nota

Na apuração do tributo CPRB será considerado o código da atividade vinculado ao lançamento de Outros Débitos/Créditos CPRB;

Quando não informado o código de atividade econômica no lançamento de outros débitos e créditos na apuração o lançamento será considerado na apuração com comportamento anterior.

O Lançamento de Ajuste afetará a Base de Cálculo na apuração da atividade e consequentemente o Valor da Contribuição.

A implementação tem efeito em períodos CPRB a partir de 01/2020 no regime de competência.

2lefttrue1Exemplo de como realizar Apuração da CPRB

Ao incluir um lançamento em Outros Débitos/Créditos com o Código de Atividade Econômica preenchido, o ajuste considerado na apuração é agrupado por Código de Atividade Econômica.

Exemplo abaixo:

falseExemplo 131Passo 1

Foi criado um Lançamento Fiscal d Saída

Imagem2Passo 2

Neste Lançamento de Saída o Item possui o tributo CPRB

Imagem3Passo 3

Para que no Período de Apuração os itens sejam agrupados por Código de Atividade Econômica, o(s) produto(s) desejado(s) devem ter esta informação preenchida na aba Campos Complementares, conforme exemplo abaixo.

Imagem2Preenchimento do Código Atividade Econômica

A **partir da versão 12.1.33** o sistema passa a considerar o Código de Atividade Econômica preenchido em Dados Fiscais do Produto:

Imagem

Caso o código não esteja preenchido em dados Fiscais do Produto será verificado o campo complementar:

Imagem3Para criar o Campo Complementar no produto

Siga o passo-a-passo:

false3true1Passo 1

Acessar o Módulo Gestão de Estoque, Compras e Faturamento

**Ir na Aba Cadastros | Mais | Campos Complementares | Produtos**

Imagem2Passo 2

Clicar em Novo e seguir as seguintes parametrizações:

**Nome do campo:** CODATIVECONOMIC

**Tipo:** Alfanumérico.

**Tamanho:** 8 posições.

Imagem4Lançamento de Outros Débitos\Créditos 

O lançamento de Outros Débitos\Créditos deve ser preenchido com Id. da Atividade Econômica que foi cadastrado previamente, o campo Código de Ajuste deve ser informado conforme o campo **codAjuste** do registro R-2060 da REINF.

O Tipo deve ser  Débito ou Crédito com Subtipo: **Não se Aplica**

Lançamento de Outros **Débitos** Exemplo:

Imagem

Lançamento de Outros **Créditos** Exemplo:

Imagem5Tipo de Apuração CPRB

**Agora será necessário parametrizar o Tipo de Apuração CPRB, para isso, siga os passos**

false4true1Passo 1

Gestão Fiscal, Aba Cadastros, selecionar Filiais, Clicar em Anexos, selecionar Dados Fiscais:

Imagem2Passo 2

Vá até a Aba Tributos. No Tipo de Apuração o parâmetro Regime de Competência deve estar selecionado, caso não esteja marcado ou esteja selecionado como "Não se Aplica", será considerado o Regime de Competência.

Imagem3Passo 3

Finalmente ao realizar o processo de Encerramento de Período de Apuração da CPRB os itens serão agrupados pelo Código de Atividade Econômica.

Imagem

Abaixo Exemplos do Encerramento de uma Apuração CPRB com Receias Desoneradas:

ImagemImagem
