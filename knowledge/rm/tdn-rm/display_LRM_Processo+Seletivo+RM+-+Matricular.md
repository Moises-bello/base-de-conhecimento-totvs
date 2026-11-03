---
content_hash: 7637419f49894e72cd756c6e957d33e7d1d2579055169f41c82261d7b1a6bcde
fetched_at: '2026-06-29T00:10:12.621191+00:00'
page_id: '454830973'
product: rm
source: tdn-rm
title: Processo Seletivo RM - Matricular
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+Seletivo+RM+-+Matricular
version: 28
---

## Visão Geral do Programa

O objetivo deste ProcessServer é possibilitar matricular candidatos aprovados no processo seletivo através de WebService. A matrícula do candidato poderá ser visualizadas através da visão de Matrícula no período letivo do aluno do Totvs Educacional.

Este ProcessServer também poderá ser utilizado para matricular candidatos através de processos seletivos que utilizem a modalidade venda online de cursos.

Através do processServer "**EduMatricAprovadosPSData**" é possível, por meio do método **ExecuteWithXmlParams**, realizar a inclusão da matrícula do candidato.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

### Método ExecuteWithXmlParams

Este método realizará a inclusão da matrícula do candidato.

O contexto para execução do processo e validações dos parâmetros do sistema junto ao perfil do usuário, são  $CODCOLIGADA, $CODFILIAL, $CODTIPOCURSO, $CODSISTEMA e $CODUSUARIO.

A seguir temos dois exemplos de XML um **completo,** com todas as tags, e outro **reduzido**, apenas com as tags necessárias.

xmlExemplo de XML COMPLETO para matricular candidato aprovado no processo seletivotrue

S
EduMatricAprovadosPSAction
true
false
false
mestre





$CODUNIDADEBIB
1

$CHAPAFUNCIONARIO
-1

$EXERCICIOFISCAL
1

$CODFILIAL
1

$RHTIPOUSR
-1

$CODUSUARIOSERVICO


$EDUTIPOUSR
-1

$CODLOCPRT
1

$CODUSUARIO
mestre

$CODSISTEMA
S

$CODCOLIGADA
1

$CODTIPOCURSO
3

$CODIGOEXTERNO
-1

$IDPRJ
-1
DotNet

false

978c1f00-fa98-4147-bd5e-16bdc4e889c4
Falha na execução do processo

false
BHN050103194
true
10.31.8.189
false


1
212852
false
BHN050103194

1000
1
guilherme.campolina
false

false
false



Assistente de matrícula de candidatos aprovados em processo seletivo
0
true
false
2019-02-07T16:50:51.6937442-02:00
JobMonitor
false
EduMatricAprovadosPSData

RM.Edu.Interfaces.IEduMatricAprovadosPS
4
RM.Edu.Interfaces.Intf, Version=12.1.24.1, Culture=neutral, PublicKeyToken=null
false
true

Processo executado com sucesso
false
true
mestre
false



1287302
1
1



0

118

04706139988
1985-12-15T00:00:00
27
JULIANA FRIEDRICH FARAJ
2
0


30264311/882861
EnsinoSuperior
false
false
false

1
1
3
T4BIO

0
0

 /
 /
false
413
10
27
false
false


1
mestre
false
false
true
false
false
true
false
false
false
true
0
0
104

false
false
123
123
123
false
NaoMatricularGerarLog
7

]]>xmlExemplo de XML REDUZIDO para matricular candidato aprovado no processo seletivotrue




EduMatricAprovadosPSData






$CODFILIAL
1

$CODUSUARIO
mestre

$CODSISTEMA
S

$CODCOLIGADA
1

$CODTIPOCURSO
3
DotNet






1287302
1
1



0

118

04706139988
1985-12-15T00:00:00
27
JULIANA FRIEDRICH FARAJ
2
0


30264311/882861
EnsinoSuperior
false
false
false

1
1
3
T4BIO

0
0

 /
 /
false
413
10
27
false
false


1
mestre
false
false
true
false
false
true
false
false
false
true
0
0
104

false
false
123
123
123
false
NaoMatricularGerarLog
7

]]]]>
]]>xmlExemplo do retorno da matrícula do candidato aprovado no processo seletivotrue


