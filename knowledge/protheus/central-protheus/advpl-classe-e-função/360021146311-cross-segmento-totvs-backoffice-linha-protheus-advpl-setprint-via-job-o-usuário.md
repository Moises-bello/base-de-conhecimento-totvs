---
article_id: 360021146311
category: ADVPL - Classe e Função
content_hash: 377756465dbe6255826b34da7ff64c5775db9b4a7f1000cb6249691e733247bf
fetched_at: '2026-06-28T22:40:18.008523+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - SetPrint via job:
  O usuário possui restrição de horário de acesso'
type: support-article
updated_at: '2022-09-18T15:06:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021146311-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-SetPrint-via-job-O-usu%C3%A1rio-possui-restri%C3%A7%C3%A3o-de-hor%C3%A1rio-de-acesso
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao utilizar a função SetPrint via JOB está apresentando a seguinte mensagem: " O usuário possui restrição de horário de acesso. O horário definido para uso é das  às "  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Causa**Ao utilizar a função SetPrint via JOB, não está setado o ambiente e nem qual usuário irá realizar a operação, por este motivo  é apresentado a mensagem.

**Solução**Para solucionar essa ocorrência, deverá incluir na sua customização a preparação de ambiente com o usuário e senha que será responsável pela impressão.

**Exemplo**

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
#include "tbiconn.ch"  
  
User Function setprint()  
  
local wnrel  
local cString := "SA1"  
local titulo := "Teste Impressão de Relatorios"  
local NomeProg := "XXX"   
local Tamanho := "M"  
  
private aReturn := { "Zebrado", 1,"Administracao", 1, 2,"", "",1 }  
  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" USER "ADMINISTRADOR" PASSWORD ""  
  
wnrel:= SetPrint(cString,NomeProg,"",@titulo,"", "", "",.F.,.F.,.F.,Tamanho,,.F.)  
  
SetDefault(aReturn,cString, ,.t.)  
  
RptStatus({|lEnd| TestRel(@lEnd,wnRel,cString,Tamanho,NomeProg)},titulo)  
  
return  
  
static function TestRel(lEnd,WnRel,cString,Tamanho,NomeProg)  
  
local cabec1,cabec2  
local cRodaTxt := oemtoansi("Rodapé")  
local nCntImpr   
local nTipo  
  
nCntImpr := 0  
  
li := 80  
  
m_pag := 1 //³ Inicializa os codigos de caracter Comprimido da impressora ³  
  
nTipo := 15 //³ Monta os Cabecalhos ³  
  
titulo:= oemtoansi("Lista de Clientes")  
  
cabec1:= oemtoansi("COD LOJA NOME NOME FANTASIA ")  
  
cabec2:=""  
  
dbSelectArea("SA1")  
dbGoTop()  
  
SetRegua(LastRec())  
  
while !(SA1->(Eof()))  
IncRegua()  
  
if Li > 60   
//cabec(titulo,cabec1,cabec2,nomeprog,tamanho,15)   
//@ Li,0 PSAY __PrtThinLine()  
  
// Cabecalho  
@ li,0 PSAY __PrtFatLine()  
li++  
@ li,0 PSAY __PrtLogo()  
li++  
@ li,0 PSAY __PrtFatLine()  
li+= 2  
  
endIf  
  
nCntImpr++   
Li++  
  
@ Li,01 PSAY A1_COD   
@ Li,05 PSAY A1_LOJA   
@ Li,10 PSAY A1_NOME   
@ Li,51 PSAY A1_NREDUZ  
  
if Li > 60   
Li:=66   
endif  
  
SA1->(dbSkip())  
  
endDo  
  
if li != 80   
Roda(nCntImpr,cRodaTxt,Tamanho)  
endIf  
  
Set Device to Screen  
  
if aReturn[5] = 1   
Set Printer To dbCommitAll()   
OurSpool(wnrel)  
endIf  
  
MS_FLUSH()  
  
return
```

**Saiba Mais**

**[PREPARE ENVIRONMENT](http://tdn.totvs.com/pages/releaseview.action?pageId=6814708)**

**[SetPrint](http://tdn.totvs.com/pages/releaseview.action?pageId=6815081)**
