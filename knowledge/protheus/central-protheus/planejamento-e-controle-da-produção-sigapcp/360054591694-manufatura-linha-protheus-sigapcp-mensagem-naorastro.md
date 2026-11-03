---
article_id: 360054591694
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 62c5dc0050cc19f4e964a70ec4fa6191dc7adb4a0d455d16ad48a1dd78067cde
fetched_at: '2026-06-28T22:42:44.523937+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem NAORASTRO
type: support-article
updated_at: '2022-02-16T18:07:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054591694-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-NAORASTRO
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:42 min**  
**Ocorrência**No módulo **PCP - Planejamento e Controle da Produção** ao realizar o apontamento no **MATA250 - Apontamento de Produção** e informar um lote no campo **D3\_LOTECTL - Lote** é apresentada a mensagem **NAORASTRO**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem é apresentada pois o produto da **OP - Ordem de Produção** não controla **Lote**.  
  
**Solução**Para que essa mensagem não seja apresentada primeiro é necessário avaliar se o parâmetro **MV\_RASTRO - Determina a utilização ou não da Rastreabilidade dos Lotes de Produção** está **ativo**.  
Depois é necessário informar no **MATA010 - Cadastro do Produto** o campo **B1\_RASTRO - Rastro** igual a **L -Lote**.
