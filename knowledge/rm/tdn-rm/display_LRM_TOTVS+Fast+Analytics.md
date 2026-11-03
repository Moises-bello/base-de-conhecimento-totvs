---
content_hash: b97244cb1d4743ca90649d382cbedec1ac84bb406c9f38ecf154484b303e3c5c
fetched_at: '2026-06-29T00:08:55.355756+00:00'
page_id: '348297004'
product: rm
source: tdn-rm
title: TOTVS Fast Analytics
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Fast+Analytics
version: 388
---

Objetivo 

Apresentar todas as Dimensões e Fatos do TOTVS Fast Analytics com o mapeamento dos campos utilizados nas consultas.

### Definição da Regra de Negócio

O Fast Analytics provê uma maior agilidade na construção de consultas que tem com o objetivo a extração de dados para a utilização no GoodData.

Conceitos importantes de **Business Intelligence (BI):Provento e Descontos do Envelope de Pagamento**

* **Dimensão:** Possui característica descritiva. Qualifica as informações provenientes da tabela Fato. Através dela é possível analisar os dados sob múltiplas perspectivas. São exemplos de Dimensões: Projeto, Tarefa e Conta Contábil.
* **Fato:** Possui característica quantitativa. A partir dela são extraídas as métricas que são cruzadas com os dados das Dimensões, concebendo, assim, informações significativas para a análise do usuário. A Fato armazena as medições necessárias para avaliar o assunto pretendido.

 Abaixo algumas Dimensões e Fatos necessários para a extração de dados da base da linha RM:

TabControlUnificadosUnificadosUnificados

### Dimensões:

* Coligada:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| DESCRICAO | Descrição da Coligada |

* Filial:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| CODFILIAL | Identificador da Filial |
| NOMEFANTASIA | Nome Fantasia da Filial |

* Moeda:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| SIMBOLO | Código da Moeda |
| DESCRICAO | Descrição da Moeda |

* Natureza Orçamentária:

1558547731324\_-1503670817

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| CODTBORCAMENTO | Código da Natureza Orçamentária/Financeira |
| DESCRICAO | Descrição da Natureza Orçamentária/Financeira |

* Centro de Custo:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCCUSTO | Identificador do Centro de Custo |
| NOME | Nome do Centro de Custo |

* Conta Contábil:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| CODCONTA | Identificador da Conta Contábil |
| DESCRICAO | Descrição da Conta Contábil |

Inc1IncorporaçãoIncorporação

**Fast Analytics Incorporação**

Deck 1Inc1IndicadoresIndicadores

Os indicadores desenvolvidos pelo TIN estão descritos abaixo:

Abas indicadoresInc5Painel de IndicadoresPainel de Indicadores

Painel de Indicadores do Fast Analytics TIN

Este dashboard permite visualizar os indicadores de desempenho da Incorporadora, permitindo verificar a receita do período, unidades vendidas, imóveis distratados e o valor gasto na devolução. Além disso é possível ver através dos indicadores o estoque de subunidades disponíveis e os indicadores financeiros.

Os indicadores são mostrados através dos seguintes filtros:

* Data
* Coligada
* Empreendimento

Os paineis podem mostrar valores maiores que 1000, para isso será utilizada a seguinte legenda para contabilização dos valores:

Além disso, a parte superior de cada indicador mostra se o resultado é positivo ou negativo, de acordo com as cores. Caso verde é um indicador positivo e vermelho um indicador Negativo ou ponto de atenção.

Neste Painel, ao clicar em um dos valores/ percentuais apresentados, o sistema demonstrará o detalhamento do mesmo. Este detalhamento será apresentado em forma de Tabela, podendo o usuário visualiza-lo também em formato de gráfico (Linha, Barras ou Pizza).

**INDICADORES DE VENDAS**

* **Valor de Venda:** Dados os filtros acima, será calculado qual o valor somado de todas as vendas no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todas as coligadas com o Valor vendido, a quantidade de imóveis vendidos, valor de distrato e quantidade de imóveis distratados.

* **Função:**Lista as funções.

* **Imóveis vendidos:** Este indicador mostra a quantidade de imóveis vendidos no período selecionado.

* **Valor do Distrato:** É feito um somatório de todo o valor que foi devolvido no período através de distratos.

* **Imóveis distratados:** Representa a quantidade de imóveis distratados no período. Lembrete: Também é mostrado a diferença percentual do período anterior ao selecionado e do mesmo período do ano anterior.

* **Percentual de Distrato:** Este indicador mostra o percentual de distrato que houve no período em relação ao número de vendas.

**INDICADORES DE DISPONIBILIDADE**

Os indicadores de disponibilidade estão associados às subunidades que ainda não foram vendidas. Cada indicador mostra o valor total de todas as coligadas.Em outra aba é possível ver o detalhamento da disponibilidade de cada empreendimento ou coligada.

É possível ver a quantidade de imóveis disponíveis, o valor nominal (da tabela de preço) de todos esses imóveis, e a velocidade de venda que é uma previsão que utiliza a média de vendas mensais de subunidades, por exemplo:

Caso o valor de venda disponível seja R$ 1.000.000,00 (Um milhão) e por mês a incorporadora vende em média R$ 100.000,00 (Cem mil). Assim a velocidade de venda para chegar à Um milhão é de 10 meses.

**INDICADORES FINANCEIROS**

Este painel de indicadores financeiros demonstram a saúde financeira da Incorporadora. Serão visualizados os valores recebidos e à receber dos financiamentos e também o percentual de inadimplência, conforme imagem abaixo:

A comparação entre períodos mostra a evolução do recebimento financeiro e pode indicar estratégias para melhorar o índice de recebimento e diminuir inadimplência. Cada indicador tem o seu detalhamento que pode chegar no nível de subunidade. Foi criada uma aba somente com gráficos e termômetros financeiros com o intuito de ter uma análise financeira mais detalhada. Veja a aba **"Recebimentos Financeiros"**.

Inc6VendasVendas

A Aba de Vendas possui os seguinte filtros:

* Data
* Coligada
* Estado
* Município
* Empreendimento
* Vendedor

Este dashboard possui os seguintes gráficos:

* **Evolução do valor de venda do período**

As barras representam o valor (em milhões) das vendas no mês. O mês central é o mês selecionado e sempre será mostrado o mês anterior e o posterior. A linha representa a quantidade de imóveis (subunidades) vendidos naquele mês. É mostrado também as médias dos valores de venda por mês e de quantidade de subunidades vendidas.

* **Evolução do distrato do Período**

Assim como a venda, temos os mesmos indicadores para a evolução do distrato, o valor devolvido e a quantidade de subunidades distratadas.

* **Termômetro de Vendas/Distrato**

Este conjunto de painéis mostram um termômetro com a relação de vendas e distratos no período, quanto maior o número de vendas em relação à distratos, maior a saúde financeira da incorporadora. À direita são mostrados os 5 motivos que mais ocorreram de distrato.

* **Distribuição do valor de vendas nos estados brasileiros**

O mapa acima mostra onde estão acontecendo as vendas da Incorporadora, podendo ser visualizadas por estado ou por cidades. No lado esquerdo é mostrado um descritivo por Regiões do Brasil. É mostrado o valor dos imóveis vendidos e a quantidade.

* **Ranking de Vendas e Distratos por Empreendimento**

Este ranking mostra por empreendimento, qual vendeu mais e qual teve mais distratos, além disso o quanto isso representa em (%) de todas as vendas e todos os distratos.

* **Ranking de Vendedores**

O Ranking mostra os Top 10 Vendedores da Incorporadora, a barra mostra o valor R$ de suas vendas e a linha mostra o valor percentual em relação a tudo que foi vendido.

* **Distribuição do valor de Venda por Preço de Subunidade**

Este gráfico mostra quais tipos de subunidades deram maior retorno financeiro, de acordo com a faixa de preço da subunidade, no exemplo acima as subunidades que tem preço menor que R$ 500.000,00 tiveram uma receita maior que as outras faixas de preço.

Inc7Disponibilidade de ImóveisDisponibilidade de Imóveis

A Aba de Disponibilidade de Imóveis é responsável por mostrar a análise do Estoque de subunidades. É possível verificar detalhadamente a velocidade média de vendas, a evolução de venda. A distribuição dos imóveis e quais empreendimentos possuem mais imóveis disponíveis.

Os seguintes filtros estão disponíveis neste dashboard:

* Data
* Coligada
* Estado
* Município
* Empreendimento

Teremos os seguintes gráficos disponíveis:

* **Evolução do valor de venda dos Imóveis/Subunidades**

O gráfico de barras mostra o valor de vendas por mês selecionado no filtro data. Juntamente as linhas mostram a quantidade de subunidades vendidas por mês.

Do lado direito, temos um gráfico de barras mostrando um valor Total de todo o período selecionado e também a quantidade total de imóveis vendidos no período selecionado. Logo abaixo dos gráficos temos os valores médios por mês de vendas (R$) e subunidades vendidas.

* **Valores consolidados**

Estes são os valores consolidados da Incorporadora, no exemplo acima, são calculados os valores para toda a base de dados.

* **Distribuição dos imóveis a venda geograficamente**

O mapa acima mostra a localização por cidade ou por estado de todos os imóveis disponíveis para venda. Juntamente temos a distribuição por região e a somatória do preço das subunidades. A visualização pode ser feita tanto por cidades quanto por estado.

* **Ranking de estados com maior disponibilidade de imóveis para venda.**

O gráfico de barras demonstra por estado, o quanto de valor R$ aquele Estado pode gerar vendendo suas subunidades, de acordo com o preço cadastrado. A linha informa a quantidade de subunidades disponíveis para o Estado.

Na parte inferior do gráfico, temos a representatividade dos top 5 estados em relação a todos os estados em que a Incorporadora possui imóveis disponíveis. No exemplo acima a incorporadora possui imóveis em apenas 2 estados, sendo então 100% da representatividade.

* **Ranking de cidades com maior disponibilidade de imóveis para venda.**

Assim como o gráfico anterior, este gráfico é um ranking de Imóveis disponíveis e seu potencial de venda, porém a granularidade do gráfico são as cidades ao invés de estados.

* **Comparativo de empreendimentos com a disponibilidade de imóveis a venda, distratos e preço do imóvel**

O ranking acima representa quais empreendimentos possuem maior disponibilidade de imóveis para venda, qual valor essa disponibilidade representa de possível receita e a quantidade de distratos que houve no empreendimento. Cada empreendimento possui sua posição no ranking e o percentual que ele representa em relação a toda base de dados.

Inc8RecebimentosRecebimentos

O Dashboard da aba Recebimentos demonstra a saúde financeira da Incorporadora, trazendo informações sobre a situação dos títulos, valor recebido no período e recebimentos em atraso.

Nesta aba, temos os seguintes filtros para exibição dos dados:

* Data de Vencimento
* Coligada
* Centro de Custo
* Número da venda
* Empreendimento

Os seguintes gráficos estão disponíveis para análise:

* **Evolução dos recebimentos**

Com o gráfico acima podemos analisar mês a mês qual foi o valor recebido (em verde), o que falta a receber mas não está em atraso (em amarelo) e os recebimentos atrasados (em vermelho). As linhas demonstram a quantidade de títulos (lançamentos financeiros) que estão naquela situação e a sua evolução em relação ao tempo.

* **Distribuição dos recebimentos**

No lado direito temos os gráficos de pizza que demonstra a distribuição percentual dos lançamentos, tanto em valor quanto em quantidade de títulos. Esse valor se altera de acordo com os filtros selecionados.

* **Ranking de Empreendimentos com maior incidência de atrasos de recebimentos.**

Este ranking explicita quais os 10 empreendimentos mais tem parcelas em atraso em suas vendas, de acordo com o valor que se deve. As linhas mostram o percentual que este empreendimento representa em todo valor que está atrasado (somatório dos valores das parcelas em atraso de todos os empreendimentos). Na parte inferior do gráfico temos uma representatividade desse top 10 em relação a todos os empreendimentos da base de dados.

* **Tempo de atraso dos recebimentos**

Este gráfico demonstra quanto tempo as parcelas ficam em atraso. Cada faixa de tempo mostra qual o valor a se receber e na parte inferior do gráfico a média de tempo que as parcelas ficam em atraso.

* **Lista de títulos e seu status no período**

Esta lista demonstra todos os títulos no período escolhido e a sua situação, mostrando o ID do Lançamento, a data de vencimento, o valor e quantos dias está em atraso, ou se está no prazo. Além disso é mostrado de qual empreendimento pertence este título.

No canto inferior é mostrado um somatório do valor dos títulos mostrados.

É possível clicar no Empreendimento e ver em detalhe qual unidade e subunidade pertence este título.

Inc2DimensõesInc2

Dimensões utilizadas:

* **Vendedor\_Funcionário**

| Coluna | Descrição |
| --- | --- |
| CODCOLIGADA | Coligada do Funcionário |
| CHAPA | Código do Funcionário |
| NOME | Nome do Funcionário |

* **Vendedor\_Cliente/Comprador**

| Coluna | Descrição |
| --- | --- |
| CODCOLIGADA | Coligada do Comprador/Vendedor |
| CODCFO | Código do Comprador/Vendedor |
| NOME | Nome do Comprador/Vendedor |

* **Subunidade**

| Coluna | Descrição |
| --- | --- |
| COD\_PESS\_EMPR | Código do Empreendimento |
| NUM\_UNID | Código da Unidade/Bloco |
| NUM\_SUB\_UNID | Código da Subunidade/Apartamento |
| DESCRICAO | Descrição da Subunidade |

* **Unidade**

| Coluna | Descrição |
| --- | --- |
| COD\_PESS\_EMPR | Código do Empreendimento |
| NUM\_UNID | Código da Unidade |
| DSC\_LOCAL | Descrição da Unidade |
| QTD\_SUB\_UNID | Quantidade de Subunidades da Unidade |

* **Empreendimento**

| Coluna | Descrição |
| --- | --- |
| COD\_PESS\_EMPR | Código do Empreendimento |
| CODCOLIGADA | Código da Coligada |
| NOME | Nome do Empreendimento |
| NOMEFANTASIA | Nome Fantasia do Empreendimento |
| CNPJ | CNPJ do Empreendimento |
| QTD\_UNID | Quantidade de Unidades |
| QTD\_SUB\_UNID\_EMPR | Quantidade de Subunidades |
| SITUACAOEMPREENDIMENTO | Situação do Empreendimento |
| LOGRADOURO | Rua do Empreendimento (Endereço) |
| NUMEROEND | Número do Endereço do Empreendimento |
| COMPLEMENTOEND | Complemento do Endereço |
| BAIRRO | Bairro do Empreendimento |
| CEP | CEP da localização do Empreendimento |
| CIDADE | Cidade do Empreendimento |
| UF | Estado do Empreendimento |
| DSCTIPOEMPREENDIMENTO | Tipo de Empreendimento |
|  |  |

* **Centro de Custo**

| Coluna | Descrição |
| --- | --- |
| CODCOLIGADA | Coligada do Centro de Custo |
| NOME | Nome do Centro de Custo |
| CODCCUSTO | Código do Centro de Custo |

* **Tipo de Parcela**

| Coluna | Descrição |
| --- | --- |
| COD\_TIPO\_PARC | Código do Tipo de Parcela |
| DSC\_TIPO\_PARC | Descrição do Tipo de Parcela |

* **Situação da Venda**

| Coluna | Descrição |
| --- | --- |
| COD\_SIT\_VENDA | Código da Situação da Venda |
| DSC\_SIT\_VENDA | Descrição da Situação da Venda |

* **Distrato**

| Coluna | Descrição |
| --- | --- |
| CODTIPODISTRATO | Código do Tipo de Distrato (Unilateral/Bilateral) |
| DSCTIPODISTRATO | Descrição do Tipo de Distrato |
| CODMOTIVODISTRATO | Código do Motivo de Distrato |
| DSCMOTIVODISTRATO | Descrição do Motivo de Distrato |

Inc3FatosFatos

Para o Fast Analytics - Totvs Incorporação, temos os seguintes fatos disponíveis:

1. Ranking de Vendedores: Será possível verificar quais vendedores tiveram maior receita no período, tanto em valor de Receita quanto de Subunidades vendidas.
2. Disponibilidade ou estoque de Subunidades: Informações sobre as subunidades que podem ser vendidas e quanto de receita esse estoque pode gerar
3. Carteira: Uma análise de todo o recebimento e inadimplência no período.
4. Vendas Distratadas: Uma análise sobre os principais motivos para o distrato e o valor gasto em devolução para o cliente.

* **Vendedor**

| Coluna | Descrição |
| --- | --- |
| NUM\_VENDA | Número da venda |
| DAT\_VENDA | Data da venda |
| IDVENDEDOR | Código do Vendedor |
| COLIGADA\_VENDEDOR\_CFO | Coligada do Vendedor (Fornecedor) |
| CODIGO\_VENDEDOR\_CFO | Código do Vendedor (Fornecedor) |
| COLIGADA\_VENDEDOR\_FUNCIONARIO | Coligada do Vendedor (Funcionário) |
| CODIGO\_VENDEDOR\_FUNCIONARIO | Código do Vendedor (Funcionário) |
| VT\_TOT\_VENDA | Valor Total da Venda |

* **Estoque de Subunidades**

| Coluna | Descrição |
| --- | --- |
| INSTANCIA | Instância do Banco de Dados (RM/Protheus) |
| CODEMPREENDIMENTO | Código do Empreendimento |
| CODUNIDADE | Código da Unidade |
| CODSUBUNIDADE | Código da Subunidade |
| PRECOSUBUNIDADE | Preço da Subunidade |

* **Carteira**

| Coluna | Descrição |
| --- | --- |
| CODCOLIGADA | Código da Coligada da Carteira |
| COD\_PESS\_EMPR | Código do Empreendimento |
| CODCCUSTO | Código do Centro de Custo |
| CODCFO | Código do Comprador |
| NUMVENDA | Número da Venda |
| CONTRATO | Número do Contrato da venda |
| COD\_SIT\_VENDA | Código da Situação da Venda |
| NUM\_UNID | Código da Unidade |
| NUM\_SUB\_UNID | Código da Subunidade |
| DATAVENCIMENTO | Data de Vencimento da Parcela |
| DATABAIXA | Data da baixa do Lançamento |
| IDLAN | Código do Lançamento |
| NUMPARC | Número da Parcela no Financiamento |
| CODGRUPO | Número do grupo da venda |
| CODTIPOPARC | Código do Tipo da Parcela |
| STATUS | Status do Lançamento |
| VALOR | Valor do Componente |
| COD\_COMPN | Código do Componente |
| VALORBAIXADO | Valor baixado do Componente |

* **Vendas Distratadas**

| Coluna | Descrição |
| --- | --- |
| CODCOLIGADA | Código da Coligada da Venda Distratada |
| NUMVENDA | Número da Venda |
| COD\_SIT\_VENDA | Código da Situação da Venda |
| CODTIPODISTRATO | Código do Tipo de Distrato |
| CODMOTIVODISTRATO | Código do Motivo de Distrato |
| DATABASEDISTRATO | Data base do Distrato |
| COD\_PESS\_EMPR | Código do Empreendimento |
| NUM\_UNID | Número da Unidade |
| NUM\_SUB\_UNID | Número da Subunidade |
| VALORDEVOLUCAO | Valor a ser devolvido para o cliente pelo distrato |

Inc10DiagramaDiagrama

Diagrama das ligações entre as dimensões e os fatos

ObrasProjetosObras e ProjetosObras e Projetos01ESPTOPIndicadoresIndicadoresTabela Analítica de Funcionários03PITOPPainel de IndicadoresPainel de Indicadores

Este dashboard permite visualizar os indicadores de desempenho do Projeto, permitindo verificar o Valor Total dos Pagamentos e Recebimentos, Custo Apropriado, Avanço Físico e os Valores Médios, assim como indica um percentual em relação ao Mês e Ano anteriores.

Os indicadores exibidos são quebrados periodicamente conforme os filtros aplicados. Os filtros utilizados neste Dashboard são:

* **Período:** Informe a Data Início e Data Fim das quais deseja extrair as informações, sendo que a Data Fim deve ser obrigatoriamente maior que a Data Início.
* **Coligada:** Coligada(s) das Obras e Projetos que deseja extrair os indicadores.
* **Filial:** Filial(ais) das Obras e Projetos que deseja extrair os indicadores.
* **Centro de Custo:** Selecione o Centro de Custo das Obras e Projetos que deseja extrair os indicadores.
* **Projeto:** Selecione o(s) Projeto(s) dos quais deseja extrair os indicadores.
* **Tarefa:** Selecione a(s) Tarefa(s) das quais deseja extrair ps indicadores.
* **Moeda:** Selecione a Moeda.

Neste Painel, ao clicar em um dos valores/ percentuais apresentados, o sistema demonstrará o detalhamento do mesmo. Este detalhamento será apresentado em forma de Tabela, podendo o usuário visualiza-lo também em formato de gráfico (Linha, Barras ou Pizza).

* **Avanço Físico**

Representa o Percentual Realizado do Projeto/Tarefa. Essa informação é extraída do cronograma realizado considerando o percentual da tarefa em relação ao projeto.

* **Custo Previsto**

Representa o valor do Custo Previsto do Projeto/Tarefa. Essa informação é extraída do cálculo (Percentual Planejado \* Custo Total da Tarefa).

* **Custo Apropriado**

Representa o valor do Custo Apropriado do Projeto/Tarefa. Essa informação é extraída do cálculo (Quantidade Apropriada \* Preço Unitário Apropriado), considerando o fator de conversão no caso de moeda estrangeira.

* **Média Custo Apropriado**

Representa a média do valor do Custo Apropriado do Projeto/Tarefa. Essa informação é extraída do cálculo (Quantidade Apropriada \* Preço Unitário Apropriado)/ Quantidade Apropriada, considerando o fator de conversão no caso de moeda estrangeira.

* **Qtd Tarefas Finalizadas**

Representa o número de tarefas concluídas, baseando-se nas informações do Avanço Físico no qual Percentual Realizado é maior ou igual à 100%.

* **Total Pago**

Representa o total de pagamentos realizados, baseando-se nas informações da visão financeira realizada.

* **Vlr Pago em Atraso**

Representa o total de pagamentos em atraso, ou seja, aqueles cuja data da baixa é maior do que a data de vencimento, baseando-se nas informações da visão financeira realizada.

* **Vlr a Pagar**

Representa o total de pagamentos em aberto, baseando-se nas informações da visão financeira.

* **Vlr no Prazo a Pagar**

Representa o total de pagamentos em aberto que estão dentro do prazo de vencimento, baseando-se nas informações da visão financeira.

* **Vlr Atrasado a Pagar**

Representa o total de pagamentos em aberto que passaram do prazo de vencimento, baseando-se nas informações da visão financeira.

* **Vlr Previsto a Pagar**

Representa o total de pagamentos relacionados ao custo previsto que estão em aberto, baseando-se nas informações da visão financeira.

* **Vlr Total Recebido**

Representa o total de recebimentos, baseando-se nas informações da visão financeira realizada.

