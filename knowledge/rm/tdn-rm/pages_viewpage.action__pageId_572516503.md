---
content_hash: f8e7695e6d7d929d74833092ddf8b53fb5955abc0681c4e14c9ed7bdf57efb60
fetched_at: '2026-06-29T00:10:52.450879+00:00'
page_id: '572516503'
product: rm
source: tdn-rm
title: DT- MP 905 - Cálculo do 13º salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572516503
version: 2
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Cálculo de 13º salário |
| **Situação/Requisito:** | Para a MP 905 foi previsto que ao final de cada mês, o empregado receberá o pagamento imediato das seguintes parcelas: remuneração; décimo terceiro salário proporcional; e férias proporcionais com acréscimo de um terço e sobre todo o montante incidirá a alíquota mensal de dois por cento à título de FGTS.  Na conversão do contrato verde amarelo para prazo indeterminado dentro do ano há a necessidade de calcular o 13º salário considerando as parcelas já pagas mensalmente. |
| **Solução/Implementação:** | Criado o código de cálculo 441 – 13º salário Contrato Verde Amarelo que é um provento do tipo valor.  Quando a 1ª parcela de 13º salário for calculada e existir evento com esse código de cálculo na ficha financeira, o evento terá seu valor acumulado para desconto do valor já pago como adiantamento da 1ª parcela de 13º salário.  Para o calcular a 2a parcela conforme salário atual serão descontados valores pagos antecipadamente e que serão acumulados nesse código de cálculo.  Na orientação do cálculo da MP 905 foi para criar evento com “código de cálculo 0 – Sem Código de Cálculo Existente”, isso antes da liberação do “código de cálculo 441 - 13º SALÁRIO CONTRATO VERDE AMARELO”, portanto a partir de agora o evento deverá ter o “código de cálculo 441 - 13º SALÁRIO CONTRATO VERDE AMARELO”.  Para a alteração do contrato de verde amarelo para tempo indeterminado durante o ano deverá ser feita a alteração do evento criado anteriormente com “código de cálculo 0 – Sem Código de Cálculo Existente” para “código de cálculo 441 - 13º SALÁRIO CONTRATO VERDE AMARELO”.  Essa alteração também deve ser feita para o evento de média. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-10046](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-10046) |
| **Documento de Referência:** | [Código de cálculo 441 - 13º SALÁRIO CONTRATO VERDE AMARELO](https://tdn.totvs.com.br/pages/viewpage.action?pageId=572516387)  [Movimento Mensal](https://tdn.totvs.com.br/display/LRM/Movimento+Mensal) |
| **Pacote:** | N/A |
