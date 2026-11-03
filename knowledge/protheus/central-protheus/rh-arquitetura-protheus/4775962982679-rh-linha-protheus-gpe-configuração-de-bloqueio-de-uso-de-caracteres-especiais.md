---
article_id: 4775962982679
category: RH - Arquitetura Protheus
content_hash: 5351eaf8afc5c340454e8a9d19d7500d214ea7795b2868ac2910c43fb0215715
fetched_at: '2026-06-28T22:43:03.249967+00:00'
product: protheus
section_id: 206960847
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração de bloqueio de uso de caracteres especiais
type: support-article
updated_at: '2022-07-20T20:24:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4775962982679-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-de-bloqueio-de-uso-de-caracteres-especiais
---

**Dúvida**Como fazer a configuração de bloqueio de uso de caracteres especiais ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O Protheus pode ser configurado para aceitar ou não caracteres especiais (Exemplo: Ç, Ã, Á, etc.)  
O mesmo é configurado a partir do parâmetro MV\_ACENTO no configurador (SIGACFG)  
  
A configuração é possível pois, empresas que não realizam a emissão de notas fiscais tem a opção de aceitar ou não a inserção deste tipo de caracteres  
  
No caso de empresas emissoras de notas fiscais, é aconselhável desabilitar (MV\_ACENTO = N), pois a SEFAZ não aceita notas fiscais que contenham este tipo de caracteres gerando rejeição.
