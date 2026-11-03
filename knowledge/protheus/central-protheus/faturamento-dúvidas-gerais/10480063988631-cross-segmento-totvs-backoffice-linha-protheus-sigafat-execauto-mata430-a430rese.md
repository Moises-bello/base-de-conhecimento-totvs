---
article_id: 10480063988631
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e64c86898495473f75167cb4fa9261ea913a134b6f15c838858e003309fdf92c
fetched_at: '2026-06-28T22:38:32.794558+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - EXECAUTO MATA430
  (A430Reserv)
type: support-article
updated_at: '2022-11-25T12:30:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10480063988631-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-EXECAUTO-MATA430-A430Reserv
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do **Execauto MATA430 - Controle de Reservas.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**Função utilizada para geração de Reservas via rotina automática (ExecAuto).  
  
**Exemplo**

```
#INCLUDE 'TOTVS.CH'  
#INCLUDE "RWMAKE.CH"  
  
User Function My430RES()  
  
Local aOperacao := {}  
Local cNumero := '000009' //C0_NUM - Numero da reserva (inclusão, alteração ou exclusão)  
Local cProduto := '000015 ' //Será utilizado o conteúdo do campo C0_PRODUTO exatamente com o seu tamanho, contando os espaços em branco.  
Local cLocal := '01' //C0_LOCAL  
Local nQuant := 1 //C0_QUANT  
Local aLote := {"","","",""}   
Local nOpc := 1 //Seleciona o tipo da operacao (1-Inclusao / 2-Alteracao / 3-Exclusao)  
Local lReservOk := .T.  
  
Private aHeader := {}  
Private aCols := {}  
  
//PREPARACAO DO AMBIENTE  
RpcSetEnv("99","01","Administrador","","FAT","MATA430") //Empresa, Filial  
ConOut(Repl("-",80))  
ConOut(PadC("Teste de Inclusao / Alteracao / Exclusao de Reserva",80))  
  
If nOpc == 1 //INCLUSAO  
  
ConOut(Repl("-",80))  
ConOut(PadC("Teste de Inclusao",80))  
ConOut("Inicio: " + Time())  
  
//MONTAGEM DO HEADER E ACOLS PARA CAMPOS CUSTOMIZADOS OU PADRAO  
DbSelectArea("SC0")  
  
If FieldPos("C0_FILRES") > 0  
aAdd(aHeader,{ GetSx3Cache("C0_FILRES",'X3_TITULO '),;  
GetSx3Cache("C0_FILRES",'X3_CAMPO '),;  
GetSx3Cache("C0_FILRES",'X3_PICTURE'),;  
GetSx3Cache("C0_FILRES",'X3_TAMANHO'),;  
GetSx3Cache("C0_FILRES",'X3_DECIMAL'),;  
GetSx3Cache("C0_FILRES",'X3_VALID '),;  
GetSx3Cache("C0_FILRES",'X3_USADO '),;  
GetSx3Cache("C0_FILRES",'X3_TIPO '),;  
GetSx3Cache("C0_FILRES",'X3_F3 '),;  
GetSx3Cache("C0_FILRES",'X3_CONTEXT'),;  
GetSx3Cache("C0_FILRES",'X3_CBOX '),;  
GetSx3Cache("C0_FILRES",'X3_RELACAO') })  
Endif  
  
aadd(aCOLS,"01") //C0_FILRES  
  
aOperacao:= {nOpc ,; //[1] -> [Operacao: 1-Inclui, 2-Altera, 3-Exclui]  
"VD",; //[2] -> [Tipo da Reserva]  
"",; //[3] -> [Documento que originou a Reserva]  
"",; //[4] -> [Solicitante]  
xFilial("SC0")} //[5] -> [Filial da Reserva]  
  
CONOUT("Iniciando a gravacao")  
lReservOk := a430Reserv(aOperacao,cNumero,cProduto,cLocal,nQuant,aLote,aHeader,aCols)  
  
If lReservOk  
Conout('Reserva cadastrada com Sucesso!')  
Else  
Conout('Problemas ao cadastrar reserva')  
MOSTRAERRO()  
EndIf  
  
ConOut("Fim: " + Time())  
  
ElseIf nOPC == 2 //ALTERACAO  
  
ConOut(Repl("-",80))  
ConOut(PadC("Teste de Alteracao",80))  
ConOut("Inicio: " + Time())  
  
//SELECIONAR ITEM PARA ALTERAR  
DbSelectArea("SC0")  
SC0->(DbSetOrder(1))  
  
IF!SC0->(DbSeek(xFilial("SC0")+cNumero+cProduto+cLocal))  
ConOut("Nao localizado o item para alterar")  
lReservOk:=.F.  
Return lReservOk  
EndIf  
  
aOperacao:= {nOpc ,; //[1] -> [Operacao: 1-Inclui, 2-Altera, 3-Exclui]  
"VD",; //[2] -> [Tipo da Reserva]  
"000002 ",; //[3] -> [Documento que originou a Reserva]  
SC0->C0_SOLICIT,; //[4] -> [Solicitante]  
SC0->C0_FILIAL} //[5] -> [Filial da Reserva]  
  
nQuant:= SC0->C0_QUANT  
  
CONOUT("Iniciando a gravacao")  
lReservOk := a430Reserv(aOperacao,cNumero,cProduto,cLocal,nQuant,aLote,aHeader,aCols)  
  
If lReservOk  
Conout('Reserva alterada com Sucesso!')  
Else  
Conout('Problemas ao alterar reserva')  
MOSTRAERRO()  
EndIf  
  
ConOut("Fim: " + Time())  
  
ElseIf nOPC == 3 //EXCLUSAO  
  
ConOut(Repl("-",80))  
ConOut(PadC("Teste de Exclusao",80))  
ConOut("Inicio: " + Time())  
  
//SELECIONAR ITEM PARA EXCLUIR  
DbSelectArea("SC0")  
SC0->(DbSetOrder(1))  
  
IF!SC0->(DbSeek(xFilial("SC0")+cNumero+cProduto+cLocal))  
ConOut("Nao localizado o item para excluir")  
lReservOk:=.F.  
Return lReservOk  
EndIf  
  
aOperacao:= {nOpc ,; //[1] -> [Operacao: 1-Inclui, 2-Altera, 3-Exclui]  
SC0->C0_TIPO,; //[2] -> [Tipo da Reserva]  
SC0->C0_DOCRES,; //[3] -> [Documento que originou a Reserva]  
SC0->C0_SOLICIT,; //[4] -> [Solicitante]  
SC0->C0_FILIAL} //[5] -> [Filial da Reserva]  
  
nQuant:= SC0->C0_QUANT  
  
CONOUT("Iniciando a exclusao")  
lReservOk := a430Reserv(aOperacao,cNumero,cProduto,cLocal,nQuant,aLote,aHeader,aCols)  
  
If lReservOk  
Conout('Reserva excluida com Sucesso!')  
Else  
Conout('Problemas ao excluir reserva')  
MOSTRAERRO()  
EndIf  
  
ConOut("Fim: " + Time())  
  
EndIf  
  
RpcClearEnv()  
  
Return lReservOk
```

**Exemplo**

**[A430Reserv - Rotina Automática (ExecAuto)](https://tdn.totvs.com/x/HuNc)**
