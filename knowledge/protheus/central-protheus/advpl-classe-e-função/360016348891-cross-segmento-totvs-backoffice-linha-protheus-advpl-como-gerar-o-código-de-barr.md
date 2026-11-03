---
article_id: 360016348891
category: ADVPL - Classe e Função
content_hash: 911d0f63feb49f9aee835380964eb8ebc120c35b8f7af563d0509e2897896a74
fetched_at: '2026-06-28T22:40:15.527046+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como gerar o código
  de barras GS1-128
type: support-article
updated_at: '2024-03-20T18:55:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016348891-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-gerar-o-c%C3%B3digo-de-barras-GS1-128
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como gerar o código de barras GS1-128? **Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80 **Solução**Algumas informações de antemão sobre CODE-128, EAN-128 E O GS1-128:

* **CODE-128:** Simbologia de código de barras linear definida pelo ISO
* **EAN-128:** Evolução do CODE128, aparentemente iguais, porém com um maior espaçamento para melhor a velocidade de leitura
* **GS1-128:** Conceito que trabalha com o modelo EAN-128 (evoluído do CODE-128) para injeção de informações no código

Resumo das informações acima citadas

O GS1-128 não é um tipo de código de barras, mas sim um conceito que usa o CODE-128 aprimorado (conhecido como EAN-128) para adição de informações no código.

Como funciona o GS1-128?  
O GS1-128 trabalha com um conceito de índices chamados de Identificadores de Aplicação (*AI - Application Identifiers*), onde cada identificador corresponde à uma informação que será contida em uma quantidade de caracteres previamente delimitada.

Vídeo ilustrativo do funcionamento do GS1-128

**Identificadores de aplicação (*Application identifiers*)**

Note no exemplo abaixo o código de barras utilizado:

![SSCCsampleEAN128.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360012092851/SSCCsampleEAN128.gif)

(01)05391234567892(15)051231(10)APO1536Z(00)353912345678910118

Perceba que antes de cada agrupamento de valores, temos um identificador de aplicação (AI) entre parênteses.

De acordo com a Wikipédia (<https://pt.wikipedia.org/wiki/GS1-128>) e o Guia GS1 Identificação Avançada - Versão 1.0 - R01 (<https://www.gs1br.org>), os AI  01, 15, 10, 00 correspondem à:

* **00:** Serial Shipping Container Code (SSCC) | **Tamanho:** 18 dígitos numéricos
* **01:** Global Trade Item Number (GTIN) | **Tamanho:** 14 dígitos numéricos
* **10:** Número Batch | **Tamanho:** de 1 a 20 dígitos alfanuméricos
* **15:** Melhor antes de... (usado no controlo da qualidade) | **Tamanho:** 6 dígitos numéricos no formato AAMMDD

Assim sendo, o programa que efetuou a leitura, pode recuperar as informações do código de barras, avaliar o que elas significam por meio dos AI, pesquisar os códigos na base de dados e retornar o que eles significam.

**GS1-128 NO PROTHEUS**

As funções do Protheus que efetuam a impressão de códigos de barras CODE-128 ou EAN-128, podem gerar um código compatível com o conceito GS1-128.

**Exemplo com Fwmsprinter**

```
#Include "TOTVS.ch"  
#Include "TBICONN.ch"  
  
User Function T50CODBAR()  
    Local oPrinter :=NIL  
    Local cCODE128 :="(01)05391234567892(15)051231(10)APO1536Z"  
  
    RPCSetEnv("99", "01")  
        oPrinter := FwMsPrinter():New("code.rel", 6, .F., NIL, .T., NIL, NIL, NIL, NIL, NIL, .F., NIL)  
        oPrinter:cPathPDF := "\system\"  
          
        oPrinter:StartPage()  
            oPrinter:FwMsBar("CODE128" /*cTypeBar*/, 41 /*nRow*/, 1 /*nCol*/, cCODE128 /*cCode*/,;  
            NIL/*lCheck*/, /*Color*/, oPrinter /*oPrint*/, .T./*lHorz*/, NIL/*nWidth*/,;  
            NIL/*nHeigth*/, .T./*lBanner*/, "Arial"/*cFont*/, NIL/*cMode*/, .F./*lPrint*/,  
            2/*nPFWidth*/, 2/*nPFHeigth*/, .F./*lCmtr2Pix*/)  
        oPrinter:EndPage()  
  
        oPrinter:Setup()  
        oPrinter:Preview()  
    RPCClearEnv()  
Return (NIL)
```
