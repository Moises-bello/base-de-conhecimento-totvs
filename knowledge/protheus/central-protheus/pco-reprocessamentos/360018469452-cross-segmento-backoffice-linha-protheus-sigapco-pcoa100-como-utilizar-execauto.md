---
article_id: 360018469452
category: PCO - Reprocessamentos
content_hash: 0ca8b355592f25a7d1bc9d80e1e51e36821ec51ee125d8f9b0e89d15d22e733a
fetched_at: '2026-06-28T22:37:06.996242+00:00'
product: protheus
section_id: 1500001551022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA100 COMO_UTILIZAR_EXECAUTO_ROT_PLAN_ORCAMENTARIA_PCOA100?
type: support-article
updated_at: '2023-11-21T14:11:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018469452-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA100-COMO-UTILIZAR-EXECAUTO-ROT-PLAN-ORCAMENTARIA-PCOA100
---

**Dúvida**COMO\_UTILIZAR\_EXECAUTO\_ROT\_PLAN\_ORCAMENTARIA\_PCOA100?

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
   
**Solução**

A rotina automática ExecAuto da planilha orçamentaria pode ser utilizado de 2 formas conforme segue:

1) Para incluir a planilha orçamentaria (AK1) e o nó principal da estrutura (AK3)

Neste caso somente deve ser passado a função PCOA100 apenas o array xAutoCab contendo os campos da tabela de planilha orçamentaria (AK1).

O argumento da função xAutoItens não deve ser passado a função.

2)Para alteração de itens orçamentarios (AK2) tanto para inclusão de itens como para alteração

Neste caso deve ser passado a função PCOA100 os array xAutoCab e xAutoItens sendo que:

-No array xAutoCab deve ser passado o codigo da planilha, a versão e a conta orçamentária que vai receber os itens passado no array xAutoItens e em ambos os array deve se referir a campos da tabela de itens orçamentários (AK2).Para se referenciar aos períodos deve o nome do campo ser precedido da letra P seguido de 2 digitos numericos que corresponde ao período, assim fica P01 para primeiro período P02 para segundo periodo e segue esta sequencia.

Para alterar um item ja existente deve ser usado a clausula LINPOS no primeiro elemento, no segundo o campo referente ao item e no terceiro o código do item da planilha.

Para incluir um novo item na planilha no conteudo do campo AK2\_ID deve ser passado "\*".

Exemplo: xAutoCab := { {"AK2\_ORCAME", "MYPLANORC" , nil},;  
{"AK2\_VERSAO", "0001" , nil},;  
{"AK2\_CO" , "1010111" , nil}; }

xAutoItens := {}   
//exemplo de alteracao de um item ja existente na planilha   
aAdd(xAutoItens,{ {'AK2\_ORCAME' ,'MYPLANORC' , NIL},;   
{'AK2\_VERSAO' ,'0001' , NIL},;  
{'AK2\_CO' ,'111' , NIL},;  
{'AK2\_ID' ,'0001', NIL},;  
{'AK2\_CLASSE' ,'000001' , NIL},;  
{'LINPOS' ,'AK2\_ID' , '0001'},; //no 2o. elemento de LINPOS tem que ser passado o campo do item e no 3o.elemento o codigo do item  
{'P01' ,11000 , NIL},; //primeiro período

  {'P02' ,12000 , NIL},; //segundo período

{'P03' ,13000 , NIL},;  
{'P04' ,14000 , NIL},;  
{'P05' ,15000 , NIL},;  
{'P06' ,16000 , NIL},;  
{'P07' ,17000 , NIL},;  
{'P08' ,18000 , NIL},;  
{'P09' ,19000 , NIL},;  
{'P10' ,20000 , NIL},;  
{'P11' ,21000 , NIL},;  
{'P12' ,22000 , NIL};  
} )

//exemplo de inclusão de novo item na planilha   
aAdd(xAutoItens,{ {'AK2\_ORCAME' ,'MYPLANORC' , NIL},;   
{'AK2\_VERSAO' ,'0001' , NIL},;  
{'AK2\_CO' ,'111' , NIL},;  
{'AK2\_ID' ,'\*', NIL},;  
{'AK2\_CLASSE' ,'000001' , NIL},;  
{'P01' ,11000 , NIL},; //primeiro período

{'P02' ,12000 , NIL},; //segundo período  
{'P03' ,13000 , NIL},;  
{'P04' ,14000 , NIL},;  
{'P05' ,15000 , NIL},;  
{'P06' ,16000 , NIL},;  
{'P07' ,17000 , NIL},;  
{'P08' ,18000 , NIL},;  
{'P09' ,19000 , NIL},;  
{'P10' ,20000 , NIL},;  
{'P11' ,21000 , NIL},;  
{'P12' ,22000 , NIL};  
} )

//---------------------------------------------------------//

Abaixo exemplo de código fonte para incluir planilha (AK1) e para alterar itens da planilha (AK2)

