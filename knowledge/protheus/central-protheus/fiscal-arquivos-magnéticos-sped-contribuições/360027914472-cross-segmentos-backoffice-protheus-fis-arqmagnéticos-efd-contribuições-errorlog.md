---
article_id: 360027914472
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: a30d409be18a3a7065f3e5c9cd209e085d607c1eff8b344768f9593193177f8c
fetched_at: '2026-06-28T22:42:05.198092+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Errorlog "Alias does not exist: F3N"'
type: support-article
updated_at: '2023-01-04T17:49:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027914472-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Errorlog-Alias-does-not-exist-F3N
---

**Ocorrência**Quando ocorre o **ErrorLog** "*Alias does not exist **F3N** "*  
   
 **Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**Esse incidente ocorre, pois a Tabela **F3N**está corrompida ou foi criada incorretamente no **Banco de Dados.**  
   
 **Solução**1. Fazer o *Download* do **Dicionário de Dados** que está em anexo;  
2. Copiar os arquivos **sdfbra.txt** e **sx2.unq** para a pasta *SYSTEMLOAD* do **Protheus** e Executar o **UPDDISTR**;  
3. Executar a rotina novamente.
