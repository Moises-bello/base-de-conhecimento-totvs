---
content_hash: 841e27753687c34ce6ffe48223e94dd1e20a92cec64c4cceddfd15e891c67c8f
fetched_at: '2026-06-29T00:09:26.775559+00:00'
page_id: '423938421'
product: rm
source: tdn-rm
title: Avaliação Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938421
version: 3
---

O Totvs Gestão Patrimonial possibilita ao usuário realizar, através do menu Operações Patrimoniais, a avaliação patrimonial dos ativos. O objetivo da Avaliação Patrimonial de acordo com as normas internacionais de contabilidade, é garantir que a troca ou liquidação de um Ativo Imobilizado ocorra em condições justas de valor de mercado. É realizada uma análise técnica para identificar o valor do patrimônio, levando em consideração fatores como custos, direitos e utilização econômica para finalidade, na situação e data. Ou seja, este processo também chamado de Deemed Cost (Custo Atribuído), é utilizado quando for identificado que o valor contábil do ativo se encontra visivelmente inferior ou superior ao valor de mercado. Um desajuste de valor que pode comprometer o balanço patrimonial e resultado das entidades.

Através desse processo, o Totvs Gestão Patrimonial permite realizar a avaliação alterando o Valor de Mercado, a Vida Útil restante em meses do patrimônio e/ou Taxa de Depreciação Mensal. Essas informações serão apresentadas após inserir o cenário de cálculo para qual a avaliação será realizada.

**Valor de Mercado/ Valor da Avaliação**

É o valor pelo qual o patrimônio poderá ser negociado entre as partes interessadas. Não é um valor de venda, não é um valor de compra, é um valor que após analise foi considerado justo, verdadeiro e ideal para o patrimônio. Marcando a opção "Inserir valores absolutos de avaliação" é possível informar nesse campo apenas o valor da avaliação**.**

Exemplo

Patrimônio com valor contábil de R$ 18.000,00, após avaliação foi definido que seu valor de mercado é R$ 22.300,00. Nesse contexto, esse patrimônio teve uma avaliação positiva de R$ 4.300,00. Marcando "Inserir valores absolutos de avaliação" o usuário deverá informar R$ 4.300,00 (Valor da Avaliação) ou desmarcando, deverá informar o valor justo (Valor de Mercado) R$ 22.300,00.

**Vida útil restante em meses**

A avaliação poderá ser realizada alterando também a vida útil restante do patrimônio. Deve ser informado o tempo em meses que a entidade espera utilizar economicamente o ativo. Alterando essa informação, a taxa de depreciação do cenário principal irá aumentar ou reduzir e uma nova taxa será criada para o cenário avaliado, permitindo que eles terminem de depreciar juntos.

**Taxa de depreciação mensal**

O Processo poderá ser realizado alterando também a taxa de depreciação que o ativo sofre mensalmente. Editando essa informação, a vida útil do cenário principal irá aumentar ou reduzir e uma nova taxa será criada para o cenário avaliado, permitindo que eles terminem de depreciar juntos.

Além do cenário de cálculo e valores, é necessário informar a data da avaliação. Essa data deverá estar inserida no período de cálculo, pois o sistema irá gerar uma ocorrência para essa data, que poderá ser contabilizada marcando o flag "contabilizar".

A contabilização será baseada em eventos contábeis de avaliação, que deverão ser criados no cadastro de evento e vinculados ao Grupo de Patrimônio/Cenário de Cálculo.

OBSERVAÇÃO: Contabilizações de ocorrências como Baixa, Acréscimo, Transferência de controle em patrimônios avaliados, o sistema irá aplicar o evento contábil especifico para esse tipo de patrimônio. Portanto, para correta execução dessas ocorrências, estes eventos também deverão ser parametrizados no grupo de patrimônio.

Os dados do laudo da Avaliação também são de preenchimento obrigatório. Deverão ser informados no processo o número, data e o responsável pela a Avaliação Patrimonial. O usuário poderá acrescentar observações complementares.

Após a execução da avaliação patrimonial, é possível verifica-las nas consultas de ocorrências, no menu Operações Patrimoniais ou até mesmo por dentro do cadastro de patrimônios dos ativos envolvidos na avaliação. É possível, também nestas consultas, excluir a avaliação patrimonial e também contabilizá-la posteriormente a sua execução.

Os relatórios do sistema desenvolvidos pela TOTVS já estão preparados para exibir informações de avaliação patrimonial, sendo possível compor saldos de grupos de patrimônios e grupos de contas com este tipo de operação patrimonial.

Informações complementares

* [Parecer Consultoria Tributária Segmentos](http://tdn.totvs.com.br/pages/releaseview.action?pageId=173082551)
Veja também

* Cálculo Detalhado da Avaliação Patrimonial
* Ajustes Eventos Contábeis de Avaliação
* Importar Avaliação Patrimonial
