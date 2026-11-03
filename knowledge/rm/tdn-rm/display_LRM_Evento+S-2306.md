---
content_hash: 81b7e0b1c41bb04cc2af97e8484e81fa87865d352bea12b05867c56bc8c47f9a
fetched_at: '2026-06-29T00:08:56.318448+00:00'
page_id: '351376478'
product: rm
source: tdn-rm
title: Evento S-2306
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2306
version: 14
---

Leiautestrue2Leiaute S-1.0Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do cálculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideTrabSemVinculo | cpfTrab |  |  |  |
| ideTrabSemVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| ideTrabSemVinculo | codCateg |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'CODCATEGORIAESOCIAL' da tabela 'FCFO';    Caso seja autônomo Externo retorna o campo 'CATEGORIAESOCIAL' da tabela 'PPAGTOAUTONOMOEXT'. Não tendo informação ou sendo zero será o de/para  do campo 'CATAUTONOMO' da tabela  'PPAGTOAUTONOMOEX' que armazena a categoria do SEFIP e faz o de/Para para categoria do eSocial.;    O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
| infoTSVAlteracao | dtAlteracao |  | DATAEVENTO | Se o campo alterado possuir histórico busca a data de mudança do histórico, caso contrário é gerado conforme data atual |
| infoTSVAlteracao | natAtividade |  |  | Caso PFUNC.ESOCIALNATATIVIDADE seja "2" retorna "2 - Trabalho Rural" caso contrário, retorna "1 - Trabalho Urbano" |
| cargoFuncao | nmCargo |  |  | Recupera o valor do campo PFUNCAO.NOME. |
| cargoFuncao | CBOCargo |  |  | Recupera o valor do campo PFUNCAO.CBO2002. |
| cargoFuncao | nmFuncao |  |  | Recupera o valor do campo PFUNCAO.NOME de acordo com o valor de PFUNC.CODFUNCAOCONF. |
| cargoFuncao | CBOFuncao |  |  | Recupera o valor do campo PFUNCAO.CBO2002 de acordo com o valor de PFUNC.CODFUNCAOCONF. |
| remuneracao | vrSalFx |  |  | Caso o funcionário utilize salário composto, retorna a soma que compõe o total do salário do histórico salarial. Para mais informações, acesse o link  [DT - S-2206 e S-2306 - Geração da tag <vrSalFx>](https://tdn.totvs.com/pages/viewpage.action?pageId=838954096).  Caso o parametro "Considerar maior valor de salário-hora na tag vrSalFx para professores/horistas" esteja marcado, retorna o maior salário hora cadastrado conforme data do histórico salarial.  Caso contrário, retorna o salário do histórico salarial |
| remuneracao | undSalFixo |  |  | Se PFUNC.CODTIPO for igual a "O" ou "F" retorna "7 - Não se aplica", caso contrário será verificado o tipo de recebimento conforme a serguir:   Caso PFUNC.CODRECEBIMENTO seja "D - Diarista" retorna "2 - Por Dia";  Caso PFUNC.CODRECEBIMENTO seja "H - Horista" ou "P - Professor Horista" retorna "1 - Por Hora";  Caso PFUNC.CODRECEBIMENTO seja "M - Mensalista" ou "O - Outros" retorna "5 - Por Mês";  Caso PFUNC.CODRECEBIMENTO seja "Q - Quinzenalista" retorna "4 - Por Quinzena";  Caso PFUNC.CODRECEBIMENTO seja "S - Semanalista" retorna "3 - Por Semana";  Caso PFUNC.CODRECEBIMENTO seja "T - Tarefeiro" retorna "6 - Por Tarefa"; |
| remuneracao | dscSalVar |  |  | Recupera valor do campo PFUNC.DESCRICAOSALVARIAVEL |
| infoDirigenteSindical | tpRegPrev | PFUNC | TIPOREGPREVDIRIGENTESINDICAL |  |
| infoTrabCedido | tpRegPrev | PFUNC | TIPOREGIMEPREVIDENCIARIOCEDIDO |  |
| infoEstagiario | natEstagio | PFUNC | NATUREZAESTAGIO |  |
| infoEstagiario | nivEstagio | PFUNC | CODNIVELESTAGIO |  |
| infoEstagiario | areaAtuacao | PFUNC | AREAATUACAOESTAGIO |  |
| infoEstagiario | nrApol | PFUNC | NUMEROAPOLICEESTAGIO |  |
| infoEstagiario | dtPrevTerm | PFUNC | DTPREVTERMINOESTAGIO |  |
| instEnsino | cnpjInstEnsino | VENTIDADES | CGCCPF |  |
| instEnsino | nmRazao | VENTIDADES | RAZAOSOCIAL |  |
| instEnsino | dscLograd | VENTIDADES | LOGRADOURO |  |
| instEnsino | nrLograd | VENTIDADES | NUMERO |  |
| instEnsino | bairro | VENTIDADES | BAIRRO |  |
| instEnsino | cep | VENTIDADES | CEP |  |
| instEnsino | codMunic |  |  | Código recuperado através dos campos VENTIDADES.ESTADO e VENTIDADES.LOCALIDADE |
| instEnsino | uf | VENTIDADES | ESTADO |  |
| ageIntegracao | cnpjAgntInteg | VENTIDADES | CGCCPF |  |
| supervisorEstagio | cpfSupervisor | PFUNC | CPFCOORDENADORESTAGIO |  |

true2Leiaute S-1.2Leiaute S-1.2

Mapeamento dos campos para o leiaute S-1.2

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do cálculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideTrabSemVinculo | cpfTrab |  |  |  |
| ideTrabSemVinculo | codCateg |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'CODCATEGORIAESOCIAL' da tabela 'FCFO';    Caso seja autônomo Externo retorna o campo 'CATEGORIAESOCIAL' da tabela 'PPAGTOAUTONOMOEXT'. Não tendo informação ou sendo zero será o de/para  do campo 'CATAUTONOMO' da tabela  'PPAGTOAUTONOMOEX' que armazena a categoria do SEFIP e faz o de/Para para categoria do eSocial.;    O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
| infoTSVAlteracao | dtAlteracao |  | DATAEVENTO | Se o campo alterado possuir histórico busca a data de mudança do histórico, caso contrário é gerado conforme data atual |
| infoTSVAlteracao | natAtividade |  |  | Caso PFUNC.ESOCIALNATATIVIDADE seja "2" retorna "2 - Trabalho Rural" caso contrário, retorna "1 - Trabalho Urbano" |
| cargoFuncao | nmCargo |  |  | Recupera o valor do campo PFUNCAO.NOME. |
| cargoFuncao | CBOCargo |  |  | Recupera o valor do campo PFUNCAO.CBO2002. |
| cargoFuncao | nmFuncao |  |  | Recupera o valor do campo PFUNCAO.NOME de acordo com o valor de PFUNC.CODFUNCAOCONF. |
| cargoFuncao | CBOFuncao |  |  | Recupera o valor do campo PFUNCAO.CBO2002 de acordo com o valor de PFUNC.CODFUNCAOCONF. |
| remuneracao | vrSalFx |  |  | Caso o funcionário utilize salário composto, retorna a soma que compõe o total do salário do histórico salarial. Para mais informações, acesse o link  [DT - S-2206 e S-2306 - Geração da tag <vrSalFx>](https://tdn.totvs.com/pages/viewpage.action?pageId=838954096).  Caso o parametro "Considerar maior valor de salário-hora na tag vrSalFx para professores/horistas" esteja marcado, retorna o maior salário hora cadastrado conforme data do histórico salarial.  Caso contrário, retorna o salário do histórico salarial |
| remuneracao | undSalFixo |  |  | Se PFUNC.CODTIPO for igual a "O" ou "F" retorna "7 - Não se aplica", caso contrário será verificado o tipo de recebimento conforme a serguir:   Caso PFUNC.CODRECEBIMENTO seja "D - Diarista" retorna "2 - Por Dia";  Caso PFUNC.CODRECEBIMENTO seja "H - Horista" ou "P - Professor Horista" retorna "1 - Por Hora";  Caso PFUNC.CODRECEBIMENTO seja "M - Mensalista" ou "O - Outros" retorna "5 - Por Mês";  Caso PFUNC.CODRECEBIMENTO seja "Q - Quinzenalista" retorna "4 - Por Quinzena";  Caso PFUNC.CODRECEBIMENTO seja "S - Semanalista" retorna "3 - Por Semana";  Caso PFUNC.CODRECEBIMENTO seja "T - Tarefeiro" retorna "6 - Por Tarefa"; |
| remuneracao | dscSalVar |  |  | Recupera valor do campo PFUNC.DESCRICAOSALVARIAVEL |
| infoDirigenteSindical | tpRegPrev | PFUNC | TIPOREGPREVDIRIGENTESINDICAL |  |
| infoTrabCedido | tpRegPrev | PFUNC | TIPOREGIMEPREVIDENCIARIOCEDIDO |  |
| infoMandElet | indRemunCargo |  |  | Recupera o valor do campo PFUNC.INDICATIVOREMUNERACAOCARGO |
| infoMandElet | tpRegPrev |  |  |  |
| infoEstagiario | natEstagio | PFUNC | NATUREZAESTAGIO |  |
| infoEstagiario | nivEstagio | PFUNC | CODNIVELESTAGIO |  |
| infoEstagiario | areaAtuacao | PFUNC | AREAATUACAOESTAGIO |  |
| infoEstagiario | nrApol | PFUNC | NUMEROAPOLICEESTAGIO |  |
| infoEstagiario | dtPrevTerm | PFUNC | DTPREVTERMINOESTAGIO |  |
| instEnsino | cnpjInstEnsino |  |  |  |
| instEnsino | nmRazao | VENTIDADES | RAZAOSOCIAL |  |
| instEnsino | dscLograd | VENTIDADES | LOGRADOURO |  |
| instEnsino | nrLograd | VENTIDADES | NUMERO |  |
| instEnsino | bairro | VENTIDADES | BAIRRO |  |
| instEnsino | cep | VENTIDADES | CEP |  |
| instEnsino | codMunic |  |  | Código recuperado através dos campos VENTIDADES.ESTADO e VENTIDADES.LOCALIDADE |
| instEnsino | uf | VENTIDADES | ESTADO |  |
| ageIntegracao | cnpjAgntInteg | VENTIDADES | CGCCPF |  |
| supervisorEstagio | cpfSupervisor | PFUNC | CPFCOORDENADORESTAGIO |  |
| localTrabGeral | tpInsc |  |  | Caso o parâmetro "Considera CNO nas tags localTrabGeral do S-1005 para funcionários alocados em um único tomador obra própria"  esteja marcado e o funcionário possua somente um tomador de serviço que seja obra própria retorna "4 - CNO";   Caso PSECAO.CAEPF esteja preenchido retorna "3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ". |
| localTrabGeral | nrInsc |  |  | Caso tpInsc seja 1: retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 3: retorna valor do campo PSECAO.CAEPF;  Caso tpInsc seja 4: retorna valor do campo FCFOCEI.CEI. |
| localTempDom | tpLograd |  |  |  |
| localTempDom | dscLograd | PSECAO | RUA |  |
| localTempDom | nrLograd | PSECAO | NUMERO |  |
| localTempDom | complemento | PSECAO | COMPLEMENTO |  |
| localTempDom | bairro | PSECAO | BAIRRO |  |
| localTempDom | cep | PSECAO | CEP |  |
| localTempDom | codMunic |  |  |  |
| localTempDom | uf | PSECAO | ESTADO |  |
| horContratual | qtdHrsSem |  |  | Média de horas semanais, considerando uma projeção de 7 dias.  Regra do cálculo:   Caso parâmetro para considerar jornada do funcionário esteja marcado no parametrizador do eSocial: jornada mensal / 4   Demais cenários: soma das horas das jornadas de trabalho do horário, dividido pelos dias do horário (todos os índices, inclusive dias de descanso), multiplicado por 7 (fixo).  É importante observar que, para cada hora de adicional noturno, será aplicado no cálculo um percentual de 14,29% da Nona Hora.   Certifique-se de considerar esta observação ao realizar os cálculos. |
| horContratual | tpJornada |  |  | Código recuperado através do campo AHORARIO.TIPOJORESOCIAL |
| horContratual | tmpParc | PFUNC | TEMPOPARCIAL |  |
| horContratual | horNoturno |  |  | Caso a jornada semanal contratual do funcionário possua horário noturno (no todo ou em parte), retorna S - Sim. Caso contrário, retorna N - Não. |
| horContratual | dscJorn |  |  | Caso o parâmetro "Considerar descrição do horário na tag dscJorn dos eventos S-2200 e S-2206" esteja marcado, retorna o valor do campo AHORARIO.DESCRICAO.  Caso contrário, retorna a descrição da jornada semanal contratual, contendo os dias da semana e os respectivos horários contratuais (entrada, saída e  intervalos) |
| alvaraJudicial | nrProcJud | PFUNC | NRPROCJUD |  |
| observacoes | observacao |  |  | Informação obtida a partir dos registros da tabela PFUNCOBSERVACAO campo OBSERVACAO nos anexos do funcionário. |
| treiCap | codTreiCap | VCURSOS | CODTREINAMENTOESOCIAL |  |
