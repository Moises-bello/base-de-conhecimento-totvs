---
content_hash: 77456774c00713e70fa71e0c65ab1aa7853cf4f66497042f28ce2ab06b2d577d
fetched_at: '2026-06-29T00:08:58.596107+00:00'
page_id: '360450043'
product: rm
source: tdn-rm
title: Matricular aluno nas disciplinas
type: documentation
url: https://tdn.totvs.com/display/LRM/Matricular+aluno+nas+disciplinas
version: 11
---

## Visão Geral do Programa

O objetivo deste ProcessServer é possibilitar matricular o aluno em disciplinas através de WebService. As disciplinas matriculadas poderão ser visualizadas através da visão de Matrícula no período letivo do aluno do Totvs Educacional.

Através do processServer "**EduMatriculaProcData**" é possível, por meio do método **ExecuteWithXmlParams**, realizar a inclusão de disciplina na matrícula do aluno.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

### Método ExecuteWithXmlParams

Este método realizará a inclusão de disciplina na matrícula do aluno.

Os campos chaves obrigatórios para gravação no banco de dados (PrimaryKey) são:  CODCOLIGADA; IDPERLET; IDHABILITACAOFILIAL; RA

O contexto para execução do processo e validações dos parâmetros do sistema junto ao perfil do usuário, são  $CODCOLIGADA, $CODFILIAL, $CODTIPOCURSO, $CODSISTEMA e $CODUSUARIO.

Importante

* O campo **MatricularDisc** deverá estar obrigatoriamente com o valor **Sim.**
* A tag **Disciplinas** obrigatoriamente deverá ser informada.

A seguir temos dois exemplos de XML um **completo,** com todas as tags, e outro **reduzido**, apenas com as tags necessárias.

xmlExemplo de XML COMPLETO para matricular aluno nas disciplinastrue




EduMatriculaProcData



S
EduMatriculaDiscAction
true
false
false
mestre





$EXERCICIOFISCAL
2

$CODLOCPRT
-1

$CODTIPOCURSO
1

$EDUTIPOUSR
-1

$CODUNIDADEBIB
5

$CODCOLIGADA
1

$RHTIPOUSR
-1

$CODIGOEXTERNO
-1

$CODSISTEMA
S

$CODUSUARIOSERVICO


$CODUSUARIO
mestre

$IDPRJ
2

$CHAPAFUNCIONARIO
-1

$CODFILIAL
1
DotNet

false

db998f27-adff-4602-b809-41fa8e593786
Falha na execução do processo

false
BHD0003799
true
10.31.8.49
false


1
103872
false
BHD0003799
EduMatricPLAction
1000
1
tiago.alves
false

false
false


1
27
4
ES-00226

CODCOLIGADA
IDPERLET
IDHABILITACAOFILIAL
RA
SMatricPL
Matricular aluno nas disciplinas
0
true
false
2018-09-24T14:44:59.8676932-03:00
JobMonitor
false
EduMatriculaProcData

RM.Edu.Interfaces.IEduMatriculaProc
4
RM.Edu.Interfaces.Intf, Version=12.1.22.1, Culture=neutral, PublicKeyToken=null
false
true

Processo executado com sucesso
false
true
mestre
false
true

false
false

false
true
false

true
1

1





1


1
1


mestre



false
false
false







2018-09-24T14:45:00.9237988-03:00





Nao



false
false
false
68

N

1

S001-1
1





14
13

1


1
TSI-2-032
0
mestre

2018-09-24T14:45:00.9237988-03:00


false
false
false
4

27
1128


true
false



false
false

PLEncerrado

false
false

ForaPeriodoMatricula

false
false

AlunoInadimplente

false
false

OcorrenciaAluno

false
false

TurmaCheia

false
false

FaltaDocObrigatorio

false
false

EmprestimoAtrasoBib

false
false

DebitoBiblioteca

false
false

StatusBloqAltSitMat

false
false

ForaPeriodoTurma

false
false

