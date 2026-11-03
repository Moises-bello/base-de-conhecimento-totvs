---
article_id: 360028971111
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b68932f92d8ba2431e52fc2567c012d20880e17b2c4d87eeba7a35fd18646889
fetched_at: '2026-06-28T22:38:31.059965+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP - FAT - erro no parâmetroFWFormViewStruct: O erro no método GETPROPERTY:
  Campo B1_QTDSER não encontrado. on FWFORMVIEWSTRUCT:GETPROPERTY(FWFORMVIEWSTRUCT.PRW)'
type: support-article
updated_at: '2021-04-28T15:54:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028971111-MP-FAT-erro-no-par%C3%A2metroFWFormViewStruct-O-erro-no-m%C3%A9todo-GETPROPERTY-Campo-B1-QTDSER-n%C3%A3o-encontrado-on-FWFORMVIEWSTRUCT-GETPROPERTY-FWFORMVIEWSTRUCT-PRW
---

**Ocorrência**

Sistema apresenta errorlog :  
**erro no parâmetroFWFormViewStruct: O erro no método GETPROPERTY: Campo B1\_QTDSER não encontrado. on FWFORMVIEWSTRUCT:GETPROPERTY(FWFORMVIEWSTRUCT.PRW)** como resolver?

**Ambiente**

Microsiga Protheus – Faturamento – A partir da versão 11.80  
   
 **Causa**

O erro ocorre devido alteração de nível ou ordem de campo.  
   
 **Solução**

Verificar se o campo **B1\_QTDSER**está configurado com NÍVEL = 1. Caso esteja com conteúdo diferente, colocar = 1.  
  
Verifique também a ordem do campo, este é um campo com legenda vermelha que não pode ter sua ordem alterada.

No padrão a ordem deste campo é **135** caso esteja diferente disso corrija para evitar o errorlog.

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029779651/3.png)
