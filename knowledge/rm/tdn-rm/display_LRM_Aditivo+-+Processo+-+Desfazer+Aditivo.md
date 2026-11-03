---
content_hash: 373d390695bd8e943e390cebdac1799252095c3ad8353a87bcbd9420ddbc590e
fetched_at: '2026-06-29T00:09:47.070676+00:00'
page_id: '435104906'
product: rm
source: tdn-rm
title: Aditivo - Processo - Desfazer Aditivo
type: documentation
url: https://tdn.totvs.com/display/LRM/Aditivo+-+Processo+-+Desfazer+Aditivo
version: 5
---

Este processo irá desfazer o último aditivo efetivado, e restaurar as últimas informações presentes no sistema, antes da efetivação do último aditivo.

Sejam informações referentes ao aluguel ou até mesmo informações de gestão financeira como por exemplo as alterações de lançamentos.

**Observação:** (restrição para quando se usa o módulo de condomínio): Para os imóveis associados à Subunidades, não será permitido Desfazer o Aditivo, caso haja fechamento de calculado ou integrado ao financeiro, que utilize o Imóvel em questão, dentro do período do Aditivo.

**Observação:** O processo de desfazer o aditivo de alteração de aluguel em dobro realiza o cancelamento das parcelas de aluguel posteriores à data de efetivação do aditivo e, consequentemente, das parcelas do fundo de promoção.

Como o fundo de promoção pode possuir configuração de cálculo vinculada às parcelas de aluguel, é necessário que essas parcelas também sejam canceladas, a fim de manter a integridade das informações.

Dessa forma, para que o aditivo de aluguel em dobro possa ser desfeito, não deve existir nenhuma parcela de aluguel ou de fundo de promoção com status remetido, registrado ou baixado.
