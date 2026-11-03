---
article_id: 10759140332439
category: RH - Contabilização
content_hash: ce57e5278536affb697b2c0b107957311a5552e687205c98739bf2e991d33158
fetched_at: '2026-06-28T22:43:45.971815+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: 'RH - Linha Protheus - GPE - HELP: CTAEQUA123 - As entidades contábeis são
  iguais no débito e crédito, invalidando o lançamento'
type: support-article
updated_at: '2025-07-24T14:08:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10759140332439-RH-Linha-Protheus-GPE-HELP-CTAEQUA123-As-entidades-cont%C3%A1beis-s%C3%A3o-iguais-no-d%C3%A9bito-e-cr%C3%A9dito-invalidando-o-lan%C3%A7amento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33687530386711) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**HELP: CTAEQUA123 - As entidades contábeis são iguais no débito e crédito, invalidando o lançamento.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**A conta débito e conta crédito de um dos lançamentos contábeis são iguais.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

Após o HELP ser apresentado conforme print abaixo, será necessário realizar duas validações:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10759577606167)

1) Se for um lançamento manual , alterar a conta débito ou crédito , considerando que um lançamento de partida dobrada não pode ter a mesma conta nos campos débito e crédito.

2) Se os lançamentos forem gerados automaticamente através da rotina GPEM110 e com os lançamentos padrões atrelados às verbas, identificar qual verba possui contas iguais (ou se todos os lançamentos estão com o mesmo problema) e ajustar a fórmula de modo que sejam consideradas contas diferentes.  
  
Em caso de apoio para as configurações, acione nossa Equipe HUB através do suporte Protheus RH, para análise e orçamento da demanda, uma vez que este atendimento é realizado somente através de consultoria.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)

[Página Centralizadora da Contabilização Protheus RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
