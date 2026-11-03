---
article_id: 360027618311
category: Escrita Fiscal - Impostos - ICMS
content_hash: b0c9223bf661e7f6e5b867699dcbad0014a70e038d5030b989c589e3641da5ab
fetched_at: '2026-06-28T22:39:25.976232+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- MV_DATAFIS - Configuração
  Data Limite Fiscal
type: support-article
updated_at: '2021-07-20T13:55:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027618311-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-MV-DATAFIS-Configura%C3%A7%C3%A3o-Data-Limite-Fiscal
---

**Dúvida**

Como configurar a data limite fiscal?

**Ambiente**

Todas as versões.

**Solução**

Preencher o parâmetro **MV\_DATAFIS.**

**Descrição do parâmetro:**

Data limite para realização de operações fiscais.

Após a data preenchida no parâmetro o sistema não permite registro de documentos fiscais e nem exclusão de documentos fiscais que foram inseridos no sistema anteriormente a data preenchida no parâmetro.

Após o preenchimento do parâmetro, o sistema não permite que registros fiscais sejam alterados.

A Data que estiver no parâmetro será referente ao dia para bloqueio das operações.

A exclusão de documentos fiscais inseridos no sistema somente será possível, caso a data seja após a data preenchida no parâmetro, pois essa data serve como data limite para alteração.

 Observação: Esse parâmetro bloqueia somente operações fiscais.
