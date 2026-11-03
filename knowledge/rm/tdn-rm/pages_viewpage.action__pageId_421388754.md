---
content_hash: 9537c0121faa4bb4879d6d9c79c2f7f50d278edd3c66072b7897a6f261789784
fetched_at: '2026-06-29T00:09:18.697532+00:00'
page_id: '421388754'
product: rm
source: tdn-rm
title: Composição do Valor líquido Hoje
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388754
version: 4
---

Para facilitar a visualização dos valores que compõe o valor liquido, os dados desse anexo estarão contidos dentro de uma grid, onde cada linha conterá os dados de determinado valor, apresentados pelas colunas: Descrição, Grupo, Valor Original, Valor Baixado e Valor Saldo.  
A coluna Grupo, indica a descrição do tipo do campo que compõe ou não o valor liquido:

**Valores que compõem o Valor Líquido:**

* Valor Original,
* Valor Indexado,
* Juros,
* Multa,
* Desconto,
* Capitalização
* Valores Opcionais que compõem o valor. (De acordo com o Parâmetro Ação como "Descontar" ou "Acrescentar").
* Valores Opcionais que não compõem o Valor Líquido. (De acordo com parâmetro Ação como "Nada").
* Valores de Integração.
* Valor Líquido que contém o valor corrente.

Este anexo se encontra em Contas a Pagar/Receber| Lançamentos|Anexo|Composição do Valor Líquido.

O "Valor Original" busca o valor corrente do lançamento para os dois primeiros grupos acima e dos valores de integração correntes para o terceiro grupo. A exceção a essa regra é o campo Valor Indexado, cujo valor será obtido através de um serviço que toma como entrada valores do lançamento (Valor Original, Indexador, Moeda, Data de Emissão) com data de referência a corrente.

O "Valor Baixado" é composto a partir do somatório do valor dos itens de baixa de status "Baixado", "Cheque", "Remetido" e "Borderô", para os dois primeiros grupos e dos valores de integração baixados no terceiro.  
Já o "Valor Saldo" é obtido através do serviço de cálculo do valor líquido do lançamento que já exibe os saldos restantes para os três primeiros grupos acima. Esse serviço também exibe o valor atual na data corrente, do campo do grupo "Valor Líquido" que diferente dos anteriores, este tem valor único.

Os seguintes campos, quando o valor original, baixado e saldo estão zerados, não são exibidos: Valor IRRF, Valor INSS, Valor SEST/SENAT, Juros Vendor, Valor Devolução, Valor Adiantamento, Valor Nota Crédito. A exibição dos Valores de Integração depende da parametrização do sistema e de sua definição.
