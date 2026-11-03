---
article_id: 360028194151
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: ae44508c6d32399fbcc7b0371cf01926c1057ccc1a6c5e65085bd9880b4f60f1
fetched_at: '2026-06-28T22:42:05.194977+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Errorlog "Alias does not exist: F2Z"'
type: support-article
updated_at: '2023-01-04T17:49:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028194151-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Errorlog-Alias-does-not-exist-F2Z
---

**Ocorrência**Quando ocorre o **ErrorLog** "*Alias does not exist **F2Z**"*  
   
 **Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**Esse incidente ocorre, pois a Tabela **F2Z**está corrompida ou foi criada incorretamente no **Banco de Dados.**  
   
 **Solução**1. Fazer o *Download* do **Dicionário de Dados** que está em anexo;  
2. Copiar os arquivos **sdfbra.txt** e **sx2.unq** para a pasta *SYSTEMLOAD* do **Protheus** e Executar o **UPDDISTR**;  
3. Executar a rotina novamente.
