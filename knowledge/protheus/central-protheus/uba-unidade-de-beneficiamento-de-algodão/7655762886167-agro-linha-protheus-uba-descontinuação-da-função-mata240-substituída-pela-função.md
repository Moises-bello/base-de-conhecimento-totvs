---
article_id: 7655762886167
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 5892bca87b9944ebce7a9c880b6dfe547e4c33a7f73b3190e4587adb3d042039
fetched_at: '2026-06-28T22:45:35.586801+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Descontinuação da função MATA240, substituída
  pela função MATA241
type: support-article
updated_at: '2025-06-18T14:03:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7655762886167-Agro-Linha-Protheus-UBA-Descontinua%C3%A7%C3%A3o-da-fun%C3%A7%C3%A3o-MATA240-substitu%C3%ADda-pela-fun%C3%A7%C3%A3o-MATA241
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21895919363991) Tempo aproximado para leitura: **00:00:40 min** **Dúvida**Qual a mudança que teve na rotina **AGRA600**, depois da descontinuação do **Movimentação Simples - MATA240**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - Versão 12  
  
**Solução**Na rotina **Romaneio de entrada - AGRA600** foi removido a chamada da função **Gera estorno sem Ordem de Produção - A600GERAD3**, a qual gerava estorno quando havia somente movimentação de estoque sem ordem de produção.  
Em análise, atualmente o Sistema sempre gera a ordem de produção e as movimentações. Esta função existia para compatibilidade de uma regra de negócio já descontinuada na versão **Protheus 11 - P11**, sendo assim a função **A600GERAD3** passará a ser descontinuada.
