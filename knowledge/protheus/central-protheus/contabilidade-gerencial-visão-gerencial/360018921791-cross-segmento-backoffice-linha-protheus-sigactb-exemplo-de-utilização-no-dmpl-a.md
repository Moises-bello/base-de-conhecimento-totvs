---
article_id: 360018921791
category: Contabilidade Gerencial - Visão Gerencial
content_hash: 1795d4e9b8735a3763bcad812b84169abc05645e921a1e130d807c5c60b1621b
fetched_at: '2026-06-28T22:40:50.684372+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus- SIGACTB: Exemplo de utilização
  no DMPL a função SaldoCT7Fil'
type: support-article
updated_at: '2022-07-18T19:58:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018921791-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Exemplo-de-utiliza%C3%A7%C3%A3o-no-DMPL-a-fun%C3%A7%C3%A3o-SaldoCT7Fil
---

**Dúvida**Exemplo de utilização no DMPL a função SaldoCT7Fil

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial –  versão 11.80 **Solução**

No campo formula da visão referente ao DMPL incluir a sintaxe abaixo:

SALDO=U\_TESTEPC()

Onde TestePc() é uma User Function exemplificada abaixo.

Veja também os links TDN:

[CTB0054\_Visão\_Gerencial-Campo\_Fórmula](http://tdn.totvs.com/pages/viewpage.action?pageId=233766503)

[CTB0055\_Visão\_Gerencial-Expressões\_especiais](http://tdn.totvs.com/pages/viewpage.action?pageId=234455566)

[CTB0058\_Visão\_Gerencial-Uso\_de\_fórmulas](http://tdn.totvs.com/pages/viewpage.action?pageId=234456108)

Exemplo de fonte com utilização da função SaldoCT7Fil

#INCLUDE "PROTHEUS.CH"

USER FUNCTION TESTEPC()

LOCAL cConta,dData,cMoeda,cTpSald  
Local nSaldoAtu,nDebito,nCredito,nAtuDeb,nAtuCrd,nSaldoAnt,nAntDeb,nAntCrd  
Local xSald, xSaldAnt

cConta := "11"  
cMoeda := '01'  
cTpSald := '1'  
//saldo anterior  
dData := CTOD("31/12/2015")  
xSaldAnt=SaldoCT7Fil(cConta,dData,cMoeda,cTpSald,"TESTEPC" /\*cRotina\*/)  
//saldo atual  
dData := CTOD("31/12/2016")  
xSald=SaldoCT7Fil(cConta,dData,cMoeda,cTpSald,"TESTEPC" /\*cRotina\*/)

//----------------------------------------------------------------------------------------------------------------------------//  
//Retorno:   
//[1] Saldo Atual (com sinal)  
//[2] Debito na Data   
//[3] Credito na Data   
//[4] Saldo Atual Devedor   
//[5] Saldo Atual Credor   
//[6] Saldo Anterior (com sinal)   
//[7] Saldo Anterior Devedor   
//[8] Saldo Anterior Credor   
//----------------------------------------------------------------------------------------------------------------------------//

//composicao dos valores extraindo os dados dos arrays xSald (Atual) e xSaldAnt (Anterior)

nSaldoAtu := xSald[1]  
nDebito := xSald[4]-xSaldAnt[4]  
nCredito := xSald[5]-xSaldAnt[5]  
nAtuDeb := nDebito  
nAtuCrd := nCredito  
nSaldoAnt := xSaldAnt[1]  
nAntDeb := xSaldAnt[4]  
nAntCrd := xSaldAnt[5]

xSald := {nSaldoAtu,nDebito,nCredito,nAtuDeb,nAtuCrd,nSaldoAnt,nAntDeb,nAntCrd}

RETURN(xSald)
