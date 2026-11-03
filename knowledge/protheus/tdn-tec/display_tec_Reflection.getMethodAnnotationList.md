---
content_hash: f7d37e1bcb01cc860a75d4e19b9d08590db6bc6c4c858353f101f74de6af92b9
fetched_at: '2026-07-02T19:24:23.334581+00:00'
page_id: '447090530'
product: protheus
source: tdn-tec
title: Reflection.getMethodAnnotationList
type: documentation
url: https://tdn.totvs.com/display/tec/Reflection.getMethodAnnotationList
version: 9
---

Reflection.getMethodAnnotationList

Efetua a busca de **Annotations** associadas a um determinado método.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| ``` xParam** ``` | objeto/caractere\*\* | Objeto instância da classe/nome da classe\*\* onde está definido o método cujas **Annotations** serão retornadas | X |  |
| ``` cMethodName ``` | caractere | Método onde serão procuradas as **Annotations** | X |  |

Implementação de comportamento

A partir do *build* **24.3.0.0**, também haverá a opção de passar simplesmente o **nome** da classe em **xParam,** conforme exemplo 2. Mas continua valendo a passagem da instância do objeto (exemplo 1). 

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aRet | array | Array contendo em cada posição um objeto do tipo **Json** onde cada propriedade é o nome da  **Annotation** encontrada. Caso nada seja encontrado, seu valor é NIL. |

## Exemplos

cppEclipseexemplo1.tlpptruecppEclipseexemplo2.tlpptrue

## Resultado dos Exemplos

2

Primeira Annotation

Segunda Annotation

## Abrangência

17.3.0.3

## Veja também
