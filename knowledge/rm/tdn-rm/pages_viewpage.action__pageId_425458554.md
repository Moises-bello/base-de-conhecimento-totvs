---
content_hash: d69dcc141e08f799de958a8b19274711c617e70569bd1de93f89d76d0effec5e
fetched_at: '2026-06-29T00:09:30.895424+00:00'
page_id: '425458554'
product: rm
source: tdn-rm
title: Fórmulas Visuais - Educacionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458554
version: 21
---

Fórmula Visual: Matrícula

# Fórmulas Visuais da Matrícula

Recurso para associação de fórmula visual nos principais processos da matrícula.

Ao criar uma fórmula visual para estes gatilhos os parâmetros são obtidos a partir da atividade **RMSWorkflow** raiz.

Atenção

No processo de matrícula feito através do Portal, as fórmula visuais configuradas para os eventos  "Após execução" ou "Após cadastrar" das seguintes ações:

* "Matricular aluno em um período letivo",
* "Alterar a situação do aluno no período letivo",
* "Matricular aluno em uma disciplina",
* "Alterar a situação do aluno na disciplina",
* "Alterar a situação do aluno em um curso",
* e "Cadastrar contrato matrícula;

não devem ser utilizada em situações que consideram que a ação foi concluída efetivamente, pois no momento em que a fórmula é executada nesse processo, as transações ainda estão pendentes de serem persistidas no banco de dados, podendo ser confirmadas ou não de acordo com as ações seguintes do processo.

## 1. Matricular aluno em um período letivo

### Gatilhos

* Antes da execução
* Após a execução

### Parâmetros

| Parâmetro | Descrição | Tipo |
| --- | --- | --- |
| CodColigada | Código da Coligada | int |
| CodContrato | Código do Contrato | string |
| CodFilial | Código da Filial | int |
| CodMotivo | Código do Motivo | int? |
| CodPlanoPgto | Código do Plano de Pagamento | string |
| CodStatus | Código do Stauts | int |
| CodStatusNovo | Código do Stauts Novo | int? |
| CodStatusPendenteDisc | Código do Status Pendente da Disciplina | int? |
| CodStatusPendentePL | Código do Status Pendente do Período Letivo | int? |
| CodTipoCurso | Código do Nível de Ensino | int |
| CodTipoMat | Código do Tipo de Matrícula | int? |
| CodTurma | Código da Turma | string |
| CodUsuario | Código do Usuário | string |
| CopiarRespFinanceiroContrato | Copiar Responsável Financeiro do Contrato? | bool |
| CotaFinal | Cota Final | int? |
| CotaInicial | Cota Inicial | int? |
| DataFinalParc | Data Final da Parcela | DateTime? |
| DataInicialParc | Data Inicial da Parcela | DateTime? |
| DataMatricula | Data da Matrícula | DateTime |
| DtCompetenciaFinal | Data de Competência Final | string |
| DtCompetenciaFinalMov | Data de Competência Final do Movimento | string |
| DtCompetenciaInicial | Data de Competência Inicial | string |
| DtCompetenciaInicialMov | Data de Competência Inicial do Movimento | string |
| GerarLancamento | Gera Lançamento? (Sim/Nao) | string |
| IdHabilitacaoFilial | Identificador da Habilitação da Filial | int |
| IdPerLet | Identificador do Período Letivo | int |
| MatriculaWeb | Matrícula da Web? | bool |
| ParcelaFinal | Parcela Final | int? |
| ParcelaInicial | Parcela Inicial | int? |
| Periodo | Período | int? |
| RA | Registro Acadêmico | string |

## 2. Matricular aluno em uma disciplina

### Gatilhos

* Antes da execução
* Após a execução

### Parâmetros

| Parâmetro | Descrição | Tipo |
| --- | --- | --- |
| CodColigada | Código da Coligada | int |
| CodCurso | Código do Curso | string |
| CodDisc | Código da Disciplina | string |
| CodFilial | Código da Filial | int |
| CodGrade | Código da Grade | string |
| CodHabilitacao | Código da Habilitação | string |
| CodItinerarioFormativo | Código do Itinerário Formativo | int? |
| CodMotivo | Código do Motivo | int? |
| CodPerLet | Código do Período Letivo | string |
| CodSituacaoMatriculaEspera | Código da Situação de Matrícula em Espera | int |
| CodStatus | Código do Status | int |
| CodStatusNovo | Código do Status Novo | int? |
| CodStatusPL | Código do Status do Período Letivo | int |
| CodSubturma | Código da Subturma | string |
| CodTipoCurso | Código do Tipo de Curso | int |
| CodTurma | Código da Turma | string |
| CodTurno | Código do Turno | int |
| CodUsuario | Código do Usuário | string |
| DataMatricula | Data de Matrícula | DateTime |
| IdHabilitacaoFilial | Identificador da Habilitação da Filial | int? |
| IdPerLet | Identificador do Período Letivo | int |
| IdTurmaDisc | Identificador da Turma/Disciplina | int |
| IdTurmaDiscOrigem | Identificador da Turma/Disciplina Origem | int? |
| IdTurmaDiscPrincipal | Identificador da Turma/Disciplina Principal | int? |
| MatriculaWeb | Matrícula na Web? | bool |
| Periodo | Período | int |
| RA | Registro Acadêmico | string |
| TipoDiscGrade | Tipo de Disciplina da Grade (Default/Obrigatoria/Optativa/Eletiva) | string |
| TipoDisciplina | Tipo de Disciplina (Normal/Interna/Extra/Dependencia/ItinerarioFormativo) | string |
| TipoMat | Tipo de Matrícula | int? |

