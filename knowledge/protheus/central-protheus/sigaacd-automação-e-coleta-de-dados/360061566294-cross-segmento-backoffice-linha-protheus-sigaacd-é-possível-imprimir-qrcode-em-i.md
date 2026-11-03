---
article_id: 360061566294
category: SIGAACD - Automação e Coleta de Dados
content_hash: b5eb7a0949297e9fd91a95656760a33e8554ad1a2ba1a714969237f524701db4
fetched_at: '2026-06-28T22:39:12.695243+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - É possível Imprimir
  QRCODE em impressora térmica?
type: support-article
updated_at: '2025-03-12T12:45:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061566294-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-%C3%89-poss%C3%ADvel-Imprimir-QRCODE-em-impressora-t%C3%A9rmica
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24763346952855) Tempo aproximado para leitura: **00:01:00 min***

**Dúvida**Consigo imprimir QRCODE em impressora térmica?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17  
  
**Solução**

As funções de impressão térmica (MSCB)**não possuem um parâmetro para impressão de códigos 2D (QRCode e DataMatrix)**, todavia temos situações onde determinadas empresas precisam utilizar essa função. Então temos uma função que auxilia nessa possibilidade. Lembrando que é uma forma de tratamento que deve ser testada e avaliada se cabe na regra e necessidade do usuário.

**Cenário de um case utilizando a impressora Zebra modelo S600:**

A impressora que utilizamos no case é uma da marca Zebra, modelo S600. Para gerar o QRCODE utilizamos a função **[FwQrCode](https://tdn.totvs.com.br/display/public/PROT/FwQrCode)**.  
  
Por padrão o QRCode gerado é gravado como imagem na pasta TEMP do próprio Windows, em debug da função poderá ser visualizado no objeto uma propriedade onde está instanciado o diretório onde é gravada a imagem.

1° Passo - Para realizar a conversão, é necessário que a imagem esteja em qualidade 16 bits monocromático, pois é uma exigência da própria impressora (Zebra S600), utilizamos o Paint do Windows para realizar essa modificação salvando a mesma na qualidade descrita e já redimensionando o tamanho.   
  
2° Passo - Utilizar essa imagem que geramos após os processos anteriores na impressão, primeiramente deve-se realizar a conversão para o formato em que a impressora irá reconhecer, em nosso cenário de teste, com a impressora Zebra S600, com a extensão \*.GRF.   
  
3° Passo - Para conversão deve-se utilizar um Studio disponibilizado pela própria fabricante da impressora ou algum programa específico que tenha essa função.   
  
4° Passo - Após obter a imagem com a extensão correta a mesma deverá ser salva no diretório system do RootPath nomeada com a extensão referente.   
  
5° Passo - Utilizamos o fonte abaixo para efetuar a impressão:

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

Observações:

➜ Na conversão deve-se atentar ao tamanho da imagem com o tamanho da etiqueta;

➜ Existe a função **[MSCBWrite,](https://tdn.totvs.com/pages/releaseview.action?pageId=6090943)** que também pode ser utilizada no processo de impressão onde existe a possibilidade de modificar algumas informações da imagem via linguagem da impressora;  
➜ Reforçamos que o procedimento sugerido é um paliativo, por padrão as funções de impressão térmica (MSCB) não suportam impressão de códigos 2D.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados (ACD)*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360002469152-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