* **Vlr Recebido em Atraso**

Representa o total de recebimentos em atraso, nos quais a data da baixa é maior do que a data de vencimento, conforme as informações da visão financeira realizada.

* **Vlr a Receber**

Representa o total de recebimentos em aberto, conforme as informações da visão financeira.

* **Vlr no Prazo a receber**

Representa o total de recebimentos em aberto que estão dentro do prazo de vencimento, conforme as informações da visão financeira.

TELA

* **Vlr Atrasado a Receber**

Representa o total de recebimentos em aberto que passaram do prazo de vencimento, conforme as informações da visão financeira.

* **Vlr Previsto a Receber**

Representa o total de recebimentos que estão em aberto, conforme as informações da visão financeira e custo previsto.

VGTOPVisão GeralVisão Geral

No Dashboard da Visão Geral, são apresentados a visão Financeira, Visão Econômica e dados de Custo das Obras e Projetos. Os indicadores exibidos são quebrados periodicamente conforme os filtros aplicados. Os filtros utilizados neste Dashboard são:

* **Período:** Informe a Data Início e Data Fim das quais deseja extrair as informações, sendo que a Data Fim deve ser obrigatoriamente maior que a Data Início.
* **Coligada:** Coligada(s) das Obras e Projetos que deseja extrair os indicadores.
* **Filial:** Filial(ais) das Obras e Projetos que deseja extrair os indicadores.
* **Centro de Custo:** Selecione o Centro de Custo das Obras e Projetos que deseja extrair os indicadores.
* **Projeto:** Selecione o(s) Projeto(s) dos quais deseja extrair os indicadores.
* **Tarefa:** Selecione a(s) Tarefa(s) das quais deseja extrair ps indicadores.
* **Moeda:** Selecione a Moeda.

* **Valor Pago X Valor Recebido**

Neste gráfico podemos verificar a Visão Financeira das Obras e Projetos. Visualizamos no mesmo o Valor pago versus o Valor Recebido separado pelo Período filtrado e pelos valores recebidos e pagos.

Ao clicar no drill down (bolinha de indicadores em cada período) o sistema apresenta indicadores pelo período clicado apresentando as tarefas e os Totais (Pagos ou Recebidos) assim como um totalizador (Rollup). Pode-se ter a visão por diversos gráficos Tabela, Gráfico de Linha, Gráfico de Barra e Gráfico de Pizza.

Clicando na seta indicadora para baixo ↓ o sistema permite a visualização deste Relatório e o Donwload como PDF (Retrato), PDF (Paisagem), XLSX, CSV (Formatado) e CSV (Dados Brutos).

Ao clicar no período o sistema apresenta indicadores para o período clicado apresentando as Naturezas Orçamentárias o Total Pago e o Total Recebido assim como um totalizador (Rollup). Pode-se ter uma visão por diversos gráficos, Tabela, Gráfico de Linha, Gráfico de Barra e Gráfico de Pizza.

Clicando na seta indicadora para baixo ↓ o sistema permite a visualização deste Relatório e o Donwload como PDF (Retrato), PDF (Paisagem), XLSX, CSV (Formatado) e CSV (Dados Brutos).

Ao lado, são apresentadas algumas métricas indicativas por Projeto, que são:

**Custo Previsto:** Custo Previsto para as Obras e Projetos filtrados, buscando os dados do Cronograma Previsto.

**Custo Apropriado:** Custo Apropriado das Obras e Projetos filtrados, buscando os dados do Cronograma Apropriado.

**Avanço Físico:** Avanço Físico das Obras e Projetos Filtrados, buscando os dados do Cronograma.

Nestas métricas também é possíveis a visualização das Obras e Projetos cujo os dados foram extraídos assim como o seu Totalizador. Basta clicar no valor apresentado na métrica e será permitida visualização por diversos gráficos como, Tabela, Gráfico de Linha, Gráfico de Barra e Gráfico de Pizza.

Clicando na seta indicadora para baixo ↓ o sistema permite a visualização deste Relatório e o Donwload como PDF (Retrato), PDF (Paisagem), XLSX, CSV (Formatado) e CSV (Dados Brutos).

* **Visão Econômica**

Neste gráfico podemos verificar a Visão Econômica (Contabil) das Obras e Projetos. Visualizamos os Custos e as Receitas dos Projetos no Período filtrado.

Ao clicar no drill down (Bolinha de indicadores em cada período) o sistema apresenta indicadores pelo período clicado apresentando as Contas Contábeis assim como um totalizador (Rollup) sendo permitida a visão por diversos gráficos, Tabela, Gráfico de Linha, Gráfico de Barra e Gráfico de Pizza.

Clicando na seta indicadora para baixo ↓ o sistema permite a visualização deste Relatório e o Donwload como PDF (Retrato), PDF (Paisagem), XLSX, CSV (Formatado) e CSV (Dados Brutos).

Ao clicar no período o sistema apresenta indicadores para o período clicado apresentando os Centros de Custo, o Total do Custo e da Receita, assim como um totalizador (Rollup) e sendo possível visão por diversos gráficos, Tabela, Gráfico de Linha, Gráfico de Barra e Gráfico de Pizza.

Em ambos os casos basta clicar na seta indicadora para baixo ↓ e o sistema permite a visualização deste Relatório e o Donwload como PDF (Retrato), PDF (Paisagem), XLSX, CSV (Formatado) e CSV (Dados Brutos).

* **Custo Apropriado X Custo Previsto**

Neste gráfico podemos verificar o Custo Apropriado versus o Custo Previsto separado por Projeto filtrado. Ao clicar na barra do Gráfico são apresentado os Custos por Tarefa.

* **Custo Previsto**

Este gráfico extrai as informações sobre o Custo Previsto do cronograma planejado conforme o período definido.

CATOPCusto ApropriadoCusto Apropriado

No Dashboard do Custo Apropriado, é apresentada a análise do custo apropriado por tarefas.

Os indicadores exibidos são quebrados periodicamente conforme os filtros aplicados. Os filtros utilizados neste Dashboard são:

* **Período:** Data início e Data fim que deseja extrair as informações, sendo que a Data fim deve ser obrigatoriamente maior que a Data início.
* **Coligada:** Das Obras e Projetos que deseja extrair indicadores de Movimentação Financeira.
* **Filial:** Das Obras e Projetos que deseja extrair indicadores de Movimentação Financeira.
* **Centro de Custo:** Das Obras e Projetos que deseja extrair indicadores de Movimentação Financeira.
* **Projeto:** Apenas os Projetos que deseja extrair indicadores de Movimentação Financeira.
* **Tarefa:** Apenas as Tarefas que deseja extrair indicadores de Movimentação Financeira.
* **Moeda:** Movimentação Financeira das Obras e Projetos que foram utilizada determinada Moeda.

* **Qtd Tarefas Finalizadas por Período:**

Representa a quantidade de tarefas finalizadas no intervalo filtrado. Ao clicar na quantidade o sistema exibirá os indicadores, podendo alternar entre visões de gráfico de tabela, linha, barra e pizza.

* **Valor Custo Apropriado:**

Representa o totalizador do valor do custo apropriado das tarefas finalizadas no intervalo filtrado. Ao clicar no valor o sistema exibirá os indicadores, podendo alternar entre visões de gráfico de tabela, linha, barra e pizza.

* **Média Custo Apropriado:**

Representa a média do valor do custo apropriado das tarefas no intervalo filtrado. Ao clicar na média o sistema exibirá os indicadores, podendo alternar entre visões de gráfico de tabela, linha, barra e pizza.

* **Quantidade de Tarefas Finalizadas por Data**

Representa número de tarefas finalizadas no intervalo filtrado. Ao clicar na quantidade o sistema exibirá os indicadores, podendo alternar entre visões de gráfico de tabela, linha, barra e pizza.

* **Top 10 Tarefas com Maior Custo**

Este gráfico apresenta as dez tarefas com maior custo no intervalo filtrado. Ao clicar na quantidade o sistema exibirá os indicadores, podendo alternar entre visões de gráfico de tabela, linha, barra e pizza.

* **Custo Apropriado por Mês**

Representa o custo apropriado por mês. Ao clicar na quantidade o sistema exibirá os indicadores, podendo alternar entre visões de gráfico de tabela, linha, barra e pizza.

* **Top 5 Projetos com Maior Custo Apropriado**

Este gráfico apresenta os cinco projetos com maior custo apropriado no intervalo filtrado. Ao clicar na quantidade o sistema exibirá os indicadores, podendo alternar entre visões de gráfico de tabela, linha, barra e pizza.

PAGTOPPagamentos Pagamentos 

**Evolução dos Pagamentos**

Neste gráfico podemos verificar os títulos a pagar, visualizando as linhas diferenciando o Total Pago do Total em Aberto e do Total em Atraso.

Ao clicar em qualquer valor do gráfico, será apresentado o detalhamento dos valores contidos naquele ponto do gráfico. Para o detalhamento de um período inteiro basta clicar em um dos períodos apresentados que será exibido os totais pagos, em aberto e em atraso apenas do período selecionado.

Ao lado, são apresentados os gráficos acumulados dos títulos a pagar, mostrando os títulos por valor e por quantidade:

Em ambos os gráficos pode-se detalhar os valores clicando tanto nos valores como em uma área do gráfico.

**Situação dos Títulos Pagos**

Neste gráfico são apresentados, conforme o filtro selecionado as top 10 tarefas com títulos pagos.

Cada tarefa pode ser clicada para que seja visualizado o detalhamento dos títulos da mesma, sendo possível verificar os títulos pagos período a período os títulos pagos.

RECEBTOPRecebimentosRecebimentos

No Dashboard de Financeiro – Contas a Receber, é apresentado um resumo dos títulos financeiros a receber. Os indicadores exibidos são quebrados periodicamente conforme os filtros aplicados. Os filtros utilizados neste Dashboard são:

* **Período:** Data início e Data fim que deseja extrair as informações, sendo que a Data fim deve ser obrigatoriamente maior que a Data início.
* **Coligada:** Das Obras e Projetos que deseja extrair indicadores de Movimentação Financeira.
* **Filial:** Das Obras e Projetos que deseja extrair indicadores de Movimentação Financeira.
* **Centro de Custo:** Das Obras e Projetos que deseja extrair indicadores de Movimentação Financeira.
* **Projeto:** Apenas os Projetos que deseja extrair indicadores de Movimentação Financeira.
* **Tarefa:** Apenas as Tarefas que deseja extrair indicadores de Movimentação Financeira.
* **Moeda:** Movimentação Financeira das Obras e Projetos que foram utilizada determinada Moeda.

---

**Evolução dos Recebimentos**

Neste gráfico podemos verificar os títulos a receber, visualizando as linhas diferenciando o Total Recebido do Total em Aberto e do Total em Atraso.

Ao clicar em qualquer valor do gráfico, será apresentado o detalhamento dos valores contidos naquele ponto do gráfico. Para o detalhamento de um período inteiro basta clicar em um dos períodos apresentados que será exibido os totais recebidos em aberto e em atraso apenas do período selecionado.

Ao lado, são apresentados os gráficos acumulados dos títulos a receber, mostrando os títulos por valor e por quantidade:

Em ambos os gráficos pode-se detalhar os valores clicando tanto nos valores como em uma área do gráfico.

**Situação dos Títulos Recebidos**

Neste gráfico são apresentados, conforme o filtro selecionado as top 10 tarefas com títulos recebidos.

Cada tarefa pode ser clicada para que seja visualizado o detalhamento dos títulos da mesma, sendo possível verificar os títulos recebidos período a período.

DIMDimensõesDimensõesDimensõesDIM

**Dimensões:**

* Projeto:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| IDPRJ | Identificador do Projeto |
| CODFILIAL | Identificador da Filial |
| CODPRJ | Código do Projeto |
| DESCRICAO | Descrição do Projeto |

* Tarefa:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| IDPRJ | Identificador do Projeto |
| IDTRF | Identificador da Tarefa |
| CODTRF | Código da Tarefa |
| NOME | Nome da Tarefa |
| CODFILIAL | Identificador da Filial |
| CODPRJ | Código do Projeto |
| DESCRICAO | Descrição do Projeto |

FATFatosFatosFatosFAT

**Fatos:**

* Avanço Físico:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| IDPRJ | Identificador do Projeto |
| CODFILIAL | Identificador da Filial |
| IDTRF | Identificador da Tarefa |
| DTINICIO | Data Início do Período |
| PERCREALIZADO | Percentual Realizado |

* Custo Apropriado:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| IDPRJ | Identificador do Projeto |
| IDTRF | Identificador da Tarefa |
| NUMPERIODO | Número do Período |
| MOEDA | Moeda do Custo |
| VALOR | Valor do Custo Apropriado |
| PERCENTUAL | Percentual do Apropriado |
| QUANTIDADE | Quantidade do Apropriado |
| CAMPOINFORMADO | Campo Informado (V) |
| DATAINICIOPERIODO | Data Início do Período |
| DATAFINALPERIODO | Data Fim do Período |

* Custo Previsto:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| IDPRJ | Identificador do Projeto |
| CODFILIAL | Identificador da Filial |
| IDTRF | Identificador da Tarefa |
| DTINICIO | Data Início do Período Previsto |
| CODMOEDA | Código da Moeda (Parâmetro do Projeto ou Geral) |
| VALOR | Valor do Custo Previsto |

* Índice do Projeto:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| CODFILIAL | Identificador da Filial |
| IDPRJ | Identificador do Projeto |
| DTINICIO | Data Início do Período |
| AVANCO | Percentual Realizado |

* Visão Financeira Previsto:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| STATUSLAN | Status do Lançamento |
| PAGREC | Pagar ou Receber |
| DATAVENCIMENTO | Data de Vencimento |
| CODFILIAL | Identificador da Filial |
| CODMOEDA | Moeda |
| CODNATFINANCEIRA | Natureza Orçamentária Financeira |
| IDPRJ | Identificador do Projeto |
| IDTRF | Identificador da Tarefa |
| EDEVOLUCAO | Classificação do Tipo de Documento |
| CODCCUSTO | Centro de Custo |
| TOTALABERTO | Valor Total |

* Visão Financeira Realizado:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| PAGREC | Pagar ou Receber |
| DATABAIXA | Data de Baixa |
| CODCCUSTO | Centro de Custo |
| CODFILIAL | Identificador da Filial |
| CODMOEDA | Moeda |
| CODNATFINANCEIRA | Natureza Orçamentária Financeira |
| IDPRJ | Identificador do Projeto |
| IDTRF | Identificador da Tarefa |
| EDEVOLUCAO | Classificação do Tipo de Documento |
| BXVENCIDO | Vencido |
| TOTALPAGO | Total Pago |

* Visão Econômica:

| Campo | Descrição |
| --- | --- |
| INSTANCIA | Instância do Produto (RM) |
| CODCOLIGADA | Identificador da Coligada |
| CODFILIAL | Identificador da Filial |
| IDPRJ | Identificador do Projeto |
| DATA | Data |
| CODCCUSTO | Centro de Custo |
| CONTA | Conta |
| TIPO | Tipo Visão Econômica |
| CODMOEDA | Moeda |
| VALOR | Valor |

ConfiguraçõesConfigPrj

Para que as informações da base de dados do BI possam ser enviadas para os projetos do GoodData, é necessário realizar a implantação e configuração do Agent que realiza a execução das sentenças de extração de informações e as envia aos projetos.

* **Implantação e Configuração do Agent para o Gooddata:**
  + **Definição dos parâmetros de conexão:**  
    - A pasta do agente deve estar na raiz C:\ da estação de trabalho;
    - O programa "run.bat" é o responsável por executar o Agent;
    - Antes de configurar o Agent, é necessário ter em mãos os seguintes dados para configurá-lo:

      * Credenciais de acesso (usuário / senha) do usuário responsável por enviar os dados para a plataforma GoodData (em geral é configurado um usuário corporativo do cliente para esta tarefa). Este usuário deve ter o nível de “Admin” no projeto;
      * Código do projeto do GoodData onde serão carregados os dados;
      * Código do processo de ETL que será executado ao receber os dados;
      * Nome do processo de ETL (Em geral é o nome do ERP que o cliente possui. Ex: Protheus / Datasul / VirtualAge).
    - Para conexões com bancos de dados são necessários os seguintes dados:
      * IP do banco de dados;
      * Porta do banco de dados;
      * Nome da instancia do banco de dados;
      * Credenciais de acesso (usuário / senha) para usuário do banco de dados. Este usuário só precisa ter acesso de leitura no banco.
  + **Configuração do arquivo "config.properties":** Este arquivo é composto por um conjunto de parâmetros, um em cada linha, formatados como “parâmetro=valor”. Sua configuração é necessária para a execução do Agent.
    - **Parâmetros gerais:**
      * gdc.upload\_archive: Preencher com o nome do arquivo .zip a ser enviado para o servidor da GoodData;
      * gdc.username: Preencher com o nome de usuário do GoodData;
      * gdc.password: Preencher com a senha do usuário da GoodData;
      * gdc.upload\_url; Preencher com a URL do servidor WebDav da GoodData que irá receber os dados;
      * gdc.etl.process\_url; Preencher com a URL do servidor da GoodData que irá executar o ETL;
      * gdc.etl.graph: Preencher com a URL do primeiro graph (processo) de ETL a ser executado;
      * gdc.crypto: Preencher com TRUE / FALSE. Este parâmetro define se as senhas do usuário do gooddata e do banco de dados estão criptografadas, evitando que qualquer usuário abra o arquivo config.properties e descubra a mesma. Para gerar a senha criptografada, é necessário executar o programa “encrypt\_pwd.bat”, disponível dentro do Agent;
      * gdc.backup: Preencher com TRUE / FALSE. Este parâmetro define se o arquivo enviado para o servidor do GoodData será armazenado em backup por alguns dias;
      * param.GERAL\_INSTANCIA: Pode ser utilizado como campo das consultas para determinar qual o produto, como por exemplo "RM" ou "Datasul";
      * param.START\_DATE : Data inicial do período de extração de dados, para ser utilizada nas sentenças;
      * param.FINAL\_DATE: Data final do período de extração de dados, para ser utilizada nas sentenças;  
        param.EXTRACTION\_DATE: Data que corresponde ao dia no qual os dados estão sendo extraídos.
    - **Parâmetros de banco de dados:**
      * jdbc.driver\_path: Preencher com o caminho e arquivo do driver de conexão com o banco;
      * jdbc.driver: Preencher com o nome do driver de conexão com o banco;
      * jdbc.url: Preencher com a string de conexão para o banco de dados;
      * jdbc.username: Preencher com o usuário de banco;
      * jdbc.password: Preencher com a senha do usuário de banco.
    - **Parâmetros de modo de carga:**
      * gdc.etl.param.LOAD\_MODE\_DIM: Preencher com FULL\_LOAD ou INCREMENTAL. Define o modo de carga de todos os datasets de dimensão do projeto;
      * gdc.etl.param.LOAD\_MODE\_FCT: Preencher com FULL\_LOAD ou INCREMENTAL. Define o modo de carga de todos os datasets de fatos do projeto.
    - **Parâmetros específicos para os fatos do TOTVS Obras e Projetos:**
      * param.TIPO\_MOV\_RECEITA: Este parâmetro é utilizado no gráfico Visão Econômica e nele devem ser informados os códigos dos tipos de movimento de receita do TOTVS Compras, Estoque e Faturamento (RMNucleus) que contabilizam, mas que não geram lançamentos financeiros;
      * param.COLUNA\_TIPO\_NATUREZA\_RECEITA: Este parâmetro é utilizado no gráfico Visão Econômica e nele deve ser informada a natureza contábil dos lançamentos contábeis gerados pelos tipos de movimento informados no parâmetro param.TIPO\_MOV\_RECEITA acima. Caso a natureza contábil dos lançamentos seja a crédito, este parâmetro deverá ser preenchido com CPARTIDA.CREDITO, já caso a natureza seja débito informe CPARTIDA.DEBITO;
      * param.TIPO\_MOV\_CUSTO: Este parâmetro é utilizado no gráfico Visão Econômica e nele devem ser informados os códigos dos tipos de movimento de custo do TOTVS Compras, Estoque e Faturamento (RMNucleus) que contabilizam, mas que não geram lançamentos financeiros;
      * param.COLUNA\_TIPO\_NATUREZA\_CUSTO: Este parâmetro é utilizado no gráfico Visão Econômica e nele deve ser informada a natureza contábil dos lançamentos contábeis gerados pelos tipos de movimento informados no parâmetro param.TIPO\_MOV\_CUSTO acima. Caso a natureza contábil dos lançamentos seja a crédito, este parâmetro deverá ser preenchido com CPARTIDA.CREDITO, já caso a natureza seja débito informe CPARTIDA.DEBITO;
      * param.TIPO\_MOV\_DEV\_COMPRA: Este parâmetro é utilizado no gráfico Visão Econômica e nele devem ser informados os códigos dos tipos de movimento de devolução de compra do TOTVS Compras, Estoque e Faturamento (RMNucleus) que contabilizam, mas que não geram lançamentos financeiros;
      * param.COLUNA\_TIPO\_NATUREZA\_DEV\_COMPRA: Este parâmetro é utilizado no gráfico Visão Econômica e nele deve ser informada a natureza contábil dos lançamentos contábeis gerados pelos tipos de movimento informados no parâmetro param.TIPO\_MOV\_DEV\_COMPRA acima. Caso a natureza contábil dos lançamentos seja a crédito, este parâmetro deverá ser preenchido com CPARTIDA.CREDITO, já caso a natureza seja débito informe CPARTIDA.DEBITO;
      * param.TIPO\_MOV\_DEV\_VENDA: Este parâmetro é utilizado no gráfico Visão Econômica e nele devem ser informados os códigos dos tipos de movimento de devolução de venda do TOTVS Compras, Estoque e Faturamento (RMNucleus) que contabilizam, mas que não geram lançamentos financeiros;
      * param.COLUNA\_TIPO\_NATUREZA\_DEV\_VENDA: Este parâmetro é utilizado no gráfico Visão Econômica e nele deve ser informada a natureza contábil dos lançamentos contábeis gerados pelos tipos de movimento informados no parâmetro param.TIPO\_MOV\_DEV\_VENDA acima. Caso a natureza contábil dos lançamentos seja a crédito, este parâmetro deverá ser preenchido com CPARTIDA.CREDITO, já caso a natureza seja débito informe CPARTIDA.DEBITO;
      * param.COLUNA\_TIPO\_NATUREZA\_FIN\_RECEBER: Este parâmetro é utilizado no gráfico Visão Econômica e nele deve ser informada a natureza contábil dos lançamentos contábeis gerados pelas baixas a receber. Caso a natureza contábil dos lançamentos seja a crédito, este parâmetro deverá ser preenchido com CPARTIDA.CREDITO, já caso a natureza seja débito informe CPARTIDA.DEBITO;
      * param.COLUNA\_TIPO\_NATUREZA\_FIN\_PAGAR: Este parâmetro é utilizado no gráfico Visão Econômica e nele deve ser informada a natureza contábil dos lançamentos contábeis gerados pelas baixas a pagar. Caso a natureza contábil dos lançamentos seja a crédito, este parâmetro deverá ser preenchido com CPARTIDA.CREDITO, já caso a natureza seja débito informe CPARTIDA.DEBITO.
  + ****Funcionamento do Agent:****
    - O Agent é o programa responsável por extrair os dados do banco de dados do cliente, enviá-los para o GoodData, e ativar a execução do ETL, responsável por carregar efetivamente os dados no GoodData. São executadas os seguintes passos:
      1. Leitura de todos os parâmetros do arquivo config.properties;
      2. Realização de um teste de conexão com a plataforma GoodData, utilizando o usuário/senha informados no arquivo config.properties;
      3. Se os parâmetros de banco de dados forem informados, o Agent irá verificar a existência de uma pasta “query” no local em que foi instalado, e se conectar ao banco de dados:
         1. Se a pasta existir, todos os arquivos .txt dentro desta pasta (e suas subpastas) serão lidos pelo agent, e executados no banco de dados como queries;
         2. Se a pasta não existir, o agent irá procurar as queries a serem executadas na tabela “I01” do banco de dados. Esta tabela “I01” armazena todas as queries do FAST Analytics, criptografadas;
         3. Execução de todas as queries extraídas.
      4. Se os parâmetros de banco de dados não forem informados, o Agent irá selecionar todos os arquivos presentes na pasta “Dados”, para envio para o GoodData;
      5. Compressão (.zip) de todos os resultados gerados;
      6. Conexão com a plataforma GoodData;
      7. Envio dos arquivo .zip ao GoodData;
      8. Execução do ETL.
    - Todas as execuções do Agent são armazenadas na pasta “log” do mesmo. O arquivo de log gerado pelo Agent pode ser enviado para a equipe de suporte caso algum erro venha a ocorrer em sua execução, juntamente com o arquivo “config.properties” utilizado.
  + **Exemplo de diretório de implantação e de parâmetros do "config.properties":**
    - Diretório:
    - **config.properties:**
