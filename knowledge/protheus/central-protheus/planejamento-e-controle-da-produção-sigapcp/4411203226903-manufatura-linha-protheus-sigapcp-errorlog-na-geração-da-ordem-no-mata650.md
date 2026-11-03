---
article_id: 4411203226903
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: dab16f41ba3271cf45a8f3e0a943ad502f1d91c4dcaaf8ef576afc8c551bf509
fetched_at: '2026-06-28T22:42:42.311212+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Error.log na geração da Ordem no MATA650
type: support-article
updated_at: '2022-08-18T17:49:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411203226903-Manufatura-Linha-Protheus-SIGAPCP-Error-log-na-gera%C3%A7%C3%A3o-da-Ordem-no-MATA650
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:14 min****Ocorrência**Está gerando o **Error : 102 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Sintaxe incorreta próxima a** / **Error : 105 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Aspas não fechadas depois da cadeia de caracteres '  
GROUP BY D3\_EMISSAO '** ao abrir **OP - Ordem de Produção** no **MATA650 - Ordens de Produção**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Este erro ocorre, pois o Sistema utiliza a aspas para montar as *querys*, e existe uma **OP** cadastrada com **aspas**em algum campo.  
  
**Solução**Para resolver esta situação é necessário identificar o campo que possui a aspas e realizar o ajuste desse registro na tabela.  
  
Geralmente as **aspas** estão em algum campo da tabela: **SC2 - Ordens de Produção**.  
Então dentro do *log*localize a tabela em questão com os registros e verifique se há algum campo com **aspas**.  
  
Segue um exemplo:

```
Error : 102 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Sintaxe incorreta próxima a '01001'.  
Error : 105 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Aspas não fechadas depois da cadeia de caracteres '   
GROUP BY D3_EMISSAO '.  
( From tMSSQLConnection::GetQueryFile )  
Thread ID [5220] User [Administrador] IO [549] Tables [22] MaxTables [23] Comment [MATA650 - TCPIP - ThreadID(6536)] SP [ ] Traced [No] SQLReplay   
[No] InTran [No] DBEnv [MSSQL/DADOSMP12] DBThread [(SPID 54,59)] Started [23/05/2021 09:04:55] IP [192.168.1.212:1102] IDLE [ ] InTransact [ ]   
Memory [0] Running [ROP_QUERY for 0 s.] RCV [13366] SND [30429] TCBuild [20200606-20201110] TCVersion [20.1.1.2] ARCH [64] OS [WINDOWS]   
BUILD [RELEASE]   
SELECT COUNT(*) AS REGSD3,MAX(D3_EMISSAO) AS EMISSAO FROM SD3060 WHERE D3_FILIAL = '01' AND D3_OP = ' '' ' 01001 ' AND D3_ESTORNO <> 'S' AND   
D_E_L_E_T_ = ' ' GROUP BY D3_EMISSAO on A650DEFLEG(MATA650.PRX) 06/11/2020 14:39:56 line : 12310
```

Neste caso ao pesquisar pela tabela **SC2** é possível verificar que a aspa se encontra no campo **C2\_NUM(C) - Numero da OP**, como pode ser verificado no destaque abaixo:

