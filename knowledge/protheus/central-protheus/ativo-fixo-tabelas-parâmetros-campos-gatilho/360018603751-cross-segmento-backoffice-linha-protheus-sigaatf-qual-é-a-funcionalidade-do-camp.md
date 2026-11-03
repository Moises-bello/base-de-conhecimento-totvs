---
article_id: 360018603751
category: Ativo Fixo - Tabelas, Parâmetros, Campos .Gatilho
content_hash: be404c8cb9fbc67e9d163b9108397750dd38f003375c94ef0c1f87c37a5a685f
fetched_at: '2026-06-28T22:41:50.292847+00:00'
product: protheus
section_id: 1500001536201
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF -  Qual é a funcionalidade
  do campo N1_ORIGEM?
type: support-article
updated_at: '2022-03-21T12:55:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018603751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Qual-%C3%A9-a-funcionalidade-do-campo-N1-ORIGEM
---

**Dúvida**Qual é a funcionalidade do campo N1\_ORIGEM?

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo - Todas as versões  
  
  
**Solução**

O campo N1\_ORIGEM foi desenvolvido pela TOTVS **exclusivamente para proteções internas do módulo Ativo Fixo (SIGAATF)**. Este campo não tem tratamento e gravações relacionadas às integrações de outros módulos com o Ativo Fixo.   
  
**Exemplos de utilização no sistema**

* Ativos gerados a partir da rotina **Apropriação AVP de Bens de Provisão (ATFA460)** não podem ser excluídos pela rotina **Cadastro de Ativos (ATFA010)**, pois o campo N1\_ORIGEM está com o valor igual a ATFA460.

* Um bem/ativo planejado somente pode ser excluído por meio do estorno da efetivação, na rotina de **Planejamento de Ativo (ATFA310),**pois o campo N1\_ORIGEM está com o valor igual a ATFA310.
