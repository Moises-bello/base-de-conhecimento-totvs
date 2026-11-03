---
content_hash: ec791a11f98dbcc0e717c9edc4400848c9e654b1ffbccb33c0410c957dc9287b
fetched_at: '2026-06-29T00:06:25.677418+00:00'
page_id: '224442717'
product: rm
source: tdn-rm
title: ER_PCREQ-9420_Relatorio_de_Analise_de_Valor_Agregado_por_Centro_de_Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9420_Relatorio_de_Analise_de_Valor_Agregado_por_Centro_de_Custo
version: 171
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Obras e Projetos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP011 | **IRM1** | PCREQ-9419 |
| **Requisito1** | PCREQ-9420 | **Subtarefa1** | PDR\_CP\_TOP010-86 |
| **Chamado2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Este documento tem por objetivo apresentar as implementações necessárias para cálculo e visão da Análise de Valor Agregado por Centro de Custo e demais processos necessários para correta alimentação da base de dados, listadas abaixo:

* Alteração da origem de dados do relatório de Análise de Valor Agregado
* Criação da visão e cálculo do relatório de Análise de Valor Agregado por Centro de Custo
* Processo de Replanejamento da Linha de Base
* Apropriação de Mão de Obra Indireta
* Ajustes e fluxos de apropriação de custo
  + Apropriação de custo de equipamento por integração com módulo de manutenção.
  + Apropriação de custo de contratos no momento da liberação do período.

## Definição da Regra de Negócio

## RN01 - Alteração da origem de dados do relatório de Análise de Valor Agregado

Atualmente o relatório de Análise de Valor Agregado  permite que os dados sejam extraídos por origem padrão ou através de fórmula. 

 Após análise aprofundada dos processos e conhecimento de uso da ferramenta pelo mercado, identificamos inicialmente duas divergências com a origem de dados considerada ideal, listadas abaixo:

1. Origem do Valor planejado
   1. Atualmente o Cronograma Planejado é considerado no cálculo do valor planejado, mas é considerado como ideal a obtenção dos dados a partir da Linha Base.
   2. Visando disponibilizar o correto cálculo, mas também permitir que usuários utilizem o Cronograma Planejado caso desejem, será criado o parâmetro "Utilizar linha base como valor planejado (COTA)", que será considerado como default a partir da liberação deste requisito. Caminho do parâmetro: Parâmetros de Projeto >> Projeto
2. Origem do Custo Real
   1. Atualmente o Custo Real é obtido a partir do Cronograma Medido, sendo considerado como ideal a obtenção a partir do Valor Apropriado.
   2. O cálculo padrão será alterado para obter o CR a partir do Valor Apropriado.

Este modelo foi analisado e considerado ideal por possuir melhor aderência com os processos de cópia de linha base e replanejamento, além de ser o modelo utilizado por um grande número de clientes através da implementação de fórmulas.

|  | COTA | VP | COTR | VA | CRTR | CR |
| --- | --- | --- | --- |
| Modelo Antigo | Valor do Cronograma Planejado | Valor do Cronograma Realizado | Valor do Cronograma Medido |
| Novo Modelo - Utilizando Cronograma Planejado | Valor do Cronograma Planejado | Valor do Cronograma Realizado | Valor Apropriado |
| Novo Modelo - Utilizando Linha Base | Valor da Linha Base | Valor agregado considerando custo  unitário da linha base\* | Valor Apropriado |

**\* **O cálculo obterá o valor agregado a partir da quantidade realizada e o valor unitário da Linha Base,**conforme a seguinte fórmula:**

**COTR (VA) = Quantidade Realizada (Cronograma Realizado) \* ( Valor da Linha Base / Quantidade da Linha Base).**

**O cálculo do COTR deve ser realizado a cada período para que os valores estejam corretos.**

**Exemplo:**

**Tarefa 1 no Período 1 => 5,00 \* (60,00 / 4,00) = 75,00**

**Tarefa 1 no Período 2 => 5,00 \* (40,00 / 6,00) = 33,33**

**TOTAL = SOMA dos 2 Períodos => 108,33**

**Obs.: Caso não haja Linha Base no período será considerada a seguinte lógica de precedência:**

1. **Caso haja Linha Base no período será obtido o valor do mesmo.**
2. **Não havendo Linha Base no período, o valor será obtido a partir da Linha Base do período anterior ao atual (o primeiro mais próximo).**
3. **Não havendo Linha Base no período e nem em períodos anteriores, o valor será obtido a partir da primeira Linha Base encontrada nos períodos posteriores.**