controladoriaControladoria

Detalhamento sobre as dimensões e fatos relacionadas ao Fast Analytics da Controladoria:

geral\_controladoriatruectb\_dimensoesDimensões

Em desenvolvimento...

ctb\_fatosFatos

Segue o nome e detalhamento das fatos utilizadas pela Controladoria:

* **Contabilidade**:  
  Extrai o saldo e as movimentações (totais de débitos e créditos) das contas contábeis conforme o período definido na extração. Os valores são quebrados mensalmente, por empresa, filial, centro de custo e conta contábil, dentro do período de extração.

  | Campo | Decrição | Indicador (Gooddata) |
  | --- | --- | --- |
  | VLSALDOINICIAL | Indica o saldo inicial contábil do período. | Vl Saldo Inicial Real |
  | VLMOVCONTABIL | Indica o valor que foi realizado no período | Vl Movimento Contábil Real |
  | VLDEBITO | Indica o valor do movimento a debito no período. | Vl Débito Real |
  | VLCREDITO | Indica o valor do movimento a crédito no período | Vl Crédito Real |
  | VLSALDOFINAL | Indica o saldo final contábil do período | Vl Saldo Final Real |
  | VLAPURACAORESULTADO | Indica o valor contábil referente à apuração de resultado. (Histórico de fechamento) | Vl Apuração Resultado |

educacionalEducacional

Detalhamento sobre as dimensões e fatos relacionadas ao Fast Analytics do Educacional:

Geral\_Educacionaledu\_dimensoesDimensões

No Educacional, atualmente existem as seguintes Dimensões:



Segue detalhamento das dimensões citadas anteriormente:

* **Área de Conhecimento (apenas Ensino Superior):** **edudimareaconhecimento**  
  Lista as áreas de conhecimento dos cursos (Ex.: Ciências Exatas, Ciências Biológicas, Engenharias, etc).

  | Campo | Descrição | Campo no Banco de Dados |
  | --- | --- | --- |
  | INSTANCIA | Instância do Produto (RM) | Não se aplica |
  | CODCOLIGADA | Identificador da Coligada | SAREA.CODCOLIGADA |
  | CODAREA | Identificador da Área de Conhecimento | SAREA.CODAREA |
  | NOME | Descrição da Área de Conhecimento | SAREA.NOME |

* **Bolsa Educacional:** **edudimbolsaeducacional**Lista as bolsas disponíveis na instituição de ensino.

  | Campo | Descrição | Campo no Banco de Dados |
  | --- | --- | --- |
  | INSTANCIA | Instância do Produto (RM) | Não se aplica |
  | CODCOLIGADA | Identificador da Coligada | SBOLSA.CODCOLIGADA |
  | CODBOLSA | Identificador da Bolsa | SBOLSA.CODBOLSA |
  | CODAGRUPBOLSA | Identificador do Agrupamento de Bolsas | EDUKPI\_BOLSA.IDAGRUP |
  | NOME | Descrição da Bolsa | SBOLSA.NOME |
  | DESCAGRUPBOLSA | Descrição do Agrupamento de Bolsas | SAGRUPANALYTICS.DESCRICAO |
  | FIES | Identifica FIES | SBOLSA.FIES |

  ObservaçãoO cadastro dos agrupamento de bolsas pode ser feito em: **TOTVS Educacional | Integração | Cadastro de Agrupamentos**, dessa forma,  
  os filtros existentes no GoodData exibirão esses agrupamentos, de forma decrescente, e não mais todas as bolsas parametrizadas   
  (esse comportamento é válido desde que a opção **Ativa agrupamento de bolsas** esteja marcada no parametrizador do TOTVS Fast Analytics).

* **Curso:** **edudimcurso**  
  Lista os cursos da instituição de ensino, conforme parametrização dos cursos que serão enviados para o GoodData.

  | Campo | Descrição | Campo no Banco de Dados |
  | --- | --- | --- |
  | INSTANCIA | Instância do Produto (RM) | Não se aplica |
  | CODCOLIGADA | Identificador da Coligada | SCURSO.CODCOLIGADA |
  | CODCURSO | Identificador do Curso | SCURSO.CODCURSO |
  | NOME | Descrição do Curso | SCURSO.NOME |

* **Habilitação:** **edudimhabilitacao**  
  Lista as habilitações cadastradas para cursos do ensino superior (Ex.: Curso de Ciências Biológicas com habilitação em Ecologia).  
  No caso do ensino básico, lista as séries/anos (Ex.: 1º ano do Ensino Fundamental).

  | Campo | Descrição | Campo no Banco de Dados |
  | --- | --- | --- |
  | INSTANCIA | Instância do produto (RM) | Não se aplica |
  | CODCOLIGADA | Identificador da coligada | SHABILITACAO.CODCOLIGADA |
  | CODCURSO | Identificador do curso relacionado com a habilitação | SHABILITACAO.CODCURSO |
  | CODHABILITACAO | Identificador da habilitação | SHABILITACAO.CODHABILITACAO |
  | NOME | Descrição da habilitação | SHABILITACAO.NOME |

* **Modalidade de Curso:** **edudimmodalidadecurso**  
  Lista as modalidades disponível para o curso (Presencial ou EAD).

  | Campo | Descrição | Campo no Banco de Dados |
  | --- | --- | --- |
  | INSTANCIA | Instância do produto (RM) | Não se aplica |
  | CODCURPRESDIST | Identificador da modalidade | Não se aplica |
  | DESCRICAO | Descrição da modalidade | Não se aplica |

* **Nível de Ensino: edudimnivelensino**  
  Lista os níveis de ensino disponíveis na Instituição de Ensino.

  | Campo | Descrição | Campo no Banco de Dados |
  | --- | --- | --- |
  | INSTANCIA | Instância do produto (RM) | Não se aplica |
  | CODCOLIGADA | Identificador da coligada | STIPOCURSO.CODCOLIGADA |
  | CODTIPOCURSO | Identificador do nível de ensino | STIPOCURSO.CODTIPOCURSO |
  | NOME | Descrição do nível de ensino | STIPOCURSO.NOME |
  | APRESENTACAO | Identificador binário do nível de ensino | STIPOCURSO.APRESENTACAO |
  | APRESENTACAODESCRICAO | Descrição do campo apresentação (Básico ou Superior) | Não se aplica |

* **Período Letivo: edudimperiodoletivo**  
  Lista os períodos letivos da instituição de ensino, conforme valores parametrizados dos períodos letivos que serão enviados ao GoodData.

  | Campo | Descrição | Campos no Banco de Dados |
  | --- | --- | --- |
  | INSTANCIA | Instância do produto (RM) | Não se aplica |
  | CODCOLIGADA | Identificador da coligada | SPLETIVO.CODCOLIGADA |
  | IDPERLET | Identificador do período letivo ou agrupamento | Caso período letivo: SPLETIVO.IDPERLET Caso agrupamento: AGRUPPLETIVO.ID |
  | CODPERLET | Código alfanumérico do período letivo ou do agrupamento | Caso período letivo: SPLETIVO.CODPERLET Caso agrupamento: AGRUPPLETIVO.CODAGRUPAMENTO |
  | DESCRICAO | Descrição do período letivo ou do agrupamento | Caso período letivo: SPLETIVO.DESCRICAO Caso agrupamento: AGRUPPLETIVO.DESCRICAO |
  | ORDEM | Ordem definida no cadastro de agrupamentos para exibição, de forma decrescente,  dos itens no filtro de período letivo do GoodData (válido apenas quando configurado o agrupamento de período letivos). | Caso período letivo: 0 Caso agrupamento: AGRUPPLETIVO.ORDEM |
  | ENCERRADO | Indica se o período letivo está encerrado | SPLETIVO.ENCERRADO |

  ObservaçãoO cadastro dos agrupamentos de períodos letivo pode ser feito em: **TOTVS Educacional | Integração | Cadastro de Agrupamentos**, dessa forma,  
  os filtros existentes no GoodData exibirão esses agrupamentos, de forma decrescente, e não mais todos os períodos letivos parametrizados   
  (esse comportamento é válido desde que a opção **Ativa agrupamento de períodos letivos** esteja marcado no parametrizador do TOTVS Fast Analytics).

* **Serviços**: edudimservicos  
  Lista os serviços relacionados as parcelas de cursos da instituição de ensino, conforme valores parametrizados dos serviços que serão enviados ao GoodData

  | Campo | Descrição | Campo do Banco de Dados |
  | --- | --- | --- |
  | INSTANCIA | Instância do produto (RM) | Não se aplica |
  | CODCOLIGADA | Identificador da coligada | SSERVICO.CODCOLIGADA |
  | CODSERVICO | Identificador do serviço | SSERVICO.CODSERVICO |
  | NOME | Descrição do serviço | SSERVICO.NOME |

* **Tipo do Curso (apenas Ensino Superior):** **edudimtipocurso**  
  Lista os tipos de cursos cadastrados (Ex: Bacharelado, Licenciatura, etc)

  | Campo | Descrição | Campo no Banco de Dados |
  | --- | --- | --- |
  | INSTANCIA | Instância do produto (RM) | Não se aplica |
  | CODCOLIGADA | Identificador da coligada | SMODALIDADECURSO.CODCOLIGADA |
  | CODMODALIDADECURSO | Identificador do tipo do curso | SMODALIDADECURSO.CODMODALIDADECURSO |
  | DESCRICAO | Descrição do tipo do curso | SMODALIDADECURSO.DESCRICAO |

* **Tipo de Documento:** **edudimtipodocumento**  
  Lista os tipos de documentos relacionados aos lançamentos gerados a partir das parcelas do contrato, conforme valores parametrizadas dos tipos de documentos que serão enviados ao GoodData.

  | Campo | Descrição | Campo no Banco de Dados |
  | --- | --- | --- |
  | INSTANCIA | Instância do produto (RM) | Não se aplica |
  | CODCOLIGADA | Identificador da coligada | FTDO.CODCOLIGADA |
  | CODTDO | Identificador do tipo do documento | FTDO.CODTDO |
  | DESCRICAO | Descrição do tipo do documento | FTDO.DESCRICAO |

* **Turno:** **edudimturno**  
  Lista os turnos disponíveis na instituição de ensino.

  | Campo | Descrição | Campo no Banco de Dados |
  | --- | --- | --- |
  | INSTANCIA | Instância do produto (RM) | Não se aplica |
  | CODCOLIGADA | Identificador da coligada | STURNO.CODCOLIGADA |
  | CODTURNO | Identificador do turno | STURNO.CODTURNO |
  | NOME | Descrição do Turno | STURNO.NOME |
edu\_fatosFatos

No Educacional, atualmente existem as seguintes Fatos:

* Acadêmico:
* Financeiro:

Segue detalhamento das fatos citadas anteriormente:

* **ALUNOS**: edufatoalunos  
  Lista as informações sobre os alunos matriculados na instituição de ensino, conforme o período definido pelos parâmetros de extração.   
    
  Os indicadores de Alunos, são quebrados mensalmente por:
  + Coligada
  + Filial
  + Nível de Ensino
  + Curso
  + Habilitação
  + Período Letivo
  + Turno
  + Modalidade
  + Área de Conhecimento
  + Tipo do Curso.  
  Para a correta visualização no GoodData, os campos da fato de Aluno possuem suas regras, que estarão listadas na tabela abaixo, no entanto todos eles possuem como regras comuns as seguintes:
  + O aluno deve estar relacionado a um curso parametrizado para ser enviado ao GoodData.
  + O aluno deve estar relacionado a um período letivo parametrizado para ser enviado ao GoodData.

  | Campo | Descrição | Indicador (GoodData) | Regra |
  | --- | --- | --- | --- |
  | BASE | Quantidade de alunos ativos no mês anterior ao período de datas selecionado | **Quantidade de Alunos Base** | + Parametrização de alunos ativos. + **Data da matrícula** deve ser menor que a data final de extração. + **Data da matrícula** deve estar dentro das datas início e término ou início e previsão de término do período letivo, ou anterior a data de início do período letivo. + **Data final de extração** deve estar dentro das datas início e término ou início e previsão de término do período letivo. |
  | FIES | Quantidade de alunos ativos na instituição que possuem bolsa FIES | **Quantidade de Alunos com FIES** | + Parametrização de alunos ativos. + Marcação da flag “FIES” no cadastro de bolsa no TOTVS Educacional. + **Data da matrícula** deve ser menor que a data final de extração. + **Data da matrícula** deve estar dentro das datas início e término ou início e previsão de término do período letivo. + **Data final de extração** deve estar dentro das datas início e término ou início e previsão de término do período letivo. |
  | BOLSISTAS | Quantidade de alunos ativos na instituição que possui algum tipo de bolsa ativa (inclusive FIES) | **Quantidade de Alunos Bolsistas** | + Parametrização de alunos ativos. + Parametrização de bolsas. + **Data da matrícula** deve ser menor que a data final de extração (alterada mês a mês até a data final escolhida na extração). + **Data da matrícula** deve estar dentro das datas início e término ou início e previsão de término do período letivo. + **Data final de extração** deve estar dentro das datas início e término ou início e previsão de término do período letivo. |
  | EVADIDOS | Quantidade de alunos que evadiram da instituição de ensino | **Quantidade de Alunos Evadidos** | + Parametrização de alunos evadidos. + **Data** **de alteração do status da matrícula no período letivo**, para um status que indica que o aluno evadiu, deve estar dentro do período de extração. + **Data****inicial e final do período de extração** deverão estar dentro das datas início e término ou início e previsão de término do período letivo. |
  | FORMADOS | Quantidade de alunos formados | **Quantidade de Alunos Formados** | + **Ensino Superior**    - Parametrização de egresso de alunos.   - **Data de conclusão de curso** deve estar dentro do período de extração, quando o parâmetro "Considerar a Data de Conclusão de Curso" estiver marcado. Nesse caso, o extrator considerará a data de conclusão, ao invés da Situação de Matrícula parametrizada.   - **Data** **de alteração do status da matrícula no período letivo**, para um status que indica que o aluno é egresso, deve estar dentro do período de extração.   - **Data inicial e final do período de extração** deverão estar dentro das datas início e término ou início e previsão de término do período letivo. + **Ensino Básico**   - Parametrização de egresso de alunos.   - Parametrização de última série egresso.   - **Data** **de alteração do status da matrícula no período letivo**, para um status que indica que o aluno é egresso, deve estar dentro do período de extração.   - **Data inicial e final do período de extração** deverão estar dentro das datas início e término ou início e previsão de término do período letivo. |
  | NOVOS | Quantidade de novos alunos que ingressaram no primeiro período/série da instituição de ensino | **Quantidade de Novos Alunos** | + Parametrização de alunos ativos. + **Data de matrícula** deve estar dentro do período de extração. + **Data da matrícula** deve estar dentro das datas início e término ou início e previsão de término do período letivo + **Data inicial e final do período de extração** deverão estar dentro das datas início e término ou início e previsão de término do período letivo. + Não deve existir matrícula em outro período letivo para o aluno. + Aluno não pode ter sido transferido de outro curso. + Último status do aluno no mês de entrada no curso, deve ser um dos status parametrizado para os indicadores de aluno ativo, evadido ou transferido internamente para outro curso da instituição de ensino. |
  | ATIVOS alunosativos | Quantidade de alunos ativos | **Quantidade de Alunos Ativos** | + Parametrização de alunos ativos. + **Data da matrícula** deve ser menor que a data final de extração. + **Data da matrícula** deve estar dentro das datas início e término ou início e previsão de término do período letivo, ou anterior à data de início do período letivo. + **Data final de extração** deve estar dentro das datas início e término ou início e previsão de término do período letivo. |
  | TRANSFERENCIAINTERNAENTRADA | Quantidade de transferências internas de entrada em cursos | **Quantidade de Transferência Interna Entrada** | + Parametrização de transferência interna. + **Data da matrícula** deve ser menor que a data final de extração. + **Data da matrícula** deve estar dentro das datas início e término ou início e previsão de término do período letivo, ou anterior à data de início do período letivo. + **Data final de extração** deve estar dentro das datas início e término ou início e previsão de término do período letivo. + O aluno deve ter status de transferência interna no último log da habilitação de origem. |
  | TRANSFERENCIAINTERNASAIDA | Quantidade de transferências internas de saída de cursos | **Quantidade de Transferência Interna Saída** | + Parametrização de transferência interna. + **Data da matrícula** deve ser menor que a data final de extração. + **Data da matrícula** deve estar dentro das datas início e término ou início e previsão de término do período letivo, ou anterior à data de início do período letivo. + **Data final de extração** deve estar dentro das datas início e término ou início e previsão de término do período letivo. + **Data** **de alteração do status da matrícula no período letivo**, para um status que indica que houve transferência interna, deve estar dentro do período de extração. |

* **BOLSA**: edufatobolsa  
  Lista informações sobre quantidade e valor de bolsas concedidas para os alunos da instituição de ensino.  
    
  Os indicadores de alunos, são quebrados mensalmente por:

  + Coligada
  + Filial
  + Nível de Ensino
  + Curso
  + Habilitação
  + Período Letivo
  + Turno
  + Modalidade
  + Área de Conhecimento
  + Tipo do Curso
  + Serviço
  + Código da Bolsa
  + Data de Vencimento da Parcela

  Para a correta visualização no GoodData, os campos da fato de Bolsa possuem as seguintes regras comuns:

  + As bolsas devem estar relacionadas à parcelas com data de vencimento no período de extração.
  + As bolsas devem estar disponíveis no período letivo do contrato onde foi concedida.
  + As bolsas devem estar aplicadas à parcelas com lançamento já gerados.

  | Campo | Descrição | Indicador (GoodData) | Regra |
  | --- | --- | --- | --- |
  | QTDEBOLSA | Quantidade de bolsas (exceto FIES). | **Quantidade de Bolsa** | + Não contém regra específica |
  | QTDEFIES | Quantidade de FIES. | **Quantidade de FIES** | + Não contém regra específica |
  | VALORBOLSA | Valor total de bolsas (exceto FIES). | **Valor Bolsa** | + Não contém regra específica |
  | VALORFIES | Valor total de FIES. | **Valor FIES** | + Não contém regra específica |

* **FATURAMENTO**: edufatofaturamento  
  Lista o faturamento previsto para a instituição de ensino, conforme o período definido pelos parâmetros de extração.  
    
  Os indicadores de Faturamento, são quebrados mensalmente por:

  + Coligada
  + Filial
  + Nível de Ensino
  + Curso
  + Habilitação
  + Período Letivo
  + Turno
  + Modalidade
  + Área de Conhecimento
  + Tipo do Curso
  + Serviço
  + Tipo de Documento
  + Centro de Custo
  + Data de Faturamento

  Para a correta visualização no GoodData, os campos da fato de Faturamento possuem as seguintes regras comuns:

  + Serão considerados para o cálculo do faturamento os lançamentos do educacional que possuem status diferente de cancelado.
  + O lançamento deve possuir data de faturamento, entre a data inicial e final de extração.

  | Campo | Descrição | Indicador (GoodData) | Regra |
  | --- | --- | --- | --- |
  | VALORFATURAMENTO | Valor total do faturamento. | **Valor Faturamento** | + Tipo do contrato **diferente de Acordo**. + Não ser lançamento relacionado a bolsa de crédito. |
  | VALORBOLSA | Valor total de bolsas. | **Valor Bolsa** | + Tipo do contrato **diferente de Acordo**. |
  | VALORFATURAMENTOACORDO | Valor total de acordos. | **Valor Faturamento Acordo** | + Contrato **do tipo Acordo**. + Não ser lançamento relacionado a bolsa de crédito. |
* **INADIMPLÊNCIA**: edufatoinadimplencia  
  Lista a inadimplência da instituição de ensino (acumulada e mensal), conforme o período definido pelos parâmetros de extração.  
    
  Os indicadores de Inadimplência, são quebrados mensalmente por:

  + Coligada
  + Filial
  + Nível de Ensino
  + Curso
  + Habilitação
  + Período Letivo
  + Turno
  + Modalidade
  + Área de Conhecimento
  + Tipo do Curso
  + Serviço
  + Tipo de Documento
  + Centro de Custo
  + Mês de Vencimento

  Para a correta visualização no GoodData, os campos da fato de Inadimplência possuem as seguintes regras comuns:

  + Serão considerados para o cálculo de inadimplência, lançamentos que estejam com status **Baixado** ou **Baixado por Acordo** e cuja data de vencimento somada ao valor do parâmetro **Número de dias após o vencimento para considerar como inadimplência** esteja entre o período de extração e menor que a data da baixa do lançamento.
  + Serão considerados para o cálculo de inadimplência, lançamentos que estejam com status **Em Aberto**, **Parcialmente Baixado** e cuja data de vencimento somada ao valor do parâmetro **Número de dias após o vencimento para considerar como inadimplência** esteja entre o período de extração.

  | Campo | Descrição | Indicador (GoodData) | Regra |
  | --- | --- | --- | --- |
  | VLINADIMPLENCIACUMULADO | Valor total da inadimplência acumulada até o mês da extração. | **Valor Inadimplência Acumulado** | + Tipo do contrato **diferente de Acordo**. + A partir do mês que a baixa é feita o valor deixa de ser considerado. |
  | VLINADIMPLENCIAMENSAL | Valor total da inadimplência no mês da extração. | **Valor Inadimplência Mensal** | + Tipo do contrato **diferente de Acordo**. |
  | VLINADIMPLENCIAACORDO | Valor total da inadimplência acumulada até o mês da extração. | **Valor Inadimplência Acordo** | + Contratos **do tipo Acordo**. + A partir do mês que a baixa é feita o valor deixa de ser considerado. |
  | VLINADIMPLENCIAACORDOMENSAL | Valor total da inadimplência no mês da extração. | **Valor Inadimplência Acordo Mensal** | + Contratos **do tipo Acordo**. |

