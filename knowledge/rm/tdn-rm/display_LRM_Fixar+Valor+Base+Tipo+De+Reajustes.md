---
content_hash: c97166c9f8e9ed22a9c88b9b393095dfb80da35660a693e824978d8ff5289231
fetched_at: '2026-06-29T00:05:52.852526+00:00'
page_id: '1060236794'
product: rm
source: tdn-rm
title: Fixar Valor Base Tipo De Reajustes
type: documentation
url: https://tdn.totvs.com/display/LRM/Fixar+Valor+Base+Tipo+De+Reajustes
version: 1
---

**Não será possível fazer esse controle automático, cada cliente terá que testar e validar a viabilidade de executar o congelamento no período de aniversário de cada contrato. Fazer a Importação separada para cada aniversário e tipo de reajuste**

**Normal ou com Fórmula**

1. Juros Pré-fixado e CM **Mensal**

1. Juros Price, Sac, Sacre
2. CM Mensal

1. Não tem problema, pode fixar o reajuste na última data reajustada

2. Juros Pré-fixado e CM **Anual**

1. Juros Price, Sac, Sacre
2. CM Anual

1. **Tem** problema, pode fixar o reajuste na última data reajustada do aniversário

3. Juros e CM **Mensal**

1. Juros Mensal
2. CM Mensal

1. Não tem problema, pode fixar o reajuste na última data reajustada

4. Juros e CM **Anual**

1. Juros Anual
2. CM Anual

1. **Tem** problema, pode fixar o reajuste somente na última data reajustada do aniversário

5. Juros Mensal e CM **Anual ou Vice-Versa**

1. Juros Mensal
2. CM Anual

1. **Tem** problema, o sistema só pode fixar o valor na data do último aniversário anual

**Pro-Rata**

1. Juros Pré-fixado e CM **Mensal Pro-rata**

1. Juros Price, Sac, Sacre
2. CM Mensal

1. **Tem** que garantir que o reajuste **tenha sido executado no último dia do mês** e aí sim permitir congelar nesse momento.

2. Juros Pré-fixado e CM **Anual Pro-rata**

1. Juros Price, Sac, Sacre
2. CM Anual

1. **Tem** que garantir que o reajuste **tenha sido executado no último dia do mês** e aí sim permitir congelar nesse momento do aniversário do CM.

3. Juros e CM **Mensal Pro-rata**

1. Juros Mensal
2. CM Mensal

1. **Tem** que garantir que o reajuste **tenha sido executado no último dia do mês** e aí sim permitir congelar nesse momento.

4. Juros e CM **Anual Pro-rata**

1. Juros Anual
2. CM Anual

1. **Tem** que garantir que o reajuste **tenha sido executado no último dia do mês** e aí sim permitir congelar nesse momento do aniversário do CM.

5. Juros Mensal e CM **Anual Pro-rata ou Vice-Versa**

1. Juros Mensal **Pro Rata**
2. CM Anual

1. **Tem** que garantir que o reajuste **tenha sido executado no último dia do mês** do Aniversário do CM e aí sim permitir congelar nesse momento do aniversário do CM.

**Resíduo**

1. Juros Pré-fixado e CM **Mensal**

1. não existe essa situação

2. Juros Pré-fixado e CM **Anual Resíduo**

1. Juros Price, Sac, Sacre
2. CM Anual Resíduo

1. **Tem** problema, pode fixar o reajuste na última data reajustada do aniversário

3. Juros e CM **Mensal Resíduo**

1. Juros Mensal
2. CM Mensal

1. Não tem problema, pode fixar o reajuste na última data reajustada

4. Juros e CM **Anual Resíduo**

1. Juros Anual **Resíduo**
2. CM Anual **Resíduo**

1. **Tem** problema, pode fixar o reajuste somente na última data reajustada do aniversário

5. Juros Mensal e CM **Anual Resíduo ou Vice-Versa**

1. Juros Mensal
2. CM Anual **Resíduo**

1. **Tem** problema, o sistema só pode fixar o valor na data do último aniversário anual