**Exemplo de uso do parâmetro "Utilizar linha base como valor planejado (COTA)"**

O valor deste parâmetro deve ser escolhido com base na forma de uso do cronograma por parte do cliente.

Caso o cliente faça replanejamentos recorrentes, utilizando o Cronograma Planejado como COTA todos os indicadores informariam que o realizado foi exatamente o executado (para os períodos já executados), não trazendo a visão desejada. Visando estes casos, considerados como maioria, foi implementado o parâmetro para considerar a Linha Base como COTA e este foi considerado como comportamento padrão.

Exemplificando o uso da Linha Base como COTA, no momento em que o planejamento foi finalizado e oficializado com a área executiva da empresa seria feita a cópia do Cronograma Planejado para Linha Base. A partir deste momento o Cronograma Planejado pode ser replanejado conforme qualquer necessidade, pois a comparação da Análise de Valor Agregado será executada sempre com relação à Linha Base e assim apresentará como planejamento os valores acordados com a alta gestão. Caso haja um novo realinhamento com a alta gestão será necessário somente efetuar nova cópia do Cronograma Planejado para a Linha Base.

**Protótipo de tela do parâmetro "Utilizar linha base como valor planejado (COTA)"**

## RN02 - Análise de Valor Agregado por Centro de Custo

A visão do relatório de Análise de Valor Agregado por Centro de Custo consolidará os valores calculados no processo a partir da informação de centro de custo das tarefas (vide regra de obtenção abaixo), apresentando os indicadores do período atual (selecionado como período de referência no processamento) e dos períodos acumulados. Seguindo a premissa de execução padrão do relatório, o mesmo somente poderá ser executado para a planilha de atividades e cenário principal.

Os cálculos por Centro de Custo serão executados no mesmo processamento que atualmente faz os cálculos por Obra/Etapa/Tarefa, caso o parâmetro "Calcular Índices de Tarefas por Centro de Custo" esteja marcado.

Os valores calculados no processamento serão armazenados na base de dados para visualização futura. Esta implementação se faz necessária pois esta deve ser uma foto da situação no momento do processamento e caso a consolidação por centro de custos fosse efetuada no momento da visualização os dados poderiam ser diferentes, por exemplo devido a alterações nos rateios de centro de custo após a execução do processo.

O relatório será apresentado no padrão de Grid do RM, assim permitindo exportação para Excel, geração de gráficos, agrupamento por colunas e outras funcionalidades.

As informações totalizadas (todos os centros de custo) serão apresentadas na primeira linha do relatório, seguida pelas linhas de cada centro de custo identificados também pelos respectivos responsáveis.

****Regras do parâmetro de execução por Centro de Custo****

1. Somente será permitido executar o cálculo por Centro de Custo caso o cálculo por Tarefas também esteja marcado para execução. 
   1. Caso não esteja marcado para calcular por Tarefa o controle de cálculo por Centro de Custo será desabilitado e terá valor "desmarcado".
2. Caso o parâmetro de cálculo por Centro de Custo esteja marcado, obrigatoriamente será selecionado o parâmetro "Acumular valores por período".
   1. Caso esteja marcado para calcular por Centro de Custo o controle "Acumular valores por período" será desabilitado e terá valor "marcado".

**Protótipo da tela**

**Consolidação por centro de custo das Tarefas -**Os centros de custo para os quais os valores devem ser rateados serão sempre obtidos a partir do rateio de centro de custos das tarefas, seguindo a regra de ordem padrão do TOP (listada abaixo), desconsiderando assim possíveis rateios divergentes no movimento ou outras fontes de dados.

 **Cálculo e armazenamento das informações -** O cálculo e armazenamento das informações será efetuado com comportamento padrão e conforme os parâmetros de execução do processo. 

O valores calculados serão armazenados por período e com a informação acumulada por períodos, devendo ser consolidado entre período atual e acumulado conforme o layout do relatório na própria rotina.

A visão do relatório deverá apresentar os indicadores obtidos na base de dados para o período atual, referente ao parâmetro de processamento, nos campos que possuem sempre o valor acumulado e efetuar o cálculo dos campos referente ao período atual a partir da informação deste e do período anterior.

 **Ordem de obtenção dos centros de custo**

1. **Rateio de centro de custo da Tarefa**
2. **Rateio de centro de custo das Etapas superiores**
3. **Rateio de centro de custo da Obra**
4. **Centro de custo do Projeto**

