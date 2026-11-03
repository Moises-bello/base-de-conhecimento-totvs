---
content_hash: 69598bdea25a25d05b95dcd9cc9a6cbaf01f14a4b9d1668c364315d392469fc9
fetched_at: '2026-06-29T00:10:19.445233+00:00'
page_id: '4813679'
product: rm
source: tdn-rm
title: Saldo Negativo na Ficha
type: documentation
url: https://tdn.totvs.com/display/LRM/Saldo+Negativo+na+Ficha
version: 5
---

BLOCK

Saldo Negativo na Ficha

FAQ: **Saldo Negativo na Ficha**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 10.70 |

Sintoma

* **Sintoma**

Seu Estoque está ficando negativo no relatório de ‘Ficha Física Financeira’, mesmo parametrizado para “Barrar Saldo Menor que Zero”?

Causa

* **Causas**

1. Um tipo de movimento de saída estava parametrizado com “Efeito sobre o Saldo Físico” igual a Não Altera ou Aumenta. Em seguida percebeu-se que a parametrização estava incorreta e o “Efeito sobre o Saldo Físico” foi alterado para Diminuir. Na sequencia foi executado o processo de ‘Regeração de Saldos e Custo’ ou somente a ‘Regeração da Ficha Física-Financeira’, onde as informações do estoque são recalculadas considerando a parametrização atual de todos os tipos de movimentos.

2. Foram incluídas movimentações que afetam o estoque com data retroativa à data atual. No momento da inclusão de um movimento o saldo considerado para validação do estoque, é o ‘Saldo on line’ do produto, que não leva em consideração a data retroativa dos movimentos. Na sequencia foi executado o processo de ‘Regeração de Saldos e Custo’ ou somente a ‘Regeração da Ficha Física-Financeira’, onde as informações do estoque são recalculadas e ordenadas considerando o parâmetro “Ordem dos movimentos ao regerar Ficha Ficha-Financeira” que deve estar habilitada com a opção Ordem de inclusão/alteração do movimento.

Solução

* **Solução**

Analisar a movimentação do produto que está com saldo negativo, utilizando o relatório de Ficha Física-Financeira e providenciar o ajuste, considerando a melhor alternativa dentro das estratégias de gestão do estoque da empresa:

* Ajustar a parametrização do tipo de movimento ou,
* Ajustar a data de movimentação do estoque do movimento que provocou o saldo negativo ou,
* Incluir movimentação de ajuste positivo de estoque.

Em seguida:

* Executar processo de ‘Regeração de Saldos e Custo’ ou somente ‘Regeração da Ficha Física-Financeira’;

Emitir relatório de Ficha Física-Financeira e validar as informações.

* **Informações Adicionais**

O processo de ‘Regeração de Saldos e Custos’ não faz validação do Parâmetro “Barrar Saldo Menor que Zero”.

Observações

O documento em questão está postado no blog da Totvs e pode ser consultado através do link : <http://totvsconnect.blogspot.com/2010/10/dica-saldo-negativo-na-ficha-rm-nucleus.html>
