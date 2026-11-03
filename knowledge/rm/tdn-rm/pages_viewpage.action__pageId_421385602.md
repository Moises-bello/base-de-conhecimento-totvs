---
content_hash: 0b6b9cb79b2f850d06ef7232f48d09622babd18592d0af582c1eca1b5b45d2d9
fetched_at: '2026-06-29T00:09:16.884472+00:00'
page_id: '421385602'
product: rm
source: tdn-rm
title: Análise de Valor Agregado por Centro de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385602
version: 4
---

A visão do relatório de Análise de Valor Agregado por Centro de Custo consolidará os valores calculados no processo a partir da informação de centro de custo das tarefas (vide regra de obtenção abaixo), apresentando os indicadores do período atual (selecionado como período de referência no processamento) e dos períodos acumulados. Seguindo a premissa de execução padrão do relatório, o mesmo somente poderá ser executado para a planilha de atividades e cenário principal   
  
 Os cálculos por Centro de Custo serão executados no mesmo processamento que atualmente faz os cálculos por Obra/Etapa/Tarefa, caso o parâmetro "Calcular Índices de Tarefas por Centro de Custo" esteja marcado.  
  
 Os valores calculados no processamento serão armazenados na base de dados para visualização futura. Esta implementação se faz necessária pois esta deve ser uma foto da situação no momento do processamento e caso a consolidação por centro de custos fosse efetuada no momento da visualização os dados poderiam ser diferentes, por exemplo devido a alterações nos rateios de centro de custo após a execução do processo.  
  
 O relatório será apresentado no padrão de Grid do RM, assim permitindo exportação para Excel, geração de gráficos, agrupamento por colunas e outras funcionalidades.  
  
 As informações totalizadas (todos os centros de custo) serão apresentadas na primeira linha do relatório, seguida pelas linhas de cada centro de custo identificados também pelos respectivos responsáveis.

**Regras do parâmetro de execução por Centro de Custo**

1. Somente será permitido executar o cálculo por Centro de Custo caso o cálculo por Tarefas também esteja marcado para execução.   
a.Caso não esteja marcado para calcular por Tarefa o controle de cálculo por Centro de Custo será desabilitado e terá valor "desmarcado".  
2. Caso o parâmetro de cálculo por Centro de Custo esteja marcado, obrigatoriamente será selecionado o parâmetro "Acumular valores por período".  
a. Caso esteja marcado para calcular por Centro de Custo o controle "Acumular valores por período" será desabilitado e terá valor "marcado".

**Ordem de obtenção dos centros de custo**  
3.Rateio de centro de custo da Tarefa  
4.Rateio de centro de custo das Etapas superiores  
5.Rateio de centro de custo da Obra  
6.Centro de custo do Projeto

**Fórmulas de cálculo da Análise de Valor Agregado (não modificadas):**  
·          **IDP = VA / VP**  
·          **IDC = VA / CR**  
·          **VC (Variação de Custo) = VA - CR**  
·          **Variação de Prazo = VA - VP**  
·          **VC % (Variação de Custo) = (VA - CR) / CR**  
·          **Variação de Prazo % = (VA - VP) / VP**  
·          **EPT (Variações Típicas) = Custo Total - VA**  
Esta fórmula desconsidera o ganho ou perda de produtividade até o período para o cálculo da estimativa restante para terminar.  
·          **EPT (Variações Atípicas) = (Custo Total - VA) / IDC**  
Esta fórmula considera que o ganho ou perda de produtividade até o período ocorrerá também nos períodos futuros, assim o considerando para o cálculo da estimativa restante para terminar.  
·          **ENT (Utilizando orçamento restante) = (Custo Total – VA) + CR**  
Esta fórmula considera que a estimativa no término (valor gasto ao final do projeto) será o valor gasto até o momento somado à estimativa para terminar com variações típicas, ou seja, desconsiderando o ganho ou perda de produtividade.  
·          **ENT (Utilizando IDC) = ((Custo Total – VA) / IDC ) + CR**  
Esta fórmula considera que a estimativa no término (valor gasto ao final do projeto) será o valor gasto até o momento somado à estimativa para terminar com variações atípicas, ou seja, considerando o ganho ou perda de produtividade.

