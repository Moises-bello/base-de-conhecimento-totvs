---
article_id: 360049722513
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 934134b4835c0b6084ed754f5503b34640657c91ae52fe8da4569769252754b8
fetched_at: '2026-06-28T22:38:33.139814+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP - FAT - Uso de Sublote na Contabilização de Documentos Online e Offline
  (CTBANFS)
type: support-article
updated_at: '2021-04-28T15:53:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049722513-MP-FAT-Uso-de-Sublote-na-Contabiliza%C3%A7%C3%A3o-de-Documentos-Online-e-Offline-CTBANFS
---

**Dúvida**

Como utilizar Sublotes na Contabilização de Documentos Online e Offline (**CTBANFS**)?  
   
 **Ambiente**

Microsiga Protheus –  A partir da versão 12.  
  
**Solução**

O parâmetro **MV\_SUBLOTE** contém o numero do **Sublote** **padrão** informado no campo "Sub-lote" (**CT5\_SBLOTE**) do cadastro de **Lançamentos Padronizados**.

Caso o parâmetro esteja **em branco**, o sistema habilita o campo "Sub-lote" (CT5\_SBLOTE) para **preenchimento manual**, esta informação é levada para o campo **CT2\_SBLOTE** na contabilização dos documentos.

![01.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360074315593/01.PNG)

Porém, não é possível utilizar **sublotes diferentes** no mesmo processo, pois a chave contábil é composta pelos campos **Filial + Data + Lote + Sub-Lote + Documento**, este conceito de uso existe para **todas as rotinas** de contabilização do sistema.

**Saiba Mais**: **<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019073652-MP-SIGACTB-N%C3%9AMERO-DE-LOTE-CONT%C3%81BIL?source=search]&nbsp;j>**
