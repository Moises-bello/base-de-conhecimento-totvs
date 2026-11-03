---
article_id: 360017794011
category: Contabilidade Gerencial - Visão Gerencial
content_hash: f74fe3b4c14fc665aa0022fa9fa49b9ffd94a1ef338de7899ba8cdae6d1ca81b
fetched_at: '2026-06-28T22:40:50.637688+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB : COMO UTILIZAR FUNCAO
  SALDOCT7FIL'
type: support-article
updated_at: '2022-06-06T20:02:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017794011-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-COMO-UTILIZAR-FUNCAO-SALDOCT7FIL
---

**Dúvida**

|  |
| --- |
| Utilização da Função SALDOCT7FIL para extrair saldo das contas contábeis. |

**Ambiente**A partir da versão 11.80  
  
  
**Solução**

A função SaldoCT7Fil retorna um array contendo os valores de saldos para uma determinada conta contábil em uma data informada.

Sintaxe da Função:

SaldoCT7Fil(cConta,dData,cMoeda,cTpSald,cRotina,lImpAntLP,dDataLP,aSelFil)

Parametros:

cConta = Conta Contabil (Caracter)

dData = Data do Saldo Contabil (Data)

cTpSald = Tipo de Saldo Contabil (1-Real) (Caracter)

cRotina = Rotina que chama a função (Caracter)

lImpAntLP = Indica se considera saldo antes da Apuração de Resultado (Logico .T. ou .F.)

dDataLP = Data de Apuracao de Resultado (Data)

aSelFil = Array com as Filiais consideradas para saldo (Array) - Este parametro somente deve ser passado quando necessário somar saldo de 2 ou mais filiais, por padrão, considera a filial posicionada

Retorno:

[1] Saldo Atual (com sinal)   
[2] Debito na Data  
[3] Credito na Data  
[4] Saldo Atual Devedor  
[5] Saldo Atual Credor  
[6] Saldo Anterior (com sinal)  
[7] Saldo Anterior Devedor  
[8] Saldo Anterior Cred

Exemplo de Utilização:

USER FUNCTION TESTEPC()

LOCAL cConta,dData,cMoeda,cTpSald  
Local nSaldoAtu,nDebito,nCredito,nAtuDeb,nAtuCrd,nSaldoAnt,nAntDeb,nAntCrd  
Local xSaldAnt

cConta := "11"  
cMoeda := '01'  
cTpSald := '1'  
//saldo anterior  
dData := CTOD("31/12/2015")  
xSaldAnt=SaldoCT7Fil(cConta,dData,cMoeda,cTpSald,"TESTEPC" /\*cRotina\*/)

//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//³ Retorno: ³  
//³ [1] Saldo Atual (com sinal) ³  
//³ [2] Debito na Data ³  
//³ [3] Credito na Data ³  
//³ [4] Saldo Atual Devedor ³  
//³ [5] Saldo Atual Credor ³  
//³ [6] Saldo Anterior (com sinal) ³  
//³ [7] Saldo Anterior Devedor ³  
//³ [8] Saldo Anterior Credor ³  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ

Return(xSaldAnt)