**Layout do relatório**

**Fórmulas de cálculo da Análise de Valor Agregado ( não modificadas ):**

* **IDP = VA / VP**
* **IDC = VA / CR**
* **VC (Variação de Custo) = VA - CR**
* **Variação de Prazo = VA - VP**
* **VC % (Variação de Custo) = (VA - CR) / CR**
* **Variação de Prazo % = (VA - VP) / VP**
* **EPT (Variações **Atípicas**) = Custo Total - VA**
  + Esta fórmula desconsidera que o ganho ou perda de produtividade deve ser desconsiderado na estimativa, ou seja, que foi atípico e não continuará ocorrendo.
* **EPT (Variações **Típicas**) = (**Custo Total - VA)** / IDC**
  + Esta fórmula considera que o ganho ou perda de produtividade até o período ocorrerá também nos períodos futuros, assim o considerando para o cálculo da estimativa restante para terminar.
* **ENT **(Utilizando orçamento restante) = (Custo Total – VA) + ****CR********
  + Esta fórmula considera que a estimativa no término (valor gasto ao final do projeto) será o valor gasto até o momento somado à estimativa para terminar com variações típicas, ou seja, desconsiderando o ganho ou perda de produtividade.
* ********ENT (Utilizando IDC) = (****(Custo Total – VA)/ IDC ) + ****CR****************
  + Esta fórmula considera que a estimativa no término (valor gasto ao final do projeto) será o valor gasto até o momento somado à estimativa para terminar com variações atípicas, ou seja, considerando o ganho ou perda de produtividade.

## Demais cálculos:

* Custo Total:
  + Totalizador: Soma dos VP's de todos os Centros de Custo no último período
  + Por Centro de Custo: VP no último período
* Saldo:
  + Totalizador: Soma dos VP's de todos os Centros de Custo no último período - Soma dos CR's de todos os Centros de Custo no período atual
  + Por Centro de Custo: VP no último período - CR no período atual

## RN03 - Alteração do processo de Cópia da Linha Base

O processo de Cópia da Linha Base será alterado para permitir que nos períodos já realizados seja copiado para o Valor Base o valor apropriado no período, em detrimento ao comportamento atual que efetua a cópia do valor previsto. A seleção entre os dois comportamentos será efetuado a partir do parâmetro de projeto "**Obter Valor da Linha Base a partir do Valor Apropriado para períodos fechados anteriores"**, que possui por padrão o comportamento atual.

**Simulação -****Base de dados Inicial**

|  | | Período 1 | Período 2 | Período 3 | Período 4 | Período 5 | Período 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Linha Base | Qtd | 5 | 10 | 10 | 10 | 10 | 10 |
| R$ | 50 | 100 | 100 | 100 | 100 | 100 |
| Previsto | Qtd | 5 | 10 | 10 | 10 | 10 | 10 |
| R$ | 60 | 120 | 130 | 130 | 130 | 130 |
| Realizado | Qtd | 3 | 8 | 10 |  |  |  |
| R$ | 36 | 96 | 130 |  |  |  |
| Apropriado | R$ | 50 | 110 | 150 |  |  |  |

**Base de dados após replanejamento**

|  | | Período 1 | Período 2 | Período 3 | Período 4 | Período 5 | Período 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Linha Base | Qtd | 5 | 10 | 10 | 10 | 10 | 10 |
| R$ | 50 | 100 | 100 | 100 | 100 | 100 |
| Previsto | Qtd | 3 | 8 | 10 | 12 | 11 | 11 |
| R$ | 36 | 96 | 130 | 156 | 143 | 143 |
| Realizado | Qtd | 3 | 8 | 10 |  |  |  |
| R$ | 36 | 96 | 130 |  |  |  |
| Apropriado | R$ | 50 | 110 | 150 |  |  |  |

****Base de dados após Cópia de Linha Base****

* **Parâmetro **"O**btenção do valor de cópia a partir do cronograma apropriado"****inativo**

|  | | Período 1 | Período 2 | Período 3 | Período 4 | Período 5 | Período 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Linha Base | Qtd | 3 | 8 | 10 | 12 | 11 | 11 |
| R$ | 36 | 96 | 130 | 156 | 143 | 143 |
| Previsto | Qtd | 3 | 8 | 10 | 12 | 11 | 11 |
| R$ | 36 | 96 | 130 | 156 | 143 | 143 |
| Realizado | Qtd | 3 | 8 | 10 |  |  |  |
| R$ | 36 | 96 | 130 |  |  |  |
| Apropriado | R$ | 50 | 110 | 150 |  |  |  |

