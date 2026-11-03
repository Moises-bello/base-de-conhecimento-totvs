---
article_id: 36019183178775
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: 2103b3f263e50ffaf4b02418a1ea7f6cb6eb063478fecae787ab662670057cf1
fetched_at: '2026-06-28T22:39:55.133160+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Falha de
  Schema: Element ''{http://www.portalfiscal.inf.br/nfcom}ICMS41'': This element is
  not expected'
type: support-article
updated_at: '2025-10-31T17:35:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36019183178775-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Falha-de-Schema-Element-http-www-portalfiscal-inf-br-nfcom-ICMS41-This-element-is-not-expected
---

**Ocorrência**  
Ao realizar a transmissão de uma NFCOM, ocorre a falha de schema abaixo:  
  
Element '{http://www.portalfiscal.inf.br/nfcom}**ICMS41': This element is not expected.** Expected is one of ( {http://www.portalfiscal.inf.br/nfcom}**ICMS00**, {http://www.portalfiscal.inf.br/nfcom}**ICMS20**, {http://www.portalfiscal.inf.br/nfcom}**ICMS40**, {http://www.portalfiscal.inf.br/nfcom}**ICMS51**, {http://www.portalfiscal.inf.br/nfcom}**ICMS90**, {http://www.portalfiscal.inf.br/nfcom}**ICMSSN**, {http://www.portalfiscal.inf.br/nfcom}**indSemCST** ).  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
Essa falha ocorre por conta do layout e schema atual da Sefaz não permitir o ICMS41:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36019183152151)  
  
Fonte: <https://dfe-portal.svrs.rs.gov.br/Nfcom/Documentos>   
  
**Solução**  
Para correção, o ICMS configurado via TES ou Configurador de Tributos deverá ser uma das opções listadas: ICMS00, ICMS20, ICMS40, ICMS51, ICMS90, ICMSSN ou indSemCST.  
  
Lembrando que qualquer dúvida relacionada à configuração em si desses ICMS, a equipe Fiscal deverá ser acionada.
