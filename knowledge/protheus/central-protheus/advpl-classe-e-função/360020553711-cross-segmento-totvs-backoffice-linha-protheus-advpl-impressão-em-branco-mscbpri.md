---
article_id: 360020553711
category: ADVPL - Classe e Função
content_hash: 709e4dc3fe91e14a4b7622c97e75850cdfb191653439ff8bc300418227d1ec71
fetched_at: '2026-06-28T22:40:16.944614+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Impressão em branco
  MSCBPrinter
type: support-article
updated_at: '2024-03-13T00:46:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020553711-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Impress%C3%A3o-em-branco-MSCBPrinter
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:02:00 min****Dúvida**Impressão da etiqueta na linguagem EPL para a impressora Zebra TLP 2844 na versão 12, MSCBPrinter, onde imprime normalmente na versão 11 e quando migrado para versão 12 ela imprime, mas sai em branco.   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Função MSCBFORM(.F.) // default .T.  - Desabilita o uso de comandos de formulário na impressão da etiqueta na linguagem EPL para a impressora Zebra TLP 2844.

Segue exemplo:

```
Local cPorta := "LPT1"  
Local cModelo := "TLP 2844"  
  
MSCBPRINTER(cModelo,cPorta, , , .F., , , , ,,.f. , )  
MSCBFORM(.F.)//Resolvido problema na impressão da TLP 2844  
MSCBCHKSTATUS(.F.)  
MSCBBEGIN(1,6)  
MSCBSAY(090,165,"TESTE TESTE ","R","2","03,03")  
MSCBInfoEti("Produto","30X100")  
  
MSCBEND()  
MSCBCLOSEPRINTER()
```
