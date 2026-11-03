---
content_hash: 0159be00b0a118297101a6a97ce6fe35cebd4210fadebb31507746c21646b6bc
fetched_at: '2026-06-29T00:08:56.335798+00:00'
page_id: '351376480'
product: rm
source: tdn-rm
title: Evento S-2399 - Mapeamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2399+-+Mapeamento
version: 27
---

Leiautestrue2Leiaute S-1.3

Mapeamento dos campos para o leiaute S-1.3

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | indGuia |  |  | Campo gerado com valor fixo '1' apenas para empregador com natuzera jurídica 402-2 - Segurado Especial |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideTrabSemVinculo | cpfTrab |  |  |  |
| ideTrabSemVinculo | codCateg |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'CODCATEGORIAESOCIAL' da tabela 'FCFO';    Caso seja autônomo Externo retorna o campo 'CATEGORIAESOCIAL' da tabela 'PPAGTOAUTONOMOEXT'. Não tendo informação ou sendo zero será o de/para  do campo 'CATAUTONOMO' da tabela  'PPAGTOAUTONOMOEX' que armazena a categoria do SEFIP e faz o de/Para para categoria do eSocial.;    O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
| infoTSVTermino | dtTerm | PFUNC | DATADEMISSAO |  |
| infoTSVTermino | mtvDesligTSV |  |  | Caso PFUNC.TIPODEMISSAO seja "2 - Inic. Empregador sem justa causa" ou "H - Exoneração de Cargo Comissionado" retorna "1 - Exoneração do Diretor Não Empregado sem justa causa, por deliberação da assembléia, dos sócios cotistas ou da autoridade competente";    Caso PFUNC.TIPODEMISSAO seja "4 - Inic. Empregado sem justa causa" retorna "3 - Exoneração a pedido de Diretor Não Empregado";  Caso PFUNC.TIPODEMISSAO seja "8 - Falecimento", "F - Falecimento p/ acidente de trabalho" ou "P - Falecimento p/ doenca profissional" retorna "5 - Morte do Diretor Não Empregado";    Caso PFUNC.TIPODEMISSAO seja "C - Culpa Recíproca" retorna "4 - Exoneração do Diretor Não Empregado por culpa recíproca ou força maior";    Caso PFUNC.TIPODEMISSAO seja "T - Término de contrato de trabalho" retorna "2 - Término de Mandato do Diretor Não Empregado que não tenha sido reconduzido ao cargo" |
| infoTSVTermino | pensAlim |  |  | Sistema verifica nos parâmetros de pensão dos dependentes do funcionário. Caso, parâmetro "Retenção FGTS" esteja marcado e  os dependentes que tiverem 'Fórmula de Cálculo' ou 'Fórmula Adicional' será considerado do tipo '2- Valor'. Para os que tiverem apenas 'Percentual' informado será considerado '1- Percentual'.  Para os que tiverem valor na 'Movimentação da Pensão de Dependentes' e o 'Percentual' preenchido será considerado o tipo '3- Percentual e Valor'.   Caso, parâmetro "Retenção FGTS" esteja desmarcado, será considerado o tipo '0- Não existe'. |
| infoTSVTermino | percAliment |  |  | Somatório do campo percentual para os dependentes que não tiverem fórmula de cálculo e fórmula adicional de pensão. |
| infoTSVTermino | vrAlim |  |  | Será feito o somatório do movimento de pensão alimentícia do beneficiário na competência de acordo com o código de incidência tributária da rubrica para o IRRF. |
| infoTSVTermino | nrProcTrab | PFUNC | NROPROCESSOTRAB |  |
| dmDev | ideDmDev |  |  | Recupera o valor do campo PFFINANC.NROPERIODO. Quando se trata de autônomo do Gestão Financeira ou Externo obtêm o valor de suas respectivas movimentações |
| dmDev | indRRA |  |  | Caso o valor do campo PFPERFF.NROPERIODO seja igual ao campo "Período folha/férias" ou "Período décimo terceiro" ou "Período rescisão" disponível no parametrizador retorna "S" |
| infoRRA | tpProcRRA | PFHSTRRA | TIPOPROCESSO |  |
| infoRRA | nrProcRRA | PFHSTRRA | NROPROCESSO |  |
| infoRRA | descRRA | PFHSTRRA | NATUREZARRA |  |
| infoRRA | qtdMesesRRA | PFHSTRRA | QTDMESES |  |
| despProcJud | vlrDespCustas | PFHSTRRA | VALORDAJUD |  |
| despProcJud | vlrDespAdvogados |  |  | Retorna o somatório dos valores do campo "VALORPAGOADVOGADO" da tabela "PFHSTRRAADVOGADOS" |
| ideAdv | tpInsc |  |  | Retorna 1 caso seja informado um CNPJ válido no campo "CPFCNPJADVOGADO" da tabela "PFHSTRRAADVOGADOS"  ou retorna 2 caso seja informado um CPF válido no campo "CPFCNPJADVOGADO" da tabela "PFHSTRRAADVOGADOS" |
| ideAdv | nrInsc | PFHSTRRAADVOGADOS | CPFCNPJADVOGADO |  |
| ideAdv | vlrAdv | PFHSTRRAADVOGADOS | VALORPAGOADVOGADO |  |
| ideEstabLot | tpInsc |  |  | Caso PSECAO.TPLOTACAO seja 10, 21, 24 ou 90 retorna vazio;  Caso PSECAO.TPLOTACAO seja 01, 04, 05, 06, 08 ou 09 retorna "1 - CNPJ";  Caso PSECAO.TPLOTACAO seja 03 ou 07 retorna "2 - CPF";  Caso PSECAO.TPLOTACAO seja 02 retorna "4 - CNO (Cadastro Nacional de Obra)";  Outro caso retorna "1 - CNPJ";  Para esse evento são válidos somente os códigos "1 - CNPJ e "4 - CNO" |
| ideEstabLot | nrInsc |  |  | Caso PSECAO.TPLOTACAO seja 01, 03, 04, 05, 06, 07, 08 ou 09 retorna PSECAO.CGC;  Caso PSECAO.TPLOTACAO seja 02 retorna PSECAO.CNO;  Caso PSECAO.TPLOTACAO seja 10, 21, 24 ou 90 retorna vazio;  Outro caso retorna PSECAO.CGC;  Para esse evento são válidos somente os valores retornados do campo PSECAO.CGC ou PSECAO.CNO |
| ideEstabLot | codLotacao |  |  | Caso seção no nível de quebra do FPAS possua um valor de FPAS definido, recupera o código desta seção, caso contrário recupera o código da seção no nível de quebra da filial. |
| detVerbas | codRubr | PEVENTO | CODIGO |  |
| detVerbas | ideTabRubr |  |  | Caso exista Prefixo para os eventos de tabela, retorna o caractere parametrizado, caso contrário, retorna GCOLIGADA.CODIGO |
| detVerbas | qtdRubr | PFFINANC | REF |  |
| detVerbas | fatorRubr |  |  | Caso PEVENTO.VALHORDIAREF seja Hora ou Referência retorna PEVENTO.PORCINCID, caso contrário retorna vazio |
| detVerbas | vrRubr | PFFINANC | VALOR |  |
| detVerbas | indApurIR |  |  | Se for verba de IRRF RRA (códigos de cálculo 207, 211 ou 215) o valor será 1, caso contrário será 0. |
| descFolha | tpDesc |  |  | Caso PFEMPRT.EMPCONSGARANTFGTS seja igual a 2 retorna 1. |
| descFolha | instFinanc | PFEMPRT | MATINSTCONS |  |
| descFolha | nrDoc | PFEMPRT | NUMCONTEMPCONS |  |
| descFolha | observacao | PFEMPRT | OBSERVACAO |  |
| planSaude | cnpjOper |  |  | Recupera o valor do campo VOPERADORASAUDE.CNPJ informado no cadastro de operadora de saúde |
| planSaude | regANS |  |  | Recupera o valor do campo VOPERADORASAUDE.REGISTROANS informado no cadastro de operadora de saúde |
| planSaude | vlrSaudeTit |  |  | Valor do evento – Valor do titular informado no histórico de assistência saúde |
| infoDepSau | cpfDep |  |  | Recupera o valor do campo PFDEPEND.CPF informado no cadastro de dependentes |
| infoDepSau | vlrSaudeDep |  |  | Valor do evento – Valor do dependente informado no histórico de assistência saúde |
| infoAgNocivo | grauExp |  |  | Campo calculado a partir do Código de Ocorrência obtido no Histórico de Ocorrência (PHSTOCORRENCIA) para a competência do Dissídio (perRef) conforme abaixo:  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 0, 1ou 5 retorna "1-Não ensejador de aposentadoria especial";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 4 ou 8 retorna "4-Ensejador de Aposentadoria Especial - FAE25\_06% (25 anos de contribuição e alíquota de 6%)";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 3 ou 7 retorna "3-Ensejador de Aposentadoria Especial - FAE20\_09% (20 anos de contribuição e alíquota de 9%)";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 2 ou 6 retorna "2-Ensejador de Aposentadoria Especial - FAE15\_12% (15 anos de contribuição e alíquota de 12%)" |
| infoSimples | indSimples |  |  |  |
| procJudTrab | tpTrib |  |  | Caso PFPROCESSOSJUDICIAIS.TPTRIBUTO seja 'IRRF' retorna 1  Caso PFPROCESSOSJUDICIAIS.TPTRIBUTO seja 'INSS' retorna 2  Caso PFPROCESSOSJUDICIAIS.TPTRIBUTO seja 'FGTS' retorna 3  Caso PFPROCESSOSJUDICIAIS.TPTRIBUTO seja 'Contribuição sindical' retorna 4 |
| procJudTrab | nrProcJud | PFPROCESSOSJUDICIAIS | NROPROCESSO |  |
| procJudTrab | codSusp | PFPROCESSOSJUDICIAIS | CODSUSPPROCJUD |  |
| infoMV | indMV |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'INDMV' da tabela 'PESOCIALCLIFOR';  Caso seja autônomo Externo retorna o campo 'INDMV' da tabela 'PPAGTOAUTONOMOEX';  Caso o funcionário possua vinculo em outra empresa, tanto referente a outra coligada como externo, e o valor da contribuição seja igual a zero, então retorna 1;  Caso o funcionário possua vinculo em outra empresa, tanto referente a outra coligada como externo, e o valor da contribuição seja menor que o teto do INSS, então retorna 2.  Nos demais casos retorna 3. |
| remunOutrEmpr | tpInsc |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'TPINSCRICAO' da tabela 'PESOCIALCLIFORMULTVINCULOS';  Caso seja autônomo Externo retorna 1 ou 2 de acordo com o campo "CNPJREMUNOUTREMPR" da tabela 'PPAGTOAUTONOMOEX';  Caso seja vinculo externo retorna o campo 'TPINSCRICAO' da tabela 'PFMULTVINCULOSEXTERNO';  Caso seja vinculo outra coligada retorna o campo 'IDENTIFICACAOCGC' da tabela 'PSECAO' |
| remunOutrEmpr | nrInsc |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'NRINSCRICAO' da tabela 'PESOCIALCLIFORMULTVINCULOS';  Caso seja autônomo Externo retorna o campo 'CNPJREMUNOUTREMPR'  da tabela 'PPAGTOAUTONOMOEX';  Caso seja vinculo externo retorna o campo 'NRINSCRICAO' da tabela 'PFMULTVINCULOSEXTERNO';  Caso seja vinculo outra coligada retorna o campo 'CGC' da tabela 'PSECAO' |
| remunOutrEmpr | codCateg |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'CODCATEGORIA' da tabela 'PESOCIALCLIFORMULTVINCULOS';  O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
| remunOutrEmpr | vlrRemunOE |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'VLRREMUNERACAO' da tabela 'PESOCIALCLIFORMULTVINCULOS';  Caso seja vinculo externo retorna o campo 'VLRREMUNERACAO' da tabela 'PFMULTVINCULOSEXTERNO';  Caso seja vinculo outra coligada retorna o campo 'BASEINSS' mais 'BASEINSS13' da tabela 'PFPERFF' |
| remunAposTerm | indRemun | PFUNC | INDSITREMUNAPOSDESLIG |  |
| remunAposTerm | dtFimRemun | PFUNC | DTFIMQUARENTENA |  |
