---
article_id: 360020782832
category: ADVPL - Rotina Automática
content_hash: 974753e2104c4a58af6c4550623d4b34ecfa99cd94c584371e78fb8c81da503a
fetched_at: '2026-06-28T22:40:25.071389+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Utilização da rotina
  FINA050 com Múltiplas Naturezas e Múltiplos Centro de Custo
type: support-article
updated_at: '2025-12-12T13:46:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020782832-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Utiliza%C3%A7%C3%A3o-da-rotina-FINA050-com-M%C3%BAltiplas-Naturezas-e-M%C3%BAltiplos-Centro-de-Custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36970876810391)Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Estamos tentando utilizar a rotina automática fina050 com múltiplas naturezas e não estamos tendo sucesso, pois a rotina não retorna erro, porem não insere registros na SEV nem SEZ.  
Vocês podem mandar um exemplo de como devemos usar esse recurso?

**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**

Exemplo de utilização da rotina com múltiplas Naturezas e centro de custo.

```
#Include 'Protheus.ch'
#INCLUDE "TBICONN.CH"

USER FUNCTION 050MULT()

LOCAL aCab := {} // array que recebera o titulo a receber
 LOCAL aAuxEv :={} // array auxiliar do rateio multinaturezas
 LOCAL aRatEvEz:={} //array do rateio multinaturezas
 LOCAL aAuxEz :={} // Array auxiliar de multiplos centros de custo
 LOCAL aRatEz:={} //Array do rateio de centro de custo em multiplas naturezas

PREPARE ENVIRONMENT EMPRESA '99' FILIAL '01'

PRIVATE lMsErroAuto := .F.

aadd( aCab ,{"E2_PREFIXO" , 'MUL' , Nil }) 
 aadd( aCab ,{"E2_NUM" , "8887" , Nil })
 aadd( aCab ,{"E2_PARCELA" , '1' , Nil })
 aadd( aCab ,{"E2_TIPO" , 'NF ' , Nil })
 aadd( aCab ,{"E2_NATUREZ" , '500 ', Nil })
 aadd( aCab ,{"E2_FORNECE" , '002 ' , Nil })
 aadd( aCab ,{"E2_LOJA" , '01' , Nil })
 aadd( aCab ,{"E2_EMISSAO" , dDataBase , Nil })
 aadd( aCab ,{"E2_VENCTO" , dDataBase , Nil })
 aadd( aCab ,{"E2_VALOR" , 1000 , Nil })
 aadd( aCab ,{"E2_BASEPIS" , 500 , Nil }) 
 aadd( aCab ,{"E2_MULTNAT" , '1' , Nil }) //rateio multinaturezs = sim

//#########################################################################################################&
 //Adicionando o vetor da 1º Natureza &
 //#########################################################################################################&

aadd( aAuxEv ,{"EV_NATUREZ" , padr('500 ',tamsx3("EV_NATUREZ")[1]), Nil })//natureza a ser rateada
 aadd( aAuxEv ,{"EV_VALOR" , 500, Nil })//valor do rateio na natureza
 aadd( aAuxEv ,{"EV_PERC" , 100, Nil })//percentual do rateio na natureza
 aadd( aAuxEv ,{"EV_RATEICC" , "1", Nil })//indicando que há rateio por centro de custo

//###########################################&
 //Adicionando multiplos centros de custo &
 //###########################################&

//primeiro centro de custo
 aAuxEz:={}
 aadd( aAuxEz ,{"EZ_CCUSTO" , '001', Nil })//centro de custo da natureza
 aadd( aAuxEz ,{"EZ_VALOR" , 250 , Nil })//valor do rateio neste centro de custo
 aadd(aRatEz,aAuxEz)
 //segundo centro de custo 
 aAuxEz:={}
 aadd( aAuxEz ,{"EZ_CCUSTO" , '002', Nil })//centro de custo na natureza
 aadd( aAuxEz ,{"EZ_VALOR" , 250 , Nil })//valor do rateio neste centro de custo
 aadd(aRatEz,aAuxEz)

aadd(aAuxEv,{"AUTRATEICC" , aRatEz, Nil })//recebendo dentro do array da natureza os multiplos centros de custo
 aAdd(aRatEvEz,aAuxEv)//adicionando a natureza ao rateio de multiplas naturezas

// Limpar os Arrays
 aAuxEv:={} // Array auxiliar do rateio multinaturezas
 aAuxEz:={} // Array auxiliar de multiplos centros de custo
 aRatEz:={} // Array do rateio de centro de custo em multiplas naturezas

//#########################################################################################################&
 //Adicionando o vetor da 2º Natureza &
 //#########################################################################################################&

aadd( aAuxEv ,{"EV_NATUREZ" , padr('499 ',tamsx3("EV_NATUREZ")[1]), Nil })//natureza a ser rateada
 aadd( aAuxEv ,{"EV_VALOR" , 500, Nil })//valor do rateio na natureza
 aadd( aAuxEv ,{"EV_PERC" , 100, Nil })//percentual do rateio na natureza
 aadd( aAuxEv ,{"EV_RATEICC" , "1", Nil })//indicando que há rateio por centro de custo

//###########################################&
 //Adicionando multiplos centros de custo &
 //###########################################&

//primeiro centro de custo
 aadd( aAuxEz ,{"EZ_CCUSTO" , '001', Nil })//centro de custo da natureza
 aadd( aAuxEz ,{"EZ_VALOR" , 250 , Nil })//valor do rateio neste centro de custo
 aadd(aRatEz,aAuxEz)
 //segundo centro de custo 
 aAuxEz:={}
 aadd( aAuxEz ,{"EZ_CCUSTO" , '002', Nil })//centro de custo na natureza
 aadd( aAuxEz ,{"EZ_VALOR" , 250 , Nil })//valor do rateio neste centro de custo
 aadd(aRatEz,aAuxEz)

aadd(aAuxEv,{"AUTRATEICC" , aRatEz, Nil })//recebendo dentro do array da natureza os multiplos centros de custo
 aAdd(aRatEvEz,aAuxEv)//adicionando a natureza ao rateio de multiplas naturezas

aAdd(aCab,{"AUTRATEEV", aRatEvEz,Nil})//adicionando ao vetor aCab o vetor do rateio

MsExecAuto( { |x,y,z| FINA050(x,y,z)} , aCab, ,3) //inclusao

If lMsErroAuto
 MostraErro()
 Else
 ConOut("Título incluído com sucesso!")
 Endif

RESET ENVIRONMENT

Return
```
