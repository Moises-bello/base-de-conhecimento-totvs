---
article_id: 360025215771
category: ADVPL - Classe e Função
content_hash: 41cad486f696d3f296e42a37eb8d386c234b94f8fb670c80bb8d8c7c40cd0584
fetched_at: '2026-06-28T22:40:16.912182+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Gerar impressão
  de imagem impressora térmica
type: support-article
updated_at: '2024-07-04T15:02:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025215771-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Gerar-impress%C3%A3o-de-imagem-impressora-t%C3%A9rmica
---

**Dúvida**Mandei uma etiqueta para a impressora zebra GC420t, sendo que textos e números imprimem normalmente, porém o logo não imprime.

Quais funções devo usar? Foi efetuado tentativa em .bmp e pcx.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Deve-se usar a [**MSCBLoadGRF.**](http://tdn.totvs.com/pages/releaseview.action?pageId=6090939) porém é necessário converter a imagem, a classe não entende as extensões .bmp e .pcx

Para realizar a conversão é necessário que a imagem esteja em qualidade 16 bits monocromático, trata-se de uma exigência da própria impressora. É possível utilizar o Paint do *Windows* para realizar essa modificação, salvando a imagem na qualidade descrita e já redimensionando o tamanho.

Com a imagem convertida em 16 bits monocromático, é necessário realizar a conversão para o formato em que a impressora irá reconhecer, no caso com a extensão \*.GRF.   
Para conversão deve-se utilizar um Studio disponibilizado pela própria fabricante da impressora ou algum programa específico que tenha essa função.   
Após obter a imagem com a extensão correta a mesma deverá ser salva no diretório system do RootPath nomeada com a extensão referente.   
  
Utilizamos o fonte abaixo para efetuar a impressão:

```
#Include "TOTVS.ch"  
#Include "TBICONN.ch"  
#Include "TBICODE.ch"  
  
User Function ImpQRCod()  
    Local cPorta  := "LPT1"  
    Local cModelo := "ZEBRA"  
  
    MSCBPrinter(cModelo, cPorta, NIL, NIL, .F., NIL, NIL, NIL, , NIL, .F.) // CONFIGURAÇÃO DA IMPRESSORA  
    MSCBChkStatus(.F.)                                                     // VERIFICA STATUS DA IMPRESSORA  
    MSCBLoadGRF("NOME.GRF")                                                // CARREGA IMAGEM NA MEMÓRIA DA IMPRESSORA  
  
    MSCBBegin(1, 6)               // INICIA A IMPRESSÃO  
        MSCBGrafic(10, 8, "NOME") // IMPRESSÃO DE ARQUIVO NA MEMÓRIA  
    MSCBEnd()                     // FINALIZA IMPRESSÃO  
  
    MSCBClosePrinter() // FINALIZA CONEXÃO COM A IMPRESSORA  
  
Return (NIL)
```

\* Na conversão deve-se atentar ao tamanho da imagem com o tamanho da etiqueta.  
\*\* Existe a função **MSCBWrite** (<http://tdn.totvs.com/pages/releaseview.action?pageId=6090943>) que também pode ser utilizada no processo de impressão onde existe a possibilidade de modificar algumas informações da imagem via linguagem da impressora.
