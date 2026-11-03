---
content_hash: ccb90a4834e725b2b19887b8226abd8f52eab2e215db39e67272133b3bb503ad
fetched_at: '2026-06-29T00:08:57.765286+00:00'
page_id: '354475089'
product: rm
source: tdn-rm
title: Lança indenização adicional na dispensa sem justa causa, no período de 30 dias
  antes da data base
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354475089
version: 2
---

**Produto:** TOTVS Folha de Pagamento **Versão:** 12.1  
 **Processo de Negócio:** Folha de Pagamento  
 **Processo do Sistema:** Cálculo da rescisão

**Procedimento**

Criar os eventos com:

Código de Cálculo 344 - Indenização Adicional na Dispensa Antes Data Base

Código de Cálculo 345 - Diferença Indeniz. Adic. na Dispensa Antes Data Base

Sendo que o evento de código de cálculo deverá ter a fórmula para retorno do valor de cada sindicato. No caso do exemplo abaixo a fórmula retorna o salário do funcionário.

Marcar no sindicato o parâmetro: “Lança indenização adicional na dispensa sem justa causa, no período de 30 dias antes da data base” e informar o dia e mês da data base.

Ao calcular uma rescisão que está dentro do prazo de 30 dias que antecede o dia e mês da data base cadastrado no sindicato será lançado o evento de código de cálculo 344.

Quando houver cálculo de rescisão complementar cujo valor da fórmula do código de cálculo 344 seja influenciado, será lançado o evento de código de cálculo 345.

**Observação:** 01 - Estes códigos de cálculo somente serão lançados se o parâmetro estiver marcado e a data informada, caso não satisfaça uma das condições o evento não será lançado.

02 - A data informada no sindicato entra no cálculo de dias, portanto se o aviso for 03/03 terminando dia 01/04 será pago o evento, caso seja 04/03 terminando em 02/04 não será pago o evento.
