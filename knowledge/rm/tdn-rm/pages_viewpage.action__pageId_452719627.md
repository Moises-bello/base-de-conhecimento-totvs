---
content_hash: e04a7e8bb494d4b9b00d240a8508b00676993530f972c4d064851156983fa121
fetched_at: '2026-06-29T00:10:09.316612+00:00'
page_id: '452719627'
product: rm
source: tdn-rm
title: Fórmulas / Funções - B (PTO)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719627
version: 3
---

**Fórmulas / Funções - B**

* **Função BASEDIAFER:** Retorna o número de horas base ( em minutos) que o funcionário deveria trabalhar se o dia não fosse feriado.

**Sintaxe:** BASEDIAFER ( DATA )

**Tipo de Retorno:** Valor

**Exemplo:** BASEDIAFER ( '12/10/2000') A função irá retornar as horas base ( em minutos ) do dia informado ('/10/2000') se ele não fosse feriado. Dia 12/10/2000 Feriado 00:00 às 24:00

**Horário do funcionário:** Dia 12/10/2000 14:00E 20:00S – o sistema irá retornar 360 minutos.

* **Função BATDIA:** Retorna as batidas efetuadas pelo funcionário no dia determinado.

**Sintaxe:** BATDIA ( DATA )

**Tipo de Retorno:** Valor

**Exemplo:** BATDIA ('10/11/2000') A função irá retornar as batidas do funcionário do dia 10/11/2000 08:00E 12:00S 14:00E 18:00S 18:10E 23:15S

* **Função BHATRFAL:** Retorna o saldo de horas de atrasos e faltas do banco de horas diário até a data estipulada. Ela pode considerar o saldo anterior (1) ou não considerar o saldo anterior (0), o saldo anterior é referente aos valores que estão na tabela ATUALFUN.

**Sintaxe:** BHATRFAL: (DATA, STRING).

**Tipo de Retorno:** Valor

**Exemplo:** BHATRFAL: ('07/07/1999', '') A função irá retornar o saldo de horas de atraso e falta até o dia 07/07 do banco de horas diário considerando também o saldo inicial de horas.

* **Função BHEXTRA:** Retorna o saldo de horas extras do banco de horas diário até a data estipulada. Ela pode considerar o saldo anterior (1) ou não considerar o saldo anterior (0), o saldo anterior é referente aos valores que estão na tabela ATUALFUN.

**Sintaxe:** BHEXTRA: (DATA, STRING).

**Tipo de Retorno:** Valor

**Exemplo:** BHEXTRA: ('07/07/1999', '') A função irá retornar somente o saldo de horas extras até o dia 07/07 do banco de horas diário.

|  |  |
| --- | --- |
|  | Informações Complementares |

[  
Funções Específicas do TOTVS Automação de Ponto|Fórmulas - PTO]
