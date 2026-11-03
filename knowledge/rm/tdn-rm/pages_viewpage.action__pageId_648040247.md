---
content_hash: a362fcf0378479cba8964f1a9406715c0929a0ed3529d20675d195645d0bd4bf
fetched_at: '2026-06-29T00:11:11.526373+00:00'
page_id: '648040247'
product: rm
source: tdn-rm
title: Inserir Saldo Inicial de Conta de Eliminação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=648040247
version: 12
---

Esse processo insere o Saldo Inicial de Eliminação.

Ao fechar um Exercício Contábil, se necessário, é possível realizar a inserção do Saldo anterior das Eliminações.

**EXIBIÇÃO DO PROCESSO:**

Esse processo será exibido **uma única vez** em Coligadas que possuem Contas de Eliminação. Uma vez executado será preciso reabrir o período e encerrar novamente para correção dos valores informados.

**INFORMAÇÕES IMPORTANTES PARA A UTILIZAÇÃO:**

* Apenas são exibidas contas que possuem o campo "Eliminar valores na consolidação" marcado.
* **Atenção**, caso não deseje utilizar alguma das contas como Eliminação, basta não editá-la.
* Ao optar pela utilização deve-se preencher os campos: "Coligada de Eliminação",  "Conta de Eliminação" e "Valor de Eliminação" diretamente no Grid, quando a linha estiver pronta para a execução o campo "Status" trará uma sinalização verde e será inclusa uma nova linha para informar uma próxima coligada de contra partida.

* No campo "Valor de Eliminação" o valor inserido deverá ser diferente de zero e menor ou igual ao valor de referência.
* Não é permitido alterar um valor inserido, caso haja alguma correção exclua a linha inserida incorretamente e crie novamente.

**APÓS A UTILIZAÇÃO:**

* O registro original terá seu valor modificado para a diferença entre  "Valor" e "Valor de Eliminação" e será criado um novo registro idêntico ao original, contendo no campo "Valor" o "Valor de Eliminação" e com os campos "Coligada de Eliminação", "Conta de Eliminação" e "Coligada Conta de Eliminação" preenchidos.
* Para Coligadas que possuem multimoeda os valores atualizados e inseridos terão como referência a cotação do valor original.

Exemplo: Digamos que o dólar seja a segunda moeda utilizada pela coligada. Se o campo "Valor", do registro original, for R$100,00 e o "Valor Eliminado" for R$20,00, qual será o valor em dólar para o campo "Valor Eliminado"? Neste caso iremos resgatar, na tabela de multimoeda, o valor em dólar correspondente aos R$100,00. Se ele for equivalente a US$25,00 iremos realizar a seguinte conta, 25,00 / 100,00 = 0,25. Esse valor corresponde a cotação. Para encontrar o valor em dólar iremos multiplicar o campo "Valor Eliminado" em reais pela cotação (20,00 \* 0,25 = US$5,00). Na linha correspondente ao valor restante (R$80,00), o valor atualizado em dólar será de US$20,00, totalizando os US$25,00 originais.
