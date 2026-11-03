---
article_id: 360027642592
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 7c5016d5e9605521ace65234634f75aa50c97fb593dc525c404a2cbbec404f68
fetched_at: '2026-06-28T22:39:56.274003+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - A data da
  prestação do serviço deverá estar contida no Período de Vigência do Código de Serviço
type: support-article
updated_at: '2025-07-14T21:41:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027642592-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-A-data-da-presta%C3%A7%C3%A3o-do-servi%C3%A7o-dever%C3%A1-estar-contida-no-Per%C3%ADodo-de-Vig%C3%AAncia-do-C%C3%B3digo-de-Servi%C3%A7o
---

**Ocorrência**Ao realizar a transmissão de uma NFSE é apresentado o erro: '**A data da prestação do serviço deverá estar contida no Período de Vigência do Código de Serviço'.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**De acordo com a rejeição "A data da prestação do serviço deverá estar contida no Período de Vigência do Código de Serviço", isso ocorre pelo fato do Código de Serviço utilizado ter sofrido alguma alteração por parte da Prefeitura.  
  
**Solução**Nesse caso, entre em contato com a prefeitura, pois o código de serviço utilizado na nota não está mais em vigência via Web Service.

A prefeitura irá orientar qual o novo código deverá ser utilizado, neste caso deverá alterar no cadastro de produto com o novo código.

Obs.: O campo para Código de Serviço é o **B1\_CODISS**, com exceção de filiais dos municípios de São Paulo-SP, Recife-PE e e Blumenau-SC que deverão informar no campo **B1\_TRIBMUN**.
