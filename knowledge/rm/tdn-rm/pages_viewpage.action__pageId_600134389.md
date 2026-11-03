---
content_hash: 9e68f0d6e09fd804bf67eed3029d687aac3f7a46148595920a639c90c3762ff0
fetched_at: '2026-06-29T00:10:57.850358+00:00'
page_id: '600134389'
product: rm
source: tdn-rm
title: Configuração do Relatório para o Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=600134389
version: 23
---

# Descrição

O objetivo principal deste provedor de dados é prover os dados em memória no momento da matrícula do aluno, ou seja, dados que ainda não foram salvos no banco de dados, além de prover dados básicos do aluno e dados financeiros referente ao plano de pagamento escolhido pelo aluno.

É importante frisar que os provedores abaixo somente funciona para relatório de contrato no portal do aluno, não sendo aplicado em nenhum outro lugar.

## Dados Básico do Aluno - Configuração

Como configurar

Este provedor tem o objetivo de trazer os **dados do aluno** pela tabela mostrada abaixo.

**SDADOSMATRICULAPORTAL**

Tabela de dados básicos da matrícula do aluno, segue os campos possíveis:

* CODCOLIGADA: código da coligada do contexto.
* CODFILIAL: código da filial do contexto.
* CODTIPOCURSO: código do nível de ensino do contexto.
* IDHABILITACAOFILIAL: identificador da matriz aplicada.
* IDPERLET: identificador do período letivo.
* NOMEALUNO: nome do aluno.
* CPFALUNO: CPF do aluno.
* RA: registro acadêmico do aluno.
* GERARMANIFESTO: indica se será gerado relatório com manifesto ou não.

Para adicionar o novo provedor acesse o relatório adicione conforme imagem abaixo.

Após adicionar o provedor a tabela SDADOSMATRICULAPORTAL estará disponível na lista de campos.

A partir daí é montar o layout desejado clicando e arrastando os campos para o layout do relatório.

Além disso é necessário criar os parâmetros conforme imagem.

Depois disso informar os parâmetros para o provedor de dados.

## Dados Financeiros - Configuração

Como configurar

Este tem o objetivo de trazer os **dados financeiros** do aluno pela tabela mostrada abaixo.

**SDADOSFINANCEIROS**

Tabela de dados financeiros, segue os campos possíveis:

* CODPLANOPAGAMENTOSELECIONADO: código do plano de pagamento selecionado.
* NUMPARCELAPLANOPAGTO: número de parcelas do plano de pagamento.
* VALORLIQPLANOPAGTODESCONSIDERADESCONTOS: valor líquido do plano de pagamento (desconsidera os descontos das parcelas do plano de pagamento).
* VALORPLARCELAPLANOPAGTO:  valor da parcela do plano de pagamento (valor total / número de parcelas).
* VALORTOTALPLANOPAGTO: valor total do plano de pagamento.

Para adicionar o novo provedor acesse o relatório adicione conforme imagem abaixo.

Após adicionar o provedor a tabela SDADOSFINANCEIROS estará disponível na lista de campos.

A partir daí é montar o layout desejado clicando e arrastando os campos para o layout do relatório.

Além disso é necessário criar os parâmetros conforme imagem.

Depois disso informar os parâmetros para o provedor de dados.

## Dados das Turmas/Disciplinas Selecionadas - Configuração

Como configurar

Este provedor tem o objetivo de trazer os **id das turmas/disciplinas selecionadas** do aluno pela tabela mostrada abaixo.

**STURMADISCSELECIONADAS**

Tabela das turmas/disciplinas selecionadas, segue os campos possíveis:

* CODCOLIGADA: código da coligada da turma/disciplina selecionada.
* IDTURMADISC: identificador da turma/disciplina selecionada.

Para adicionar o novo provedor acesse o relatório adicione conforme imagem abaixo.

Após adicionar o provedor a tabela STURMADISCSELECIONADAS estará disponível na lista de campos.

A partir daí é montar o layout desejado clicando e arrastando os campos para o layout do relatório.

Além disso é necessário criar os parâmetros conforme imagem.

Depois disso informar os parâmetros para o provedor de dados.

## Todos os dados - Configuração

Como configurar

O primeiro passo é criar um novo relatório informando a fonte de dados que é o novo provedor criado, o **Dados do contrato na matrícula do aluno no portal**.

Vale ressaltar que este provedor somente funciona se vinculado ao cadastro do relatório conforme abaixo.

**Uma vez vinculado não é possível remover a fonte de dados**, para remover, será necessário criar um novo relatório.

Ao abrir o layout do relatório e ir na lista de campos três tabelas irão aparecer, SDADOSFINANCEIROS, SDADOSMATRICULAPORTAL e STURMADISCSELECIONADAS, com os seus respectivos campos.

**SDADOSFINANCEIROS**

Tabela de dados financeiros, segue os campos possíveis:

* CODPLANOPAGAMENTOSELECIONADO: código do plano de pagamento selecionado.
* NUMPARCELAPLANOPAGTO: número de parcelas do plano de pagamento.
* VALORLIQPLANOPAGTODESCONSIDERADESCONTOS: valor líquido do plano de pagamento (desconsidera os descontos das parcelas do plano de pagamento).
* VALORPLARCELAPLANOPAGTO:  valor da parcela do plano de pagamento (valor total / número de parcelas).
* VALORTOTALPLANOPAGTO: valor total do plano de pagamento.

**SDADOSMATRICULAPORTAL**

Tabela de dados básicos da matrícula do aluno, segue os campos possíveis:

* CODCOLIGADA: código da coligada do contexto.
* CODFILIAL: código da filial do contexto.
* CODTIPOCURSO: código do nível de ensino do contexto.
* IDHABILITACAOFILIAL: identificador da matriz aplicada.
* IDPERLET: identificador do período letivo.
* NOMEALUNO: nome do aluno.
* CPFALUNO: cpf do aluno.
* RA: registro acadêmico do aluno.

**STURMADISCSELECIONADAS**

Tabela das turmas/disciplinas selecionadas, segue os campos possíveis:

* CODCOLIGADA: código da coligada da turma/disciplina selecionada.
* IDTURMADISC: identificador da turma/disciplina selecionada.

A partir daí é montar o layout desejado clicando e arrastando os campos para o layout do relatório.

Para exibir por exemplo o código da turma e nome da disciplina selecionada, deverá ser feito da seguinte maneira, primeiro deve-se criar uma consulta sql conforme abaixo.

Esta consulta deverá ser adicionada no relatório. Ao adicionar a consulta irá aparecer na lista de campos conforme abaixo.

Aparecendo ai é só arrastar os campos desejados para o layout do relatório.

Quando o aluno for finalizar a matrícula o relatório será exibido conforme o novo layout.

# Relatório Exemplo

Segue relatório exemplo utilizando os três novos providers abaixo:

* Dados do contrato na matrícula do aluno no portal
* Dados básicos do aluno
* Turmas/Disciplinas selecionadas

Para baixar o exemplo do relatório .
