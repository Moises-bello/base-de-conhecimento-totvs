---
article_id: 6442739708439
category: Configurações
content_hash: 4464ff8e0e1330effa3ee8e475b64e2bb89e508a2f2732cb368bf321edb9cf4e
fetched_at: '2026-06-28T22:46:29.876980+00:00'
product: rm
section_id: 1500000835121
source: central-rm
title: RH - RM - PTO - Parâmetros do feriado no sindicato
type: support-article
updated_at: '2025-02-07T13:28:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6442739708439-RH-RM-PTO-Par%C3%A2metros-do-feriado-no-sindicato
---

**Considera apenas o feriado** Habilitando este parâmetro o sistema irá considerar o intervalo de horas cadastrado para o feriado independentemente das batidas realizadas pelo funcionário.  
Exemplo:  
Feriado: Dia 01/05/2022 - Início: 00:00 e Fim: 24:00

Jornada: 22:00 - 05:00

Resultado Feriado

|  |  |  |
| --- | --- | --- |
| **Data** | **Entrada 1** | **Saída 1** |
| 30/04/2022 | 22:00 |  |
| 01/05/2022 | Feriado |  |
| 02/05/2022 |  | 05:00 |

**Considera jornada planejada que iniciou no feriado** Habilitando este parâmetro o sistema irá considerar a batida iniciada no dia do feriado até a saída da jornada como feriado.  
Exemplo:  
Feriado: Dia 01/05/2022 - Início: 00:00 e Fim: 24:00

Jornada: 22:00 - 05:00

Resultado Feriado

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Entrada 1** | **Saída 1** | **Entrada 2** |
| 30/04/2022 | 22:00 |  |  |
| 01/05/2022 |  | 05:00 | 22:00 - [Feriado] |
| 02/05/2022 |  | 05:00 - [Feriado] | 22:00 |

**Considera jornada planejada que terminou no feriado** Habilitando este parâmetro o sistema irá considerar a batida iniciada no dia antes do feriado até a saída da jornada no dia do feriado.  
Exemplo:  
Feriado: Dia 01/05/2022 - Início: 00:00 e Fim: 24:00  
Jornada: 22:00 - 05:00

Resultado Feriado

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Entrada 1** | **Saída 1** | **Entrada 2** |
| 30/04/2022 | 22:00 - [Feriado] |  |  |
| 01/05/2022 |  | 05:00 - [Feriado] | 22:00 |
| 02/05/2022 |  | 05:00 | 22:00 |

**Substitui jornada planejada que faz interseção com o feriado** Habilitando este parâmetro o sistema irá considerar toda a jornada que fizer interseção com o feriado.

Exemplo:

Feriado: Dia  01/05/2022 = Início: 00:00 e Fim: 24:00

Exemplo:  
Horário planejado:  
Dia 1 = 22:00 +05:00  
Dia 2 = 22:00 +05:00  
Dia 3 = 22:00 +05:00  
   
Será considerado:  
Dia 1 = 22:00 +05:00 FERIADO  
Dia 2 = 22:00 +05:00 FERIADO  
Dia 3 = 22:00 +05:00

**Substitui jornada planejada que iniciou no feriado, até o fim do feriado** Habilitando este parâmetro o sistema irá considerar a batida iniciada no dia do feriado até a hora fim cadastrada para o feriado.  
Exemplo:  
Feriado: Dia 01/05/2022 - Início: 00:00 e Fim: 24:00  
Jornada: 22:00 - 05:00

Resultado Feriado

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Entrada 1** | **Saída1** | **Entrada2** |
| 30/04/2022 | 22:00 |  |  |
| 01/05/2022 |  | 05:00 | 22:00 - [Feriado até 24:00] |
| 02/05/2022 |  | 05:00 | 22:00 |

**Considera extras de refeição no feriado :** Habilitando este parâmetro o sistema irá calcular extra de refeição em feriados.

Exemplo 1:

Feriado: Dia 01/05/2022 -  Início: 00:00 e Fim: 24:00  (Extra Não Autorizada)

Horário Planejado: 08:00-12:00-14:00-18:00

Batida Realizada: 08:00-12:22-13:30-18:00

 Resultado da ocorrência:

| Inicio | Fim | Tipo de ocorrência | Descrição |
| --- | --- | --- | --- |

| 08:00 | 12:00 | EFN | Extra Feriado Não Autorizado |
| 12:00 | 12:22 | ERFN | Extra Refeição Feriado Não Autorizado |
| 13:30 | 14:00 | ERFN | Extra de Refeição Feriado Não Autorizado |
| 14:00 | 18:00 | EFN | Extra Feriado Não Autorizado |
