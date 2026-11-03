---
article_id: 360043290254
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 991f99bb977507047a6e7a6c1b27139adb9fae41904407d268fcd3f37f6d6180
fetched_at: '2026-06-28T22:42:40.756318+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Aglutinação de ordens de produção no
  MATA720
type: support-article
updated_at: '2024-07-09T12:44:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043290254-Manufatura-Linha-Protheus-SIGAPCP-Aglutina%C3%A7%C3%A3o-de-ordens-de-produ%C3%A7%C3%A3o-no-MATA720
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24753691081111) Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Quando é possível aglutinar as **OPs - Ordens de Produção**por meio do **MATA720 - Aglutina OPs**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
A aglutinação de **OPs** será possível quando:

* For o mesmo **produto**, **revisão**, **roteiro**, **centro de custo** e **tipo**;
* Tiver os mesmos opcionais;
* Quando as **OPs** estiverem dentro do mesmo período selecionado para aglutinação;
* Não encontrar nenhum apontamento ou requisição de material para a **OP** a ser aglutinada;
* Tiver o mesmo conteúdo no campo **C2\_TPOP - Tipo Op**.

**Importante**  
Se as **OPs** atendem níveis diferentes, não aglutinará.
