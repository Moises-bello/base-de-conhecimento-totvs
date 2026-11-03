---
content_hash: 048fe834ab0f0ae7964597f8fdb8d114d626be5d0741045dc88deac33d7e1c9d
fetched_at: '2026-06-29T00:10:02.627274+00:00'
page_id: '452718985'
product: rm
source: tdn-rm
title: Solução de Conflito de Férias,Afastamentos, Admissão e Demissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718985
version: 13
---

**Solução de conflito Férias:**

**Considera apenas as férias**

Exemplo:

Férias 30/09/2021 a

Horário Noturno  22:00-22:59-23:59-05:00

Resultado: Será considerada as férias a partir da saida1 das 22:00h dia 30/09/2021.

**Substitui Jornada Planejada que iniciou nas férias**

Exemplo:

Férias 30/09/2021 a

Horário Noturno  22:00-22:59-23:59-05:00

Resultado: Será considerada as férias a partir da Entrada2  das 22:00h dia 30/09/2021.

**Substitui Jornada Planejada que Terminou nas férias**

Exemplo:

Férias 30/09/2021 a 04/10/2021

Horário Noturno  22:00-22:59-23:59-05:00

Resultado: Será considerada as férias a partir da Entrada2  das 22:00h dia 29/09/2021.

**Solução de conflito Afastamento:**

**Considera apenas o Afastamento**

Exemplo:

Afastamento Dia 01/08/2021 até 06/10/2021 23:59

Horário Noturno  23:31-02:30-03:20-06:30

Resultado:

Afastamento 07/10/2021

23:31-00:00

**Substitui Jornada Planejada que iniciou no Afastamento**

Exemplo:

Afastamento Dia 01/08/2021 até 06/10/2021 23:59

Horário Noturno  23:31-02:30-03:20-06:30

Resultado:

Afastamento 07/10/2021

23:31-06:30

**Substitui Jornada Planejada que terminou no Afastamento**

Exemplo:

Afastamento Dia 01/08/2021 até 06/10/2021 23:59

Horário Noturno  23:31-02:30-03:20-06:30

Resultado:

Afastamento 05/10/2021

23:31- +06:30 Dia 05/10/2021 até saída 06/10/2021.

Resultado: Horário com parâmetro marcado "Considerar a data final da jornada como data referência"

Afastamento 06/10/2021

-23:31-06:30 Dia 05/10/2021 até a saída 06/10/2021
