---
article_id: 360018561812
category: Ativo Fixo - Bens terceiros
content_hash: 92c0afae6577391f929b8d315cc950ff3bce7c978b3ad31b495ee135d8f12465
fetched_at: '2026-06-28T22:41:44.459375+00:00'
product: protheus
section_id: 1500001536381
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF Utilização da rotina automática
  do cadastro de Bens de Terceiros
type: support-article
updated_at: '2023-11-29T18:15:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018561812-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Utiliza%C3%A7%C3%A3o-da-rotina-autom%C3%A1tica-do-cadastro-de-Bens-de-Terceiros
---

**Dúvida**Exemplo de utilização da rotina automática do cadastro de Bens de Terceiros  
  
**Ambiente**Protheus – Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**User Function Myatfa320()

Local aItens := {}Local aDadosAuto := {} // Array com os dados a serem enviados pela MsExecAuto() para gravacao automatica do ativo em terceiroLocal nOpcaoLocal aCab := { {'NO\_FILIAL' ,'01 ' ,NIL},; {'NO\_CODIGO' ,'000001' ,NIL},; {'NO\_CBASE' ,'1234567890' ,NIL},; {'NO\_ITEM' ,'1234' ,NIL},; {'NO\_FORNEC' ,'000000' ,NIL},; {'NO\_LOJA' ,'00' ,NIL},; {'NO\_TIPCES' , 'C' ,NIL} } Private lMsHelpAuto := .f. // Determina se as mensagens de help devem ser direcionadas para o arq. de logPrivate lMsErroAuto := .f. // Determina se houve alguma inconsistencia na execucao da rotina nOpcao := Aviso("Atencao - Bens de Terceiros", "Incluir / Alterar ou Excluir ?", {"Incluir", "Alterar", "Excluir"})If nOpcao == 1 //Inclusao CODIGO 000001 //NESTE CASO O CONTROLE DE NUMERACAO DEVE ESTAR NA ROTINA DO USUARIO aAdd(aItens,{ {'NO\_SEQ' ,'001' , NIL},; {'NO\_STATUS' ,'1' , NIL},; {'NO\_VIGINI' ,CTOD('01/01/12'), NIL},; {'NO\_VIGFIM' ,CTOD('31/12/12'), NIL},; {'NO\_CONTATO' ,'INCLUSAO DO CONTATO' ,NIL} } ) MSExecAuto( {|a,b,c,x,y,z| ATFA320(a,b,c,x,y,z)} ,"SNO",0,3,3,aCab,aItens) ElseIf nOpcao == 2 //Alteracao aAdd(aItens,{ {'NO\_SEQ' ,'001' , NIL},; // em alteracao o campo Seq deve ser informado {'NO\_STATUS' ,'2' , NIL},; {'NO\_VIGINI' ,CTOD('01/01/12'), NIL},; {'NO\_VIGFIM' ,CTOD('31/12/12'), NIL},; {'NO\_CONTATO' ,'ALTERACAO DO CONTATO' ,NIL} } ) aAdd(aItens,{ {'NO\_SEQ' ,'002' , NIL},; // em alteracao o campo Seq deve ser informado {'NO\_STATUS' ,'1' , NIL},; {'NO\_VIGINI' ,CTOD('31/01/13'), NIL},; {'NO\_VIGFIM' ,CTOD('31/12/13'), NIL},; {'NO\_CONTATO' ,'NOVO CONTATO NA ALTERACAO' ,NIL} } ) dbSelectArea("SNO") dbSetOrder(1) If dbSeek(xFilial()+'000001') // EM CASO DE ALTERACAO USUARIO DEVERA POSICIONAR NO REGISTRO A SER ALTERADO MSExecAuto( {|a,b,c,x,y,z| ATFA320(a,b,c,x,y,z)} ,"SNO",0,4,4,aCab,aItens) EndIf ElseIf nOpcao == 3 //Exclusao dbSelectArea("SNO") dbSetOrder(1) If dbSeek(xFilial()+'000001') //EM CASO DE EXCLUSAO USUARIO DEVERA POSICIONAR NO REGISTRO A SER EXCLUIDO MSExecAuto( {|a,b,c,x,y,z| ATFA320(a,b,c,x,y,z)} ,"SNO",0,5,5,aCab,aItens) EndIfEndIf If lMsErroAuto lRetorno := .F. MostraErro()Else lRetorno:=.T.EndIfReturn