* **A RECEBER**: edufatoareceber  
  Lista os valores A Receber da instituição de ensino.  
    
  Os indicadores dos valores a receber, são quebrados mensalmente por:

  + Coligada
  + Filial
  + Nível de Ensino
  + Curso
  + Habilitação
  + Período Letivo
  + Turno
  + Modalidade
  + Área de Conhecimento
  + Tipo do Curso
  + Centro de Custo
  + Mês de Vencimento

  Para a correta visualização no GoodData, os campos da fato A Receber possuem as seguintes regras comuns:

  + Serão considerados para o cálculo dos valores a receber os lançamentos do educacional que possuem status igual a **Em Aberto** ou **Parcialmente Baixado**.
  + Se o lançamento estiver em aberto, é considerado apenas o valor original para definição do valor a receber/valor a receber acordo.
  + Apenas lançamentos relacionados à matrículas no período letivo de coligadas ativas serão enviados para o GoodData.

  | Campo | Descrição | Indicador (GoodData) | Regra |
  | --- | --- | --- | --- |
  | VALORARECEBER | Valor total a receber pela instituição de ensino no mês. | **Valor a Receber** | + Se o lançamento estiver parcialmente baixado, é efetuado a seguinte operação: valor original -  desconto + juros + multa - valor baixado. + Tipo do contrato **diferente de Acordo**. |
  | VLARECEBERACORDO | Valor total a receber pela instituição de ensino no mês de lançamentos gerados por acordo. | **Valor a Receber Acordo** | + Se o lançamento estiver parcialmente baixado, é efetuado a seguinte operação: valor original -  desconto + juros + multa - valor baixado + valor acréscimo do acordo - valor desconto do acordo + Contratos **do tipo Acordo**. |
  | VALORBOLSA | Valor total de bolsas relacionadas aos lançamentos a receber, gerados a partir de contratos do tipo padrão, pela instituição de ensino | Valor Bolsa | + Tipo do contrato **diferente de Acordo** |
* **RECEBIDO: edufatorecebido**  
  Lista os valores Recebidos pela instituição de ensino.  
    
  Os indicadores de valores recebidos, são quebrados mensalmente por:

  + Coligada
  + Filial
  + Nível de Ensino
  + Curso
  + Habilitação
  + Período Letivo
  + Turno
  + Modalidade
  + Área de Conhecimento
  + Tipo do Curso
  + Serviço
  + Tipo de Documento
  + Centro de Custo
  + Mês da Baixa

  Para a correta visualização no GoodData, os campos da fato de valor recebido possuem as seguintes regras comuns:

  + Serão considerados para o cálculo dos valores recebidos os lançamentos do educacional que possuem status igual a **Baixado** ou **Parcialmente Baixado**.
  + É considerado como valor recebido o valor baixado.
  + A data da baixa do lançamento precisa estar dentro do período de extração.
  + Apenas lançamentos relacionados à matrículas no período letivo de coligadas ativas serão enviados para o GoodData.
  + Caso seja realizada uma baixa retroativa, deverá ser executada uma nova extração para o período da data de baixa deste lançamento.

  | Campo | Descrição | Indicador (GoodData) | Regra |
  | --- | --- | --- | --- |
  | VALORRECEBIDO | Valor diário recebido. | **Valor Recebido** | + Tipo do contrato **diferente de Acordo**. |
  | VALORRECACORDO | Valor diário recebido de contratos do tipo Acordo. | **Valor Recebido do Acordo** | + Contratos **do tipo Acordo**. |

* ****ACORDO: edufatoacordo****Lista a quantidade de acordos realizados pela instituição, a quantidade de alunos que fizeram acordos, a quantidade de acordos que já tiveram todos os seus lançamentos baixados e a quantidade de acordos que ainda possuem lançamentos em aberto.  
    
  Os indicadores de Acordo, são quebrados mensalmente por:

  + Coligada
  + Filial
  + Nível de Ensino
  + Curso
  + Habilitação
  + Período Letivo
  + Turno
  + Modalidade
  + Área de Conhecimento
  + Serviço

  Para a correta visualização no GoodData, os campos da fato de acordo possuem as seguintes regras comuns:

  + Serão considerados para o cálculo dos valores relacionados à contratos do tipo **Acordo**.
  + Apenas lançamentos relacionados à matrículas no período letivo de coligadas ativas serão enviados para o GoodData.

  | Campo | Descrição | Indicador (GoodData) | Regra |
  | --- | --- | --- | --- |
  | QTDALUNO | Quantidade de alunos que realizaram acordos.   **Observação:** Caso o aluno possua duas matrículas em cursos distintos, ele será retornado duas vezes no indicador de quantidade de alunos. | **Quantidade de Alunos** | + **Data do contrato** deve estar dentro do período de extração. |
  | QTDACORDO | Quantidade de contratos do tipo acordo realizados pela instituição. | **Quantidade de Acordos** | + **Data do contrato** deve estar dentro do período de extração. |
  | QTDACORDOFINALIZADO | Quantidade de contratos do tipo acordo que já foram finalizados, ou seja, que já tiveram todos os seus lançamentos baixados. | **Quantidade de Acordos Recebidos** | + Apenas contratos com **todos os lançamentos baixados**. + **Data da baixa** precisa estar dentro do período de extração. |
  | QTDACORDOARECEBER | Quantidade de contratos do tipo acordo que ainda possuem lançamentos a serem recebidos pela instituição. | **Quantidade de Acordos a Receber** | + Apenas contratos com **lançamentos abertos ou parcialmente baixados**. |

Parametrizador

Existe um parametrizador, dentro do TOTVS Integração, que deve ser configurado para o correto funcionamento da extração dos dados para o GoodData.  
Acesse o parametrizador em: **TOTVS Integração | Ferramentas | Parâmetros | TOTVS Business Analytics | Parâmetros por Empresa | Educacional**.

Observações

* Para conseguir acessar o parametrizador, o perfil do usuário deverá ter permissão de acesso em:  
  **TOTVS Serviços Globais | Segurança | Perfil | Sistema: Integração | Selecione o Perfil | Acesso a Menus | Integração | Ferramentas | Ferramentas | Parâmetros.**
* O parametrizador **funciona por Coligada**, ou seja, cada coligada possui seu parametrizador trabalhando de forma independente.

Atualmente, o Educacional possui os seguintes itens no parametrizador (verificar em cada item, a partir de qual versão ele se encontra disponível):



Abaixo, será apresentado cada item do parametrizador, assim como suas particularidades:

* **Edu - Filial (A partir da versão 12.1.24)**eduparamfilial  
  Nesse item, deverão ser parametrizadas todas as filiais que serão enviadas para o GoodData:  
    
    
    
  **Todas as Filiais serão exibidas para seleção.**

  Observação

  Caso um registro esteja vinculado a uma **filial** que não foi parametrizada na tela acima, ele não será enviado para o GoodData.
* **Edu - Situação de Matrícula de Evasão (A partir da versão 12.1.20)** eduparamsituacaoevasao  
  Nesse item, deverão ser parametrizadas todas as situações de matrícula que indiquem que um aluno evadiu da instituição de ensino:  
    
    
    
  **Regras para a situação de matrícula de evasão ser exibida:**
  + Deve ser uma situação de matrícula parametrizada para ser um **status no períodos letivo** (TOTVS Educacional | Currículo e Oferta | Situação de matrícula | Aba: Status no período letivo | No período letivo) ou um **status no curso** (TOTVS Educacional | Currículo e Oferta | Situação de matrícula | Aba: Status no curso | No curso).
  + A situação de matrícula **não pode estar parametrizada** nos itens ,  e .
* **Edu - Situação de Matrícula de Egresso - Ensino Superior **(A partir da versão 12.1.20)**** eduparamsituacaoegressosuperior  
  Nesse item, deverão ser parametrizadas todas as situações de matrícula que indiquem que um aluno é um egresso (válido apenas para Ensino Superior):

  Observação

  Caso o parâmetro **Considerar a Data de Conclusão de Curso para indicar Egresso do Aluno** estiver marcado, o extrator considerará a data de conclusão no curso, ao invés da Situação de Matrícula parametrizada

  **Regras para a situação de matrícula de egresso ser exibida:**

  + Deve ser uma situação de matrícula parametrizada para ser um **status no curso** (TOTVS Educacional | Currículo e Oferta | Situação de matrícula | Aba: Status no curso | No curso).
  + Deve ser uma situação de matrícula parametrizada para indicar **conclusão do curso** (TOTVS Educacional | Currículo e Oferta | Situação de matrícula | Aba: Status no curso | Indica conclusão do curso).
  + Deve ser uma situação de matrícula criada para o **nível de Ensino Superior**.
  + A situação de matrícula **não pode estar parametrizada** no item .
* **Edu - Situação de Matrícula de Alunos Ativos **(A partir da versão 12.1.20)**** eduparamsituacaoativos  
  Nesse item, deverão ser parametrizadas todas as situações de matrícula que indiquem que um aluno está ativo:  
    
    
    
  **Regras para a situação de matrícula de alunos ativos ser exibida:**  
  + Deve ser uma situação de matrícula parametrizada para ser um **status no períodos letivo** (TOTVS Educacional | Currículo e Oferta | Situação de matrícula | Aba: Status no período letivo | No período letivo).
  + A situação de matrícula **não pode estar parametrizada** no item .
* **Edu - Situação de Matrícula Transferência Interna **(A partir da versão 12.1.20)**** eduparamsituacaotransferenciainterna  
  Nesse item, deverão ser parametrizadas todas as situações de matrícula que indiquem que um aluno realizou uma transferência interna:  
    
    
    
  **Regras para a situação de matrícula de alunos ativos ser exibida:**  
  + Deve ser uma situação de matrícula parametrizada para ser um **status no curso** (TOTVS Educacional | Currículo e Oferta | Situação de matrícula | Aba: Status no curso | No curso).
  + Deve ser uma situação de matrícula parametrizada para indicar **transferência** (TOTVS Educacional | Currículo e Oferta | Situação de matrícula | Aba: Status no curso | Indica transferência).
  + A situação de matrícula **não pode estar parametrizada** para indicar **conclusão do curso** (TOTVS Educacional | Currículo e Oferta | Situação de matrícula | Aba: Status no curso | Indica conclusão do curso).
  + Deve ser uma situação de matrícula criada para o **nível de Ensino Superior**.
  + A situação de matrícula **não pode estar parametrizada** no item .
* **Edu - Curso Educacional **(A partir da versão 12.1.20)**** eduparamcurso  
  Nesse item, deverão ser parametrizadas todos os cursos que serão enviados para o GoodData:  
    
    
    
  **Regras para o curso ser exibido:**  
  + Caso seja um curso de Ensino Superior:
    - No cadastro do curso, o campo **Presencial/Distância** deve estar preenchido.
    - No cadastro do curso, o campo **Modalidade** deve estar preenchido.
    - No cadastro do curso, o campo **Área** deve estar preenchido.
  + Caso seja um curso de Ensino Básico:
    - No cadastro do curso, o campo **Modalidade** deve estar preenchido.Observação

  Caso um registro esteja vinculado a um **curso** que não foi parametrizado na tela acima, ele não será enviado para o GoodData.
* **Edu - Tipo de Documento **(A partir da versão 12.1.20)**** eduparamtipodocumento  
  Nesse item, deverão ser parametrizadas todos os tipos de documentos que serão enviados para o GoodData:  
    
    
    
  **Todos os Tipos de Documento serão exibidos para seleção.**

  Observação

  Caso um registro esteja vinculado a um **tipo de documento** que não foi parametrizado na tela acima, ele não será enviado para o GoodData.
* **Edu - Serviços **(A partir da versão 12.1.20)**** eduparamservicos  
  Nesse item, deverão ser parametrizadas todos os serviços que serão enviados para o GoodData:  
    
    
    
  **Todos os Serviços serão exibidos para seleção.**

  ObservaçãoCaso um registro esteja vinculado a um **serviço** que não foi parametrizado na tela acima, ele não será enviado para o GoodData.
* **Edu - Bolsas **(A partir da versão 12.1.24)**** eduparambolsas  
  Nesse item, deverão ser parametrizadas todas as bolsas que serão enviadas para o GoodData:

  ObservaçãoCaso o parâmetro **Ativa agrupamento de bolsa** esteja marcado, será considerado na extração os agrupamentos de bolsas cadastrados em: **TOTVS Educacional | Integração | Cadastro de Agrupamentos,** dessa forma, os filtros existentes no GoodData exibirão os agrupamentos e não mais todas as bolsas parametrizadas.

  **Todas as Bolsas serão exibidas para seleção.**
* **Edu - Período Letivo** **(A partir da versão 12.1.20)**eduparamperiodoletivo  
  Nesse item, deverão ser parametrizadas todos os períodos letivos que serão enviados para o GoodData:

  ObservaçãoCaso o parâmetro **Ativa agrupamento de períodos letivos** esteja marcado, será considerado na extração os agrupamentos de períodos letivos cadastrados em: **TOTVS Educacional | Integração | Cadastro de Agrupamentos,** dessa forma, os filtros existentes no GoodData exibirão os agrupamentos e não mais todos os períodos letivos parametrizados.

  **Regras para o período letivo ser exibido:**

  + No cadastro do período letivo o campo Data de Início, deve estar preenchido.
  + No cadastro do período letivo o campo Data de Término, ou Previsão de Término, deve estar preenchido.ObservaçãoCaso um registro esteja vinculado a um **período letivo** que não foi parametrizado na tela acima, ele não será enviado para o GoodData.
* **Edu - Situação de Matrícula de Egresso - Ensino Básico **(A partir da versão 12.1.20)**** eduparamsituacaoegressobasico  
  Nesse item, deverão ser parametrizados todos os períodos letivos que serão enviados para o GoodData:  
    
    
    

  **Regras para a situação de matrícula de egresso ser exibida:**

  + Deve ser uma situação de matrícula parametrizada para ser um **status no períodos letivo** (TOTVS Educacional | Currículo e Oferta | Situação de matrícula | Aba: Status no período letivo | No período letivo).
  + Deve ser uma situação de matrícula criada para o **nível de Ensino Básico**.
  + A situação de matrícula **não pode estar parametrizada** no item .
* **Edu - Última Série Egresso - Ensino Básico **(A partir da versão 12.1.20)**** eduparamultimaserie  
  Nesse item, deverão ser parametrizados os registros da última série do ensino básico ofertada pela instituição:  
    
    
    

  **Regras para a série ser exibida:**

  + Deve ser uma série criada para o **nível de Ensino Básico**.
* **Edu - Data Faturamento **(A partir da versão 12.1.21)**** eduparamdatafaturamento  
  Nesse item, deverá ser escolhido qual data será considerada para definição do faturamento:
* **Edu - Inadimplência **(A partir da versão 12.1.21)**** eduparaminadimplencia  
  Nesse item, deverá ser parametrizado o quantidade de dias de carência após o vencimento, para que o extrator não considere como inadimplência:  
    
    
    
  **Exemplo:**Supondo que a data de vencimento do lançamento seja: **06/08/2018**, mas o parâmetro esteja com o valor **5**, então o lançamento só será considerado para inadimplência após o dia **11/08/2018**.

faqFAQ

**FAQ - Perguntas frequentes sobre a extração no Fast Analytics**

**Por que alguns cursos não são exibidos no parametrizador do Fast Analytics?**  
Existem algumas regras que determinam quais status, cursos, períodos letivos serão exibidos no parametrizador de extração do Fast Analytics. Para mais informações sobre essas regras deve-se acesso a aba de "Parametrizador" existente nessa documentação sobre o Fast Analytics.

**Após executar uma extração os dados não são exibidos no Gooddata.**  
Existem alguns pontos que devem ser verificados nesse caso:

1º) Verificar se o valor dos parâmetros referente a data de início e fim de extração estão entre "aspas simples" (apenas para os casos que a data está fixa):

param.EXTRACAO\_PERIODO\_DATA\_INICIAL='20180701'  
param.EXTRACAO\_PERIODO\_DATA\_FINAL='20181031'

2º) Acessar o log de extração e verificar se ocorreu algum erro no processo de extração (dica: fazer uma busca no arquivo pela palavra "erro").  
3º) Caso nenhum erro tenha sido encontrado, no final do log existe um link para o local na nuvem onde os arquivos .csv são gerados e lidos pelo Gooddata. Acesse esse link e baixe o arquivo .zip existente nele. Dentro desse arquivo encontramos o .csv relacionado com a fato que está sendo extraída (além do .csv de dimensões e outras fatos). Abra o arquivo .csv e verifique se existem registros.

O link para o local onde os arquivos .csv são gerados está presente no log de extração no seguinte formato: < INFO> Main: Arquivos de dados enviados para o GoodData: Para: <https://na1-di.gooddata.com/project-uploads/ln7evkc6qxrz8jno5wn6s7rs0aqmvilm/today/>

4º) Caso existam registros no arquivo .csv, o próximo passo será acessar o log do Gooddata para verificar se ocorreu algum erro durante a execução do ETL.

O link para o log do ETL estará presente no log da extração no seguinte formato: < INFO> Main: Log de execução: URL: <https://analytics.totvs.com.br/gdc/projects/ln7evkc6qxrz8jno5wn6s7rs0aqmvilm/dataload/processes/cbdf451a-7abd-4d8a-b796-4a110538c409/executions/5c9529d5e4b04ed3daaaddc0/log>

5º) No último caso, deve ser verificado os relatórios no projeto do Gooddata que está sendo extraído as informações em busca de algum erro de semântica.

**O seguinte erro é exibido no log de extração:**

*<ERROR> "Error 404 :: Not Found"*  
Verificar se o id do projeto foi informado corretamente na propriedade "gdc.upload\_url" do my.properties

**O seguinte erro é exibido no log de extração:**

*<ERROR> Main: Erro ao conectar no banco de dados*

- Verificar se o usuário e senha de acesso ao banco de dados estão corretos (fazer um teste logando diretamente na base da dados utilizando o mesmo usuário).

- Caso as senhas informadas no my.properties estejam criptografadas, a propriedade **gdc.crypto** deve ser igual a TRUE.

**O seguinte erro é exibido no log de extração:**  
*<ERROR> GdcRESTApiWrapper: Error 404 :: Not Found*  
*<ERROR> GdcRESTApiWrapper: Graph RM - Educacional/graph/Main\_Educacional.grf não encontrado no processo de ETL*   
*Processo: [https://analytics.totvs.com.br/gdc/projects/ln7evkc6qxrz8jno5wn6s7rs0aqmvilm/dataload/processes/cbdf451a-7abd-4d8a-b796-4a110538c409–/](https://analytics.totvs.com.br/gdc/projects/ln7evkc6qxrz8jno5wn6s7rs0aqmvilm/dataload/processes/cbdf451a-7abd-4d8a-b796-4a110538c409--/)*  
*<DEBUG> GdcRESTApiWrapper: Process cbdf451a-7abd-4d8a-b796-4a110538c409-- not found.*

Verificar se o id do processo foi informado corretamente na propriedade "gdc.etl.process\_url" do my.properties.

**O seguinte erro é exibido no log de extração:**  
*<ERROR> GdcRESTApiWrapper: Graph RM2 - Educacional/graph/Main\_Educacional.grf não encontrado no processo de ETL*   
*Processo: <https://analytics.totvs.com.br/gdc/projects/ln7evkc6qxrz8jno5wn6s7rs0aqmvilm/dataload/processes/cbdf451a-7abd-4d8a-b796-4a110538c409/>*  
*<DEBUG> GdcRESTApiWrapper: Executable RM2 - Educacional/graph/Main\_Educacional.grf not found in process cbdf451a-7abd-4d8a-b796-4a110538c409*  
Verificar se o caminho dos graphs foi informado corretamente na propriedade "gdc.etl.graph".

Dica: Uma maneira para descobrir o caminho correto é acessando o projeto do cliente no Gooddata | Administrar | Integração de Dados | Download. Após baixar o arquivo zip, navegar até a pasta "graph" (o caminho apresentado é o que deve ser inserido na propriedade).

**Não é possível configurar mais de 200 itens em uma variável no Gooddata?**  
A plataforma do Gooddata não permite a seleção de mais de 200 itens ao configurar uma variável. Nesse caso, será necessário configurar 200 itens na variável existente e, para os itens restante, criar uma nova variável. Após a criação, será necessário alterar todas as métricas que utilizam a variável V para incluir a utilização da variável V2.

**Qual a diferença entre carga utilizando a propriedade FULL\_LOAD e INCREMENTAL no my.properties?**  
Na extração FULL\_LOAD, todos os dados da nuvem do GoodData serão apagados para inserir a nova carga. Já na extração INCREMENTAL, apenas os dados do período da extração serão excluídos.

**Por que as informações no GoodData não chegam ao nível de detalhamento de alunos?**

Os gráficos exibidos no GoodData não chegam ao nível operacional pois eles exibem informações gerenciais.  Para esse conceito ficar mais claro, é importante sabermos a diferença entre um relatório operacional e as informações geradas por uma ferramento de Business Intelligence (BI):

O Fast Analytics é uma ferramenta completa de BI para auxílio à tomada de decisões, monitoramento e planejamento. Um relatório operacional apenas exibe os dados brutos, ou com pouco processamento para tratar uma demanda específica e geralmente operacional. Uma ferramenta de Business Intelligence é um processo que consiste na extração, consolidação e transformação de dados brutos em informações relevantes.

Para exemplificar a transformação feita durante esse processo, vamos considerar as informações sobre os alunos (ativos, evasão, egresso, etc). Elas são geradas pelo Fast Analytics considerando regras sobre o status, data de matrícula e/ou data de alteração da matrícula, datas do período letivo, etc., com visões por coligada, filial, nível de ensino, curso, dentre outras. Conforme explicado acima, mais do que saber quais são os alunos que evadiram da instituição, uma ferramenta de BI entrega informações relevantes para entender melhor o histórico da evasão, acompanhar a evolução e elaborar as melhores estratégias de retenção.

**O seguinte erro é exibido no log de extração:**  
*<DEBUG> GdcRESTApiWrapper: ETL error, see log file...*

Um nos prováveis motivos para o erro é a existência de um espaço em branco, antes ou depois, das palavras INCREMENTAL ou FULL\_LOAD, nas tags gdc.etl.param.LOAD\_MODE\_FCT ou gdc.etl.param.LOAD\_MODE\_DIM, dentro do(s) arquivo(s) myProperties.

**O seguinte erro é exibido no log de extração, porém não existe nenhum lugar no script que possua esse caractere de forma incorreta:**  
*Incorrect syntax near '/'.*

Caso de fato não exista nenhum lugar nos scripts de extração que justifique esse erro, provavelmente ele está sendo ocasionado por existir, na frente das datas de início e fim de extração (tags: param.EXTRACAO\_PERIODO\_DATA\_INICIAL  
param.EXTRACAO\_PERIODO\_DATA\_FINAL), dentro do(s) arquivo(s) myProperties a tentativa de um texto comentado, utilizando os caracteres // . Para o correto funcionamento da extração, não se pode colocar nenhum informação após a data informada nas tags.

**Por que os filtros de um dashboard no GoodData não estão sendo aplicados em um ou mais indicadores existentes nesse mesmo dashboad?**

Nesse caso deve-se verificar se o indicador está configurado para ser restringido pelos filtros do dashboard: Editar o dashboard, clicar no ícone de "engrenagem" | filtros e marcar os filtros que afetarão o indicador

indicadoresIndicadores

**OBSERVAÇÃO:**

Para as fatos de Aluno, Contabilidade e Financeiro (com exceção da aba de Lançamentos Recebidos), os dados possuem uma granularidade mensal, ou seja, os dados são extraídos tendo meses como referência e não dias.   
Por isso, deve utilizar-se o seguinte componente de data:  
  
  
  
Abaixo estão descritos os indicadores criados para o Educacional:

eduindicadoreseduindicalunosAlunos

| Indicador | Definição | Cálculo do Indicador |
| --- | --- | --- |
| ativosAlunos ativos | Quantidade de alunos ativos. Um aluno é considerado ativo quando está regularmente matriculado em um curso. | Valor no ÚLTIMO mês do período selecionado |
| baseAlunos da Base | Quantidade de alunos ativos no mês anterior ao período de datas selecionado. | Valor no ÚLTIMO mês do período selecionado |
| novosNovos alunos | Quantidade de novos alunos que ingressaram no primeiro período/série da instituição de ensino | Valor no ÚLTIMO mês do período selecionado |
| transfEntradaTransferência Interna Entrada | Quantidade de transferências internas de entrada em cursos. Uma transferência interna ocorre quando um aluno muda de curso, turno, filial ou habilitação. | Valor no ÚLTIMO mês do período selecionado |
| transfSaidaTransferência Interna Saída | Quantidade de transferências internas de saídas de cursos. Uma transferência interna ocorre quando um aluno muda de curso, turno, filial ou habilitação. | Valor no ÚLTIMO mês do período selecionado |
| formadosFormados | Quantidade de alunos formados | Valor no ÚLTIMO mês do período selecionado |
| bolsistasBolsistas | Quantidade de alunos ativos na instituição que possuem algum tipo de bolsa ou FIES ativos. | Valor no ÚLTIMO mês do período selecionado |
| evasaoEvasão | Percentual de evasão. Um aluno é considerado evasor quando começou a frequentar as aulas de um curso e o abandonou posteriormente | onde:  **∑evasores**: soma dos evasores no período selecionado  **renovações**: alunos que renovaram matrícula no período selecionado |

# Observações

* **Painel Alunos:**
  1. Presencial: fração de  que corresponde a cursos presenciais;
  2. EAD: fração de  que corresponde a cursos EAD;
  3. %Var. Mês Anterior: variação de , no último mês do período selecionado, em relação ao mês anterior;
  4. %Var. Ano Anterior: variação de , no último mês do período selecionado, em relação ao mesmo mês do ano anterior.

* **Evolução do número de alunos:** a categoria outros representa o total de alunos que não se enquadram nos outros casos como, por exemplo, renovação e transferência interna não registrada. Transferência interna não registrada é quando sua entrada ou saída não consta no log de alteração de matrícula)