StatusBloqMatricPL

false
false

StatusBloqTranc

false
false

ForaPeriodoTranc

false
false

TrancPrimeiroPeriodo

false
false

MaxPeriodosTranc

false
false

NumPeriodosTranc

false
false

AlterouNumero

false
false

StatusBloqDisc

false
false

DiscAtraso

false
false

ChoqueHorarios

false
false

PreRequisito

false
false

CoRequisito

false
false

DisciplinaCursada

false
false

DisciplinaEmCurso

false
false

MinCreditos

false
false

MinDisciplinas

false
false

MinCargaHoraria

false
false

AprovEstudos

false
false

LimiteMatricula

false
false

PercLimiteMat

false
false

MinimoCreditosPL

false
false

MaximoCreditosPL

false
false

ParamCurso

false
false

JaMatriculadoPL

false
false

ProcEmail

false
false

ExcluiMatriculaComMovimento

false
false

PreRequisitoFormula

false
false

CoRequisitoFormula

false
false

ParamMatricula

false
false

StatusBloqAltSitMatDisc

false
false

MatriculaEmTurmaDiscGerencial

false
false

AlteraDataMatricula

false
false

DesenturmacaoTurmaMista

false
false

StatusBloqAltSitMatDiscPortal

false
false

MatrizCurricularInativa

false
false

TurmaCheiaCorrequisito

false
false

SincUsuarioIntegracaoPergamum

false
false

ErroConsultaPendenciaBiblioteca

false
false

PermiteMatOutraFilial

false
false

PermiteMatOutroNivelEnsino

false
false

MatriculaComMovimentacao
0
0


2147483647
16

0
false
false
false
false
false
0

false
false



ALGORÍTMOS E TÉCNICAS DE PROGRAMAÇÃO I




2.0000
2.0000




Produto

0
1
true
false
true
false
false
false
ES-00226
false
false
Default
Normal
1
false
false
true
true
 /
 /



false
Nao
true
true
0
4

27



false
false
true

0



61
0

eduProcessLog61
0
0




false
false

PLEncerrado

false
false

ForaPeriodoMatricula

false
false

AlunoInadimplente

false
false

OcorrenciaAluno

false
false

TurmaCheia

false
false

FaltaDocObrigatorio

false
false

EmprestimoAtrasoBib

false
false

DebitoBiblioteca

false
false

StatusBloqAltSitMat

false
false

ForaPeriodoTurma

false
false

StatusBloqMatricPL

false
false

StatusBloqTranc

false
false

ForaPeriodoTranc

false
false

TrancPrimeiroPeriodo

false
false

MaxPeriodosTranc

false
false

NumPeriodosTranc

false
false

AlterouNumero

false
false

StatusBloqDisc

false
false

DiscAtraso

false
false

ChoqueHorarios

false
false

PreRequisito

false
false

CoRequisito

false
false

DisciplinaCursada

false
false

DisciplinaEmCurso

false
false

MinCreditos

false
false

MinDisciplinas

false
false

MinCargaHoraria

false
false

AprovEstudos

false
false

LimiteMatricula

false
false

PercLimiteMat

false
false

MinimoCreditosPL

false
false

MaximoCreditosPL

false
false

ParamCurso

false
false

JaMatriculadoPL

false
false

ProcEmail

false
false

ExcluiMatriculaComMovimento

false
false

PreRequisitoFormula

false
false

CoRequisitoFormula

false
false

ParamMatricula

false
false

StatusBloqAltSitMatDisc

false
false

MatriculaEmTurmaDiscGerencial

false
false

AlteraDataMatricula

false
false

DesenturmacaoTurmaMista

false
false

StatusBloqAltSitMatDiscPortal

false
false

MatrizCurricularInativa

false
false

TurmaCheiaCorrequisito

false
false

SincUsuarioIntegracaoPergamum

false
false

ErroConsultaPendenciaBiblioteca

false
false

PermiteMatOutraFilial

false
false

PermiteMatOutroNivelEnsino

