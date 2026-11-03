---
content_hash: a23b6a19dd564e422388ccec9b2b58e5fe09035cbe88a56a651f18f906e37e2c
fetched_at: '2026-06-29T00:11:26.735264+00:00'
page_id: '719675925'
product: rm
source: tdn-rm
title: Evento S-2501
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2501
version: 8
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
| ideProc | nrProcTrab | VPROCESSOTRIBUTOS | NRPROCTRAB |  |
| ideProc | perApurPgto | VPROCESSOTRIBUTOS | PERAPURPGTO |  |
| ideProc | obs | VPROCESSOTRIBUTOS | OBS |  |
| ideTrab | cpfTrab | VPROCTRIBTRABALHADOR | CPFTRAB |  |
| calcTrib | perRef | VPROCCALCTRIB | PERREF |  |
| calcTrib | vrBcCpMensal | VPROCCALCTRIB | VRBCCPMENSAL |  |
| calcTrib | vrBcCp13 | VPROCCALCTRIB | VRBCCP13 |  |
| infoCRContrib | tpCR | VPROCCRCONTRIB | TPCR |  |
| infoCRContrib | vrCR | VPROCCRCONTRIB | VRCR |  |
| infoCRIRRF | tpCR | VPROCTRIBIRRF | TPCR |  |
| infoCRIRRF | vrCR | VPROCTRIBIRRF | VRCR |  |
| infoIR | vrRendTrib | VPROCTRIBIRRF | VRRENDTRIB |  |
| infoIR | vrRendTrib13 | VPROCTRIBIRRF | VRRENDTRIB13 |  |
| infoIR | vrRendMoleGrave | VPROCTRIBIRRF | VRRENDMOLEGRAVE |  |
| infoIR | vrRendIsen65 | VPROCTRIBIRRF | VRRENDISEN65 |  |
| infoIR | vrJurosMora | VPROCTRIBIRRF | VRJUROSMORA |  |
| infoIR | vrRendIsenNTrib | VPROCTRIBIRRF | VRRENDISENNTRIB |  |
| infoIR | descIsenNTrib | VPROCTRIBIRRF | DESCISENNTRIB |  |
| infoIR | vrPrevOficial | VPROCTRIBIRRF | VRPREVOFICIAL |  |
| infoRRA | descRRA | VPROCTRIBINFORRA | DESCRRA |  |
| infoRRA | qtdMesesRRA | VPROCTRIBINFORRA | QTDMESESRRA |  |
| despProcJud | vlrDespCustas | VPROCTRIBINFORRA | VLRDESPCUSTAS |  |
| despProcJud | vlrDespAdvogados | VPROCTRIBINFORRA | VLRDESPADVOGADOS |  |
| ideAdv | tpInsc | VPROCTRIBIDEADV | TPINSC |  |
| ideAdv | nrInsc | VPROCTRIBIDEADV | NRINSC |  |
| ideAdv | vlrAdv | VPROCTRIBIDEADV | VLRADV |  |
| dedDepen | tpRend | VPROCTRIBDEDDEPEN | TPREND |  |
| dedDepen | cpfDep | VPROCTRIBDEDDEPEN | CPFDEP |  |
| dedDepen | vlrDeducao | VPROCTRIBDEDDEPEN | VLRDEDUCAO |  |
| penAlim | tpRend | VPROCTRIBPENALIM | TPREND |  |
| penAlim | cpfDep | VPROCTRIBPENALIM | CPFDEP |  |
| penAlim | vlrPensao | VPROCTRIBPENALIM | VLRPENSAO |  |
| infoProcRet | tpProcRet | VPROCTRIBINFOPROCRET | TPPROCRET |  |
| infoProcRet | nrProcRet | VPROCTRIBINFOPROCRET | NRPROCRET |  |
| infoProcRet | codSusp | VPROCTRIBINFOPROCRET | CODSUSP |  |
| infoValores | indApuracao | VPROCTRIBINFOVALORES | INDAPURACAO |  |
| infoValores | vlrNRetido | VPROCTRIBINFOVALORES | VLRNRETIDO |  |
| infoValores | vlrDepJud | VPROCTRIBINFOVALORES | VLRDEPJUD |  |
| infoValores | vlrCmpAnoCal | VPROCTRIBINFOVALORES | VLRCMPANOCAL |  |
| infoValores | vlrCmpAnoAnt | VPROCTRIBINFOVALORES | VLRCMPANOANT |  |
| infoValores | vlrRendSusp | VPROCTRIBINFOVALORES | VLRRENDSUSP |  |
| dedSusp | indTpDeducao | VPROCTRIBDEDSUSP | INDTPDEDUCAO |  |
| dedSusp | vlrDedSusp | VPROCTRIBDEDSUSP | VLRDEDSUSP |  |
| benefPen | cpfDep | VPROCTRIBBENEFPEN | CPFDEP |  |
| benefPen | vlrDepenSusp | VPROCTRIBBENEFPEN | VLRDEPENSUSP |  |
| infoIRComplem | dtLaudo | VPROCTRIBINFOIRCOMPLEM | DTLAUDO |  |
| infoDep | cpfDep | VPROCTRIBINFODEP | CPFDEP |  |
| infoDep | dtNascto | VPROCTRIBINFODEP | DTNASCTO |  |
| infoDep | nome | VPROCTRIBINFODEP | NOME |  |
| infoDep | depIRRF | VPROCTRIBINFODEP | DEPIRRF |  |
| infoDep | tpDep | VPROCTRIBINFODEP | TPDEP |  |
| infoDep | descrDep | VPROCTRIBINFODEP | DESCRDEP |  |

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
| ideProc | nrProcTrab | VPROCESSOTRIBUTOS | NRPROCTRAB |  |
| ideProc | perApurPgto | VPROCESSOTRIBUTOS | PERAPURPGTO |  |
| ideProc | ideSeqProc | VPROCESSOTRIBUTOS | IDESEQPROC |  |
| ideProc | obs | VPROCESSOTRIBUTOS | OBS |  |
| ideTrab | cpfTrab | VPROCTRIBTRABALHADOR | CPFTRAB |  |
| calcTrib | perRef | VPROCCALCTRIB | PERREF |  |
| calcTrib | vrBcCpMensal | VPROCCALCTRIB | VRBCCPMENSAL |  |
| calcTrib | vrBcCp13 | VPROCCALCTRIB | VRBCCP13 |  |
| infoCRContrib | tpCR | VPROCCRCONTRIB | TPCR |  |
| infoCRContrib | vrCR | VPROCCRCONTRIB | VRCR |  |
| infoCRIRRF | tpCR | VPROCTRIBIRRF | TPCR |  |
| infoCRIRRF | vrCR | VPROCTRIBIRRF | VRCR |  |
| infoCRIRRF | vrCR13 | VPROCTRIBIRRF | VRCR13 |  |
| infoIR | vrRendTrib | VPROCTRIBIRRF | VRRENDTRIB |  |
| infoIR | vrRendTrib13 | VPROCTRIBIRRF | VRRENDTRIB13 |  |
| infoIR | vrRendMoleGrave | VPROCTRIBIRRF | VRRENDMOLEGRAVE |  |
| infoIR | vrRendMoleGrave13 | VPROCTRIBIRRF | VRRENDMOLEGRAVE13 |  |
| infoIR | vrRendIsen65 | VPROCTRIBIRRF | VRRENDISEN65 |  |
| infoIR | vrRendIsen65Dec | VPROCTRIBIRRF | VRRENDISEN65DEC |  |
| infoIR | vrJurosMora | VPROCTRIBIRRF | VRJUROSMORA |  |
| infoIR | vrJurosMora13 | VPROCTRIBIRRF | VRJUROSMORA13 |  |
| infoIR | vrRendIsenNTrib | VPROCTRIBIRRF | VRRENDISENNTRIB |  |
| infoIR | descIsenNTrib | VPROCTRIBIRRF | DESCISENNTRIB |  |
| infoIR | vrPrevOficial | VPROCTRIBIRRF | VRPREVOFICIAL |  |
| infoIR | vrPrevOficial13 | VPROCTRIBIRRF | VRPREVOFICIAL13 |  |
| rendIsen0561 | vlrDiarias | VPROCTRIBIRRF | VLRDIARIAS |  |
| rendIsen0561 | vlrAjudaCusto | VPROCTRIBIRRF | VLRAJUDACUSTO |  |
| rendIsen0561 | vlrIndResContrato | VPROCTRIBIRRF | VLRINDRESCONTRATO |  |
| rendIsen0561 | vlrAbonoPec | VPROCTRIBIRRF | VLRABONOPEC |  |
| rendIsen0561 | vlrAuxMoradia | VPROCTRIBIRRF | VLRAUXMORADIA |  |
| infoRRA | descRRA | VPROCTRIBINFORRA | DESCRRA |  |
| infoRRA | qtdMesesRRA | VPROCTRIBINFORRA | QTDMESESRRA |  |
| despProcJud | vlrDespCustas | VPROCTRIBINFORRA | VLRDESPCUSTAS |  |
| despProcJud | vlrDespAdvogados | VPROCTRIBINFORRA | VLRDESPADVOGADOS |  |
| ideAdv | tpInsc | VPROCTRIBIDEADV | TPINSC |  |
| ideAdv | nrInsc | VPROCTRIBIDEADV | NRINSC |  |
| ideAdv | vlrAdv | VPROCTRIBIDEADV | VLRADV |  |
| dedDepen | tpRend | VPROCTRIBDEDDEPEN | TPREND |  |
| dedDepen | cpfDep | VPROCTRIBDEDDEPEN | CPFDEP |  |
| dedDepen | vlrDeducao | VPROCTRIBDEDDEPEN | VLRDEDUCAO |  |
| penAlim | tpRend | VPROCTRIBPENALIM | TPREND |  |
| penAlim | cpfDep | VPROCTRIBPENALIM | CPFDEP |  |
| penAlim | vlrPensao | VPROCTRIBPENALIM | VLRPENSAO |  |
| infoProcRet | tpProcRet | VPROCTRIBINFOPROCRET | TPPROCRET |  |
| infoProcRet | nrProcRet | VPROCTRIBINFOPROCRET | NRPROCRET |  |
| infoProcRet | codSusp | VPROCTRIBINFOPROCRET | CODSUSP |  |
| infoValores | indApuracao | VPROCTRIBINFOVALORES | INDAPURACAO |  |
| infoValores | vlrNRetido | VPROCTRIBINFOVALORES | VLRNRETIDO |  |
| infoValores | vlrDepJud | VPROCTRIBINFOVALORES | VLRDEPJUD |  |
| infoValores | vlrCmpAnoCal | VPROCTRIBINFOVALORES | VLRCMPANOCAL |  |
| infoValores | vlrCmpAnoAnt | VPROCTRIBINFOVALORES | VLRCMPANOANT |  |
| infoValores | vlrRendSusp | VPROCTRIBINFOVALORES | VLRRENDSUSP |  |
| dedSusp | indTpDeducao | VPROCTRIBDEDSUSP | INDTPDEDUCAO |  |
| dedSusp | vlrDedSusp | VPROCTRIBDEDSUSP | VLRDEDSUSP |  |
| benefPen | cpfDep | VPROCTRIBBENEFPEN | CPFDEP |  |
| benefPen | vlrDepenSusp | VPROCTRIBBENEFPEN | VLRDEPENSUSP |  |
| infoIRComplem | dtLaudo | VPROCTRIBINFOIRCOMPLEM | DTLAUDO |  |
| infoDep | cpfDep | VPROCTRIBINFODEP | CPFDEP |  |
| infoDep | dtNascto | VPROCTRIBINFODEP | DTNASCTO |  |
| infoDep | nome | VPROCTRIBINFODEP | NOME |  |
| infoDep | depIRRF | VPROCTRIBINFODEP | DEPIRRF |  |
| infoDep | tpDep | VPROCTRIBINFODEP | TPDEP |  |
| infoDep | descrDep | VPROCTRIBINFODEP | DESCRDEP |  |
