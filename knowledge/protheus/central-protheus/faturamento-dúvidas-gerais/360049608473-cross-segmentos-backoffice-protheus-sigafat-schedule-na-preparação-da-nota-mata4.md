---
article_id: 360049608473
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 309a4bb801e636a638c3633e7670bc8e89799b0f99e93a94b33b14683b39f0f7
fetched_at: '2026-06-28T22:38:29.882670+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Schedule na preparação da
  nota (MATA460a ou MATA461).
type: support-article
updated_at: '2024-04-16T14:56:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049608473-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Schedule-na-prepara%C3%A7%C3%A3o-da-nota-MATA460a-ou-MATA461
---

**Dúvida**

É possível utilizar **S*****chedule*** na rotina de preparação da nota (**MATA460a** ou **MATA461**)?  
  
**Ambiente**Microsiga Protheus- todas as versões.  
  
**Solução**

Não existe chamada para tratamento via Schedule da Preparação de Documento de Saída ( **MATA460a** ou **MATA461**), o sistema não habilita a opção de parametrização, indicando que **não é possível** schedular.

Além disso, no fonte **MATA461**, chama a função **FTjobnfs da rotina FATxJOB** para a realização da geração da nota, onde não existe chamada para tratamento relacionado a **Schedule**.  
  
O que é possível tratar no **Schedule:**

**1-Atualização tardia do estoque :** **[MP - FAT - Atualização de Estoque tardia na geração da NF de Saída MV\_NFS\_JOB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020914632-MP-FAT-Atualiza%C3%A7%C3%A3o-de-Estoque-tardia-na-gera%C3%A7%C3%A3o-da-NF-de-Sa%C3%ADda-MV-NFS-JOB)**

**2-Transmissão, Monitoramento e Cancelamento Automáticos: [MP - NFE - AUTONFE Transmissão, Monitoramento e Cancelamento Automáticos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029358971-MP-NFE-AUTONFE-Transmiss%C3%A3o-Monitoramento-e-Cancelamento-Autom%C3%A1ticos?source=search)**