false
false

MatriculaComMovimentacao
0
0

false
false
false


0




1
false
true
ES-00226
false

Inclusao
IdParcela
false
false
true
true

Sim
]]]]>
]]>xmlExemplo de XML REDUZIDO para matricular aluno no período letivo junto com as disciplinastrue




EduMatriculaProcData






$CODTIPOCURSO
1

$CODCOLIGADA
1

$CODSISTEMA
S

$CODUSUARIO
mestre

$CODFILIAL
1
DotNet


1
4
ES-00222

CODCOLIGADA
IDHABILITACAOFILIAL
RA

1
1
1
1
TSI-2-032
mestre
2018-09-19T07:44:41.625612-03:00


1
1
13
1
mestre
2018-09-24T12:58:13.7370737-03:00
false
4
27
1128
1
ES-00226
Normal
1
true
4
27
1
ES-00222
Sim
]]]]>
]]>xmlExemplo do retorno da matrícula do aluno em disciplinastrue


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
| Tags do item PrimaryKeyList É obrigatório informar esta tag. Segue exemplo: falseExemplo do item PrimaryKeyListxml  1 4 ES-00222 ]]> | | | | | | |
| Tags do item PrimaryKeyNames É obrigatório informar esta tag. Segue exemplo: falseExemplo do item PrimaryKeyNamexml CODCOLIGADA IDHABILITACAOFILIAL RA ]]> | | | | | | |
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
| CadastrarDisciplinas | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Carregamento das disciplinas na tela do processo de matrícula. |
| Tags do item MatricPLParams Esta tag é obrigatória, segue referência de todos os itens.   | Tag | Obrigatório | Parâmetro  Interno | Aceita  Nulo | Tipo de  Dados | Exemplo | Descrição | | --- | --- | --- | --- | --- | --- | --- | | AlteraMatrizContratoOriginal | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Altera matriz do contrato original na transferência interna. | | ApagarNumeroDiario | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é para apagar o número do diário da matrícula no período letivo e/ou na disciplina de origem na mudança de turma. | | CR | Não | Sim | Sim | Decimal | Não é necessário informar no XML. | Coeficiente de rendimento. | | CadastrarContrato | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é para cadastrar contrato. | | CancelarLancamentos | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é para cancelar lançamentos. | | CarteiraEmitida | Não | Não | Sim | Booleano | false | Indica se a carteirinha foi emitida. Campo exclusivo para o **Ensino Básico**. | | ClientIP | Não | Sim | Sim | String | Não é necessário informar no XML. | Número de IP da máquina onde foi originada a chamada para a matrícula. | | CobrarDocsTipoIngressoRematriculaEB | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se na rematrícula do ensino básico será considerado documentos do tipo ingresso. | | CodColigada | Sim | Não | Não | Inteiro | 1 | Código da coligada. | | CodContrato | Não | Não | Sim | String | 655 | Código do contrato caso o aluno já possua. | | CodFilial | Sim | Não | Não | Inteiro | 1 | Código da filial. | | CodFormula | Não | Sim | Sim | String | Não é necessário informar no XML. | Código da fórmula. | | CodInstDestino | Não | Sim | Sim | String | Não é necessário informar no XML. | Código da instituição de destino. | | CodMotivo | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Código do motivo. | | CodMotivoTransferencia | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Código do motivo da transferência. | | CodPlanoPgto | Não | Não | Sim | String | SIPP | Código do plano de pagamento. | | CodStatus | Sim | Não | Não | Inteiro | 1 | Código da situação de matrícula. | | CodStatusNovo | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Novo código da situação de matrícula. | | CodStatusRes | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Código da situação de resultado. | | CodTipoCurso | Sim | Não | Não | Inteiro | 1 | Código do tipo de curso (nível de ensino). | | CodTipoMat | Não | Não | Sim | Inteiro | 1 | Código do tipo de matrícula. | | CodTurma | Não | Não | Sim | String | TSI-2-032 | Código da turma do período letivo. | | CodTurmaAnterior | Não | Sim | Sim | String | Não é necessário informar no XML. | Código da turma anterior. | | CodUsuario | Sim | Não | Não | String | mestre | Código do usuário. | | ColigadaRelatBoleto | Não | Não | Sim | Inteiro | 1 | Código da coligada do relatório do boleto. Para o seu preenchimento a situação de matrícula tem que exigir contrato financeiro e o campo **IdRelatBoleto** deverá estar preenchido. | | ColigadaRelatContrato | Não | Não | Sim | Inteiro | 1 | Código da coligada do relatório do contrato. Para o seu preenchimento a situação de matrícula tem que exigir contrato financeiro e o campo **IdRelatContrato** deverá estar preenchido. | | ContratosTemp | Não | Sim | Sim | Objeto | Não é necessário informar no XML. | Lista de contratos | | CopiarDescontoPorAntecipacao | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é para copiar descontos por antecipação do contrato antigo na criação de um novo contrato. | | CopiarRespFinanceiroContrato | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é para copiar responsável financeiro do contrato. | | CopiarVencimentos | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é para copiar os vencimentos. | | CotaFinal | Não | Não | Sim | Inteiro | 1 | Cota final. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true** e o campo **TipoSelecaoParcela = Parcela**. | | CotaInicial | Não | Não | Sim | Inteiro | 1 | Cota inicial. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true** e o campo **TipoSelecaoParcela = Parcela**. | | DataCancelamentoContrato | Não | Sim | Sim | Data | Não é necessário informar no XML | Data de cancelamento do contrato. | | DataCancelamentoParcelas | Não | Sim | Sim | Data | Não é necessário informar no XML | Data de cancelamento das parcelas. | | DataFinalParc | Não | Não | Sim | Data | 2018-09-30 | Data final da parcela. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true** e o campo T**ipoSelecaoParcela = Data**. | | DataIngresso | Não | Sim | Sim | Data | Não é necessário informar no XML. | Data de ingresso. | | DataInicialParc | Não | Não | Sim | Data | 2018-09-11 | Data inicial da parcela. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true** e o campo T**ipoSelecaoParcela = Data**. | | DataMatricula | Sim | Não | Não | Data | 2018-09-17 | Data da matrícula. | | DataMatriculaAnterior | Não | Sim | Sim | Data | Não é necessário informar no XML. | Data da matrícula anterior. | | DataMatriculaEncerra | Não | Sim | Sim | Data | Não é necessário informar no XML. | Data de encerramento da matrícula para efeitos do Educacenso. | | DataMatriculaEncerraAnterior | Não | Sim | Sim | Data | Não é necessário informar no XML. | Data anterior de encerramento da matricula para efeitos do Educacenso. | | DataMatriculaEncerraNova | Não | Sim | Sim | Data | Não é necessário informar no XML. | Data nova de encerramento da matricula para efeitos do Educacenso. | | DataMatriculaNova | Não | Sim | Sim | Data | Não é necessário informar no XML. | Data nova de matrícula. | | DiaFixo | Não | Sim | Sim | Enumerado | Não é necessário informar no XML. | Indica se o dia é fixo. | | DiaVencimento | Não | Sim | Sim | Data | Não é necessário informar no XML. | Dia do vencimento. | | Tags do item Disciplinas Esta tag é **obrigatória**. Segue referência de todos os itens. false Para cada disciplina que deseja que o aluno seja matriculado é necessário criar um novo EduMatriculaDiscParams. Itens da tag EduMatriculaDiscParams  | Tag | Obrigatório | Parâmetro  Interno | Aceita  Nulo | Tipo de  Dados | Exemplo | Descrição | | --- | --- | --- | --- | --- | --- | --- | | AlunoRegular | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se o aluno é regular. | | ApagarNumeroDiario | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Apagar número do diário na matrícula da disciplina. | | AtendeuCreditoMinimo | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se atendeu a quantidade de créditos mínimos (utilizado para processo seletivo terceirizado). | | CargaHoraria | Não | Sim | Sim | Decimal | Não é necessário informar no XML. | Carga horária. | | ClientIP | Não | Sim | Sim | String | Não é necessário informar no XML. | Número de IP da máquina onde foi originada a chamada para a matrícula. | | CobPosteriorMatric | Não | Sim | Sim | String | Não é necessário informar no XML. | Cobrança posterior a matrícula. | | CodCampus | Não | Sim | Sim | String | Não é necessário informar no XML. | Código do campus. | | CodColigada | Sim | Não | Não | Inteiro | 1 | Código da coligada. | | CodCurso | Não | Sim | Sim | String | Não é necessário informar no XML. | Código do curso. | | CodDisc | Não | Sim | Sim | String | Não é necessário informar no XML. | Código da disciplina. | | CodFilial | Sim | Não | Não | Inteiro | 1 | Código da filial. | | CodFormula | Sim | Não | Sim | String | Não é necessário informar no XML. | Código da fórmula. | | CodGrade | Sim | Não | Sim | String | Não é necessário informar no XML. | Código da matriz curricular. | | CodHabilitacao | Sim | Não | Sim | String | Não é necessário informar no XML. | Código da habilitação. | | CodMotivo | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Código do motivo. | | CodPerLet | Não | Sim | Sim | String | Não é necessário informar no XML. | Código do período letivo. | | CodSituacaoMatriculaEspera | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Código da situação de matrícula da lista de espera. | | CodStatus | Sim | Não | Não | Inteiro | 13 | Código da situação de matrícula. | | CodStatusNovo | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Código nova da situação de matrícula. | | CodStatusPL | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Código da situação de matrícula do período letivo. | | CodStatusRes | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Código da situação de resultado. | | CodSubturma | Não | Não | Sim | String | A | Código da subturma. | | CodTipoCurso | Sim | Não | Não | Inteiro | 1 | Código do tipo de curso (nível de ensino). | | CodTurma | Não | Sim | Sim | String | TSI-2-032 | Código da turma. | | CodTurno | Não | Sim | Sim | String | Não é necessário informar no XML. | Código do turno. | | CodUsuario | Sim | Não | Não | String | mestre | Código do usuário. | | CoeficienteRendimeto | Não | Sim | Sim | Decimal | Não é necessário informar no XML. | Coeficiente de rendimento. | | DataMatricula | Sim | Não | Não | Data | 2018-09-19 | Data de matrícula. | | DescStatusNovo | Não | Sim | Sim | String | Não é necessário informar no XML. | Descrição da situação de matrícula nova. | | DtAlteracao | Não | Sim | Sim | Data | Não é necessário informar no XML. | Data de alteração. | | EnturmandoTurmaMista | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se está enturmando em turma mista. | | ExcluirMatricula | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é para excluir a matrícula se não tiver vaga e não for colocar na lista de espera | | GerarLogMatricPL | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é para gerar log da matrícula no período letivo. | | IdHabilitacaoFilial | Sim | Não | Não | Inteiro | 4 | Id. da habilitação filial (matriz aplicada). | | IdHabilitacaoFilialOrigem | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Id. origem da habilitação filial (matriz aplicada). | | IdPerLet | Sim | Não | Não | Inteiro | 27 | Id. do período letivo. | | IdTurmaDisc | Sim | Não | Não | Inteiro | 1128 | Id. da turma/disciplina. | | IdTurmaDiscOrigem | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Id. origem da turma/disciplina. | | IdTurmaDiscSubst | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Id. de substituição da turma/disciplina. | | IncluirListaEspera | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é para incluir em lista de espera. | | IsEnturmacao | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se a matrícula está sendo feita pelo processo de enturmação. | | LogExcecoes | Não | Sim | Sim | Objeto | Não é necessário informar no XML. | Log de exceções. | | LogInformacoes | Não | Sim | Sim | Objeto | Não é necessário informar no XML. | Log de informações. | | MatriculaNoUltimoPeriodo | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se o aluno está tentando se matricular no último período de seu curso. | | MatriculaSubstituicaoAtiva | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se a substituição da matrícula será incluída na lista de espera. | | MatriculaViaProcessoSeletivoRM | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica matrícula realizada via Processo Seletivo RM. | | MatriculaViaProcessoSeletivoTerceirizado | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica matrícula realizada via Processo Seletivo Terceirizado. | | MatriculaWeb | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica matrícula realizada via web. | | MatrizAluno | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Id. da habilitação filial (matriz aplicada). | | MediaGlobal | Não | Sim | Sim | Decimal | Não é necessário informar no XML. | Média global. | | MudancaStatus | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é mudança de situação de matrícula. | | MudancaTurma | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se á mudança de turma. | | NomeAluno | Não | Sim | Sim | String | Não é necessário informar no XML. | Nome do aluno | | NomeCampus | Não | Sim | Sim | String | Não é necessário informar no XML. | Nome do campus. | | NomeCurso | Não | Sim | Sim | String | Não é necessário informar no XML. | Nome do curso. | | NomeDisc | Não | Sim | Sim | String | Não é necessário informar no XML. | Nome da disciplina. | | NomeFilial | Não | Sim | Sim | String | Não é necessário informar no XML. | Nome da filial. | | NomeHabilitacao | Não | Sim | Sim | String | Não é necessário informar no XML. | Nome da habilitação. | | NomeMatrizCurricular | Não | Sim | Sim | String | Não é necessário informar no XML. | Nome da matriz curricular. | | NomeTurno | Não | Sim | Sim | String | Não é necessário informar no XML. | Nome do turno. | | NumCreditos | Não | Sim | Sim | Decimal | Não é necessário informar no XML. | Número de créditos. | | NumCreditosCob | Não | Sim | Sim | Decimal | Não é necessário informar no XML. | Número de créditos de cobrança. | | NumDiario | Não | Não | Sim | Inteiro | 1 | Número do diário na matrícula da disciplina. | | NumDiarioAnterior | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Número do diário anterior. | | ObsHistorico | Não | Sim | Sim | String | Não é necessário informar no XML. | Observação do histórico. | | OrdemPriorMatricula | Não | Sim | Sim | String | Não é necessário informar no XML. | Ordem de prioridade de matrícula. | | Origem | Não | Sim | Sim | Enumerado | Não é necessário informar no XML. | Indica se a turma/disciplina teve origem no produto ou na customização. | | ParamDiversos | Não | Sim | Sim | Objeto | Não é necessário informar no XML. | Parâmetros para auxílio na matrícula. | | Periodo | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Código do período da matriz curricular. | | PeriodoDeMatricula | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Indica o período que o aluno está tentando se matricular. | | PermiteAlterarDados | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se permite a alteração dos dados. | | PermiteTransfInternaAlunoInadimplente | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Permite a transferência interna de alunos inadimplentes. | | PodeRodarNumeracaoAutomatica | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Utilizado na enturmação para otimização da movimentação de Enturmação e Desenturmação. | | PossivelFormando | Não | Sim | Sim | Booleano | Não é necessário informar no Não é necessário informar no XML.XML. | Possível Formando. | | ProcessoListaEsperaPrioridade | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é o processo de lista de espera por prioridade. | | ProcurarOutraTurma | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se não tiver vagas, procurar outra turma da mesma disciplina e horário. | | RA | Sim | Não | Não | String | ES-00222 | Registro acadêmico. | | Rematricula | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é rematrícula. | | SalvouMatricula | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se salvou a matrícula. | | TipoDiscGrade | Não | Sim | Sim | Enumerado | Não é necessário informar no XML. | Tipo de disciplina da grade. | | TipoDisciplina | Sim | Não | Não | Enumerado | Normal | Tipo de disciplina. Valores permitidos:   * Normal * Interna * Extra * Dependencia | | TipoMat | Sim | Não | Não | Inteiro | 1 | Tipo de matrícula. | | TransferenciaInterna | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é transferência interna. | | ValidadoTurmaMista | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se foi validado a turma mista. | | ValidarInadimplencia | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se vai validar a inadimplência. | | ValidarIntegracaoBiblioteca | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se vai validar a inadimplência na integração com a biblioteca. | | | | | | | | | DtCompetenciaFinal | Não | Não | Sim | String | 03/2018 | Data de competência final. | | DtCompetenciaInicial | Não | Não | Sim | String | 01/2018 | Data de competência inicial. | | DtMatriculaPag | Não | Sim | Sim | Data | Não é necessário informar no XML. | Data de pagamento da matrícula. | | DtResultado | Não | Sim | Sim | Data | Não é necessário informar no XML. | Data do resultado da matrícula. | | DtSolicitacaoAlteracao | Não | Sim | Sim | Data | Não é necessário informar no XML. | Data da solicitação de alteração. | | EmTransacao | Não | Sim | Sim | Booleano | EmTransacao | Indica o status da transação. | | GerarLancamento | Não | Não | Sim | Booleano | false | Indica se é para gerar lançamento. Somente irá gerar lançamento se a situação de matrícula exigir contrato financeiro e o obedecer os critérios abaixo:   * Preencher o campo **CodPlanoPgto;** * Preencher o campo **TipoSelecaoParcela**, ver valores permitidos pertinentes a este campo. | | GerarLog | Não | Não | Sim | Booleano | true | Indica se é para gerar log ao matricular aluno. | | GerouContratoComPlano | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se gerou contrato com plano de pagamento. | | IDPS | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Id. do processo seletivo. | | IdHabilitacaoFilial | Sim | Não | Não | Inteiro | 4 | Id. da habilitação filial (matriz aplicada). | | IdHabilitacaoFilialOrigem | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Id. origem da habilitação filial (matriz aplicada). | | IdPerLet | Sim | Não | Não | Inteiro | 27 | Id. do período letivo. | | IdRelatBoleto | Não | Não | Sim | Inteiro | 1 | Id. do relatório do boleto. Para o seu preenchimento a situação de matrícula tem que exigir contrato financeiro e o campo **ColigadaRelatBoleto** deverá estar preenchido. | | IdRelatContrato | Não | Não | Sim | Inteiro | 1 | Id. do relatório do contrato. Para o seu preenchimento a situação de matrícula tem que exigir contrato financeiro e o campo **ColigadaRelatContrato** deverá estar preenchido. | | Identificador | Não | Sim | Sim | String | Não é necessário informar no XML. | Identificador. | | IsDesenturmacao | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é desenturmação. | | IsEnturmacao | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é enturmação. | | IsRematricula | Sim | Sim | Não | Booleano | false | Indica se é rematrícula. Sempre informar **false**. | | LogContrato | Não | Sim | Sim | Objeto | Não é necessário informar no XML. | Log referênte a informações impactam no cancelamento  do contrato. | | LogExcecoes | Não | Sim | Sim | Objeto | Não é necessário informar no XML. | Log de exceções. | | MatriculaWeb | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é matrícula web. | | MudancaStatus | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é mudança de situação de matrícula. | | MudancaTurma | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é mudança de turma. | | NomeAluno | Não | Sim | Sim | String | Não é necessário informar no XML. | Nome do aluno. | | NumCarteira | Não | Não | Sim | String | 10 | Número da carteirinha. Campo exclusivo para o **Ensino Básico**. | | NumeroInscricao | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Número de inscrição. | | OrigemParcela | Não | Sim | Sim | Enumerado | Não é necessário informar no XML. | Origem da parcela. | | ParametrosDiversos | Não | Sim | Sim | Objeto | Não é necessário informar no XML. | Parâmetros para auxílio na matrícula. | | ParcelaFinal | Não | Não | Sim | Inteiro | 1 | DataInicialParc | | ParcelaInicial | Não | Não | Sim | Inteiro | 1 | Parcela inicial. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true** e o campo **TipoSelecaoParcela = Parcela**. | | Periodo | Não | Não | Sim | Inteiro | 1 | Código do período da matriz curricular. | | PermiteTransfInternaAlunoInadimplente | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se permite a transferência interna do aluno inadimplente. | | PodeRodarNumeracaoAutomatica | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Utilizado na enturmação para otimização da movimentação de Enturmação e Desenturmação. | | RA | Sim | Não | Não | String | ES-00222 | Registro acadêmico (RA) do aluno. | | RematriculaEBasicoAjusteContratoHabFilial | Não | Sim | Sim | Booleano | PermiteTransfInternaAlunoInadimplente | Indica se estamos ajustando SCONTRATO.IDHABILITACAOFILIAL na rematrícula do nível de ensino Básico. | | Tags do item ResponsaveisFinanceirosContrato Esta tag não é obrigatória. Segue referência de todos os itens. false Para cada responsável financeiro que deseja inserir é necessário criar um novo EduResponsavelContratoItem. Itens da tag EduResponsavelContratoItem  | Tag | Obrigatório | Parâmetro  Interno | Aceita  Nulo | Tipo de  Dados | Exemplo | Descrição | | --- | --- | --- | --- | --- | --- | --- | | InternalId | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | InternalId. | | CodCfo | Sim | Não | Não | String | C01455 | Código do cliente. | | CodColCfo | Sim | Não | Não | Inteiro | 1 | Código da coligada do cliente. | | CodColigada | Sim | Não | Não | Inteiro | 1 | Código da coligada. | | CodContrato | Não | Sim | Sim | String | Não é necessário informar no XML. | Código do contrato. | | IdPeriodoLetivo | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Id. do período letivo. | | Nome | Não | Sim | Sim | String | Não é necessário informar no XML. | Nome do cliente. | | Percentual | Sim | Não | Não | Inteiro | Double | Percentual. | | RegistroAcademico | Não | Sim | Sim | String | Não é necessário informar no XML. | Registro acadêmico. | | ResponsavelMovimento | Não | Não | Não | Enumerado | Nao | Indica se o responsável também é responsável pelo movimento.  Valores permitidos: **Sim** ou **Nao.** |  falseExemplo do item EduResponsavelContratoItemxml   C01455 1 1  0 Felipe Paulo Novaes 100  Nao ]]> | | | | | | | |  |  |  |  |  |  |  | | TipoOperacao | Não | Sim | Sim | Enumerado | Não é necessário informar no XML. | Tipo de operação (Inclusão, Alteração e Exclusão). | | TipoSelecaoParcela | Não | Não | Sim | Enumerado | Parcela | Tipo de seleção de parcela. Somente preencher se o campo **GerarLancamento = true**. Valores permitidos:   * **Parcela** * **Data** | | TransferenciaInterna | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é transferência interna. | | TurnosDiferentes | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica que está havendo uma alteração de turno na mudança de turma. | | UsarPlanoPgtoParametrizacaoCurso |  |  |  |  |  |  | | ValidarInadimplenciaBiblioteca | Não | Sim | Sim | Booleano | Não é necessário informar no XML. | Indica se é para validar a inadimplência do aluno na biblioteca. | | ViaCarteira | Não | Não | Sim | String | Primeira | Via da carteirinha. Campo exclusivo para o **Ensino Básico**. | | grupoRelat | Não | Sim | Sim | Inteiro | Não é necessário informar no XML. | Grupo de relatório. | | | | | | | |
| MatricularDisc | Sim | Não | Não | Enumerado | Sim | Indica matrícula em disciplina. Sempre informar **Sim**. |

Importante

* As tags que não são obrigatórias e/ou que aceitam nulo o recomendado é **não** informar elas no XML.

Para efetuar matrícula apenas no período letivo ou no período letivo junto com as disciplinas consulte o seguinte documento: <http://tdn.totvs.com/x/kZSaFQ>
