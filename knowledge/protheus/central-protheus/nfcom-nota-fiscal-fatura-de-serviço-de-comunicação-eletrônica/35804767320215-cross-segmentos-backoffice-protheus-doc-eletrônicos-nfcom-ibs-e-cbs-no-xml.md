---
article_id: 35804767320215
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: 1a2009f5e308762b3ae47c162300a9ee6fc1daeb6c4bd6cfe36cd31fda480edc
fetched_at: '2026-06-28T22:39:55.142730+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - IBS e CBS
  no XML
type: support-article
updated_at: '2025-10-22T13:59:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35804767320215-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-IBS-e-CBS-no-XML
---

**Dúvida**  
Como destacar os novos impostos de IBS e CBS no XML da NFCOM?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões.  
  
**Solução**  
Conforme divulgado pela Sefaz, o grupo de IBSCBS foi adiado para **03/11/2025** em **ambiente de homologação:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35804810970135)  
Fonte: <https://dfe-portal.svrs.rs.gov.br/Nfcom/Documentos#> (Menu Notas Técnicas).  
  
Já no **ambiente de produção**, permanece com data de **01/11/2025.**  
Caso sejam enviadas antes dessas datas, ocorrerão rejeições.  
  
E para se adequar, basta providenciar a compilação do rdmake **NFCOMSEFAZ** no RPO do Protheus:  
- 12.1.2310: <https://r.totvs.io/p/1216904> [SOMENTE GARANTIA ESTENDIDA]   
- 12.1.2410: <https://r.totvs.io/p/1216902>  
  
Lembrando que os impostos IBS e CBS serão obtidos a partir do Configurador de Tributos:  
- <https://tdn.totvs.com/pages/releaseview.action?pageId=990757992>
