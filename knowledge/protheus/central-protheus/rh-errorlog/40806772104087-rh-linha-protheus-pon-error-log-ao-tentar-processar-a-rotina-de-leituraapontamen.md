---
article_id: 40806772104087
category: RH - Error.log
content_hash: c9d4f488b40834c8d21f6d6834aa03c4cec448ff633879bb8f13e47569e36755
fetched_at: '2026-06-28T22:44:49.539783+00:00'
product: protheus
section_id: 32419193161751
source: central-protheus
title: RH - Linha Protheus - PON - Error log ao tentar processar a rotina de Leitura/Apontamento
  (PONM010)
type: support-article
updated_at: '2026-05-28T19:34:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40806772104087-RH-Linha-Protheus-PON-Error-log-ao-tentar-processar-a-rotina-de-Leitura-Apontamento-PONM010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40806745827735) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
**Error log** ao tentar processar a rotina de **Leitura/Apontamento** (PONM010): **DBRUnlock** ***cannot be called in a transaction on*** **UNLOCKREGS(RHLIBLCK.PRX)**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para correção do erro é necessário atualização de APPSERVER e DBACCESS:  
APPSERVER:  
<https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/unified-search?query=appserver>  
  
DBACCESS Linux:  
<https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1168439>  
  
DBACCESS Windows:  
<https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1168438>

**Saiba Mais:**  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
