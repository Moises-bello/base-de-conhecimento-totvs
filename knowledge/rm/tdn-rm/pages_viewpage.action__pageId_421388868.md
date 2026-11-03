---
content_hash: 67e9aaa06b834bd532f4cac2eb889b48f1a32f24a45c8fd7953933481ccbbd23
fetched_at: '2026-06-29T00:09:19.409749+00:00'
page_id: '421388868'
product: rm
source: tdn-rm
title: Cálculo de Juros e Multa no lançamento de INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388868
version: 4
---

O cálculo de Juros e Multa no Lançamento de Tributos do INSS consiste em atualizar o valor do Lançamento Financeiro considerando dias de vencimento no momento da Baixa.

**Atenção**

Necessário cadastrar o Índice SELIC que será utilizado para o cálculo de Juros. Disponível no Menu: Movimentações Bancárias  | Moedas  | Moedas e Índices.

Verificar nos parâmetros do Calendário Oficial se a flag: " Considerar sábado como dia útil " está habilitado. Disponível no Menu: Ambiente  | Parâmetros  | Totvs Gestão Financeira  | Contas a Pagar  | Manutenção de Lançamentos  | Calendário Oficial. Caso positivo o sistema irá considerar os valores de juros e multa ao sábados, caso não esteja habilitado os valores serão calculados no primeiro dia útil após o vencimento.

Informar nos parâmetros da Baixa disponível no Menu: Ambiente | Parâmetros  | Totvs Gestão Financeira  | Contas a Pagar | Baixa | IRRF / INSS.

* No campo Taxa Selic: ( Informar a cotação já cadastrada com os índices e seus respectivos valores);
* No campo : % Multa por Dia ( Informar o valor de 0,33%);
* No parâmetro: % Máximo Multa por Dia ( Informar o percentual máximo que poderá ser cobrado de multa.

**Cálculo de Juros de INSS**

Utilizando taxa SELIC - Cálculo utilizado à data 03/12/2008

Suponha-se que o vencimento do Lançamento é no mês de Janeiro de 2008; para Lançamentos Financeiros que geraram INSS os vencimentos que possuem:   
    
   
    
 **Cálculo de Multa de INSS**

Cálculo utilizado à data 03/12/2008  
    
   
 Cálculo utilizando taxa SELIC - **Medida Provisória 449 de 03 de dezembro de 2008**.   
    
   
   
 **Observação**

Soma da SELIC é o percentual (%) da SELIC do mês que é calculado a partir do valor do lançamento gerado.   
 Exemplo: Suponha-se que o valor do INSS é R$ 400,00 e a SELIC do mês é 1,5. O cálculo ficaria da seguinte forma:

* INSS R$ 400,00 / 1,5 = R$ 6,00 (Valor da SELIC no mês)

Para cálculo de Multa de INSS - Medida Provisória 449 de 03 de Dezembro de 2008

* Calculada à taxa de 0,33% (trinta e três centésimos por cento), por dia de atraso.
* A multa será calculada a partir do primeiro dia subsequente ao do vencimento do prazo previsto para o pagamento do tributo ou da contribuição até o dia em que ocorrer seu pagamento.
* O percentual da multa a ser aplicado fica limitado a 20% (vinte por cento) caso houver 60 dias de atraso.
