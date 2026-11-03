---
article_id: 360044784133
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: a874f1a6070022cee1d02f8b2f437c50c9710e0bffa5396cc57cff16421c7a7b
fetched_at: '2026-06-28T22:39:57.373399+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - E348 EMISSÃO
  COM SERVIÇO EVENTUAL NÃO PERMITIDO PELO MUNICÍPIO
type: support-article
updated_at: '2025-06-02T12:21:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044784133-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-E348-EMISS%C3%83O-COM-SERVI%C3%87O-EVENTUAL-N%C3%83O-PERMITIDO-PELO-MUNIC%C3%8DPIO
---

**Ocorrência**Ao realizar a transmissão de uma RPS é apresentado a seguinte rejeição: E348 - EMISSÃO COM SERVIÇO EVENTUAL NÃO PERMITIDO PELO MUNICÍPIO. INFORME UM SERVIÇO QUE NÃO SEJA EVENTUAL.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**A rejeição ocorre quando é utilizado um Código de Serviço temporário que já expirou ou que não poderá ser mais utilizado pela empresa em questão.  
  
Obs.:   
I. A própria prefeitura disponibiliza esse e os demais códigos a serem utilizados;  
II. Geralmente ocorre quando a retenção é dentro do próprio município, para este, citamos como exemplo o município de Paulínia.  
  
**Solução**Verificar no portal da prefeitura ou solicitar para eles quais códigos de serviços corretos e liberados para uso. Após isso preenche-lo no campo B1\_CODISS no Cadastro de Produtos.
