---
content_hash: b7d8a6df9098cbb433cb4b83c4c4af4e07952cdf31f3ca451dfd30fd73ae1835
fetched_at: '2026-06-29T00:10:57.122647+00:00'
page_id: '594414856'
product: rm
source: tdn-rm
title: SobreAviso
type: documentation
url: https://tdn.totvs.com/display/LRM/SobreAviso
version: 2
---

Definições sobre o cálculo das horas de Sobreaviso

**Gerar extra normal/compensado/descanso/feriado de extra sobreaviso**

Marcando este parâmetro o sistema irá calcular horas extras normal/compensado/descanso/feriado para o funcionário que trabalhar no intervalo de horas de SobreAviso.

Exemplo:

Horário do Funcionário: 08:00 12:00 14:00 18:00

Horário de SobreAviso: 00:00 às 08:00

Batidas do Funcionário: 02:00E 04:00S 08:00E 12:00S 14:00E 18:00S

Cálculo do sistema com o parâmetro marcado:

00:00 às 08:00 = 08:00 Horas de SobreAviso (SAV)

02:00 às 04:00 = 02:00 Extra Normal Autorizado (EA)

02:00 às 04:00 = 02:00 Sobre Aviso Extra Normal (SAN)

Com o parâmetro desmarcado o sistema não vai calcular a hora extra normal:

00:00 às 08:00 = 08:00 Horas de SobreAviso (SAV)

02:00 às 04:00 = 02:00 Sobre Aviso Extra Normal (SAN)

**Deduzir extras de sobreaviso no cálculo de horas de sobreaviso**

Marcando este parâmetro o sistema vai deduzir das horas que foram trabalhadas no período de sobre aviso do cálculo das horas de SobreAviso (SAV)

Exemplo:

Horário do Funcionário: 08:00 12:00 14:00 18:00

Horário de SobreAviso: 00:00 às 08:00

Batidas do Funcionário: 02:00E 04:00S 08:00E 12:00S 14:00E 18:00S

Cálculo do sistema com o parâmetro marcado:

00:00 às 02:00 = 02:00 Horas de SobreAviso (SAV)

02:00 às 04:00 = 02:00 Sobre Aviso Extra Normal (SAN)

04:00 às 08:00 = 04:00 Horas de SobreAviso (SAV)

Cálculo do sistema com o parâmetro marcado:

00:00 às 08:00 = 08:00 Horas de SobreAviso (SAV)

02:00 às 04:00 = 02:00 Sobre Aviso Extra Normal (SAN)

**Não compensar extras de sobreaviso**

Este parâmetro é considerado para os funcionários com horário do tipo Flexível. Com o parâmetro marcado qualquer extra efetuada durante o período do sobreaviso não entrará no cálculo da compensação de horas do horário flexível.

Exemplo:

Horário do Funcionário: 08:00 12:00 14:00 18:00

Horário de SobreAviso: 00:00 às 08:00

Batidas do Funcionário: 02:00E 04:00S 10:00E 12:00S 14:00E 18:00S

Cálculo do sistema com o parâmetro marcado:

00:00 às 08:00 = 08:00 Horas de SobreAviso (SAV)

02:00 às 04:00 = 02:00 Sobre Aviso Extra Normal (SAN)

08:00 às 10:00 = 02:00 Atraso (A)

Cálculo do sistema com o parâmetro desmarcado:

00:00 às 02:00 = 02:00 Horas de SobreAviso (SAV)

02:00 às 04:00 = 02:00 Extra Normal que foi compensada (ENC)

04:00 às 08:00 = 04:00 Horas de SobreAviso (SAV)

08:00 às 10:00 = 02:00 Atraso que foi compensado (AC)
