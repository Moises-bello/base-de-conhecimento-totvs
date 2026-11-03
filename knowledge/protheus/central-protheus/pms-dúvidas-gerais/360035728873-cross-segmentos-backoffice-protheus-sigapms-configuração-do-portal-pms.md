---
article_id: 360035728873
category: PMS - Dúvidas Gerais
content_hash: f9b6ea4dfa4d94f9ae8f5604dd7c7806682d27458d8aef9cb531061f7244fb54
fetched_at: '2026-06-28T22:37:17.634559+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Configuração do Portal PMS
type: support-article
updated_at: '2025-11-13T13:25:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035728873-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Configura%C3%A7%C3%A3o-do-Portal-PMS
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36308916686871) Tempo aproximado para leitura: **00:03:00 min******

**Dúvida**

Como configurar o portal do PMS?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões.  
  
**Solução**

A configuração do portal PMS, obedece as mesmas premissas do portal do vendedor**:** ***[PPVD0003\_Configuração\_completa\_do\_Portal\_do\_Vendedor](https://tdn.totvs.com/pages/viewpage.action?pageId=236596491)***

A diferença será a inclusão do calendário (**MATA780**) e do recurso (**PMSA050**) de projeto no módulo PMS , onde o cadastro de recursos deverá ser vinculado ao usuário do configurador para o acesso do portal, no mais, as configurações serão as mesmas.

![calendario de projeto.gif](https://tdn.totvs.com/download/attachments/515277789/calendario%20de%20projeto.gif?version=1&modificationDate=1568295718767&api=v2)

![recurso pms.gif](https://tdn.totvs.com/download/attachments/515277789/recurso%20pms.gif?version=1&modificationDate=1568295753363&api=v2)

![usuÃ¡rio de portal -pms.gif](https://tdn.totvs.com/download/attachments/515277789/usu%C3%A1rio%20de%20portal%20-pms.gif?version=1&modificationDate=1568296079740&api=v2)

Para a configuração do server.ini, basta seguir as informações da Documentação acima (Configuração completa do portal do vendedor).

**Observação:**

No caso do acesso de serviços de integração do SmartERP, é possível o uso do portal, porém é preciso adquirir a licença para o uso deste serviço.

**Saiba mais**:

**[PMS0028 - Configuração do Portal PMS](https://tdn.totvs.com/pages/viewpage.action?pageId=515277789)**

[**Portal do vendedor**](https://tdn.totvs.com/x/eh59IQ)
