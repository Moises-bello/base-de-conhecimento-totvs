---
content_hash: 63f4fdc2d5d2687ce8d58f603596b94eaea1656a7bd8a30bcb8d415f71ff45f7
fetched_at: '2026-06-29T00:06:30.094726+00:00'
page_id: '235312613'
product: rm
source: tdn-rm
title: TUNBAT_DT_Frequencia_Diaria_WebService_TBC
type: documentation
url: https://tdn.totvs.com/display/LRM/TUNBAT_DT_Frequencia_Diaria_WebService_TBC
version: 122
---

# Manipulação de Frequência Diária através de WebService

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | *Classis.NET* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Frequência Diária* | *Frequência Diária.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Manipulação de Frequência Diária através de WebService*.* | *Frequência Diária.* | |  |  | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | N/A |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *SFREQUENCIA* |
| **Sistema(s) Operacional(is):** | *Windows* |

## **Digitação de Frequência Diária através do TBC**

Para digitação de Frequência Diária através do TBC (WebService wsDataServer), foi criado um novo dataserver chamado EduFrequenciaDiariaWSData para que seja possível a digitação da frequência diária pelo WebService. Este dataserver irá manipular as frequências dos alunos contidos na tabela SFREQUENCIA, o campo AULASDADAS da tabela SETAPAS e AULASDADAS da tabela SNOTAETAPA.

**ReadView**

O ReadView irá retornar um DataSet contendo 2 tabelas. SFREQUENCIAWS e NumAulasEtapa.

**Exemplo de retorno do NumAulasEtapa:**

xml
40
2016-02-29T00:00:00
2016-07-09T00:00:00
N
2016-03-24T12:08:56.29
38
]]>

**Exemplo de retorno do SFREQUENCIAWS:**

xml
1
614919
499205
1284372
2016-02-29T00:00:00
A
499205
]]>

**Parâmetros**

**DataServerName:** Informar o dataServer EduFrequenciaDiariaWSData.

**Filtro:** O filtro passado no ReadView deverá conter obrigatoriamente no mínimo três informações: CODCOLIGADA, CODETAPA e IDTURMADISC. Os campos contidos neste filtro podem ser informados em qualquer ordem. Exemplo: CODCOLIGADA = 1 AND CODETAPA = 1 AND IDTURMADISC = 614919 AND SPLANOAULA.DATA = 29/02/2016

**Contexto**: O parâmetro de contexto é importante para que o DataServer consulte as informações contidas nos parâmetros do sistema. Portanto, é muito importante que as informações passadas sejam condizentes com a mesma Coligada, Filial e Nível de Ensino das frequências manipuladas. Os valores são separados por vírgula, e não devem conter espaços entre os valores e o igual (=).

Segue abaixo um exemplo de todos os parâmetros informados no SoapUI.

xml




EduFrequenciaDiariaWSData

CODCOLIGADA = 1 AND CODETAPA = 1 AND
IDTURMADISC = 614919 AND SPLANOAULA.DATA = 29/02/2016

 CODCOLIGADA=1;CODTIPOCURSO=1;CODFILIAL=1;CODSISTEMA=S 

mestre

totvs
]]>

**ReadRecord**

O ReadRecord irá retornar um DataSet contendo 4 tabelas. SFREQUENCIA, AlunosFreq, PlanoAulaFreq e NumAulasEtapa.

**Exemplo do retorno da SFREQUENCIA:**

xml
1
499205
614919
1284372
2016-02-29T00:00:00
A
499205
]]>

**Exemplo do retorno da AlunosFreq:**

xml
1
2016-02-29T00:00:00
499209
21:00
22:23
26222496
614919
]]>

**Exemplo do retorno da NumAulasEtapa:**

xml
40
2016-02-29T00:00:00
2016-07-09T00:00:00
N
2016-03-24T17:58:34.753
38
]]>

**Parâmetros**

**DataServerName:** Informar o dataServer EduFrequenciaDiariaWSData.

**PrimaryKey:** Deverá ser passado 5 valores para chave primária separados por ponto e vírgula (;). São eles, CODCOLIGADA, IDTURMADISC, CODETAPA, SPLANOAULA.DATA (De), SPLANOAULA.DATA (Até), CODSUBTURMA.

Os 3 primeiros parâmetros são obrigatórios. CODCOLIGADA, IDTURMADISC e CODETAPA. Os demais são opcionais. Exemplo: 1;614919;1;29/02/2016;29/02/2016;2

**Contexto**: O parâmetro de contexto é importante para que o DataServer consulte as informações contidas nos parâmetros do sistema. Portanto, é muito importante que as informações passadas sejam condizentes com a mesma Coligada, Filial e Nível de Ensino das frequências manipuladas. Os valores são separados por vírgula, e não devem conter espaços entre os valores e o igual (=).

Segue abaixo um exemplo de todos os parâmetros informados no SoapUI.

xml




EduFrequenciaDiariaWSData

1;614919;1;29/02/2016;29/02/2016

CODCOLIGADA=1;CODTIPOCURSO=1;CODFILIAL=1;CODSISTEMA=S

mestre

totvs
]]>

**SaveRecord**

O SaveRecord irá efetivamente manipular os registros da tabela SFREQUENCIA. Para que os dados sejam salvos corretamente, devem ser seguidos algumas premissas.

Deverá ser obrigatoriamente ser passado um DataTable chamado **PARAMS**, passando algumas informações que são pré-requisitos para o dataserver. Este DataTable deve conter os campos: CODCOLIGADA, IDTURMADISC, CODETAPA, AULASDADAS e CODSUBTURMA.

Outro DataTable chamado **AlunosFreq** também deverá ser passado como parâmetro, contendo os campos CODCOLIGADA, RA, IDTURMADISC, IDTURMADISCORIGEM.

Deverá também conter o datatable referente a SFREQUENCIA no qual contém as informações da frequência efetivamente.

O campo **Data** deverá ser informado no formato americano (YYYY-MM-DD), concatenado também com as informações de hora (HH:MM:SS). Para o cadastro de frequência este valor de hora será ignorado, porém, se torna obrigatório informar este valor juntamente com a data, devido a este campo fazer parte da Chave-primária da tabela de SFREQUENCIA, onde o WebService wsDataServer utiliza esta informação para pesquisar se a mesma frequência já existe na base. Portanto o horário pode ser sempre informado como “T00:00:00”.

O campo **Presenca** espera dois valores. P ou A.

P: Presença

A: Ausência.

Se for informado uma ausência para o aluno, o dataServer irá incluir um novo registro na tabela SFREQUENCIA indicando esta ausência. Se for informado uma Presença, o dataserver irá **excluir** o registro referente a ausência do aluno na tabela SFREQUENCIA.

**Turma Gerencial:**

Caso seja necessário a manipulação de registros de frequência para Turmas Gerenciais, deve ser informado o código IDTURMADISC da turma gerencial na tabela PARAMS dos parâmetros passados para o SaveRecord, e nos demais lugares onde deve ser informado o IDTURMADISC, deve ser informado o IDTURMADIC da Turma/Disciplina em que o aluno está matriculado aluno.

Segue abaixo um exemplo de todos os parâmetros informados no SoapUI.

xml

1
614919
499205
1739082
A
2016-02-29T00:00:00

1
614919
499208
1739082
A
2016-02-29T00:00:00

1
1739082
614919


1
614919
1
40

]]]]>]]>

divs
