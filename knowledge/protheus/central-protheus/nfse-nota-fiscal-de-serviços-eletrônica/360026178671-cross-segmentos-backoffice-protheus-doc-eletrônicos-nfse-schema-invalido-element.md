---
article_id: 360026178671
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 93d9c800e2e00291b34dbb7372900b675805db2015fa895545ef8c7c3f45f958
fetched_at: '2026-06-28T22:39:58.516618+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Schema invalido:
  Element Servico This element is not expected Expected is Prestador '
type: support-article
updated_at: '2025-06-20T11:58:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026178671-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Schema-invalido-Element-Servico-This-element-is-not-expected-Expected-is-Prestador
---

**Dúvida**Element '{http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd}Servico': This element is not expected.  
Expected is ( {http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd}Prestador )  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.

**Solução**Esse erro ocorre porque há mais de um serviço no RPS.  
A Prefeitura diz que para transmissão via WebService só será aceito um Serviço por RPS.  
Nesse caso é preciso aglutinar os itens, para isso utilize o Parâmetro MV\_ITEMAGL= S.

A aglutinação dos itens no XML segue as seguintes regras:

- Todos os itens devem ter a mesma alíquota de ISS.  
- Todos os itens devem ter o mesmo código de ISS.  
- Todos os itens devem ter o mesmo código de Tributação municipal.

Se os pontos acima não forem obedecidos, o rdmake gera a mesma quantidade de itens da nota no XML do RPS, ocasionando erro de SCHEMA.
