---
article_id: 4413445087255
category: Financeiro - Contas a Receber
content_hash: b3e1ec76d9d00836dcd23ca038cd2bfb999b487ce2f58de2f878661785fecaa6
fetched_at: '2026-06-28T22:38:13.843685+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Rotina automática
  FINA460
type: support-article
updated_at: '2021-11-17T20:31:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413445087255-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Rotina-autom%C3%A1tica-FINA460
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Há um exemplo de Execução automática da rotina Liquidação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro  - Todas as versões  
  
**Solução**Disponibilizado para utilização a montagem de array a AutoItens conforme a condição de pagamento. 

**Exemplo**

```
Montando o array a AutoItens manualmente, sem utilizar uma condição de pagamento  
  
#INCLUDE 'Protheus.ch'  
  
User Function TST460()  
  
Local nX        :=  0  
Local aCab      :=  {}  
Local aItens    :=  {}  
Local cFiltro   :=  ""  //filtro quem conterá os títulos que serão liquidados gerado com base no array aTitOri  
Local aTitOri   :=  {}        
Local cCliLiq   :=  '000001'  
Local cLojaLiq  :=  '01'  
Local cNaturez  :=  '000001'  
Local nMoeda    :=  1  
Local cTipoLiq  :=  'FT '  
Local cCond     :=  ""  
  
Private lMsErroAuto     := .F.  
Private lAutoErrNoFile  := .T.  
  
Aadd(aTitOri,{;  
'D MG 01 ',; //E1_FILIAL  
'LFG',; //E1_PREFIXO  
'LFG100001',; //E1_NUM  
' ',; //E1_PARCELA  
'NF ',; //E1_TIPO  
'000001',; //E1_CLIENTE  
'01'; //E1_LOJA  
})  
  
Aadd(aItens,{;  
{"E1_PREFIXO"   ,'LFG' },;  
{'E1_NUM' , 'LFG100002' },;  
{'E1_PARCELA' , 'A' },;  
{'E1_VENCTO' , STOD('20190630') },;  
{'E1_VLCRUZ' , 500.00 } })  
  
Aadd(aItens,{;  
{"E1_PREFIXO"   ,'LFG' },;  
{'E1_NUM' , 'LFG100002' },;  
{'E1_PARCELA' , 'B' },;  
{'E1_VENCTO' , STOD('20190730') },;  
{'E1_VLCRUZ' , 500.00 } })  
  
//Filtro do Usuario  
cFiltro := " ("  
  
For nX := 1 To Len(aTitOri)  
    If nX > 1  
        cFiltro += " .Or. "  
    EndIf  
    cFiltro += " ("  
    cFiltro += " E1_FILIAL == '" + aTitOri[nX][1] + "' .And. "  
    cFiltro += " E1_PREFIXO == '" + aTitOri[nX][2] + "' .And. E1_NUM == '" + aTitOri[nX][3] + "' .And. "  
    cFiltro += " E1_PARCELA == '" + aTitOri[nX][4] + "' .And. E1_TIPO == '" + aTitOri[nX][5] + "' .And. "  
    cFiltro += " E1_CLIENTE == '" + aTitOri[nX][6] + "' .And. E1_LOJA == '" + aTitOri[nX][7] + "' )"      
Next  
cFiltro += ") .And. E1_SITUACA $ '0FG' .And. E1_SALDO > 0 .And. Empty(E1_NUMLIQ) "  
  
//Array do processo automatico (aAutoCab)  
aCab:={{"cCondicao"     ,cCond      },;  
        {"cNatureza"    ,cNaturez   },;  
      {"E1_TIPO"      ,cTipoLiq   },;  
       {"cCliente"     ,cCliLiq    },;  
       {"nMoeda"       ,nMoeda   },;  
      {"cLoja"        ,cLojaLiq  }}  
  
Fina460(,aCab , aItens , 3, cFiltro)  
  
Return
```

**Saiba mais**

[Execução automática da rotina Liquidação - Exemplo de Execauto FINA460](https://tdn.totvs.com/pages/releaseview.action?pageId=358449689)
