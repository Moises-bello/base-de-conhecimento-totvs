---
content_hash: 1279ffaf232b8cd87eb309388b7a319384fd1afa70dddf9e530675e2301fac17
fetched_at: '2026-06-29T00:10:07.720654+00:00'
page_id: '452719422'
product: rm
source: tdn-rm
title: Fórmulas / Funções - I (PTO)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719422
version: 2
---

**Fórmulas / Funções - I**

* **Função INCANO:** Soma ao mês o número de meses e retorna o ano correspondente.

**Sintaxe:** INCANO (MÊS, ANO, NÚMERO DE MESES)

**Tipo de Retorno:** Valor

**Exemplo:**

INCANO(10, 1995, 5) = 1996.

A função somará 5 ao mês de outubro de 1995, retornando 1996.

* **Função INCMES:** Soma ao mês informado o número de meses e retorna o mês correspondente.

**Sintaxe:** INCMES (MÊS, NÚMERO DE MESES PARA SOMAR)

**Tipo de Retorno:** Valor

**Exemplo:** INCMES(10, 20) = 6.

* **Função INDICEDIA:** Retorna o índice ou a letro do horário do funcionário em uma data.

**Sintaxe:** INDICEDIA (DATA , STRING)

**Tipo de Retorno:** String Esta função retorna a letra do horário que está associada no histórico de horário do funcionário para a data informada na fórmula, ou retorna o índice do horário que o funcionário está trabalhando na data informada. Para a função retornar a letra do índice é necessário informar 'no campo STRING. Para a função retornar o índice do horário é necessário informar 'no campo STRING.

**Exemplo:**

Histórico do horário do funcionário: Horário – Código – Letra do índice 01/05/2000 – 0001 – F 10/07/2006 – 0004 – B 17/07/2006 – 0018 – A 24/07/2006 – 0001 – F

**Fórmula:** INDICEDIA ('10/05/2006' , 'L')

Resultado: F Entendendo a fórmula: No dia 10/05/2006 o funcionário está usando o horário de código 0001 e no seu histórico está associado à letra F. INDICEDIA ('09/07/2006' , 'L') Resultado: F Entendendo a fórmula: No dia 09/07/2006 o funcionário está usando o horário de código 0001 e no seu histórico está associado à letra F. INDICEDIA ('15/07/2006' , 'L') Resultado: B Entendendo a fórmula: No dia 15/07/2006 o funcionário está usando o horário de código 0004 e no seu histórico está associado à letra B. INDICEDIA ('10/08/2006' , 'L') Resultado: F Entendendo a fórmula: No dia 10/08/2006 o funcionário está usando o horário de código 0001 e no seu histórico está associado à letra F. INDICEDIA ('09/07/2006' , 'I') Resultado: 7 Entendendo a fórmula: No dia 09/07/2006 o funcionário deve trabalhar no índice 7 do horário de código 0001. INDICEDIA ('10/08/2006' , 'L') Resultado: 4 Entendendo a fórmula: No dia 10/08/2006 o funcionário deve trabalhar no índice 4 do horário de código 0001.

* **Função INT:** Retorna parte inteira de um valor.

**Sintaxe:** INT (VALOR)

**Tipo de Retorno:** Inteiro

**Exemplo****:**

INT (50.3) = 50.

* **Funções INTREF:** Retornar o intervalo de refeição ( em minutos ) em uma determinada data.

**Sintaxe:** INTREF(VALOR , DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

Funcionário tem o seguinte horário no dia 01/06/2000: 08:00 12:00 14:00 18:00 Onde o intervalo de refeição é de 12:00 às 14:00 INTREF(1,'01/06/2000') = início da refeição cadastrada em 01/06/2000

– o sistema irá retornar 720 minutos que se refere a entrada de 12:00 do intervalo de refeição. INTREF(2,'01/06/2000') = fim da refeição cadastrada em 01/06/2000

– o sistema irá retornar 840 minutos que se refere às 14:00 do retorno do intervalo de refeição.

Caso o funcionário tenha mais intervalos de refeição cadastrados no mesmo dia, basta aumentar o índice da refeição ( campo valor da fórmula ).

INTREF(3,'01/06/2000') = 2o início da refeição cadastrada em 01/06/2000

INTREF(4,'01/06/2000') = 2o início da refeição cadastrada em 01/06/2000

* **Função IPERNOT:** Retorna a hora (em minutos) de início do período noturno cadastrado no parâmetro do sistema.

**Sintaxe:** IPERNOT

**Tipo de Retorno:** Valor

**Exemplo:**

IPERNOT = 1320.

* **Função IPM:** Retorna a data do início do período mensal cadastrado no parâmetro do sistema.

**Sintaxe:** IPM

**Tipo de Retorno:** Data

**Exemplo:**

IPM = 01/11/2000

* **Função IPQ:** Retorna a data do início do período quinzenal cadastrado no parâmetro do sistema.

**Sintaxe:** IPQ

**Tipo de** **Retorno:** Data

**Exemplo:** IPQ = 01/11/2000

* **Função IPS:** Retorna a data do início do período semanal cadastrado no parâmetro do sistema.

**Sintaxe:** IPS

**Tipo de Retorno:** Data

**Exemplo:** IPS = 01/11/2000

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funções Específicas do TOTVS Automação de Ponto
