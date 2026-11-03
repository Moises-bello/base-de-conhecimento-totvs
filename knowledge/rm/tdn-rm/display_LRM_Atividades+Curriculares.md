---
content_hash: 8d7a0d4c85dd3a4beecd49549037fb206de4f37c1d48a4e283e080c8d54c70d2
fetched_at: '2026-06-29T00:08:47.144234+00:00'
page_id: '318611465'
product: rm
source: tdn-rm
title: Atividades Curriculares
type: documentation
url: https://tdn.totvs.com/display/LRM/Atividades+Curriculares
version: 10
---

## Visão Geral do Programa

O objetivo deste dataserver é possibilitar a inclusão e alteração de atividades curriculares através de webservice. As informações incluídas ou alteradas poderão ser visualizadas no anexo de atividades curriculares do curso/habilitação do aluno no TOTVS Gestão Educacional.

Através do dataserver "**EduInscAlunoAtvOfertadaData**" é possível, por meio do método **SaveRecord**, realizar a manutenção de atividades curriculares, assim como na tela de anexo de atividades curriculares do curso/habilitação do aluno no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

### Método SaveRecord

Este método realiza a inclusão ou alteração de uma atividade curricular para um aluno. Deve ser informando o código da coligada e o id da atividade, além das outras informações que compõe a atividade curricular do aluno. O sistema irá realizar uma inclusão da atividade curricular caso o id da atividade não exista na base. Se o id já existir, a atividade curricular será alterada de acordo com as informações passadas.

Observação: Caso sejam passadas para o dataserver informações para campo complementar, deve ser utilizada a mesma coligada e o mesmo id da atividade curricular.

#### **Utilização do WebService**

**Inclusão de atividade curricular**

Para realizar inclusão de uma atividade curricular para um aluno, deve ser utilizado a operação de SaveRecord. Deve ser passado um XML contendo todos os campos que serão incluídos na atividade curricular. O campo IDATIVIDADE deve conter um valor inexistente no banco (por exemplo -1 ou  0). Caso queira incluir também um campo complementar, o XML deve conter a tabela SATIVIDADEALUNO com os campos CODCOLIGADA e IDATIVIDADE possuindo os mesmos valores da tabela SATIVIDADEALUNO.

Campos obrigatórios: CODCOLIGADA, IDATIVIDADE, IDHABILITACAOFILIAL e RA

### Exemplo de XML para inclusão de atividade curricular

### Exemplo do retorno da inclusão da atividade curricular

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada e o id da atividade inserida no item SaveRecordResult

**Alteração de atividade curricular**

Para realizar alteração de uma atividade curricular para um aluno, deve ser utilizado a operação de SaveRecord. Deve ser passado um XML contendo todos os campos que serão alterados na atividade curricular. O campo IDATIVIDADE deve conter o id da atividade que se deseja alterar. Caso queira alterar também o campo complementar, o XML deve conter a tabela SATIVIDADEALUNO com os campos CODCOLIGADA e IDATIVIDADE possuindo os mesmos valores da tabela SATIVIDADEALUNO.

Campos obrigatórios: CODCOLIGADA, IDATIVIDADE

### Exemplo de XML para alteração de atividade curricular

### Exemplo do retorno da alteração da atividade curricular

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada e o id da atividade alterada no item SaveRecordResult