1
]]>falseTabela de referência das Tags do XML

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tags do item EduMatriculaParamsProc** | | | | | | |
| Tag | Obrigatório | Parâmetro  Interno | Aceita  Nulo | Tipo de  Dados | Exemplo | Descrição |
| ActionModule | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| ActionName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| CanParallelize | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| CanSendMail | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| CanWaitSchedule | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| CodUsuario | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| ConnectionId | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| ConnectionString | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| Tags do item Context É obrigatório informar esta tag, porém com as seguintes keys: CODTIPOCURSO, CODCOLIGADA, CODSISTEMA, CODUSUARIO e CODFILIAL. Segue exemplo: falseExemplo do item Contextxml   $CODTIPOCURSO 1  $CODCOLIGADA 1  $CODSISTEMA S  $CODUSUARIO mestre  $CODFILIAL 1 DotNet ]]> | | | | | | |
| CustomData | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| DisableIsolateProcess | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| DriverType | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ExecutionId | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| FailureMessage | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| FriendlyLogs | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| HideProgressDialog | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| HostName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| Initialized | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| Ip | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| IsolateProcess | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| JobID | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| JobServerHostName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| MasterActionName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| MaximumQuantityOfPrimaryKeysPerProcess | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| MinimumQuantityOfPrimaryKeysPerProcess | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| NetworkUser | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| NotifyEmail | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| NotifyEmailList | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| NotifyFluig | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| OnlineMode | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| Tags do item PrimaryKeyList É obrigatório informar esta tag. Segue exemplo: falseExemplo do item PrimaryKeyListxml ]]> | | | | | | |
| Tags do item PrimaryKeyNames É obrigatório informar esta tag. Segue exemplo: falseExemplo do item PrimaryKeyNamexml]]> | | | | | | |
| PrimaryKeyTableName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ProcessName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| QuantityOfSplits | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| SaveLogInDatabase | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| SaveParamsExecution | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ScheduleDateTime | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| Scheduler | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| SendMail | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ServerName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ServiceInterface | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ShouldParallelize | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ShowReExecuteButton | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| StatusMessage | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| SuccessMessage | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| SyncExecution | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| UseJobMonitor | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| UserName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| WaitSchedule | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| Tags do item EduMatricAprovadosPSParamsProc Esta tag é obrigatória, segue referência de todos os itens.   | Tag | Obrigatório | Parâmetro  Interno | Aceita  Nulo | Tipo de  Dados | Exemplo | Descrição | | --- | --- | --- | --- | --- | --- | --- | | Tags do item de Alunos Aprovados  | Tag | Obrigatório | Parâmetro  Interno | Aceita  Nulo | Tipo de  Dados | Exemplo | Descrição | | --- | --- | --- | --- | --- | --- | --- | | Cartidentidade | Não | Não | Sim | String | `1287302` | Carteira de identidade | | Classificacao | Não | Não | Sim | Inteiro | 1 | Classificação | | CodColigada | Sim | Não | Não | Inteiro | 1 | Código da coligada | | CodMae | Não | Não | **Sim** | Inteiro | Não é necessário informar no XML. | Código da mãe. | | CodPai | Não | Não | **Sim** | Inteiro | Não é necessário informar no XML. | Código do pai. | | CodRespAcademico | Não | Não | **Sim** | Inteiro | Não é necessário informar no XML. | Código do responsável acadêmico. | | CodUsuarioPS | Não | Não | Sim | Inteiro | 0 | Código do usuário do processo seletivo | | Codcoligadaresponsavel | Não | Não | **Sim** | Inteiro | Não é necessário informar no XML. | Código da coligada do responsável. | | Codpessoa | Não | Não | Sim | Inteiro | 118 | Código da pessoa | | Codpessoaresponsavel | Não | Não | **Sim** | Inteiro | Não é necessário informar no XML. | Código da pessoa responsável. | | Cpf | Não | Não | Sim | String | `04706139988` | CPF | | Dtnascimento | Não | Não | Sim | Data | `1985-12-15` | Data de nascimento | | Idps | Não | Não | Sim | Inteiro | 27 | Id. do processo seletivo | | Nome | Não | Não | Sim | String | `JULIANA FRIEDRICH FARAJ` | Nome | | Numeroinscricao | Não | Não | Sim | Inteiro | 2 | Número de inscrição. | | Pontuacao | Não | Não | Sim | Decimal | 0 | Pontuação. | | RA | Não | Não | Sim | String | Não é necessário informar no XML. | Registro acadêmico (RA) do aluno. | | ResponsavelFinanceiro | Não | Não | Sim | Objeto | Não é necessário informar no XML. | Informações do responsável financeiro | | Telefone1 | Não | Não | Sim | String | `882861` | Telefone | |  |  |  |  |  |  |  | | | | | | | | | Apresentacao | Não | Sim | Sim | Enumerado | `EnsinoSuperior` | Descrição do nível de ensino ( EnsinoSuperior ou EnsinoBasico). | | CadastraAlunoComoRespFinanc | Não | Não | Sim | Booleano | `false` | Indica se é para cadastrar o próprio aluno como responsável financeiro. Necessário informar CPF. | | CadastraContrato | Não | Não | Sim | Booleano | `false` | Indica se é para cadastrar Contrato. Necessário ser informado CodCFO. | | CadastraResponsavelPSComoRespFinanc | Não | Não | Sim | Booleano | `false` | Indica se é para cadastrar o responsável pelo processo seletivo como responsável financeiro do aluno. | | CodCampus | Não | Não | Sim | String | Não é necessário informar no XML. | Código do Campus/Polo. | | CodColigada | Sim | Não | Não | Inteiro | 1 | Código da coligada. | | CodFilial | Sim | Não | Não | Inteiro | 1 | Código da filial. | | CodTipoCurso | Sim | Não | Não | Inteiro | 3 | Código do tipo de curso (nível de ensino). | | CodigoTurma | Não | Não | Sim | String | `T4BIO` | Código da Turma. | | Contexto | Sim | Não | Não | Objeto |  | Contexto | | CotaFinal | Não | Não | Sim | Inteiro | 0 | Cota final. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true .** | | CotaInicial | Não | Não | Sim | Inteiro | 0 | Cota inicial. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true .** | | DataIngresso | Não | Não | **Sim** | Data | Não é necessário informar no XML. | Data de ingresso. | | DtCompetenciaFinal | Não | Não | Sim | String | 03/2018 | Data de competência final | | DtCompetenciaInicial | Não | Não | Sim | String | 01/2018 | Data de competência inicial | | GerarLancamento | Sim | Não | Sim | Booleano | false | Indica se é para gerar lançamento.   Somente irá gerar lançamento se a situação de matrícula exigir contrato financeiro e o obedecer os critérios abaixo:   * Preencher o campo **CodPlanoPgto;** * Preencher o campo **TipoSelecaoParcela**, ver valores permitidos pertinentes a este campo. | | HabilitacaoFilial | Não | Não | Sim | Inteiro | 413 | Id. da matriz aplicada | | IdAreaInteresse | Não | Não | Sim | Inteiro | 10 | Id. da área de interesse | | IdProcessoSeletivo | Não | Não | Sim | Inteiro | 27 | Id. do processo seletivo | | IncluirListaEspera | Não | Não | Sim | Booleano | false | Indica se é para incluir na lista de espera | | MatriculaOfertaOnline | Não | Não | Sim | Booleano | false | Indica se é matrícula em oferta online | | Tags do item de Perfil de Usuário  | Tag | Obrigatório | Parâmetro  Interno | Aceita  Nulo | Tipo de  Dados | Exemplo | Descrição | | --- | --- | --- | --- | --- | --- | --- | | InternalId | Não | **Sim** | Sim | String | Não é necessário informar no XML. |  | | CodColigada | Sim | Não | Nao | Inteiro | 1 | Código da coligada | | CodUsuario | Sim | Não | Não | String | mestre | Código do Usuário | | MatriculaAlunoComAtrasoBiblioteca | Não | Não | Sim | Booleano | false | Alterar situação de matrícula ou matricular aluno com empréstimo em atraso | | MatriculaAlunoComDebitoBiblioteca | Não | Não | Sim | Booleano | false | Alterar situação de matrícula ou matricular alunos com débitos na biblioteca | | MatriculaAlunoInadimplente | Não | Não | Sim | Booleano | true | Indica se é para matricular alunos inadimplentes | | MatriculaAlunoSemDocObrigatorios | Não | Não | Sim | Booleano | false | Indica se é para matricular alunos sem documentos obrigatórios entregues | | MatriculaAlunosComOcorrencia | Não | Não | Sim | Booleano | false | Indica se é para matricular alunos com ocorrências que bloqueiam a matrícula | | MatriculaComConflitoHorarios | Não | Não | Sim | Booleano | true | Indica se é para matricular alunos com choque de horários | | MatriculaComConflitoPreReq | Não | Não | Sim | Booleano | false | Indica se é para matricular alunos em disciplinas que o pré/co-requisitos não foi cumprido | | MatriculaEmTurmaCheia | Não | Não | Sim | Booleano | false | Indica se é para matricular em turmas com excesso de alunos | | MatriculaForaDoPeriodo | Não | Não | Sim | Booleano | false | Indica se é para matricular alunos após a data limite de matrícula no período letivo | | MatriculaSemMinCredPLetivo | Não | Não | Sim | Booleano | true | Indica se é para matricular alunos com créditos abaixo/acima do nº mínimo/máximo de créditos do período leitvo | | | | | | | | | ParcelaFinal | Não | Não | Sim | Inteiro | 1 | Parcela final. | | ParcelaInicial | Não | Não | Sim | Inteiro | 1 | Parcela inicial. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true.** | | PeriodoLetivo | Sim | Não | Não | Inteiro | 104 | Id. do Período letivo. | | PlanoPagamento | Não | Não | Sim | Objeto | Não é necessário informar no XML. | Plano de pagamento. | | SobrescreverDeficienciasAlunos | Não | Não | Sim | Booleano | false | Indica se as deficiências do candidato sobrescreverão as do aluno | | SobrescreverEnderecoAlunos | Não | Não | Sim | Booleano | false | Indica se o endereço do candidato sobrescreverão o do aluno | | StatusMatricCurso | Não | Não | Sim | Inteiro | 1 | Status da matrícula do curso. | | StatusMatricDisciplinas | Não | Não | Sim | Inteiro | 1 | Status da matrícula da disciplina | | StatusMatricPeriodoLetivo | Não | Não | Sim | Inteiro | 1 | Status da matrícula no período letivo. | | SubstituiRespFinanc | Não | Não | Sim | Data | false | Substituir responsável financeiro quando utilizar RA existente.  Caso esteja marcado com True nas tags CadastraAlunoComoRespFinanc ou CadastraResponsavelPSComoRespFinanc, o sistema irá substituir o responsável financeiro do aluno existente. | | TipoEscolhaGerarRA | Não | Não | Sim | Enumerado | NaoMatricularGerarLog | Definir a utilização de RA para candidatos existentes.  Opções de conteúdo permitido da tag:  NaoMatricularGerarLog = Não matricular o candidato se este contiver dois ou mais RA's e gerar Log.  UsarSomenteUmRa = Utilizar o primeiro RA que encontrar.  GerarNovoRA = Gerar novo RA.  PriorizarRAMesmoContexto = Prioriza a reutilização de um RA do mesmo contexto, caso não encontre utiliza o primeiro RA que encontrar.  ReutilizarRASomenteMesmoContexto = Utilizar RA somente se for do mesmo contexto, caso não encontre não matricular o aluno e gerar log. | | TipoMatricula | Não | Não | **Sim** | Inteiro | 7 | Tipo de matrícula. | | VincProvas | Não | Não | Sim | Data | Não é necessário informar no XML. | Grava as notas que o candidato conseguiu nas provas do Totvs Avaliação e Pesquisa. Necessário informar alunos aprovados. | | | | | | | |

Importante

* As tags que não são obrigatórias e/ou que aceitam nulo o recomendado é **não** informar elas no XML.
Informações

À partir das versões 12.1.24.274, 12.1.25.223, 12.1.26.166 e 12.1.27.107 foi disponibilizado os parâmetros:

* "DiasVencimentoPrimeiraParcela", este parâmetro permite definir quais os dias para o vencimento da primeira parcela do contrato quando definido para gerar contrato. Este parâmetro só está disponível para utilização via webservice e deve ser adicionado dentro do XML no seguinte formato:

xmlInformações0]]>

* "GerarContratoAssinado", este parâmetro permite se ao gerar o contrato o mesmo já vai indicar que está assinado. Este parâmetro só está disponível para utilização via webservice e deve ser adicionado dentro do XML no seguinte formato:

xmlInformaçõesfalse]]>Venda online de cursos

Para utilização deste ProcessServer para matricular candidatos na modalidade de venda online de cursos, é necessário alterar a tag "MatriculaOfertaOnline" no XML do processo no seguinte formato:

xmlBloco de códigotrue]]>
