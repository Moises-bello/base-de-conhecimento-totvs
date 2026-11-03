---
article_id: 40935270760087
category: Materiais - Compras (SIGACOM)
content_hash: 63db6d75a5322eb3b46881466f76abc1050ba3a87900fcf76b5ad1731f0909e5
fetched_at: '2026-06-28T22:41:11.809377+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Cross Segmentos (Linha Protheus) - Compras (SIGACOM)
  - NFC Pedido de Compras não está carregando Descrição e Centro de custo
type: support-article
updated_at: '2026-06-03T14:40:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40935270760087-Cross-Segmento-TOTVS-Cross-Segmentos-Linha-Protheus-Compras-SIGACOM-NFC-Pedido-de-Compras-n%C3%A3o-est%C3%A1-carregando-Descri%C3%A7%C3%A3o-e-Centro-de-custo
---

O Protheus não carrega corretamente dados além do primeiro item no Pedido de Compras devido à falta da função RestArea() na customização do Ponto de Entrada AVALCOT. Essa função é essencial para restaurar o contexto original da memória, garantindo que todas as linhas sejam alimentadas corretamente. A correção envolve implementar RestArea() conforme a documentação técnica da TOTVS.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40935270755351) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Por que o sistema Protheus não realiza o carregamento correto da descrição (C7\_DESCRI), unidade de medida (C7\_UM), almoxarifado (C7\_LOCAL), conta contábil (C7\_CONTA), centro de custo (C7\_CC) e ordem de produção (C7\_OP) para além do primeiro item no Pedido de Compras (PGCA010)?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2410

**Solução**

O comportamento ocorre devido à ausência da função **RestArea()** dentro da customização do Ponto de Entrada **AVALCOT** utilizado na rotina. Quando o ponto de entrada altera o posicionamento das tabelas na memória sem restaurar o contexto original, as linhas subsequentes do pedido deixam de ser alimentadas corretamente.

Para corrigir o problema, certifique-se de que a implementação do Ponto de Entrada siga as diretrizes da documentação técnica da TOTVS, incluindo obrigatoriamente a utilização da função **RestArea()** para preservar o ambiente durante a execução da rotina customizada. Todas as tabelas utilizadas no ponto precisam passar pelo **RestArea()**

Exemplo:

**RestArea(aAreaSC7)**

**RestArea(aAreaSC1)**

**RestArea(aAreaSB1)**

Documentação Técnica do ponto [AVALCOT](https://tdn.totvs.com/display/PROT/AVALCOT+-+Manipula+Pedido+de+Compras+da+tabela+SC7)

**SAIBA MAIS EM :**

[**PÁGINA CENTRALIZADORA COMPRAS**](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[**Mais Artigos Materiais - Compras (SIGACOM)**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