**Demais cálculos:**  
Custo Total:  
Totalizador: Soma dos VP's de todos os Centros de Custo no último período  
Por Centro de Custo: VP no último período  
Saldo:  
Totalizador: Soma dos VP's de todos os Centros de Custo no último período - Soma dos CR's de todos os Centros de Custo no período atual  
Por Centro de Custo: VP no último período - CR no período atual  
**RN03 - Alteração do processo de Cópia da Linha Base**  
O processo de Cópia da Linha Base será alterado para permitir que nos períodos já realizados seja copiado para o Valor Base o valor apropriado no período, em detrimento ao comportamento atual que efetua a cópia do valor previsto. A seleção entre os dois comportamentos será efetuado a partir do parâmetro de projeto **"Obter Valor da Linha Base a partir do Valor Apropriado para períodos fechados anteriores"**, que possui por padrão o comportamento atual.  
**RN05 - Apropriação de Mão de Obra Indireta**

**RN06 - Ajustes e fluxos de Apropriação de Custos**  
Visando viabilizar fluxos alternativos para Apropriação de Custos quando integrado ao BackOffice Protheus serão criados novo parâmetro de projeto e na tela de contratos responsáveis por informar o momento da apropriação do mesmo. Atualmente o processo viabiliza somente a apropriação a partir da Nota Fiscal retornada pelo BackOffice Protheus, sendo este também informado como o valor padrão do novo parâmetro criado.

**Consolidação por centro de custo das Tarefas -**Os centros de custo para os quais os valores devem ser rateados serão sempre obtidos a partir do rateio de centro de custos das tarefas, seguindo a regra de ordem padrão do TOP (listada abaixo), desconsiderando assim possíveis rateios divergentes no movimento ou outras fontes de dados.

**Cálculo e armazenamento das informações** - O cálculo e armazenamento das informações será efetuado com comportamento padrão e conforme os parâmetros de execução do processo.   
Os valores calculados serão armazenados por período e com a informação acumulada por períodos, devendo ser consolidado entre período atual e acumulado conforme o layout do relatório na própria rotina.  
A visão do relatório deverá apresentar os indicadores obtidos na base de dados para o período atual, referente ao parâmetro de processamento, nos campos que possuem sempre o valor acumulado e efetuar o cálculo dos campos referente ao período atual a partir da informação deste e do período anterior.

O Totvs Obras e Projetos apresentam diferentes formas para apropriação de Mão de Obra Indireta, listadas abaixo:  
**Apropriação de Mão de Obra Indireta por importação ou manualmente**  
Caso não haja integração com software de Folha de Pagamento (Ponto Eletrônico) não haverá automação de apontamentos de mão de obra (direta ou indireta), sendo necessário efetuar a apropriação manualmente a partir da rotina "Apropriação de Serviços/Insumos" para que os custos sejam aplicados no cronograma apropriado e consequentemente no relatório de Análise de Valor Agregado.  
**Apropriação de Mão de Obra Indireta a partir do processo de revaloração**  
O processo de Revaloração de Mão de Obra será alterado para se tornar responsável também pela apropriação de custos de Mão de Obra Indireta, considerando como Mão de Obra Indireta todos os funcionários pertencentes a alguma equipe do Projeto (mobilidade, risco ou timesheet) mas que não possuírem nenhum apontamento no período.  
**Origem dos dados**  
Será considerado como quantidade de horas trabalhadas e o custo do funcionário no período os valores retornados pelo processo na consulta ao software de Folha de Pagamento (Ponto Eletrônico) configurado.  
**Rateio de tarefas**  
O rateio de tarefas dos apontamentos será efetuado conforme regra de precedência apresentada abaixo:  
  
