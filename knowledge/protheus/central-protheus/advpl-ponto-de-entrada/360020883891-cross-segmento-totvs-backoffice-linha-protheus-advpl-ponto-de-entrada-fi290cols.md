---
article_id: 360020883891
category: ADVPL - Ponto de Entrada
content_hash: 6ab6e4fc516fbe35c5c589a6ec30c4d74bff11ffbf8fea513ed13488170e2e64
fetched_at: '2026-06-28T22:40:11.821184+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  FI290COLS mostra o campo mas não grava.
type: support-article
updated_at: '2021-12-29T14:14:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020883891-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-FI290COLS-mostra-o-campo-mas-n%C3%A3o-grava
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:03:00 min  
  
Dúvida**Estou utilizando o Ponto de Entrada **FI290COLS** porém ele não grava as informações, como eu faço para que sejam gravadas estas informações?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**O ponto de Entrada **FI290COLS** serve apenas para inclusão de campos no Acols e Aheader da rotina, para que sejam gravados os campos no titulo é necessário a utilização em conjunto do segundo ponto, o **FA290**.

Exemplo **FI290COLS:**

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
  
User Function FI290COLS() // Indica o Array que será alterado: 1- aHeader; 2- aCols  
  
  
Local nTipo := PARAMIXB[1] // Array   
Local aRet := PARAMIXB[2] // Posição do Array   
Local nI := PARAMIXB[3] // Posição do Array aHeader   
Local nCount // Array com os campos a serem incluídos   
Local aColPE := {"E2_CODBAR","E2_SALDO","E2_ORIGEM","E2_DIRF","E2_CODRET "} // Condição utilizado para retornar o restante do aHeader  
  
  
If nTipo == 1  
  
dbSelectArea("SX3")   
 dbSetOrder(2)  
  
  
 For nCount := 1 to len(aColPE)   
 DbSeek(aColPE[nCount])   
   
 AADD(aRet,{ X3TITULO(aColPE[nCount]), aColPE[nCount], X3PICTURE(aColPE[nCount]), TamSx3(aColPE[nCount])[1] ,0,"","û",Posicione("SX3",2,aColPE[nCount],'X3_TIPO'),"SE2" } ) // "Cabeçalho do campo adicinado FI290Cols"   
   
 next // Ponto que Incrementa os valores das colunas   
   
Else  
  
aAdd(aRet[nI],SE2->E2_CODBAR) //Novo campo Adicionado   
 aAdd(aRet[nI],SE2->E2_SALDO) //Novo campo Adicionado   
 aAdd(aRet[nI],SE2->E2_ORIGEM) //Novo campo Adicionado   
 aAdd(aRet[nI],SE2->E2_DIRF) //Novo campo Adicionado   
 aAdd(aRet[nI],SE2->E2_CODRET) //Novo campo Adicionado   
 //Identifica se o registro esta deletado   
 //Esta posição deve ser adicionada sempre que   
 //criado o ponto de entrada   
 AaDD(aRet[nI],.F.)   
   
EndIF   
   
Return aRet
```

Exemplo **FA290:**

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
  
user function FA290()  
  
 SE2->(RecLock("SE2"))   
 SE2->E2_CODBAR := ACOLS[1][8]   
 SE2->(MsUnLock())  
  
  
Return(.T.)
```

**Saiba mais**[Ponto de entrada FA290](http://tdn.totvs.com/display/public/mp/FA290+-+Grava+faturas+a+pagar+--+11968)  
[Ponto de entrada FI290COLS](https://tdn.totvs.com/display/public/PROT/FI290COLS+-+Incluir+campos+adicionais+na+tela+de+faturas)
