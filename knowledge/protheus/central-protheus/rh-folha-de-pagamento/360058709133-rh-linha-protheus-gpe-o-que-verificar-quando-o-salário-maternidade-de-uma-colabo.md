---
article_id: 360058709133
category: RH - Folha de Pagamento
content_hash: 00f5a1ea5eb1187e340b42e46f5c8322a00e9f50756f92efe9529074672d611e
fetched_at: '2026-06-28T22:44:16.077932+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando o salário maternidade de
  uma colaboradora cujo salário é superior a R$ 30.000,00 for calculado incorretamente.
type: support-article
updated_at: '2024-09-10T16:50:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058709133-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-sal%C3%A1rio-maternidade-de-uma-colaboradora-cujo-sal%C3%A1rio-%C3%A9-superior-a-R-30-000-00-for-calculado-incorretamente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26273834353175) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Colaboradora cujo salário contratual é de R$ 33.071,18, e ao calcular a folha de pagamento sistema calcula maternidade de R$ 28,81

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098765813)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Solução**Verificar o parâmetro **MV\_LIMDMAT**, nele será informado o **valor limite de dedução para a Licença Maternidade.****![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096453114)**

O conteúdo informado deve ser 39293,32 (sem o ponto).  
Se o conteúdo estiver com valor contendo ponto o calculo será feito incorretamente.  
Após ajustar o parâmetro de 39.293,32 para 39293,32 o valor será calculado corretamente.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096454214)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
