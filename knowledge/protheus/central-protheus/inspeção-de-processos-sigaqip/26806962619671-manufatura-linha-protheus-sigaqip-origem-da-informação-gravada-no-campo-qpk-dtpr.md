---
article_id: 26806962619671
category: Inspeção de Processos (SIGAQIP)
content_hash: d91f7db6a90124b6e251a94a650e9a46e4395a4848bb6eb0f3bd26d265d053c4
fetched_at: '2026-06-28T22:42:25.890946+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Origem da informação gravada no campo
  QPK_DTPROD - Data de Produção
type: support-article
updated_at: '2024-10-03T12:53:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26806962619671-Manufatura-Linha-Protheus-SIGAQIP-Origem-da-informa%C3%A7%C3%A3o-gravada-no-campo-QPK-DTPROD-Data-de-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26806993182871) Tempo aproximado para leitura: **00:00:45 min** **Dúvida**Qual a origem da informação gravada no campo **QPK\_DTPROD - Data de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**

O campo **QPK\_DTPROD - Data de Produção** pode assumir o valor de um dos 3 campos abaixo, variando segundo as parametrizações realizadas:  
1) Assume o valor do campo **C2\_DATPRI - Data Prevista de Início** se o parâmetro **MV\_QINSPEC - Indica, onde será realizada a Inspeção do Material quando houver integração QIP x PCP** estiver com conteúdo igual a **1**;  
2) Assume o valor do campo **H6\_DTPROD - Data de Produção** se o parâmetro **MV\_QINSPEC** estiver com conteúdo igual **2** e o **Apontamento** for realizado pela rotina **MATA680 - Produção PCP Mod 1** ou **MATA681 - Produção PCP Mod 2**;  
3) Assume o valor do campo **D3\_EMISSAO - Data de Emissão** se o parâmetro **MV\_QINSPEC** estiver com conteúdo igual a **2,** o parâmetro **MV\_QIPOPEP - Define a prioridade dos dados em relação à operação o entre os ambientes QIP e PCP** com conteúdo igual a **3** e **Apontamento** ocorrer pela rotina **MATA250 - Produção Simples**.
