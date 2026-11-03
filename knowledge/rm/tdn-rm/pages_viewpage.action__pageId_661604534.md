---
content_hash: 2bd8656bc43a9625002ccb41549bd4fe02737f3cc16c5a6c5caf97b05cdc56e1
fetched_at: '2026-06-29T00:11:15.668126+00:00'
page_id: '661604534'
product: rm
source: tdn-rm
title: Aluguel Complementar - Controle de Faturamento Diário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=661604534
version: 8
---

### Introdução

---

Disponível a partir da versão 12.1.2205, o controle de faturamento diário segue as mesmas premissas do [controle de faturamento](https://tdn.totvs.com/pages/viewpage.action?pageId=520659292) por competência, entretanto, seu cadastro pode ser feito diariamente, possibilitando flexibilizar as cobranças complementares associadas ao contrato.

### Procedimentos para utilização

---

Para que este anexo possa estar disponível, devemos primeiro conferir acesso ao mesmo em *Serviços Globais / Segurança / Perfis*. Na imagem abaixo a permissão que deverá ser concedida:

Com a permissão habilitada, poderemos cadastrar um controle de faturamento diário em *Aluguel / Contrato de Locação / Anexo / Controle de Faturamento Diário*

Os campos deste cadastro são:

* **Código Medição Diário:** Auto incremental, não editável.
* **Data da medição:** Data cuja medição será processada. A data da medição deve estar dentro do período da faixa cadastrada no aluguel complementar.
* **Valor do Faturamento:** Valor do faturamento no dia.
* **Valor do Faturamento 2:** Valor do faturamento 2 no dia.

O faturamento 2 só será habilitado quando o contrato possuir faixa do tipo **faturamento composto** e a data da medição estar dentro do período desta faixa.

Para contratos rescindidos ou distratados, será possível inserir medições, contanto que sejam cadastradas em períodos que compreendam o tempo de vigência do contrato de locação.

Veja mais

---

* [Aluguel - Contrato de Locação - Gerar Aluguel Complementar](https://tdn.totvs.com/pages/viewpage.action?pageId=435105013)
* [Aluguel - Contrato de Locação - Cancelar Aluguel Complementar](https://tdn.totvs.com/pages/viewpage.action?pageId=520659357)
* [Aluguel - Contrato de Locação - Importação de Medição de Faturamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105012)
