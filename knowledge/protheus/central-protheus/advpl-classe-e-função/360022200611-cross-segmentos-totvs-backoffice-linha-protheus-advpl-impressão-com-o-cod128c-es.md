---
article_id: 360022200611
category: ADVPL - Classe e Função
content_hash: 1f88ac150c7ddec932c55daa47a0a176c5d5ee5df2ae375879bc9099fe90a8a4
fetched_at: '2026-06-28T22:40:20.407613+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Impressão com o
  COD128C está apresentando um zero a mais.
type: support-article
updated_at: '2022-01-11T18:35:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200611-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Impress%C3%A3o-com-o-COD128C-est%C3%A1-apresentando-um-zero-a-mais
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao gerar um código de barras com a função COD128C está apresentando um zero a mais. Seria um erro?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

Não, a classe Fwmsprinter tem a função COD128C para geração de código de barras, porém o subconjunto C é utilizado para duplicar a densidade de códigos com conteúdo apenas NUMÉRICO e número PAR de dígito, exemplo de customização:

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
#Include "RPTDEF.CH"  
#INCLUDE "TBICONN.CH"  
  
user function MyCODE128C()  
  
Local oPrinter  
  
  
PREPARE ENVIRONMENT EMPRESA "T1" FILIAL "01"  
  
oPrinter := FWMSPrinter():New('teste',6,.F.,,.T.,,,,,.F.)  
  
oPrinter:Setup()  
oPrinter:setDevice(IMP_PDF)  
oPrinter:cPathPDF :="C:\"  
oPrinter:Say(10,0,"Teste para Code128C")  
oPrinter:Code128c(200, 10, '1234567', 50)  
oPrinter:EndPage()  
oPrinter:Preview()  
  
FreeObj(oPrinter)  
  
oPrinter := Nil  
RESET ENVIRONMENT  
  
  
return
```

Retorno da imagem.

![](http://tdn.totvs.com/download/attachments/286502367/image2017-8-25%2011%3A29%3A30.png?version=1&modificationDate=1503671397000&api=v2)

12345607

**Saiba mais**[FWMsPrinter](http://tdn.totvs.com/display/public/mp/FWMsPrinter)
