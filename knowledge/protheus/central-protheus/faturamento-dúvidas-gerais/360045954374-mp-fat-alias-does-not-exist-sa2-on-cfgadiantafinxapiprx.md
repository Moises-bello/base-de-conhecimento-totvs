---
article_id: 360045954374
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 02511b1f546aae00848abbd89b643378e380deaa9670d3796f1a7a06bed9108c
fetched_at: '2026-06-28T22:38:31.156772+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Alias does not exist SA2 on CFGADIANTA(FINXAPI.PRX)
type: support-article
updated_at: '2021-04-28T15:53:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045954374-MP-FAT-Alias-does-not-exist-SA2-on-CFGADIANTA-FINXAPI-PRX
---

**Ocorrência**

Após configurar o server.ini para utilização do **FATJOBNFE**,  o console do server apresenta o seguinte erro:

**Alias does not exist SA2 on CFGADIANTA(FINXAPI.PRX) 23/03/2020 16:25:43 line : 28**

**Ambiente**

Microsiga Protheus - a partir da verão 12.

**Causa**

O erro era caudao devido as variáveis **Staticas** que eram carregadas antes do **PrepareEnvironment** do **FatJobNFE**, e então a função **CFGAdianta** tentava abrir as tabelas antes do **Prepare Environment**, causando erro ao iniciar o **JOB**.

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do **pacote de correção** ,conforme a release de sistema:

**12.1.27:<https://r.totvs.io/p/956812> ;**

**12.1.25:<https://r.totvs.io/p/956811> ;**

**12.1.23:<https://r.totvs.io/p/956810> ;**

**12.1.17:<https://r.totvs.io/p/956809> (apenas para garantia estendida);**

2. Aplique o pacote via TDS ou o VS-CODE, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
