---
article_id: 360022403911
category: ADVPL - Ponto de Entrada
content_hash: d185c3a24cd486fafa449fbe5daafaca2515733b200bfd89fff833836f0093eb
fetched_at: '2026-06-28T22:40:12.743454+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  para validação de rotina
type: support-article
updated_at: '2021-12-30T14:33:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022403911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-para-valida%C3%A7%C3%A3o-de-rotina
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min****Dúvida**Existe algum ponto de entrada, para valida o acesso em um determinado horário, onde o usuário só possa utilizar a rotina em um horário especifico, exemplo MATA440(liberação de pedidos), no horário de segunda a sábado das 7:30 as 16:00?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

Neste caso pode utilizar o ponto Genérico para validação, [**MBRWBTN - Validação da rotina**](http://tdn.totvs.com/pages/releaseview.action?pageId=6815197)

```
Exemplo de customização  
  
#Include 'Protheus.ch'  
  
User Function MBRWBTN()  
Local lRet := .T.  
  
IF FunName()=="MATA440"  
 lRet := .F.  
 Alert("MBRWBTN"+" O ponto retornou : "+cValToChar(lRet))  
Endif  
  
If ( __cUserId == '000004' )   
 Final('Usuário sem acesso ao sistema')  
EndIf  
  
Return lRet
```

**Saiba mais**Funções para auxilio na customização:

[Final - Finaliza o sistema](http://tdn.totvs.com/display/public/PROT/Final+-+Finaliza+o+sistema)  
[FunName - Nome do programa em execução](http://tdn.totvs.com/pages/releaseview.action?pageId=6814875)  
[RetCodUsr](http://tdn.totvs.com/display/public/PROT/RetCodUsr)