## 3. Alterar a situação do aluno no período letivo

### Gatilhos

* Antes da execução
* Após a execução

### Parâmetros

| Parâmetro | Descrição | Tipo |
| --- | --- | --- |
| CodColigada | Código da Coligada | int |
| CodContrato | Código do Contrato | string |
| CodFilial | Código da Filial | int |
| CodMotivo | Código do Motivo | int? |
| CodPlanoPgto | Código do Plano de Pagamento | string |
| CodStatus | Código do Status | int |
| CodStatusNovo | Código do Status Novo | int? |
| CodTipoCurso | Código do Nível de Ensino | int |
| CodTipoMat | Código do Tipo de Matrícula | int? |
| CodTurma | Código da Turma | string |
| CodUsuario | Código do Usuário | string |
| DataMatricula | Data da Matrícula | DateTime |
| IdHabilitacaoFilial | Identificador da Habilitação da Filial | int |
| IdPerLet | Identificador do Período Letivo | int |
| MatriculaWeb | Matrícula na Web? | bool |
| Periodo | Período | int? |
| RA | Registro Acadêmico | string |

## 4. Alterar a situação do aluno na disciplina

### Gatilhos

* Antes da execução
* Após a execução

### Parâmetros

| Parâmetro | Descrição | Tipo |
| --- | --- | --- |
| CodColigada | Código da Coligada | int |
| CodCurso | Código do Curso | string |
| CodDisc | Código da Disciplina | string |
| CodFilial | Código da Filial | int |
| CodGrade | Código da Grade | string |
| CodHabilitacao | Código da Habilitação | string |
| CodItinerarioFormativo | Código do Itinerário Formativo | int? |
| CodMotivo | Código do Motivo | int? |
| CodPerLet | Código do Período Letivo | string |
| CodStatus | Código do Satatus | int |
| CodStatusNovo | Código do Status Novo | int? |
| CodStatusPL | Código do Status do Período Letivo | int |
| CodSubturma | Código da Subturma | string |
| CodTipoCurso | Código do Nível de Ensino | int |
| CodTurma | Código da Turma | string |
| CodTurno | Código do Turno | int |
| CodUsuario | Código do Usuário | string |
| DataMatricula | Data da Matrícula | DateTime |
| IdHabilitacaoFilial | Identificador da Habilitação da Filial | int? |
| IdPerLet | Identificador do Período Letivo | int |
| IdTurmaDisc | Identificador da Turma/Disciplina | int |
| IdTurmaDiscOrigem | Identificador da Turma/Disciplina Origem | int? |
| IdTurmaDiscPrincipal | Identificador da Turma/Disciplina Principal | int? |
| MatriculaWeb | Matrícula na Web? | bool |
| RA | Registro Acadêmico | string |
| TipoDiscGrade | Tipo de Disciplina da Grade (Default/Obrigatoria/Optativa/Eletiva) | string |
| TipoDisciplina | Tipo de Disciplina (Normal/Interna/Extra/Dependencia/ItinerarioFormativo) | string |
| TipoMat | Tipo de Matrícula | int? |

## 5. Selecionar disciplinas na matrícula online

### Gatilhos

* Após a execução

### Parâmetros

| Parâmetro | Descrição | Tipo |
| --- | --- | --- |
| CodColigada | Código da Coligada | int |
| CodCurso | Código do Curso | string |
| CodDisc | Código da Disciplina | string |
| CodFilial | Código da Filial | int |
| CodGrade | Código da Grade | string |
| CodHabilitacao | Código da Habilitação | string |
| CodItinerarioFormativo | Código do Itinerário Formativo | int? |
| CodMotivo | Código do Motivo | int? |
| CodStatus | Código do Status | int |
| CodStatusNovo | Código do Status Novo | int? |
| CodStatusPL | Código do Status do Período Letivo | int |
| CodSubturma | Código da Subturma | string |
| CodTipoCurso | Código do Nível de Ensino | int |
| CodTurma | Código da Turma | string |
| CodTurno | Código do Turno | int |
| CodUsuario | Código do Usuário | string |
| DataMatricula | Data da Matrícula | DateTime |
| IdHabilitacaoFilial | Identificador da Habilitação | int? |
| IdPerLet | Identificador do Período Letivo | int |
| IdTurmaDisc | Identificador da Turma/Disciplina | int |
| IdTurmaDiscOrigem | Identificador da Turma/Disciplina Origem | int? |
| IdTurmaDiscPrincipal | Identificador da Turma/Disciplina Principal | int? |
| MatriculaWeb | Matrícula na Web? | bool |
| RA | Registro Acadêmico | string |
| TipoDiscGrade | Tipo de Disciplina da Grade (Default/Obrigatoria/Optativa/Eletiva) | string |
| TipoDisciplina | Tipo de Disciplina (Normal/Interna/Extra/Dependencia/ItinerarioFormativo) | string |
| TipoMat | Tipo de Matrícula | int? |

