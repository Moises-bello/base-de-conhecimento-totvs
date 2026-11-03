---
content_hash: 428f6cfee9be9dadc03cf96b89ba377c4499f061c728ddc6e1b6bf5b7b83bbb6
fetched_at: '2026-06-29T00:10:06.853450+00:00'
page_id: '452719344'
product: rm
source: tdn-rm
title: Feriados
type: documentation
url: https://tdn.totvs.com/display/LRM/Feriados
version: 18
---

**Considera apenas o feriado** :

Importante

* Ao marcar o parâmetro "Considera extras de refeição no feriado" e utilizando essa solução de conflito, no horário por limite , o produto irá verificar qual o maior intervalo de limite após realizar a quebra do intervalo (antes ou após o início do feriado), para aplicar a ausência e a extra de refeição, caso contrário o sistema realiza um corte na jornada, podendo alocar a marcação de ausência de refeição após às 00:00.

**Exemplo Horário Semiflexível:** 19:00  20:00  21:00 +07:00

Limite de Refeição: 20:00 23:59  
Executado: 18:58 | 21:54 | 22:51 | +07:00

Considera extras de refeição no feriado **Desmarcado.**

**Ocorrências:**

18:58 | 21:54 | Extra Feriado Autorizado  
21:54 | 22:54 | Ausência de Refeição

22:54 | 00:00| Extra Feriado Autorizado  
00:00 | 07:00 | Trabalho

---

**Exemplo Horário Semiflexível:** 19:00  20:00  21:00 +07:00

Limite de Refeição: 20:00 04:30 (intervalo após 00:00 maior)  
Executado: 18:58 | 21:54 | 22:51 | +07:00

Considera extras de refeição no feriado **Marcado.**

**Ocorrências:**

18:58 | 21:54 | Extra Feriado Autorizado  
22:51 | 00:00 | Extra Feriado Autorizado  
00:00 | 01:00 | Ausência de Refeição  
01:00 | 07:00 | Trabalho

---

**Exemplo Horário Semiflexível:** 19:00  20:00  21:00 +07:00

Limite de Refeição: 20:00 03:30 (intervalo após 00:00 menor)  
Executado: 18:58 | 21:54 | 22:51 | +07:00

Considera extras de refeição no feriado **Marcado.**

**Ocorrências:**

18:58 | 21:54 | Extra Feriado Autorizado  
21:54 | 22:54 | Ausência de Refeição  
22:54 | 00:00 | Extra Feriado Autorizado  
00:00 | 03:30 | Trabalho  
03:30 | 07:00 | Extra Feriado Autorizado

---

**Considera jornada planejada que iniciou no feriado :** Habilitando este parâmetro o sistema irá considerar a batida iniciada no dia do feriado até a saída da jornada como feriado.  
Exemplo:  
Feriado: Dia 02/02/2011 - Início: 00:00 e Fim: 24:00  
Horário Planejado

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Entrada 1** | **Saída 1** | **Entrada 2** |
| 01/02/2011 | 22:00 |  |  |
| 02/02/2011 |  | 05:00 | 22:00 |
| 03/02/2011 |  | 05:00 |  |

Resultado Feriado

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Entrada 1** | **Saída 1** | **Entrada 2** |
| 01/02/2011 | 22:00 |  |  |
| 02/02/2011 |  | 05:00 | 22:00 - [Feriado] |
| 03/02/2011 |  | 05:00 - [Feriado] | 22:00 |

**Considera jornada planejada que terminou no feriado :** Habilitando este parâmetro o sistema irá considerar a batida iniciada no dia antes do feriado até a saída da jornada no dia do feriado.  
Exemplo:  
Feriado: Dia 02/02/2011 - Início: 00:00 e Fim: 24:00  
Horário Planejado

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Entrada 1** | **Saída 1** | **Entrada 2** |
| 01/02/2011 | 22:00 |  |  |
| 02/02/2011 |  | 05:00 | 22:00 |
| 03/02/2011 |  | 05:00 |  |

Resultado Feriado

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Entrada 1** | **Saída 1** | **Entrada 2** |
| 01/02/2011 | 22:00 - [Feriado] |  |  |
| 02/02/2011 |  | 05:00 - [Feriado] | 22:00 |
| 03/02/2011 |  | 05:00 | 22:00 |

**Substitui jornada planejada que faz interseção com o feriado :** Habilitando este parâmetro o sistema irá considerar toda a jornada que fizer interseção com o feriado.

Exemplo:

Feriado: Dia  02/02/2011 = Início: 00:00 e Fim: 24:00

Exemplo:  
Horário planejado:  
Dia 1 = 22:00 +05:00  
Dia 2 = 22:00 +05:00  
Dia 3 = 22:00 +05:00  
   
Será considerado:  
Dia 1 = 22:00 +05:00 FERIADO  
Dia 2 = 22:00 +05:00 FERIADO  
Dia 3 = 22:00 +05:00

**Substitui jornada planejada que iniciou no feriado, até o fim do feriado :** Habilitando este parâmetro o sistema irá considerar a batida iniciada no dia do feriado até a hora fim cadastrada para o feriado.  
Exemplo:  
Feriado: Dia 02/02/2011 - Início: 00:00 e Fim: 24:00  
Horário Planejado

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Entrada 1** | **Saída1** | **Entrada2** |
| 01/02/2011 | 22:00 |  |  |
| 02/02/2011 |  | 05:00 | 22:00 |
| 03/02/2011 |  | 05:00 |  |

Resultado Feriado

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Entrada 1** | **Saída1** | **Entrada2** |
| 01/02/2011 | 22:00 |  |  |
| 02/02/2011 |  | 05:00 | 22:00 - [Feriado até 24:00] |
| 03/02/2011 |  | 05:00 | 22:00 |

**Considera extras de refeição no feriado :** Habilitando este parâmetro o sistema irá calcular extra de refeição em feriados.

Exemplo 1:

Feriado: Dia 21/04/2021 -  Início: 00:00 e Fim: 24:00  (Extra Não Autorizada)

Horário Planejado: 08:00-12:00-14:00-18:00

Batida Realizada: 08:00-12:22-13:30-18:00

 Resultado da ocorrência:

| Inicio | Fim | Tipo de ocorrência | Descrição |
| --- | --- | --- | --- |
| 08:00 | 12:00 | EFN | Extra Feriado Não Autorizado |
| 12:00 | 12:22 | ERFN | Extra Refeição Feriado Não Autorizado |
| 13:30 | 14:00 | ERFN | Extra de Refeição Feriado Não Autorizado |
| 14:00 | 18:00 | EFN | Extra Feriado Não Autorizado |

Exemplo 2:

Feriado: Dia 26/04/2021 -  Início: 00:00 e Fim: 24:00  (Extra Autorizada)

Horário Planejado: 08:00-12:00-14:00-18:00

Batida Realizada: 08:00-12:22-13:30-18:00

 Resultado da ocorrência:

| Inicio | Fim | Tipo de ocorrência | Descrição |
| --- | --- | --- | --- |
| 08:00 | 12:00 | EFN | Extra Feriado Autorizado |
| 12:00 | 12:22 | ERFA | Extra Refeição Feriado Autorizado |
| 13:30 | 14:00 | ERFA | Extra de Refeição Feriado  Autorizado |
| 14:00 | 18:00 | EFN | Extra Feriado Autorizado |
