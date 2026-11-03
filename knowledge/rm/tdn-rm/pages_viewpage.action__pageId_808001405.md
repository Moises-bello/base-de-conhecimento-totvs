---
content_hash: 8172c72d0ea6500343945dfacf30a90265446258c43a8249a63e99cd6416213f
fetched_at: '2026-06-29T00:11:43.533247+00:00'
page_id: '808001405'
product: rm
source: tdn-rm
title: Padrão - SmartUI - Desenvolvimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808001405
version: 3
---

Para o padrão de visão dos dados para CRUD simples segue o layout a ser utilizado no componente.  
  
<t-page-resource  
  [t-service-api]="serviceApi"  
  [t-schema-api]="schemaApi"  
  [t-striped]="true"  
  [t-actions-inline-table]="true"  
  t-route-resource="cadgerais"  
  [t-process-options]="processOptions"  
  [t-allow-delete]="true"  
  [t-selectable]="true"  
>  
</t-page-resource>

Padrão - APIs   
  
seguir o padrão criado para estado civil (ImbEstadoCivilController) ou midia (ImbMidiaController)
