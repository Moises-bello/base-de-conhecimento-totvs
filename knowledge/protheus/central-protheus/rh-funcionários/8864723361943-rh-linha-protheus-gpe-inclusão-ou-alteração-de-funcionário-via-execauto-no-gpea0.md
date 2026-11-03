---
article_id: 8864723361943
category: RH - Funcionários
content_hash: 0cb0ff968c10c67dba68258c17c64dc790ad64d81499f60e2f6caebeca838cc1
fetched_at: '2026-06-28T22:43:28.577820+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Inclusão ou alteração de Funcionário via Execauto
  no GPEA010
type: support-article
updated_at: '2026-06-12T11:06:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8864723361943-RH-Linha-Protheus-GPE-Inclus%C3%A3o-ou-altera%C3%A7%C3%A3o-de-Funcion%C3%A1rio-via-Execauto-no-GPEA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23378220237079) Tempo aproximado para leitura: **00:03:00**  
  
**Dúvida**  
Como realizar a inclusão ou alteração de Funcionário via ***Execauto*** no GPEA010?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Solução**  
Através da execução deste ***Execauto**,* é possível automatizar a entrada de dados na tabela **SRA - Cadastro de Funcionários.**  
Na chamada da rotina GPEA010, deve ser informado um *array*, por exemplo: **aCabec,** que irá corresponder aos dados da tabela **SRA.**  
  
**Sintaxe:**

                    { {"RA\_FILIAL" , conteudo1, NIL},;  
                    {"RA\_MAT" , conteudo2, NIL};  
                    {campoAdicional3 , conteudo3, Nil},;  
                    {campoAdicional4 , conteudo4 Nil};  
                    } 

É importante realizar uma **análise cuidadosa** na passagem dos campos e de seus conteúdos, não somente informar os campos obrigatórios, mas também **fornecer campos adicionais** que podem ser necessários **devido a regra de negócio envolvida**.  
  
Processos que podem ser executados pelo *Execauto*:  
**> nOpc = 3** - Inclusão  
**> nOpc = 4** - Alteração  
  
**Exemplo de inclusão:**

#INCLUDE "Protheus.CH"  
//Esta rotina tem a finalidade de efetuar o lancamento automatico de funcionarios  
//atraves do mecanismo de rotina automatica.  
//Nesse exemplo, a chamada da funcao U\_GP010AUT deve ser realizada a partir do menu.  
  
User Function GP010AUT()  
  
Local aCabec   := {}  
PRIVATE lMsErroAuto := .F.  
  
//### Primeiro Funcionario ######################################### //  
//-- Inclusao de 1 funcionario da matricula '000009'  
  
aCabec   := {}  
aadd(aCabec,{"RA\_FILIAL"        ,"M SP 01 "                         ,Nil        })  
aadd(aCabec,{"RA\_MAT"           ,"000009"                           ,Nil        })  
aadd(aCabec,{'RA\_NOME'          ,'TESTE EXECAUTO'                   ,Nil        })  
aadd(aCabec,{'RA\_SEXO'          ,'F'                                ,Nil        })  
aadd(aCabec,{'RA\_RACACOR'       ,'2'                                ,Nil        })  
aadd(aCabec,{'RA\_NASC'          ,Stod('19901215')                   ,Nil        })  
aadd(aCabec,{'RA\_ESTCIVI'       ,'S'                                ,Nil        })  
aadd(aCabec,{'RA\_CPAISOR'       ,'01058'                            ,Nil        })  
aadd(aCabec,{'RA\_NACIONA'       ,'10'                               ,Nil        })  
aadd(aCabec,{'RA\_NACIONC'       ,'01058'                            ,Nil        })  
aadd(aCabec,{'RA\_NATURAL'       ,'SP'                               ,Nil        })  
aadd(aCabec,{'RA\_NCODMUNN'      ,'50308'                            ,Nil        })  
aadd(aCabec,{'RA\_GRINRAI'       ,'50'                               ,Nil        })  
aadd(aCabec,{'RA\_CC'            ,'01'                               ,Nil        })  
aadd(aCabec,{'RA\_ADMISSA'       ,Stod('20240102')                   ,Nil        })  
aadd(aCabec,{'RA\_TIPOADM'       ,'9B'                               ,Nil        })  
aadd(aCabec,{'RA\_OPCAO'         ,Stod('20240102')                   ,Nil        })  
aadd(aCabec,{'RA\_BCDPFGT'       ,'34100'                            ,Nil        })  
aadd(aCabec,{'RA\_CTDPFGT'       ,'222285'                           ,Nil        })  
aadd(aCabec,{'RA\_HRSMES'        ,220                                ,Nil        })  
aadd(aCabec,{'RA\_PROCES'        ,'00001'                            ,Nil        })  
aadd(aCabec,{'RA\_CATFUNC'       ,'M'                                ,Nil        })  
aadd(aCabec,{'RA\_HRSEMAN'       ,44                                 ,Nil        })  
aadd(aCabec,{'RA\_CODFUNC'       ,'01'                               ,Nil        })  
aadd(aCabec,{'RA\_HOPARC'        ,'1'                                ,Nil        })  
aadd(aCabec,{'RA\_SINDICA'       ,'01'                               ,Nil        })  
aadd(aCabec,{'RA\_TIPOPGT'       ,'M'                                ,Nil        })  
aadd(aCabec,{'RA\_VIEMRAI'       ,'10'                               ,Nil        })  
aadd(aCabec,{'RA\_CATEFD'        ,'101'                              ,Nil        })  
aadd(aCabec,{'RA\_COMPSAB'       ,'1'                                ,Nil        })  
aadd(aCabec,{'RA\_CIC'           ,'77913603062'                      ,Nil        })  
aadd(aCabec,{'RA\_TNOTRAB'       ,'01'                               ,Nil        })  
aadd(aCabec,{'RA\_REGRA'         ,'01'                               ,Nil        })  
aadd(aCabec,{'RA\_SEQTURN'       ,'01'                               ,Nil        })  
aadd(aCabec,{'RA\_TIPENDE'       ,'2'                                ,Nil        })  
aadd(aCabec,{'RA\_LOGRTP'        ,'R'                                ,Nil        })  
aadd(aCabec,{'RA\_LOGRDSC'       ,'TESTE'                            ,Nil        })  
aadd(aCabec,{'RA\_NUMENDE'       ,'100'                              ,Nil        })  
aadd(aCabec,{'RA\_BAIRRO'        ,'JD TESTE'                         ,Nil        })  
aadd(aCabec,{'RA\_ESTADO'        ,'SP'                               ,Nil        })  
aadd(aCabec,{'RA\_CODMUN'        ,'50308'                            ,Nil        })  
aadd(aCabec,{'RA\_CEP'           ,'01000000'                         ,Nil        })  
aadd(aCabec,{'RA\_ADTPOSE'       ,'\*\*\*N\*\*'                           ,Nil        })  
  
