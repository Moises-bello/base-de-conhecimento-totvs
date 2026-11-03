---
content_hash: cc6af16b95a9ca8c149e53e35788da0b539467091ef24d0bb3b53df68860f3fb
fetched_at: '2026-06-29T00:08:56.206555+00:00'
page_id: '351376279'
product: rm
source: tdn-rm
title: Evento S-2206
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2206
version: 44
---

Leiautestrue1Leiaute S-1.3

Mapeamento dos campos para o leiaute S-1.3

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro\_eSocial** | **Campo\_eSocial** | **Tabela\_RM** | **Coluna\_RM** | **Informações\_do\_calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideVinculo | cpfTrab |  |  |  |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| altContratual | dtAlteracao |  | DATAEVENTO | Se o campo alterado possuir histórico busca a data de mudança do histórico, caso contrário é gerado conforme data atual.  Para alteração salarial por dissídio busca o campo "Data de Inclusão". |
| altContratual | dtEf |  | DATAEFETIVA | Para alteração salarial busca o campo "Data da Mudança" do Histórico Salarial. |
| vinculo | tpRegPrev | PFUNC | TPREGIMEPREV |  |
| infoCeletista | tpRegJor |  |  | Recupera valor do campo PFUNC.TIPOREGIMEJORNADA |
| infoCeletista | natAtividade |  |  | Caso PFUNC.ESOCIALNATATIVIDADE seja "2" retorna "2 - Trabalho Rural" caso contrário, retorna "1 - Trabalho Urbano" |
| infoCeletista | dtBase |  |  | Caso PSINDIC.MESDATABASE seja maior que "0" retorna o valor dessa coluna, caso contrário recupera o mês do campo PSINDIC.DATABASECORRSALARIAL |
| infoCeletista | cnpjSindCategProf | PSINDIC | CNPJ |  |
| trabTemporario | justProrr | PFUNC | JUSTIFICATIVAPRORROGTEMP |  |
| aprend | indAprend |  |  | Recupera o valor do campo PFUNC.MODALIDADECONTRATACAO. |
| aprend | cnpjEntQual |  |  | Caso indAprend seja 1: retorna valor do campo PFUNC.CNPJEMPRESACONTRATANTEAPRENDIZ. |
| aprend | tpInsc |  |  |  |
| aprend | nrInsc |  |  | Caso indAprend seja 2: retorna valor do campo PFUNC.CNPJEMPRESACONTRATANTEAPRENDIZ. |
| aprend | cnpjPrat |  |  | Recupera o valor do campo PFUNC.INSCESTABELECIMENTOATIVPRATICAS. |
| infoEstatutario | tpPlanRP |  |  | Recupera o valor do campo PFUNC.TIPOPLANOSEGREGACAOMASSA |
| infoEstatutario | indTetoRGPS |  |  | Recupera o valor do campo PFUNC.TETORGPS |
| infoEstatutario | indAbonoPerm |  |  | Recupera o valor do campo PFUNC.ABONOPERMANENCIA |
| infoContrato | nmCargo |  |  | Recupera o valor do campo PFUNCAO.NOME. |
| infoContrato | CBOCargo |  |  | Recupera o valor do campo PFUNCAO.CBO2002. |
| infoContrato | nmFuncao |  |  | Recupera o valor do campo PFUNCAO.NOME de acordo com o valor de PFUNC.CODFUNCAOCONF. |
| infoContrato | CBOFuncao |  |  | Recupera o valor do campo PFUNCAO.CBO2002 de acordo com o valor de PFUNC.CODFUNCAOCONF. |
| infoContrato | acumCargo |  |  | Recupera o valor do campo PFUNC.FUNCAOACUMULAVEL |
| infoContrato | codCateg |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'CODCATEGORIAESOCIAL' da tabela 'FCFO';    Caso seja autônomo Externo retorna o campo 'CATEGORIAESOCIAL' da tabela 'PPAGTOAUTONOMOEXT'. Não tendo informação ou sendo zero será o de/para  do campo 'CATAUTONOMO' da tabela  'PPAGTOAUTONOMOEX' que armazena a categoria do SEFIP e faz o de/Para para categoria do eSocial.;    O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
| remuneracao | vrSalFx |  |  | Caso o funcionário utilize salário composto, retorna a soma que compõe o total do salário do histórico salarial.  Para mais informações, acesse o link  [DT - S-2206 e S-2306 - Geração da tag <vrSalFx>](https://tdn.totvs.com/pages/viewpage.action?pageId=838954096).  Caso o parametro "Considerar maior valor de salário-hora na tag vrSalFx para professores/horistas" esteja marcado, retorna o maior salário hora cadastrado conforme data do histórico salarial.  Caso contrário, retorna o salário do histórico salarial |
| remuneracao | undSalFixo |  |  | Se PFUNC.CODTIPO for igual a "O" ou "F" retorna "7 - Não se aplica", caso contrário será verificado o tipo de recebimento conforme a serguir:   Caso PFUNC.CODRECEBIMENTO seja "D - Diarista" retorna "2 - Por Dia";  Caso PFUNC.CODRECEBIMENTO seja "H - Horista" ou "P - Professor Horista" retorna "1 - Por Hora";  Caso PFUNC.CODRECEBIMENTO seja "M - Mensalista" ou "O - Outros" retorna "5 - Por Mês";  Caso PFUNC.CODRECEBIMENTO seja "Q - Quinzenalista" retorna "4 - Por Quinzena";  Caso PFUNC.CODRECEBIMENTO seja "S - Semanalista" retorna "3 - Por Semana";  Caso PFUNC.CODRECEBIMENTO seja "T - Tarefeiro" retorna "6 - Por Tarefa"; |
| remuneracao | dscSalVar |  |  | Recupera valor do campo PFUNC.DESCRICAOSALVARIAVEL |
| duracao | tpContr |  |  | Caso o tipo de operação seja Carga Inicial e PFUNC.TEMPRAZOCONTR seja um e PFUNC.TIPOCONTPRAZODETERMINADO seja "Definido em dias" e data do fim do prazo do contrato seja maior ou igual que a data de obrigatoriedade dos eventos não períodicos retorna "2 - Prazo determinado, definido em dias" ou  Caso o tipo de operação seja Carga Inicial e PFUNC.TEMPRAZOCONTR seja um e PFUNC.TIPOCONTPRAZODETERMINADO seja "Vinculado a ocorrência de um fato" e data do fim do prazo do contrato seja maior ou igual que a data de obrigatoriedade dos eventos não períodicos retorna "3 - Prazo determinado, vinculado à ocorrência de um fato" ou  Caso o tipo de operação não seja Carga Inicial e PFUNC.TEMPRAZOCONTR seja um e PFUNC.TIPOCONTPRAZODETERMINADO seja "Definido em dias" e data do fim do prazo do contrato seja maior ou igual que a data da geração do XML retorna "2 - Prazo determinado, definido em dias" ou  Caso o tipo de operação não seja Carga Inicial e PFUNC.TEMPRAZOCONTR seja um e PFUNC.TIPOCONTPRAZODETERMINADO seja "Vinculado a ocorrência de um fato" e data do fim do prazo do contrato seja maior ou igual que a data da geração do XML retorna "3 - Prazo determinado, vinculado à ocorrência de um fato" ou  caso contrário, retorna "1 - Prazo indeterminado" |
| duracao | dtTerm | PFUNC | FIMPRAZOCONTR |  |
| duracao | clauAssec |  |  |  |
| duracao | objDet | PFUNC | MOTIVOCONTPRAZODETERMINADO |  |
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
| horContratual | qtdHrsSem |  |  | Média de horas semanais, considerando uma projeção de 7 dias.  Regra do cálculo:   Caso parâmetro para considerar jornada do funcionário esteja marcado no parametrizador do eSocial: jornada mensal / 4   Demais cenários: soma das horas das jornadas de trabalho do horário, dividido pelos dias do horário (todos os índices, inclusive dias de descanso), multiplicado por 7 (fixo).   No caso do funcionário ter direito ao adicional noturno, realiza-se o cálculo desse benefício.  Para mais informações, acesse o link |
| horContratual | tpJornada |  |  | Código recuperado através do campo AHORARIO.TIPOJORESOCIAL |
| horContratual | tmpParc | PFUNC | TEMPOPARCIAL |  |
| horContratual | horNoturno |  |  | Caso a jornada semanal contratual do funcionário possua horário noturno (no todo ou em parte), retorna S - Sim. Caso contrário, retorna N - Não. |
| horContratual | dscJorn |  |  | Caso o parâmetro "Considerar descrição do horário na tag dscJorn dos eventos S-2200 e S-2206" esteja marcado, retorna o valor do campo AHORARIO.DESCRICAO.  Caso contrário, retorna a descrição da jornada semanal contratual, contendo os dias da semana e os respectivos horários contratuais (entrada, saída e  intervalos) |
| alvaraJudicial | nrProcJud | PFUNC | NRPROCJUD |  |
| observacoes | observacao |  |  | Informação obtida a partir dos registros da tabela PFUNCOBSERVACAO campo OBSERVACAO nos anexos do funcionário. |
| treiCap | codTreiCap | VCURSOS | CODTREINAMENTOESOCIAL |  |