## 6. Alterar a situação do aluno em um curso

### Gatilhos

* Antes da execução
* Após a execução

### Parâmetros

| Parâmetro | Descrição | Tipo |
| --- | --- | --- |
| CodCampus | Código do Campus | string |
| CodColigada | Código da Coligada | int |
| CodCurso | Código do Curso | string |
| CodGrade | Código da Grade | string |
| CodHabilitacao | Código da Habilitação | string |
| CodInst | Código da Instituição da Transferência | int? |
| CodInstDiploma | Código da Insituição do Diploma | int? |
| CodStatusCurso | Código do Status do Curso | int? |
| CodTipoCurso | Código do Nível de Ensino | int |
| CodTipoIngresso | Código do Tipo de Ingresso | int? |
| CodUsuario | Código do Usuário | string |
| DataColacaoGrau | Data da Colação de Grau | DateTime? |
| DataConclusaoCurso | Data da Conclusão do Curso | DateTime? |
| DataEmissaoDiploma | Data da Emissão do Diploma | DateTime? |
| DataIngresso | Data de Ingresso | DateTime? |
| DataProcSel | Data do Processo Seletivo | DateTime? |
| DataProvao | Data do Provão | DateTime? |
| DataRegistroDiploma | Data do Registro do Diploma | DateTime? |
| DesabilitaIntegralizacaoCurso | Desabilita Integralização do Curso? | string |
| IdHabilitacaoFilial | Identificador da Habilitação da Filial | int |
| MediaGlobal | Média Global | decimal |
| MediaVestibular | Média Vestibular | decimal? |
| Observacao | Observação | string |
| PaginaRegistro | Página do Registro | string |
| PontosVestibular | Pontos Vestibular | string |
| RA | Registro Acadêmico | string |

## 7. Cadastrar contrato na matrícula

### Gatilhos

* Antes da execução
* Após a execução

### Parâmetros

| Parâmetro | Descrição | Tipo |
| --- | --- | --- |
| CodColigada | Código da Coligada | int |
| CodContrato | Código do Contrato | string |
| CodFilial | Código da Filial | int |
| CodPlanoPgto | Código do Plano de Pagamento | string |
| CodStatus | Código do Status | int |
| CodTipoCurso | Código do Nível de Ensino | int |
| CodTipoMat | Código do Tipo de Matrícula | int? |
| CodTurma | Código da Turma | string |
| CodUsuario | Código do Usuário | string |
| CopiarRespFinanceiroContrato | Copiar Responsável Financeiro do Contrato? | bool |
| CotaFinal | Cota Final | int? |
| CotaInicial | Cota Inicial | int? |
| DataFinalParc | Data Final da Parcela | DateTime? |
| DataInicialParc | Data Inicial da Parcela | DateTime? |
| DataMatricula | Data da Matrícula | DateTime |
| DtCompetenciaFinal | Data da Competência Final | string |
| DtCompetenciaFinalMov | Data da Competência Final da Movimentação | string |
| DtCompetenciaInicial | Data da Competência Inicial | string |
| DtCompetenciaInicialMov | Data da Competência Inicial da Movimentação | string |
| GerarLancamento | Gera Lançamento? (Sim/Nao) | string |
| IdHabilitacaoFilial | Identificador da Habilitação da Filial | int |
| IdPerLet | Identificador do Período Letivo | int |
| MatriculaWeb | Matrícula na Web? | bool |
| ParcelaFinal | Parcela Final | int? |
| ParcelaInicial | Parcela Inicial | int? |
| RA | Registro Acadêmico | string |

A funcionalidade foi criada com o objetivo de facilitar a criação e a associação das Fórmulas Visuais aumentando a interação do usuário com o sistema.  
O processo de associação das Fórmulas Visuais na parametrização da Matrícula contemplará apenas a estrutura do Winform; será permitido associar apenas uma Fórmula Visual por gatilho.

Fórmula Visual: Cadastra Frequência

Essa fórmula está disponível em: **Gestão educacional | gestão | Ferramentas de Análise | Fórmula Visual | 'Atividades' - Educacional | Cadastra Frequência**

Essa Atividade tem como objetivo, executar através da fórmula, a inclusão da frequência diária para o Aluno.

Nela, a Instituição de ensino poderá informar os parâmetros:

* CodColigada
* Data (data da Aula)
* IdHorarioTurma
* IdTurmaDisc
* RegistroAcademico
* TipoFrequencia
* AuldasDadas
* CodEtapa

Atividade: CodSubTurma

O parêmtro: *CodSubTurma* está disponível a a partir do partch: 12.1.2410.230

* IdJustificativa
* Justificada

Veja Também

---

[Boletim Técnico - EDU\_BT\_EntryPoints\_Matrícula](http://tdn.totvs.com/pages/viewpage.action?pageId=161349689)
