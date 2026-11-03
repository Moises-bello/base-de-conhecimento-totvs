---
article_id: 33668988094103
category: Financeiro - Contas a Receber
content_hash: 95610f5408946697fc2dcc871065faf60cf104df7583c15b7d706d72636a820a
fetched_at: '2026-06-28T22:38:12.599528+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA060 - Como configurar o ExecAuto
  para a rotina de Transferência de Títulos (FINA060)
type: support-article
updated_at: '2026-03-25T12:43:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33668988094103-Cross-Segmentos-Backoffice-Linha-Protheus-FINA060-Como-configurar-o-ExecAuto-para-a-rotina-de-Transfer%C3%AAncia-de-T%C3%ADtulos-FINA060
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33668966151063) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Como configurar o ExecAuto para a rotina de Transferência de Títulos (FINA060)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões   
  
**Solução**  
Parâmetros para a inclusão de borderô por rotina automática FINA060:

| **Parâmetro 1** | Numérico | nOpcAuto - 3 Inclusão de borderô. |
| --- | --- | --- |
| **Parâmetro 2** | Array | Array com 2 dimensões, sendo a primeira um array com informações do borderô e a segunda um array com os títulos. |

Estrutura do array com informações do borderô:

| AUTBANCO | Caracter | Código do banco. |
| --- | --- | --- |
| AUTAGENCIA | Caracter | Código da agência. |
| AUTCONTA | Caracter | Código da conta. |
| AUTSITUACA | Caracter | Situação a ser transferida o título. |
| AUTNUMBOR | Caracter | Número do borderô. |
| AUTDATAMOV | Data | Data do movimento. |
| AUTTXDESC | Numérico | Taxa de desconto para carteira descontada. |
| AUTTXIOF | Numérico | Taxa de IOF para carteira descontada. |
| AUTSUBCONTA | Caracter | Número da subconta do banco |
| AUTESPECIE | Caracter | Código da espécie do pagamento (contida na tabela F77) |
| AUTBOLAPI | Logico | Define se o borderô em questão será transmitido via API (Boletos) |

Estrutura do array com informações dos títulos ( chave de busca para o índice 1 ) :

| E1\_FILIAL | Caracter | Filial do título |
| --- | --- | --- |
| E1\_PREFIXO | Caracter | Prefixo do título. |
| E1\_NUM | Caracter | Número do título. |
| E1\_PARCELA | Caracter | Parcela do título. |
| E1\_TIPO | Caracter | Tipo do do título. |

Exemplo:

User function AUTO060BOR()

Local cTmp := "TMPBOR"  
Local cFiltro := ""  
Local aTit := {}  
Local aBor := {}

Local cBanco := "001"  
Local cAgencia := "001"  
Local cConta := "001"

Local cSituaca := "1"  
Local cNumBor := ""  
Local dDataMov := ""

Local cEspecie := '99'

Local cSubconta := '001'

//-- Variáveis utilizadas para o controle de erro da rotina automática  
Local aErroAuto :={}  
Local cErroRet :=""  
Local nCntErr :=0  
Private lMsErroAuto := .F.  
Private lMsHelpAuto := .T.  
Private lAutoErrNoFile := .T.

PREPARE ENVIRONMENT EMPRESA "XX" FILIAL "XX " USER "admin"

dDataMov := Ctod("19/04/2019")

// Filtro SQL para para adicionar os titulos no borderô  
cFiltro := "%"+"E1\_PREFIXO = 'BOR' AND E1\_TIPO ='NF'"+"%"

If Select( cTmp ) > 0

(cTmp)->( dbCloseArea() )

EndIf

BeginSQL Alias cTmp

SELECT

E1\_FILIAL,  
E1\_PREFIXO,  
E1\_NUM,  
E1\_PARCELA,  
E1\_TIPO

FROM

%table:SE1%

WHERE

%exp:cFiltro%  
AND E1\_SALDO > 0  
AND %NotDel%

EndSQL

//Adiciona os títulos no array  
While (cTmp)→(!EOF())

aAdd(aTit,;  
{;

{"E1\_FILIAL" ,(cTmp)->E1\_FILIAL },;  
{"E1\_PREFIXO" ,(cTmp)->E1\_PREFIXO },;  
{"E1\_NUM" ,(cTmp)->E1\_NUM },;  
{"E1\_PARCELA" ,(cTmp)->E1\_PARCELA },;  
{"E1\_TIPO" ,(cTmp)->E1\_TIPO };

})  
(cTmp)→(dbSkip())

EndDo

(cTmp)->(dbCloseArea()) //Fecho a tabela temporária

If Empty(aTit) .OR. cSituaca == "0" //Caso não encontre títulos ou situação 0 deve sair da rotina.

RETURN(.F.)

EndIf

//Informações bacárias para o borderô  
aAdd(aBor, {"AUTBANCO" , PadR(cBanco ,TamSX3("A6\_COD")[1]) })  
aAdd(aBor, {"AUTAGENCIA" , PadR(cAgencia ,TamSX3("A6\_AGENCIA")[1]) })  
aAdd(aBor, {"AUTCONTA" , PadR(cConta ,TamSX3("A6\_NUMCON")[1]) })  
aAdd(aBor, {"AUTSITUACA" , PadR(cSituaca ,TamSX3("E1\_SITUACA")[1]) })  
aAdd(aBor, {"AUTNUMBOR" , PadR(cNumBor ,TamSX3("E1\_NUMBOR")[1]) }) // Caso não seja passado o número será obtido o próximo pelo padrão do sistema  
aAdd(aBor, {"AUTSUBCONTA" , PadR(cSubconta,TamSX3("EA\_SUBCTA")[1]) })  
aAdd(aBor, {"AUTESPECIE" , PadR(cEspecie,TamSX3("EA\_ESPECIE")[1]) })

If cSituaca $ "2|7" // Carteira descontada deve ser informada as taxas e data do movimento

aAdd(aBor, {"AUTTXDESC" ,10})  
aAdd(aBor, {"AUTTXIOF" ,5})  
aAdd(aBor, {"AUTDATAMOV" ,dDataMov})

EndIf

MSExecAuto({|a, b| FINA060(a, b)}, 3,{aBor,aTit})

If lMsErroAuto

aErroAuto := GetAutoGRLog()  
For nCntErr := 1 To Len(aErroAuto)

cErroRet += aErroAuto[nCntErr]

Next

Conout(cErroRet)

EndIf

Return

**Saiba mais**

[FIN0084 - DT Rotina automática FINA060 - Inclusão de borderô](https://tdn.totvs.com/pages/releaseview.action?pageId=485450320)
