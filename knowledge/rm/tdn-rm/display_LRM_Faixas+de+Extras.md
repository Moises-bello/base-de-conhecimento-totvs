---
content_hash: 7429b1cbe8f6e522945a627ce9f5852484c2b2a6df6edd20fa3fbf3dcfa56b47
fetched_at: '2026-06-29T00:10:04.767653+00:00'
page_id: '452719247'
product: rm
source: tdn-rm
title: Faixas de Extras
type: documentation
url: https://tdn.totvs.com/display/LRM/Faixas+de+Extras
version: 2
---

**Considera faixas de distribuição de horas extras por intervalo de horas**

Com esse parâmetro habilitado o cadastro das faixas de extra será feito por intervalo de horas, ou seja definindo hora início e fim para cada faixa de extra existente.  
Exemplo:  
1ª faixa - Início: 07:00 e Fim: 08:00  
2ª faixa - Início: 18:00 e Fim: 19:00  
3ª faixa - Início: 19:00 e Fim: 20:00  
4ª faixa - Início: 20:00 e Fim: 21:00  
5ª faixa - Início: 21:00 e Fim: 23:59  
   
Horário Planejado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Entrada 2 | Saída1 |
| 25/02/2011 | 08:00 | 12:00 | 14:00 | 18:00 |

Horário Executado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Entrada 2 | Saída1 |
| 25/02/2011 | 07:00 | 12:00 | 14:00 | 23:00 |

Funcionário executou Horas Extras da seguinte forma:  
Início: 07:00 e Fim: 08:00 = 01:00 Extra  
Início: 18:00 e Fim: 23:00 = 05:00 Extras  
   
As Horas Extras serão distribuidas da serguinte forma:  
1ª faixa - Início: 07:00 e Fim: 08:00 = 01:00 Extra  
2ª faixa - Início: 18:00 e Fim: 19:00 = 01:00 Extra  
3ª faixa - Início: 19:00 e Fim: 20:00 = 01:00 Extra  
4ª faixa - Início: 20:00 e Fim: 21:00 = 01:00 Extra  
5ª faixa - Início: 21:00 e Fim: 23:00 = 02:00 Extra  
   
Ao ter este parâmetro marcado em combinação com o parâmetro de Considera Atitude do Evento (localizado na aba de Banco de Horas) será levado em consideração a atitude cadastrada no evento da faixa de extras.

**Tipo de faixa**

Documentação:[IMPLEMENTAÇÃO PARA ATENDER NOVAS REGRAS DA CCT SINDADOS](https://tdn.totvs.com/display/public/LRM/DT_CCTSindados)

**Faixa de distribuição de horas extras**

Pelas faixas de distribuição de extras definimos em até cinco faixas de extra normal quantas horas cada faixa irá ter.  
Exemplo:  
1ª faixa - 02:00 - as duas primeiras horas extras  
2ª faixa - 02:00 - a terceira e quarta hora extra  
3ª faixa - 01:00 - a quinta hora extra  
4ª faixa - 01:00 - a sexta hora extra  
5ª faixa - 01:00 - a sétima hora extra  
    
Horário Planejado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Entrada 2 | Saída1 |
| 25/02/2011 | 08:00 | 12:00 | 14:00 | 18:00 |

Horário Executado

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída1 | Entrada 2 | Saída1 |
| 25/02/2011 | 07:00 | 12:00 | 14:00 | 23:00 |

Funcionário executou Horas Extras da seguinte forma:  
Início: 07:00 e Fim: 08:00 = 01:00 Extra  
Início: 18:00 e Fim: 23:00 = 05:00 Extras  
   
As Horas Extras serão distribuidas da serguinte forma:  
1ª faixa - 02:00 - as duas primeiras horas extras  
de 07:00 as 08:00 = 01:00   
de 18:00 as 19:00 = 01:00  
   
2ª faixa - 02:00 - a terceira e quarta hora extra  
de 19:00 as 20:00 = 01:00   
de 20:00 as 21:00 = 01:00  
   
3ª faixa - 01:00 - a quinta hora extra  
de 21:00 as 22:00 = 01:00  
   
4ª faixa - 01:00 - a sexta hora extra  
de 22:00 as 23:00 = 01:00
