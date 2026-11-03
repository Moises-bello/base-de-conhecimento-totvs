---
content_hash: f2f1564ba67a4e85bb7d2094da6bb0908f0e2f3f97c4c251d880a4235bcda0a7
fetched_at: '2026-06-29T00:10:03.708325+00:00'
page_id: '452719137'
product: rm
source: tdn-rm
title: 'Tempo considerado para continuação de jornada :'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719137
version: 47
---

Parâmetro utilizado para a definição da jornada de referência do intervalo executado. Caso o intervalo executado não faça interseção com o intervalo planejado atual(Horário planejado) é feita a seguinte conta: Fim do último intervalo executado da jornada que está sendo verificada + este parâmetro. Caso o início do intervalo executado pendente, esteja menor ou igual a este valor, será considerado o intervalo como da jornada atual.

**Tempo de acréscimo para jornadas sem trabalho ao se definir a jornada de referência do intervalo executado**

Quando a definição de jornada de referência de um intervalo é por aproximação, existem definições óbvias.  Por exemplo quando o intervalo executado faz interseção apenas com uma jornada planejada, ela faz parte dessa.

**Exemplo:**

Temos o seguinte horário planejado e trabalhado:

Planejado   01 08:00 18:00 TRABALHO

Executado  01  16:00 20:00

O intervalo executado 01 16:00 20:00 faz interseção com a jornada planejada 01 08:00 18:00, então obviamente é dessa jornada.

Mas quando o intervalo executado não faz interseção com nenhum planejado a definição é feita por aproximação apenas.

**Exemplo :**

Planejado   01 08:00 18:00 TRABALHO

Planejado   02 08:00 18:00 TRABALHO

Executado  01 21:00 23:30.

 O intervalo executado "01 21:00 23:30" é referente a jornada do dia "01 08:00 18:00", pois sua diferença para essa são 3:00.

Já para a jornada planejada "02 08:00 18:00" são de 08:30.

Mas este raciocínio não soluciona bem para todos os casos, por isso foi criado este parâmetro. Imagine esse raciocínio para dias de descanso e compensado com dias de trabalho.

**Exemplo :**

Planejado 01 00:00 00:00 DESCANSO

Planejado 02 16:00 22:00 TRABALHO

Executado 01 06:00 08:00

Por aproximação, o intervalo executado está a 06:00 da jornada planejada "01 00:00 00:00". Já da jornada planejada "02 16:00 22:00" está a 08:00.

O problema é que o entendimento mais comum é que nesses casos os intervalos executados sejam do dia de trabalho, o que demanda a necessidade de parametrizar esse comportamento.

**Observação:**

O tempo de acréscimo será considerado para alocação das batidas que fazem interseção com a jornada de trabalho.

Exemplo para a jornada a seguir:

Considerando que esta definido 3:00 , as batidas serão alocadas no dia 16/07/2021 somente se a batida de saída ocorre até as 09:20 do dia 17.

Como a saída ocorreu as 06:37 a batida será considerada para a jornada de trabalho.
