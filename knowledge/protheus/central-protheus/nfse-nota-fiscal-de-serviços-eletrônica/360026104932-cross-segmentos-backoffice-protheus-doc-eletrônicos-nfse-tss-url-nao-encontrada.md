---
article_id: 360026104932
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: a61efdb2e83ae2bfa3623650d87b392a1d9a732a0cf7aa5ee344945110f82893
fetched_at: '2026-06-28T22:39:58.600970+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: URL
  nao encontrada para Entidade: xxxxxx Ambiente: 2 Modelo: 56 UF: 3550308'
type: support-article
updated_at: '2022-07-25T19:03:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026104932-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-URL-nao-encontrada-para-Entidade-xxxxxx-Ambiente-2-Modelo-56-UF-3550308
---

**Dúvida**Erro apresentado no console do TSS:URL nao encontrada para Entidade: xxxxxx Ambiente: 2 Modelo: 56 UF: 3550308 Versao: Servico:  
--------------------------------------------------------------------------------------------------------  
WSCERR044 / Não foi possível POST : URL URL nao encontrada para Entidade: xxxxxx Ambiente: 2 Modelo: 56 UF: 3550308 Versao: Servico: ( 11001 : Host not found. )

ADVPL WSDL Client 1.120703 / TOTVS 2011 Série T MSSQL Sped on 20190403 11:13:58

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**O erro ocorre porque houve a tentativa de transmissão de uma NFSE em ambiente de homologação para o município de São Paulo-SP, onde no ambiente não possui a URL correspondente na tabela SPED158 do TSS.

Para correção, basta apenas realizar a atualização das URL's através da documentação abaixo:  
- [Atualização de URL's](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025394911-TSS-Atualiza%C3%A7%C3%A3o-das-URLs-do-TSS)
