---
content_hash: f1a1cd50ef2b89a7d7cf86163b0eb5a011b3d2414ef883231ea1fd4222c148c6
fetched_at: '2026-06-29T00:08:56.499516+00:00'
page_id: '351376676'
product: rm
source: tdn-rm
title: Evento S-2230
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2230
version: 17
---

Leiautes2Leiaute 2.5

Mapeamento dos campos para o leiaute 2.5.00

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
| ideVinculo | cpfTrab | PPESSOA | CPF |  |
| ideVinculo | nisTrab |  |  | Caso seja autônomo e FCFO.NIT estiver preenchido, retorna FCFO.NIT, caso contrário, retorna FCFO.CIAUTONOMO;  Caso não seja autônomo e codCateg diferente de contribuinte individual (721, 722, 723, 731, 734, 738, 761, 771) retorna PFUNC.PISPASEP, caso contrario, retorna PFUNC.CI |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| ideVinculo | codCateg |  |  | Caso seja autônomo do Fluxus retorna o campo 'CODCATEGORIAESOCIAL' da tabela 'FCFO';   Caso seja autônomo Externo retorna o campo 'CATEGORIAESOCIAL' da tabela 'PPAGTOAUTONOMOEXT'. Não tendo informação ou sendo zero será o de/para  do campo 'CATAUTONOMO' da tabela  'PPAGTOAUTONOMOEX' que armazena a categoria do SEFIP e faz o de/Para para categoria do eSocial.;   O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
| iniAfastamento | dtIniAfast |  |  | Se o afastamento for de férias retorna PFUFERIASPER.DATAINICIO, caso não seja, retorna PFHSTAFT.DTINICIO |
| iniAfastamento | codMotAfast |  |  | Caso o afastamento for de férias, retorna "15 - Gozo de férias ou recesso - Afastamento temporário para o gozo de férias ou recesso";  Caso exista informação no parametrizador do eSocial no De/Para de afastamento retorna o valor do campo Cód. Motivo eSocial;  Caso PFHSTAFT.TIPO seja "T - Af.Ac.Trabalho" ou PFHSTAFT.TIPO seja "O - Doença Ocupacional"retorna "01 - Acidente/Doença do trabalho";  Caso PFHSTAFT.TIPO seja "P - Af.Previdência" retorna "03 - Acidente/Doença não relacionada ao trabalho";  Caso PFHSTAFT.TIPO seja "I - Apos. Invalidez" retorna "06 - Aposentadoria por invalidez";  Caso PFHSTAFT.TIPO seja "R - Licença Remun." retorna "16 - Licença remunerada - Liberalidade da empresa ou Acordo/Convenção Coletiva de Trabalho";  Caso PFHSTAFT.TIPO seja "W - Licença Mater. Compl. 180 dias" retorna "18 - Licença Maternidade - a partir de 120 dias até 180 dias";  Caso PFHSTAFT.TIPO seja "L - Licença s/venc" retorna "21 - Licença não remunerada ou Sem Vencimento";  Caso PFHSTAFT.TIPO seja "S ou N - Mandato Sindical" retorna "24 - Mandato Sindical - Afastamento temporário para exercício de mandato sindical";  Caso PFHSTAFT.TIPO seja "C - Contrato de Trabalho Suspenso" retorna "27 - Qualificação - Afastamento por suspensão do contrato de acordo com o art 476-A da CLT";  Caso PFHSTAFT.TIPO seja "M - Serv.Militar" retorna "29 - Serviço Militar - Afastamento temporário"  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTADOCAO seja VERDADEIRO retorna "20 - Licença Maternidade - Afastamento temporário por motivo de licença-maternidade decorrente de adoção ou guarda judicial de criança";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTABORTONAOCRIME seja VERDADEIRO retorna "19 - Licença Maternidade - Afastamento temporário por motivo de aborto não criminoso";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTANTECIPACAO  seja VERDADEIRO retorna "35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTPRORROGACAO  seja VERDADEIRO retorna "35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e quantidade de dias de afastamento igual a 120 retorna "17 - Licença Maternidade - 120 dias";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e quantidade de dias de afastamento igual a 15 e seja falso os parâmetros MOTIVOAFASTANTECIPACAO e MOTIVOAFASTPRORROGACAO retorna "35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico";  Caso PFHSTAFT.TIPO seja "K-Cessão / Requisição " retorna "14 - Cessão / Requisição ";  Caso PFHSTAFT.TIPO seja "Q - Prisão / Cárcere" retorna "11 - Cárcere". |
| iniAfastamento | infoMesmoMtv |  |  | Se o afastamento decorre de mesmo motivo de afastamento anterior onde codMotAfastamento = [01,03] dentro de 60 dias retorna S - Sim. Caso contrário retorna N - Não. |
| iniAfastamento | tpAcidTransito | PFHSTAFT | TIPOACIDENTETRANSITO |  |
| iniAfastamento | observacao |  |  | Se o afastamento for de férias retorna PFUFERIASPER.OBSERVACAO, caso não seja, retorna PFHSTAFT.OBSERVACAO |
| infoAtestado | codCID | VOCORRENCIA | CID |  |
| infoAtestado | qtdDiasAfast |  |  | Total de dias retornado do cálculo PFHSTAFT.DTFINAL - PFHSTAFT.DTINICIO |
| emitente | nmEmit | VPROFISSIONALSAUDE | NOMEPROFISSIONAL |  |
| emitente | ideOC |  |  | Caso VPROFISSIONALSAUDE.CODORGAOCLASSE seja "CRM" retorna "1";  Caso VPROFISSIONALSAUDE.CODORGAOCLASSE seja "CRO" retorna "2";                                                                     Caso VPROFISSIONALSAUDE.CODORGAOCLASSE seja "RMS" retorna "3" |
| emitente | nrOc | VPROFISSIONALSAUDE | NUMEROREGISTRO |  |
| emitente | ufOC | VPROFISSIONALSAUDE | CODUFREGISTRO |  |
| infoCessao | cnpjCess | PFHSTAFT | CNPJORGAOCEDIDO |  |
| infoCessao | infOnus | PFHSTAFT | INFOONUS |  |
| infoMandSind | cnpjSind | PFHSTAFT | CNPJSINDICATO |  |
| infoMandSind | infOnusRemun |  |  | Caso PFHSTAFT.TIPO seja "S" retorna "2 - Apenas do Sindicato";  Caso PFHSTAFT.TIPO seja "N" e PFHSTAFT.INFOONUSREMUNERACAO seja 0 retorna "1 - Apenas do Empregador";  Caso PFHSTAFT.TIPO seja "N" e PFHSTAFT.INFOONUSREMUNERACAO seja 1 retorna "3 - Parte do Empregador, sendo a diferença e/ou complementação salarial paga pelo Sindicato"; |
| infoMandElet | cnpjMandElet | PFHSTAFT | CNPJMANDATOELETIVO |  |
| infoMandElet | indRemunCargo | PFHSTAFT | INDICATIVOREMUNERACAOCARGO |  |
| infoRetif | origRetif | PFHSTMOTIVOAFAST | ORIGEMALTERACAO |  |
| infoRetif | tpProc |  |  | Caso PFHSTMOTIVOAFAST.TIPOPROCESSO seja "A - Administrativo" retorna 1;  Caso PFHSTMOTIVOAFAST.TIPOPROCESSO seja "J - Judicial" retorna 2;  Caso PFHSTMOTIVOAFAST.TIPOPROCESSO seja "N - Número de Benefício (NB) do INSS" retorna 3. |
| infoRetif | nrProc | PFHSTMOTIVOAFAST | NUMPROCESSO |  |
| fimAfastamento | dtTermAfast |  |  | Se o afastamento for de férias retorna PFUFERIASPER.DATAFIM, caso não seja, retorna PFHSTAFT.DTFINAL |