Conforme o comportamento padrão do processo os valores são alterados conforme lógica abaixo:

Para todos os períodos

Previsto (Qtd) → Linha Base (Qtd)  
Previsto (R$)  → Linha Base (R$)

****Base de dados após Cópia de Linha Base****

* **Parâmetro "O**btenção do valor de cópia a partir do cronograma apropriado"**ativo**
* ****Parâmetro "Período Inicial" de travamento do cronograma Previsto = 3****

|  | | Período 1 | Período 2 | Período 3 | Período 4 | Período 5 | Período 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Linha Base | Qtd | 3 | 8 | 10 | 12 | 11 | 11 |
| R$ | 50 | 110 | 150 | 156 | 143 | 143 |
| Previsto | Qtd | 3 | 8 | 10 | 12 | 11 | 11 |
| R$ | 36 | 96 | 130 | 156 | 143 | 143 |
| Realizado | Qtd | 3 | 8 | 10 |  |  |  |
| R$ | 36 | 96 | 130 |  |  |  |
| Apropriado | R$ | 50 | 110 | 150 |  |  |  |

Conforme o comportamento para o parâmetro ativo os valores são alterados conforme lógica abaixo:

Para os períodos já executados (períodos anteriores travados)

Previsto (Qtd) → Linha Base (Qtd)  
Apropriado (R$) →  Linha Base (R$)

Para os períodos futuros

Previsto (Qtd) → Linha Base (Qtd)  
Previsto (R$)  → Linha Base (R$)

## RN05 - Apropriação de Mão de Obra Indireta

O TOTVS Obras e Projetos apresenta diferentes formas para apropriação de Mão de Obra Indireta, listadas abaixo:

**Apropriação de Mão de Obra Indireta por importação ou manualmente**

Caso não haja integração com software de Folha de Pagamento (Ponto Eletrônico) não haverá automação de apontamentos de mão de obra (direta ou indireta), sendo necessário efetuar a apropriação manualmente a partir da rotina "Apropriação de Serviços/Insumos" para que os custos sejam aplicados no cronograma apropriado e consequentemente no relatório de Análise de Valor Agregado.

******Apropriação de Mão de Obra Indireta a partir do processo de revaloração******

O processo de Revaloração de Mão de Obra será alterado para se tornar responsável também pela apropriação de custos de Mão de Obra Indireta, considerando como Mão de Obra Indireta todos os funcionários pertencentes a alguma equipe do Projeto (mobilidade, risco ou timesheet) mas que não possuírem nenhum apontamento no período.

**Origem dos dados**

Será considerado como quantidade de horas trabalhadas e o custo do funcionário no período os valores retornados pelo processo na consulta ao software de Folha de Pagamento (Ponto Eletrônico) configurado.

**Rateio de tarefas**

O rateio de tarefas dos apontamentos será efetuado conforme regra de precedência apresentada abaixo:

**Existe alocação para o funcionário?**

**Sim** => O rateio dos custos do funcionário será realizado irmãmente pelas tarefas às quais este recurso possui alocação, desconsiderando a quantidade de alocação.

**Não** => O rateio dos custos do funcionário será realizado irmãmente pelas tarefas às quais a sua função estiver associado ao insumo ou composição vinculados.

## RN06 - Ajustes e fluxos de Apropriação de Custos

Visando viabilizar fluxos alternativos para Apropriação de Custos quando integrado ao BackOffice Protheus serão criados novo parâmetro de projeto e na tela de contratos responsáveis por informar o momento da apropriação do mesmo. Atualmente o processo viabiliza somente a apropriação a partir da Nota Fiscal retornada pelo BackOffice Protheus, sendo este também informado como o valor padrão do novo parâmetro criado.

**Parâmetros**

* Parâmetro de projeto: "Apropriar liberação em"

Parâmetro está localizado no caminho "Parâmetros do Projeto → Contratos → Liberação" e informa em qual ponto deve ser executada a apropriação da liberação do contrato, caso o mesmo esteja parametrizado para gerar apropriação.

* Parâmetro de contrato: "Apropria liberação de Período"

Parâmetro está localizado no caminho "Cadastro de Contrato → Defaults" e informa se a liberação do período deve gerar apropriação ao integrar com o módulo de Suprimento/Faturamento.

**Visibilidade dos parâmetros**

