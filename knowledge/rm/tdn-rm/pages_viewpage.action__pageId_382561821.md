---
content_hash: 46169c3ea25149d9649edeed99260ce4e39eac3c39e5edddc8e3fc75cec194d6
fetched_at: '2026-06-29T00:09:04.225068+00:00'
page_id: '382561821'
product: rm
source: tdn-rm
title: DataServer de Frequência diária/Justificativa de falta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382561821
version: 47
---

O objetivo deste DataServer é possibilitar a busca, inclusão e alteração da frequência diária do aluno através de um Webservice. Tudo que for realizado, poderá ser visualizado na tela de frequência diária no TOTVS Gestão Educacional.

Através do DataServer **EduFrequenciaDiariaWSData** e por meio dos métodos **ReadView,** **ReadRecord e SaveRecord**, é possível realizar a busca, inclusão e manutenção das frequências dos alunos em turmas/disciplinas no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Método ReadView

Complementar ao método ReadRecord, o **ReadView** utilizará um filtro para realizar a consulta das frequências diárias já salvas dos alunos.

Para realizar a chamada do ReadView, o XML irá conter uma tag chamada **Filtro**, onde deverá ser informado os seguintes parâmetros:

* CODCOLIGADA: Código da Coligada.
* IDTURMADISC: Id da turma/disciplina.
* CODETAPA: Código da etapa.
* SPLANOAULA.DATA: Data de início.
* SPLANOAULA.DATA: Data final.
* CODSUBTURMA (opcional)

Segue um exemplo de filtro que pode ser especificado na tag **Filtro** do XML do método ReadView:

sqlExemplo:

Um exemplo utilizando o filtro opcional por **subturma**:

sqlExemplo:

**Importante:**

Quando houver a necessidade de retornar informações das frequências dos alunos em uma **Sub-turma**, **é obrigatório utilizar o método ReadView**, e não o ReadRecord devido a arquitetura do ReadRecord filtrar apenas pelos campos da PK da frequência diária, que não inclui a Sub-turma.

Os campos de datas precisam ser informados com o nome da tabela e do campo para que o sistema identifique o filtro corretamente.

Para isso é necessário que a data seja informada utilizando "SPLANOAULA.DATA".

sqlExemplo de XML para consulta por ReadView da frequência de alunostrue




EduFrequenciaDiariaWSData

CODCOLIGADA = 1 AND IDTURMADISC = 1055 AND CODETAPA = 1 AND SPLANOAULA.DATA = 30-09-2018 AND SPLANOAULA.DATA = 20-10-2018

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>sqlExemplo de XML de retornotrue




1
1055
295
0000107
2018-10-01T00:00:00
A
295

1
1055
295
0000107
2018-10-08T00:00:00
A
295

1
1055
295
0000107
2018-10-15T00:00:00
A
295

1
1055
295
0000112
2018-10-01T00:00:00
A
295
]]]]>
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de uma frequência de aluno. **O sistema realiza apenas a inclusão de marcações de ausências.**

Caso seja definida uma marcação de presença, o sistema não irá incluir nenhum registro e o retorno será vazio.

Caso exista uma marcação de ausência, ela será excluída e o retorno, também, será vazio.

**Inclusão de uma marcação de frequência**

Para realizar inclusão de uma marcação de frequência, deve ser utilizada a operação ***SaveRecord*** que irá manipular os registros da tabela **SFREQUENCIA**.

Para que os dados sejam salvos corretamente, devem ser seguidos algumas premissas.

O **XML,** **obrigatoriamente**, deverá conter uma tag chamada **PARAMS** que será responsável por passar os seguintes campos pré-requisitos para a inclusão/alteração da marcação de frequência:

* CODCOLIGADA: Código da coligada.
* IDTURMADISC: Id da turma/disciplina.
* CODETAPA: Código da Etapa.
* AULASDADAS: Quantidade de aulas dadas.
* CODSUBTURMA: Código da subturma (opcional).

Nota

Quando o **SaveRecord** for chamado através de uma**Fórmula Visual** na atividade de **Salvar registro**, deve-se passar os campos concatenados, separados por vírgula (,) e sem espaços através item **Dados do Usuário** na atividade de **Salvar Registro,**para o sistema utilizar na montagem dos parâmetros (**PARAMS)**necessários para as validações da frequência.

A tag com o nome **AlunosFreq,** deverá ser incluída no **XML**, contendo os campos:

