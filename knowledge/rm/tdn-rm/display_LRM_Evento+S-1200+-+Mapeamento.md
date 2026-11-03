---
content_hash: abccf125b5ba50ac8f69a8cd9f24502395af86619a1fa7623e184d2661e80cae
fetched_at: '2026-06-29T00:08:56.412532+00:00'
page_id: '351376519'
product: rm
source: tdn-rm
title: Evento S-1200 - Mapeamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1200+-+Mapeamento
version: 40
---

Leiautes2Leiaute S-1.3

Mapeamento dos campos para o leiaute S-1.3

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro\_eSocia**l | **Campo\_eSocial** | **Tabela\_RM** | **Coluna\_RM** | **Informações\_do\_calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | indApuracao |  | INDAPURACAO |  |
| ideEvento | perApur |  |  | Informação recuperada através dos campos 'MESCOMP e ANOCOMP' da Tabela PESOCIALFOLHAMENSAL |
| ideEvento | indGuia |  |  | Campo gerado com valor fixo '1' apenas para empregador com natuzera jurídica 402-2 - Segurado Especial |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideTrabalhador | cpfTrab |  |  |  |
| infoMV | indMV |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'INDMV' da tabela 'PESOCIALCLIFOR';  Caso seja autônomo Externo retorna o campo 'INDMV' da tabela 'PPAGTOAUTONOMOEX';  Caso o funcionário possua vinculo em outra empresa, tanto referente a outra coligada como externo, e o valor da contribuição seja igual a zero, então retorna 1;  Caso o funcionário possua vinculo em outra empresa, tanto referente a outra coligada como externo, e o valor da contribuição seja menor que o teto do INSS, então retorna 2.  Nos demais casos retorna 3. |
| remunOutrEmpr | tpInsc |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'TPINSCRICAO' da tabela 'PESOCIALCLIFORMULTVINCULOS';  Caso seja autônomo Externo retorna 1 ou 2 de acordo com o campo "CNPJREMUNOUTREMPR" da tabela 'PPAGTOAUTONOMOEX';  Caso seja vinculo externo retorna o campo 'TPINSCRICAO' da tabela 'PFMULTVINCULOSEXTERNO';  Caso seja vinculo outra coligada retorna o campo 'IDENTIFICACAOCGC' da tabela 'PSECAO' |
| remunOutrEmpr | nrInsc |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'NRINSCRICAO' da tabela 'PESOCIALCLIFORMULTVINCULOS';  Caso seja autônomo Externo retorna o campo 'CNPJREMUNOUTREMPR'  da tabela 'PPAGTOAUTONOMOEX';  Caso seja vinculo externo retorna o campo 'NRINSCRICAO' da tabela 'PFMULTVINCULOSEXTERNO';  Caso seja vinculo outra coligada retorna o campo 'CGC' da tabela 'PSECAO' |
| remunOutrEmpr | codCateg |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'CODCATEGORIA' da tabela 'PESOCIALCLIFORMULTVINCULOS';  O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
| remunOutrEmpr | vlrRemunOE |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'VLRREMUNERACAO' da tabela 'PESOCIALCLIFORMULTVINCULOS';  Caso seja vinculo externo retorna o campo 'VLRREMUNERACAO' da tabela 'PFMULTVINCULOSEXTERNO';  Caso seja vinculo outra coligada retorna o campo 'BASEINSS' mais 'BASEINSS13' da tabela 'PFPERFF' |
| infoComplem | nmTrab |  |  | Caso seja autônomo do Gestão Financeira retorna FCFO.NOME, caso seja autônomo externo retorna PPAGTOAUTONOMOEXT.NOMEAUTONOMO, caso seja autônomo cadastrado na Folha de Pagamento retorna PFUNC.NOME |
| infoComplem | dtNascto |  |  | Caso seja autônomo do Gestão Financeira retorna FCFO.DTNASCIMENTO, caso seja autônomo externo retorna PPAGTOAUTONOMOEXT.DTNASCIMENTO, caso seja autônomo cadastrado na Folha de Pagamento retorna PPESSOA.DTNASCIMENTO |
| procJudTrab | tpTrib |  |  | Caso PFPROCESSOSJUDICIAIS.TPTRIBUTO seja 'IRRF' retorna 1  Caso PFPROCESSOSJUDICIAIS.TPTRIBUTO seja 'INSS' retorna 2  Caso PFPROCESSOSJUDICIAIS.TPTRIBUTO seja 'FGTS' retorna 3  Caso PFPROCESSOSJUDICIAIS.TPTRIBUTO seja 'Contribuição sindical' retorna 4 |
| procJudTrab | nrProcJud | PFPROCESSOSJUDICIAIS | NROPROCESSO |  |
| procJudTrab | codSusp | PFPROCESSOSJUDICIAIS | CODSUSPPROCJUD |  |
| infoInterm | dia |  |  | Dias do mês efetivamente trabalhados pelo empregado conforme horário informado na convocação |
| dmDev | ideDmDev |  |  | Recupera o valor do campo PFFINANC.NROPERIODO. Quando se trata de autônomo do Gestão Financeira ou Externo obtêm o valor de suas respectivas movimentações |
| dmDev | codCateg |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'CODCATEGORIAESOCIAL' da tabela 'FCFO';    Caso seja autônomo Externo retorna o campo 'CATEGORIAESOCIAL' da tabela 'PPAGTOAUTONOMOEXT'. Não tendo informação ou sendo zero será o de/para  do campo 'CATAUTONOMO' da tabela  'PPAGTOAUTONOMOEX' que armazena a categoria do SEFIP e faz o de/Para para categoria do eSocial.;    O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
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
| ideEstabLot | tpInsc |  |  | Caso seja autônomo do Gestão Financeira ou autônomo Externo:  Caso PSECAO.CAEPF esteja preenchido retorna "3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ";  Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado e tomador obra própria:  Caso FCFOCEI.CEI esteja preenchido retorna "4 - CNO (Cadastro Nacional de Obra)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ";  Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado e tomador diferente de obra própria:  Caso PSECAO.CAEPF esteja preenchido retorna "3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ";  Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   Caso PSECAO.CAEPF esteja preenchido retorna "3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ". |
| ideEstabLot | nrInsc |  |  | Caso parâmetro “Filial é SCP” esteja marcado retorna o valor do campo GFILIAL.CGC da filial informada no campo DFILIAL.CODFILIALSOCIOSCP, independente do tpInsc;  Caso seja autônomo do Gestão Financeira ou autônomo Externo:  Caso tpInsc seja 1: retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 3: retorna valor do campo PSECAO.CAEPF;  Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado e tomador obra própria:  Caso tpInsc seja 1: retorna valor do campo FCFO.CGCCFO;  Caso tpInsc seja 4: retorna valor do campo FCFOCEI.CEI;  Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado e tomador diferente de obra própria:  Caso tpInsc seja 1: retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 3: retorna valor do campo PSECAO.CAEPF;  Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   Caso tpInsc seja 1: retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 3: retorna valor do campo PSECAO.CAEPF. |
| ideEstabLot | codLotacao |  |  | Caso seção no nível de quebra do FPAS possua um valor de FPAS definido, recupera o código desta seção, caso contrário recupera o código da seção no nível de quebra da filial. |
| remunPerApur | matricula | PFUNC | MATRICULAESOCIAL |  |
| remunPerApur | indSimples |  |  | Caso exista registro na tabela PFHSTINDSIMPLES com a DTMUDANCA menor ou igual último dia do mês (PESOCIALEVENTOS.MESCOMP) e ano (PESOCIALEVENTOS.ANOCOMP) retorna PFHSTINDSIMPLES.CODIGO histórico mais atual.    Senão retorna PFUNC.INDSIMPLES |
| itensRemun | codRubr | PEVENTO | CODIGO |  |
| itensRemun | ideTabRubr |  |  | Caso exista Prefixo para os eventos de tabela, retorna o caractere parametrizado, caso contrário, retorna GCOLIGADA.CODIGO |
| itensRemun | qtdRubr | PFFINANC | REF |  |
| itensRemun | fatorRubr |  |  | Caso PEVENTO.VALHORDIAREF seja Hora ou Referência retorna PEVENTO.PORCINCID, caso contrário retorna vazio |
| itensRemun | vrRubr | PFFINANC | VALOR |  |
| itensRemun | indApurIR |  |  | Retorna 0 |
| descFolha | tpDesc |  |  | Caso PFEMPRT.EMPCONSGARANTFGTS seja igual a 2 retorna 1. |
| descFolha | instFinanc | PFEMPRT | MATINSTCONS |  |
| descFolha | nrDoc | PFEMPRT | NUMCONTEMPCONS |  |
| descFolha | observacao | PFEMPRT | OBSERVACAO |  |
| infoAgNocivo | grauExp |  |  | Campo calculado a partir do Código de Ocorrência obtido no Histórico de Ocorrência (PHSTOCORRENCIA) para a competência do Dissídio (perRef) conforme abaixo:  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 0, 1ou 5 retorna "1-Não ensejador de aposentadoria especial";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 4 ou 8 retorna "4-Ensejador de Aposentadoria Especial - FAE25\_06% (25 anos de contribuição e alíquota de 6%)";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 3 ou 7 retorna "3-Ensejador de Aposentadoria Especial - FAE20\_09% (20 anos de contribuição e alíquota de 9%)";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 2 ou 6 retorna "2-Ensejador de Aposentadoria Especial - FAE15\_12% (15 anos de contribuição e alíquota de 12%)" |
| ideADC | dtAcConv | PDADOSDIS | DTACORDO |  |
| ideADC | tpAcConv | PDADOSDIS | TPACORDO |  |
| ideADC | dsc | PDADOSDIS | DESCRICAO |  |
| ideADC | remunSuc |  |  | Se estiver marcado o campo 'Pagamento de verbas devidas pela empresa sucessora a empregados   desligados ainda na sucedida' no cadastro do Dissídio/Acordo Coletivo o valor será 'S', caso contrário será 'N'. |
| idePeriodo | perRef |  |  | O sistema buscará o mês e ano que existirem nos campos PFVERBASDIS.ANOREF e PFVERBASDIS.MESREF de acordo com a competência do desligamento. |
| ideEstabLot | tpInsc |  |  | Caso seja autônomo do Gestão Financeira ou autônomo Externo:  Caso PSECAO.CAEPF esteja preenchido retorna "3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ";  Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado e tomador obra própria:  Caso FCFOCEI.CEI esteja preenchido retorna "4 - CNO (Cadastro Nacional de Obra)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ";  Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado e tomador diferente de obra própria:  Caso PSECAO.CAEPF esteja preenchido retorna "3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ";  Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   Caso PSECAO.CAEPF esteja preenchido retorna "3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ". |
| ideEstabLot | nrInsc |  |  | Caso seja autônomo do Gestão Financeira ou autônomo Externo:  Caso tpInsc seja 1: retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 3: retorna valor do campo PSECAO.CAEPF;  Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado e tomador obra própria:  Caso tpInsc seja 1: retorna valor do campo FCFO.CGCCFO;  Caso tpInsc seja 4: retorna valor do campo FCFOCEI.CEI;  Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado e tomador diferente de obra própria:  Caso tpInsc seja 1: retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 3: retorna valor do campo PSECAO.CAEPF;  Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   Caso tpInsc seja 1: retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 3: retorna valor do campo PSECAO.CAEPF. |
| ideEstabLot | codLotacao |  |  | Caso seção no nível de quebra do FPAS possua um valor de FPAS definido, recupera o código desta seção, caso contrário recupera o código da seção no nível de quebra da filial. |
| remunPerAnt | matricula | PFUNC | MATRICULAESOCIAL |  |
| remunPerAnt | indSimples |  |  | Caso exista registro na tabela PFHSTINDSIMPLES com a DTMUDANCA menor ou igual último dia do mês (PESOCIALEVENTOS.MESCOMP) e ano (PESOCIALEVENTOS.ANOCOMP) retorna PFHSTINDSIMPLES.CODIGO histórico mais atual.    Senão retorna PFUNC.INDSIMPLES |
| itensRemun | codRubr | PEVENTO | CODIGO |  |
| itensRemun | ideTabRubr |  |  | Caso exista Prefixo para os eventos de tabela, retorna o caractere parametrizado, caso contrário, retorna GCOLIGADA.CODIGO |
| itensRemun | qtdRubr | PFFINANC | REF |  |
| itensRemun | fatorRubr |  |  | Caso PEVENTO.VALHORDIAREF seja Hora ou Referência retorna PEVENTO.PORCINCID, caso contrário retorna vazio |
| itensRemun | vrRubr | PFFINANC | VALOR |  |
| itensRemun | indApurIR |  |  | Retorna 0 |
| infoAgNocivo | grauExp |  |  | Campo calculado a partir do Código de Ocorrência obtido no Histórico de Ocorrência (PHSTOCORRENCIA) para a competência do Dissídio (perRef) conforme abaixo:  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 0, 1ou 5 retorna "1-Não ensejador de aposentadoria especial";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 4 ou 8 retorna "4-Ensejador de Aposentadoria Especial - FAE25\_06% (25 anos de contribuição e alíquota de 6%)";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 3 ou 7 retorna "3-Ensejador de Aposentadoria Especial - FAE20\_09% (20 anos de contribuição e alíquota de 9%)";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 2 ou 6 retorna "2-Ensejador de Aposentadoria Especial - FAE15\_12% (15 anos de contribuição e alíquota de 12%)" |
| infoComplCont | codCBO |  |  | Caso seja autônomo do Gestão Financeira retorna FCFO.CBOAUTONOMO, caso seja autônomo externo retorna PPAGTOAUTONOMOEXT.CBOAUTONOMO, caso seja autônomo cadastrado na Folha de Pagamento retorna PFUNCAO.CBO2002 |
| infoComplCont | natAtividade |  |  | Caso seja autônomo do Gestão Financeira e FCFO.RAMOATIV seja 16 ou autônomo externo e PPAGTOAUTONOMOEXT.NATUREZAATIV seja 16 ou autônomo cadastrado na Folha de Pagamento e PFUNC.ESOCIALNATATIVIDADE seja 2 retorna '2-Trabalho Rural' senão retorna '1-Trabalho Urbano' |
