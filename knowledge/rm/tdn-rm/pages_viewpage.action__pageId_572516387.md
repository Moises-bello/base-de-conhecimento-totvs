---
content_hash: 3cdace5b561402eabb44d5373a08cba3047189d68ac1266c51e53cad873cb15a
fetched_at: '2026-06-29T00:10:52.446884+00:00'
page_id: '572516387'
product: rm
source: tdn-rm
title: Código de Cálculo 441 - 13º SALÁRIO CONTRATO VERDE AMARELO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572516387
version: 3
---

Provento do tipo valor.

Quando a 1ª parcela de 13º salário for calculada e existir evento com esse código de cálculo na ficha financeira, o evento terá seu valor acumulado para desconto do valor já pago como adiantamento da 1ª parcela de 13º salário.

**Exemplo:**

Criado os eventos de 13º salário e Média de 13º salário, ambos com código de cálculo 0 e lançado no envelope de pagamento do funcionário contratado por contrato verde amarelo nos meses de janeiro a junho.

No mês de julho o contrato passou a ser por tempo indeterminado.

Nesse caso os eventos criados para pagamento 13º salário e Média de 13º salário no contrato verde amarelo devem ter seus códigos de cálculo alterados para o código de cálculo 441 – 13º salário Contrato Verde Amarelo.

No pagamento da 1ª parcela de 13º salário em novembro o cálculo será:

Calculando evento: 0009 - 1ª PARCELA 13º SALARIO

              Código de Cálculo 9 - Prioridade 0

                     Data de Admissão: 06/01/2020

                     Total de Avos de Direito = 12

                     Salário Total: 2.000,000000

                     Valor pago no evento de cc 441 nos meses 01, 02, 03, 04, 05, 06/2020: 935,48

                     13o.Salário a ser pago: 2.000,000000 - 935,48 = 1.064,520000

                     Valor da 1ª Parcela: 13 salário(1.064,520000) / 2 = 532,260000

                     Valor do evento: 532,26

Para o calcular a 2a parcela conforme salário atual será descontado valores pagos antecipadamente e que serão acumulados nesse código de cálculo.

**Exemplo:**

Seguindo os dados do exemplo anterior, no pagamento da 2ª parcela de 13º salário em dezembro o cálculo do desconto será:

Calculando evento: 0035 - ADIANTAMENTO 13º SALARIO

              Código de Cálculo 35 - Prioridade 81

                     Valor pago no evento de cc 9 no mês 11/2020: 532,26

                     Valor pago no evento de cc 441 nos meses 01, 02, 03, 04, 05, 06/2020: 935,48

                     Valor do evento: 1.467,74