//---------------------------------------------------------//

#include "[Protheus.ch](http://protheus.ch/)"

User Function TstPcoa100()

Local aAutoCab  
Local aAutoItens

Private lMsHelpAuto := .T.  
Private lMsErroAuto := .F.

If MsgYesNo("Deseja Incluir planilha - Caso nao sera considerado alterar","Atencao")  
aAutoCab := { ;  
{"AK1\_CODIGO", "TSTPCOA100" , nil},;  
{"AK1\_VERSAO", "0001" , nil},;  
{"AK1\_DESCRI" , "TESTE DO PCOA100 PARA INCLUIR PLANILHA" , nil},;  
{"AK1\_TPPERI" , "3" , nil},;  
{"AK1\_INIPER" , CTOD("01/01/16") , nil},;  
{"AK1\_FIMPER" , CTOD("31/12/16") , nil},;  
{"AK1\_CTRUSR" , "1" , nil},;  
{"AK1\_STATUS" , "1" , nil};  
}  
  
MSExecAuto( {|x,y,z,a,b,c| PCOA100(x,y,z, a, b, c)}, 3/\*nCallOpcx\*/,/\*cRevisa\*/, /\*lRev\*/, /\*lSim\*/,aAutoCab, /\*xAutoItens\*/) //inclusão AK1  
  
If !lMsErroAuto  
msgalert("Incluido com sucesso! ")  
Else   
  
msgalert("Erro na inclusao!")  
MostraErro()  
EndIf  
Else  
//alteracao da planilha - estrutura tem que estar pronto AK1 / AK3  
aAutoCab := { ;  
{"AK2\_ORCAME", "TSTPCOA100" , nil},;  
{"AK2\_VERSAO", "0001" , nil},;  
{"AK2\_CO" , "111" , nil};   
}  
  
aAutoItens := {}   
//exemplo de alteracao de um item ja existente na planilha   
aAdd(aAutoItens,{ {'AK2\_ORCAME' ,'TSTPCOA100' , NIL},;   
{'AK2\_VERSAO' ,'0001' , NIL},;  
{'AK2\_CO' ,'111' , NIL},;  
{'AK2\_ID' ,'0001', NIL},;  
{'AK2\_CLASSE' ,'000001' , NIL},;  
{'LINPOS' ,'AK2\_ID' , '0001'},;  
{'P01' ,11000 , NIL},;  
{'P02' ,12000 , NIL},;  
{'P03' ,13000 , NIL},;  
{'P04' ,14000 , NIL},;  
{'P05' ,15000 , NIL},;  
{'P06' ,16000 , NIL},;  
{'P07' ,17000 , NIL},;  
{'P08' ,18000 , NIL},;  
{'P09' ,19000 , NIL},;  
{'P10' ,20000 , NIL},;  
{'P11' ,21000 , NIL},;  
{'P12' ,22000 , NIL};  
} )  
  
//exemplo de inclusao de um novo item na planilha  
aAdd(aAutoItens,{ {'AK2\_ORCAME' ,'TSTPCOA100' , NIL},;   
{'AK2\_VERSAO' ,'0001' , NIL},;  
{'AK2\_CO' ,'111' , NIL},;  
{'AK2\_ID' ,'\*', NIL},; //para inclusão de novo item da planilha deve ser passado no conteúdo "\*" e nao deve ser utilizado LINPOS  
{'AK2\_CLASSE' ,'000001' , NIL},;  
{'P01' ,111000 , NIL},;  
{'P02' ,112000 , NIL},;  
{'P03' ,113000 , NIL},;  
{'P04' ,114000 , NIL},;  
{'P05' ,115000 , NIL},;  
{'P06' ,116000 , NIL},;  
{'P07' ,117000 , NIL},;  
{'P08' ,118000 , NIL},;  
{'P09' ,119000 , NIL},;  
{'P10' ,120000 , NIL},;  
{'P11' ,121000 , NIL},;  
{'P12' ,122000 , NIL};  
} )  
  
MSExecAuto( {|x,y,z,a,b,c| PCOA100(x,y,z, a, b, c)}, 4/\*nCallOpcx\*/,/\*cRevisa\*/, /\*lRev\*/, /\*lSim\*/,aAutoCab, aAutoItens) //4=alteração para manipular itens da planilha  
  
If !lMsErroAuto  
msgalert("Alterado os itens da planilha com sucesso! ")  
Else   
msgalert("Erro na alteracao dos itens da planilha!")  
MostraErro()  
EndIf  
  
EndIf

Return

**Importante:**

Não existe rotina automática para inclusão ou alteração da estrutura da planilha (AK3).

Sintaxe da função PCOA100:

PCOA100(3/\*nCallOpcx\*/,/\*cRevisa\*/, /\*lRev\*/, /\*lSim\*/,aAutoCab, /\*xAutoItens\*/) //3=inclusão 4=alteração
