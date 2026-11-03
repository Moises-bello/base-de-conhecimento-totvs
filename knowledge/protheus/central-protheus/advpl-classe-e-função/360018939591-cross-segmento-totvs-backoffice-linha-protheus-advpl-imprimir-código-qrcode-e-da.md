---
article_id: 360018939591
category: ADVPL - Classe e Função
content_hash: af53bd857ae84624ff0fa28b59aee88d19339c07a68f95dd9fb0055771bfdf3e
fetched_at: '2026-06-28T22:40:14.192490+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Imprimir código
  QRCODE e DataMatrix em impressora térmica
type: support-article
updated_at: '2025-08-25T12:02:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018939591-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Imprimir-c%C3%B3digo-QRCODE-e-DataMatrix-em-impressora-t%C3%A9rmica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34420605969815)Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como imprimir código QRCODE em impressora térmica?

**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**

As funções de impressão térmica padrão (**MSCB**) não possuem um parâmetro nativo para impressão de **códigos 2D**, como **QRCode** e **DataMatrix**. Diante de uma necessidade específica de um cliente, desenvolvemos uma solução alternativa.   
É crucial entender que este método é uma solução paliativa e deve ser rigorosamente testado e avaliado para verificar sua aderência à regra de negócio e à necessidade específica do projeto.

**A - Fluxo da Solução Implementada (ZEBRA com FwQrCode)**

1. **Geração do QR Code:**  
   Utilizamos a função **FwQrCode**. Por padrão, o **QR Code** gerado é salvo como uma imagem no diretório **TEMP** do Windows. O caminho completo do arquivo pode ser visualizado durante o debug, em uma propriedade do objeto retornado pela função.
2. **Pré-Processamento da Imagem:**  
   A impressora exige que a imagem esteja no formato monocromático de 16 bits. Para esta conversão, utilizamos uma ferramenta como o Paint do Windows:  
   Abra a imagem gerada.  
   Redimensione-a para o tamanho adequado à etiqueta.  
   Salve-a novamente, selecionando a qualidade Monocromático de 16 bits.
3. **Conversão para Formato da Impressora (.GRF):**  
   A imagem processada precisa ser convertida para o formato proprietário **.GRF**.  
   Esta conversão deve ser feita utilizando um software específico, como o **Zebra Designer Studio** (disponibilizado pela fabricante) ou outra ferramenta com essa funcionalidade.
4. **Implementação no Sistema:**  
   O arquivo \***.GRF** final deve ser salvo no diretório **system** do **RootPath** da aplicação.  
   A função de impressão deve ser configurada para referenciar este arquivo pelo nome completo, incluindo a extensão **.GRF**.  
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

* Na conversão deve-se atentar ao tamanho da imagem com o tamanho da etiqueta.

**B - Imagem usando comando na linguagem da impressora (ZPL)**

* Como alternativa, a função **MSCBWrite** também pode ser empregada no processo de impressão.   
  Este método permite enviar comandos diretamente na linguagem da impressora (**ZPL**, por exemplo), incluindo a manipulação de imagens para a geração de **códigos 2D**.  
  O trecho de código abaixo foi utilizado para implementar essa solução por meio da função **MSCBWrite**:

```
#Include "TOTVS.ch"  
#Include "TBICONN.ch"  
#Include "TBICODE.ch"  
  
User Function ImpCod()  
Local cPorta := "LPT1"  
Local cModelo := "ZEBRA"  
  
    MSCBPrinter(cModelo, cPorta, NIL, NIL, .F., NIL, NIL, NIL, , NIL, .F.) // CONFIGURAÇÃO DA IMPRESSORA  
    MSCBChkStatus(.F.) // VERIFICA STATUS DA IMPRESSORA  
  
    // INICIA A IMPRESSÃO  
    MSCBBEGIN(1,6)  
   
    //PASSA O COMANDO PARA A IMPRESSORA  
    MSCBWRITE("^FO50,50^BXN,60,200,0,0,M,'011234567890123421ABCDEFG'^FS")  
  
    // FINALIZA IMPRESSÃO  
    MSCBEND()  
    MSCBCLOSEPRINTER()  
  
Return (NIL)
```

**Importante:**

Ressaltamos que as soluções propostas são somente paliativas, já que as funções de impressão térmica **MSCB**, por padrão, não suportam a impressão de **códigos 2D**.

**Saiba mais**

[FwQRCode](https://tdn.totvs.com.br/display/public/framework/FwQrCode)[MSCBWrite](https://tdn.totvs.com/pages/releaseview.action?pageId=6090943)  
[MSCBPrinter](https://tdn.totvs.com.br/display/public/mp/MSCBPrinter+-+Configura+Impressora+--+30557)
