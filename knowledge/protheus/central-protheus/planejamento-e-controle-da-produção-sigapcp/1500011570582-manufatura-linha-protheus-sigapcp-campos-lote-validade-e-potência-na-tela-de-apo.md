---
article_id: 1500011570582
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 4a2bc99b9a7a6f32e89e1ca189e12eb3ae1d8267b45a9e9c52e41d0b2d22c4f7
fetched_at: '2026-06-28T22:42:41.023068+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Campos lote, validade e potência na
  tela de apontamento de produção
type: support-article
updated_at: '2021-05-21T11:48:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011570582-Manufatura-Linha-Protheus-SIGAPCP-Campos-lote-validade-e-pot%C3%AAncia-na-tela-de-apontamento-de-produ%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Por que os campos **D3\_LOTECTL - Lote**, **D3\_DTVALID  - Validade do Lote Informado** e **D3\_POTENCI - Potência do Lote** não são apresentados na tela do **MATA250 - Produção Simples**, mesmo estando habilitados?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Esses campos não são listados na tela quando o parâmetro **MV\_PRODAUT - Gera lançamentos automáticos de produção das ordens de produções vinculadas a OP - Ordem de produção pai** está habilitado.   
Isso porque quando o parâmetro **MV\_PRODAUT** está habilitado são gerados os lotes para todos os produtos que controlam lote e tem suas **OPs** apontadas, e para permitir a edição dos dados dos lotes ao confirmar o apontamento é apresentada uma tela listando os produtos e os dados de seus respectivos lotes.
