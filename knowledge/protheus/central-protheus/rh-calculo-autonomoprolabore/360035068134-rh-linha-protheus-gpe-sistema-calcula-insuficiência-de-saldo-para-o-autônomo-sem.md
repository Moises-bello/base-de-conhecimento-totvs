---
article_id: 360035068134
category: RH - Calculo Autonomo/Prolabore
content_hash: e046c587b5976d566bbf513126cb722eae2175ae274eee58ebeaebfd43c12288
fetched_at: '2026-06-28T22:43:15.251954+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema calcula insuficiência de saldo para o autônomo
  semanalista
type: support-article
updated_at: '2025-08-08T11:37:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035068134-RH-Linha-Protheus-GPE-Sistema-calcula-insufici%C3%AAncia-de-saldo-para-o-aut%C3%B4nomo-semanalista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24996792425239) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Sistema calcula insuficiência de saldo para o autônomo semanalista.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Sistema calcula a insuficiência de saldo, ID de cálculo **0045** para o autônomo semanalista mesmo que não tenha o pagamento ID **0218**, porque, quando ocorre um arredondamento (Provento), em uma semana, durante o fechamento ele é lançado na semana seguinte como desconto.

Se nesta semana não existe pagamento, o desconto vira insuficiência de saldo para que seja transportado para a semana seguinte como desconto novamente, até que exista um pagamento.

Se nesta situação a insuficiência de saldo não for gerada, o arredondamento pago na primeira semana nunca será descontado do funcionário.

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
