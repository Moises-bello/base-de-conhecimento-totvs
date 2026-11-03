---
article_id: 360029389751
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d3696a3ff90869125e254eeb77e1a9eb4d92ead5f22ff30664b87e79695cc7e1
fetched_at: '2026-06-28T22:42:42.052788+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Como reservar automaticamente o lote
  e/ou endereço no momento do empenho do material '
type: support-article
updated_at: '2022-08-03T13:18:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029389751-Manufatura-Linha-Protheus-SIGAPCP-Como-reservar-automaticamente-o-lote-e-ou-endere%C3%A7o-no-momento-do-empenho-do-material
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:00:30 min****Dúvida**É possível reservar automaticamente o **lote/endereço** a ser consumido no momento do **empenho do material**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para no momento do empenho realizar a reserva automaticamente do **lote/endereço** do material a ser consumido, altere na lista de parâmetros do **F12** da rotina **MATA650****- Ordem de Produção** o conteúdo do parâmetro **Sugere Lote/End a Empenhar?** para **Sim** e o conteúdo do parâmetro **MV\_CONSEST - Considera estoque na geração de Ordem de produção** para **S**.
