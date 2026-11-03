---
content_hash: f813ac74fc0eea125501fa0e8811e1c43c1528b861a30852d101324db10e9c5b
fetched_at: '2026-06-29T00:11:26.648215+00:00'
page_id: '718971878'
product: rm
source: tdn-rm
title: Novo Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Novo+Contrato
version: 14
---

**Importante:**

Para que o TOTVS Biblioteca processe as taxas de multa, taxas de empréstimo e/ou taxas de cadastro do usuário através do contrato no **TOTVS Educacional** é necessário que o módulo esteja parametrizado para integrar com o **TOTVS Educacional** e **TOTVS Financeiro**.

## **CONTEÚDO**

Quando houver integração financeira e integração com o **TOTVS Educacional** os valores relacionados a taxas de cadastro de usuário (importação de alunos), taxas de multa e taxa de empréstimo não serão mais gerados diretamente no **TOTVS Gestão Financeira**, a partir de agora será criado um contrato no momento da importação do usuário ou devolução para o aluno vinculado ao usuário do**TOTVS Gestão Bibliotecária.**

Neste contrato serão geradas as parcelas correspondentes aos valores processados e a geração de lançamentos passará a seguir as regras do **TOTVS Educacional**,permitindo assim a visualização de boletos relacionados a taxas de multa, taxa de empréstimo e/ou taxas de cadastro no extrato financeiro do **Portal do Aluno**.

Caso não esteja integrado com o **TOTVS Educacional**, mas esteja integrado com o **TOTVS Financeiro** e o usuário não seja um aluno, ou já foi um aluno, mas não possui matrícula ativa, então deverá ser mantido o comportamento anterior, os valores serão processados diretamente no **TOTVS Financeiro**.

**Regras:**

O contrato será criado com as seguintes características:

* Não vai possuir matriz aplicada
* O tipo contrato será: TOTVS Gestão Bibliotecária
* Período letivo/nível de ensino correspondente a matrícula atual do aluno
* Este contrato não poderá ser alterado

**Observação:**

Para alunos que possuem mais de uma matrícula ativa, ao processar uma taxa de multa, será necessário o usuário do **TOTVS Gestão Bibliotecária** selecionar qual será o nível de ensino/período letivo que será considerado para processar a taxa. Quando essa tela não for apresentada é porque o aluno não possui mais de uma matrícula em período letivos/níveis de ensino distintos.

## Responsável financeiro

O TOTVS Gestão Bibliotecária utilizará o responsável do usuário cadastrado para gerar as parcelas e lançamentos, não será utilizado o responsável do aluno.

## Agrupamento de lançamentos

Por padrão o sistema irá gerar uma parcela para cada tipo de operação realizada na devolução, ou seja, se a devolução gerar taxa de multa e empréstimo, será gerado uma parcela para cada item, ou seja, uma parcela para taxa de empréstimo e outra para taxa de multa para cada publicação devolvida.

Caso seja utilizado agrupamento de lançamentos, o sistema irá agrupar todas as taxas de multa em uma parcela e todas as taxas de empréstimos, caso exista, em outra parcela.

## Importação de alunos

Ao importar um aluno através do processo de importação de usuários, caso o usuário possua mais de um nível de ensino/período letivo o aluno não será importado, será exibido um log no final do processo e o aluno poderá ser importado posteriormente através da tela de movimentações onde será possível selecionar nível de ensino/período letivo será utilizado para geração da taxa de cadastro.
