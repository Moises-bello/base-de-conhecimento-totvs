---
article_id: 360021232732
category: RH - Rescisão
content_hash: 25c5eb372c34121bda1ebda3dfb5657bf50c30150adaadbda9642d1e009bfc28
fetched_at: '2026-06-28T22:43:48.458885+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao calcular a rescisão gera a mensagem: Verifique
  o cálculo do adiantamento do funcionário, foram encontradas inconsistências'
type: support-article
updated_at: '2026-06-25T12:23:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021232732-RH-Linha-Protheus-GPE-Ao-calcular-a-rescis%C3%A3o-gera-a-mensagem-Verifique-o-c%C3%A1lculo-do-adiantamento-do-funcion%C3%A1rio-foram-encontradas-inconsist%C3%AAncias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33488003725335) Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao calcular a rescisão gera a mensagem: Verifique o calculo do adiantamento do funcionário, foram encontradas inconsistências. Não será possível finalizar a rescisão.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Causa**Por conta do e-social não deve existir verbas vinculadas ao roteiro ADI nas tabelas RGB, SRC e SRD sem a verba de pagamento - identificador 0006.  
  
O Sistema só grava verbas no roteiro ADI dentro das tabelas mencionadas, quando há cálculo de adiantamento e não foi cancelado corretamente. O cancelamento do adiantamento dentro do mês é comum quando o funcionário é demitido próximo a data de pagamento.

Conforme evidência abaixo, no caso de cálculo e cancelamento de adiantamento o Sistema não mantém gravada nenhuma verba nas tabelas RGB, SRC e SRD.  
   
1. Após o cálculo e fechamento do ADI mês 10/2018:

```
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018206692)
```

2. Após o fechamento do mês 10/2018 foi gerado dentro do período 11/2018:

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018077171)
```

3. SRC após o cálculo do adiantamento, mês 11/2018:

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018206832)
```

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018206852)
```

4. Cancelamento de cálculo (GPEM160):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018206952)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018207012)

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018077551)
```

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018077611)
```

5. Após o cancelamento do adiantamento a verba de origem F permaneceu na RGB:

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018207232)
```

6. Após o fechamento do ADI, a verba que estava na RGB permaneceu lá, porém com o roteiro FOL.

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018077671)
```

**Solução:**

Após o cancelamento do cálculo de adiantamento a verba de Base IR mês anterior - identificador 0106 deve está relacionado com o roteiro FOL.

**Saiba mais**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
