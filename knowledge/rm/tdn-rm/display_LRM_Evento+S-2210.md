---
content_hash: d48233415e1fb3315230dd3bf80639df1402a8cbc5ea96721b39e547705077dd
fetched_at: '2026-06-29T00:08:56.235886+00:00'
page_id: '351376283'
product: rm
source: tdn-rm
title: Evento S-2210
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2210
version: 13
---

Leiautestrue1Leiaute S-1.1

Mapeamento dos campos para o leiaute S-1.1

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do cálculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideVinculo | cpfTrab | PPESSOA | CPF |  |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| ideVinculo | codCateg |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'CODCATEGORIAESOCIAL' da tabela 'FCFO';    Caso seja autônomo Externo retorna o campo 'CATEGORIAESOCIAL' da tabela 'PPAGTOAUTONOMOEXT'. Não tendo informação ou sendo zero será o de/para  do campo 'CATAUTONOMO' da tabela  'PPAGTOAUTONOMOEX' que armazena a categoria do SEFIP e faz o de/Para para categoria do eSocial.;    O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| cat | dtAcid | VOCORRENCIA | DATAHORA |  |
| cat | tpAcid |  |  | Caso VOCORRENCIA.CODTIPOOCORRENCIA esteja relacionada com VTIPOOCORRENCIA, a validação do campo 'tpAcid' deve receber valores: 1, 2, 3.  TIPOACIDENTE com valor igual a '1' retorna '1'  TIPOACIDENTE com valor igual a '2' retorna '2'  TIPOACIDENTE com valor igual a '3' retorna '3' |
| cat | hrAcid |  |  | Hora do Acidente, no formato HHMM |
| cat | hrsTrabAntesAcid |  |  | Horas trabalhadas antes do acidente, no formato HHMM |
| cat | tpCat | VOCORRENCIA | TIPOCAT |  |
| cat | indCatObito |  |  | Caso VOCORRENCIA.MORTE seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| cat | dtObito | PPESSOA | DATAOBITO |  |
| cat | indComunPolicia |  |  | Caso VOCORRENCIA.REGPOLICIAL seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| cat | codSitGeradora |  |  | Informações oriundas das tabelas VFONTEGERADORA (Situação Geradora do Acidente de Trabalho) e VFONTEGERDOENCA (Agente Causador / Situação Geradora de Doença Profissional). |
| cat | iniciatCAT | VOCORRENCIA | TIPOINICIATIVA |  |
| cat | obsCAT | VOCORRENCIA | DESCRICAO |  |
| cat | ultDiaTrab | VOCORRENCIA | DIASANTECEDACIDENTE |  |
| cat | houveAfast | VOCORRENCIA | HOUVEAFASTAMENTO |  |
| localAcidente | tpLocal | VOCORRENCIA | LOCALACIDENTEINSS |  |
| localAcidente | dscLocal | VOCORRENCIA | LOCALACIDENTE |  |
| localAcidente | tpLograd |  |  | Código recuperado através dos campos VOCORRENCIA.TPLOGRADOUROACIDENTE e DCODIFICACAOLOGRADOURO.CODIGO |
| localAcidente | dscLograd | VOCORRENCIA | LOGRADOUROACIDENTE |  |
| localAcidente | nrLograd |  |  | Caso tenha valor preenchido, será obtido de VOCORRENCIA.NUMEROACIDENTE. Caso não tenha valor será preenchido com 'S/N'. |
| localAcidente | complemento | VOCORRENCIA | COMPLOGRADOUROACIDENTE |  |
| localAcidente | bairro | VOCORRENCIA | BAIRROACIDENTE |  |
| localAcidente | cep |  |  | CEP recuperado através do campo VOCORRENCIA.CEPLOCALACIDENTE. |
| localAcidente | codMunic |  |  | Código recuperado através dos campos VOCORRENCIA.UFLOCALACIDENTE e VOCORRENCIA.CODMUNICIPIOACIDENTE |
| localAcidente | uf | VOCORRENCIA | UFLOCALACIDENTE |  |
| localAcidente | pais |  |  | Código recuperado através do campo VOCORRENCIA.UFLOCALACIDENTE (país em que está o estado selecionado) |
| localAcidente | codPostal | VOCORRENCIA | CEPLOCALACIDENTE |  |
| ideLocalAcid | tpInsc | VOCORRENCIA | TIPOINSCRICAO |  |
| ideLocalAcid | nrInsc | VOCORRENCIA | NROINSCRICAO |  |
| parteAtingida | codParteAting | VNATUREZA | CODPARTECORPO |  |
| parteAtingida | lateralidade | VOCORRENCIAPARTEATINGIDA | LATERALIDADE |  |
| agenteCausador | codAgntCausador |  |  | Código recuperado através dos campos VPPRAFONTEGERA.CODESOCIALAGENTECAUSADOR ou VPPRAFONTEGERA.CODESOCIALFONTEGERADORADOENCA |
| atestado | dtAtendimento | VOCORRENCIA | DATAMEDICA |  |
| atestado | hrAtendimento |  |  | Horário de Atendimento no formato HHMM |
| atestado | indInternacao |  |  | Indicativo do Internação: Valores Válidos: S, N |
| atestado | durTrat | VOCORRENCIA | DURACAOTRATAMENTO |  |
| atestado | indAfast |  |  | Indicativo do Internação: Valores Válidos: S, N |
| atestado | dscLesao | VNATUREZALESAO | CODCLIENTE |  |
| atestado | dscCompLesao | VOCORRENCIA | DESCCOMPLESAO |  |
| atestado | diagProvavel | VOCORRENCIA | DIAGNOSTICO |  |
| atestado | codCID | VOCORRENCIA | CID |  |
| atestado | observacao | VOCORRENCIA | OBSERVACAOMEDICA |  |
| emitente | nmEmit | VPROFISSIONALSAUDE | NOMEPROFISSIONAL |  |
| emitente | ideOC |  |  | Caso VPROFISSIONALSAUDE.CODORGAOCLASSE seja "CRM" retorna "1";  Caso VPROFISSIONALSAUDE.CODORGAOCLASSE seja "CRO" retorna "2";                                                                     Caso VPROFISSIONALSAUDE.CODORGAOCLASSE seja "RMS" retorna "3" |
| emitente | nrOC | VPROFISSIONALSAUDE | NUMEROREGISTRO |  |
| emitente | ufOC | VPROFISSIONALSAUDE | CODUFREGISTRO |  |
| catOrigem | nrRecCatOrig | PESOCIALEVENTOS | ID |  |