* **Painel Bolsistas:**
  1. Percentual de Bolsistas: percentual de em relação aos .
  2. FIES: percentual  que possuem FIES.
  3. %Var. Mês Anterior: variação de  no último mês do período selecionado, em relação ao mês anterior.
  4. %Var. Ano Anterior: variação de  no último mês do período selecionado, em relação ao mesmo mês do ano anterior.

* **Painel de Evasão:**
  1. Presencial: percentual de  de cursos presenciais;
  2. EAD: percentual de  nos cursos de EAD;
  3. %Var. Mês Anterior: total de no período selecionado em relação ao mês anterior.
  4. %Var. Ano Anterior: total de no período selecionado em relação ao mesmo período do ano anterior.

eduindiccontabilidadeContabilidade

| Indicador | Definição | Cálculo do Indicador |
| --- | --- | --- |
| receitabrutaReceita Bruta | Valor da receita bruta de vendas e serviços na instituição de ensino. | Valor ACUMULADO no período selecionado |
| outrasreceitasOutras Receitas | Outras receitas operacionais da instituição de ensino. | Valor ACUMULADO no período selecionado |
| receitaliquidaReceita Líquida | Valor da receita líquida da instituição de ensino no período de datas selecionado. | onde: **receita bruta total** = receita bruta + outras receitas; **perdas** = perdas estimadas em créditos de liquidação duvidosa; **bolsas** = despesas bolsas/gratuidades |
| pecldPECLD | Percentual de comprometimento da receita bruta da instituição de ensino com perdas estimadas em créditos de liquidação duvidosa no período de datas selecionado. | onde:   **perdas** = perdas estimadas em créditos de liquidação duvidosa; |
| despesasdocenteDespesas folha docente | Despesas com folha de pagamento do corpo docente da instituição de ensino. | Valor ACUMULADO no período selecionado |
| despesasadmDespesas folha administrativa | Despesas com folha de pagamento do administrativo da instituição de ensino. | Valor ACUMULADO no período selecionado |
| outrasdespesasOutras despesas | Despesas operacionais da instituição de ensino. | Valor ACUMULADO no período selecionado |
| despesasDespesas | Despesas da instituição de ensino no período selecionado. | Despesas folha docente + despesas folha administrativa + outras despesas |
| despesasbolsasDespesas bolsas / gratuidades | Despesas antecipadas com bolsas/gratuidades no período selecionado. | Valor ACUMULADO no período selecionado |
| rentabilidadepercRentabilidade (%) | Percentual da rentabilidade geral bruta (LAJIDA) da instituição de ensino no período selecionado. |  |
| rentabilidadevalorRentabilidade (R$) | Valor de rentabilidade da instituição de ensino no período selecionado. | receita líquida - despesas |

# Observações

* **Painel Receita Bruta (R$)**
  1. %Bolsas: valor das  em relação a ;
  2. %Var. Ano Anterior: variação da , no período selecionado, em relação ao mesmo período do ano anterior
* **Painel Receita Líquida (R$)**
  1. %Var. Ano Anterior: variação da , no período selecionado, em relação ao mesmo período do ano anterior.
* **Painel PECLD**
  1. Presencial: fração da que corresponde a cursos presenciais;
  2. EAD: fração da que corresponde a cursos EAD;
  3. %Var. Ano Anterior: variação da , no período selecionado, em relação ao mesmo período do ano anterior.
* **Painel Despesas**
  1. Evolução das despesas totais: , no período selecionado, em relação ao mesmo período no ano anterior;
  2. Folha Docente x RL: despesas  em relação à ;
  3. Folha Administrativa x RL: em relação à ;
  4. Outras despesas x RL: em relação à .
* **Painel Rentabilidade (R$)**
  1. %Var. Ano Anterior: variação da , no período selecionado, em relação ao mesmo período do ano anterior;
  2. Valor: valor da .
eduindicfinanceiroFinanceiro

| Indicador | Definição | Cálculo do Indicador |
| --- | --- | --- |
| edufaturamentoFaturamento | Somatório de todas as receitas prevista pela instituição de ensino. | Valor ACUMULADO no período selecionado |
| eduinadimplenciaInadimplência | Descumprimento de uma obrigação financeira com a instituição de ensino, como o não pagamento de um bem ou serviço. | Valor ACUMULADO no período selecionado |
| edulancamentosareceberLançamentos a receber | São os direitos de recebimento de valores que a instituição tem, seja com outra empresa ou pessoa. | Valor ACUMULADO no período selecionado |
| edulancamentosrecebidosLançamentos recebidos | São os direitos já recebidos pela instituição, de outras empresas ou pessoas. | Valor ACUMULADO no período selecionado. |
| eduticketmedioTicket Médio | É um indicador de performance de vendas, que fornece o valor médio das mensalidades da instituição. | onde:  **SM** = Somatório do valor das mensalidades. **QtdA** = Quantidade total de alunos ativos. **QtdAF** = Quantidade total de alunos formados. |
| edubolsasBolsas | É um desconto no valor da mensalidade oferecido por instituições de ensino, que pode ser parcial ou total. | Valor ACUMULADO no período selecionado. |
| edufiesFIES | É um programa cujo objetivo é financiar a graduação de Ensino Superior de estudantes que não possuem condições de arcar com os custos de sua formação. | Valor ACUMULADO no período selecionado. |
| edualunoacordoAlunos com acordo | São alunos que realizaram acordo na instituição de ensino. | Valor ACUMULADO no período selecionado. |
| eduacordoAcordo | É uma modalidade de negociação, que consiste em formalizar um novo plano de pagamento para os lançamentos financeiros. | Valor ACUMULADO no período selecionado. |
| eduacordovigenteAcordo vigente | São acordos que possuem pelo menos um lançamento em aberto. | Valor ACUMULADO no período selecionado. |
| eduacordofinalizadoAcordo finalizado | São acordos que possuem todos seus lançamentos finalizados. | Valor ACUMULADO no período selecionado. |

# Observações

* **Painel Faturamento:**
  1. Total de Bolsas: valor total do  com bolsas.
  2. %Var. Ano Anterior: variação, em porcentagem, do total de , no último mês do período selecionado, em relação ao mesmo mês do ano anterior.
  3. Variação (bolsas): indica a porcentagem que o valor de bolsas faturadas representam em relação ao valor total faturado.

* **Painel Ticket Médio:**
  1. Faturamento relacionado: valor do faturamento considerado para cálculo do  da instituição de ensino.
  2. %Var. Mês Anterior: variação, em porcentagem, do valor do , no último mês do período selecionado, em relação ao mês anterior.
  3. %Var. Ano Anterior. variação, em porcentagem, do valor do , no último mês do período selecionado, em relação ao mesmo mês do ano anterior.
* **Painel Inadimplência:**
  1. %Var. Ano Anterior: variação, em porcentagem, do valor da , no último mês do período selecionado, em relação ao mesmo mês do ano anterior.
  2. %Var. de Acordo: indica a porcentagem de acordos inadimplentes, em relação ao valor total da inadimplência.
* **Painel Lançamentos a receber:**
  1. %Var. Faturamento: indica a porcentagem que os  que equivalem em relação ao valor total do faturamento.
  2. %Var. de Acordo: indica a porcentagem que os acordos a receber que equivalem em relação ao valor total da inadimplência.
* **Painel Lançamentos recebidos:**
  1. %Var. Ano Anterior: indica a evolução do  no período selecionado, comparado ao ano anterior.
* **Painel Bolsas e FIES:**
  1. %Var. Ano Anterior: indica a evolução do valor total de +  oferecido no período selecionado, comparado ao ano anterior.
  2. Quantidade: Quantidade de  +  oferecidas no período selecionado
* **Painel Bolsas:**
  1. %Var. Ano Anterior: indica a evolução do valor total de  oferecido no período selecionado, comparado ao ano anterior.
  2. Quantidade: Quantidade de  oferecidas no período selecionado.
* **Painel FIES:**
  1. %Var. Ano Anterior: indica a evolução do valor total de  oferecido no período selecionado, comparado ao ano anterior.
  2. Quantidade: Quantidade de  oferecidas no período selecionado.

* **Painel Total de alunos com acordo:**
  1. %Var. Mês Anterior: variação, em porcentagem, da quantidade de , no último mês do período selecionado, em relação ao mês anterior.
  2. %Var. Ano Anterior: variação, em porcentagem, da quantidade de , no último mês do período selecionado, em relação ao mesmo mês do ano anterior.
* **Painel Acordo:**
  1. %Var. Mês Anterior: variação, em porcentagem, da quantidade de , no último mês do período selecionado, em relação ao mês anterior.
  2. %Var. Ano Anterior: variação, em porcentagem, da quantidade de , no último mês do período selecionado, em relação ao mesmo mês do ano anterior.
* **Painel Acordo Vigente:**
  1. %Var. Mês Anterior: variação, em porcentagem, da quantidade de , no último mês do período selecionado, em relação ao mês anterior.
  2. %Var. Ano Anterior: variação, em porcentagem, da quantidade de , no último mês do período selecionado, em relação ao mesmo mês do ano anterior.
* **Painel Acordo Finalizado:**
  1. %Var. Mês Anterior: variação, em porcentagem, da quantidade de , no último mês do período selecionado, em relação ao mês anterior.
  2. %Var. Ano Anterior: variação, em porcentagem, da quantidade de , no último mês do período selecionado, em relação ao mesmo mês do ano anterior.

rhRHFast Analytics RM RH01envelope\_de\_pagamentoEnvelope de PagamentoEnvelope de Pagamento

Este dashboard permite visualizar dos KPIs de pagamento, com a possibilidade de realizar o filtro entre empresa, filiais, seções, departamento e etc. Podendo ter uma Análise Geral, Evolução e Ranking relativos aos pagamentos líquido, descontos, proventos, base de cálculos e previsões do envelope.

Os indicadores exibidos são quebrados periodicamente conforme os filtros aplicados. Os filtros utilizados neste dashboard são:

* **Date (Data de competência):** Informe a Data Início e Data Fim das quais deseja extrair as informações, sendo que a Data Fim deve ser obrigatoriamente maior que a Data Início.
* **Empresa:** Empresa(s) que deseja extrair os indicadores.
* **Filial:** Filial(ais) que deseja extrair os indicadores.
* **Seção:** Selecione a(s) Seção(ões) que deseja extrair os indicadores.
* **Centro de Custo:** Selecione o(s) Centro(s) de Custo que deseja extrair os indicadores.
* **Departamento:** Selecione o(s) Departamento(s) dos quais deseja extrair os indicadores.

01.01analise\_geralAnálise GeralPagamento Envelope - Análise Consolidada

Neste painel, ao clicar em um dos valores/ percentuais apresentados, o sistema demonstrará o detalhamento do mesmo. Este detalhamento será apresentado em forma de Tabela, podendo o usuário visualiza-lo também em formato de gráfico (Linha, Barras ou Pizza).

* **Valor Líquido Pagamento:** Dados os filtros acima, será somado de todos os valores valores líquidos (diferença entre proventos e descontos) no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todas as empresas com o valor líquido pagamento, valor provento pagamento, valor desconto pagamento, valor líquido férias, valor provento férias, valor desconto férias, banco de horas e hora extra.

* **Valor Provento Pagamento:**Dados os filtros acima, será somado todos os valores de proventos no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todas as empresas com o valor líquido pagamento, valor provento pagamento, valor desconto pagamento, valor líquido férias, valor provento férias, valor desconto férias, banco de horas e hora extra.

* **Valor Desconto Pagamento:** Dados os filtros acima, será somado de todos os valores de descontos no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todas as empresas com o valor líquido pagamento, valor provento pagamento, valor desconto pagamento, valor líquido férias, valor provento férias, valor desconto férias, banco de horas e hora extra.

* **Valor Base Cálculo:** Dados os filtros acima, será somado de todos os valores de base de cálculo e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação.

* **Quantidade de****Funcionários****:**Dados os filtros acima, será somado de todos os funcionários e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação.

evolucaoEvoluçãoEvolução Pagamento Envelope

**Evolução Pagamento Envelope**

Demonstra a variação dos pagamentos entre os meses, variações em quantidade de funcionários e a previsão de pagamento para os próximos meses.

* **Valor Líquido Pago x Qtd. Funcionários:** Representação gráfica do total do valor líquido pago em relação a quantidade de funcionário mensalmente. As barras representam o valor (em milhões) dos valores líquido no mês. A linha representa a quantidade de funcionários do mês.

* **Valor Provento Pago x Qtd. Funcionários:**Representação gráfica do total do valor de provento pago em relação a quantidade de funcionário mensalmente. As barras representam o valor (em milhões) dos valores de provento no mês. A linha representa a quantidade de funcionários do mês.

* **Valor Desconto Pgto x Qtd. Funcionários:**Representação gráfica do total do valor de desconto pago em relação a quantidade de funcionário mensalmente. As barras representam o valor (em milhões) dos valores de desconto no mês. A linha representa a quantidade de funcionários do mês.

* **Valor Base Calc. Envelope x Qtd. Funcionários:**Representação gráfica do total do valor de base de cálculo pago no envelope em relação a quantidade de funcionário mensalmente. As barras representam o valor (em milhões) dos valores de base de cálculo no mês. A linha representa a quantidade de funcionários do mês.

* **Previsão de Pagamento Líquido:** Representação gráfica da previsão do pagamento líquido mensalmente. A linha representa a quantidade de funcionários do mês. A previsão é estimada na regressão linear de 4 períodos futuros com base nos dados existentes.

RankingRankingRanking

**Ranking**

Demonstra os principais pagantes por empresa, funcionário e filial.

* **TOP 10 Seções:**Representação gráfica dos 10 maiores valores de pagamento do valor líquido por seção. A barra representa o valor líquido pago por seção e a linha representa a quantidade total de funcionários da seção.

Ao clicar na seção, é exibido um gráfico com as funções da seção selecionada. A barra representa o valor líquido pago por função e a linha representa a quantidade total de funcionários da função.

Ao clicar na função, é exibido um gráfico com os funcionários da função selecionada. A barra representa o valor líquido pago por funcionário e a linha representa a quantidade total de funcionários.

* ****TOP 10 Departamentos:****Representação gráfica dos 10 maiores valores de pagamento do valor líquido por departamento. A barra representa o valor líquido pago por departamento e a linha representa a quantidade total de funcionários do departamento.

Ao clicar no departamento, é exibido um gráfico com os centro de custo do departamento selecionado. A barra representa o valor líquido pago por centro de custo e a linha representa a quantidade total de funcionários do departamento.

Ao clicar no centro de custo, é exibido um gráfico com as funções do centro de custo selecionado. A barra representa o valor líquido pago por função e a linha representa a quantidade total de funcionários do centro de custo.

Ao clicar na função, é exibido um gráfico com os funcionários da função selecionada. A barra representa o valor líquido pago por funcionário e a linha representa a quantidade total de funcionários.

* **Ranking por Filial:** Representação gráfica do ranking por filial apresentado o valor líquido pago, percentual em cima do valor total e o percentual acumulado por filial

Ao clicar no nome da filial, é exibido um detalhamento dos departamentos da filial selecionada.

Ao clicar no nome do departamento, é exibido um detalhamento dos centros de custo do departamento selecionado.

Ao clicar no nome do centro de custo, é exibido um detalhamento das funções do centro de custo selecionado.

Ao clicar no nome da função, é exibido um detalhamento dos funcionários da função selecionada.

envelope\_feriasEnvelope FériasEnvelope Férias

Este dashboard permite visualizar dos KPIs de pagamento  de envelope de férias, com a possibilidade de realizar o filtro entre empresa, filiais, seções, departamento e etc. Podendo ter uma Análise Geral, Evolução e Ranking relativos aos pagamentos líquido, descontos, proventos, base de cálculos e previsões do envelope.

Os indicadores exibidos são quebrados periodicamente conforme os filtros aplicados. Os filtros utilizados neste dashboard são:

* **Date (Data de competência):** Informe a Data Início e Data Fim das quais deseja extrair as informações, sendo que a Data Fim deve ser obrigatoriamente maior que a Data Início.
* **Empresa:** Empresa(s) que deseja extrair os indicadores.
* **Filial:** Filial(ais) que deseja extrair os indicadores.
* **Seção:** Selecione a(s) Seção(ões) que deseja extrair os indicadores.
* **Centro de Custo:** Selecione o(s) Centro(s) de Custo que deseja extrair os indicadores.
* **Departamento:** Selecione o(s) Departamento(s) dos quais deseja extrair os indicadores.

01.02analise\_geral\_feriasAnálise GeralEnvelope Férias - Análise Consolidada

Neste painel, ao clicar em um dos valores/ percentuais apresentados, o sistema demonstrará o detalhamento do mesmo. Este detalhamento será apresentado em forma de Tabela, podendo o usuário visualiza-lo também em formato de gráfico (Linha, Barras ou Pizza).

* **Valor Líquido de Férias:**Dados os filtros acima, será somado de todos os valores líquidos de férias (diferença entre proventos e descontos) no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o valor líquido férias, valor provento férias, valor desconto férias, valor de base de cálculo férias e quantidade de funcionários por pagamento de férias. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **Valor Provento Férias:**Dados os filtros acima, será somado todos os valores de proventos de férias no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o valor líquido férias, valor provento férias, valor desconto férias, valor de base de cálculo férias e quantidade de funcionários por pagamento de férias. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **Valor Desconto Férias:**Dados os filtros acima, será somado todos os valores de descontos de férias no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o valor líquido férias, valor provento férias, valor desconto férias, valor de base de cálculo férias e quantidade de funcionários por pagamento de férias. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **Valor Base Cálculo Férias:**Dados os filtros acima, será somado todos os valores de base de cálculo de férias no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o valor líquido férias, valor provento férias, valor desconto férias, valor de base de cálculo férias e quantidade de funcionários por pagamento de férias. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **Quantidade de Funcionários Pagos:**Dados os filtros acima, será somado de todos os funcionários e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o valor líquido pagamento, valor provento pagamento, valor desconto pagamento, valor líquido férias, valor provento férias, valor desconto férias, banco de horas e hora extra. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

evolucao\_feriasEvoluçãoEvolução Pagamento Envelope/Férias

* **Valor Líquido de Férias x Quantidade Funcionários:** As barras representam o valor líquido de férias no mês. O mês central é o mês selecionado e sempre será mostrado o mês anterior e o posterior. A linha representa a quantidade de funcionários naquele mês.

* **Valor Provento de Férias x Quantidade Funcionários:** As barras representam o valor de provento de férias no mês. O mês central é o mês selecionado e sempre será mostrado o mês anterior e o posterior. A linha representa a quantidade de funcionários naquele mês.

* **Valor Desconto de Férias x Quantidade Funcionários:** As barras representam o valor de desconto de férias no mês. O mês central é o mês selecionado e sempre será mostrado o mês anterior e o posterior. A linha representa a quantidade de funcionários naquele mês.

* **Valor Base Cálculo de Férias x Quantidade Funcionários:** As barras representam o valor de base de cálculo de férias no mês. O mês central é o mês selecionado e sempre será mostrado o mês anterior e o posterior. A linha representa a quantidade de funcionários naquele mês.

