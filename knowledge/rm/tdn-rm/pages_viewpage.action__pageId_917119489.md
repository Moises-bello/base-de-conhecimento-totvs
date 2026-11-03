---
content_hash: bedb00a71402590091cb707137e7b1049c96f9a100e75a02aa52e084d4154859
fetched_at: '2026-06-29T00:12:06.872972+00:00'
page_id: '917119489'
product: rm
source: tdn-rm
title: Proposta - Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=917119489
version: 5
---

O objetivo desta página é explicar o funcionamento dos relatórios padrão utilizados na proposta do PI.

Importante!

* Regras principais para criação/alteração de relatórios para impressão no PI -

**Dentro da Proposta:**

* Plano de Pagamento

**Na visão de Propostas:**

* Proposta: Imprimir
* Plano de Pagamento: Imprimir

Ao definir o plano de pagamento na proposta, ele será impresso conforme estabelecido na negociação entre corretor e comprador. As datas definidas nesse momento serão respeitadas na impressão, mesmo que existam parametrizações invisíveis na montagem do plano que influenciem diretamente sua estrutura.

Um desses parâmetros é a prioridade dos componentes geradores de parcela, responsável por ajustar as datas de vencimento. Caso duas parcelas coincidam na mesma data, a de menor prioridade será deslocada até que não haja conflito. No entanto, isso não altera a data originalmente definida na negociação.

**Exemplo:**  
No cenário abaixo, a parcela "Sinal" coincide com a parcela "Mensal" em 03/2024. Assim, as parcelas "Mensal" serão ajustadas para começar apenas após o término das parcelas "Sinal".

**Sinal**

* Data de Início: 18/02/2025
* Quantidade de Parcelas: 5
* Prioridade: 0

**Mensal**

* Data de Início: 18/03/2025
* Quantidade de Parcelas: 80
* Prioridade: 1

Nos relatórios, a negociação original será preservada, mas as parcelas serão exibidas conforme o ajuste automático realizado pelo *TOTVS Construção Gestão de Imóveis*.

Veja a demonstração no vídeo abaixo:

250
