---
article_id: 360028618672
category: Financeiro - Contabilização
content_hash: ffe7a211d385df829acef227f4b3d46126de0788f478815a253eab7d033d64a2
fetched_at: '2026-06-28T22:38:05.229597+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Error.log Alias does
  not exist: SEK  on FA371PROCESSA(FINA371.PRW)'
type: support-article
updated_at: '2025-11-13T19:42:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028618672-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Error-log-Alias-does-not-exist-SEK-on-FA371PROCESSA-FINA371-PRW
---

**Ocorrência**  
Ao acessar a rotina de contabilização **FINA371** com **RPO** do BRASIL é apresentado o *Alias does not exist*: SEK on FA371PROCESSA (FINA371.PRW)  
  
  
**Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 12

**Causa**

O erro ocorre porque a rotina **FINA371** utilizada não é pertinente ao padrão de dicionário brasileiro (bra).  
Essa rotina faz referência à tabela **SEK**, que **não existe para o ambiente do Brasil**, resultando na mensagem apresentada no **error.log**.  
  
Para o Brasil, deve-se utilizar a rotina **CTBAFIN (Contabilização Off-line)**.  
Caso não encontre esta rotina **disponibilizada no menu padrão**, é necessário incluí-la manualmente no **menu SIGAFIN**, através do **Configurador (SIGACFG)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36320200566551)
