---
content_hash: 7274a8c7334538bc932a2adf91849be0b1b2f063312e2d5410deffab7d16ab04
fetched_at: '2026-06-29T00:10:09.387207+00:00'
page_id: '452719652'
product: rm
source: tdn-rm
title: Fórmulas / Funções - A (PTO)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719652
version: 2
---

**Fórmulas / Funções - A**

* **Função ANODT:** Retorna ano de uma data

**Sintaxe:** ANODT(')

**Tipo de Retorno:** Valor

**Exemplo:** ANODT ('/01/1997') Esta função irá retornar 1997

* **Função ATITUDEOCOR:** Retorna a atitude (pagar/descontar ou compensar) das ocorrências ( extras, faltas e atrasos).

**Sintaxe:** ATITUDEOCOR ( DATA , STRING )

**Tipo de Retorno:** String

**Observação:** No campos STRING da função temos que informar o tipo da ocorrência, se é um atraso, uma falta, ou uma extra. Segue os tipos que devem ser utilizados:

A - Atraso, F - Falta, E - Extra Normal, C - Extra Compensado, D - Extra Descanso, R- Extra Feriado

Abaixo estão os possíveis resultados da função:

C – Quando a atitude da ocorrência for Compensar

P – Quando a atitude da ocorrência for Pagar

D – Quando a atitude da ocorrência for Descontar

F – Quando não existir ocorrência para o dia informado, ou o tipo da ocorrência informado no campo STRING estiver incorreto. O resultado será F ( Falso ).

**Exemplos:** ATITUDEOCOR ('02/11/2002' , 'F') Acompanhar a execução da Fórmula: Constante literal  02/11/2002 Constante literal  F Chamada a funcao ATITUDEOCOR  02/11/2002 F Resultado da funcao ATITUDEOCOR  C Resultado da formula  C A falta do dia 02/11/2002 tem a atitude C ( Compensar ). ATITUDEOCOR ('07/11/2002' , 'E') Constante literal  07/11/2002 Constante literal  E Chamada a funcao ATITUDEOCOR  02/11/2002 E Resultado da funcao ATITUDEOCOR  P Resultado da formula  P A hora extra do dia 07/11/2002 tem a atitude P ( Pagar )

* **Função ATRIBUI:** Atribui valor a uma memória

**Sintaxe:** ATRIBUI(NÚMERO DA MEMÓRIA, INDEFINIDO)

**T****ipo de Retorno:** De acordo com o que for atribuído à memória

**Exemplo:** ATRIBUI (1, FOR('')) Memória de nº 1 guardará valor da fórmula de código 0001.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funções Específicas do TOTVS Automação de Ponto
