---
article_id: 29540808684951
category: Financeiro - Baixas a Receber
content_hash: 574b8316dd6da34c3697644e49c4a52158a31e7d55f9890cf2bf3fa369c5b511
fetched_at: '2026-06-28T22:37:43.760185+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus- SIGAFIN - Exemplo ExecAuto
  FINA070
type: support-article
updated_at: '2026-04-02T11:55:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29540808684951-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Exemplo-ExecAuto-FINA070
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29540792488983)Tempo aproximado para leitura:**00:07:00 min**

**Dúvida**  
Como baixar títulos no contas a receber pelo ExecAuto FINA070  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus – Financeiro – A partir da versão 12.1.17  
  
**Solução:**  
  
Parâmetros utilizados na rotina:

* **xAutoCab**  
  Permite informar um array com os dados do título a ser baixado, incluindo informações necessárias para a baixa, como data da baixa, data de crédito, entre outros.
* **nOpc**  
  Define a operação que será realizada na rotina.   
  3: Baixa de título  
  5: Cancelamento de baixa  
  6: Exclusão de baixa
* **lNoMbrowse**  
  Variável lógica que indica se o browse da rotina FINA070 será exibido ou não.
* **nOpBaixa**  
  Determina qual baixa (ou cancelamento de baixa) será executado.  
  Exemplo:  
  Se um título foi baixado em duas ou mais baixas parciais, este parâmetro permite indicar exatamente qual delas será cancelada.  
    
  **Observação importante:**  
  Esse parâmetro não segue a sequência original gravada na tabela SE5. Ou seja, ao cancelar uma baixa intermediária, a sequência é reorganizada automaticamente.
* **cFiltro**  
  Permite aplicar um filtro nos títulos apresentados no MBrowse.

Observação adicional sobre valores no array

Caso os campos abaixo sejam informados com valor zero no array da rotina automática, é necessário que o 4º elemento (lógico) seja definido como .T., para que o sistema considere o valor informado.

Se esse 4º elemento não for informado, o sistema assume os valores padrão:

AUTJUROS  
AUTMULTA  
AUTDESCONT  
AUTCM1  
AUTPRORATA

**Segue exemplo da rotina automática execauto FINA070**

```
#INCLUDE "Protheus.ch"
 
//-------------------------------
// Baixa do titulo a receber
//-------------------------------
 
User Function BAIXA070()
  
    Local aBaixa := {}
  
    aBaixa := {{"E1_PREFIXO"  ,"   "                ,Nil    },;
            {"E1_NUM"      ,"200      "            ,Nil    },;
            {"E1_PARCELA"  ," "                    ,Nil    },;
            {"E1_TIPO"     ,"NF "                  ,Nil    },;
            {"AUTMOTBX"    ,"NOR"                  ,Nil    },;
            {"AUTBANCO"    ,"001"                  ,Nil    },;
            {"AUTAGENCIA"  ,"00001"                ,Nil    },;
            {"AUTCONTA"    ,"0000000001"           ,Nil    },;
            {"AUTDTBAIXA"  ,dDataBase              ,Nil    },;
            {"AUTDTCREDITO",dDataBase              ,Nil    },;
            {"AUTHIST"     ,"BAIXA TESTE"          ,Nil    },;
            {"AUTJUROS"    ,0                      ,Nil,.T.},;
            {"AUTVALREC"   ,700                    ,Nil    }}
  
    MSExecAuto({|x,y| Fina070(x,y)},aBaixa,3)
  
Return
 
//-------------------------------
// Cancelamento da baixa do titulo a receber
//-------------------------------
User Function CANC070()
  
    Local aBaixa := {}
     
    aBaixa := {{"E1_PREFIXO"  ,"   "                ,Nil    },;
            {"E1_NUM"      ,"200      "            ,Nil    },;
            {"E1_PARCELA"  ," "                    ,Nil    },;
            {"E1_TIPO"     ,"NF "                  ,Nil    },;
            {"AUTMOTBX"    ,"NOR"                  ,Nil    },;
            {"AUTBANCO"    ,"001"                  ,Nil    },;
            {"AUTAGENCIA"  ,"00001"                ,Nil    },;
            {"AUTCONTA"    ,"0000000001"           ,Nil    },;
            {"AUTDTBAIXA"  ,dDataBase              ,Nil    },;
            {"AUTDTCREDITO",dDataBase              ,Nil    },;
            {"AUTHIST"     ,"BAIXA TESTE"          ,Nil    },;
            {"AUTJUROS"    ,0                      ,Nil,.T.},;
            {"AUTVALREC"   ,700                    ,Nil    }}
  
    MSExecAuto({|x,y| Fina070(x,y)},aBaixa,5)
  
Return
```

**Exemplo de rotina automática com rateio de múltiplas naturezas**

