---
article_id: 1500004882222
category: Originação de Grãos (OG)
content_hash: 4fe25d0f65e68a6d0bbff879cbef3f2129653dd0a2ebd4f661e3a1824f865bd0
fetched_at: '2026-06-28T22:45:41.203018+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Parâmetro MV_AGRCPVD
type: support-article
updated_at: '2025-04-23T13:32:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004882222-Agro-Linha-Protheus-AGR-Par%C3%A2metro-MV-AGRCPVD
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20476684110999)***Tempo aproximado para leitura:**00:00:25 min**  
**Dúvida**Como informar condição de pagamento utilizada nos **Romaneios de Saída**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O parâmetro **MV\_AGRCPVD - Informar condição de Pagamento nos Roameios de Saída** é do tipo **caracter** e está localizado na rotina de **Romaneio com Pesagem -  OGA250**. Permite informar a **condição de pagamento do tipo 9**, que será utilizada nos romaneios de saída venda.  
  
Caso não exista, será utilizada a condição do parâmetro **MV\_CONDPAD - Condição de Pagamento**. Por meio da condição tipo 9, será gerado o pedido de venda com a data de vencimento igual a data da previsão no **Contrato de Vendas - OGA290**.  
  
**Saiba mais**  
Para mais informações sobre o parâmetro **MV\_CONDPAD**clique no *link*: [MP - SIGALOJA - Parâmetro - MV\_CONDPAD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235440747-MP-SIGALOJA-Par%C3%A2metro-MV-CONDPAD)
