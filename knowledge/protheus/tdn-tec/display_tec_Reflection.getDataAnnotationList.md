---
content_hash: a66b6a3dc1651d1c579ace20b37654caaf98485ff3753ad253ac1e71e0f91430
fetched_at: '2026-07-02T19:24:23.321930+00:00'
page_id: '447090480'
product: protheus
source: tdn-tec
title: Reflection.getDataAnnotationList
type: documentation
url: https://tdn.totvs.com/display/tec/Reflection.getDataAnnotationList
version: 7
---

Reflection.getDataAnnotationList

Retorna um array contendo as **Annotations** atribuídas a uma propriedade de um objeto.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| ``` xParam** ``` | objeto/caractere\*\* | Objeto instância da classe/nome da classe\*\* onde será procurado/a a **Annotation**. | X |  |
| ``` cPropertyName ``` | caractere | Indica o nome da propriedade onde será procurada a **Annotation** | X |  |

Implementação de comportamento

A partir do *build* **24.3.0.0**, também haverá a opção de passar simplesmente o **nome** da classe em **xParam,** conforme exemplo 2. Mas continua valendo a passagem da instância do objeto (exemplo 1). 

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aRet | Array | **Array** contendo em cada posição um objeto **Json** contendo o valor de cada **Annotation** atribuída a propriedade do objeto. Caso nenhuma **Annotation** seja encontrada, retorna NIL. |

## Exemplos

cppEclipseexemplo1.tlpptruecppEclipseexemplo2.tlpptrue

## Resultado do Exemplo

Primeira Annotation

Segunda Annotation

## Abrangência

17.3.0.3

## Veja também