```
#INCLUDE "Protheus.ch"
 
//--------------------------------------------------
// Para correto funcionamento o parâmetro MV_MULNATR
// deve estar igual a .T.
//---------------------------------------------------
 
//-------------------------------------------------------------
// Neste exemplo é utilizada uma natureza e um centro de custo
//--------------------------------------------------------------
 
User Function EXEC070()
  
    Local aBaixa := {}
  
    aBaixa := {{"E1_PREFIXO"  ,"   "                ,Nil    },;
            {"E1_NUM"      ,"200      "            ,Nil    },;
            {"E1_PARCELA"  ," "                    ,Nil    },;
            {"E1_TIPO"     ,"NF "                  ,Nil    },;
            {"AUTMOTBX"    ,"NOR"                  ,Nil    },;
            {"AUTBANCO"    ,"001"                  ,Nil    },;
            {"AUTAGENCIA"  ,"00001"                ,Nil    },;
            {"AUTCONTA"    ,"0000000001"           ,Nil    },;
            {"AUTDTBAIXA"  ,dDataBase              ,Nil    },;
            {"AUTDTCREDITO",dDataBase              ,Nil    },;
            {"AUTHIST"     ,"BAIXA TESTE"          ,Nil    },;
            {"AUTJUROS"    ,0                      ,Nil,.T.},;
            {"AUTVALREC"   ,500                    ,Nil    }}
  
    //Adicionando o vetor da natureza
    Aadd(aAuxEv,{"EV_NATUREZ","EASY", NIL }) //Natureza a Ratear
    Aadd(aAuxEv,{"EV_VALOR", 500, NIL }) //Valor do Rateio na Natureza
    Aadd(aAuxEv,{"EV_PERC", 100, NIL }) //Percentual do Rateio na Natureza
    Aadd(aAuxEv,{"EV_RATEICC", "1", NIL }) //Rateio por Centro de Custo == 1 - Sim
 
    //Adicionando Múltiplos Centros de Custo
    //Primeiro Centro de Custo
    aAuxEz := {}
    Aadd( aAuxEz,{"EZ_CCUSTO", "000001   ", NIL}) //Centro de Custo da Natureza
    Aadd( aAuxEz, {"EZ_VALOR", 500, NIL}) //Valor do Rateio neste Centro de Custo
    Aadd(aRatEz, aAuxEz)
    Aadd(aAuxEv,{"AUTRATEICC", aRatEz, NIL}) //Recebendo dentro do Array da Natureza os Multiplos Centros de Custo
     
    Aadd(aRatEvEz,aAuxEv) //Adicionando a Natureza ao Rateio de Multiplas Naturezas
     
    MSExecAuto({|x,y,z| Fina070(x,y,,,,,,,z)},aBaixa,3,aRatEvEz)
     
    If lMsErroAuto
        MostraErro()
    Else
        MsgAlert("Baixa realizada com sucesso!")
    EndIf
  
Return
```

**Exemplo de rotina automática de título em outra moeda informando a taxa no momento da baixa**

```
#INCLUDE "Protheus.ch"
 
//-------------------------------
// Baixa do titulo a receber
//-------------------------------
 
User Function BAIXA070()
  
    Local aBaixa := {}
  
    aBaixa := {{"E1_PREFIXO"  ,"   "                ,Nil    },;
            {"E1_NUM"      ,"200      "            ,Nil    },;
            {"E1_PARCELA"  ," "                    ,Nil    },;
            {"E1_TIPO"     ,"NF "                  ,Nil    },;
            {"AUTMOTBX"    ,"NOR"                  ,Nil    },;
            {"AUTBANCO"    ,"001"                  ,Nil    },;
            {"AUTAGENCIA"  ,"00001"                ,Nil    },;
            {"AUTCONTA"    ,"0000000001"           ,Nil    },;
            {"AUTDTBAIXA"  ,dDataBase              ,Nil    },;
            {"AUTDTCREDITO",dDataBase              ,Nil    },;
            {"AUTHIST"     ,"BAIXA TESTE"          ,Nil    },;
            {"AUTJUROS"    ,0                      ,Nil,.T.},;
            {"AUTTXMOEDA"  ,5.0000                 ,Nil    }}
  
    MSExecAuto({|x,y| Fina070(x,y)},aBaixa,3)
  
Return
```

**Exemplo de rotina automática de baixas a receber com desconto**

```
#INCLUDE "Protheus.ch"
 
//-------------------------------
// Baixa do titulo a receber.
// Título no valor de R$1.000,00 com desconto de R$100,00.
//-------------------------------
 
User Function BAIXA070()
 
    // Para este exemplo foi utilizado a variável AUTDESCONT,
    // caso seja necessário aplicar decréscimo a baixa do título 
    // basta alterar a variável para AUTDECRESC, ambas variáveis
    // possuem o mesmo efeito de cálculo.
  
    Local aBaixa := {}
  
    aBaixa := {{"E1_PREFIXO"  ,"TST"                ,Nil    },;
            {"E1_NUM"      ,"TSTDESC  "            ,Nil    },;
            {"E1_PARCELA"  ," "                    ,Nil    },;
            {"E1_TIPO"     ,"NF "                  ,Nil    },;
            {"AUTMOTBX"    ,"NOR"                  ,Nil    },;
            {"AUTBANCO"    ,"001"                  ,Nil    },;
            {"AUTAGENCIA"  ,"00001"                ,Nil    },;
            {"AUTCONTA"    ,"0000000001"           ,Nil    },;
            {"AUTDTBAIXA"  ,dDataBase              ,Nil    },;
            {"AUTDTCREDITO",dDataBase              ,Nil    },;
            {"AUTDESCONT"  ,100                    ,Nil    },;
            {"AUTVALREC"   ,900                    ,Nil    }}    
 
    MSExecAuto({|x,y| Fina070(x,y)},aBaixa,3)
  
Return
```

**Saiba mais**

[Execução das operações automáticas de baixas a receber - FINA070](https://tdn.totvs.com/pages/releaseview.action?pageId=568947413)