**Existe alocação para o funcionário?**  
**Sim =>** O rateio dos custos do funcionário será realizado irmãmente pelas tarefas às quais este recurso possui alocação, desconsiderando a quantidade de alocação.  
**Não =>** O rateio dos custos do funcionário será realizado irmãmente pelas tarefas às quais a sua função estiver associado ao insumo ou composição vinculados.

**Parâmetros**  
**Parâmetro de projeto: "Apropriar liberação em"**  
Parâmetro está localizado no caminho "Parâmetros do Projeto → Contratos → Liberação" e informa em qual ponto deve ser executada a apropriação da liberação do contrato, caso o mesmo esteja parametrizado para gerar apropriação.  
**Parâmetro de contrato: "Apropria liberação de Período"**  
Parâmetro está localizado no caminho "Cadastro de Contrato → Defaults" e informa se a liberação do período deve gerar apropriação ao integrar com o módulo de Suprimento/Faturamento.  
**Visibilidade dos parâmetros**  
Os parâmetros estarão disponíveis somente em ambientes integrados ao BackOffice Protheus via Mensagem Única (novo modelo), uma vez que em integração com o BackOffice RM o processo de apropriação deve ser definido a partir do encadeamento de tipos de movimento, como já é feito nos clientes atualmente.  
O parâmetro da tela de contratos não será visível em contratos com finalidade de 'Fornecimento de Materiais' ou qualquer contrato do tipo 'A Receber', pois contratos a receber não devem ser apropriados e contratos te fornecimento de materiais geram solicitações de compra e assim sendo devem ser apropriados sempre no retorno da nota fiscal. A apropriação não deve ser executada a partir das solicitações de compra pois os valores serão alterados durante o fluxo de compras.

**Valores dos parâmetros e fluxos viabilizados**  
Os novos parâmetros podem possuir os seguintes valores e respectivos comportamentos:  
  
·          'Apropria liberação de Período' = 'Desmarcado'  
  
·          Caso o parâmetro do contrato informe que não gera apropriação na liberação do período o mesmo não gerará apropriação do Pedido do Nucleus e nem enviará ao Pedido do Protheus as informações de rateio de tarefas, assim não apropriando no Pedido e nem na Nota Fiscal.  
  
·          Esta opção deve ser utilizara para contratos ou clientes que não desejam utilizar apropriação automática na integração com Suprimento/Faturamento, sendo o mesmo efetuado manualmente ou a partir de outro sistema, como na apropriação de materiais a partir do SigaMNT.  
  
·          'Apropriar liberação em:' = 'Pedido de Compra' e 'Apropria liberação de Período' = 'Marcado'  
  
·          Utilizando esta combinação parâmetro a apropriação será efetuada no Pedido do Nucleus, mas não será enviada informação de tarefas para o Protheus para que não haja apropriação na Nota Fiscal.  
  
·          Esta opção deve ser utilizara para contratos ou clientes que não desejem efetuar a apropriação das Liberações de Período imediatamente no momento da execução do processo. Ou seja, será apropriado exatamente o valor da liberação e na mesma data.  
  
·          'Apropriar liberação em:' = 'Nota Fiscal' e 'Apropria liberação de Período' = 'Marcado'  
  
Utilizando este parâmetro a apropriação será efetuada a partir da Nota Fiscal retornada pelo Protheus. Assim sendo, a informação do rateio de tarefas será enviada ao Protheus para propagação

Informações Complementares

---

[Relatório de Analise de de Valor Agregado por Centro de Custo](http://tdn.totvs.com/display/public/LRM/ER_PCREQ-9420_Relatorio_de_Analise_de_Valor_Agregado_por_Centro_de_Custo) 

[Relatório de Analise de Valor Agregado](http://tdn.totvs.com/pages/viewpage.action?spaceKey=LRM&title=DT_PCREQ-9420_Relatorio_de_Analise_de_Valor_Agregado_por_Centro_de_Custo)