* **Previsão de pagamento de Férias Líquido:** Representação gráfica da previsão do pagamento líquido mensalmente. A linha representa a quantidade de funcionários do mês. A previsão é estimada com base nos dados existentes.

ranking\_feriasRankingRanking Férias

* **TOP 10 Seções:**Representação gráfica dos 10 maiores valores de pagamento do valor de férias líquido por seção. A barra representa o valor de férias líquido pago por seção e a linha representa a quantidade total de funcionários da seção.

Ao clicar na seção, é exibido um gráfico com as funções da seção selecionada. A barra representa o valor de férias líquido pago por função e a linha representa a quantidade total de funcionários da função.

Ao clicar na função, é exibido um gráfico com os funcionários da função selecionada. A barra representa o valor de férias líquido pago por funcionário e a linha representa a quantidade total de funcionários.

* ****TOP 10 Departamentos:****Representação gráfica dos 10 maiores valores de pagamento do valor de férias líquido por departamento. A barra representa o valor de férias líquido pago por departamento e a linha representa a quantidade total de funcionários do departamento.

Ao clicar no departamento, é exibido um gráfico com os centro de custo do departamento selecionado. A barra representa o valor de férias líquido pago por centro de custo e a linha representa a quantidade total de funcionários do departamento.

Ao clicar no centro de custo, é exibido um gráfico com as funções do centro de custo selecionado. A barra representa o valor de férias líquido pago por função e a linha representa a quantidade total de funcionários do centro de custo.

Ao clicar na função, é exibido um gráfico com os funcionários da função selecionada. A barra representa o valor de férias líquido pago por funcionário e a linha representa a quantidade total de funcionários.

* **Ranking por Filial:**Representação gráfica do ranking por filial apresentado o valor de férias líquido pago, percentual em cima do valor total e o percentual acumulado por filial. Na linha final há uma linha com o total de todas filiais.

Ao clicar no nome da filial, é exibido um detalhamento dos departamentos da filial selecionada.

Ao clicar no nome do departamento, é exibido um detalhamento dos centros de custo do departamento selecionado.

Ao clicar no nome do centro de custo, é exibido um detalhamento das funções do centro de custo selecionado.

Ao clicar no nome da função, é exibido um detalhamento dos funcionários da função selecionada.

painel\_geralPainel GeralPainel Geral

Este dashboard permite visualizar os KPIs de banco de horas, com a possibilidade de realizar o filtro entre empresa, filiais, seções, departamento e etc. Podendo ter uma relação do banco de horas por faltas e atrasos, horas trabalhadas por horas extras pagas, envelope de pagamento e pagamento de férias.

Os indicadores exibidos são quebrados periodicamente conforme os filtros aplicados. Os filtros utilizados neste dashboard são:

* **Date (Data de competência):** Informe a Data Início e Data Fim das quais deseja extrair as informações, sendo que a Data Fim deve ser obrigatoriamente maior que a Data Início.
* **Empresa:** Empresa(s) que deseja extrair os indicadores.
* **Filial:** Filial(ais) que deseja extrair os indicadores.
* **Seção:** Selecione a(s) Seção(ões) que deseja extrair os indicadores.
* **Centro de Custo:** Selecione o(s) Centro(s) de Custo que deseja extrair os indicadores.
* **Departamento:** Selecione o(s) Departamento(s) dos quais deseja extrair os indicadores.

01.03banco\_horas\_x\_atraso\_faltasBanco de Horas X Atraso e FaltasBanco de Horas X Atraso e Faltas

* **Banco de Horas:**Dados os filtros acima, será somado o banco de horas de todos, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o banco de horas, horas extras atual e horas de atraso. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **Total Hora Extra:**Dados os filtros acima, será somado o banco de horas extras de todos, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o banco de horas, horas extras atual e horas de atraso. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **Total Atraso e Falta:**Dados os filtros acima, será somado o banco de horas de atraso e falta de todos, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o banco de horas, horas extras atual e horas de atraso. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **Hora Extra X Atraso e Falta (em horas):**Representação gráfica da total de horas em relação às horas extras e de atrasos e faltas. As barras azul e cinza, representam o valor de horas de Atraso/Falta e Extra, respectivamente e a linha representa a quantidade total de horas.

* **Representatividade:**Representação gráfica da porcentagem da hora extra e de atrasos e faltas em relação ao total de horas no banco. A cor cinza representa a Hora Extra e a cor azul representa as horas de Atraso e Falta.

horas\_trabalhadas\_x\_horas\_extras\_pagasHoras Trabalhadas X Horas Extras PagasHoras Trabalhadas X Horas Extras Pagas

* **Quantidade de Horas Trabalhadas:**Dados os filtros acima, será somado todas as horas trabalhadas no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o valor de quantidade de horas trabalhadas, quantidade de horas extras e o percentual de horas extras por trabalhadas. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **Quantidade de Horas Extras Pagas:**Dados os filtros acima, será somado todas as horas extras pagas no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o valor de quantidade de horas trabalhadas, quantidade de horas extras e o percentual de horas extras por trabalhadas. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **% Horas Extras x Trabalhadas:**Dados os filtros acima, será calculado o percentual das horas extras por horas trabalhadas no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o valor de quantidade de horas trabalhadas, quantidade de horas extras e o percentual de horas extras por trabalhadas. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **Hora Extra X Atraso e Falta (em horas):** Representação gráficas da relação entre as horas extras x trabalhadas, horas trabalhadas e horas extra pagas.

pagamento\_envelope\_evolucaoPagamento Envelope - EvoluçãoPagamento Envelope - Evolução

* **Valor Líquido Pagamento:**Dados os filtros acima, será somado de todos os valores valores líquidos (diferença entre proventos e descontos) no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todas as empresas com o valor líquido pagamento, valor provento pagamento, valor desconto pagamento, valor líquido férias, valor provento férias, valor desconto férias, banco de horas e hora extra.

* **Valor Provento Pagamento:**Dados os filtros acima, será somado todos os valores de proventos no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todas as empresas com o valor líquido pagamento, valor provento pagamento, valor desconto pagamento, valor líquido férias, valor provento férias, valor desconto férias, banco de horas e hora extra.

* **Valor Desconto Pagamento:**Dados os filtros acima, será somado de todos os valores de descontos no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todas as empresas com o valor líquido pagamento, valor provento pagamento, valor desconto pagamento, valor líquido férias, valor provento férias, valor desconto férias, banco de horas e hora extra.

* **Provento e Descontos do Envelope de Pagamento:** Representação gráfica do valor total de provento em relação ao desconto no envelope de pagamento.

* **Representatividade:**Representação gráfica da porcentagem do valor total de provento em relação ao desconto. A cor cinza representa o Desconto e a cor azul representa o Provento.

envelope\_ferias\_analise\_consolidadaEnvelope Férias - Análise ConsolidadaEnvelope Férias - Análise Consolidada

* **Valor Líquido Férias:**Dados os filtros acima, será somado de todos os valores líquidos de férias (diferença entre proventos e descontos) no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o valor líquido férias, valor provento férias, valor desconto férias, valor de base de cálculo férias e quantidade de funcionários por pagamento de férias. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **Valor Provento Férias:**Dados os filtros acima, será somado todos os valores de proventos de férias no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o valor líquido férias, valor provento férias, valor desconto férias, valor de base de cálculo férias e quantidade de funcionários por pagamento de férias. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **Valor Desconto Férias:**Dados os filtros acima, será somado todos os valores de descontos de férias no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todos os períodos e empresas com o valor líquido férias, valor provento férias, valor desconto férias, valor de base de cálculo férias e quantidade de funcionários por pagamento de férias. Para uma melhor detalhamento do período poderá selecionar o período, que desejar, nome fantasia, nome departamento, descrição da seção e nome da função.

* **Provento e Descontos do Envelope de Pagamento (Provento Férias x Desconto Férias):**Representação gráfica do valor de provento em relação ao desconto no envelope de pagamento de férias.

* **Representatividade % Provento Férias x Desconto Férias Pizza:**Representação gráfica da porcentagem do valor total de provento em relação ao desconto. A cor cinza representa o Desconto e a cor azul representa o Provento.

faltas\_atrasosFaltas e AtrasosFaltas e Atrasos

Este dashboard permite visualizar os KPIs de faltas e atrasos sobre a folha de pagamento do funcionário, com a possibilidade de realizar o filtro entre empresa, filiais, seções, departamento e etc. Podendo ter uma relação da quantidade de funcionários com faltas e atrasos, por período e por centro de custo.

Os indicadores exibidos são quebrados periodicamente conforme os filtros aplicados. Os filtros utilizados neste dashboard são:

* **Date (Data de competência):** Informe a Data Início e Data Fim das quais deseja extrair as informações, sendo que a Data Fim deve ser obrigatoriamente maior que a Data Início.
* **Empresa:** Empresa(s) que deseja extrair os indicadores.
* **Filial:** Filial(ais) que deseja extrair os indicadores.
* **Seção:** Selecione a(s) Seção(ões) que deseja extrair os indicadores.
* **Centro de Custo:** Selecione o(s) Centro(s) de Custo que deseja extrair os indicadores.
* **Departamento:** Selecione o(s) Departamento(s) dos quais deseja extrair os indicadores.

01.04faltas\_atrasos\_funcionariosFaltas e AtrasosFaltas e Atrasos

* **Quantidade de Funcionários com Faltas:**Dados os filtros acima, será somado os funcionários que possuem faltas no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todas as empresas com a quantidade de funcionários com faltas e atrasos. Para um melhor detalhamento por empresa, poderá selecionar um nome fantasia, nome departamento, descrição da seção e nome da função.

* **Quantidade de Funcionários com Atrasos:**Dados os filtros acima, será somado os funcionários que possuem atrasos no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento de todas as empresas com a quantidade de funcionários com faltas e atrasos.

* **Tabela Analítica de Funcionários com Faltas:** Representação da quantidade de funcionários com faltas por período e centro de custo.

Ao clicar em um período (Mês/Ano), será exibido um detalhamento da quantidade de funcionários e quantidade de funcionários com faltas do período selecionado, por data e centro de custo.

* **Tabela Analítica de Funcionários com Atrasos:**Representação da quantidade de funcionários com atraso por período e centro de custo.

Ao clicar em um período (Mês/Ano), será exibido um detalhamento da quantidade de funcionários e quantidade de funcionários com faltas do período selecionado, por data e centro de custo.

evolucao\_faltas\_atrasosEvoluçãoEvolução Faltas e Atrasos

* **Evolução Faltas x Atrasos:** Representação gráfica da relação entre a quantidade de funcionário com faltas e atrasos, distribuída mensalmente dentro do período filtrado.

* **Representatividade em %:**Representação gráfica da relação entre o total da quantidade de funcionário com faltas e atrasos, em porcentagem, dentro do período filtrado. A cor vermelha representa a quantidade de funcionário por pagamento com faltas e a cor laranja representa a quantidade de funcionário por pagamento com atrasos.

* **Evolução de Faltas x Empresa:** Representação gráfica da quantidade de faltas de funcionários em relação à empresa como todos.

* **Evolução de Atrasos x Empresa:** Representação gráfica da quantidade de atrasos de funcionários em relação à empresa como todos.

turnoverTurnoverTurnover

Este dashboard permite visualizar os KPIs de admitidos, demitidos e permanência sobre a folha de pagamento do funcionário, com a possibilidade de realizar o filtro entre empresa, filiais, seções, departamento e etc.

Os indicadores exibidos são quebrados periodicamente conforme os filtros aplicados. Os filtros utilizados neste dashboard são:

* **Date (Data de competência):** Informe a Data Início e Data Fim das quais deseja extrair as informações, sendo que a Data Fim deve ser obrigatoriamente maior que a Data Início.
* **Empresa:** Empresa(s) que deseja extrair os indicadores.
* **Filial:** Filial(ais) que deseja extrair os indicadores.
* **Seção:** Selecione a(s) Seção(ões) que deseja extrair os indicadores.
* **Centro de Custo:** Selecione o(s) Centro(s) de Custo que deseja extrair os indicadores.
* **Departamento:** Selecione o(s) Departamento(s) dos quais deseja extrair os indicadores.

01.05turnoverTurnoverTurnover

* **Quantidade de Funcionários Admitidos:** Dados os filtros acima, será contabilizado os funcionários admitidos no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento dos funcionários admitidos, demitidos e permanências por empresas. Para uma melhor detalhamento do período poderá selecionar uma empresa que desejar clicando no nome fantasia, filial, nome departamento, descrição da seção e nome da função.

* **Quantidade de Funcionários Demitidos:**Dados os filtros acima, será contabilizado os funcionários demitidos no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento dos funcionários admitidos, demitidos e permanências por empresas. Para uma melhor detalhamento do período poderá selecionar uma empresa que desejar clicando no nome fantasia, filial, nome departamento, descrição da seção e nome da função.

* **Quantidade de Funcionários Permanência:**Dados os filtros acima, será contabilizado os funcionários de permanência no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento dos funcionários admitidos, demitidos e permanências por empresas. Para uma melhor detalhamento do período poderá selecionar uma empresa que desejar clicando no nome fantasia, filial, nome departamento, descrição da seção e nome da função.

* **Tabela Analítica de Funcionários:**A tabela dinâmica permite visualizar a quantidade de funcionários por motivo de demissão e período. Para melhor detalhamento do período, poderá clicar na data de competência (Mês/Ano) ou motivo de demissão, permitindo detalhar a nível de funcionário.

evolucao\_turnoverEvoluçãoEvolução Turnover

* **Evolução Admitidos x Demitidos e Representatividade em %:**Representação gráfica da relação entre a quantidade de funcionário admitidos e demitidos, distribuída mensalmente dentro do período filtrado. Ao lado direito, uma representação gráfica da relação da totalização de funcionários admitidos e demitidos, em porcentagem, dentro do período filtrado. A cor vermelha representa a quantidade de funcionário demitidos e a cor azul representa a quantidade de funcionário admitidos.

* **Evolução Admitidos x Grau Escolaridade:**Representação gráfica da relação da quantidade admitidos por grau de escolaridade, distribuída mensalmente dentro do período filtrado.

* **Evolução Admitidos x Empresa e Representatividade em %:**Representação gráfica da relação da quantidade de funcionário admitidos por empresa, distribuída mensalmente dentro do período filtrado. Ao lado esquerdo, uma representação gráfica da relação da totalização de funcionários admitidos na empresa, em porcentagem, dentro do período filtrado.

* **Evolução Demitidos x Empresa e Representatividade em %:**Representação gráfica da relação da quantidade de funcionário demitidos por empresa, distribuída mensalmente dentro do período filtrado. Ao lado direito, uma representação gráfica da relação da totalização de funcionários demitidos na empresa, em porcentagem, dentro do período filtrado.

ranking\_turnoverRankingRanking Turnover

* **TOP 10 Admissões por Função:**Este ranking explicita quais as 10 admissões por função realizadas dentro do período filtrado, de acordo com o valor que se deve.

* **TOP 10 Admissões por Seção:**Este ranking explicita quais as 10 admissões por seção realizadas dentro do período filtrado, de acordo com o valor que se deve.

* **TOP 10 Demissões por Função:**Este ranking explicita quais as 10 demissões por função realizadas dentro do período filtrado, de acordo com o valor que se deve.

* **TOP 10 Demissões por Seção:**Este ranking explicita quais as 10 demissões por função realizadas dentro do período filtrado, de acordo com o valor que se deve.

* **Ranking por Filial:**Este ranking explicita os admitidos e demitidos por filial dentro do período filtrado, de acordo com o valor que se deve. Para melhor detalhamento por filiar, poderá clicar na filial, nome departamento, descrição da seção, nome da função e funcionário. Desta forma, terá uma visualização por nível de detalhes de acordo o que for selecionado.

afastados\_atestadosAfastados e AtestadosAfastados e Atestados

Este dashboard permite visualizar os KPIs de afastados e atestados sobre a folha de pagamento do funcionário, com a possibilidade de realizar o filtro entre empresa, filiais, seções, departamento e etc.

Os indicadores exibidos são quebrados periodicamente conforme os filtros aplicados. Os filtros utilizados neste dashboard são:

* **Date (Data de competência):** Informe a Data Início e Data Fim das quais deseja extrair as informações, sendo que a Data Fim deve ser obrigatoriamente maior que a Data Início.
* **Empresa:** Empresa(s) que deseja extrair os indicadores.
* **Filial:** Filial(ais) que deseja extrair os indicadores.
* **Seção:** Selecione a(s) Seção(ões) que deseja extrair os indicadores.
* **Centro de Custo:** Selecione o(s) Centro(s) de Custo que deseja extrair os indicadores.
* **Departamento:** Selecione o(s) Departamento(s) dos quais deseja extrair os indicadores.

01.06afastados\_atestados\_funcionarioAfastados e AtestadosAfastados e Atestados

* **Quantidade de Funcionários Afastados:**Dados os filtros acima, será contabilizado os funcionários afastados no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento dos funcionários afastados e atestados por empresas. Para uma melhor detalhamento do período poderá selecionar uma empresa que desejar clicando no nome fantasia, filial, nome departamento, descrição da seção e nome da função.

* **Quantidade de Funcionários com Atestados:** Dados os filtros acima, será contabilizado os funcionários com atestados no período e, será feita uma comparação com o período anterior e também do mesmo período selecionado do ano anterior. É mostrado também o percentual de variação. Ao clicar no valor é mostrado um detalhamento dos funcionários afastados e atestados por empresas. Para uma melhor detalhamento do período poderá selecionar uma empresa que desejar clicando no nome fantasia, filial, nome departamento, descrição da seção e nome da função.

evolucao\_afastados\_atestadosEvoluçãoEvolução Afastados e Atestados

* **Evolução Afastados x Atestados e Representatividade em %:**Representação gráfica da relação entre a quantidade de funcionário afastados e atestados, distribuída mensalmente dentro do período filtrado. Ao lado direito, uma representação gráfica da relação da totalização de funcionários afastados e atestados, em porcentagem, dentro do período filtrado. A cor vermelha representa a quantidade de funcionário afastados e a cor laranja representa a quantidade de funcionário atestados.

* **Evolução Afastados x Empresa e Representatividade em %:** Representação gráfica da relação da quantidade de funcionário afastados por empresa, distribuída mensalmente dentro do período filtrado. Ao lado esquerdo, uma representação gráfica da relação da totalização de funcionários afastados na empresa, em porcentagem, dentro do período filtrado.

* **Evolução Atestados x Empresa e Representatividade em %:**Representação gráfica da relação da quantidade de funcionário atestados por empresa, distribuída mensalmente dentro do período filtrado. Ao lado esquerdo, uma representação gráfica da relação da totalização de funcionários atestados na empresa, em porcentagem, dentro do período filtrado.

dimensoes\_rhDimensõesDimensões RHDimensõesdimensoes\_rh

No RH, atualmente existem as seguintes Dimensões:



Segue detalhamento das dimensões citadas anteriormente:

* **Empresas:**Lista as empresas.dimensao\_empresas

| Campo | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| LINHA | Instância do Produto (RM) | Não se aplica |
| TABELA | Nome da tabela | Não se aplica |
| CODCOLIGADA | Identificador da Coligada (empresa) | GCOLIGADA.CODCOLIGADA |
| NOMEFANTASIA | Nome Fantasia Empresa | GCOLIGADA.NOME |
| NOME | Razão Social Empresa | GCOLIGADA.NOME |
| CGC | CGC - Empresa | GCOLIGADA.CGC |
| INSCRICAOESTADUAL | Inscrição Estadual Empresa | GCOLIGADA.INSCRICAOESTADUAL |
| TELEFONE | Telefone Empresa | GCOLIGADA.TELEFONE |
| FAX | Fax Empresa | GCOLIGADA.FAX |

* **Filial:**Lista as filiais.dimensao\_filial

| Campo | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| LINHA | Instância do Produto (RM) | Não se aplica |
| TABELA | Nome da tabela | Não se aplica |
| CODCOLIGADA | Identificador da Coligada | GFILIAL.CODCOLIGADA |
| CODFILIAL | Identificador da Filial | GFILIAL.CODFILIAL |
| NOMEFANTASIA | Nome Fantasia Filial | GFILIAL.NOMEFANTASIA |
| NOME | Razão Social Filial | GFILIAL.NOME |
| CGC | CGC - Filial | GFILIAL.CGC |
| INSCRICAOESTADUAL | Inscrição Estadual Filial | GFILIAL.INSCRICAOESTADUAL |
| TELEFONE | Telefone Filial | GFILIAL.TELEFONE |
| FAX | Fax Filial | GFILIAL.FAX |

* **Departamentos:** Lista os departamentos.dimensao\_departamento

| Campo | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| LINHA | Instância do Produto (RM) | Não se aplica |
| TABELA | Nome da tabela | Não se aplica |
| CODCOLIGADA | Identificador da Coligada | GDEPTO.CODCOLIGADA |
| CODFILIAL | Identificador da Filial | GDEPTO.CODFILIAL |
| CODDEPARTAMENTO | Identificador do Departamento | GDEPTO.CODDEPARTAMENTO |
| NOME | Nome do Departamento | GDEPTO.NOME |

* **Seção:** Lista as seções. dimensao\_secao

| Campo | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| LINHA | Instância do Produto (RM) | Não se aplica |
| TABELA | Nome da tabela | Não se aplica |
| CODCOLIGADA | Identificador da Coligada | PSECAO.CODCOLIGADA |
| CODFILIAL | Identificador da Filial | PSECAO.CODFILIAL |
| CODDEPARTAMENTO | Identificador do Departamento | PSECAO.CODDEPTO |
| CODCUSTO | Identificador do Centro de Custo | PSECAO.NROCENCUSTOCONT |
| CODSECAO | Identificador da Seção | PSECAO.CODIGO |
| PSECAO | Descrição da Seção | PSECAO.DESCRICAO |
| CGC | CGC - Seção | PSECAO.CGC |
| CEI | CEI - Seção | PSECAO.CEI |
| INSCRESTADUAL | Inscrição Estadual da Seção | PSECAO.INSCRESTADUAL |
| INSCRMUNICIPAL | Inscrição Municipal da Seção | PSECAO.INSCRMUNICIPAL |
| OPTASIMPLES | Opta Simples | PSECAO.OPTASIMPLES |
| RUA | Rua da  Seção | PSECAO.RUA |
| NUMERO | Número Seção | PSECAO.NUMERO |
| BAIRRO | Bairro Seção | PSECAO.BAIRRO |
| CIDADE | Cidade Seção | PSECAO.CIDADE |
| CEP | CEP - Seção | PSECAO.CEP |
| PAIS | Pais Seção | PSECAO.PAIS |
| TELEFONE | Telefone Seção | PSECAO.TELEFONE |

* **Função:** Lista as funções.dimensao\_funcao

