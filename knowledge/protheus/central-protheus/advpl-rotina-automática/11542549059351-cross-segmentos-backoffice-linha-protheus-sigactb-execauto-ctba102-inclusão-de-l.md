---
article_id: 11542549059351
category: ADVPL - Rotina Automática
content_hash: 9f218fe82e8ebfe849950ab08a9e82b69725bc46d1143c8ddccdfae656ea3586
fetched_at: '2026-06-28T22:40:25.190345+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGACTB- ExecAuto CTBA102 - Inclusão
  de Lançamentos Contábeis.
type: support-article
updated_at: '2023-01-12T15:01:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11542549059351-Cross-Segmentos-Backoffice-Linha-Protheus-SIGACTB-ExecAuto-CTBA102-Inclus%C3%A3o-de-Lan%C3%A7amentos-Cont%C3%A1beis
---

**Dúvida**ExecAuto para Inclusão de Lançamentos Contábeis -CTBA102  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - Todas as versões  
  
**Solução**Rotina Automática: CTBA102

Exemplos de execução via rotina automática na rotina de lançamentos contábeis automáticos(CTBA102), mostrando exemplos de utilização e tabelas relacionadas.

**Aviso**

A Execução automática está disponível apenas para Inclusão de lançamentos contábeis.

**Importante**

Na utilização de ExecAuto considerar os seguintes critérios:

- Passar o campo CT2\_CONVER como 15555, demais moedas devem ser feitos pela inclusão de um novo aItens

- Passar o campo CT2\_CRITER, para as demais moedas apenas inclui como conversão, não permitindo a inclusão do CT2\_VALOR zerado.

- Para alteração de registro passe novamente o aCab

**PoC**

```
#INCLUDE "PROTHEUS.CH"  
  
//-------------------------------------------------------------------  
/*/{Protheus.doc} MyCTBA102Inc   
  
Inclusão de Lançamento Automático CTBA102  
  
@author Totvs  
@since 23/06/2022  
@version 2.0  
  
/*/  
//-------------------------------------------------------------------  
  
User Function MyCTBA102Inc()  
  
Local aArea := GetArea()  
Local aCab := {}  
Local aItens := {}  
  
Private lMsErroAuto := .F.  
Private lMsHelpAuto := .T.  
Private CTF_LOCK := 0  
Private lSubLote := .T.  
  
  
RpcSetType(3)  
RpcSetEnv( 'T1', 'D MG 01 ',,,'CTB')  
  
aAdd(aCab, {'DDATALANC' ,dDataBase ,NIL} )  
aAdd(aCab, {'CLOTE' ,'333333' ,NIL} )  
aAdd(aCab, {'CSUBLOTE' ,'001' ,NIL} )  
aAdd(aCab, {'CPADRAO' ,'' ,NIL} )  
aAdd(aCab, {'NTOTINF' ,0 ,NIL} )  
aAdd(aCab, {'NTOTINFLOT' ,0 ,NIL} )  
  
aAdd(aItens,{ {'CT2_FILIAL' ,xFilial('CT2'), NIL},;  
{'CT2_LINHA' , '001' , NIL},;  
{'CT2_MOEDLC' ,'01' , NIL},;  
{'CT2_DC' ,'3' , NIL},;  
{'CT2_DEBITO' ,'101010100' , NIL},;  
{'CT2_CREDIT' ,'201010100' , NIL},;  
{'CT2_VALOR' , 3000 , NIL},;  
{'CT2_ORIGEM' ,'MSEXECAUT' , NIL},;  
{'CT2_HP' ,'' , NIL},;  
{'CT2_CONVER' ,'11' , NIL},;  
{'CT2_HIST' ,'MSEXECCT2' , NIL} } )   
  
MSExecAuto({|x, y,z| CTBA102(x,y,z)}, aCab ,aItens, 3)  
  
If lMsErroAuto  
lMsErroAuto := .F.  
MostraErro()  
Endif  
  
RestArea(aArea)  
  
  
Return
```

#### **TABELAS UTILIZADAS**

* CT2- Lançamentos Contábeis

Exemplo:

Saiba mais:

[Rotina Automática CTBA102](https://tdn.totvs.com/pages/releaseview.action?pageId=107381546)
