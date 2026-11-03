---
article_id: 360028248691
category: RH - Calculo Autonomo/Prolabore
content_hash: def9db3a5fbfb899c4aab983f44c7818ea24cb4ac8e73953f9e3492a1659ee85
fetched_at: '2026-06-28T22:43:15.147633+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o calculo de INSS e IR para Autônomo
  com mais de um pagamento no mês
type: support-article
updated_at: '2025-04-17T18:34:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028248691-RH-Linha-Protheus-GPE-Como-funciona-o-calculo-de-INSS-e-IR-para-Aut%C3%B4nomo-com-mais-de-um-pagamento-no-m%C3%AAs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25676038360599)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como funciona o calculo de INSS e IR para Autônomo com mais de um pagamento no mês?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal - A partir da versão 12.1.17.  
  
**Solução**Cálculo executado pelo processo 00004 - Semanalista  
Crie no cadastro de período os números de pagamento dentro do período conforme necessidade. No exemplo a seguir, criamos 4 pagamentos dentro da competência 04/2019.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028191132)

Lançar o valor na verba com Id 0218 com o valor da prestação de serviço.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028191131)

Calcular a folha do autônomo.​​

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028196772)

Para que o sistema enxergue os valores dos encargos já descontado do primeiro pagamento da prestação de serviço,​ **é necessário fechar o número de pagamento atual para que o próximo seja calculado.**

Tabela RGB (lançamento por funcionário) após o fechamento do número de pagamento 01

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028198952)

Devido ao eSocial, não é mais apresentado a verba de base de IR e IR descontado no mês anterior.

Não está mais sendo apresentando a verba de base de IR e IR descontado no mês anterior na tabela RGB após o fechamento das folhas, agora é guardado na memória de calculo, como já era feito com o valor do INSS.

Lançado um valor para pagamento no número de pagamento 02.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028197791)

​​

Na própria verba de base de IR está sendo considerado a base de IR mês anterior, do valor da prestação de serviço atual e do anterior.   
  
Exemplo:

*Base de IR* 2000,00 - 220,00 = 1780,00

1780,00  + 3115,00 = **4895,00**

Sendo assim, para o desconto de IR o sistema calculará sobre essa base somada, achando o valor dessa base, será descontado o IR do mês anterior.

*​​​IR descontado* 4895,00 \* 27,5%  - 869,36 = 476,76 - 112.45 (IR anterior) = **364,31**

O mesmo serve para o desconto do INSS, quer é levado em consideração o INSS descontado anteriormente dentro da competência para descontar a diferença, até que atinja o teto de desconto de INSS estabelecido.

**Importante:** Para que o cálculo fique correto é necessário que o **Tipo de Pagamento** no cadastro do Autônomo esteja =**S - Semanalista**. Do contrário, o Sistema trará um valor incorreto.

**Saiba mais:**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
