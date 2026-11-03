---
article_id: 8130287317783
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7e2add87245bf2996e665c3ed52e4b97849d41dcd19ae1292758f09c9d409a83
fetched_at: '2026-06-28T22:42:42.292879+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Erro type mismatch on compare on A650TUDOOK(MATA650.PRX)
type: support-article
updated_at: '2022-08-12T18:04:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8130287317783-Manufatura-Linha-Protheus-SIGAPCP-Erro-type-mismatch-on-compare-on-A650TUDOOK-MATA650-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:54 min****Ocorrência**Ao **incluir** ou **alterar** uma **OP - Ordem de Produção** no **MATA650 - Ordem de produção** é apresentado o erro **type mismatch on compare on A650TUDOOK(MATA650.PRX)**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa situação ocorre quando o tipo de algum parâmetro do **MV\_PARXX** da rotina **MATA650** está diferente do padrão ou algum **PE - Ponto de Entrada** ou algum**ponto de entrada / customização** que está alterando essas informações  
  
**Solução**No **error.log** se procurar pelo **MV\_PARXX**, sendo **XX = 01, 02...**, pode ser verificado que os tipos estão diferentes e os valores passados incorretos.  
  
Considerando o exemplo abaixo, as perguntas  o **MV\_PAR01**, **MV\_PAR02, MV\_PAR07** do *log* estão como **caracter** sendo que por padrão a pergunta no **MTA650** é **numérico**. E os **MV\_PAR05**, **MV\_PAR06** estão como data, sendo que por padrão são **caracter**

```
type mismatch on compare on A650TUDOOK(MATA650.PRX) 25/11/2021 14:31:39 line : 7270  
  
[build: 7.00.210324P-20211206]  
[environment: PCP]  
[thread: 24764]  
[dbthread: 7428]  
[dbversion: 21.1.1.0]  
[dbapibuild: 20210202-20210930]  
[dbarch: 64]  
[dbso: WINDOWS]  
[rpodb: top]  
[localfiles: CTREE]  
[remark: Emp :01/01 Logged :Lucio SIGAEST Obj :MATA650 - Ordens Producao]  
[threadtype: RmtSockThread]  
Called from {|| a650TudoOk()}(MATA650.PRX) 25/11/2021 14:31:39 line : 1366  
Called from {|| nOpca := 1,If(Obrigatorio(aGets,aTela).and. Eval({|| a650TudoOk()}),oDlg:End(),(nOpca:=3,.f.))}(MATA650.PRX) 25/11/2021 14:31:39 line : 1366  
Called from SAFEEVAL(MSLIB.PRW) 04/02/2022 16:14:28 line : 6994  
Called from {|| ( LOKOK:=IF(LMESSAGEDEL,IIF(FINDFUNCTION("APMSGYESNO"), APMSGYESNO(OEMTOANSI(FWI18NLANG("MSLIB","STR0014",14)), OEMTOANSI(FWI18NLANG("MSLIB","STR0015",15))), (CMSGYESNO:="MSGYESNO", &CMSGYESNO.(OEMTOANSI(FWI18NLANG("MSLIB","STR0014",14)), OEMTOANSI(FWI18NLANG("MSLIB","STR0015",15))))), .T. ),LOK:=IF(LOKOK,(REGOTO(NREG,CALIAS),SAFEEVAL(BOK)), .F. ),EVALRETOK(LOK,NBAR),IF(TYPE("INCLUI") = "L" .AND. __NNIVELBAR == 0 .AND. (VALTYPE(LOK) <> "L" .OR. LOK),__LLOOP := INCLUI,)) }(MSLIB.PRW) 04/02/2022 16:14:28 line : 995  
Called from {|| EVAL(BOK) }(FWFORMBAR.PRW) 04/02/2022 16:14:28 line : 416  
Called from ::MSDIALOG:ACTIVATE  
Called from A650ALTERA(MATA650.PRX) 25/11/2021 14:31:39 line : 1366  
Called from FWFORMBROWSE:EXECUTE(FWFORMBROWSE.PRW) 04/02/2022 16:14:28 line : 1146  
Called from {|| OSELF:EXECUTE("A650ALTERA", 4, 0,"ALTERAR", 6,"","ALTERAR","", 6) }(FWFORMBROWSE.PRW) 04/02/2022 16:14:28 line : 578  
Called from ::MSDIALOG:ACTIVATE  
Called from FWMBROWSE:ACTIVATE(FWMBROWSE.PRW) 04/02/2022 16:14:28 line : 700  
Called from FWMBROWSE(MSLIB.PRW) 04/02/2022 16:14:28 line : 10433  
Called from MBROWSE(MSLIB.PRW) 04/02/2022 16:14:28 line : 169  
Called from MATA650(MATA650.PRX) 25/11/2021 14:31:39 line : 324  
Called from __EXECUTE(APLIB090.PRW) 04/02/2022 16:14:23 line : 721  
Called from MDIEXECUTE(APLIB260.PRW) 04/02/2022 16:14:23 line : 924  
.  
.  
.  
Public 72: __READVAR(C) :M->C2_DATPRI  
Public 73: MV_PAR01(C) :06000001001   
Public 74: MV_PAR02(C) :08200001022   
Public 75: MV_PAR03(C) :   
Public 76: MV_PAR04(C) :ZZZZZZZZZZZZZZZ  
Public 77: MV_PAR05(D) :2022/08/15  
Public 78: MV_PAR06(D) :2022/08/15  
Public 79: MV_PAR07(C) :RV  
Public 80: MV_PAR08(N) :2  
Public 81: MV_PAR09(N) :1  
Public 82: MV_PAR10(N) :1  
Public 83: MV_PAR11(N) :2  
Public 84: MV_PAR12(N) :2  
Public 85: MV_PAR13(N) :2  
Public 86: MV_PAR14(N) :2  
Public 87: MV_PAR15(N) :2  
Public 88: MV_PAR16(N) :1  
Public 89: MV_PAR17(N) :1  
Public 90: MV_PAR18(N) :1  
Public 91: MV_PAR19(C) :  
Public 92: MV_PAR20(C) :  
Public 93: MV_PAR21(C) :  
Public 94: MV_PAR22(C) :
```

Neste caso, primeiramente é necessário verificar se essas perguntas estão cadastradas incorretamente na **SX1 - Perguntas e Respostas.**Caso estejam cadastradas corretamente na tabela desative os **PE**, pois algum **PE** pode estar alterando o tipo dessas perguntas.  
  
**Saiba mais**  
Artigo que explica como desativar os **PE**: [MP - Como ativar e desativar customizações no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292-MP-Como-ativar-e-desativar-customiza%C3%A7%C3%B5es-no-Protheus)