2Leiaute S-1.0Mapeamento dos campos para o leiaute S-1.0

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
| ideVinculo | cpfTrab | PPESSOA | CPF |  |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| ideVinculo | codCateg |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'CODCATEGORIAESOCIAL' da tabela 'FCFO';    Caso seja autônomo Externo retorna o campo 'CATEGORIAESOCIAL' da tabela 'PPAGTOAUTONOMOEXT'. Não tendo informação ou sendo zero será o de/para  do campo 'CATAUTONOMO' da tabela  'PPAGTOAUTONOMOEX' que armazena a categoria do SEFIP e faz o de/Para para categoria do eSocial.;    O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
| iniAfastamento | dtIniAfast |  |  | Se o afastamento for de férias retorna PFUFERIASPER.DATAINICIO, caso não seja, retorna PFHSTAFT.DTINICIO |
| iniAfastamento | codMotAfast |  |  | Caso o afastamento for de férias, retorna "15 - Gozo de férias ou recesso - Afastamento temporário para o gozo de férias ou recesso";  Caso exista informação no parametrizador do eSocial no De/Para de afastamento retorna o valor do campo Cód. Motivo eSocial;  Caso PFHSTAFT.TIPO seja "T - Af.Ac.Trabalho" ou PFHSTAFT.TIPO seja "O - Doença Ocupacional"retorna "01 - Acidente/Doença do trabalho";  Caso PFHSTAFT.TIPO seja "P - Af.Previdência" retorna "03 - Acidente/Doença não relacionada ao trabalho";  Caso PFHSTAFT.TIPO seja "Apos. Incapac. Permanente" retorna "06 - Apos. por Incapacidade Permanente";  Caso PFHSTAFT.TIPO seja "R - Licença Remun." retorna "16 - Licença remunerada - Liberalidade da empresa ou Acordo/Convenção Coletiva de Trabalho";  Caso PFHSTAFT.TIPO seja "W - Licença Mater. Compl. 180 dias" retorna "18 - Licença Maternidade - a partir de 120 dias até 180 dias";  Caso PFHSTAFT.TIPO seja "L - Licença s/venc" retorna "21 - Licença não remunerada ou Sem Vencimento";  Caso PFHSTAFT.TIPO seja "S ou N - Mandato Sindical" retorna "24 - Mandato Sindical - Afastamento temporário para exercício de mandato sindical";  Caso PFHSTAFT.TIPO seja "C - Contrato de Trabalho Suspenso" retorna "27 - Qualificação - Afastamento por suspensão do contrato de acordo com o art 476-A da CLT";  Caso PFHSTAFT.TIPO seja "M - Serv.Militar" retorna "29 - Serviço Militar - Afastamento temporário"  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTADOCAO seja VERDADEIRO retorna "20 - Licença Maternidade - Afastamento temporário por motivo de licença-maternidade decorrente de adoção ou guarda judicial de criança";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTABORTONAOCRIME seja VERDADEIRO retorna "19 - Licença Maternidade - Afastamento temporário por motivo de aborto não criminoso";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTANTECIPACAO  seja VERDADEIRO retorna "35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTPRORROGACAO  seja VERDADEIRO retorna "35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e quantidade de dias de afastamento igual a 120 retorna "17 - Licença Maternidade - 120 dias";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e quantidade de dias de afastamento igual a 15 e seja falso os parâmetros MOTIVOAFASTANTECIPACAO e MOTIVOAFASTPRORROGACAO retorna "35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico";  Caso PFHSTAFT.TIPO seja "K-Cessão / Requisição " retorna "14 - Cessão / Requisição ";  Caso PFHSTAFT.TIPO seja "Q - Prisão / Cárcere" retorna "11 - Cárcere". |
| iniAfastamento | infoMesmoMtv |  |  | Se o afastamento decorre de mesmo motivo de afastamento anterior onde codMotAfastamento = [01,03] dentro de 60 dias retorna S - Sim. Caso contrário retorna N - Não. |
| iniAfastamento | tpAcidTransito | PFHSTAFT | TIPOACIDENTETRANSITO |  |
| iniAfastamento | observacao |  |  | Se o afastamento for de férias retorna PFUFERIASPER.OBSERVACAO, caso não seja, retorna PFHSTAFT.OBSERVACAO |
| perAquis | dtInicio |  |  | Retorna o valor do campo PFUFERIAS.INICIOPERAQUIS |
| perAquis | dtFim |  |  | Retorna o valor do campo PFUFERIAS.FIMPERAQUIS |
| infoCessao | cnpjCess | PFHSTAFT | CNPJORGAOCEDIDO |  |
| infoCessao | infOnus | PFHSTAFT | INFOONUS |  |
| infoMandSind | cnpjSind | PFHSTAFT | CNPJSINDICATO |  |
| infoMandSind | infOnusRemun |  |  | Caso PFHSTAFT.TIPO seja "S" retorna "2 - Apenas do Sindicato";  Caso PFHSTAFT.TIPO seja "N" e PFHSTAFT.INFOONUSREMUNERACAO seja 0 retorna "1 - Apenas do Empregador";  Caso PFHSTAFT.TIPO seja "N" e PFHSTAFT.INFOONUSREMUNERACAO seja 1 retorna "3 - Parte do Empregador, sendo a diferença e/ou complementação salarial paga pelo Sindicato"; |
| infoRetif | origRetif | PFHSTMOTIVOAFAST | ORIGEMALTERACAO |  |
| infoRetif | tpProc |  |  | Caso PFHSTMOTIVOAFAST.TIPOPROCESSO seja "A - Administrativo" retorna 1;  Caso PFHSTMOTIVOAFAST.TIPOPROCESSO seja "J - Judicial" retorna 2;  Caso PFHSTMOTIVOAFAST.TIPOPROCESSO seja "N - Número de Benefício (NB) do INSS" retorna 3. |
| infoRetif | nrProc | PFHSTMOTIVOAFAST | NUMPROCESSO |  |
| fimAfastamento | dtTermAfast |  |  | Se o afastamento for de férias retorna PFUFERIASPER.DATAFIM, caso não seja, retorna PFHSTAFT.DTFINAL |
