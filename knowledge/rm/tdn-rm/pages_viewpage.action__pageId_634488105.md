---
content_hash: b351df44590b8a37a43546cede695d3da784682883e3d63522a1d881ac0e6730
fetched_at: '2026-06-29T00:11:06.412408+00:00'
page_id: '634488105'
product: rm
source: tdn-rm
title: Jornada referência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=634488105
version: 2
---

**Quebra intervalo executado entre jornadas planejadas que fazem interseção**

Este parâmetro deve ser utilizado para definir como o sistema deve considerar o cálculo da jornada do funcionário de acordo com as batidas efetuadas por ele e sua jornada planejada.

**Exemplo1:**

Com o parâmetro desmarcado o sistema vai considerar a jornada do funcionário até a batida de saída.

Horário planejado

SEG - 08:00E 12:00S 14:00E 18:00S

TER - 08:00E 12:00S 14:00E 18:00S

QUA - 08:00E 12:00S 14:00E 18:00S

Batidas do funcionário

SEG - 08:00E 12:00S 14:00E

TER -             09:00S

QUA - 08:00E 12:00S 14:00E 18:00S

Neste caso o sistema considera hora extra no intervalo de 18:00 da segunda-feira até 09:00 da terça-feira e 08:00 de falta na terça-feira.

**Exemplo2:**

Com o parâmetro marcado o sistema quebra o cálculo da jornada do funcionário considerando a jornada planejada.

Horário planejado

SEG - 08:00E 12:00S 14:00E 18:00S

TER - 08:00E 12:00S 14:00E 18:00S

QUA - 08:00E 12:00S 14:00E 18:00S

Batidas do funcionário

SEG - 08:00E 12:00S 14:00E

TER -             09:00S

QUA - 08:00E 12:00S 14:00E 18:00S

Neste caso o sistema considera hora extra para o intervalo de 18:00 da segunda-feira até 08:00 da terça-feira. O intervalo de 08:00 às 09:00 da terça-feira é 01:00 hora trabalhada e calcula também 07:00 de atraso para o intervalo de 09:00 às 18:00 da terça-feira.
