---
content_hash: 012731dcb2600693f6f29f51bf6f9d68a70232c718fb1adb031d1d1d54739c3d
fetched_at: '2026-07-02T19:24:28.745073+00:00'
page_id: '849115198'
product: protheus
source: tdn-tec
title: Reflection.getClassSourceName
type: documentation
url: https://tdn.totvs.com/display/tec/Reflection.getClassSourceName
version: 2
---

Reflection.getDataAnnotation

Efetua a busca de uma **Annotation** atribuída a uma classe e retorna o fonte onde a mesma foi encontrada.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| ``` cClassName ``` | caractere | Nome da classe onde será procurada a **Annotation** | X |  |
| ``` cAnnotationName ``` | caractere | Nome da **Annotation** que será procurada. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| cRet | caractere | Retorna uma string com o nome do fonte onde a **Annotationfoi** encontrada. Caso não encontre o retorno é vazio. |

## Exemplos

cppEclipseexemplo1.tlpptruecppEclipseexemplo2.tlpptrue 'U' .and. !empty(cRet))
Conout("The source name of annotation is: " + cValToChar(cRet))
else
Conout('Erro na execução da Reflection.getClassSourceName')
endif
Return]]>

## Resultado dos Exemplos

exemplo1.tlpp

## Abrangência

24.3.0.0

## Veja também
