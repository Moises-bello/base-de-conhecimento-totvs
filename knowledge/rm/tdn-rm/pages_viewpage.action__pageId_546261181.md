---
content_hash: 76bc26c0ed27e47eb6a037ecb181c2cdc398ed4df931a593960fbfaee37c2c93
fetched_at: '2026-06-29T00:10:41.645716+00:00'
page_id: '546261181'
product: rm
source: tdn-rm
title: Reajuste Revitalizado / Condição de Financiamento da Venda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546261181
version: 8
---

No cadastro de condição de financiamento assim como no cadastro de modalidade foram criados três novos campos de fórmula que permitem ao usuário definir formas alternativas de cálculo dos componentes de CM (Correção Monetária) e Juros de Contrato para as variáveis de taxa ou índice de reajuste, base de cálculo de reajuste e se o componente de CM ou Juros devem ser calculados.

1. ## **Fórmula de Validação para executar o reajuste:**

   1. Esta fórmula deve retornar verdadeiro ou falso de acordo com o que o usuário definir como condição de execução do cálculo de reajuste do componente, por exemplo, só deve reajustar se a data de reajuste for menor que a data X.
2. ## **Fórmula para definir um novo valor de índice/taxa no reajuste:**

   1. Esta fórmula permite ao usuário definir qual o índice de reajuste em função da condição determinada na fórmula podendo interferir no valor do índice calculado pelo sistema.
3. ## **Fórmula para definir um novo valor na base de cálculo do reajuste:**

   1. Esta fórmula permite que o usuário defina uma base de cálculo diferente da configurada no componente de CM ou Juros para cálculo do valor do reajuste.

Com todos estes pontos de interferência no cálculo do componente de CM e Juros o usuário pode personalizar o cálculo dos componentes como desejar.

Além disso nos processos de cópia de grupo e cópia de modalidade estes três novos campos são copiados para os componentes de Juros e Correção Monetária.

### Observação: Todo o histórico de cálculo da fórmula é gravado no log da parcela.

Nova tela do componente de CM e Juros no cadastro de condição de financiamento da venda.

Componente de Juros no cadastro de condição de financiamento da venda

Componente de CM no cadastro de condição de financiamento da venda

Importante!

Verifique [**aqui**](https://tdn.totvs.com/pages/viewpage.action?pageId=435105184)como parametrizar corretamente o componente de correção monetária, na Modalidade e nas Condições de Financiamento da venda
