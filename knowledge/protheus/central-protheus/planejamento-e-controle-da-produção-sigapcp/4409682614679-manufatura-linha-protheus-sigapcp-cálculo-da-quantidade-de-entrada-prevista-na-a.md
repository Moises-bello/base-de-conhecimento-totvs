---
article_id: 4409682614679
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: b5ef5411147964a1f18a8d07668905521a5ec7befe3d711fb3b72a18d09c78dc
fetched_at: '2026-06-28T22:42:40.944279+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Cálculo da quantidade de entrada prevista
  na abertura da OP Intermediária
type: support-article
updated_at: '2021-09-29T13:49:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409682614679-Manufatura-Linha-Protheus-SIGAPCP-C%C3%A1lculo-da-quantidade-de-entrada-prevista-na-abertura-da-OP-Intermedi%C3%A1ria
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min  
  
Dúvida**Como o Sistema calcula a **quantidade de entrada prevista** na abertura da **OP Intermediária**? **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Com o parâmetro **MV\_CONSEST - Considera Estoque na Geração de Ordem de Produção?** igual a **S**, o Sistema avalia a **quantidade prevista de entrada** informada no campo **B2\_SALPEDI - Qtde prevista p/ entrar** e subtrai a **quantidade empenhada** informada no campo **B2\_QEMP - Quantidade Empenhada**.Se o campo **B2\_QEMP** do **produto intermediário** estiver com a mesma quantidade do campo **B2\_SALPEDI**, o Sistema não considera essa **entrada prevista** para abrir a **OP Intermediária**.
