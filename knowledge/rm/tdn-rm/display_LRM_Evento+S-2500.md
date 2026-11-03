---
content_hash: e9acaba42d3ac6319d86a6cca40bc0b8d09ff2103444af825fb208f7653734df
fetched_at: '2026-06-29T00:11:26.705634+00:00'
page_id: '719675896'
product: rm
source: tdn-rm
title: Evento S-2500
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2500
version: 7
---

Leiautes2Leiaute S-1.2

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
| ideResp | tpInsc | VPROCESSOTRABALHISTA | TPINSCRESP |  |
| ideResp | nrInsc | VPROCESSOTRABALHISTA | NRINSCRESP |  |
| infoProcesso | origem | VPROCESSOTRABALHISTA | ORIGEM |  |
| infoProcesso | nrProcTrab | VPROCESSOTRABALHISTA | NRPROCTRAB |  |
| infoProcesso | obsProcTrab | VPROCESSOTRABALHISTA | OBSPROCTRAB |  |
| infoProcJud | dtSent | VPROCTRABDADOSCOMPL | DTSENT |  |
| infoProcJud | ufVara | VPROCTRABDADOSCOMPL | UFVARA |  |
| infoProcJud | codMunic | VPROCTRABDADOSCOMPL | CODMUNIC |  |
| infoProcJud | idVara | VPROCTRABDADOSCOMPL | IDVARA |  |
| infoCCP | dtCCP | VPROCTRABDADOSCOMPL | DTCCP |  |
| infoCCP | tpCCP | VPROCTRABDADOSCOMPL | TPCCP |  |
| infoCCP | cnpjCCP | VPROCTRABDADOSCOMPL | CNPJCCP |  |
| ideTrab | cpfTrab | VPROCTRABTRABALHADOR | CPFTRAB |  |
| ideTrab | nmTrab | VPROCTRABTRABALHADOR | NMTRAB |  |
| ideTrab | dtNascto | VPROCTRABTRABALHADOR | DTNASCTO |  |
| infoContr | tpContr | VPROCTRABINFOCONTRATO | TPCONTR |  |
| infoContr | indContr | VPROCTRABINFOCONTRATO | INDCONTR |  |
| infoContr | dtAdmOrig | VPROCTRABINFOCONTRATO | DTADMORIG |  |
| infoContr | indReint | VPROCTRABINFOCONTRATO | INDREINT |  |
| infoContr | indCateg | VPROCTRABINFOCONTRATO | INDCATEG |  |
| infoContr | indNatAtiv | VPROCTRABINFOCONTRATO | INDNATATIV |  |
| infoContr | indMotDeslig | VPROCTRABINFOCONTRATO | INDMOTDESLIG |  |
| infoContr | matricula | VPROCTRABINFOCONTRATO | MATRICULA |  |
| infoContr | codCateg | VPROCTRABINFOCONTRATO | CODCATEG |  |
| infoContr | dtInicio | VPROCTRABINFOCONTRATO | DTINICIO |  |
| infoCompl | codCBO | VPROCTRABINFOCONTRATOCOMPL | CODCBO |  |
| infoCompl | natAtividade | VPROCTRABINFOCONTRATOCOMPL | NATATIVIDADE |  |
| remuneracao | dtRemun | VPROCTRABREMUNERACAO | DTREMUN |  |
| remuneracao | vrSalFx | VPROCTRABREMUNERACAO | VRSALFX |  |
| remuneracao | undSalFixo | VPROCTRABREMUNERACAO | UNDSALFIXO |  |
| remuneracao | dscSalVar | VPROCTRABREMUNERACAO | DSCSALVAR |  |
| infoVinc | tpRegTrab | VPROCTRABINFOVINC | TPREGTRAB |  |
| infoVinc | tpRegPrev | VPROCTRABINFOVINC | TPREGPREV |  |
| infoVinc | dtAdm | VPROCTRABINFOVINC | DTADM |  |
| infoVinc | tmpParc | VPROCTRABINFOVINC | TMPPARC |  |
| duracao | tpContr | VPROCTRABINFOVINC | TPCONTR |  |
| duracao | dtTerm | VPROCTRABINFOVINC | DTTERM |  |
| duracao | clauAssec | VPROCTRABINFOVINC | CLAUASSEC |  |
| duracao | objDet | VPROCTRABINFOVINC | OBJDET |  |
| observacoes | observacao | VPROCTRABOBSERVACOES | OBSERVACAO |  |
| sucessaoVinc | tpInsc | VPROCTRABINFOVINC | TPINSC |  |
| sucessaoVinc | nrInsc | VPROCTRABINFOVINC | NRINSC |  |
| sucessaoVinc | matricAnt | VPROCTRABINFOVINC | MATRICANT |  |
| sucessaoVinc | dtTransf | VPROCTRABINFOVINC | DTTRANSF |  |
| infoDeslig | dtDeslig | VPROCTRABINFOVINC | DTDESLIG |  |
| infoDeslig | mtvDeslig | VPROCTRABINFOVINC | MTVDESLIG |  |
| infoDeslig | dtProjFimAPI | VPROCTRABINFOVINC | DTPROJFIMAPI |  |
| infoDeslig | pensAlim | VPROCTRABINFOVINC | PENSALIM |  |
| infoDeslig | percAliment | VPROCTRABINFOVINC | PERCALIMENT |  |
| infoDeslig | vrAlim | VPROCTRABINFOVINC | VRALIM |  |
| infoTerm | dtTerm | VPROCTRABINFOCONTRATOCOMPL | DTTERM |  |
| infoTerm | mtvDesligTSV | VPROCTRABINFOCONTRATOCOMPL | MTVDESLIGTSV |  |
| mudCategAtiv | codCateg | VPROCTRABMUDCATEGATIV | CODCATEG |  |
| mudCategAtiv | natAtividade | VPROCTRABMUDCATEGATIV | NATATIVIDADE |  |
| mudCategAtiv | dtMudCategAtiv | VPROCTRABMUDCATEGATIV | DTMUDCATEGATIV |  |
| unicContr | matUnic | VPROCTRABUNICIDADECONTRATUAL | MATUNIC |  |
| unicContr | codCateg | VPROCTRABUNICIDADECONTRATUAL | CODCATEG |  |
| unicContr | dtInicio | VPROCTRABUNICIDADECONTRATUAL | DTINICIO |  |
| ideEstab | tpInsc | VPROCTRABINFOCONTRATO | TPINSCFILIAL |  |
| ideEstab | nrInsc | VPROCTRABINFOCONTRATO | NRINSCFILIAL |  |
| infoVlr | compIni | VPROCTRABINFOCONTRATO | COMPINI |  |
| infoVlr | compFim | VPROCTRABINFOCONTRATO | COMPFIM |  |
| infoVlr | indReperc | VPROCTRABINFOCONTRATO | INDREPERC |  |
| infoVlr | indenSD | VPROCTRABINFOCONTRATO | INDENSD |  |
| infoVlr | indenAbono | VPROCTRABINFOCONTRATO | INDENABONO |  |
| abono | anoBase | VPROCTRABABONO | ANOBASE |  |
| idePeriodo | perRef | VPROCTRABPERIODO | PERREF |  |
| baseCalculo | vrBcCpMensal | VPROCTRABPERIODO | VRBCCPMENSAL |  |
| baseCalculo | vrBcCp13 | VPROCTRABPERIODO | VRBCCP13 |  |
| infoAgNocivo | grauExp | VPROCTRABPERIODO | GRAUEXP |  |
| infoFGTS | vrBcFGTSProcTrab | VPROCTRABPERIODO | VRBCFGTSPROCTRAB |  |
| infoFGTS | vrBcFGTSSefip | VPROCTRABPERIODO | VRBCFGTSSEFIP |  |
| infoFGTS | vrBcFGTSDecAnt | VPROCTRABPERIODO | VRBCFGTSDECANT |  |
| baseMudCateg | codCateg | VPROCTRABPERIODO | CODCATEG |  |
| baseMudCateg | vrBcCPrev | VPROCTRABPERIODO | VRBCCPREV |  |

