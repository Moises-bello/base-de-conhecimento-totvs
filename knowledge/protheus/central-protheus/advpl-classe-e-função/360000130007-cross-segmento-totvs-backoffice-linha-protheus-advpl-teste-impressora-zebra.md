---
article_id: 360000130007
category: ADVPL - Classe e Função
content_hash: eedd542fa1165a24a289d95e323ffb1cdfb4176f8deac126c019c8d26c7b5d16
fetched_at: '2026-06-28T22:40:18.079759+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Teste impressora
  Zebra
type: support-article
updated_at: '2023-11-17T18:38:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000130007-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Teste-impressora-Zebra
---

**Ocorrência**Ao utilizar as funções "MSCBPRINTER" não sai nenhuma impressão e também não me da nenhum tipo de erro.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Segue exemplo de teste da impressora térmica zebra

```
^XA  
^PR6  
^PQ1  
^FO80,32^BY5,1,96^BCMB07, 96,Y,N,N,N^FDABC12345^FS  
^XZ
```

No caso o código a ser gerado é ABC12345.

Grave essas informações em um arquivo de texto e realize o seguinte comando no CMD para verificarmos o comportamento.

print LPT1 C:\localdoarquivo\nomedoarquivo.txt

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014599012/mceclip0.png)

Teste de impressão utilizando a classe MSCB

```
#Include 'Protheus.ch'  
#INCLUDE "TBICONN.CH" // BIBLIOTECA  
  
User Function Impressora()  
  
Local cPorta := "LPT1"  
Local cModelo := "ZEBRA"  
  
MSCBPRINTER(cModelo, cPorta,,10,.F.,,,,,,.F.,)  
MSCBCHKSTATUS(.F.)  
MSCBBEGIN(1,6)  
MSCBSAY(10,10,"TESTE IMPRESSAO EM REDE", "N","A","040,030")  
MSCBEND()  
MSCBCLOSEPRINTER()  
  
Return
```

**Saiba Mais**[**MSCBPRINTER**](http://tdn.totvs.com/display/public/mp/MSCBPrinter+-+Configura+Impressora+--+30557)