true2Leiaute S-1.2

Mapeamento dos campos para o leiaute S-1.2

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do cálculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideVinculo | cpfTrab | PPESSOA | CPF |  |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| ideVinculo | codCateg |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'CODCATEGORIAESOCIAL' da tabela 'FCFO';    Caso seja autônomo Externo retorna o campo 'CATEGORIAESOCIAL' da tabela 'PPAGTOAUTONOMOEXT'. Não tendo informação ou sendo zero será o de/para  do campo 'CATAUTONOMO' da tabela  'PPAGTOAUTONOMOEX' que armazena a categoria do SEFIP e faz o de/Para para categoria do eSocial.;    O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| cat | dtAcid | VOCORRENCIA | DATAHORA |  |
| cat | tpAcid |  |  | Caso VOCORRENCIA.CODTIPOOCORRENCIA esteja relacionada com VTIPOOCORRENCIA, a validação do campo 'tpAcid' deve receber valores: 1, 2, 3.  TIPOACIDENTE com valor igual a '1' retorna '1'  TIPOACIDENTE com valor igual a '2' retorna '2'  TIPOACIDENTE com valor igual a '3' retorna '3' |
| cat | hrAcid |  |  | Hora do Acidente, no formato HHMM |
| cat | hrsTrabAntesAcid |  |  | Horas trabalhadas antes do acidente, no formato HHMM |
| cat | tpCat | VOCORRENCIA | TIPOCAT |  |
| cat | indCatObito |  |  | Caso VOCORRENCIA.MORTE seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| cat | dtObito | PPESSOA | DATAOBITO |  |
| cat | indComunPolicia |  |  | Caso VOCORRENCIA.REGPOLICIAL seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| cat | codSitGeradora |  |  | Informações oriundas das tabelas VFONTEGERADORA (Situação Geradora do Acidente de Trabalho) e VFONTEGERDOENCA (Agente Causador / Situação Geradora de Doença Profissional). |
| cat | iniciatCAT | VOCORRENCIA | TIPOINICIATIVA |  |
| cat | obsCAT | VOCORRENCIA | DESCRICAO |  |
| cat | ultDiaTrab | VOCORRENCIA | DIASANTECEDACIDENTE |  |
| cat | houveAfast | VOCORRENCIA | HOUVEAFASTAMENTO |  |
| localAcidente | tpLocal | VOCORRENCIA | LOCALACIDENTEINSS |  |
| localAcidente | dscLocal | VOCORRENCIA | LOCALACIDENTE |  |
| localAcidente | tpLograd |  |  | Código recuperado através dos campos VOCORRENCIA.TPLOGRADOUROACIDENTE e DCODIFICACAOLOGRADOURO.CODIGO |
| localAcidente | dscLograd | VOCORRENCIA | LOGRADOUROACIDENTE |  |
| localAcidente | nrLograd |  |  | Caso tenha valor preenchido, será obtido de VOCORRENCIA.NUMEROACIDENTE. Caso não tenha valor será preenchido com 'S/N'. |
| localAcidente | complemento | VOCORRENCIA | COMPLOGRADOUROACIDENTE |  |
| localAcidente | bairro | VOCORRENCIA | BAIRROACIDENTE |  |
| localAcidente | cep |  |  | CEP recuperado através do campo VOCORRENCIA.CEPLOCALACIDENTE. |
| localAcidente | codMunic |  |  | Código recuperado através dos campos VOCORRENCIA.UFLOCALACIDENTE e VOCORRENCIA.CODMUNICIPIOACIDENTE |
| localAcidente | uf | VOCORRENCIA | UFLOCALACIDENTE |  |
| localAcidente | pais |  |  | Código recuperado através do campo VOCORRENCIA.UFLOCALACIDENTE (país em que está o estado selecionado) |
| localAcidente | codPostal | VOCORRENCIA | CEPLOCALACIDENTE |  |
| ideLocalAcid | tpInsc | VOCORRENCIA | TIPOINSCRICAO |  |
| ideLocalAcid | nrInsc | VOCORRENCIA | NROINSCRICAO |  |
| parteAtingida | codParteAting | VNATUREZA | CODPARTECORPO |  |
| parteAtingida | lateralidade | VOCORRENCIAPARTEATINGIDA | LATERALIDADE |  |
| agenteCausador | codAgntCausador |  |  | Código recuperado através dos campos VPPRAFONTEGERA.CODESOCIALAGENTECAUSADOR ou VPPRAFONTEGERA.CODESOCIALFONTEGERADORADOENCA |
| atestado | dtAtendimento | VOCORRENCIA | DATAMEDICA |  |
| atestado | hrAtendimento |  |  | Horário de Atendimento no formato HHMM |
| atestado | indInternacao |  |  | Indicativo do Internação: Valores Válidos: S, N |
| atestado | durTrat | VOCORRENCIA | DURACAOTRATAMENTO |  |
| atestado | indAfast |  |  | Indicativo do Internação: Valores Válidos: S, N |
| atestado | dscLesao | VNATUREZALESAO | CODCLIENTE |  |
| atestado | dscCompLesao | VOCORRENCIA | DESCCOMPLESAO |  |
| atestado | diagProvavel | VOCORRENCIA | DIAGNOSTICO |  |
| atestado | codCID | VOCORRENCIA | CID |  |
| atestado | observacao | VOCORRENCIA | OBSERVACAOMEDICA |  |
| emitente | nmEmit | VPROFISSIONALSAUDE | NOMEPROFISSIONAL |  |
| emitente | ideOC |  |  | Caso VPROFISSIONALSAUDE.CODORGAOCLASSE seja "CRM" retorna "1";  Caso VPROFISSIONALSAUDE.CODORGAOCLASSE seja "CRO" retorna "2";                                                                     Caso VPROFISSIONALSAUDE.CODORGAOCLASSE seja "RMS" retorna "3" |
| emitente | nrOC | VPROFISSIONALSAUDE | NUMEROREGISTRO |  |
| emitente | ufOC | VPROFISSIONALSAUDE | CODUFREGISTRO |  |
| catOrigem | nrRecCatOrig | PESOCIALEVENTOS | ID |  |
