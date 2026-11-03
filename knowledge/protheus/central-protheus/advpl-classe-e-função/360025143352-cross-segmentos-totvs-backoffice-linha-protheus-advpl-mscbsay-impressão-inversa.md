---
article_id: 360025143352
category: ADVPL - Classe e Função
content_hash: 3c5f344684e9fc81ca482c82b51d21950f8899a3ef28c79f15095b60c6ebf362
fetched_at: '2026-06-28T22:40:20.528048+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - MSCBSAY impressão
  inversa
type: support-article
updated_at: '2022-01-14T21:04:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025143352-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-MSCBSAY-impress%C3%A3o-inversa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Precisamos desenvolver uma etiqueta com fundo invertido é possível?  
Estou utilizando a classe MSCBSAY.  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Conforme documentação da função [MSCBSay](http://tdn.totvs.com/display/public/mp/MSCBSay+-+Imprime+uma+String+--+30801) o parâmetro lReverso imprime em reverso quando estiver sobre um box preto, desta forma se faz necessário definir um box utilizando a função [MSCBBox](http://tdn.totvs.com/display/public/mp/MSCBBox+-+Imprime+um+box+--+30803). Para imprimir um box com fundo preto manipule o parâmetro nEspessura e defina "B" no cCor. Para exemplificar segue um teste, realizado na impressora Zebra modelo S600, nele imprimo um box com 1cm de altura com fundo preto e a string em branco.

```
Obs. recurso só está disponível para linguagem ZPL
```

**Exemplo de teste**

```
#include 'protheus.ch'   
  
User Function MSCBWR()  
// Exemplo usando o padrão de programação Zebra (família ZPL)  
  
Local cPorta := "LPT1"  
Local cModelo := "ZEBRA"  
  
MSCBPRINTER(cModelo,cPorta, , , .F., , , , ,,.f. , )   
 MSCBCHKSTATUS(.F.)  
  
cFonteT := "F"  
 cTam2 := "020,008" //15  
  
MSCBBEGIN(1,4,10) //Inicio da Imagem da Etiqueta  
  
MSCBBOX(1,1,100,10,40,"B") //Monta BOX  
 MSCBSAY(35,4.5,"TESTE FUNDO","N",cFonteT,cTam2,.T.)  
  
MSCBEND()  
  
MSCBCLOSEPRINTER()  
  
Return
```
