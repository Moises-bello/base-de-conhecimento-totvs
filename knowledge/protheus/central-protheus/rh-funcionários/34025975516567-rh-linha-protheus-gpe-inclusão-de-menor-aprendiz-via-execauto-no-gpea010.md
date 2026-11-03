---
article_id: 34025975516567
category: RH - Funcionários
content_hash: b36136de10d652076c207bca968202ad266cb2556bb4cd2e454cbf749ee0d04d
fetched_at: '2026-06-28T22:43:28.539513+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Inclusão de Menor Aprendiz via Execauto no GPEA010
type: support-article
updated_at: '2025-08-07T20:37:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34025975516567-RH-Linha-Protheus-GPE-Inclus%C3%A3o-de-Menor-Aprendiz-via-Execauto-no-GPEA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34025975501975) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar a inclusão de **Menor Aprendiz** via Execauto no GPEA010?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Solução**  
Através deste ***Execauto***, é possível automatizar a entrada de dados na tabela **SRA - Cadastro de Funcionários e RU2 - Informações Complementares Menor Aprendiz.**  
  
Na chamada da rotina **GPEA010** deve ser informado um *array*, por exemplo: aCabec, que irá corresponder aos dados da tabela SRA.

**Sintaxe:**  
                   {  
                   {"RA\_FILIAL" , conteudo1, NIL},;  
                   {"RA\_MAT" , conteudo2, NIL};  
                   {campoAdicional3 , conteudo3, Nil},;  
                   {campoAdicional4 , conteudo4 Nil};  
                   }

É importante realizar uma **análise cuidadosa** na passagem dos campos e de seus conteúdos, não somente informar os campos obrigatórios, mas também fornecer campos adicionais que podem ser necessários devido a regra de negócio envolvida.  
  
Pelo fato da rotina GPEA010 ser um fonte em **MVC**, para informar os dados da tabela **RU2** usaremos o modelo de dados **RU2MASTER.**  
  
Processos que podem ser executados pelo ***Execauto:***  
**> nOpc =** 3 - Inclusão  
**> nOpc =** 4 - Alteração  
  
  
**Exemplo de inclusão:**

