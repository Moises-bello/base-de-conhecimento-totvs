---
content_hash: c8b4a4e216c49c3435f37db85d21c7aee6f734f7bedee07050bd92f131e1c52a
fetched_at: '2026-07-02T19:24:28.750490+00:00'
page_id: '849562297'
product: protheus
source: tdn-tec
title: Reflection.getDataType
type: documentation
url: https://tdn.totvs.com/display/tec/Reflection.getDataType
version: 1
---

Reflection.getDataAnnotation

Retorna o tipo da propriedade de uma classe.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| xParam\*\* | objeto/caractere\*\* | Objeto instância da classe/nome da classe\*\* onde será feita a busca da **Annotation**. | X |  |
| ``` cPropertyName ``` | caractere | Nome da propriedade onde será procurada a **Annotation** | X |  |

implementação de comportamento

A partir do *build* **24.3.0.0**,também haverá a opção de passar simplesmente o **nome** da classe em **xParam,** conforme exemplo 2. Mas continua valendo a passagem da instância do objeto (exemplo 1). 

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| cRet | caracter | Retorna uma string contendo o tipo da propriedade a partir da classe pesquisada. Seu retorno é vazio caso não encontre. |

## Exemplos

cppEclipseclassProgram.tlpptruecppEclipseexemplo2.tlpptrue

## Resultado do Exemplo

numeric

## Abrangência

17.3.0.3

## Veja também
