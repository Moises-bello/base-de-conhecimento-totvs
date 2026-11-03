---
article_id: 360018845811
category: Ativo Fixo - Ponto de entrada, Customizações, Funções, Execauto
content_hash: 2805ffc80246e51b574867b596c01a9a8229ebce184096c60adec1c25acfd4b6
fetched_at: '2026-06-28T22:41:39.082082+00:00'
product: protheus
section_id: 1500001536601
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF:  Exemplo de Execauto
  (Rotina Automática) - Transferência do Ativos'
type: support-article
updated_at: '2025-04-10T12:27:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018845811-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Exemplo-de-Execauto-Rotina-Autom%C3%A1tica-Transfer%C3%AAncia-do-Ativos
---

**Dúvida**Exemplo de Execauto (Rotina Automática) - Transferência do Ativos

**Ambiente**Protheus – Ativo Fixo – A partir da versão 11.80  
renan   
**Solução**

```
User Function MyATFA060() 
 
Local aDadosAuto    := {}  // Array com os dados a serem enviados pela MsExecAuto() para gravação automática. 
Local aParamAuto    := {} 
Private lMsHelpAuto := .F. // Determina se as mensagens de help devem ser direcionadas para o arq. de log. 
Private lMsErroAuto := .F. // Determina se houve alguma inconsistência na execução da rotina em relação aos parâmetros informados 
 
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿ 
//³ O exemplo abaixo foi considerado passando somente dados de conta contábil e centro de custo, caso ³ 
//³ necessário passar os campos referentes a itens contábeis e classes de valores. ³ 
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ   
  
dDatabase := cTod("08/02/2010")   

aDadosAuto:= { {'N3_FILIAL'  ,ALLTRIM(xfilial("SN3")),Nil},; // Código da filial 
               {'N3_CBASE'   , "0000000002"          , Nil},; // Código base do ativo 
               {'N3_ITEM'    , "0001"                , Nil},; // Item sequencial do código base do ativo   
               {'N3_TIPO'    , "10" , Nil},; // Tipo do Ativo  
               {'N4_DATA'    , dDatabase             , Nil},; // Data de aquisição do ativo 
               {'N3_CCUSTO'  , "123"                 , Nil},; // Centro de Custo de Despesa 
               {'N3_CCONTAB' , "123"                 , Nil},; // Conta Contábil 
               {'N3_CCORREC' , "123"                 , Nil},; // Conta de Correção do Bem 
               {'N3_CDEPREC' , "123"                 , Nil},; // Conta Despesa Depreciação 
               {'N3_CCDEPR'  , "123"                 , Nil},; // Conta Depreciação Acumulada 
               {'N3_CDESP'   , "123"                 , Nil},; // Conta Correção Depreciação 
               {'N3_CUSTBEM' , "123"                 , Nil},; // Centro de Custo da Conta do Bem 
               {'N3_CCCORR'  , "123"                 , Nil},; // Centro Custo Correção Monetária 
               {'N3_CCDESP'  , "123"                 , Nil},; // Centro Custo Despesa Depreciação 
               {'N3_CCCDEP'  , "123"                 , Nil},; // Centro Custo Despesa Acumulada 
               {'N3_CCCDES'  , "123"                 , Nil},; // Centro Custo Correção Depreciação 
               {'N1_GRUPO'   , "GR01"                , Nil},; // Código do Grupo do Bem 
               {'N1_LOCAL'   , "LOCAL"               , Nil},; // Localização do Bem 
               {'N1_NFISCAL' , "NF001"               , Nil},; // Número da NF 
               {'N1_NSERIE'  , "SERIE"               , Nil},; // Série da NF 
               {'N1_TAXAPAD' , "999999"              , Nil}}  // Código da Taxa Padrão     
               {'TPN_CTRAB'  , "CT01  "              , Nil},; // Centro de Trabalho do Bem, utilizado somente quando integrado ao SIGAMNT 
               {'TPN_POSCON' , "150"                 , Nil},; // Primeiro Contador do Bem, utilizado somente quando integrado ao SIGAMNT 
               {'TPN_POSCO2' , "100"                 , Nil}}  // Segundo Contador do Bem, utilizado somente quando integrado ao SIGAMNT   

 
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿ 
//³ Caso deseje passar valores para os campos, Grupo, Local, NF/Série Taxa padrão, considerar ³ 
//³ como no exemplo acima utilizando os campos correspondentes da tabela SN1. ³ 
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ 

// Parâmetros das perguntas da rotina atfa060 
aAdd( aParamAuto, {"MV_PAR01", 1} ) //Pergunta 01 - Contabiliza ? 1 = Sim ; 2 = Não 
aAdd( aParamAuto, {"MV_PAR02", 2} ) //Pergunta 02 - Mostra Lanc Contab ? 1 = Sim ; 2 = Não 
aAdd( aParamAuto, {"MV_PAR03", 2} ) //Pergunta 02 - Aglut Lançamentos ? 1 = Sim ; 2 = Não 
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿   
// O quarto parâmetro pode ser configurado com os seguintes estados.  
//.T. = Espelhar.   
//.F. = Atualizar.   
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ 
MSExecAuto({|x, y, w, z| AtfA060(x, y, w, z)},aDadosAuto, 4 ,, .F.) 
 
If lMsErroAuto 
    lRetorno := .F. 
    MostraErro() 
Else 
    lRetorno:=.T. 
EndIf 
 
Return
```

