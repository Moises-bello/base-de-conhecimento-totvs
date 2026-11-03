---
article_id: 1500013046221
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9bef23389214bba09bb757b681c9dc604608a3c93aef04c66234881439923260
fetched_at: '2026-06-28T22:42:42.041746+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como o Sistema verifica as solicitações
  de compra a serem consideradas no MRP
type: support-article
updated_at: '2021-06-02T19:14:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500013046221-Manufatura-Linha-Protheus-SIGAPCP-Como-o-Sistema-verifica-as-solicita%C3%A7%C3%B5es-de-compra-a-serem-consideradas-no-MRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:35 min  
  
Dúvida**Como o Sistema verifica as **SC - Solicitações de compra** a serem consideradas no **MRP - Material Requiriments Planning**? **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O Sistema realiza as seguintes verificações para considerar as **SCs** no **MRP**:

* Estiverem no mesmo range de **armazéns** definido na parametrização do **MRP**;
* Campo **C1\_RESIDUO - Solic. eliminado resíduo** estiver em branco
* Campo **C1\_QUANT - Quantidade da SC** > **C1\_QUJE - Quantidade em pedido**.