```
SC2060; Rdd:TOPCONN; Alias:SC2; Filter :; Recno:1692; Total Recs:1692; Order:1  
Index (0) :**SC20601 C2_FILIAL+C2_NUM+C2_ITEM+C2_SEQUEN+C2_ITEMGRD  
Index (1) :SC20602 C2_FILIAL+C2_PRODUTO+DTOS(C2_DATPRF)  
Index (2) :SC20603 C2_FILIAL+C2_CC+DTOS(C2_DATPRF)  
Index (3) :SC20604 C2_FILIAL+C2_TPOP+C2_NUM+C2_ITEM+C2_SEQUEN+C2_ITEMGRD  
Index (4) :SC20605 C2_FILIAL+C2_CHAVE  
Index (5) :SC20606 C2_FILIAL+C2_NUM+C2_ITEM+C2_SEQUEN+C2_PRODUTO+C2_ITEMGRD  
Index (6) :SC20607 C2_FILIAL+C2_PRODUTO+C2_IDEINV  
Index (7) :SC20608 C2_FILIAL+C2_PRODUTO+C2_REVI  
Index (8) :SC20609 C2_FILIAL+C2_NUM+C2_ITEM+C2_PRODUTO  
Index (9) :SC2060A C2_FILIAL+C2_PROGRAM  
Index (10) :SC2060B C2_FILIAL+C2_PRODUTO+C2_ROTEIRO  
Field 1: C2_FILIAL(C) :01  
Field 2: C2_NUM(C) :'''   
Field 3: C2_ITEM(C) :01  
Field 4: C2_SEQUEN(C) :001  
Field 5: C2_PRODUTO(C) :MA06010068   
Field 6: C2_LOCAL(C) :01  
Field 7: C2_CC(C) :101300101  
Field 8: C2_QUANT(N) :24  
Field 9: C2_UM(C) :JG  
Field 10: C2_DATPRI(D) :2021/05/22  
Field 11: C2_DATPRF(D) :2021/06/26  
Field 12: C2_OBS(C) :   
Field 13: C2_EMISSAO(D) :2021/05/22  
Field 14: C2_PRIOR(C) :500  
Field 15: C2_QUJE(N) :0  
Field 16: C2_DATRF(D) :00/00/00  
Field 17: C2_STATUS(C) :N  
Field 18: C2_DESTINA(C) :   
Field 19: C2_VATU1(N) :0  
Field 20: C2_VINI1(N) :0  
Field 21: C2_VFIM1(N) :0  
Field 22: C2_VATU2(N) :0  
Field 23: C2_VINI2(N) :0  
Field 24: C2_VFIM2(N) :0  
Field 25: C2_VATU3(N) :0  
Field 26: C2_VINI3(N) :0  
Field 27: C2_VFIM3(N) :0  
Field 28: C2_VATU4(N) :0  
Field 29: C2_VINI4(N) :0  
Field 30: C2_VFIM4(N) :0  
Field 31: C2_VATU5(N) :0  
Field 32: C2_VINI5(N) :0  
Field 33: C2_VFIM5(N) :0  
Field 34: C2_APRATU1(N) :0  
Field 35: C2_APRINI1(N) :0  
Field 36: C2_APRFIM1(N) :0  
Field 37: C2_APRATU2(N) :0  
Field 38: C2_APRINI2(N) :0  
Field 39: C2_APRFIM2(N) :0  
Field 40: C2_APRATU3(N) :0  
Field 41: C2_APRINI3(N) :0  
Field 42: C2_APRFIM3(N) :0  
Field 43: C2_APRATU4(N) :0  
Field 44: C2_APRINI4(N) :0  
Field 45: C2_APRFIM4(N) :0  
Field 46: C2_APRATU5(N) :0  
Field 47: C2_APRINI5(N) :0  
Field 48: C2_APRFIM5(N) :0  
Field 49: C2_NIVEL(C) :   
Field 50: C2_DATAJI(D) :00/00/00  
Field 51: C2_DATAJF(D) :00/00/00  
Field 52: C2_AGLUT(C) :   
Field 53: C2_SEGUM(C) :JG  
Field 54: C2_PERDA(N) :0  
Field 55: C2_OK(C) :   
Field 56: C2_DTUPROG(D) :00/00/00  
Field 57: C2_QTUPROG(N) :0  
Field 58: C2_SEQPAI(C) :   
Field 59: C2_HORAJI(C) :   
Field 60: C2_HORAJF(C) :   
Field 61: C2_ROTEIRO(C) :   
Field 62: C2_IDENT(C) :   
Field 63: C2_RECURSO(C) :   
Field 64: C2_PEDIDO(C) :   
Field 65: C2_ITEMPV(C) :   
Field 66: C2_OPC(C) :   
Field 67: C2_QTSEGUM(N) :24  
Field 68: C2_VINIFF1(N) :0  
Field 69: C2_VINIFF2(N) :0  
Field 70: C2_VINIFF3(N) :0  
Field 71: C2_VINIFF4(N) :0  
Field 72: C2_VINIFF5(N) :0  
Field 73: C2_VFIMFF1(N) :0  
Field 74: C2_VFIMFF2(N) :0  
Field 75: C2_VFIMFF3(N) :0  
Field 76: C2_VFIMFF4(N) :0  
Field 77: C2_VFIMFF5(N) :0  
Field 78: C2_APINFF1(N) :0  
Field 79: C2_APINFF2(N) :0  
Field 80: C2_APINFF3(N) :0  
Field 81: C2_APINFF4(N) :0  
Field 82: C2_APINFF5(N) :0  
Field 83: C2_APFIFF1(N) :0  
Field 84: C2_APFIFF2(N) :0  
Field 85: C2_APFIFF3(N) :0  
Field 86: C2_APFIFF4(N) :0  
Field 87: C2_APFIFF5(N) :0  
Field 88: C2_TPOP(C) :F  
Field 89: C2_REVI(C) :   
Field 90: C2_CHAVE(C) :   
Field 91: C2_CERQUA(C) :   
Field 92: C2_REVISAO(C) :   
Field 93: C2_OPERAC(C) :   
Field 94: C2_GRADE(C) :   
Field 95: C2_ITEMGRD(C) :   
Field 96: C2_ITEMCTA(C) :   
Field 97: C2_CLVL(C) :   
Field 98: C2_LAUDO(C) :   
Field 99: C2_VERIFI(N) :0  
Field 100: C2_GRUPO(C) :   
Field 101: C2_IDEINV(C) :   
Field 102: C2_CHVQIP(C) :   
Field 103: C2_SEQMRP(C) :   
Field 104: C2_LINHA(C) :   
Field 105: C2_MOPC(C) :  
Field 106: C2_VFIMRP1(N) :0  
Field 107: C2_VFIMRP2(N) :0  
Field 108: C2_VFIMRP3(N) :0  
Field 109: C2_VFIMRP4(N) :0  
Field 110: C2_VFIMRP5(N) :0  
Field 111: C2_VINIRP1(N) :0  
Field 112: C2_VINIRP2(N) :0  
Field 113: C2_VINIRP3(N) :0  
Field 114: C2_VINIRP4(N) :0  
Field 115: C2_VINIRP5(N) :0  
Field 116: C2_APRIRP1(N) :0  
Field 117: C2_APRIRP2(N) :0  
Field 118: C2_APRIRP3(N) :0  
Field 119: C2_APRIRP4(N) :0  
Field 120: C2_APRIRP5(N) :0  
Field 121: C2_APRFRP1(N) :0  
Field 122: C2_APRFRP2(N) :0  
Field 123: C2_APRFRP3(N) :0  
Field 124: C2_APRFRP4(N) :0  
Field 125: C2_APRFRP5(N) :0  
Field 126: C2_PROGRAM(C) :   
Field 127: C2_PMACNUT(N) :0  
Field 128: C2_PMICNUT(N) :0  
Field 129: C2_BATUSR(C) :000355  
Field 130: C2_BATCH(C) :   
Field 131: C2_BATORCA(C) :N  
Field 132: C2_BATROT(C) :MATA650   
Field 133: C2_DIASOCI(N) :99  
Field 134: C2_ORDSEP(C) :   
Field 135: C2_IDAPS(C) :   
Field 136: C2_TPPR(C) :I  
Field 137: C2_BLQAPON(C) :2  
Field 138: C2_STTERCE(C) :   
Field 139: C2_OPTERCE(C) :2  
Field 140: C2_CODSAF(C) :
```
