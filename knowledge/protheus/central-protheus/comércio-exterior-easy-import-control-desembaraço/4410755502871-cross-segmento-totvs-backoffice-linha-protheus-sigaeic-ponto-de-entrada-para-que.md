---
article_id: 4410755502871
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 11b320ee8b6d8a1d75cbc93b960a570c7885a127e9655c2c5787ec62a4b260e8
fetched_at: '2026-06-28T22:39:50.163583+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto de entrada
  para quebra de itens para número de serie da NF
type: support-article
updated_at: '2021-10-14T21:36:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410755502871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-entrada-para-quebra-de-itens-para-n%C3%BAmero-de-serie-da-NF
---

**Dúvida** Precisarei incluir o número de série para cada item da NF **(EICDI154)** e efetuar a quebra, mesma lógica da numeração de Lote. Temos algum ponto de entrada para quebra de itens da Nota fiscal e de lote?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Contro*l – Todas versões  
  
**Solução**Para as quebras do itens será necessário implementar dois pontos de entrada:  
  
1) **Tem\_Outra\_Quebra**: Este ponto ele vai ligar a variável **lQuebra\_Espe** para informar ao sistema que usa uma quebra específica.

|  |  |  |
| --- | --- | --- |
| **Nome** | **Tipo** | **Descrição** |
| **TEM\_OUTRA\_QUEBRA** | Caracter | Possibilita customizar novas opções de quebra para a Nota Fiscal. |

Exemplo:

```
#Include 'Protheus.ch'  
  
User Function EICDI154()  
  
If ValType(ParamIXB) == "A"  
    cParam:= ParamIXB[1]  
Else  
    cParam:= ParamIXB  
EndIf  
cParam:= Upper(cParam)  
  
Case cParam == "TEM_OUTRA_QUEBRA"  
   lQuebra_espe:=.T.  
   IF nItem >= GetMV("MV_HDNFIMP") .OR.;  
      cForn # Work1->WKFORN .OR.;  
      nItem == 0 .OR. cCFO # Work1->WK_CFO .OR.;  
      (lIntDraw .AND. Work1->WKACMODAL # cACModal) .OR.;  
      (lQuebraOperacao .AND. cOperacao # Work1->WK_OPERACA)  
      lQuebrou_NF:=.T.  
   Endif  
  
EndCase  
  
Return
```

2) **QUEBROU\_NF**: Para informar ao sistema quando deve quebrar a nota (é chamado item a item, e  informa true na variável **lQuebrou\_NF** para quebrar).

|  |  |  |
| --- | --- | --- |
| **Nome** | **Tipo** | **Descrição** |
| **QUEBROU\_NF** | Caracter | Possibilita controlar a quebra de nota. |

Exemplo:

```
#Include 'Protheus.ch'  
  
User Function EICDI154()  
  
If ValType(ParamIXB) == "A"  
    cParam:= ParamIXB[1]  
Else  
    cParam:= ParamIXB  
  
EndIf  
cParam:= Upper(cParam)  
  
Case cParam == "QUEBROU_NF"  
    IF nTipoNF == 2 .Or. nTipoNF == 7   
        IF Work1->WKNOTAOR <> cNumComp .OR. Work1->WKSERIEOR <> cSerieComp .Or. nItem >= nValQuebra  
            cNumComp := WORK1->WKNOTAOR  
            cSerieComp := WORK1->WKSERIEOR  
            lQuebrou_NF:= .T.  
       ENDIF  
EndCase  
  
Return
```

**Saiba mais**[PE EICDI154 - Recebimento de Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=574364993)