* CODCOLIGADA: Código da coligada.
* RA: Registro Acadêmico do aluno.
* IDTURMADISC: Id da turma/disciplina.
* IDTURMADISCORIGEM: Id da turma/disciplina de origem (para mais informações [clique aqui](https://tdn.totvs.com/x/FvxbGQ)).

Por fim, a tag **SFREQUENCIA** conterá as informações da frequência que será lançada:

* CODCOLIGADA: Código da coligada.
* IDTURMADISC: Id da turma/disciplina.
* RA: Registro Acadêmico do aluno.
* PRESENCA: A ou P.
* JUSTIFICADA: 0 ou 1.
* IDJUSTIFICATIVAFALTA: Id da justificativa da falta (para mais informações [clique aqui](https://tdn.totvs.com/x/pfpbGQ)).
* DATA: Data da aula.

Importante

O campo **PRESENCA** espera dois valores. (P ou A)

P: Presença

A: Ausência.

O campo **JUSTIFICADA** espera dois valores. (1 ou 0)

1: Falta abonada

0: Falta não abonada.

**Turma Gerencial:**

Caso seja necessária a manipulação de registros de frequência para turmas gerenciais, deve ser informado o código **IDTURMADISC** da turma gerencial na tag **PARAMS** dos parâmetros passados para o ***SaveRecord.***

No lançamento da frequência, o **IDTURMADISC** deverá conter o código da turma/disciplina em que o aluno está matriculado.

false

O campo **Data** deverá ser informado no formato americano **(*****YYYY-MM-DD*****).**

Exemplo: **2018-07-11T00:00:00**

***Obs.:*** A parte horária é necessária, composta por "**T00:00:00**", para que o sistema entenda corretamente a data.

xmlExemplo de XML para inclusão/alteração de uma frequênciatrue

EduFrequenciaDiariaWSData



1
1217
295
ES-00180
A
1
6
2018-07-17T00:00:00

1
ES-00180
1217


1
1217
1
1

]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno da inclusão/alteração de uma frequênciatrue
1;295;1217;ES-00180;17/07/2018 00:00:00
]]>

## Método ReadRecord

Este método consulta as frequências dos alunos já registradas, aplicando filtros baseados em campos específicos previamente definidos pelo RM. Vale ressaltar que o método **ReadRecord** não retorna informações de frequências de alunos com **CODSUBTURMA**, pois o ReadRecord filtra apenas pelos campos de chave primária da Frequencia Diária ignorando qualquer informação adicional, portanto para essa operação deve ser utilizada obrigatoriamente o método **ReadView**.

Para realizar a chamada ao método ReadRecord, deve ser passado um **XML** contendo tags com a seguinte estrutura:

**DatasServerName**: EduFrequenciaDiariaWSData

**PrimaryKey**: Os seguintes campos fazem parte da chave primária da consulta executada pelo método ReadRecord. Qualquer valor adicional não será considerado no filtro:

* Código da coligada
* Código da turma/disciplina
* Código da etapa de falta da turma/disciplina
* Data início do plano de aula
* Data final do plano de aula

**Contexto**: Informar qual é o contexto utilizado durante a execução do WebService, contendo os seguintes campos, separados por ponto e vírgula.

* CODCOLIGADA: Código da coligada.
* CODFILIAL: Código da filial.
* CODTIPOCURSO: Código do nível de ensino.
* CODSISTEMA: Código do sistema, no caso "S" para o Educacional.

Segue um exemplo do **XML** utilizado para a chamada a função ReadRecord:

xmlExemplo de XML para chamada ao ReadRecordtrue

EduFrequenciaDiariaWSData

1;295;1;01-01-2024;31-01-2024;125

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>

Ao executar o método ReadRecord filtrando pelos valores da chave primaria informada, caso não retorne registro, será retornado um XML vazio contendo o nome do **DataSet**, conforme exemplo abaixo:

xmlExemplo do retorno sem registrostrue<EduFrequenciaDiaria />]]>

Caso contrário, será retornado os dados conforme abaixo:

xmlExemplo do retorno de consulta de uma frequênciatrue


1
295
1217
ES-00180
2018-07-17T00:00:00
A
0
2
]]]]>
]]>

Para a inclusão de uma justificativa, será necessário informar o código da mesma, cadastrada anteriormente, através do menu de cadastros auxiliares.

***Educacional | Currículo e Oferta | Auxiliares | Justificativas de falta***

Exemplo:

2 - Visita ao médico

*<JUSTIFICADA>1</JUSTIFICADA>*

*<IDJUSTIFICATIVAFALTA>2</IDJUSTIFICATIVAFALTA>*

**Importante:**

Para fórmulas visuais usar a Atividade **EduFrequenciaActivity**. Para mais informações sobre Atividades acesse o a documentação: .

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
