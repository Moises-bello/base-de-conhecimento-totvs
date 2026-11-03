---
article_id: 360027987311
category: Escrita Fiscal - Error.log
content_hash: a70c7423c28b321d0f416e6c24b98fbfd22ae1e9d567f2af392e8e86589baa39
fetched_at: '2026-06-28T22:39:32.924186+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: MP - FIS - Errorlog "Alias does not exist F3K" ou "Alias does not exist CDV"
type: support-article
updated_at: '2025-02-04T19:16:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027987311-MP-FIS-Errorlog-Alias-does-not-exist-F3K-ou-Alias-does-not-exist-CDV
---

**Ocorrência**Quando ocorre o **ErrorLog** "*Alias does not exist **F3K***" ou "*Alias does not exist **CDV***".  
  
 **Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**Esse incidente ocorre, pois as Tabelas **F3K** ou **CDV** estão corrompidas ou foram criadas incorretamente no **Banco de Dados**.  
   
 **Solução**  
 1. Fazer o *Download* do **Dicionário de Dados** que está em anexo;  
 2. Copiar os arquivos **sdfbra.txt** e **sx2.unq** para a pasta *SYSTEMLOAD* do **Protheus** e Executar o **UPDDISTR**;  
 3. Executar a rotina novamente.
