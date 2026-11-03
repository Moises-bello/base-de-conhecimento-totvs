---
content_hash: d0eabe0b63d339e1628eb13949d8669aba3e8dc7b26d4aeeb1167ca8c3e590a2
fetched_at: '2026-06-29T00:10:10.720459+00:00'
page_id: '452719918'
product: rm
source: tdn-rm
title: Fórmulas / Funções - S
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719918
version: 2
---

**Fórmulas / Funções - S**

* **Função SEN:** Retorna o seno de um valor.

**Sintaxe:** SEN (VALOR)

**Tipo de Retorno:** Valor

* **Função STR:** Retorna número de acordo co máscara informada, que pode ser composta da seguinte forma: Com noves: o número será completado com espaços brancos à esquerda. Com zeros ou '(minúsculo ou maiúsculo): o número será completado com zeros à esquerda (pode-se usar separador de decimais: '.'(ponto) ou ','(vírgula).

**Sintaxe:** STR (VALOR, STRING)

**Tipo de Retorno:** String

**Exemplo:** STR (CHAPA, '') – retornará a chapa do empregado do empregado com zeros à esquerda. STR (27, '') – retornará 027 STR (12, ',99') – retornará 12,00 STR (5, '.00') – retornará 05.00

* **Função STRLEFT:** Retorna número de caracteres da string da direita para a esquerda..

**Sintaxe:** STRLEFT (STRING, Nº DE CARACTERES)

**Tipo de Retorno:** String

**Exemplo:**

STRLEFT (TABFUNC (', '), 5)

Nome do funcionário: ITAMAR MENDES DA SILVEIRA.

Retornará "VEIRA

* **Função STRRIGHT:** Retorna "n" caracteres da string a partir da esquerda para a direita.

**Sintaxe:** STRRIGHT (STRING, Nº DE CARACTERES)

**Tipo de Retorno:** String

**Exemplo:**

STRRIGHT ((TABFUNC (', '), 6)

Nome do funcionário: ITAMAR MENDES DA SILVEIRA

Retornará: ITAMAR.

* **Função SUBSTR:** Retorna pedaço de uma string, a partir de uma posição determinada.

**Sintaxe:** SUBSTR (STRING, INÍCIO, NÚMERO DE CARACTERES)

**Tipo de Retorno:** String

**Exemplo:**

1) SUBSTR( TABFUNC (', '), 1 , 10)

Essa fórmula retornará o nome do funcionário com dez caracteres a partir da primeira posição do nome.

Sobre a função TABFUNC, incluída no exemplo, ver o tópico Funções - T.

2) SUBSTR( TABFUNC (', '), 8 , 18)

Nome do funcionário: ITAMAR MENDES DA SILVEIRA.

Retornará: MENDES DA SILVEIRA.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funções Específicas do TOTVS Automação de Ponto
