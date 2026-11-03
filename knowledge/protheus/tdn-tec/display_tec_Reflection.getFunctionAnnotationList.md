---
content_hash: 9b1ab5f3c3ce247f84ea2ee46a156841812a663c9a424509015d1c15fb5326a8
fetched_at: '2026-07-02T19:24:23.328452+00:00'
page_id: '447090514'
product: protheus
source: tdn-tec
title: Reflection.getFunctionAnnotationList
type: documentation
url: https://tdn.totvs.com/display/tec/Reflection.getFunctionAnnotationList
version: 2
---

Reflection.getFunctionAnnotationList

Retorna uma lista contendo as **Annotation** a partir de um programa fonte e uma função específica.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| ``` cSourceName ``` | caractere | Programa fonte onde será efetuada a busca | X |  |
| ``` cPropertyName ``` | caractere | Função contendo as **Annotations** | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aRet | array | Array onde cada posição é um objeto do tipo **Json** cujas propriedades são as **Annotations**  e seus respectivos valores. Caso não encontre nenhuma **Annotation**  o retorno será NIL. |

## Exemplos

cppEclipsetest\_doc\_resourceGetFunctionAnnotationList.tlpptruecppEclipsetest\_doc\_getFunctionAnnotationList.tlpptrue0)
conout(aRet[1]["empresa"])
conout(aRet[2]["segmento"])
conout(aRet[3]["setor"])
else
conout('Não foram encontradas Annotations com os parametros pesquisados')
endif
return]]>

## Resultado do Exemplo

Totvs  
Software  
Tecnologia

```

```

## Abrangência

17.3.0.3

## Veja também
