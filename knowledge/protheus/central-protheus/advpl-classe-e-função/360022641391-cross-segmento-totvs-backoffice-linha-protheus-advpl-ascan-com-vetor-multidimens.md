---
article_id: 360022641391
category: ADVPL - Classe e Função
content_hash: 75d04a44b1f374c7f43f2084d1d3672205e83b47176eda5b627d014c1c87805c
fetched_at: '2026-06-28T22:40:14.395448+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - AScan() com vetor
  multidimensional
type: support-article
updated_at: '2024-01-31T10:26:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022641391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-AScan-com-vetor-multidimensional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao utilizar o a função AScan() para encontrar um campo dentro de um vetor multidimensional de três níveis ou mais, o mesmo não está sendo encontrado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019829532/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**A função AScan() avalia apenas o segundo nível do vetor, assim sendo, caso o campo avaliado esteja no terceiro nível, a função sempre retornará zero  
  
**Solução**Caso o vetor seja composto de apenas um item pode ser utilizado o exemplo abaixo:

ESTRUTURA

```
AVECTOR: VETOR  
AVECTOR[1]: ITEM 1  
AVECTOR[1][1]: DADO 1  
AVECTOR[1][1][1]: CAMPO 1  
AVECTOR[1][1][2]: VALOR 1  
AVECTOR[1][1][2]: NIL 1  
AVECTOR[1][2]: DADO 2  
AVECTOR[1][2][1]: CAMPO 2  
AVECTOR[1][2][2]: VALOR 2  
AVECTOR[1][2][2]: NIL 2
```

CÓDIGO

```
// nPosField := AScan(aVector, {|x| AllTrim(x[1]) == "W2_COND_PA"})  
nPosField := AScan(aVector[1], {|x| AllTrim(x[1]) == "W2_COND_PA"})  
  
// EXIBIÇÃO DE MENSAGEM  
ConOut(Repl("-", 80))  
ConOut(PadC("Field: W2_COND_PA | Content: " + aVector[1][nFieldPos][2], 80))  
ConOut(Repl("-", 80))
```

Contudo caso o vetor tenha mais de um item na estrutura, utilize o seguinte exemplo:  
  
ESTRUTURA

```
AVECTOR: VETOR  
AVECTOR[1]: ITEM 1  
AVECTOR[1][1]: DADO 1  
AVECTOR[1][1][1]: CAMPO 1  
AVECTOR[1][1][2]: VALOR 1  
AVECTOR[1][1][2]: NIL 1  
AVECTOR[2]: ITEM 2  
AVECTOR[2][1]: DADO 1  
AVECTOR[2][1][1]: CAMPO 1  
AVECTOR[2][1][2]: VALOR 1  
AVECTOR[2][1][2]: NIL 1
```

CÓDIGO

```
// LAÇO DE REPETIÇÃO PARA A QUANTIDADE DE ITENS  
For nX := 1 To Len(aVector)  
    // nPosField := AScan(aVector, {|x| AllTrim(x[1]) == "W2_COND_PA"})  
    nPosField := AScan(aVector[nX], {|x| AllTrim(x[1]) == "W2_COND_PA"})  
  
   // EXIBIÇÃO DE MENSAGEM  
   ConOut(Repl("-", 80))  
   ConOut(PadC("Field: W2_COND_PA | Content: " + aVector[nX][nFieldPos][2], 80))  
   ConOut(Repl("-", 80))  
Next nX
```

**Saiba mais**  
[Função ASCAN](http://tdn.totvs.com/pages/viewpage.action?pageId=23889121)
