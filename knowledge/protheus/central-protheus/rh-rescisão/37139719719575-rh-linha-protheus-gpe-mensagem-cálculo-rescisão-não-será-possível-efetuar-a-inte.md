---
article_id: 37139719719575
category: RH - Rescisão
content_hash: 2d72fdf4b042b760876acaaa52dc5281933c7cfe29d3d19f3638e902effd793c
fetched_at: '2026-06-28T22:43:49.773305+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Mensagem cálculo rescisão: Não será possível efetuar
  a integração. Há verbas com incidência de IR relacionada a Plano de Saúde , mas
  não há dados no cadastro de Plano de Saúde Ativo'
type: support-article
updated_at: '2026-05-19T20:45:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37139719719575-RH-Linha-Protheus-GPE-Mensagem-c%C3%A1lculo-rescis%C3%A3o-N%C3%A3o-ser%C3%A1-poss%C3%ADvel-efetuar-a-integra%C3%A7%C3%A3o-H%C3%A1-verbas-com-incid%C3%AAncia-de-IR-relacionada-a-Plano-de-Sa%C3%BAde-mas-n%C3%A3o-h%C3%A1-dados-no-cadastro-de-Plano-de-Sa%C3%BAde-Ativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37139719706903) Tempo aproximado para leitura: **01:30 min**  
  
**Dúvida**  
Por que rotina rescisão apresenta mensagem: Não será possível efetuar a integração. Há verbas com incidência de IR relacionada a Plano de Saúde , mas não há dados no cadastro de Plano de Saúde Ativo?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37139735005207)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
A rotina gera a mensagem devido a verba de plano de saúde ter sido lançada manualmente em rescisão origem I. Para o devido desconto deve ser calculado o Plano de Saúde roteiro PLA e integrado dentro da rescisão.  
   
Devido a DIRF no eSocial é necessário calcular o Plano de Saúde roteiro PLA e integrar dentro da rescisão deste modo gera desconto verba origem G.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Como integrar valores de assistência médica/odontológica na rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055304013-RH-Linha-Protheus-GPE-Como-integrar-valores-de-assist%C3%AAncia-m%C3%A9dica-odontol%C3%B3gica-na-rescis%C3%A3o)
