---
article_id: 1500001854242
category: ADVPL - Rotina Automática
content_hash: 02c41ef8fcac397452fec2b86f224b69616c591714422a4630f774103ccc265c
fetched_at: '2026-06-28T22:40:24.093916+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Exemplo ExecAuto FINA080
  estorno parcial
type: support-article
updated_at: '2021-12-29T15:07:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001854242-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Exemplo-ExecAuto-FINA080-estorno-parcial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como realizar via ExecAuto FINA080 o estorno parcial?  
  
**Ambiente**Protheus – ADVPL – A partir da versão 12.  
  
**Solução**No ExecAuto deve ser informado o **nSeqBx** como parâmetro preenchendo a sequência de baixa a ser estornada conforme exemplo:

```
#Include 'Protheus.ch'  
#include "tbiconn.ch"  
  
User Function BxFINA080(nOpc, nVlrPag, nSeqBx)  
Local cChave := ""  
Local lRet := .T.  
  
//Operação a ser realizada (3 = Baixa, 5 = cancelamento, 6 = Exclusão)  
Default nOpc := 6  
  
//Valor a ser baixado  
Default nVlrPag := 0  
  
//Sequência de baixa a ser cancelada.  
Default nSeqBx := 1  
  
Private lMsErroAuto := .F.  
Private cHistBaixa := "Teste exclusão fina080"  
  
DbSelectArea("SE2")  
SE2->(dbSetOrder(1))  
SE2->(dbGoTop())  
  
cChave := SE2->(E2_FILIAL+E2_PREFIXO+E2_NUM+E2_PARCELA+E2_TIPO+E2_FORNECE+E2_LOJA)  
  
If SE2->(dbSeek(cChave))  
    If nOpc == 3  
        If lRet := (nVlrPag + SE2->E2_SALDO) > 0  
            nVlrPag := If(nVlrPag > 0, nVlrPag, SE2->E2_SALDO)  
        EndIf  
    ElseIf SE2->E2_VALOR >= SE2->E2_SALDO  
        nVlrPag := 0  
    EndIf  
      
    If lRet  
        aBaixa := {}          
          
        Aadd(aBaixa, {"E2_FILIAL", SE2->E2_FILIAL,  nil})  
        Aadd(aBaixa, {"E2_PREFIXO", SE2->E2_PREFIXO,  nil})  
        Aadd(aBaixa, {"E2_NUM", SE2->E2_NUM,      nil})  
        Aadd(aBaixa, {"E2_PARCELA", SE2->E2_PARCELA,  nil})  
        Aadd(aBaixa, {"E2_TIPO", SE2->E2_TIPO,     nil})  
        Aadd(aBaixa, {"E2_FORNECE", SE2->E2_FORNECE,  nil})  
        Aadd(aBaixa, {"E2_LOJA", SE2->E2_LOJA ,    nil})  
        Aadd(aBaixa, {"AUTMOTBX", "NOR",            nil})  
        Aadd(aBaixa, {"AUTBANCO", "001",            nil})  
        Aadd(aBaixa, {"AUTAGENCIA", "AG001",          nil})  
        Aadd(aBaixa, {"AUTCONTA", "CTA001 ",     nil})  
        Aadd(aBaixa, {"AUTDTBAIXA", dDataBase,        nil})  
        Aadd(aBaixa, {"AUTDTCREDITO", dDataBase,        nil})  
        Aadd(aBaixa, {"AUTHIST", cHistBaixa,       nil})  
        Aadd(aBaixa, {"AUTVLRPG", nVlrPag,          nil})  
  
        //Pergunte da rotina  
        AcessaPerg("FINA080", .F.)                    
          
        //Chama a execauto da rotina de baixa manual (FINA080)  
        MsExecauto({|x,y,z,v| FINA080(x,y,z,v)}, aBaixa, nOpc, .F., nSeqBx)  
          
        If lMsErroAuto  
            MostraErro()  
        Else  
            If nOpc == 3  
                Alert("Baixa efetuada com sucesso")  
            Else  
                Alert("Exclusão realizada com sucesso")  
            EndIf  
        EndIf  
    Else  
        Alert("O título não possui saldo a pagar em aberto")  
    EndIf  
Else  
    Alert("O título a pagar não foi localizado")  
EndIf  
  
Return
```

**Observação:** Para um título que possui 4 baixas, temos as sequências: 01, 02, 03 e 04. Para excluir a primeira baixa de sequência 01, é necessário informar no ExecAuto o valor 1.  
Uma vez excluída a baixa 01, a sequência 02 passa a ser a primeira baixa, a 03 a segunda e assim por diante.

**Saiba mais:**  
**[Baixa e Cancelamento Contas a Pagar](https://tdn.totvs.com/display/public/PROT/Baixa+e+Cancelamento+Contas+a+Pagar)**

**[Exclusao baixa cp execauto](https://tdn.totvs.com/display/public/PROT/617600+DSERFINP-992+DT+Exclusao+baixa+cp+execauto)**
