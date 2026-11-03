---
article_id: 360021873431
category: Requisições
content_hash: 68731d1251052b9f46a1a586e73937962858c8b827b5812581263478d2b05347
fetched_at: '2026-06-28T22:47:25.371898+00:00'
product: rm
section_id: 1500000861382
source: central-rm
title: 'RH - RM - RHU - Erro ao criar requisição: "Não foi possível localizar nenhuma
  seção que o requisitante X seja chefe. Para criar ou visualizar requisição é necessário
  ser chefe de alguma seção."'
type: support-article
updated_at: '2026-06-02T13:48:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021873431-RH-RM-RHU-Erro-ao-criar-requisi%C3%A7%C3%A3o-N%C3%A3o-foi-poss%C3%ADvel-localizar-nenhuma-se%C3%A7%C3%A3o-que-o-requisitante-X-seja-chefe-Para-criar-ou-visualizar-requisi%C3%A7%C3%A3o-%C3%A9-necess%C3%A1rio-ser-chefe-de-alguma-se%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27005820941207)**Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**  
Quando o gestor tenta incluir uma requisição no portal aparece a seguinte mensagem:

*"Não foi possível localizar nenhuma seção que o requisitante X seja chefe. Para criar ou visualizar requisição é necessário ser chefe de alguma seção."*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018554331)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas – A partir da versão 12.1  
  
**Causa**  
 Essa mensagem está relacionada ao fato de que a inclusão do chefe na visão de chefes/supervisores está com a data inicial superior à competência do Labore (TOTVS Folha de Pagamento ).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27005806787351)

**Solução**  
 Quando a competência do TOTVS Folha de Pagamento (RM Labore) for liberada para o mês e ano igual ou superior à data inicial do cadastro do chefe na visão de chefes/supervisores, o gestor poderá efetuar inclusões de requisições normalmente.

Outra possibilidade, caso não queira aguardar a liberação da competência, é alterar a data de início para o mês e ano de competência que a Folha de Pagamento (RM Labore) se encontra.
