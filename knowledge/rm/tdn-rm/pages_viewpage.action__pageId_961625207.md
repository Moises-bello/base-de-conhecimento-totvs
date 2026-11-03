---
content_hash: 2fd68a3fec301e63d5321610ae04248d5f7d7aff9fc4e99dc996224ffd9621d6
fetched_at: '2026-06-29T00:12:13.951878+00:00'
page_id: '961625207'
product: rm
source: tdn-rm
title: FAQ - Admissão de Funcionário via WS FopFuncData - TAG USUARIO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=961625207
version: 6
---

Este documento tem como objetivo demonstrar o comportamento do processo de admissão de funcionários por meio do WebService FOPFUNCDATA, considerando a transmissão ou não dos valores na TAG **USUARIO**. Elaboramos uma documentação que mapeia todos os cenários de combinação relacionados ao comportamento da TAG **CODUSUARIO**, visando facilitar o entendimento dos clientes que utilizam o WebService FopFuncData.

| Cenário da TAG USUÁRIO no XML | | Comportamento Produto |
| --- | --- | --- |
| **1** | XML enviado sem a tag <USUARIO>, transmitindo as tags <CODIGO> e <CODPESSOA> de um novo registro de pessoa na base. | O campo CODUSUARIO da tabela PPESSOA não será preenchido. |
| **2** | XML enviado com a tag <USUARIO>, transmitindo as tags  <CODIGO> e <CODPESSOA>  de um novo registro de pessoa na base. | O campo CODUSUARIO da tabela PPESSOA será preenchido com o valor repassado na tag.  **Observação**: Para o correto funcionamento, já deve existir o usuário cadastro na                  base. |
| **3** | XML enviado sem a tag <USUARIO>, transmitindo as tags <CODIGO> e <CODPESSOA> de um registro de pessoa já existente na base. | Caso o campo CODUSUARIO da tabela PPESSOA já tenha um usuário associado, este será replicado no novo registro. |
| **4** | XML enviado com a tag <USUARIO>  transmitindo as tags <CODIGO> e <CODPESSOA>  de um registro de pessoa já existente na base. | Caso o campo CODUSUARIO da tabela PPESSOA já tenha um usuário associado, este será sobrescrito com o novo valor repassado na tag. |
| **5** | XML enviado sem a tag <USUARIO>  repassando a tag <CODIGO>, <CODPESSOA> e a tag <CHAPA> de um registro de pessoa  já com  vínculo na base. | Caso o campo CODUSUARIO da tabela PPESSOA já tenha um usuário associado, este será replicado no novo registro. Caso contrário, este permanecerá nulo. |
| **6** | XML enviado com a tag <USUARIO>  transmitindo as tags <CODIGO>, <CODPESSOA> e a tag <CHAPA>de um registro de pessoa já com  vínculo na base. | Caso o campo CODUSUARIO da tabela PPESSOA já tenha um usuário associado, este será sobrescrito com o novo valor repassado na tag. |
| **7** | XML enviado com a tag <USUARIO> nula  transmitindo as tags <CODIGO>, <CODPESSOA> e a tag <CHAPA> de um pessoa já com um vínculo na base. | Em cenários em que a tag é enviada com valor nulo (<CODUSUARIO/>), o campo mesmo que preenchido será alterado para nulo. |
| **8** | XML enviado sem a tag <USUARIO> sem transmitir as tags <CODIGO>, <CODPESSOA> e <CHAPA>, gerando automaticamente o código de pessoa e com a base parametrizada para utilizar o sequencial de chapa. | Os campos CODPESSOA e CHAPA serão gerados automaticamente validando a unicidade de pessoa e respeitando os valores da tabela GAUTOINC. O campo CODUSUARIO da tabela PPESSOA será gerado com o valor nulo. |
| **9** | XML enviado com a tag <USUARIO> sem transmitir as tags <CODIGO>, <CODPESSOA> e <CHAPA>, gerando automaticamente o código de pessoa e com a base parametrizada para utilizar o sequencial de chapa. | Os campos CODPESSOA e CHAPA serão gerados automaticamente validando a unicidade de pessoa e respeitando os valores da tabela GAUTOINC. O campo CODUSUARIO da tabela PPESSOA será gerado com o valor repassado na tag. |
| **10** | XML enviado com a tag <USUARIO> nula, transmitindo as tags <CODIGO>, <CODPESSOA>  e com a base parametrizada para utilizar o sequencial de chapa. | Os campos CODPESSOA e CHAPA serão gerados automaticamente validando a unicidade de pessoa e  respeitando os valores da tabela GAUTOINC. O campo CODUSUARIO da tabela PPESSOA será gerado com o valor nulo e caso exista valores já associados na tabela PPESSOA,  este será alterado para nulo. |