Os parâmetros estarão disponíveis somente em ambientes integrados ao BackOffice Protheus via Mensagem Única (novo modelo), uma vez que em integração com o BackOffice RM o processo de apropriação deve ser definido a partir do encadeamento de tipos de movimento, como já é feito nos clientes atualmente.

O parâmetro da tela de contratos não será visível em contratos com finalidade de 'Fornecimento de Materiais' ou qualquer contrato do tipo 'A Receber', pois contratos a receber não devem ser apropriados e contratos te fornecimento de materiais geram solicitações de compra e assim sendo devem ser apropriados sempre no retorno da nota fiscal. A apropriação não deve ser executada a partir das solicitações de compra pois os valores serão alterados durante o fluxo de compras.

**Valores dos parâmetros e fluxos viabilizados**

Os novos parâmetros podem possuir os seguintes valores e respectivos comportamentos:

* 'Apropria liberação de Período' = 'Desmarcado'
  + Caso o parâmetro do contrato informe que não gera apropriação na liberação do período o mesmo não gerará apropriação do Pedido do Nucleus e nem enviará ao Pedido do Protheus as informações de rateio de tarefas, assim não apropriando no Pedido e nem na Nota Fiscal.
  + Esta opção deve ser utilizara para contratos ou clientes que não desejam utilizar apropriação automática na integração com Suprimento/Faturamento, sendo o mesmo efetuado manualmente ou a partir de outro sistema, como na apropriação de materiais a partir do SigaMNT.
* 'Apropriar liberação em:' = 'Pedido de Compra' e  'Apropria liberação de Período' = 'Marcado'  
  + Utilizando esta combinação parâmetro a apropriação será efetuada no Pedido do Nucleus, mas não será enviada informação de tarefas para o Protheus para que não haja apropriação na Nota Fiscal.
  + Esta opção deve ser utilizara para contratos ou clientes que não desejem efetuar a apropriação das Liberações de Período imediatamente no momento da execução do processo. Ou seja, será apropriado exatamente o valor da liberação e na mesma data.
* 'Apropriar liberação em:' = 'Nota Fiscal' e  'Apropria liberação de Período' = 'Marcado'  
  + Utilizando este parâmetro a apropriação será efetuada a partir da Nota Fiscal retornada pelo Protheus. Assim sendo, a informação do rateio de tarefas será enviada ao Protheus para propagação até a Nota Fiscal e posterior retorno, mas não será gerado apropriação no Pedido do Nucleus para que o mesmo não seja apropriado em duplicidade.
  + Esta opção deve ser utilizara para contratos ou clientes que desejem efetuar a apropriação das Liberações de Período no momento do retorno das Notas Fiscais. Ou seja, será apropriado exatamente o valor da liberação e na mesma data.

****Tipos de movimento****

Os tipos de movimento de Pedido de Compra e Nota Fiscal utilizados na integração com BackOffice Protheus serão alterados para receber rateio de tarefa por itens de forma opcional e para gerar apropriação. Assim sendo, caso seja inserida a informação de tarefa no rateio o movimento automaticamente efetuará a sua apropriação, sendo o controle de inserção de tarefa de responsabilidade dos parâmetrossupracitado.

**Exemplo de fluxos de apropriação**

****Fluxo com integração com BackOffice Protheus (Padrão)****

**Parâmetros da simulação**

* + Integração com Protheus ativa.
  + Integração com SigaMNT inativa.
  + Parâmetro 'Apropriar liberação em:' com valor 'Nota Fiscal'
  + Todos os contratos - 'Apropria liberação de Período' com valor 'Marcado'.

**Fluxo com integração com ****BackOffice Protheus, integração de apontamentos com****SigaMNT e apropriação de contratos de serviço na liberação**

**Parâmetros da simulação**

* + Integração com Protheus ativa.
  + Integração com SigaMNT ativa.
  + Parâmetro 'Apropriar liberação em:' com valor 'Pedido de Compra'.
  + Contrato de fornecimento de Materiais - Comportamento padrão (não possui parametrização).
  + Contrato de prestação de serviços - 'Apropria liberação de Período' com valor 'Marcado'.
  + Contrato de equipamentos - 'Apropria liberação de Período' com valor 'Desmarcado'.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| PrjAvaGravarIndicesProcAction | Processo de Cálculo | RM >> Gestão de obras e Projetos >> Controle >> Análise de Valor Agregado >> Processo "Calcular Índices" | RN01 , RN02 |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
