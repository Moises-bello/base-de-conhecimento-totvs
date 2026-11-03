---
content_hash: 2fa432e77d0a33d453b37c31b16329585fad90a40c93c22b0ab6543bb57cba36
fetched_at: '2026-06-29T00:05:47.355224+00:00'
page_id: '1010818273'
product: rm
source: tdn-rm
title: Cálculo da Folha - Cálculo conforme competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1010818273
version: 6
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Conforme [DT - Crédito Trabalhador - Novos campos na tabela de Importação do Crédito](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1010257226) foi implementado um campo específico para registrar a competência do arquivo de importação. A partir dessa alteração, o cálculo da folha de pagamento considera este novo campo para determinar a aplicação do desconto referente ao empréstimo na modalidade crédito do trabalhador.

O desconto somente deverá ser aplicado caso o campo de competência esteja preenchido e corresponda exatamente à competência da folha de pagamento em processamento.

Na rescisão também foi feito o tratamento e o desconto deve ser efetuado de acordo com a competência informada no novo campo.

Observação:

Exceção para férias, a provisão deve ser realizada quando o novo campo corresponder ao mês das férias ou ao mês anterior.

Para ver em quais patches foi liberada a alteração consulte [DT - Crédito do Trabalhador - Cálculo conforme competência](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1010812982)

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios:

Validação dos campos da tabela de empréstimos:

* + **PFEMPRT.MESCOMPATUAL**
  + **PFEMPRT.ANOCOMPATUAL**

O campo será preenchido na base de dados e apresentado na tela do anexo Empréstimo do cadastro de funcionários

Neste mesmo funcionário tem outro empréstimo que deixarei com o campo Nulo na base de dados:

IMPORTANTE:

**01 -** Ao executar o script para a criação do campo deve-se importar o arquivo para o correto preenchimento dessa competência.

Se este campo estiver nulo na base de dados e apresentando valor zerado na visão do cadastro de empréstimo, este valor do empréstimo não será lançado.

**Exemplo:**

No mês de Outubro de 2025 o funcionário quitou o empréstimo.

No inicio do mês de Novembro de 2025 foi executado o atualizador na base de dados criando os campos com valor NULL

* + **PFEMPRT.MESCOMPATUAL**
  + **PFEMPRT.ANOCOMPATUAL**

Ao importar o arquivo disponibilizado no Emprega Brasil e o nome desse funcionário não estará no arquivo de Novembro de 2025, então o campo continuará nulo para este funcionário.

Quando executado o lançamento do desconto do empréstimo, então este funcionário não terá o desconto em folha porque não estava presente no arquivo e com isso este campo não foi atualizado.

Atenção:

**Caso importar o arquivo do Emprega Brasil antes de atualizar a base de dados no mês que deve ter o desconto do empréstimo consignado deve-se importar novamente o arquivo para preenchimento correto destes campos mês e ano da competência atual, sob risco de não ser descontado nenhum dos empréstimos por estarem com o campo Nulo.**

**02 -** Estes campos de mês/ano competência do credito do trabalhador foram tratados no lançamento do desconto pelo Grupo de Eventos e na Rescisão, e também no provisionamento no Adiantamento e no cálculo do recibo de Férias. Se o evento de desconto for lançado diretamente no envelope de pagamento do funcionário será feito o cálculo sem considerar os campos de mês/ano competência do credito do trabalhador, ficando o controle por conta do usuário.

Estando a base de dados também no mês 03/2025

Lançando o empréstimo pelo grupo de eventos:

No envelope foi lançado apenas o empréstimo considerando os campos de mês/ano competência do credito do trabalhador igual a competência atual da base de dados

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
