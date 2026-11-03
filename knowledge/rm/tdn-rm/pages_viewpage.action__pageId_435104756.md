---
content_hash: 6cae5bea991c4c44d93647491311767dcc2cac943e6b71cc824756fb97bc913a
fetched_at: '2026-06-29T00:09:46.030653+00:00'
page_id: '435104756'
product: rm
source: tdn-rm
title: Totvs Incorporação - Parâmetros - Integração Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104756
version: 5
---

Nesta opção temos os parâmetros da Integração Contábil no sistema. São eles:

* **Prioridade de data padrão de contabilização da venda:** Defina a ordem de prioridade que o sistema seguirá para realizar a contabilização da venda, marcando as opções e organizando-as na desejada, através das setas na lateral direita deste agrupador. Se nenhuma data padrão for selecionada, será utilizada a data da venda como data padrão para contabilização.
  + **Usar Data Inclusão da venda como data padrão para contabilização;**
  + **Usar Data Base da venda como data padrão para contabilização;**
  + **Usar Data de Assinatura do contrato como data padrão para contabilização;**
* **Usar contabilização assíncrona na venda (offline):** Marque esta opção para que a a contabilização nas vendas (efetivação de contratos de venda, aditivos, reajustes, seguros, etc.) possa ser realizada posteriormente à execução das ações que geram contabilização, ou seja, de forma não sincronizada com a execução destas ações, podendo obter um ganho de performance neste processos, uma vez que os mesmos serão finalizados independentemente da conclusão do processo de contabilização.
  + **Estornar a contabilização do reajuste automaticamente na contabilização assíncrona:** Idem a explicação acima, porém para o estorno da contabilização de reajuste;
  + **Estornar a contabilização do seguro automaticamente na contabilização assíncrona:** Idem explicações acima, porém para o estorno da contabilização do seguro;
* **Utilizar o período contábil para calcular os valores de curto e longo prazo:** Marque esta opção para que os valores calculados para a contabilização a curto e a longo prazo seja realizada automaticamente com base no período contábil definido no módulo Contábil;. Caso deseje utilizar um período diferente, preencha os campos logo abaixo, informando a quantidade de meses:
  + **Período limite curto prazo (Em meses);**
  + **Período de apuração da transferência (Em meses).**
* **Inverter a conta contábil do aditivo caso o valor seja negativo:** Marque esta opção caso deseje que o sistema realize automaticamente a inversão da conta contábil dos aditivos, caso o valor de algum deles seja negativo;
* **Usar vencimento da parcela para cálculo da data de emissão do lançamento (Somente Aluguel):** Com este parâmetro marcado, o sistema irá calcular a data de emissão das parcelas sendo o ultimo dia do mês anterior ao vencimento de cada parcela. Este processo somente será executado se o contrato for de Aluguel, o parâmetro acima estiver marcado, e o componente gerador de parcelas tenha o seu Tipo de Parcela configurado o parâmetro Efeito Financeiro = Efeito Contábil.

Os parâmetros abaixo foram descontinuados nas versões mais atuais:

* **Utiliza campo classificação no evento contábil:** Ao marcar, o sistema irá utilizar o campo classificação das conta contábeis.
* **Excluir contas contábeis zeradas:** Ao marcar, o sistema irá excluir as contas contábeis que estão zeradas.
* **Manter Filial, Percentual e Históricos – Cadastrados no item do Evento Contábil:** Ao marcar, o sistema irá manter Filial, Percentual e Históricos que foram cadastrados no item do Evento Contábil.

[Voltar](http://tdn.totvs.com/pages/viewpage.action?pageId=435105436)
