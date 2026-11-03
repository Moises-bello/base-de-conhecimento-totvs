---
content_hash: ca1167f0a174a447176fa834a9263529204a99d8821001d58afd1897452bc6fc
fetched_at: '2026-06-29T00:05:53.878512+00:00'
page_id: '1071993457'
product: rm
source: tdn-rm
title: Aplicação da Natureza no processo de importação de batidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1071993457
version: 7
---

* *Importar batidas com parâmetro de natureza:* ***Horário planejado**.*

O sistema define a natureza da batida (Entrada ou Saída) com base na jornada do colaborador e nos intervalos planejados, *ignorando a ausência de refeição e os limites de refeição*.

1. Sem Jornada (Sem Trabalho)

Com batida anterior (Considera os  últimos 3 dias anteriores ao período ): A **natureza** será a **contrária** à da última batida importada.

Sem batida anterior: A **natureza** será **Entrada**.

1. Com Jornada (Baseado em Intervalos)

Antes do 1º intervalo: Batida menor que o início do primeiro intervalo planejado, a **natureza** é **Entrada**.

Depois do último intervalo: Batida maior que o fim do último intervalo planejado, a **natureza** é **Saída**.

Dentro de um intervalo: O sistema calcula a qual extremidade a batida está mais próxima:

Mais **próxima** do **início**,  **Entrada**.

Caso contrário: Mais **próxima** do **fim**, **Saída**.

Fora dos intervalos (mas não nos extremos iniciais/finais): Se a batida não se encaixar nas regras acima, o sistema busca a última batida (que seja anterior à atual e diferente do tipo "T - trânsito") e aplica a natureza contrária a ela.

* *Importar batidas com parâmetro de natureza:* ***desmarcado****.*

O produto não verifica se existe jornada planejada para a data/batida. Nem quais são as batidas posteriores à que está sendo importada.

Será verificada a *natureza da última batida importada* (a última batida considerada deve ser menor que a batida que está sendo verificada e não ser do tipo T- trânsito) para definir a ***natureza contrária***.

 Caso *não exista batida* (Considera início do Período – 3 dias), será considerada como ***Entrada**.*

* *Importar batidas com parâmetro de natureza:* ***Considerando o período.***

Será avaliado se existe ***batida anterior*** e aplicada a **natureza contrária** para a batida que está sendo verificada. É **ajustada** a **natureza** das **batidas posteriores** à que está sendo importada. 

Quando não existem batidas anteriores, (batida anterior é menor que a batida que está sendo verificada e não ser do tipo T- trânsito). Será feita a verificação da jornada planejada do horário, e o mesmo cálculo da natureza na importação com o horário planejado.

Caso não exista jornada planejada para o dia, a batida será considerada como *Entrada*. E serão ajustadas todas as batidas posteriores caso existam.

* *Importar batidas com parâmetro de natureza:  **Jornada.***

Todas as batidas são gravadas com a natureza padrão – Entrada. Após a gravação do registro será aplicado o cálculo para adequação da natureza. 

1- As batidas são agrupadas conforme a jornada e se existir mais de uma batida será alterada a natureza conforme cálculo: 

Batida na posição Par. Natureza: **Entrada**

Batida na posição Ímpar. Natureza: **Saída**.

2 -Caso exista uma única batida para a jornada será mantida como Entrada. 

**Observação:** Para as importações considerando o horário planejado ou considerando a jornada, é aplicado um cálculo para identificar o limite de cada jornada planejada do horário, ou seja, qual o limite de cada índice em comparação com o índice do dia anterior ou posterior.
