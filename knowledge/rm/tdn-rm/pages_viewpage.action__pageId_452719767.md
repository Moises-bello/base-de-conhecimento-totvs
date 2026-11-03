---
content_hash: 12af30f2edc870ee793554efd2759820d89254a1dc8a0000f83e1de42915ddac
fetched_at: '2026-06-29T00:10:09.983252+00:00'
page_id: '452719767'
product: rm
source: tdn-rm
title: Código de Cálculo 19 - Adiantamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719767
version: 5
---

Desconto do tipo valor. O sistema descontará o valor do adiantamento pago no mês, lançado no código de cálculo 034 - Pagamento de Adiantamento. Empresas nas quais, no Adiantamento, incida IRRF, deverão marcar a opção "Dedutível IRRF" ou "Estorna IRRF" na pasta Inc. Descontos da Janela de Edição Eventos.

**Atenção**

O campo "Dedutível IRRF" ou "Estorna IRRF" na pasta "Inc. Descontos" deverá ser marcado, quando o sistema estiver trabalhando com o regime de Caixa. Ele não deverá ser marcado, quando o regime for competência.

Lembrete

A marcação do campo Valor Dedutível ou Estorna IRRF é de responsabilidade do usuário, sendo que o valor dedutível refere-se ao que é dedução legal e o valor que estorna é o valor que abate na base do imposto de renda, por exemplo falta.

**Observação**

Se este evento não contiver nenhuma fórmula, o CC19 será lançado com o total de todos os eventos de CC34 (Pagamento de Adiantamento) existente na movimentação mensal. Caso contrário, ele obedecerá a fórmula informada neste evento.

Códigos de Cálculo
