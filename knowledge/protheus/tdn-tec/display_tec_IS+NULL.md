---
content_hash: 4b06256e59e8cdac00ed28ec5ba992a921cae71431964e7e140c9829fe57cb21
fetched_at: '2026-07-02T19:24:27.986437+00:00'
page_id: '701677554'
product: protheus
source: tdn-tec
title: IS NULL
type: documentation
url: https://tdn.totvs.com/display/tec/IS+NULL
version: 14
---

IS NULL (Expressão)

A expressão **IS NULL** é utilizada para avaliar se o conteúdo de uma variável ou resultado de alguma operação ou retorno de função é **NULO**.

Esta mesma expressão também pode ser utilizada como **IS NOT NULL**.

IMPORTANTE

---

Um conteúdo **NULL** não é um conteúdo em branco mas sim um conteúdo **NULO**, onde é caracterizado por ser do tipo **CHAR** ou **VARCHAR** com tamanho de zero caracteres, ou seja, vazio.

Em resumo, "*não é possível comparar um valor com conteúdo **NULL** com outro valor de conteúdo também **NULL"***, muito menos um valor de conteúdo **NULL** com outro valor qualquer diferente de **NULL** usando operadores comuns como =, >=, <=, <>, !=. Neste caso é preciso sempre utilizar a expressão **IS NULL** ou **IS NOT NULL** conforme a sintaxe abaixo.

## Sintaxe

|  |
| --- |
| `IF [VALUE] IS { NOT` `} NULL THEN`  `(...)`  `END IF` |

## Parâmetros

| Nome | Tipo | Descrição |
| --- | --- | --- |
| ``` VALUE ``` | Qualquer tipo 4GL | Nome da variável, função ou valor fixo que deve ser avaliado se seu conteúdo é **NULO** ou não.                               **TRUE** - Conteúdo é nulo.                                                                                                                                 **FALSE** - Conteúdo não é nulo. |

## Observações

* Uma variável do tipo caractere (**CHAR** ou **VARCHAR**) onde seu conteúdo tenha um ou mais caracteres preenchidos ou no mínimo **UM** espaço em branco já é considerado **NÃO NULO**. Já se o conteúdo for vazio de tamanho zero, onde *length(<var>) = 0*, indica que seu conteúdo **É NULO (*IS NULL*).**
* Uma variável do tipo numérica, por exemplo **SMALLINT,** quando recebe um conteúdo inválido que não é numérico, assume automaticamente o valor **NULL**, ou seja *LET variavelnumerica = " "* irá gerar conteúdo **NULL** na variável.
* **ATENÇÃO PARA ESTE CASO!** Uma variável caractere que tenha o valor atual em branco como conteúdo, ou seja, um ou mais espaços em branco, quando for utilizada com uma expressão *variavel CLIPPED*, irá automaticamente retornar um conteúdo **NULL**, pois a diretiva **CLIPPED** tem como objetivo eliminar todos os espaços em branco existentes no final do conteúdo de um valor tipo **CHAR** ou **VARCHAR**, gerando neste caso um conteúdo vazio com tamanho 0 (zero), caracterizando o valor como **NULL**.

rubyConfluenceEXEMPLOS DE EXPRESSÕES
