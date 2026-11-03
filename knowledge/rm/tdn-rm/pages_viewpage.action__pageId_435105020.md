---
content_hash: b4ea5c2057a408bf548da36a0c21ef8a83c2e1dfcf157489381ce8da96b9c556
fetched_at: '2026-06-29T00:09:47.590585+00:00'
page_id: '435105020'
product: rm
source: tdn-rm
title: Dados Reajuste - Exemplo - Resíduo Contrato de Locação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105020
version: 5
---

# **Cálculo do Resíduo em Contrato de Locação com Reajuste Pro-Rata**

---

O valor do resíduo é a diferença do valor que foi cobrado no lançamento com vencimento no mês de reajuste anual e o valor reajustado pro-rata dia do mesmo lançamento.

* Caso o valor do resíduo seja zero, o valor da parcela em questão poderá ser reajustado e não existirá resíduo a ser cobrado para a próxima parcela.
* Caso o valor seja maior que zero, e por algum motivo a parcela não pode ser alterada (baixada, remetida a banco, etc.) o resíduo será cobrado na próxima parcela.

# **Cálculo de Resíduo em Contrato de Locação sem Reajuste Pro-Rata**

---

É necessário a geração de resíduo sempre que o reajuste não for aplicado às parcelas do Contrato de Locação, seja, ou por falta de cadastro de índice, ou por esquecimento, ou pelos lançamentos financeiros estarem remetidos a banco, ou pagos.  
Enfim, situações que não permitem a regeração dos lançamentos reajustados.

# **Comportamento do sistema caso ocorra a incidência de resíduo em um período de reajuste**

---

O reajuste tentará regerar os lançamentos financeiros afetados: Neste caso se os lançamentos financeiros estiverem quitados ou remetidos a banco, não será possível atualizar os valores destas parcelas e o sistema irá discriminar o valor de resíduo para estas parcelas.  
O valor de resíduo das parcelas na situação acima serão somados ao valor atualizado da próxima parcela passível de regeração.

Importante!A geração de resíduo para as parcelas dos Contratos de Locação não está condicionada ao cálculo Pro-Rata dia, ou seja, mesmo que a aplicação do reajuste seja feita em mês cheio, se a parcela correspondente a competência reajustada não permitir alteração (regerar) o sistema irá gerar o resíduo para a cobrança na próxima parcela.

**Veja Também**

---
