---
content_hash: f1072d7dcd4730f9ad034c820b5e5f6dbdce1695166062b66c8e3831b2bd32da
fetched_at: '2026-06-29T00:08:51.153787+00:00'
page_id: '337346599'
product: rm
source: tdn-rm
title: Listar Boletos
type: documentation
url: https://tdn.totvs.com/display/LRM/Listar+Boletos
version: 11
---

## Visão Geral do Programa

O objetivo do método **"ListarBoletos"**, presente no webservice do Educacional (**wsEdu**), é disponibilizar uma listagem de todos os boletos dos contratos do aluno, em aberto no **TOTVS Gestão Educacional**, que estiverem vinculados à turma/disciplina informada.

A API irá retornar uma lista com os códigos dos boletos e suas respectivas datas de vencimentos.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

### Método ListarBoletos

Este método realiza a listagem de todos os boletos do aluno, presente em seus contratos não cancelados no TOTVS Gestão Educacional. Como informações obrigatórias no **XML**, devem ser informados o registro acadêmico do aluno, código da coligada, código da filial, código do tipo de curso e o identificador de uma turma/disciplina a qual o aluno está matriculado. Todos os boletos listados estarão vinculados ao curso/habilitações da matriz da turma/disciplina informada.

É importante destacar que serão listados, somente, os boletos em abertos.

Referente às informações: código da coligada, código da filial, código do tipo de curso e o identificador da turma/disciplina do aluno, elas deverão ser informadas no campo **"CodTurmaConcat",** separadas por vírgula.

Segue um exemplo, abaixo:

xml




ES-212814

1,1,1,1171
]]>

Na imagem acima observa que:

* Na tag "**RA**" tem a informação:
  + Registro acadêmico do aluno igual a ES-212814
* Na tag "**CodTurmaConcat**" tem as informações:
  + Código da Coligada igual a 1
  + Código da Filial igual a 1
  + Código do Tipo de Curso igual a 1
  + Referência da Turma/Disciplina do Aluno igual a 1171

O sistema irá realizar a consulta dos boletos do aluno, à partir das informações presente nas tag's "**RA**" e "**CodTurmaConcat**". Caso as informações existirem na base de dados, o sistema irá retorna um XML com os identificadores dos boletos e suas respectivas datas de vencimentos, conforme exemplo abaixo.

xmltrue



20/01/2025
7422
20/02/2025
7423
20/03/2025
7424
15/04/2025
7440
18/04/2025
7425
20/05/2025
7426
19/06/2025
7427
18/07/2025
7428
20/08/2025
7429
18/09/2025
7430
20/10/2025
7431
20/11/2025
7432
18/12/2025
7433
]]]]>
]]>

Caso nos contratos não cancelados do aluno não tenham boletos bancários vinculados ou o usuário não tenha permissão para visualização dos boletos do aluno, o retorno do XML será apresentado da seguinte forma:

xml





]]>
