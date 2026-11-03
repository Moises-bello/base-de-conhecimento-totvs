---
content_hash: 31b8827122deb633e6655d80ec69cc29cab0afd750edc506897170e62916cfac
fetched_at: '2026-06-29T00:10:09.308360+00:00'
page_id: '452719624'
product: rm
source: tdn-rm
title: Grupos de Descanso - Anexos
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupos+de+Descanso+-+Anexos
version: 82
---

Este anexo é utilizado para cadastrar o dia e o intervalo do descanso para o funcionário.  
Através do cadastro é possível controlar:  
   
**Identificação**  
Para cadastrar um descanso no grupo de descanso é necessário informar:  
   
**Data**  
Informe neste campo uma data maior que a data do início do período atual.  
   
**Hora Início/Hora Fim**  
Estes campos são utilizados para informar o intervalo do dia que será considerado como descanso para o funcionário. Podemos cadastrar um descanso no intervalo de 00:00 às 24:00.

**Observação**  
O sistema impossibilita a inserção de descansos com intervalos em interseção para uma mesma data.  
   
**Considera descanso como:** **Hora início até o fim do intervalo planejado:** Marcando este parâmetro, será considerado como extra de descanso o intervalo executado do início do descanso até o fim do intervalo planejado.

**Exemplo:** Horário planejado: 08:00 12:00 14:00 18:00 Descanso: 09:00 11:00 Será considerado: Horário planejado: 08:00 09:00 Descanso: 09:00 18:00  
   
**Extra apenas na interseção com o descanso:** Marcando este parâmetro, será considerado como extra de descanso a interseção entre o descaso cadastrado e o intervalo planejado.

**Exemplo1:** Horário planejado: 08:00 12:00 14:00 18:00 Descanso: 09:00 11:00 Será considerado: Horário planejado: 08:00 09:00 Descanso: 09:00 11:00 Horário planejado: 11:00 12:00 14:00 18:00

**Exemplo2:** Horário planejado: 08:00 12:00 14:00 18:00 Descanso: 07:00 11:00 Será considerado: Descanso: 07:00 11:00 Horário planejado: 11:00 12:00 14:00 18:00

**Toda jornada em interseção com o descanso:** Marcando este parâmetro, será considerado como extra de descanso toda a jornada que fizer interseção com o descanso cadastrado.

**Exemplo:** Horário planejado: Dia 1 = 22:00 +05:00 Dia 2 = 22:00 +05:00 Dia 3 = 22:00 +05:00 Descanso: Dia 2 = 00:00 +00:00, será considerado: Dia 1 = 22:00 +05:00 Descanso Dia 2 = 22:00 +05:00 Descanso Dia 3 = 22:00 +05:00

**Considera o intervalo planejado ao fazer interseção com o Descanso:** Marcando este parâmetro, será considerado como extra de descanso intervalo de descanso que fizer interseção com o intervalo planejado.

**Considera como descanso todo o intervalo planejado que iniciou no próprio descanso:** Marcando esse parâmetro, será considerado como extra de descanso todo o intervalo planejado iniciado no dia do descanso cadastrado.

**Exemplo:** Horário planejado: Dia 1 = 22:00 +05:00 Dia 2 = 22:00 +05:00 Dia 3 = 22:00 +05:00 Descanso: Dia 2 = 00:00 +00:00, será considerado: Dia 1 = 22:00 +05:00 Dia 2 = 22:00 +05:00 Descanso Dia 3 = 22:00 +05:00

**Considera como descanso todo o intervalo planejado que terminou no próprio descanso:** Marcando esse parâmetro, será considerado como extra de descanso todo o intervalo planejado que terminou no dia do descanso cadastrado.

**Exemplo:** Horário planejado: Dia 1 = - 22:00 05:00 Dia 2 = -22:00 05:00 Dia 3 = -22:00 05:00 Descanso: Dia 2 = 00:00 +00:00, será considerado: Dia 1 = -22:00 05:00 = 07:00 Trabalhadas Dia 2 = -22:00 05:00 = 07:00 de Descanso e Dia 3 = -22:00 05:00 = 07:00 Trabalhadas
