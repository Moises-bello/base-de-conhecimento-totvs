---
article_id: 19259220058647
category: RH - Folha de Pagamento
content_hash: 8abd2d6fa4e2181173df3d5c5fd65aad9ad62b6e3093b4368d075c7e6b50a6d3
fetched_at: '2026-06-28T22:44:17.080826+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como as verbas do ponto eletrônico transitam na
  folha de pagamento.
type: support-article
updated_at: '2025-06-13T19:46:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19259220058647-RH-Linha-Protheus-GPE-Como-as-verbas-do-ponto-eletr%C3%B4nico-transitam-na-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19259220006423) Tempo aproximado para leitura: **01:00:00 min** **Dúvida**Como as verbas do ponto eletrônico transitam na folha de pagamento.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**No módulo **SIGAPON - 16**, são gerados Resultados (tabela SPB) após o cálculo mensal do ponto.

Após a geração desses resultados temos uma rotina de integração desses valores com a folha de pagamento que deve executada.

Para verificar os lançamentos que foram integrados, acesse no módulo **SIGAGPE - 07** - Atualizações > Lançamentos > Por Funcionário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19259235911831)

Verifique que a verba é apresenta com a origem E, que se refere ao ponto eletrônico.  
  
No momento do cálculo da folha de pagamento, essa verba será calculada baseada na referência de horas oriunda do ponto e manterá também sua origem (E) :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19259263325335)

**Saiba mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como identificar a origem das verbas gravadas no cálculo da folha e períodos abertos de fechados (tabelas SRC e SRD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016689031-RH-Linha-Protheus-GPE-Como-identificar-a-origem-das-verbas-gravadas-no-c%C3%A1lculo-da-folha-e-per%C3%ADodos-abertos-de-fechados-tabelas-SRC-e-SRD)

[RH - Linha Protheus - PON - Integração com a Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050379453-RH-Linha-Protheus-PON-Integra%C3%A7%C3%A3o-com-a-Folha-de-Pagamento)
