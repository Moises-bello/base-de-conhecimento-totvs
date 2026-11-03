---
article_id: 40611399419799
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 00ad542ec16d3a3ee2208b9b4363029f65bffd3fd14b5bb5405d38c80c8d9580
fetched_at: '2026-06-28T22:39:58.628010+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Versões de
  layout não aparecendo na listagem do Wizard.cfg
type: support-article
updated_at: '2026-06-24T17:56:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40611399419799-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Vers%C3%B5es-de-layout-n%C3%A3o-aparecendo-na-listagem-do-Wizard-cfg
---

**Ocorrência**  
Ao acessar o Wizard.cfg da rotina FISA022 não estão sendo apresentadas as versões de layout para configuração:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40611399407127)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões.  
  
**Causa**  
Isso ocorre quando o ambiente está desatualizado (TSS/Protheus).  
  
**Solução**  
Para correção, deverão ser realizados os procedimentos abaixo:  
  
**1. Atualizações**  
Protheus  
- Aplicação da Expedição Contínua: [12.1.2410](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1171486) | [12.1.2510](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1224039) (aceitando apenas os fontes mais recentes)  
  
TSS  
- Aplicação da Expedição Contínua: [12.1.2410](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1164047) | [12.1.2510](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1224026) (aceitando apenas os fontes mais recentes)  
- Inclusão do arquivo tssnewnfse.json na pasta SYSTEM do TSS: [12.1.2410](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1092384) | [12.1.2510](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1092384)  
**[Ambientes TSS Cloud Compartilhado já contemplam as atualizações do TSS]**  
  
**2. Procedimentos**  
Por último e de **extrema importância**, **reiniciar os serviços do ambiente por completo** (DBACCESS, TSS e Protheus), evitando que qualquer thread antiga antes da atualização possa impactar na persistência do problema.
