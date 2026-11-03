---
content_hash: 680b90688d89728e0428fb55cff207244a24ef69405fa081c58d8f4dcb6d1b3a
fetched_at: '2026-06-29T00:09:19.488354+00:00'
page_id: '422545598'
product: rm
source: tdn-rm
title: Período de Apuração (Informações Adicionais)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545598
version: 3
---

O cadastro do Período de Apuração é composto das seguintes abas:

**Apuração**

Nesta pasta o usuário terá as informações de:

* Saldo anterior do tributo
* Saldo credor/Devedor
* Saldo original
* Data de vencimento
* Crédito outorgado

***Observações:***O sistema calculará o Crédito Outorgado referente aos serviços de Transporte automaticamente durante o encerramento dos períodos. O cálculo será efetuado aplicando o percentual definido no Cadastro de Filiais - Anexos | Dados Fiscais | Tributos, sobre o saldo do débito do período, ou seja, do somatório do valor informado no campo Valor de ICMS do Lançamento Fiscal. Serão considerados para esta totalização apenas os Lançamentos Fiscais de Saída associados aos códigos de Naturezas de Operação dos grupos 5.35X e 6.35X.  
 Somente serão considerados Lançamentos Fiscais de Saída associados às Naturezas Fiscais.  
 Lançamentos Fiscais Estornados e/ou Cancelados não serão selecionados para este cálculo.

* Débito Extemporâneo
* Total ICMS D.A (Diferencial de alíquota) Entrada

***Observação*:**O sistema calculará o valor do ICMS diferencial de alíquota referentes às Operações Interestaduais de Compra para o Ativo Imobilizado / Uso e Consumo em que a alíquota do Estado Origem é inferior a alíquota do Estado destino da mercadoria.

***Atenção!***Não será permitido incluir guias manuais ou automáticas caso o campo Data Vencimento não esteja preenchido.

**Detalhamento**

Essa pasta é habilitada para os impostos do Tipo IRPJ, CSLL, PIS, COFINS, OUTROS E RET.  
  
***Observação:***

* Para calcular o Débito/Crédito do TRIBUTO em um determinado Período de Apuração, basta selecionar o Período de Apuração associado a este tributo e escolher a opção Encerrar Período**.** Nesse momento os campos, serão preenchidos com valores, de acordo com as informações do evento tributário vinculado a estes tributos.

* O Campo Alíquota de Apuração será preenchido com o valor do campo Alíquota, do Cadastro de Tributos, bem como os campos Alíquota Adicional, Valor Parcela Isenta, %Serviços, %Vendas e % de Compensação.
* Será calculado o saldo do imposto considerando o Saldo do Tributo no Período anterior, a alíquota do Imposto informada na Pasta Detalhes de Apuração do Cadastro de Período e a Regra Tributária definida no Evento Tributário.
* O sistema buscará o Evento Tributário informado no Cadastro de Vigências dos Eventos Tributários. A vigência será identificada com base nas Datas Inicial e Final do Período de Apuração e o Tributo associado.
* O sistema considerará para efeito do Cálculo apenas Lançamentos Contábeis já integrados ao Lote Zero. Para a correta Apuração dos impostos, que é mensal, será necessário que a conciliação das contas contábeis no mês tenha sido realizada. - A apuração será realizada de forma consolidada, considerando todas as Filiais.
* Cada contribuinte deverá parametrizar o sistema de acordo com suas obrigações legais. Caso o contribuinte utilize o regime do Lucro Real anual, poderá realizar antecipações utilizando o Regime de Estimativa ou o Regime do Lucro Real.
* Ao encerrar o Período de Apuração o sistema precisa identificar qual a regra deve ser utilizada para o cálculo do imposto. Não pode existir mais de uma regra para o mesmo Período de Apuração.
* Ao apurar o IRPJ e CSLL devido, se o cálculo está definido como acumulativo e não tiver ocorrido cisão, o sistema considerada a movimentação contábil desde 01/01 do ano que se está apurado.
* Se tiver ocorrido cisão, o sistema seleciona as cisões ocorridas no ano que se está apurando o imposto e que ocorreram até o mês anterior ao que se está apurando, neste caso, irá considerar como data para cálculo do imposto o dia seguinte à última da cisão ocorrida na empresa e que atende a regra do passo anterior. Para isso na parametrização da regra de apuração do IRPJ e CSLL o usuário deverá definir as cisões ocorridas. Caso possua Filial SCP deve ser informado no Cadastro da Cisão (Campo: "Filial da Ocorrência") a Filial de Ocorrência da Cisão para que a mesma não seja considerada também para a Filial SCP.
* Para os tributos apurados como "Outros Tributos e RET", também poderão ser apurados via Eventos Tributários.
* Para estes Tributos, cujo Tipo do Tributo é "Outros", o sistema irá disponibilizar a Forma de Tributação Outros. Para esta Forma de Tributação serão apresentados no cadastro de Evento Tributário os SubGrupos "Receitas e Exclusões". - Para a Apuração destes Tributos o Sistema irá subtrair das Receitas as Exclusões e aplicar a alíquota informada no cadastro de Período de Apuração.