**Importante**

Na **transferência contábil**, deverá ser feito a chamada do Execauto de cada tipo de ativo separado, pois a execução automática é preparada para realizar a transferência de um tipo de ativo por vez.

---

**TRANSFERENCIA FÍSICA**

```
#Include 'Protheus.ch'
#Include 'Protheus.ch'
#Include 'tbiconn.ch'

User Function MyATFA060()
Local   aDadosAuto  := {}   // Array com os dados á serem enviados pela MsExecAuto() para gravação automática.
Private lMsHelpAuto := .F.  // Determina se as mensagens de help devem ser direcionadas para o arq. de log.
Private lMsErroAuto := .F.   // Determina se houve alguma inconsistência na execução da rotina em relação aos

//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿
//³ O exemplo abaixo foi considerado passando somente dados de conta contabil e centro de custo, caso ³
//³ necessário passar os campos referentes a itens contábeis e classes de valores.                    ³
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ   
  
dDatabase := cTod("08/02/2010")  

aDadosAuto:= {{'N3_CBASE'        , "TRANSF    "           , Nil},;    // Código base do ativo
               {'N3_ITEM'        , "001 "                 , Nil},;    // Item sequencial do código bas do ativo  
               {'N3_TIPO'    , "10"                       , Nil},; // Tipo do Ativo    
               {'N1_FILIAL'      , "D MG 02 "             , Nil},;    // Filial de Destino do Ativo
               {'N4_DATA'        , dDatabase              , Nil},;    // Data de aquisição do ativo
               {'N3_CCUSTO'      , "         "            , Nil},;    // Centro de Custo de Despesa
               {'N3_CCONTAB'     , "101010100           " , Nil},;    // Conta Contabil
               {'N3_CCORREC'     , "                    " , Nil},;    // Conta de Correcao do Bem
               {'N3_CDEPREC'     , "201010100           " , Nil},;    // Conta Despesa Depreciação
               {'N3_CCDEPR'      , "101010300           " , Nil},;    // Conta Depreciação Acumulada
               {'N3_CDESP'       , "                    " , Nil},;    // Conta Correção Depreciação
               {'N3_CUSTBEM'     , "         "            , Nil},;    // Centro de Custo da Conta do Bem
               {'N3_CCCORR'      , "         "            , Nil},;    // Centro Custo Correção Monetária
               {'N3_CCDESP'      , "         "            , Nil},;    // Centro Custo Despesa Depreciação
               {'N3_CCCDEP'      , "         "            , Nil},;    // Centro Custo Despesa Acumulada
               {'N3_CCCDES'      , "         "            , Nil},;    // Centro Custo Correção Depreciacão
               {'N1_GRUPO'       , "    "                 , Nil},;    // Código do Grupo do Bem
               {'N1_LOCAL'       , "      "               , Nil},;    // Localizacao do Bem
               {'N1_NFISCAL'     , "         "            , Nil},;    // Numero da NF
               {'N1_NSERIE'      , "         "            , Nil},;    // Serie da NF
               {'N1_TAXAPAD'     , "      "               , Nil}}     // Codigo da Taxa Padrao
               
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿
//³ Caso deseje passar valores para os campos, Grupo, Local, NF/Serie Taxa padrao, considerar ³
//³ como no exemplo acima utilizando os campos correspondentes da tabela SN1.                 ³
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿   
// O quarto parâmetro pode ser configurado com os seguintes estados.  
//.T. = Espelhar.   
//.F. = Atualizar.   
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ   

MSExecAuto({|x, y, w, z| AtfA060(x, y, w, z)},aDadosAuto, 4, aParamAuto , .F.)

If lMsErroAuto    
    lRetorno := .F.    
    MostraErro()
Else    
    lRetorno:=.T.
EndIf

Return
```

Saiba mais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=200902359>