U\_Envia(aCabec)  
  
Return(.T.)  
  
//-- Funcao criada para exemplificar a chamada da execução da rotina de cadastro de funcionarios  
  
USER Function Envia(aCabec)  
  
//-- Faz a chamada da rotina de cadastro de funcionarios (opção 3)   
  
MSExecAuto({|x,y,k,w| GPEA010(x,y,k,w)},NIL,NIL,aCabec,3)  //-- Opcao 3 - Inclusao registro  
  
//-- Retorno de erro na execucao da rotina  
  
If lMsErroAuto   
  
// VALIDAÇÃO DE ERRO NA ROTINA  
If (!lMsErroAuto) // OPERAÇÃO FOI EXECUTADA COM SUCESSO  
    ConOut(PadC("Automatic routine successfully ended", 80))  
Else // OPERAÇÃO EXECUTADA COM ERRO  
    If (!IsBlind()) // COM INTERFACE GRÁFICA  
        MostraErro()  
    Else // EM ESTADO DE JOB  
        cError := MostraErro("/dirdoc", "error.log") // ARMAZENA A MENSAGEM DE ERRO  
  
        ConOut(PadC("Automatic routine ended with error", 80))  
        ConOut("Error: "+ cError)  
    EndIf  
EndIf  
  
/\*\* DEMAIS PROCESSO EXECUTADO PELO FONTE \*\*/  
EndIf  
Return(.T.)

**Importante:**   
Para alterar o campo **Nome (RA\_NOME)**, é necessário definir um índice da tabela SRA que será utilizado para passagem no *array* aCabec. Para mais informações, acesse [**este** ***link.***](https://tdn.totvs.com/pages/releaseview.action?pageId=623874806)  
  
Para que seja possível gravar o valor de **salário (RA\_SALARIO) passado no fonte do** ***Execauto***, é necessário que o parâmetro **MV\_ALTSAL** esteja com conteúdo **N**, caso contrário, o sistema por padrão utiliza o salário informado no cadastro da **Função** vinculada ao Funcionário.  
  
O modelo do *Execauto* desta documentação deve ser usado apenas com o parâmetro **MV\_MATRICU = 0**. Para os demais casos, deve ser seguido o modelo[**desta documentação.**](https://tdn.totvs.com/pages/releaseview.action?pageId=1015569806)  
  
  
**Saiba Mais**  
[RH - Linha Protheus - GPE - Como realizar o cadastro/admissão de Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404568864151-RH-Linha-Protheus-GPE-Como-realizar-o-cadastro-admiss%C3%A3o-de-funcion%C3%A1rio)  
[RH - Linha Protheus - GPE - Rotina Automática (Execauto) em rotinas do SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/41005221053079-RH-Linha-Protheus-GPE-Rotina-Autom%C3%A1tica-Execauto-em-rotinas-do-SIGAGPE)  
[Exemplo Rotina Automática / Execauto - (Inclusão) Funcionário com Sequencial Automático - MV\_MATRICU](https://tdn.totvs.com/pages/releaseview.action?pageId=1015569806)
