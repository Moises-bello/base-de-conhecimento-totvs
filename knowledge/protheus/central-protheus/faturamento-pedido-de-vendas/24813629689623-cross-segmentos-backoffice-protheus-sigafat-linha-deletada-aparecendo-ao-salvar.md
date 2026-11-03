---
article_id: 24813629689623
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f98dba2cb3e5d5429598e884de5d105f323f2aeda6cd6b1d29003daec663ea71
fetched_at: '2026-06-28T22:38:39.878247+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Linha deletada aparecendo
  ao salvar pedido de de venda
type: support-article
updated_at: '2024-07-11T14:34:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24813629689623-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Linha-deletada-aparecendo-ao-salvar-pedido-de-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24813593325463) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Linha deletada aparecendo ao salvar pedido de de venda, o que é isso?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**Quando as condições em itens do pedido de venda, para um item ser bonificado, o item bonificado é gerado no pedido de venda, sempre, de maneira deletada, abaixo dos itens do pedido de venda.

A TES do produto bonificado é definida pelo parâmetro MV\_BONUSTS.

Caso seja informado diretamente no produto não bonificado a A TES inserida no parâmetro MV\_BONUSTS. O sistema entende que aquele item foi bonificado e o deleta, não sendo o processo indicado.

O item bonificado (sozinho e não informado diretamente) não deve ser tirado do estado de deletado, o sistema trata ele por padrão.

**Saiba mais:**

* [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Regra de Bonificação - FATA090](Cross%20Segmento%20-%20TOTVS%20Backoffice%20(Linha%20Protheus)%20-%20SIGAFAT%20-%20Regra%20de%20Bonifica%C3%A7%C3%A3o%20-%20FATA090)
* [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como tratar regra de bonificação financeira sobre os pedidos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011720347-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-tratar-regra-de-bonifica%C3%A7%C3%A3o-financeira-sobre-os-pedidos)
* [MP - FAT - Período para conceder Bonificação Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011721087-MP-FAT-Per%C3%ADodo-para-conceder-Bonifica%C3%A7%C3%A3o-Financeira)
* [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de Entrada da rotina FATA090](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402506410647-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-Entrada-da-rotina-FATA090)
