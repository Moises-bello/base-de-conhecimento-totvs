---
content_hash: b35cab886a31e972a6c28a05e3fd48455464a84ab640326bf3f9a60df6a49a80
fetched_at: '2026-07-02T19:24:23.316116+00:00'
page_id: '447090383'
product: protheus
source: tdn-tec
title: Reflection.getClassAnnotationList
type: documentation
url: https://tdn.totvs.com/display/tec/Reflection.getClassAnnotationList
version: 7
---

Reflection.getClassAnnotationList

Retorna uma array com todas as **Annotations** utilizadas na classe.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| ``` cClassName ``` | caractere | Nome da classe cujas **Annotations** serão retornadas | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aRet | Array | Retorna um array que contém em cada posição um objeto **Json** com a sua respectiva **Annotation**. Seu valor será NIL caso nenhuma **Annotation** seja encontrada. |

## Exemplos

cppEclipseexemplo1.tlpptrue 0)
conout(aRet[1]["empresa"])
conout(aRet[2]["tipo"])
else
conout('Não foi encontrada nenhuma Annotation na classe declarada !')
endif
return
]]>

## Resultado do Exemplo

Totvs

Software

## Abrangência

17.3.0.3

## Veja também
