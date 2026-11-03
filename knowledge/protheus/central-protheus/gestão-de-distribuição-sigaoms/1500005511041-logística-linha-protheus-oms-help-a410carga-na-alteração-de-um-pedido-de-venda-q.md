---
article_id: 1500005511041
category: Gestão de Distribuição (SIGAOMS)
content_hash: f232022edd2412e43b2eb1821e73897e5bbd2f824e3c8e6d8380cf4ae171f8b1
fetched_at: '2026-06-28T22:45:49.853783+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Help A410CARGA na alteração de um pedido
  de venda que está vinculado a uma  carga
type: support-article
updated_at: '2021-07-12T19:24:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005511041-Log%C3%ADstica-Linha-Protheus-OMS-Help-A410CARGA-na-altera%C3%A7%C3%A3o-de-um-pedido-de-venda-que-est%C3%A1-vinculado-a-uma-carga
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:12 min**  
**Ocorrência**Como tratar o **help A410CARGA** na alteração de um pedido de venda que está **vinculado a uma carga?**  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
 **Causa**Ao alterar um pedido de venda pela rotina **Pedido de Venda - MATA410,** caso o pedido esteja vinculado a uma carga no modulo **SIGAOMS - Order Management System,** será apresentado o **help A410CARGA**. O **Help** verifica se o pedido contém carga montada. Essa informação é gravada na tabela **SC9**, **campo C9\_CARGA**.  
  
**Solução**Caso prossiga com a alteração do pedido de venda, **automaticamente o pedido será retirado da carga.** Esse comportamento ocorre, devido a amarração da carga ser realizada com **base na tabela SC9**. Quando ocorre a alteração do pedido de venda, **o Sistema deleta tabela a SC9**, esse é comportamento do Modulo de Faturamento.Para que o **help A410CARGA**, não seja apresentado na alteração do pedido de venda, indicamos a utilização do **Ponto de Entrada OMSPEDCG.**  
  
**Saiba mais**Mais informações poderão ser acessadas nos *link*: [DT PE OMSPEDCG - Pedido em carga montada.](https://tdn.totvs.com/display/PROT/DT+PE+OMSPEDCG+-+Pedido+em+carga+montada)
