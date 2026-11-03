---
article_id: 39792109003799
category: RH - Error.log
content_hash: 6623747711009d609ab1c25f82f42674079fecceb0842c013099775f7a5121ab
fetched_at: '2026-06-28T22:44:49.548677+00:00'
product: protheus
section_id: 32419193161751
source: central-protheus
title: 'RH - Linha Protheus - PON - Error log: Invalid object name ''dbo.PN090LOCKXX'
type: support-article
updated_at: '2026-04-17T11:59:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39792109003799-RH-Linha-Protheus-PON-Error-log-Invalid-object-name-dbo-PN090LOCKXX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39792097803927) Tempo aproximado para leitura: **01:00:00 min**  
  
**Dúvida**  
***Error log*** ao processar qualquer rotina: ***Invalid object name*** **'dbo.PN090LOCKXX'**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para correção do erro, será necessário **reiniciar** os serviços do **DBaccess e Appserver** para que o arquivo do semáforo PN090LOCKXX seja criado no ambiente.  
   
Vale ressaltar que é importante que o ambiente esteja atualizado conforme Portal:  
   
• Expedição contínua - <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1170810>  
• LIB <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/unified-search?query=lib>  
• Binário AppServer [https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/unified-search?query=appserver)  
• Binário SmartClient <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/unified-search?query=webapp>  
• Dbaccess: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/unified-search?query=dbaccess>  
   
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
