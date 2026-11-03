---
article_id: 4411607483287
category: Faturamento - Integrações
content_hash: 31990dae0a6ec8f9d7676244fd8ef21f8d17039ade91433e68298c86fb3abc8d
fetched_at: '2026-06-28T22:38:26.377308+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Adapter EAI
  Integração CRM '
type: support-article
updated_at: '2024-01-15T16:20:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411607483287-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Adapter-EAI-Integra%C3%A7%C3%A3o-CRM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Mensagens de erro na integração da Nota Fiscal (**MATA461**) do modulo Faturamento Protheus com o sistema TOTVS CRM  
  
"**PaymentConditionInternalId**": "Versï¿½o da condiï¿½ï¿½o de pagamento nï¿½o suportada.\r\nAs versï¿½es suportadas sï¿½o: 1.000, 2.000"  
  
"**CurrencyInternalId**": "Versï¿½o da moeda nï¿½o suportada.\r\nAs versï¿½es suportadas sï¿½o: 1.000, 2.000 e 2.001.",  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS SIGAFAT - Todas as versões  
  
**Solução**

Configurar o **adapter MATA360** com o nome da Transação "**PaymentCondition**" e o **adapter CTBA150** como " **Currency** "  
  
Verificar também atualização dos fontes:  
  
**MATA461.PRX**  
**MATI461.PRW**  
**MATI461O.PRW**

Para atualização, aplique o pacote acumulado do módulo Faturamento: **[SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)**
