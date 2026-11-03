---
article_id: 115004675167
category: Financeiro - Movimentação Bancária
content_hash: cf3652fa1b01e7b9df0b380f0e66706e7197d0e4ee59f8b0a90d8de688d62aeb
fetched_at: '2026-06-28T22:38:19.518904+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: MP - SIGAFIN - FINA100 - Como é validado os CSTs de créditos na rotina de Movimentos
  bancários
type: support-article
updated_at: '2021-04-28T15:52:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004675167-MP-SIGAFIN-FINA100-Como-%C3%A9-validado-os-CSTs-de-cr%C3%A9ditos-na-rotina-de-Movimentos-banc%C3%A1rios
---

**Dúvida**Como é validado os CSTs de créditos na rotina de Movimentos bancários? 

**Ambiente**Microsiga Protheus – Financeiro – FINA100 - A apartir da versão 11.80

**Solução**A partir de 11/05/2016 foi disponibilizado a validação dos CSTs de créditos na rotina **FINA100** (Movimentos bancários).

Caso o movimento possua uma natureza contendo um CST de crédito e não possua o campo **E5\_CLIFOR** preenchido a rotina exibirá um alerta dizendo para escolher outra natureza ou preencher o campo **E5\_CLIFOR**.

**Saiba mais:**Para que não seja validado o CST de crédito, há o ponto de entrada **Fa100Nat**.