| Campo | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| LINHA | Instância do Produto (RM) | Não se aplica |
| TABELA | Nome da tabela | Não se aplica |
| CODIGO | Identificador da Função | PFUNCAO.CODIGO |
| NOMEFUNCAO | Nome da Função | PFUNCAO.NOME |
| CARGO | Código do Cargo | PFUNCAO.CARGO |
| NOMECARGO | Nome do Cargo | PCARGO.NOME |
| JORNADA | Jornada da Função | PCARGO.JORNADATRABALHO/60.00 |
| CBO | CBO da Funcao | PFUNCAO.CBO |
| CBO2002 | CBO2002 da Função | PFUNCAO.CBO2002 |

* **Função Complementar:** Lista as funções complementares.dimensao\_funcao\_complementar

| Campo | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| LINHA | Instância do Produto (RM | Não se aplica |
| TABELA | Nome da tabela | Não se aplica |
| CODCOLIGADA | Identificador da Coligada | PFUNC.CODCOLIGADA |
| CODFILIAL | Identificador da Filial | PFUNC.CODFILIAL |
| CODSECAO | Identificador da Seção | PFUNC.CODSECAO |
| CODFUNCAO | Identificador da Função | PFUNC.CODFUNCAO |
| CODSINDICATO | Identificador do Sindicato | PFUNC.CODSINDICATO |
| CODSITUACAO | Identificador da Situação | PFUNC.CODSITUACAO |
| CODDEPARTAMENTO | Código do Departamento | PSECAO.CODDEPTO |
| CODCUSTO | Identificador Código C.Custo | PFUNC.CODCCUSTO |

* **Funcionário:** Lista os funcionários.dimensao\_funcionario

| Campo | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| LINHA | Instância do Produto (RM) | Não se aplica |
| TABELA | Nome da tabela | Não se aplica |
| CODCOLIGADA | Identificador da Coligada | PFUNC.CODCOLIGADA |
| CODFILIAL | Identificador da Filial | PFUNC.CODFILIAL |
| CODSECAO | Identificador da Seção | PFUNC.CODSECAO |
| CODFUNCAO | Identificador da Função | PFUNC.CODFUNCAO |
| CODSINDICATO | Identificador sindicato | PFUNC.CODSINDICATO |
| CODSITUACAO | Identificador da Situação | PFUNC.CODSITUACAO |
| CODDEPARTAMENTO | Código do Departamento | PSECAO.CODDEPTO |
| CODCUSTO | Identificador  Centro Custo | PFUNC.CODCCUSTO |
| PESSOA | Identificador da Pessoa | PFUNC.CODPESSOA |
| CHAPA | Chapa do Funcionário | PFUNC.CHAPA |
| NOME | Nome do Funcionário | PFUNC.NOME |
| JORNADA | Jornada do Funcionário | PFUNC.JORNADA |
| JORNADAMENSAL | Jornada Mensal do Funcionário | PFUNC.JORNADAMENSAL |
| CODTIPO | Código do Tipo | PFUNC.CODTIPO |
| DESCRICAO | Descrição do Tipo | PTPFUNC.DESCRICAO |
| CODHORARIO | Código do Horário | PFUNC.CODHORARIO |
| DESCRICAO | Descrição do Horário | AHORARIO.DESCRICAO |
| DATAADMISSAO | Data de Admissão | PFUNC.DATAADMISSAO |
| DATADEMISSAO | Data de Demissão | PFUNC.DATADEMISSAO |
| TIPOADMISSAO | Código Tipo Admissão | PFUNC.TIPOADMISSAO |
| DESCRICAO | Descrição Tipo Admissão | PTPADMISSAO.DESCRICAO |
| TIPODEMISSAO | Código Tipo Demissão | PFUNC.TIPODEMISSAO |
| DESCRICAO | Descrição Tipo Demissão | PTPDEMISSAO.DESCRICAO |
| MOTIVOADMISSAO | Identificador  Motivo Admissão | PFUNC.MOTIVOADMISSAO |
| DESCRICAOMOTADM | Descrição Motivo Admissão | PMOTADMISSAO.DESCRICAO |
| MOTIVODEMISSAO | Identificador Motivo Demissão | PFUNC.MOTIVODEMISSAO |
| DESCRICAOMOTDEM | Descrição Motivo Demissão | PMOTDEMISSAO.DESCRICAO |
| SALARIO | Valor do Salário | PFUNC.SALARIO |
| QTDEPAI | Qtde Pai Funcionários | PFDEPEND.QTDEPAI |
| QTDEMAE | Qtde Mãe Funcionários | PFDEPEND.QTDEMAE |
| QTDEOUTROS | Qtde Outros Funcionários | PFDEPEND.QTDEOUTROS |
| QTDETOTAL | Qtde TOTAL Dependentes de Funcionário | PFDEPEND.QTDETOTAL |

* **Centro de Custo:** Lista os centros de custo.dimensao\_centro\_custo

| Campo | Descrição | Campo do Banco de Dados |
| --- | --- | --- |
| LINHA | Instância do Produto (RM) | Não se aplica |
| TABELA | Nome da tabela | Não se aplica |
| CODCOLIGADA | Identificador da Coligada | PSECAO.CODCOLIGADA |
| CODCCUSTO | Identificador do Centro de Custo da Folha | PCCUSTO.CODCCUSTO |
| NOME | Nome do Centro de Custo da Folha | PCCUSTO.NOME |
| CODCCGLOBAL | Identificador do Centro de Custo Global | PCCUSTO.CODCCGLOBAL |

* **Sindicatos:** Lista os sindicatos.dimensao\_sindicato

| Campo | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| LINHA | Instância do Produto (RM) | Não se aplica |
| TABELA | Nome da tabela | Não se aplica |
| CODCOLIGADA | Identificador da Coligada (empresa) | PSINDIC.CODCOLIGADA |
| CODIGO | Identificador do Sindicato | PSINDIC.CODIGO |
| NOME | Nome do Sindicato | PSINDIC.NOME |
| SALARIOMINIMO | O salario mínimo do sindicato | PSINDIC.SALARIOMINIMO |
| MINIMOGARANTIDO | O valor mínimo definido pelo sindicato para a categoria. | PSINDIC.MINIMOGARANTIDO |

* **Eventos:** Lista os eventos.dimensao\_evento

| Campo | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| LINHA | Instância do Produto (RM) | Não se aplica |
| TABELA | Nome da tabela | Não se aplica |
| CODCOLIGADA | Identificador da Coligada (empresa) | PEVENTO.CODCOLIGADA |
| CODIGO | Identificador do Evento | PEVENTO.CODIGO |
| DESCRICAO | Descrição do Evento | PEVENTO.DESCRICAO |
| PROVDESCBASE | Tipo do evento: provento, desconto ou base de cálculo | PEVENTO.PROVDESCBASE |
| VALHORDIAREF | Tipo do valor evento: valor, hora, dia ou referência | PEVENTO.VALHORDIAREF |
| CODIGOCALCULO | O código de cálculo relacionado ao evento | PEVENTO.CODIGOCALCULO |
| CONTACREDITO | Conta de Crédito do evento | PEVENTO.CONTACREDITO |
| CONTADEBITO | Conta de Débito do evento | PEVENTO.CONTADEBITO |
| INCACUMULADOR | Incidência no Acumulador | PEVENTO.INCACUMULADOR |
| ORDEMCALCULO | Ordem de Cálculo do evento | PEVENTO.ORDEMCALCULO |
| PRIORIDADE | Prioridade do evento | PEVENTO.PRIORIDADE |
| CODRUBRICA | Código da Rubrica | PEVENTO.CODRUBRICA |
| DESCRICAO | Descrição da Rubrica | PRUBRICA.DESCRICAO |

* **Situação do Funcionário:** Lista as situações dos funcionário.dimensao\_situacao\_funcionario

| Campo | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| LINHA | Instância do Produto (RM) | Não se aplica |
| TABELA | Nome da tabela | Não se aplica |
| CODSITUACAO | Identificador da Situação do funcionário | PCODSITUACAO.CODINTERNO |
| DESCRICAO | Descrição da Situação | PCODSITUACAO.DESCRICAO |

* **Pessoa:** Lista as pessoas.dimensao\_pessoa

| Campo | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| LINHA | Instância do Produto (RM) | Não se aplica |
| TABELA | Nome da tabela | Não se aplica |
| CODIGO | Identificador do código da Pessoa | PPESSOA.CODIGO |
| NOME | Nome da Pessoa | PPESSOA.NOME |
| BAIRRO | Bairro da Pessoa | PPESSOA.BAIRRO |
| CIDADE | Cidade da Pessoa | PPESSOA.CIDADE |
| SEXO | Sexo da Pessoa | PPESSOA.SEXO |
| RUA | Rua da Pessoa | PPESSOA.RUA |
| NUMERO | Numero da Pessoa | PPESSOA.NUMERO |
| COMPLEMENTO | Complemento da Pessoa | PPESSOA.COMPLEMENTO |
| CEP | CEP da Pessoa | PPESSOA.CEP |
| ESTADO | Estado da Pessoa | PPESSOA.ESTADO |
| CPF | CPF da Pessoa | PPESSOA.CPF |
| CARTIDENTIDADE | Carteira de identidade da Pessoa | PPESSOA.CARTIDENTIDADE |
| DTNASCIMENTO | Data de Nascimento da Pessoa | PPESSOA.DTNASCIMENTO |
| DESCRICAO | Descricao Grau Instrucao da Pessoa | PCODINSTRUCAO.DESCRICAO |

fatos\_rhFatosFatos RHFatosfatos\_rh

No RH, atualmente existem as seguintes Fatos:

* Folha de Pagamento:
* Automação de Ponto:
* Gestão de Pessoas:

Segue detalhamento das fatos citadas anteriormente:

* **envelope\_feriasEnvelope de Férias**: Lista as informações sobre os valores do envelope de férias dos funcionários das empresas conforme o período definido pelos parâmetros de extração, distinguindo os valores líquidos, proventos, desconto e base de cálculo.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| PROVDESCBASE | Tipo do evento lançado no envelope (Prov/Desc/Base Ferias) | PEVENTO.PROVDESCBASE |
| DTBASE | Data de Competência Ferias | PFUFERIASVERBAS.DTBASE |
| INICIOPERAQUIS | Data de inicio do período aquisitivo | PFUFERIASVERBAS.INICIOPERAQUIS |
| FIMPERAQUIS | Data de fim do período aquisitivo | PFUFERIASVERBAS.FIMPERAQUIS |

* **envelope\_pagamentoEnvelope de Pagamento:**Lista as informações sobre os valores do envelope de pagamento dos funcionários das empresas conforme o período definido pelos parâmetros de extração, distinguindo os valores líquidos, proventos, desconto e base de cálculo.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| ANOCOMP | Ano da Competência | PFFINANC.ANOCOMP |
| MESCOMP | Mês da Competência | PFFINANC.MESCOMP |
| NROPERIODO | Número do Período da Competência | PFFINANC.NROPERIODO |
| PROVDESCBASE | Tipo do evento lançado no envelope (Prov/Desc/Base Ferias) | PEVENTO.PROVDESCBASE |
| DTPAGTO | Data de Pagamento do Envelope | PFFINANC.DTPAGTO |
| DTBASE | Data de Competência do Envelope | PFFINANC.DTBASE |
| REF | Valor de referência do envelope | PFFINANC.REF |

* **historico\_afastamentoHistórico de Afastamento:**Lista as informações sobre os dias e horas de afastamento dos funcionários das empresas conforme o período definido pelos parâmetros de extração, bem como o tipo, descrição, motivos e observação do afastamento.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| DTINICIO | Data Início do Afastamento | PFHSTAFT.DTINICIO |
| DTFINAL | Data Final do Afastamento | PFHSTAFT.DTFINAL |
| DTCOMPETENCIA | Data De Competência | PFHSTAFT.DTINICIO |
| QTDEDIASAFASTAMENTO | Quantidade de Dias de Afastamento | (PFHSTAFT.DTFINAL - PFHSTAFT.DTINICIO) |
| QTDEHORASAFASTAMENTO | Quantidade de Horas de Afastamento | (PFHSTAFT.DTFINAL - PFHSTAFT.DTINICIO ) \* 24.00 |
| TIPO | Tipo do Afastamento | PFHSTAFT.TIPO |
| DESCRICAOTIPO | Descrição do tipo de afastamento | PCODAFAST.DESCRICAO |
| MOTIVO | Motivo do Afastamento | PFHSTAFT.MOTIVO |
| DESCRICAOMOTIVO | Descrição do motivo de afastamento | PMUDSITUACAO.DESCRICAO |
| OBSERVACAO | Obervação do afastamento | PFHSTAFT.OBSERVACAO |

* **historico\_assistencia\_medicaHistórico de Assistência Médica:**Lista as informações sobre o histórico de assistência médica dos funcionários das empresas conforme o período definido pelos parâmetros de extração, bem como os seus dependentes.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| NOME | Nome do Dependente | PFUNC.NOME |
| NRODEPEND | Numero do Dependente | PFUNC.NRODEPEND |
| ANOCOMP | Ano de Competência | PFHSTASSMED.ANOCOMP |
| MESCOMP | Mês de Competência | PFHSTASSMED.MESCOMP |
| NROPERIODO | Período de Competência | PFHSTASSMED.NROPERIODO |
| ANOREF | Ano de Referência | PFHSTASSMED.ANOREF |
| MESREF | Mês de Referência | PFHSTASSMED.MESREF |
| PERIODOREF | Período de Referência | PFHSTASSMED.PERIODOREF |
| DTBASE | Data de Competência | PFHSTASSMED.DTBASE |
| DTPAGTO | Data de Pagamento | PFHSTASSMED.DTPAGTO |
| VALOR | Valor efetivo da assistência média | PFHSTASSMED.VALOR |
| VALORORIGINAL | Valor Original | PFHSTASSMED.VALORORIGINAL |

* **historico\_feriasHistórico de Férias:**Lista as informações sobre o histórico de férias dos funcionários das empresas conforme o período definido pelos parâmetros de extração, datas de pagamento e aviso de férias, situação, dias de abono, dias de férias e faltas.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| DATAPAGTO | Data de Pagamento de Férias | PFUFERIASPER.DATAPAGTO |
| DATAAVISO | Data de Aviso de Férias | PFUFERIASPER.DATAAVISO |
| SITUACAOFERIAS | Situação da Férias | PFUFERIASPER.SITUACAOFERIAS |
| NRODIASABONO | Dias de Abono | PFUFERIASPER.NRODIASABONO |
| NRODIASFERIAS | Dias de Férias | PFUFERIASPER.NRODIASFERIAS |
| FALTAS | Faltas | PFUFERIASPER.FALTAS |

* **historico\_funcaoHistórico de Função:**Lista as informações sobre o histórico de mudança de função dos funcionários das empresas conforme o período definido pelos parâmetros de extração.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| DESCRICAO | Descrição da Mudança de Função | PMOTMUDFUNCAO.DESCRICAO |
| CODFUNCAO | Identificador da Mudança de Função | PFHSTFCO.CODFUNCAO |
| DTMUDANCA | Data de Mudança de Função | FHSTFCO.DTMUDANCA |

* **historico\_salarialHistórico Salarial:**Lista as informações sobre o histórico de salário dos funcionários das empresas conforme o período definido pelos parâmetros de extração.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| MOTIVO | Identificador do Motivo do Salário | PFHSTSAL.MOTIVO |
| DESCRICAO | Descrição do Motivo do Salário | PMOTMUDSAL.DESCRICAO |
| SALARIO | Salário do Histórico | PFHSTSAL.SALARIO |

* **historico\_secaoHistórico de Seção:**Lista as informações sobre o histórico de seção dos funcionários das empresas conforme o período definido pelos parâmetros de extração.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| DESCRICAO | Descrição da Mudança de Função | PMOTMUDFUNCAO.DESCRICAO |
| DTMUDANCA | Data de Mudança de Função | PFHSTSEC.DTMUDANCA |

* **encargosEncargos:**Lista as informações sobre os encargos dos funcionários das empresas conforme o período definido pelos parâmetros de extração, fornecendo o valor e a porcentagem do encargo.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| APLICACAO | Aplicação de utilização | PFENCARGO.APLICACAO |
| CODENCARGO | Identificador do Encargo | PENCARGO.CODENCARGO |
| DESCRICAO | Descrição do Encargo | PENCARGO.DESCRICAO |
| TIPOENCARGO | Tipo de Encargo | PENCARGO.TIPOENCARGO |
| DTBASE | Data de Competência | PENCARGO.DTBASE |
| VALOR | Valor do Encargo | PENCARGO.VALOR |
| PORCENTAGEM | Porcentagem do Encargo | PENCARGO.PORCENTAGEM |

* **historico\_provisaoHistórico de Provisão:** Lista as informações sobre os valores de histórico de provisão dos funcionários das empresas conforme o período definido pelos parâmetros de extração, distinguindo do valor de férias, 13o e entre outros.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| DTVENCFER | Data de Vencimento de Ferias | PFHSTPROV.DTVENCFER |
| DTBASE | Data de Competência | PFHSTPROV.DTBASE |
| VALPROVFER | Valor do Provento de Férias Acumulado | PFHSTPROV.VALPROVFER |
| VALPROV13 | Valor do Provento de 13o do Mês Acumulado | PFHSTPROV.VALPROV13 |
| VALPROVFERMESATUAL | Valor do Provento de Férias do Mês Atual | Calculado: Diferença do Acumulado "PFHSTPROV.VALPROVFER" e o valor de provento de férias da última data do histórico de provisão. |
| VALPROV13MESATUAL | Valor do Provento de 13o do Mês Atual | Calculado: Diferença do Acumulado "PFHSTPROV.VALPROV13" e o valor de provento de 13o da última data do histórico de provisão. |
| NROAVOSVENCFERDEC | Número de Avos de Vencimento Férias | PFHSTPROV.NROAVOSVENCFERDEC |
| NROAVOSPROPORCDEC | Número de Avos Proporcional | PFHSTPROV.NROAVOSPROPORCDEC |
| NROAVOS13DEC | Número de Avos do 13o | PFHSTPROV.NROAVOS13DEC |
| VALPROVCOMABATFER | Valor do Provento Com Abatimento Acumulado | PFHSTPROV.VALPROVCOMABATFER |
| VALPROVSEMABATFER | Valor do Provento Sem Abatimento Acumulado | PFHSTPROV.VALPROVSEMABATFER |
| VALPROVCOMABATFERMESATUAL | Valor do Provento Com Abatimento do Mês Atual | Calculado: Diferença do Acumulado "PFHSTPROV.VALPROVCOMABATFER" e o valor de provento com abatimento da última data do histórico de provisão. |
| VALPROVSEMABATFERMESATUAL | Valor do Provento Som Abatimento do Mês Atual | Calculado: Diferença do Acumulado "PFHSTPROV.VALPROVSEMABATFER" e o valor de provento sem abatimento da última data do histórico de provisão. |

* **abonos\_funcionarioAbonos do Funcionário:** Lista as informações referentes aos abonos do funcionário.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| CHAPA | Chapa do funcionário que terá o período abonado | AABONFUN.CHAPA |
| CODABONO | Codigo do Abono | AABONFUN.CODABONO |
| DESCRICAO | Descricao Abono | AABONFUN.DESCRICAO |
| LIMDIASABONO | Limite de Dias de Abono | AABONFUN.LIMDIASABONO |
| ATIVOPORTAL | Ativo no Portal | AABONFUN.ATIVOPORTAL |
| HORAINICIO | Hora Inicio | AABONFUN.HORAINICIO |
| HORAFIM | Hora Final | AABONFUN.HORAFIM |
| DATA | Data de Comp. Mov. Diario | AABONFUN.DATA |
| HORAFIM - HORAINICIO | Dif. Horario | AABONFUN.HORAFIM - AABONFUN.HORAINICIO |

* **movimento\_diario\_funcionarioMovimento Diário de Funcionário:**Lista as informações sobre o número de horas do movimento diário do funcionário levando em consideração os dados abaixo.

| Campo | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| DATA | Data de Comp. Mov. Diario | AAFHTFUN.DATA |
| ABONO | Abono | AAFHTFUN.ABONO |
| ATRASO | Atraso | AAFHTFUN.ATRASO |
| FALTA | Falta | AAFHTFUN.FALTA |
| HTRAB | Horas.Trabalhada | AAFHTFUN.HTRAB |
| EXTRAEXECUTADO | Extra Executado | AAFHTFUN.EXTRAEXECUTADO |
| ADICIONAL | Adicional | AAFHTFUN.ADICIONAL |
| BASE | Base | AAFHTFUN.BASE |
| EXTRAAUTORIZADO | Extra Autorizado | AAFHTFUN.EXTRAAUTORIZADO |
| TEMPOREF | Tempo Ref | AAFHTFUN.TEMPOREF |
| COMPENSADO | Compensado | AAFHTFUN.COMPENSADO |
| DESCANSO | Descanso | AAFHTFUN.DESCANSO |
| FERIADO | Feriado | AAFHTFUN.FERIADO |
| EXTRACALC | Extra Calculado | AAFHTFUN.EXTRACALC |
| ATRASOCALC | Atraso Calculado | AAFHTFUN.ATRASOCALC |
| FALTACALC | Falta Calculado | AAFHTFUN.FALTACALC |

* **saldo\_banco\_de\_horasSaldo de Banco de Horas:** Lista o saldo de banco de horas do funcionário considerando extras, atrasos e faltas de um período.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| DTBASE | Data de Comp. Banco Horas | ASALDOBANCOHOR.DTBASE |
| EXTRAANT | Extra Ant. Banco Horas | ASALDOBANCOHOR.EXTRAANT |
| ATRASOANT | Atraso Ant. Banco Horas | ASALDOBANCOHOR.ATRASOANT |
| FALTAANT | Falta Ant. Banco Horas | ASALDOBANCOHOR.FALTAANT |
| EXTRAATU | Extra Atual Banco Horas | ASALDOBANCOHOR.EXTRAATU |
| ATRASOATU | Atraso Atual Banco Horas | ASALDOBANCOHOR.ATRASOATU |
| FALTAATU | Falta Atual Banco Horas | ASALDOBANCOHOR.FALTAATU |

* **atestadosAtestados:**Lista as informações sobre os Atestados Médicos dos Funcionários com dados do motivo do afastamento e datas de início e fim.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| SEQATESTADO | Sequencia do Atestado | VATESTADO.SEQATESTADO |
| HORAINICIO | Hora de Inicio do Atestado | VATESTADO.HORAINICIO |
| HORAFINAL | Hora Final do Atestado | VATESTADO.HORAFINAL |
| CODTPATESTADO | Codigo do Tipo do Atestado | VATESTADO.CODTPATESTADO |
| NOMETPATESTADO | Descricao do Tipo de Atestado | VTIPOATESTADO.NOMETPATESTADO |
| DTINICIO | Data Inicio do Atestado | VATESTADO.DTINICIO |
| DTFINAL | Data Final do Atestado | VATESTADO.DTFINAL |
| CID | Codigo do CID | VATESTADO.CID |
| DESCRICAOCID | Descricao do CID | VCID.DESCRICAOCID |
| OBSERVACOES | Observacao | VATESTADO.OBSERVACOES |
| DATAPERICIA | Data de Pericia | VATESTADO.DATAPERICIA |
| NOMEMEDICO | Nome do Medico | VATESTADO.NOMEMEDICO |

* **turnOverTurnOver:** Representa a taxa de rotatividade dos colaboradores em uma empresa

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| ANOCOMP | Ano de Competencia Periodo | PERIODOS.ANOCOMP |
| MESCOMP | Mes de Competencia Periodo | PERIODOS.MESCOMP |
| MESCOMP  ANOCOMP | Data de Competencia | PERIODOS.MESCOMP  PERIODOS.ANOCOMP |
| TIPOADMISSAO | Tipo de Admissao Periodo | PERIODOS.TIPOADMISSAO |
| TIPODEMISSAO | Tipo de Demissao Periodo | PERIODOS.TIPODEMISSAO |
| DATAADMISSAO | Data de Admissao Periodo | PERIODOS.DATAADMISSAO |
| DATADEMISSAO | Data de Demissao Periodo | PERIODOS.DATADEMISSAO |
| DTTRANSFERENCIA | Data de Transferencia Periodo | PERIODOS.DTTRANSFERENCIA |
| DTBASEINIPERIODO | Dt.Base Inicial Periodo | PERIODOS.DTBASEINIPERIODO |
| DTBASEFIMPERIODO | Dt.Base Final Periodo | PERIODOS.DTBASEFIMPERIODO |
| DTBASEFIMPERIODO | Data Movimento Periodo | PERIODOS.DTBASEFIMPERIODO |
| ( DATADEMISSAO - DATAADMISSAO ) / 365.00 ) \* 12.00 | Tempo de Casa Meses | ( PERIODOS.DATADEMISSAO - PERIODOS.DATAADMISSAO ) / 365.00 ) \* 12.00 |
| ( DATADEMISSAO - DATAADMISSAO ) / 365.00 ) | Tempo de Casa Anos | ( PERIODOS.DATADEMISSAO - PERIODOS.DATAADMISSAO ) / 365.00 ) |
| ( DATADEMISSAO - DATAADMISSAO ) / 1.00 ) | Tempo de Casa Dias | ( PERIODOS.DATADEMISSAO - PERIODOS.DATAADMISSAO ) / 1.00 ) |
| QTDEINIPERIODO | Qtde. Inicio do Periodo | PERIODOS.QTDEINIPERIODO |
| QTDEADMITIDOS | Qtde. Admitidos no Periodo | PERIODOS.QTDEADMITIDOS |
| QTDEDEMITIDOS | Qtde. Demitidos no Periodo | PERIODOS.QTDEDEMITIDOS |
| QTDEFIMPERIODO | Qtde. Final do Periodo | PERIODOS.QTDEFIMPERIODO |
| QTDEADMITIDOSSEMTRANSF | Qtde. Admitidos Trf Periodo | PERIODOS.QTDEADMITIDOSSEMTRANSF |
| QTDEDEMITIDOSSEMTRANSF | Qtde. Demitidos Trf Periodo | PERIODOS.QTDEDEMITIDOSSEMTRANSF |
| DATAADMISSAO  DTBASEFIMPERIODO | Qtde. Admitidos T Casa Periodo | PERIODOS.DATAADMISSAO >= PERIODOS.DTBASEFIMPERIODO -365 AND PERIODOS.DATAADMISSAO <= PERIODOS.DTBASEFIMPERIODO |
| DATAADMISSAO  DTBASEFIMPERIODO  DATAADMISSAO  DTBASEINIPERIODO  DTBASEFIMPERIODO | Qtde. Demitidos T Casa Periodo | PERIODOS.DATAADMISSAO > PERIODOS.DTBASEFIMPERIODO -365 AND PERIODOS.DATAADMISSAO <= PERIODOS.DTBASEFIMPERIODO  AND PERIODOS.DATADEMISSAO BETWEEN PERIODOS.DTBASEINIPERIODO AND PERIODOS.DTBASEFIMPERIODO |

