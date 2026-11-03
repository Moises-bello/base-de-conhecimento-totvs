---
article_id: 360059449713
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 21db2d47cfc2918e1872f377de6a0b0016db2ae98ace4e0d29877b34e879c685
fetched_at: '2026-06-28T22:42:47.113719+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Validação de saldo no empenho do material
type: support-article
updated_at: '2021-06-17T16:40:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059449713-Manufatura-Linha-Protheus-SIGAPCP-Valida%C3%A7%C3%A3o-de-saldo-no-empenho-do-material
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min  
  
Dúvida**Em qual situação ocorre a validação de **saldo** no momento do **empenho do material**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
A validação do **saldo** do item em estoque no momento do **empenho** ocorre quando é feita a reserva do **lote/endereço**, o Sistema valida se existe **saldo** disponível dos componentes para empenhar com **lote/endereço.**  
Quando a **OP - Ordem de Produção** é aberta e não é feita a reserva do **lote/endereço** no empenho, o Sistema não valida se existe **saldo** disponível dos componentes e a análise do **saldo** será realizada somente no momento em que ocorrer a requisição do material, via apontamento de produção ou requisição manual.
