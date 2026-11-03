---
content_hash: 0620a733e3c42c3595259f8b3c61d42d1c754118de3fd55d2ed4ac65d306129c
fetched_at: '2026-06-29T00:09:04.040893+00:00'
page_id: '382543996'
product: rm
source: tdn-rm
title: 3294477 EDUCACIONAL01-5683 DT Geração de Arquivo ENADE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382543996
version: 4
---

# GERAÇÃO DE ARQUIVO ENADE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | ENADE | ENADE |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Informe a(s) rotina(s) envolvidas. | Informe o nome técnico da(s) rotina(s) envolvidas. | |  |  | |
| **Cadastros Iniciais:** | Cadastro de Curso/Habilitação |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | [3292671](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%223292671%22 "3292671")[, 3270153,](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%223270153%22 "3270153") [3308673,](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%223308673%22 "3308673") [3317902,](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%223317902%22 "3317902") [3326071](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%223326071%22 "3326071")  [3301878,](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%223301878%22 "3301878") [3349561](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%223349561%22 "3349561"), [3349233](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%223349233%22 "3349233"), [3350442](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%223350442%22 "3350442")  [3329270,](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%223329270%22 "3329270") [3364370](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%223364370%22 "3364370"), [3369446](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%223369446%22 "3369446") |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [EDUCACIONAL01-5683](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-5683) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Sql Server, Oracle |
| **Tabelas Utilizadas:** | SINSTITUICAOMEC, SCURSOMEC, SHABILITACAOFILIAL, SHABILITACAOALUNO, SMATRICPL, SSTATUS, SGRADE, SHABILITACAO, SCURSO, SPLETIVO, SALUNO, PPESSOA |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | N/A |

## Descrição

Foram feitas adequações na rotina de geração do arquivo ENADE para ingressantes e concluintes, conforme leiaute disponibilizado pelo INEP para o ano de 2018.

**Arquivo de Ingressantes:**

O nome do arquivo foi alterado para sair da seguinte forma: ENADE[CO\_PROJETO]\_ N92\_BR\_[DATA\_GERAÇÃO]\_[CO\_CURSO]\_[ORIGEM][SEQ\_GERAL].TXT,

onde:

* [CO\_PROJETO] será o código do projeto que é enviado no arquivo. Esse código aparece na tela de geração do arquivo.
* [DATA\_GERAÇÃO] será a data atual da geração do arquivo no formato "AAAAMMDD";
* [CO\_CURSO] será o código do primeiro curso da lista de alunos selecionada para a geração do arquivo;
* [ORIGEM] será o tipo da origem que é enviado no arquivo;
* [SEQ\_GERAL] será o número sequencial escolhido na rotina de geração do arquivo.

Campos alterados:

* CO\_PROJETO: Será gerado um código com os dois últimos dígitos do ano corrente mais a sequência numérica "11101" (por exemplo: 1811101). Esse código poderá ser alterado na tela de geração do arquivo.
* NU\_PERCENTUAL\_INTEGRALIZACAO: Será o percentual de carga horária integralizada pelo aluno. O valor terá uma casa decimal, separada por ponto.
* NU\_ANO\_INICIO\_GRADUACAO: Será o ano de início do curso no formato AAAA. Será utilizado o ano da data de ingresso no curso, do anexo de curso/habilitação do aluno.
* NU\_SEMESTRE\_INICIO\_GRADUACAO: Será o semestre de início do curso: 1 se for primeiro semestre e 2 se for segundo. Será utilizado a data de ingresso no curso, do anexo de curso/habilitação do aluno para identificar o semestre.

**Arquivo de Concluintes:**

O nome do arquivo foi alterado para sair da seguinte forma: ENADE[CO\_PROJETO]\_ N99\_BR\_[DATA\_GERAÇÃO]\_[CO\_CURSO]\_[ORIGEM][SEQ\_GERAL].TXT,

onde:

* [CO\_PROJETO] será o código do projeto que é enviado no arquivo. Esse código aparece na tela de geração do arquivo.
* [DATA\_GERAÇÃO] será a data atual da geração do arquivo no formato "AAAAMMDD";
* [CO\_CURSO] será o código do primeiro curso da lista de alunos selecionada para a geração do arquivo;
* [ORIGEM] será o tipo da origem que é enviado no arquivo;
* [SEQ\_GERAL] será o número sequencial escolhido na rotina de geração do arquivo.

Campos alterados:

* CO\_PROJETO: Será gerado um código com os dois últimos dígitos do ano corrente mais a sequência numérica "11101" (por exemplo: 1811101). Esse código poderá ser alterado na tela de geração do arquivo.
* NU\_CEP\_POLO: Esse campo foi retirado.
* NU\_PERCENTUAL\_INTEGRALIZACAO: Será o percentual de carga horária integralizada pelo aluno. O valor terá uma casa decimal, separada por ponto.
* NU\_ ANO\_FORMATURA: Será o ano que o aluno integralizará 100% da carga horária. Para calcular o ano foi disponibilizado duas opções na tela de geração do arquivo ENADE:
  1. Por períodos: Será calculado de acordo com o número de períodos que faltam para o aluno concluir o curso, portanto, será necessário verificar o período informado na última matrícula no período letivo do aluno.
  2. Por carga horária: Será calculado de acordo com a quantidade de carga horária que falta para o aluno concluir o curso, portanto, será necessário ter as informações de total de créditos, carga horária e máximo de créditos por período cadastrados na matriz curricular.
* NU\_ SEMESTRE\_ FORMATURA: Será o semestre que o aluno integralizará 100% da carga horária. O cálculo será feito conforme o campo NU\_ ANO\_FORMATURA.
* CO\_MUNICIPIO\_POLO: Será utilizado o município do campus do curso/habilitação do aluno. Só será obrigatório para curso de EaD. Será utilizado a tabela do IBGE conforme é feito no Censo.
