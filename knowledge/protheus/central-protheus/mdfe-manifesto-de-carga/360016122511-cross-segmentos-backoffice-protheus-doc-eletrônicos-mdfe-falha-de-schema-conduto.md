---
article_id: 360016122511
category: MDFe - Manifesto de Carga
content_hash: 5534156d409ae5d039f521a523b1539f3679f37c60c10955b3bd6f1b9913e80e
fetched_at: '2026-06-28T22:40:08.287320+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Falha de
  Schema Condutor
type: support-article
updated_at: '2025-06-17T18:11:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016122511-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Falha-de-Schema-Condutor
---

**Dúvida**Como solucionar Falha de Schema Condutor ?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

Ao transmitir **MDFe** ocorrem duas falhas de Schemas:

Element '{[http://www.portalfiscal.inf.br/mdfe}tpRod](http://www.portalfiscal.inf.br/mdfe%7dtpRod)': This element is not expected. Expected is one of ( {[http://www.portalfiscal.inf.br/mdfe}capM3](http://www.portalfiscal.inf.br/mdfe%7dcapM3),  
{[http://www.portalfiscal.inf.br/mdfe}prop](http://www.portalfiscal.inf.br/mdfe%7dprop),   
{[http://www.portalfiscal.inf.br/mdfe}condutor](http://www.portalfiscal.inf.br/mdfe%7dcondutor) ).

ou

Element '{http://www.portalfiscal.inf.br/mdfe}tpRod': This element is not expected.   
Expected is one of ( {http://www.portalfiscal.inf.br/mdfe}capKG,   
{http://www.portalfiscal.inf.br/mdfe}capM3,   
{http://www.portalfiscal.inf.br/mdfe}prop,   
{http://www.portalfiscal.inf.br/mdfe}condutor ).

Isso quer dizer que enquanto o condutor do veículo (motorista) que é obrigatório, não estiver preenchido no cadastro do veículo, gera essa falha.

Campo do motorista **DA3\_MOTORI**, após alterar o cadastro de veículo vinculando o motorista nesse campo exclua o MDFe e gere novamente.

Além disso, no cadastro de motorista os campos **NOME e CPF** devem estar preenchidos.
