---
content_hash: 89d9af0d0808b70aef8d6e576ac62631aba483afcddb94803cf8b336faa41c56
fetched_at: '2026-06-29T00:09:17.002936+00:00'
page_id: '421388549'
product: rm
source: tdn-rm
title: Ajustar Valores do Crédito de Adiantamento para Vínculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388549
version: 4
---

Na baixa do lançamento de adiantamento com retenção, o sistema gerava o lançamento de crédito de adiantamento com o valor original constituído pela soma do valor líquido mais o valor das retenções do lançamento de adiantamento.

A partir da versão 12.1.13, o valor original do lançamento de crédito de adiantamento, gerado pela baixa do lançamento de adiantamento com retenção, será composto somente pelo valor líquido do lançamento de adiantamento.  
 Desta forma, este processo tem como objetivo, percorrer todos os lançamentos de crédito de adiantamento gerados pela baixa do lançamento de adiantamento com retenção, para ajustar o seu valor original e consequentemente o seu valor vinculado, caso o lançamento esteja vinculado.

O processo está localizado em Utilitários/Ajustes na Base/Ajustar Valores do Crédito de Adiantamento para Vínculo  
 Será necessário dar permissão ao usuário/perfil que irá utilizar o processo.

**Processamento**

**Os valores que serão ajustados são:**

* Valor Original Lançamento de crédito de adiantamento.
* Valor do Vínculo Entre o vínculo do lançamento do crédito de adiantamento com o lançamento de adiantamento.
* Valor do Vínculo Entre o vínculo do lançamento do crédito de adiantamento com o lançamento de nota fiscal.
* Valor da Retenção Vinculada Entre o vínculo do lançamento do crédito de adiantamento com o lançamento de nota fiscal.
* Valor Vinculado Lançamento de crédito de adiantamento.
* Valor Original Item de baixa do lançamento de crédito de adiantamento.
* Valor Vinculado Item de baixa do lançamento de crédito de adiantamento.

**Cálculos para obter os novos valores para o ajuste**

Novo valor original lançamento de crédito de adiantamento

É o valor resultante da subtração entre o valor do vínculo antigo, entre o lançamento de crédito de adiantamento com o lançamento de adiantamento, menos o valor da retenção paga na baixa do lançamento de adiantamento.

Novo valor do vínculo entre o vínculo do lançamento do crédito de adiantamento com o lançamento de adiantamento

É o valor resultante da subtração entre o valor do vínculo antigo, entre o lançamento de crédito de adiantamento com o lançamento de adiantamento, menos o valor da retenção paga na baixa do lançamento de adiantamento.

Novo valor do vínculo entre o vínculo do lançamento do crédito de adiantamento com o lançamento de nota fiscal

É o valor resultante pelo cálculo: "Novo valor do vínculo entre o vínculo do lançamento de crédito de adiantamento com o lançamento de adiantamento" multiplicado pela divisão entre "Valor do vínculo antigo entre o vínculo do lançamento de crédito de adiantamento com o lançamento de nota fiscal" pelo "Valor do vínculo antigo entre o vínculo do lançamento de crédito de adiantamento com o lançamento de adiantamento".

Valor da Retenção Vinculada entre o vínculo do lançamento do crédito de adiantamento com o lançamento de nota fiscal

É o valor resultante da subtração entre o "valor do vínculo antigo entre o vínculo do lançamento de crédito de adiantamento com o lançamento de nota fiscal" menos o "Novo valor do vínculo entre o vínculo do lançamento de crédito de adiantamento com o lançamento de nota fiscal".

Valor Vinculado do lançamento de crédito de adiantamento

É o valor resultante do somatório dos "Novos valores do vínculo entre o vínculo do lançamento de crédito de adiantamento com o lançamento de nota fiscal".

Valor Original do item de baixa do lançamento de crédito de adiantamento

É o "Novo valor do vínculo entre o vínculo do lançamento de crédito de adiantamento com o lançamento de nota fiscal".

Valor Vinculado do Item de baixa do lançamento de crédito de adiantamento

É o "Novo valor do vínculo entre o vínculo do lançamento de crédito de adiantamento com o lançamento de nota fiscal"

**Resultados do processo**

Atualiza nos lançamentos a seguinte informação: Valor Original; Valor Vinculado; Valor Origina Baixado.

Atualiza no vínculo dos lançamentos a seguinte informação: Valor do Vínculo; Valor da Retenção Vinculada.

Atualiza nos itens de baixa dos lançamentos a seguinte informação: Valor Original; Valor Vinculado.

Atualiza os logs dos valores dos lançamentos a seguinte informação: Valor Original.

**Principais tabelas afetadas pelo processo**

FLANFRELLANFLANBAIXAFLOGVALORES
