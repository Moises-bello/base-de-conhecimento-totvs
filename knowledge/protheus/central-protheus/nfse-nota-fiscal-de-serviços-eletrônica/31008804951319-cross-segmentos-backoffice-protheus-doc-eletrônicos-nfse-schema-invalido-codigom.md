---
article_id: 31008804951319
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: c761da444f71d20ce5c2dfe35a72688fd59d5e47a2afc1c9e04bdf043e3efacd
fetched_at: '2026-06-28T22:39:58.514524+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Schema invalido:
  CodigoMunicipio'':This element is not expected. Expected is IssRetido'
type: support-article
updated_at: '2025-05-21T19:21:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31008804951319-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Schema-invalido-CodigoMunicipio-This-element-is-not-expected-Expected-is-IssRetido
---

**Dúvida**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31008789515927)  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**Esse erro ocorre **porque há mais de um serviço no RPS**.  
A Prefeitura diz que para transmissão via WebService só será aceito um Serviço por RPS.  
Nesse caso é preciso aglutinar os itens, para isso utilize o Parâmetro **MV\_ITEMAGL= S.**

A aglutinação dos itens no XML segue as seguintes regras:

- Todos os itens devem ter a **mesma alíquota de ISS;**  
- Todos os itens devem ter o **mesmo código de ISS;**- Todos os itens devem ter o **mesmo código de CNAE;**  
- Todos os itens devem ter o **mesmo código de Tributação municipal.**

Se os pontos acima não forem respeitados, o rdmake gera a mesma quantidade de itens da nota no XML do RPS, ocasionando erro de SCHEMA.
