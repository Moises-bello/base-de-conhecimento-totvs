---
article_id: 360027348693
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d3dfc18fff2ab07ffd62b8483215a0ece8c8f7b6b8508b19b06013ae762de7d2
fetched_at: '2026-06-28T22:42:42.069307+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Componente não é empenhado com número
  de lote, qual tabela é gravada a informação
type: support-article
updated_at: '2022-01-28T13:22:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027348693-Manufatura-Linha-Protheus-SIGAPCP-Componente-n%C3%A3o-%C3%A9-empenhado-com-n%C3%BAmero-de-lote-qual-tabela-%C3%A9-gravada-a-informa%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura**: 00:00:48 min**  
**Dúvida**Quando o componente controla **lote**, mas não foi empenhado com **Número de lote**, em qual tabela é gravada a informação?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Quando o empenho não possui **Número do lote** a requisição também não terá o **Número do lote** registrado na tabela **SD3 - Movimentações Internas**.  
Porém ao movimentar o **lote**, a requisição é gravada na tabela **SD5 - Requisição por lote**, e através dos campos **D5\_NUMSEQ - Número Sequencial** e **D3\_NUMSEQ - Número Sequencial** é possível realizar a relação.