2Leiaute S-1.3

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
| ideResp | tpInsc | VPROCESSOTRABALHISTA | TPINSCRESP |  |
| ideResp | nrInsc | VPROCESSOTRABALHISTA | NRINSCRESP |  |
| ideResp | dtAdmRespDir | VPROCESSOTRABALHISTA | DTADMRESPDIR |  |
| ideResp | matRespDir | VPROCESSOTRABALHISTA | MATRESPDIR |  |
| infoProcesso | origem | VPROCESSOTRABALHISTA | ORIGEM |  |
| infoProcesso | nrProcTrab | VPROCESSOTRABALHISTA | NRPROCTRAB |  |
| infoProcesso | obsProcTrab | VPROCESSOTRABALHISTA | OBSPROCTRAB |  |
| infoProcJud | dtSent | VPROCTRABDADOSCOMPL | DTSENT |  |
| infoProcJud | ufVara | VPROCTRABDADOSCOMPL | UFVARA |  |
| infoProcJud | codMunic | VPROCTRABDADOSCOMPL | CODMUNIC |  |
| infoProcJud | idVara | VPROCTRABDADOSCOMPL | IDVARA |  |
| infoCCP | dtCCP | VPROCTRABDADOSCOMPL | DTCCP |  |
| infoCCP | tpCCP | VPROCTRABDADOSCOMPL | TPCCP |  |
| infoCCP | cnpjCCP | VPROCTRABDADOSCOMPL | CNPJCCP |  |
| ideTrab | cpfTrab | VPROCTRABTRABALHADOR | CPFTRAB |  |
| ideTrab | nmTrab | VPROCTRABTRABALHADOR | NMTRAB |  |
| ideTrab | dtNascto | VPROCTRABTRABALHADOR | DTNASCTO |  |
| ideTrab | ideSeqTrab | VPROCTRABTRABALHADOR | IDESEQTRAB |  |
| infoContr | tpContr | VPROCTRABINFOCONTRATO | TPCONTR |  |
| infoContr | indContr | VPROCTRABINFOCONTRATO | INDCONTR |  |
| infoContr | dtAdmOrig | VPROCTRABINFOCONTRATO | DTADMORIG |  |
| infoContr | indReint | VPROCTRABINFOCONTRATO | INDREINT |  |
| infoContr | indCateg | VPROCTRABINFOCONTRATO | INDCATEG |  |
| infoContr | indNatAtiv | VPROCTRABINFOCONTRATO | INDNATATIV |  |
| infoContr | matricula | VPROCTRABINFOCONTRATO | MATRICULA |  |
| infoContr | codCateg | VPROCTRABINFOCONTRATO | CODCATEG |  |
| infoContr | dtInicio | VPROCTRABINFOCONTRATO | DTINICIO |  |
| infoCompl | codCBO | VPROCTRABINFOCONTRATOCOMPL | CODCBO |  |
| infoCompl | natAtividade | VPROCTRABINFOCONTRATOCOMPL | NATATIVIDADE |  |
| remuneracao | dtRemun | VPROCTRABREMUNERACAO | DTREMUN |  |
| remuneracao | vrSalFx | VPROCTRABREMUNERACAO | VRSALFX |  |
| remuneracao | undSalFixo | VPROCTRABREMUNERACAO | UNDSALFIXO |  |
| remuneracao | dscSalVar | VPROCTRABREMUNERACAO | DSCSALVAR |  |
| infoVinc | tpRegTrab | VPROCTRABINFOVINC | TPREGTRAB |  |
| infoVinc | tpRegPrev | VPROCTRABINFOVINC | TPREGPREV |  |
| infoVinc | dtAdm | VPROCTRABINFOVINC | DTADM |  |
| infoVinc | tmpParc | VPROCTRABINFOVINC | TMPPARC |  |
| duracao | tpContr | VPROCTRABINFOVINC | TPCONTR |  |
| duracao | dtTerm | VPROCTRABINFOVINC | DTTERM |  |
| duracao | clauAssec | VPROCTRABINFOVINC | CLAUASSEC |  |
| duracao | objDet | VPROCTRABINFOVINC | OBJDET |  |
| observacoes | observacao | VPROCTRABOBSERVACOES | OBSERVACAO |  |
| sucessaoVinc | tpInsc | VPROCTRABINFOVINC | TPINSC |  |
| sucessaoVinc | nrInsc | VPROCTRABINFOVINC | NRINSC |  |
| sucessaoVinc | matricAnt | VPROCTRABINFOVINC | MATRICANT |  |
| sucessaoVinc | dtTransf | VPROCTRABINFOVINC | DTTRANSF |  |
| infoDeslig | dtDeslig | VPROCTRABINFOVINC | DTDESLIG |  |
| infoDeslig | mtvDeslig | VPROCTRABINFOVINC | MTVDESLIG |  |
| infoDeslig | dtProjFimAPI | VPROCTRABINFOVINC | DTPROJFIMAPI |  |
| infoDeslig | pensAlim | VPROCTRABINFOVINC | PENSALIM |  |
| infoDeslig | percAliment | VPROCTRABINFOVINC | PERCALIMENT |  |
| infoDeslig | vrAlim | VPROCTRABINFOVINC | VRALIM |  |
| infoTerm | dtTerm | VPROCTRABINFOCONTRATOCOMPL | DTTERM |  |
| infoTerm | mtvDesligTSV | VPROCTRABINFOCONTRATOCOMPL | MTVDESLIGTSV |  |
| mudCategAtiv | codCateg | VPROCTRABMUDCATEGATIV | CODCATEG |  |
| mudCategAtiv | natAtividade | VPROCTRABMUDCATEGATIV | NATATIVIDADE |  |
| mudCategAtiv | dtMudCategAtiv | VPROCTRABMUDCATEGATIV | DTMUDCATEGATIV |  |
| unicContr | matUnic | VPROCTRABUNICIDADECONTRATUAL | MATUNIC |  |
| unicContr | codCateg | VPROCTRABUNICIDADECONTRATUAL | CODCATEG |  |
| unicContr | dtInicio | VPROCTRABUNICIDADECONTRATUAL | DTINICIO |  |
| ideEstab | tpInsc | VPROCTRABINFOCONTRATO | TPINSCFILIAL |  |
| ideEstab | nrInsc | VPROCTRABINFOCONTRATO | NRINSCFILIAL |  |
| infoVlr | compIni | VPROCTRABINFOCONTRATO | COMPINI |  |
| infoVlr | compFim | VPROCTRABINFOCONTRATO | COMPFIM |  |
| infoVlr | indReperc | VPROCTRABINFOCONTRATO | INDREPERC |  |
| infoVlr | indenSD | VPROCTRABINFOCONTRATO | INDENSD |  |
| infoVlr | indenAbono | VPROCTRABINFOCONTRATO | INDENABONO |  |
| abono | anoBase | VPROCTRABABONO | ANOBASE |  |
| idePeriodo | perRef | VPROCTRABPERIODO | PERREF |  |
| baseCalculo | vrBcCpMensal | VPROCTRABPERIODO | VRBCCPMENSAL |  |
| baseCalculo | vrBcCp13 | VPROCTRABPERIODO | VRBCCP13 |  |
| infoAgNocivo | grauExp | VPROCTRABPERIODO | GRAUEXP |  |
| infoFGTS | vrBcFGTSProcTrab | VPROCTRABPERIODO | VRBCFGTSPROCTRAB |  |
| infoFGTS | vrBcFGTSSefip | VPROCTRABPERIODO | VRBCFGTSSEFIP |  |
| infoFGTS | vrBcFGTSDecAnt | VPROCTRABPERIODO | VRBCFGTSDECANT |  |
| baseMudCateg | codCateg | VPROCTRABPERIODO | CODCATEG |  |
| baseMudCateg | vrBcCPrev | VPROCTRABPERIODO | VRBCCPREV |  |
| infoInterm | dia | VPROCTRABINFOINTERM | DIA |  |
| infoInterm | hrsTrab | VPROCTRABINFOINTERM | HRSTRAB |  |