* **processos\_trabalhistasProcessos Trabalhistas:** Lista os processos trabalhistas registrados pelos funcionários.

| Campos | Descrição | Campo no Banco de dados |
| --- | --- | --- |
| CODFORUM | Codigo do Forum | VPROCESSOS.CODFORUM |
| NOMEFORUM | Nome do Forum | VFORUNS.NOMEFORUM |
| NUMPROCESSO | Numero do Processo | VPROCESSOS.NUMPROCESSO |
| CODENTIDADE | Codigo da Entidade | VPROCESSOS.CODENTIDADE |
| RAZAOSOCIAL | Nome da Entidade | VENTIDADES.RAZAOSOCIAL |
| CODDESCRICAO | Codigo da Descricao | VPROCESSOS.CODDESCRICAO |
| TIPOPROCESSO | Tipo do Processo | VPROCESSOS.TIPOPROCESSO |
| DESCRICAO | Descricao do Tipo de Processo" | VTIPOPROCESSO.DESCRICAO |
| DATAABERTURA | Data de Abertura | VPROCESSOS.DATAABERTURA |
| DATAENCERRAMENTO | Data de Encerramento | VPROCESSOS.DATAENCERRAMENTO |
| DATARECLAMACAO | Data de Reclamacao | VPROCESSOS.DATARECLAMACAO |

* turmas**Turmas:** Listas os dados das turmas de treinamentos registrados.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| CODTURMA | Codigo da Turma | VTURMAS.CODTURMA |
| CODENTIDADE | Codigo da Entidade | VTURMAS.CODENTIDADE |
| RAZAOSOCIAL | Nome da Entidade | VENTIDADES.RAZAOSOCIAL |
| NOME | Nome da Turma | VTURMAS.NOME |
| ATIVO | Turma Ativa | VTURMAS.ATIVO |
| VAGAS | Numero de Vagas | VTURMAS.VAGAS |
| LOCAL | Local | VTURMAS.LOCAL |
| HORAINICIO | Horario Inicial | VTURMAS.HORAINICIO |
| HORATERMINO | Horario Final | VTURMAS.HORATERMINO |
| CARGAHORARIA | Carga Horaria da Turma | VTURMAS.CARGAHORARIA |
| CARGAHORARIA | Carga Horaria do Curso | VCURSOS.CARGAHORARIA |
| CODCURSO | Codigo do Curso | VTURMAS.CODCURSO |
| NOMECURSO | Nome do Cursro | VCURSOS.NOMECURSO |
| DESCRICAO | Descricao do Curso | VCURSOS.DESCRICAO |
| DTINICIO | Data Inicio | VTURMAS.DTINICIO |
| DTTERMINO | Data Final | VTURMAS.DTTERMINO |

* **participantes\_turmaParticipantes da Turma:** Lista os participantes das turmas de treinamentos.

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| CODTURMA | Codigo da Turma | VTURMA.CODTURMA |
| CODPESSOA | Codigo da Pessoa | VTURMA.CODPESSOA |
| FALTAS | Numero de Faltas | VTURMA.FALTAS |

* despesas\_turma**Despesas da Turma:** Lista as despesas das turmas de treinamentos**.**

| Campos | Descrição | Campo no Banco de Dados |
| --- | --- | --- |
| CODTURMA | Codigo da Despesa | VDESPESA.CODTURMA |
| CODDESPESA | Codido da Despesa | VDESPESA.CODDESPESA |
| DATAINIPER | Data Inicio Periodo | VDESPESA.DATAINIPER |
| DATATERPER | Data Fim Periodo | VDESPESA.DATATERPER |
| VALOR | Valor | VDESPESA.VALOR |

materiaisGestão de Estoque, Compras e Faturamento

Detalhamento sobre as dimensões e fatos relacionadas ao Fast Analytics de Gestão de Estoque, Compras e Faturamento:

geral\_materiaistruectb\_indicadoresIndicadores

Os indicadores são controlados por um filtro geral.

Com ele é possível:

* Escolher um período de datas;
* Escolher a Coligada;
* Escolher a Filial;
* Escolher a Unidade de Negócio;
* Escolher o Vendedor;
* Escolher a Instancia.

tab\_indicadoresanalise\_geralAnálise Geral

* **Análise Geral**

Em análise Geral podemos ver o resumo das três fatos permitindo ter uma visão global do fluxo de vendas, para isso é possível filtrar os resultados exibidos de acordo com o filtro.

Análise geral de Faturamento, Devolução e Pedidos.

mes\_aculmuladoMês X Acumulado

* **Mês x Acumulado**

Em Mês x Acumulado podemos ver um resumo em gráficos e números do que foi recebido no mês atual e o que foi acumulado no mês anterior, no ano anterior e nas metas traçadas.

acompanhamento\_metasAcompanhamento de Metas

* **Acompanhamento de Metas**

Resumo de Metas Atingidas e Margem, Resumo por Unidade de Negócio.

evolucaoEvolução

* **Evolução**

Demonstra a evolução de Faturamento, Devolução e Pedidos dentre um período de tempo e filtros.

sazonalidadeSazonalidade

* **Sazonalidade**

Demonstra as variações que ocorrem em intervalos regulares específicos inferiores a um ano, como semanal, mensal ou trimestral. 

acomp.diarioAcompanhamento Diário

* **Acompanhamento Diário**

ctb\_dimensoesDimensões

**Dimensões:**

Cliente (FCFO)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| FCFO.CODCOLIGADA | COD\_COLIGADA | Código de Coligada |
| FCFO.CODCFO | COD\_CLIENTE | Código do Cliente |
| FCFO.NOME | NOME\_CLIENTE | Nome do Cliente |
| FCFO.CODLOJA | COD\_LOJA | Código de Loja |
| FCFO.RAMOATIV | RAMO\_ATIV | Ramo de Atividade |

Coligada (GCOLIGADA)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| GCOLIGADA.CODCOLIGADA | CODCOLIGADA | Código de Coligada |
| GCOLIGADA.NOMEFANTASIA | DESCRICAO | Descrição de Coligada |
| GCOLIGADA.NOME | DESCRICAO | Descrição de Coligada |

Condição de Pagamento (TCPG)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| TCPG.CODCOLIGADA | COD\_COLIGADA | Código de Coligada |
| TCPG.CODCPG | COD\_CPG | Código de Condição de Pagamento |
| TCPG.NOME | NOME\_CPG | Nome Condição de Pagamento |

Filial (GFILIAL)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| GFILIAL.CODCOLIGADA | COD\_COLIGADA | Código de Coligada |
| GFILIAL.CODFILIAL | COD\_FILIAL | Código de Filial |
| GFILIAL.NOMEFANTASIA | NOME\_FANTASIA | Nome de Filial |
| DUNDNEGOCIO.DESCRICAO | UNI\_NEG | Descrição da Unidade de Negocio |
| DUNDNEGOCIO.CODCOLIGADA|DUNDNEGOCIO.CODFILIAL|DUNDNEGOCIO.CODUNDNEGOCIO | COD\_UNINEG | Código da Unidade de Negocio |

Fornecedor (FCFO)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| FCFO.CODCOLIGADA | CODCOLIGADA | Código de Coligada |
| FCFO.CODCFO | CODCFO | Código de Fornecedor |
| FCFO.NOME | NOME | Nome de Fornecedor |

Grupo Cliente (TGRUPOCF)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| TGRUPOCF.CODCOLIGADA | COD\_COLIGADA | Código de Coligada |
| TGRUPOCF.CODCOLIGADA | COD\_GRUPO\_CLIENTE | Código de Grupo de Cliente |
| TGRUPOCF.CODCOLIGADA | NOME\_GRUPO\_CLIENTE | Nome de Grupo de Cliente |

Grupo Estoque (TLOC)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| TLOC.CODCOLIGADA | COD\_COLIGADA | Código de Coligada |
| TLOC.CODLOC | COD\_GRP\_ESTOQUE | Código de Grupo de Estoque |
| TLOC.NOME | NOME\_GRP\_ESTOQUE | Nome de Grupo de Estoque |

Produto (TPRODUTO)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| TPRODUTO.CODCOLPRD | COD\_COLIGADA | Código de Coligada |
| TPRODUTO.IDPRD | COD\_PRODUTO | Código de Produto |
| TPRODUTO.NOMEFANTASIA | NOME\_PRODUTO | Nome de Produto |

Transportadora (TTRA)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| TTRA.CODCOLIGADA | COD\_COLIGADA | Código de Coligada |
| TTRA.CODTRA | COD\_TRANSPORTADORA | Código de Transportadora |
| TTRA.NOME | NOME\_TRANSPORTADORA | Nome de Transportadora |
| TTRA.NOMEFANTASIA | NOME\_FANTASIA\_TRANSPORTADORA | Nome de Transportadora |

Unidade de Medida (TUND)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| TUND.CODUND | COD\_UND | Código de Unidade de Medida |
| TUND.DESCRICAO | NOME\_UND | Nome de Unidade de Medida |
| TUND.CODUNDBASE | NOME\_ABREV\_UND | Nome Abreviado de Unidade de Medida |

Vendedor (TVEN)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| TVEN.CODCOLIGADA | COD\_COLIGADA | Código de Coligada |
| TVEN.CODVEN | COD\_VENDEDOR | Código de Vendedor |
| TVEN.NOME | NOME\_VENDEDOR | Nome de Vendedor |

Natureza (CFOP)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| DCFOP.CODCOLIGADA | COD\_COLIGADA | Código de Coligada |
| DCFOP.IDNAT | COD\_CFOP |  |
| DCFOP.NOME | NOME |  |

Centro de Custos (GCCUSTO)

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| GCCUSTO.CODCOLIGADA | COD\_COLIGADA | Código de Coligada |
| DCFOP.CODCCUSTO | CODCCUSTOPAI | Código de Centro de Custos Pai |
| GCCUSTO.NOME | DESCRICAO | Descrição de Centro de Custos |

ctb\_fatosFatos

Segue o nome e detalhamento das fatos utilizadas:

**Faturamento**:

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| FCFO.CODCOLIGADA|FCFO.CODCFO | ID\_CLIENTE | Código do Cliente |
| TMOV.CODTB1FAT | ID\_GRUPO\_ESTOQUE | Código de Grupo de Estoque |
| TMOV.CODCOLIGADA | ID\_COLIGADA | Código de Coligada |
| GFILIAL.CODFILIAL | ID\_FILIAL | Código de Filial |
| TITMMOV.IDPRD | ID\_PRODUTO | Código de Produto |
| TVEN.CODVEN | ID\_VENDEDOR | Código de Vendedor |
| TCPG.CODCPG | ID\_CONDICAO\_PAGAMENTO | Código de Condição de Pagamento |
| TITMMOV.CODUND | ID\_UNIDADE\_MEDIDA | Código de Unidade de Medida |
| TMOV.IDNAT | ID\_CFOP | Código de Natureza |
| TCFOGRUPOCF.GRUPOCF | ID\_GRUPO\_CLIENTE | Código de Grupo de Cliente |
| TMOV.DATAMOVIMENTO | DATA | Data do Faturamento |
| TMOV.DATASAIDA | DATA\_SAIDA\_NF | Data de Saída do Faturamento |
| TMOV.DATAMOVIMENTO | DATA\_COMP | Data do Faturamento |
| TMOV.VALORLIQUIDO | VALOR\_FATURAMENTO\_TOTAL | Valor total de faturamento |
| TTRBMOV.VALOR | VALOR\_ICMS\_FATURAMENTO | Valor de ICMS no faturamento |
| TTRBMOV.VALOR | VALOR\_IPI\_FATURAMENTO | Valor de IPI no faturamento |
| TTRBMOV.VALOR | VALOR\_PIS\_FATURAMENTO | Valor de PIS no faturamento |
| TTRBMOV.VALOR | VALOR\_COFINS\_FATURAMENTO | Valor de CONFINS no faturamento |
| TTRBMOV.VALOR | VALOR\_ISS\_FATURAMENTO | Valor de ISS no faturamento |
| TTRBMOV.VALOR | VALOR\_ICMS\_SUBST\_FATURAMENTO | Valor de SUBST no faturamento |
| TTRBMOV.VALOR | VALOR\_IRF\_FATURAMENTO | Valor de IRF no faturamento |
| TTRBMOV.VALOR | VALOR\_INSS\_FATURAMENTO | Valor de INSS no faturamento |
| TMOV.PESOLIQUIDO | PESO\_LIQUIDO | Peso Liquido |
| TMOV.VALORDESC | VALOR\_DESCONTO\_FATURAMENTO | Valor de desconto no faturamento |
| TMOV.VALORFRETE | VALOR\_FRETE\_NOTA\_FISCAL | Valor de frete no faturamento |
| TMOV.VALORDESP | VALOR\_DESPESA | Valor de despesa |
| TITMMOV.VALORTOTALITEM | VALOR\_FATURAMENTO\_MERCADORIA | Valor faturamento em mercadoria |
| TITMMOV.QUANTIDADE | QUANTIDADE\_FATURADA\_ITEM | Quantidade faturada de mercadoria |
| TMOV.PESOBRUTO | PESO\_BRUTO | Peso Bruto |
| TITMMOV.PRECOUNITARIO | VALOR\_UNITARIO | Valor Unitário de mercadoria |
| TMOV.SERIE | SERIE\_NOTA\_FISCAL | Serie de Nota Fiscal |
| TMOV.NUMEROMOV | NUMERO\_NOTA\_FISCAL | Número de Nota Fiscal |
| TMOVORIGEM.NUMEROMOV | NUMERO\_PEDIDO\_VENDA | Número de Pedido Venda |
| TITMMOV.NUMEROSEQUENCIAL | NUMERO\_ITEM | Número do item |
| MOV.FRETECIFOUFOB | TIPO\_FRETE | O tipo de Frete.  0 = TERCEIROS; 1 = CIF; 2 = FOB; 3 = REMETENTE; 4 = DESTINATÁRIO; 9 = SEM\_FRETE. |
| FTDO.CODMODDOC | TIPO\_NOTA\_FISCAL | Tipo de Nota Fiscal  (Entrada/Saída) |
| TMOV.INTEGRAAPLICACAO | ORIGEM\_LANCAMENTO | Origem de Lançamento |

**Devolução**:

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| FCFO.CODCOLIGADA|TMOV.CODCFO | ID\_CLIENTE | Código de Cliente |
| TITMMOV.CODTB1FAT | ID\_GRUPO\_ESTOQUE | Código de Grupo de Estoque |
| TMOV.CODCOLIGADA | ID\_COLIGADA | Código de Coligada |
| TMOV.CODFILIAL | ID\_FILIAL | Código de Filial |
| TITMMOV.IDPRD | ID\_PRODUTO | Código de Produto |
| TMOV.CODVEN1 | ID\_VENDEDOR | Código de Vendedor |
| TMOV.CODCPG | ID\_CONDICAO\_PAGAMENTO | Código de Condição de Pagamento |
| TITMMOV.CODUND | ID\_UNIDADE\_MEDIDA | Código de Unidade de Medida |
| TMOV.IDNAT | ID\_CFOP | Código de Natureza |
| TMOV.DATAMOVIMENTO | DATA | Data de Devolução |
| TITMMOV.QUANTIDADE | QTDE\_DEVOLVIDA\_ITEM | Quantidade Devolvida de Item |
| TTRBMOV.VALOR | VALOR\_ICMS\_DEVOLUCAO | Valor de IMCS na Devolução |
| TTRBMOV.VALOR | VALOR\_ICMS\_SUBST\_DEVOLUCAO | Valor de IMCS Subistituto na Devolução |
| TTRBMOV.VALOR | VALOR\_IPI\_DEVOLUCAO | Valor de IPI na Devolução |
| TTRBMOV.VALOR | VALOR\_PIS\_DEVOLUCAO | Valor de PIS na Devolução |
| TTRBMOV.VALOR | VALOR\_COFINS\_DEVOLUCAO | Valor de CONFINS na Devolução |
| TTRBMOV.VALOR | VALOR\_INSS\_DEVOLUCAO | Valor de INSS na Devolução |
| TITMMOV.VALORLIQUIDO -TTRBMOV.VALOR | VALOR\_DEVOLUCAO\_LIQUIDO | Tributo = ICMS |
| TITMMOV.VALORLIQUIDO | VALOR\_DEVOLUCAO\_MERCADORIA | Valor de Devolução de mercadoria |
| TITMMOV.VALORLIQUIDO +  TITMMOV.VALORDESP +  TITMMOV.RATEIODESP -TITMMOV.VALORDESC -TITMMOV.RATEIODESC | VALOR\_DEVOLUCAO\_TOTAL | Valor de Devolução Total |
| TITMMOV.VALORDESC +  TITMMOV.RATEIODESC | VALOR\_DESCONTO\_DEVOLUCAO | Valor de Desconto em Devolução |
| TMOV.SERIE | SERIE\_DOCUMENTO\_CLIENTE | Serie de documento |
| TMOV.NUMEROMOV | NUMERO\_DOCUMENTO\_CLIENTE | Número de documento |
| TMOVNOTA.SERIE | SERIE\_NOTA\_FISCAL | Serie de Nota Fiscal |
| TMOVNOTA.NUMEROMOV | NUMERO\_NOTA\_FISCAL | Número de Nota Fiscal |
| TITMMOV.NUMEROSEQUENCIAL | NUMERO\_ITEM\_DOCUMENTO | Número de item |
| TITMMOVNOTA.NUMEROSEQUENCIAL | NUMERO\_ITEM\_NOTA\_FISCAL | Número de item |

**Pedidos**:

| Campo RM | Campo Fast | Descrição |
| --- | --- | --- |
| TMOV.CODCOLIGADA|TMOV.CODCFO | ID\_CLIENTE | Código de Cliente |
| TMOV.CODCOLIGADA | ID\_COLIGADA | Código de Coligada |
| GFILIAL.CODFILIAL | ID\_FILIAL | Código de Filial |
| TITMMOV.IDPRD | ID\_PRODUTO | Código de Produto |
| TVEN.CODVEN | ID\_VENDEDOR | Código de Vendedor |
| TCPG.CODCPG | ID\_CONDICAO\_PAGAMENTO | Código de Condição de Pagamento |
| TMOV.IDNAT | ID\_CFOP | Código Natureza |
| TMOV.DATAMOVIMENTO | DATA | Data de Pedido |
| TITMMOV.DATAENTREGA | DATA\_ENTREGA | Data de entrega de pedido |
| TMOV.VALORLIQUIDO | VALOR\_VENDA\_TOTAL | Valor de Venda Total |
| TITMMOV.QUANTIDADE | QUANTIDADE\_VENDIDA | Quantidade Vendida |
| TITMMOV.PRECOUNITARIO | VALOR\_PRECO\_UNITARIO | Valor preço unitário |
| TITMMOV.STATUS | SITUACAO\_ITEM\_PEDIDO | Situação do Item no pedido |
| TMOV.NUMEROMOV | NUMERO\_PEDIDO | Número de pedido |
| TITMMOV.NUMEROSEQUENCIAL | NUMERO\_ITEM | Número de item |
| STATUS | STATUS\_PEDIDO | A,P,N,E,O,G  = ABERTO;  L = LIBERADO;  F,Q,Z,C,D = ENCERRADO;  R,Y,B,U,I = BLOQUEIO;  B = VERBA. |
