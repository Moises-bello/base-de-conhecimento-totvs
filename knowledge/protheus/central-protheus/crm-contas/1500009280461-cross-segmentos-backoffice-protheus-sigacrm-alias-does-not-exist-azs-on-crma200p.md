---
article_id: 1500009280461
category: CRM - Contas
content_hash: c84e95a5dc5cf6d9bed2a6847ca72751519775e3c9b22ce05029a93ee2fe1cfb
fetched_at: '2026-06-28T22:40:28.344161+00:00'
product: protheus
section_id: 1500001549042
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Alias does not exist AZS
  on CRMA200PAUT
type: support-article
updated_at: '2024-04-25T12:11:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009280461-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Alias-does-not-exist-AZS-on-CRMA200PAUT
---

**Ocorrência**Ao incluir um cliente na área de trabalho (**CRMA290**) gera o erro:

**Alias does not exist AZS on CRMA200PAUT(CRMA200.PRW) 15/09/2020 18:27:00 line : 1347**

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12

**Causa**

O erro em questão indica que o sistema não está localizando a tabela **AZS** na área de trabalho.  
Normalmente este tipo de ocorrência está relacionado a inconsistência de dicionário de dados.

**Solução**

Para que seja solucionando é importante que atualize com o dicionário de dados disponível no portal do cliente para sua release de uso e  reprocesse o **UPDDISTR** para que as atualizações de dicionário ocorram, e as tabelas e campos faltantes sejam criados corretamente.

Dicionário de Dados:

**[P12123 - página principal do dicionário de dados](https://suporte.totvs.com/portal/p/10098/download#000006/P12123/P12123DD/)**

**[P12125 - página principal do dicionário de dados](https://suporte.totvs.com/portal/p/10098/download#000006/P12125/P12125DD/)**

**[P12127 - página principal do dicionário de dados](https://suporte.totvs.com/portal/p/10098/download#000006/P12127/P12127DD/)**

**Obs. Procure baixar o dicionário completo Brasil e o diferencial Brasil.**

**Saiba mais sobre CRM:**

**[MP-CRM-COMO-CRIAR-USUÁRIO-NO-CRM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033186534-MP-CRM-COMO-CRIAR-USU%C3%81RIO-NO-CRM)**  
**[MP-CRM-Controle-de-Privilégios-do-CRM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021182892-MP-CRM-Controle-de-Privil%C3%A9gios-do-CRM)**

**[MP-CRM-Como-criar-uma-visão-na-área-de-Trabalho-](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021312172-MP-CRM-Como-criar-uma-vis%C3%A3o-na-%C3%81rea-de-Trabalho-)**

**Documento de referência: <https://tdn.totvs.com/display/public/PROT/Customer+Relationship+Management+-+Protheus+12>**