```
#INCLUDE "Protheus.CH"

User Function GP010APRENDIZ()
Local aCabec        := {}                                                   
Private lMsErroAuto := .F.

//### APRENDIZ ######################################### 
aCabec   := {}
aadd(aCabec,{"RA_FILIAL"        ,"M SP 01 "                         ,Nil        })
aadd(aCabec,{"RA_MAT"           ,"000076"                           ,Nil        })
aadd(aCabec,{'RA_NOME'          ,'FUNCIONARIO EXECAUTO APRENDIZ'    ,Nil        })
aadd(aCabec,{'RA_SEXO'          ,'F'                                ,Nil        })
aadd(aCabec,{'RA_RACACOR'       ,'2'                                ,Nil        })
aadd(aCabec,{'RA_ESTCIVI'       ,'S'                                ,Nil        })
aadd(aCabec,{'RA_CPAISOR'       ,'01058'                            ,Nil        })
aadd(aCabec,{'RA_NATURAL'       ,'SP'                               ,Nil        })
aadd(aCabec,{'RA_NACIONA'       ,'10'                               ,Nil        })
aadd(aCabec,{'RA_ADMISSA'       ,Stod('20250807')                   ,Nil        })
aadd(aCabec,{'RA_NACIONC'       ,'01058'                            ,Nil        })
aadd(aCabec,{'RA_NCODMUNN'      ,'50308'                            ,Nil        })
aadd(aCabec,{'RA_GRINRAI'       ,'45'                               ,Nil        })
aadd(aCabec,{'RA_NASC'          ,Stod('20000101')                   ,Nil        })
aadd(aCabec,{'RA_CC'            ,'01'                               ,Nil        })
aadd(aCabec,{'RA_OPCAO'         ,Stod('20250807')                   ,Nil        })
aadd(aCabec,{'RA_BCDPFGT'       ,'34100'                            ,Nil        })
aadd(aCabec,{'RA_CTDPFGT'       ,'222285'                           ,Nil        })
aadd(aCabec,{'RA_HRSMES'        ,180                                ,Nil        })
aadd(aCabec,{'RA_PROCES'        ,'00017'                            ,Nil        })
aadd(aCabec,{'RA_HRSEMAN'       ,36                                 ,Nil        })
aadd(aCabec,{'RA_CODFUNC'       ,'01'                               ,Nil        })
aadd(aCabec,{'RA_CATFUNC'       ,'E'                                ,Nil        })
aadd(aCabec,{'RA_TIPOPGT'       ,'M'                                ,Nil        })
aadd(aCabec,{'RA_TIPOADM'       ,'3A'                               ,Nil        })
aadd(aCabec,{'RA_VIEMRAI'       ,'55'                               ,Nil        })
aadd(aCabec,{'RA_HOPARC'        ,'1'                                ,Nil        })
aadd(aCabec,{'RA_COMPSAB'       ,'1'                                ,Nil        })
aadd(aCabec,{'RA_CIC'           ,'36054574019'                      ,Nil        })
aadd(aCabec,{'RA_TNOTRAB'       ,'01'                               ,Nil        })
aadd(aCabec,{'RA_REGRA'         ,'01'                               ,Nil        })
aadd(aCabec,{'RA_SEQTURN'       ,'01'                               ,Nil        })
aadd(aCabec,{'RA_CATEG'         ,'07'                               ,Nil        })
aadd(aCabec,{'RA_CATEFD'        ,'103'                              ,Nil        })
aadd(aCabec,{'RA_TPCONTR'       ,'2'                                ,Nil        })
aadd(aCabec,{'RA_DTFIMCT'       ,Stod('20260806')                   ,Nil        })
aadd(aCabec,{'RA_CLAURES'       ,'2'                                ,Nil        })
aadd(aCabec,{'RA_TIPENDE'       ,'2'                                ,Nil        })
aadd(aCabec,{'RA_LOGRTP'        ,'R'                                ,Nil        })
aadd(aCabec,{'RA_LOGRDSC'       ,'TESTE'                            ,Nil        })
aadd(aCabec,{'RA_NUMENDE'       ,'100'                              ,Nil        })
aadd(aCabec,{'RA_BAIRRO'        ,'JD TESTE'                         ,Nil        })
aadd(aCabec,{'RA_ESTADO'        ,'SP'                               ,Nil        })
aadd(aCabec,{'RA_CODMUN'        ,'50308'                            ,Nil        })
aadd(aCabec,{'RA_CEP'           ,'01000000'                         ,Nil        })
aadd(aCabec,{'RA_ADTPOSE'       ,'***N**'                           ,Nil        })


// Grava dados do APRENDIZ
U_Envia(aCabec)

// Grava dados das INF. APRENDIZ
U_GP945AUT(aCabec)

Return(.T.)

/*------------------------------------------------------------------------
GRAVACAO DO MENOR APRENDIZ
------------------------------------------------------------------------*/
USER Function Envia(aCabec)

// Faz a chamada da rotina de cadastro de funcionários (opção 3 - Inclusão) 
MSExecAuto({|x,y,k,w| GPEA010(x,y,k,w)},NIL,NIL,aCabec,3)  

If !lMsErroAuto 
    Conout("Dados de funcionario incluido com sucesso!")    
Else
    MostraErro()
EndIf

Return(.T.)

/*------------------------------------------------------------------------
GRAVACAO DAS INFORMACOES COMPLEMENTARES MENOR APRENDIZ
------------------------------------------------------------------------*/
User Function GP945AUT(aCabec)
Local aErro         := {}
Local cArqErrAuto   := ""
Local oModel        := Nil
Local lRet          := .T.

oModel := FwLoadModel("GPEA945")
oModel:SetOperation(3)
oModel:Activate()

oModel:LoadValue("SRATITLE" , "RA_MAT"      , aCabec[2][2] )
oModel:LoadValue("SRATITLE" , "RA_NOME"     , aCabec[3][2])
oModel:LoadValue("SRATITLE" , "RA_ADMISSA"  , aCabec[10][2])

oModel:SetValue("RU2MASTER","RU2_FILIAL"    ,aCabec[1][2])
oModel:SetValue("RU2MASTER","RU2_MAT"       ,aCabec[2][2])
oModel:SetValue("RU2MASTER","RU2_INDMOD"     ,"2")
oModel:SetValue("RU2MASTER","RU2_TPINSC"     ,"1")
oModel:SetValue("RU2MASTER","RU2_NUMINS"     ,"48433758000140")


If oModel:VldData()
    oModel:CommitData()
    conout("Dados de INF. Compl. Menor Aprendiz incluidos com sucesso!!")
Else
    aErro := oModel:GetErrorMessage()

    cArqErrAuto := "Id do formulario de origem:"+ ' [' + AllToChar( aErro[1] ) + ']' + Chr(13) + Chr(10)
    cArqErrAuto += "Id do campo de origem: " + ' [' + AllToChar( aErro[2] ) + ']' + Chr(13) + Chr(10)
    cArqErrAuto += "Id do formulario de erro: " + ' [' + AllToChar( aErro[3] ) + ']' + Chr(13) + Chr(10)
    cArqErrAuto += "Id do campo de erro: " + ' [' + AllToChar( aErro[4] ) + ']' + Chr(13) + Chr(10)
    cArqErrAuto += "Id do erro: " + ' [' + AllToChar( aErro[5] ) + ']' + Chr(13) + Chr(10)
    cArqErrAuto += "Mensagem do erro: " + ' [' + AllToChar( aErro[6] ) + ']' + Chr(13) + Chr(10)
    cArqErrAuto += "Mensagem da solucao: " + ' [' + AllToChar( aErro[7] ) + ']' + Chr(13) + Chr(10)
    cArqErrAuto += "Valor atribuido: " + ' [' + AllToChar( aErro[8] ) + ']' + Chr(13) + Chr(10)
    cArqErrAuto += "Valor anterior: " + ' [' + AllToChar( aErro[9] ) + ']' + Chr(13) + Chr(10)

    Alert ('Falha no ExecAuto MVC: ' + (Chr(13) + Chr(10)) + cArqErrAuto)

EndIf

oModel:DeActivate()
oModel:Destroy()
oModel := NIL

Return(.T.)
```

**Importante:**  
Para alterar o campo **Nome (RA\_NOME)**, é necessário definir um **índice da tabela SRA** que será utilizado para passagem no *array* aCabec. Para mais informações, **acesse este** [***link.***](https://tdn.totvs.com/pages/releaseview.action?pageId=623874806)

Para que seja possível gravar o **valor de salário (RA\_SALARIO)** passado no fonte do *Execauto*, é necessário que o parâmetro **MV\_ALTSAL esteja com conteúdo N**, caso contrário, o sistema por padrão utiliza o salário informado no cadastro da Função vinculada ao Funcionário.  
  
  
**Saiba Mais:**  
[RH - Linha Protheus - GPE - Inclusão ou alteração de Funcionário via Execauto no GPEA010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8864723361943-RH-Linha-Protheus-GPE-Inclus%C3%A3o-ou-altera%C3%A7%C3%A3o-de-Funcion%C3%A1rio-via-Execauto-no-GPEA010)  
[Execauto de Inclusão - Estagiário](https://tdn.totvs.com/pages/viewpage.action?pageId=623875647)
