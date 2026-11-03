---
content_hash: 6ac6f015f51e5c59fa9f682ccb4892760dce1ff48aa777781b64facb2d126b4c
fetched_at: '2026-06-29T00:10:11.257548+00:00'
page_id: '452720013'
product: rm
source: tdn-rm
title: Lançamentos Globais - Horário Sobreaviso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452720013
version: 2
---

**Lançamentos Globais - Horário Sobreaviso**

O sobreaviso deve ser lançado para aqueles funcionários para pagar as horas que o funcionário estará a disposição da empresa fora do seu horário trabalho normal. Pode ser utilizado no caso de plantão, ou seja a disposição da empresa e poderá ser chamado para trabalhar a qualquer minuto.

**Exemplo:**

No dia 08/04/2002 um funcionário X tem o horário é 08:00E 12:00S 14:00E 18:00S. Lançamos um Horário de Sobreaviso no período de 18:00 às 24:00 horas.

Se o funcionário sair da empresa as 18:00 horas, o sistema irá calcular para ele 06:00 horas de Sobreaviso referente ao intervalo de 18:00 às 24:00 horas.

Se o funcionário tiver efetuado as batidas 08:00E 12:00S 14:00E 20:30S no dia 08/04/2002, a movimentação do funcionário neste dia será:

* 02:30 horas extras normais referentes ao intervalo de 18:00 às 20:30
* 06:00 horas de Sobreaviso referente ao intervalo cadastro de Sobreaviso (18:00 às 24:00)
* 02:30 horas extras de Sobreaviso, pois o funcionário trabalhou dentro do horário de sobre aviso.

**Horário**

Informe nos campos início e fim o intervalo de datas que pretende fazer o lançamento do horário de Sobreaviso do(s) funcionário(s). O período informado tem que estar no período atual do sistema. A data início não pode ser maior que a data fim.

**Cancelar dados lançados no período**

Marque esta opção para cancelar o sobreaviso lançado para o(s) funcionário(s). O sistema só irá cancelar se informar o intervalo de hora igual ao que foi lançado.
