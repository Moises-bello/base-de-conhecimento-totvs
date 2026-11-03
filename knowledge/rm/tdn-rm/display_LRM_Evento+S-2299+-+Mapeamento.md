---
content_hash: 7ab6e30cd25a8b4516a58a34af0a9e2694bfd207f4df4fd87cf0a3ad070040bb
fetched_at: '2026-06-29T00:08:56.284787+00:00'
page_id: '351376351'
product: rm
source: tdn-rm
title: Evento S-2299 - Mapeamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2299+-+Mapeamento
version: 33
---

Leiautes1Leiaute S-1.3

Mapeamento dos campos para o leiaute S-1.3

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro\_eSocial** | **Campo\_eSocial** | **Tabela\_RM** | **Coluna\_RM** | **Informações\_do\_calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | indGuia |  |  | Campo gerado com valor fixo '1' apenas para empregador com natureza jurídica 402-2 - Segurado Especial |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideVinculo | cpfTrab | PPESSOA | CPF |  |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| infoDeslig | mtvDeslig |  |  | Retorna o que for informado pelo cliente no parametrizador do eSocial De/Para de desligamento, Caso não exista nada no De/Para :  Caso PFUNC.TIPODEMISSAO seja "1 - Inic.Empregador com justa causa" retorna "01 - Rescisão com justa causa, por iniciativa do empregador";  Caso PFUNC.TIPODEMISSAO seja "2 - Inic.Empregador sem justa causa"  e PFUNC.TEMPRAZOCONTR seja 1 e PFUNC.FIMPRAZOCONTR seja maior que PFUNC.DTDESLIGAMENTO   retorna "03 - Rescisão antecipada do contrato a termo por iniciativa do empregador"; Caso contrário retorna "02 - Rescisão sem justa causa, por iniciativa do empregador";  Caso PFUNC.TIPODEMISSAO seja "6 - Transferência com ônus p/ Cedente" retorna "02 - Rescisão sem justa causa, por iniciativa do empregador";   Caso PFUNC.TIPODEMISSAO seja "C - Culpa Recíproca" retorna "05 - Rescisão por culpa recíproca";  Caso PFUNC.TIPODEMISSAO seja "T - Término de contrato de trabalho" retorna "06 - Rescisão por término do contrato a termo";  Caso PFUNC.TIPODEMISSAO seja "3 - Inic.Empregado com justa causa" ou "4 - Inic.Empregado sem justa causa" e PFUNC.TEMPRAZOCONTR seja 1 e PFUNC.FIMPRAZOCONTR seja maior que PFUNC.DTDESLIGAMENTO   retorna "04 -Rescisão antecipada do contrato a termo por iniciativa do empregado"; Caso contrário retorna "07 - Rescisão do contrato de trabalho por iniciativa do empregado";  Caso PFUNC.TIPODEMISSAO seja "8 - Falecimento", "F - Falecimento p/ acidente de trabalho" ou "P - Falecimento p/ doenca profissional" retorna "10 - Rescisão por falecimento do empregado ";  Caso PFUNC.TIPODEMISSAO seja "5 - Transferência sem ônus p/ Cedente" e PFUNC.MOTIVOSAIDATRANSFERENCIA igual a "Sucessão de vinculo" retorna "13 - Transferência de empregado de empresa ou consórcio, para outra empresa ou consórcio que tenha assumido os encargos trabalhistas por motivo de sucessão (fusão, cisão ou incorporação)";  Caso PFUNC.TIPODEMISSAO seja "5 - Transferência sem ônus p/ Cedente" e PFUNC.MOTIVOSAIDATRANSFERENCIA igual a "Empresa consorciada" retorna "12 - Transferência de empregado da empresa consorciada para o consórcio que tenha assumido os encargos trabalhistas, e vice-versa, sem que tenha havido rescisão do contrato de trabalho";  Caso PFUNC.TIPODEMISSAO seja "5 - Transferência sem ônus p/ Cedente" e PFUNC.MOTIVOSAIDATRANSFERENCIA igual a "Empresa mesmo grupo" retorna "11 - Transferência de empregado para empresa do mesmo grupo empresarial que tenha assumido os encargos trabalhistas, sem que tenha havido rescisão do contrato de trabalho";  Caso PFUNC.TIPODEMISSAO seja "5 - Transferência sem ônus p/ Cedente" e PFUNC.MOTIVOSAIDATRANSFERENCIA igual a "Empresa inapta por inexistência de fato" retorna "43 - Transferência de empregado de empresa considerada inapta por inexistência de fato";  Caso PFUNC.TIPODEMISSAO seja "N - Rescisão Indireta" retorna "17 - Rescisão Indireta do Contrato de Trabalho";  Caso PFUNC.TIPODEMISSAO seja "U - Aposentadoria Compulsória", "I - Apos. p/ Idade com resc. contrato", "J - Apos. p/ Idade sem resc. contrato", "R - Apos. Tempo Serv. c/ Resc. Contrato", "S - Apos.tempo servico sem resc.contrato" ou "E - Aposentadoria especial" retorna "38 - Aposentadoria, exceto por invalidez";  Caso PFUNC.TIPODEMISSAO seja "A - Aposentadoria invalidez (ac. trab.)", "D - Aposentadoria invalidez (doenca)" ou "O - Aposentadoria invalidez (outros)" retorna "39 - Aposentadoria de servidor estatutário, por invalidez";  Caso PFUNC.TIPODEMISSAO seja "M - Mudanca de Regime Trabalhista" retorna "30 - Mudança de Regime Trabalhista";  Caso PFUNC.TIPODEMISSAO seja "V - Comum acordo" retorna "33 - Rescisão por acordo entre as partes (art. 484-A da CLT)";  Caso PFUNC.TIPODEMISSAO seja "G - Força Maior" retorna "27 - Rescisão por motivo de força maior";  Caso PFUNC.TIPODEMISSAO seja "H - Exoneração de Cargo Comissionado" retorna "02 - Rescisão sem justa causa, por iniciativa do empregador";  Caso funcionário seja aprendiz e PFUNC.DEMISSAODESEMPISULFINAD seja '1' retorna "41 - Rescisão do contrato de aprendizagem por desempenho insuficiente ou inadaptação do aprendiz";  Caso funcionário seja aprendiz e PFUNC.DEMISSAODESEMPISULFINAD seja '2' retorna "42 - Rescisão do contrato de aprendizagem por ausência injustificada do aprendiz à escola que implique perda do ano letivo";  Caso PFUNC.TIPODEMISSAO seja "7 - Reforma ou Transf. para Reserva" retorna "21 - Reforma militar";  Outro caso retorna vazio. |
| infoDeslig | dtDeslig | PFUNC | DTDESLIGAMENTO |  |
| infoDeslig | dtAvPrv |  |  | Retorna o valor do campo PFUNC.DTAVISOPREVIO quando o aviso prévio for trabalhado ou misto |
| infoDeslig | indPagtoAPI |  |  | Caso PFUNC.TEMAVISOPREVIO seja 1 retorna "S" caso contrário, retorna "N" |
| infoDeslig | dtProjFimAPI |  |  | Caso PFUNC.TEMAVISOPREVIO seja 1 retorna PFUNC.DTAVISOPREVIO + PFUNC.NRODIASAVISO caso contrário retorna vazio |
| infoDeslig | pensAlim |  |  | Sistema verifica nos parâmetros de pensão dos dependentes do funcionário. Caso, parâmetro "Retenção FGTS" esteja marcado e  os dependentes que tiverem 'Fórmula Adicional' será considerado do tipo '2- Valor'. Para os que tiverem apenas 'Percentual' informado será considerado '1- Percentual'.  Para os que tiverem 'Fórmula Adicional' e o 'Percentual' preenchido será considerado o tipo '3- Percentual e Valor'.  Caso, parâmetro "Retenção FGTS" esteja desmarcado, será considerado o tipo '0- Não existe'. |
| infoDeslig | percAliment |  |  | Somatório do campo percentual para os dependentes que não tiverem fórmula de cálculo e fórmula adicional de pensão. |
| infoDeslig | vrAlim |  |  | Será feito o somatório do movimento de pensão alimentícia do beneficiário na competência de acordo com o código de incidência tributária da rubrica para o IRRF. |
| infoDeslig | nrProcTrab | PFUNC | NROPROCESSOTRAB |  |
| infoDeslig | indPDV | PFUNC | ADESAOPDV | Caso campo "Tem Adesão ao Programa de Demissão Voluntária" esteja marcado no cadastro da rescisão, retorna "S";  Caso o campo esteja desmarcado ou desabilitado, *tag* não é gerada no XML.    Obs.: *Tag* gerada apenas no S-1.2. Ainda que o parâmetro esteja marcado, *tag* não é gerada em leiautes anteriores. |
| infoInterm | dia |  |  | Dias do mês efetivamente trabalhados pelo empregado conforme horário informado na convocação |
| observacoes | observacao |  |  |  |
| sucessaoVinc | tpInsc |  |  | Caso o valor informado no campo PFUNC.CNPJEMPRESASUCESSORA seja um CNPJ válido   retorna "1 - CNPJ". Caso o valor informado seja um CPF válido retorna "2 - CPF". |
| sucessaoVinc | nrInsc | PFUNC | CNPJEMPRESASUCESSORA |  |
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
| descFolha | insConsig | PFEMPRT | MATINSTCONS |  |
| descFolha | nrContr | PFEMPRT | NUMCONTEMPCONS |  |
| descFolha | observacao | PFEMPRT | OBSERVACAO |  |
| detOper | cnpjOper | VOPERADORASAUDE | CNPJ |  |
| detOper | regANS | VOPERADORASAUDE | regANS |  |
| detOper | vrPgTit |  |  | Valor do evento – Valor dos dependentes informado no histórico de assistência saúde |
| detPlano | tpDep |  |  | É recuperado a idade do dependente a partir do campo PFDEPEND.DTNASCIMENTO;  Caso PFDEPEND.GRAUPARENTESCO seja "5 - Conjuge" retorna "1 - Cônjuge.";  Caso PFDEPEND.GRAUPARENTESCO seja "C - Companheiro" retorna "2 - Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 (cinco) anos ou possua Declaração de União Estável.";  Caso PFDEPEND.GRAUPARENTESCO seja "1 - FilhoValido" ou "D - Enteado" ou "3 - FilhoValido" retorna "3 - Filho(a) ou enteado(a).";  Caso PFDEPEND.GRAUPARENTESCO seja "1 - FilhoValido" ou "D - Enteado" ou "3 - FilhoValido" e PFDEPEND.UNIVERSITARIO seja VERDADEIRO e IDADE menor ou igual a 24 retorna "4 - Filho(a) ou enteado(a) universitário(a) ou cursando escola técnica de 2º grau, até 24 (vinte e quatro) anos.";  Caso PFDEPEND.GRAUPARENTESCO seja "I - IrmaoValido" ou "N = IrmaoInvalido" ou "T - Neto" retorna "6 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial.";  Caso PFDEPEND.GRAUPARENTESCO seja "6 - Pai", "7 - Mae" ou "A - Avo" retorna "9 - Pais, avós e bisavós.";  Caso PFDEPEND.GRAUPARENTESCO seja "M - Menor Pobre" retorna "10 - Menor pobre do qual detenha a guarda judicial."  Caso PFDEPEND.GRAUPARENTESCO seja "B - Incapaz" retorna "11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador."  Caso PFDEPEND.GRAUPARENTESCO seja "G - ExConjuge" retorna "12 - Ex-cônjuge."  Caso PFDEPEND.GRAUPARENTESCO seja diferente dos códigos acima, retorna "99 Agregado/Outros". |
| detPlano | cpfDep | PFDEPEND | CPF |  |
| detPlano | nmDep | PFDEPEND | NOME |  |
| detPlano | dtNascto | PFDEPEND | DTNASCIMENTO |  |
| detPlano | vlrPgDep | PFHSTASSMED | VALOR |  |
| infoAgNocivo | grauExp |  |  | Campo calculado a partir do Código de Ocorrência obtido no Histórico de Ocorrência (PHSTOCORRENCIA) para a competência do Dissídio (perRef) conforme abaixo:  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 0, 1ou 5 retorna "1-Não ensejador de aposentadoria especial";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 4 ou 8 retorna "4-Ensejador de Aposentadoria Especial - FAE25\_06% (25 anos de contribuição e alíquota de 6%)";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 3 ou 7 retorna "3-Ensejador de Aposentadoria Especial - FAE20\_09% (20 anos de contribuição e alíquota de 9%)";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 2 ou 6 retorna "2-Ensejador de Aposentadoria Especial - FAE15\_12% (15 anos de contribuição e alíquota de 12%)" |
| infoSimples | indSimples |  |  | Caso exista registro na tabela PFHSTINDSIMPLES com a DTMUDANCA menor ou igual PFUNC.DTDESLIGAMENTO retorna PFHSTINDSIMPLES.CODIGO do histórico mais atual.    Senão retorna PFUNC.INDSIMPLES |
| ideADC | dtAcConv | PDADOSDIS | DTACORDO |  |
| ideADC | tpAcConv | PDADOSDIS | TPACORDO |  |
| ideADC | dsc | PDADOSDIS | DESCRICAO |  |
| idePeriodo | perRef |  |  | O sistema buscará o mês e ano que existirem nos campos PFVERBASDIS.ANOREF e PFVERBASDIS.MESREF de acordo com a competência do desligamento. |
| ideEstabLot | tpInsc |  |  | Caso PSECAO.TPLOTACAO seja 10, 21, 24 ou 90 retorna vazio;  Caso PSECAO.TPLOTACAO seja 01, 04, 05, 06, 08 ou 09 retorna "1 - CNPJ";  Caso PSECAO.TPLOTACAO seja 03 ou 07 retorna "2 - CPF";  Caso PSECAO.TPLOTACAO seja 02 retorna "4 - CNO (Cadastro Nacional de Obra)";  Outro caso retorna "1 - CNPJ";  Para esse evento são válidos somente os códigos "1 - CNPJ e "4 - CNO" |
| ideEstabLot | nrInsc |  |  | Caso PSECAO.TPLOTACAO seja 01, 03, 04, 05, 06, 07, 08 ou 09 retorna PSECAO.CGC;  Caso PSECAO.TPLOTACAO seja 02 retorna PSECAO.CNO;  Caso PSECAO.TPLOTACAO seja 10, 21, 24 ou 90 retorna vazio;  Outro caso retorna PSECAO.CGC;  Para esse evento são válidos somente os valores retornados do campo PSECAO.CGC ou PSECAO.CNO |
| ideEstabLot | codLotacao |  |  | Caso seção no nível de quebra do FPAS possua um valor de FPAS definido, recupera o código desta seção, caso contrário recupera o código da seção no nível de quebra da filial. |
| detVerbas | codRubr | PEVENTO | CODIGO |  |
| detVerbas | ideTabRubr |  |  | Caso exista Prefixo para os eventos de tabela, retorna o caractere parametrizado, caso contrário, retorna GCOLIGADA.CODIGO |
| detVerbas | qtdRubr | PFFINANC | REF |  |
| detVerbas | fatorRubr |  |  | Caso PEVENTO.VALHORDIAREF seja Hora ou Referência retorna PEVENTO.PORCINCID, caso contrário retorna vazio |
| detVerbas | vrRubr | PFFINANC | VALOR |  |
| detVerbas | indApurIR |  |  | Se for verba de IRRF RRA (códigos de cálculo 207, 211 ou 215) o valor será 1, caso contrário será 0. |
| infoAgNocivo | grauExp |  |  | Campo calculado a partir do Código de Ocorrência obtido no Histórico de Ocorrência (PHSTOCORRENCIA) para a competência do Dissídio (perRef) conforme abaixo:  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 0, 1ou 5 retorna "1-Não ensejador de aposentadoria especial";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 4 ou 8 retorna "4-Ensejador de Aposentadoria Especial - FAE25\_06% (25 anos de contribuição e alíquota de 6%)";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 3 ou 7 retorna "3-Ensejador de Aposentadoria Especial - FAE20\_09% (20 anos de contribuição e alíquota de 9%)";  -Caso PHSTOCORRENCIA.CODOCORRENCIA seja 2 ou 6 retorna "2-Ensejador de Aposentadoria Especial - FAE15\_12% (15 anos de contribuição e alíquota de 12%)" |
| infoSimples | indSimples |  |  | Caso exista registro na tabela PFHSTINDSIMPLES com a DTMUDANCA menor ou igual PFUNC.DTDESLIGAMENTO retorna PFHSTINDSIMPLES.CODIGO do histórico mais atual.    Senão retorna PFUNC.INDSIMPLES |
| infoTrabInterm | codConv |  |  | Informação obtida a partir dos registros da tabela PFCONVOCACAO campo CODCONVOCACAO no anexo do funcionário. |
| procJudTrab | tpTrib |  |  | Caso PFPROCESSOSJUDICIAIS.TPTRIBUTO seja 'IRRF' retorna 1  Caso PFPROCESSOSJUDICIAIS.TPTRIBUTO seja 'INSS' retorna 2  Caso PFPROCESSOSJUDICIAIS.TPTRIBUTO seja 'FGTS' retorna 3  Caso PFPROCESSOSJUDICIAIS.TPTRIBUTO seja 'Contribuição sindical' retorna 4 |
| procJudTrab | nrProcJud | PFPROCESSOSJUDICIAIS | NROPROCESSO |  |
| procJudTrab | codSusp | PFPROCESSOSJUDICIAIS | CODSUSPPROCJUD |  |
| infoMV | indMV |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'INDMV' da tabela 'PESOCIALCLIFOR';  Caso seja autônomo Externo retorna o campo 'INDMV' da tabela 'PPAGTOAUTONOMOEX';  Caso o funcionário possua vinculo em outra empresa, tanto referente a outra coligada como externo, e o valor da contribuição seja igual a zero, então retorna 1;  Caso o funcionário possua vinculo em outra empresa, tanto referente a outra coligada como externo, e o valor da contribuição seja menor que o teto do INSS, então retorna 2.  Nos demais casos retorna 3. |
| remunAposDeslig | indRemun | PFUNC | INDSITREMUNAPOSDESLIG |  |
| remunAposDeslig | dtFimRemun | PFUNC | DTFIMQUARENTENA |  |
| consigFGTS | insConsig | PFEMPRT | MATINSTCONS |  |
| consigFGTS | nrContr | PFEMPRT | NUMCONTEMPCONS |  |
