---
article_id: 35188606683415
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: 46d19579ba45c3d284589a5d4db1d92c4991c96c6b9d9f1319ef11a60e69f976
fetched_at: '2026-06-28T22:39:55.129521+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Falha de
  Schema: Element ''{http://www.portalfiscal.inf.br/nfcom} total'': This element is
  not expected'
type: support-article
updated_at: '2025-09-25T13:09:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35188606683415-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Falha-de-Schema-Element-http-www-portalfiscal-inf-br-nfcom-total-This-element-is-not-expected
---

**Ocorrência**  
Ao realizar a transmissão de uma NFCOM ocorre a falha de schema abaixo:  
  
Element '{http://www.portalfiscal.inf.br/nfcom}  
total': This element is not expected. Expected is one of (  
{http://www.portalfiscal.inf.br/nfcom}gSub,  
{http://www.portalfiscal.inf.br/nfcom}gCofat,  
{http://www.portalfiscal.inf.br/nfcom}det ).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35188606679831)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois não foi encontrado o complemento fiscal da nota.  
  
**Solução**  
Para correção, deverá acessar a rotina **MATA920** e realizar o preenchimento **completo** do Complemento Fiscal para a NFCOM, **o qual é obrigatório para todas as notas.**  
  
Exemplo abaixo para uma nota de saída:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35188606680215)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35188629124631)  
  
**IMPORTANTE**  
Qualquer dúvida no preenchimento do Complemento Fiscal, a equipe de Arquivos Magnéticos deverá ser acionada.
