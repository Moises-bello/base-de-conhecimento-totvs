---
content_hash: 4e24725616388596c5a5611c7e4ccdefe8f2a81537228d04e878f47167f9ddb9
fetched_at: '2026-06-29T00:10:02.637305+00:00'
page_id: '452718989'
product: rm
source: tdn-rm
title: Fórmulas / Funções - F
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718989
version: 2
---

**Fórmulas / Funções - F**

* **Função FOR:** Retorna o resultado de uma fórmula.

**Sintaxe:** FOR ( CÓDIGO DA FÓRMULA )

**Tipo de Retorno:** Indefinido

**Exemplo:**

A fórmula 0508 retorna as batidas do funcionário em um determinado dia.

Então segue o demonstrativo da variável:

FOR ('0508') = Constante literal  0508 Chamada a função FOR  0508 Constante literal  10/11/2000 Chamada a função BATDIA  10/11/2000

Resultado da função BATDIA  08:00E 12:00S 14:00E 18:00S 18:10E 23:15S

Resultado da fórmula  08:00E 12:00S 14:00E 18:00S 18:10E 23:15S

Resultado da função FOR  08:00E 12:00S 14:00E 18:00S 18:10E 23:15S

Resultado da fórmula  08:00E 12:00S 14:00E 18:00S 18:10E 23:15S

* **Função FPERNOT:** Retorna a hora ( em minutos ) do fim do período do adicional noturno informado no Parametrizador do Sindicato.

**Sintaxe:** FPERNOT

**Tipo de Retorno:** Valor

**Exemplo:** FPERNOT = 300 minutos

* **Função FPM:** Retorna a data do fim do período mensal.

**Sintaxe:** FPM

**Tipo de Retorno:** Data

**Exemplo:** FPM = 30/11/2000

* **Função FPQ:** Retorna a data do fim do período quinzenal.

**Sintaxe:** FPQ

**Tipo de Retorno:** Data

**Exemplo:** FPQ = 15/11/2000

* **Função FPS:** Retorna a data do fim do período semanal.

**Sintaxe:** FPS

**Tipo de Retorno:** Data

**Exemplo:** FPS = 07/11/2000

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funções Específicas do TOTVS Automação de Ponto
