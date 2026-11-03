---
content_hash: 2522314df560173e79b62abb574613222d91da0392a0cf3044820169d0c1e950
fetched_at: '2026-06-29T00:10:52.072879+00:00'
page_id: '570039440'
product: rm
source: tdn-rm
title: Cockpit de Tarefas e Insumos
type: documentation
url: https://tdn.totvs.com/display/LRM/Cockpit+de+Tarefas+e+Insumos
version: 115
---

Cockpit de Tarefas / Insumos

## O Cockpit é uma ferramenta de consulta de informações detalhadas de tarefas e insumos permitindo dessa forma um acompanhamento visual do que foi **planejado**, **realizado**, **apropriado** e **pago** no projeto selecionado.

## **Onde acessar?**

O usuário pode acessar o Cockpit de duas formas:

1. **Portal da Obra:**

   * Obtenha o link com o **administrador do projeto** ou com a **equipe de suporte**.
   * Acesse o link em um navegador web e faça login.
   * Navegue até o menu **"Cockpit de Indicadores e Insumos"**.

1. **Através do Totvs Construção Obras e Projeto:**

   * Abra o Totvs Construção Obras e Projeto.
   * Selecione o projeto desejado.
   * No menu superior, clique em "Indicadores".
   * No menu lateral, clique em "Cockpit de Indicadores e Insumos".

## **Cabeçalho e informações de Contexto:**

No cabeçalho, você encontrará informações sobre o projeto atualmente selecionado, incluindo as datas do último cálculo do projeto e das importações de movimentações do BackOffice. Os gráficos relacionados a esses cálculos serão atualizados conforme essas datas.

## **Para começar:**

Na tela inicial do portal, você verá uma caixa de pesquisa no canto superior direito da tela, utilize a caixa de pesquisa para encontrar:

* **Tarefas:**  Digite o nome completo ou seu código identificador da tarefa, etapa ou obra à qual está associada, ou algumas palavras-chave que a descrevam.
* **Insumos:** Digite o nome ou código identificador específico do insumo, ou indique sua categoria para facilitar a identificação..

**Selecione a opção desejada:**

* Na lista de resultados, clique na opção que corresponde à tarefa/etapa/obra ou ao insumo que você procura.
* O sistema abrirá uma nova página com mais informações sobre a tarefa/etapa/obra ou o insumo selecionado, carregando as informações e gráficos referentes ao mesmo.

|  |  |
| --- | --- |
| **Selecionando uma Obra / Etapa / Tarefa** | **Selecionando um Insumo** |
|  |  |

## **Gráficos e Informações Disponíveis:**

.Informações e Gráficos da TarefasDetalhamento das informações relacionadas a tarefa.

Ao pesquisar uma tarefa no campo de busca do TCOP, você terá acesso imediato aos gráficos que mostram a evolução dos valores da tarefa. Além disso, os cinco principais insumos são exibidos logo abaixo, com a opção de 'Veja Mais' para listar todos os insumos disponíveis. 

**DETALHAMENTO DE INFORMAÇÕES DA TAREFA:**

|  |  |
| --- | --- |
|  | Apresenta o nome e código da tarefa. |
|  | **Status** Este quadro mostra o percentual concluído da tarefa, etapa ou obra.  **Como funciona:**   * **Obras e etapas:** O avanço é calculado pela proporção do percentual realizado  de todas as tarefas dentro da obra ou etapa. * **Tarefas:** O avanço é o percentual concluído da tarefa conforme constam no PERT, ou no cronograma realizado em projetos que não utilizam o PERT.   **O que considera no gráfico:**   * **Quando não utiliza o PERT:** Exibe até quatro barras representando o percentual concluído nos quatros últimos meses, conforme consta no cronograma realizado da tarefa. * **Quando utiliza o PERT:** Exibe uma barra com o percentual total de conclusão da tarefa. |
|  | **Custo** **Gráfico Apropriado X Planejado**: No quadro custo é exibida uma barra informando o percentual  do valor apropriado da tarefa em relação ao valor que foi planejado para a mesma. Os valores de apropriações são recuperados a partir dos valores apropriados importados do BackOffice e das apropriações realizadas diretamente no projeto. Mais informações sobre a importação de apropriação em: [Apropriações e Movimentações do BACKOFFICE no TCOP - TOTVS Construção Obras e Projetos](https://tdn.totvs.com/pages/viewpage.action?pageId=518472242).  **Planejado:** Os valores de planejamento serão recuperados a partir do cronograma previsto das tarefas, sendo atualizados conforme o último cálculo do cronograma e do projeto. Tarefas indiretas e tarefas de receita não são consideradas na soma do valor total planejado.  **Apropriado:**  **O que são valores apropriados?**  No Portal Obras e Projetos, valores apropriados referem-se a movimentações do BackOffice e apropriações que foram definidas como apropriações. Isso inclui itens como:   * **Notas fiscais:** Valores de produtos ou serviços adquiridos para a obra. * **Baixas de estoque:** Materiais utilizados na construção. * **Títulos financeiros:** Despesas com pagamentos a fornecedores, mão de obra, etc. * **Mão de obra:** Valor das horas apontadas. * **Equipamentos:** Valor dos apontamentos de uso dos equipamentos. * **Transporte:** Valor dos apontamentos dos ciclos de transporte.   **Onde encontrar mais informações sobre apropriações?**  Para obter mais detalhes sobre o processo de apropriação no Portal Obras e Projetos, consulte a documentação oficial: <https://tdn.totvs.com/x/MkLnHg>.  **Como os valores apropriados são atualizados?**  Os valores apropriados são atualizados automaticamente com base na data da última importação de movimentações do BackOffice. Isso garante que você sempre tenha acesso aos dados mais recentes.  **Saldo:** O saldo disponível para a realização da tarefa é exibido com a seguinte fórmula: **Planejado - Apropriado**. |
|  | **Pedido e  Pedido Extra** Os valores **Entregues** e **Pagos** são exibidos somente se o projeto estiver parametrizado para buscar apropriação no BackOffice.  **Gráfico Entregue X Pedido:** No gráfico exibe o percentual da soma dos valores entregues em relação à soma dos valores pedidos.  **Pedido:** Exibe a soma dos valores dos itens dos pedidos. Os valores são calculados multiplicando a quantidade pedida pelo preço orçado de itens de pedidos que foram enviados para o “Suprimento / Faturamento”.  **Entregue:**  Exibe a soma valores dos itens pedidos que foram entregues à obra. Esses valores são atualizados automaticamente de acordo com a data da última importação de dados do BackOffice.  Os parâmetros relacionados a entregas e devoluções estão acessíveis nos parâmetros de projeto em "Integração | Suprimentos / Faturamento | Movimentação do BackOffice".  Entregue com BackOffice PROTHEUS:  São considerados valores de prenotas ou notas fiscais de entradas relacionadas a pedidos originados do TCOP.  è possível definir no parâmetro do projeto onde será considerado como entregue, se na prenota ou na nota. Por padrão é considerado na prenota.    Entregue com BackOffice RM: São considerados tipos de movimentos de entrega e devolução.    **Pago:** Exibe a soma dos valores totais de itens de pedidos que foram pagos, ou seja, ocorreu a baixa no financeiro. |
|  | **Contratos a Pagar** **Total:** Exibe a soma dos valores contratados para a tarefa, considerando:   * Somente contratos com a finalidade de prestação de serviços, parcelas fixas e marco contratual; * Somente contratos com o tipo a pagar; * Aditivos relacionados ao contrato e a tarefa são considerados; * Contratos com status em negociação ou cancelado não são considerados. |
|  | **Contratos Medidos** **Gráfico Medido X Contratado:** Exibe o gráfico com o percentual equivalente à soma dos valores medidos em relação à soma dos valores contratados.  **Medido:** Exibe o valor medido da tarefa em contratos de serviços e insumos, sendo que o valores de contratos de insumos são considerados após realizar a medição para a tarefa. Realiza o abatimento de valores em períodos de estornos.  **Contratado:** Exibe o valor contratado para a tarefa conforme detalhado acima no tópico  **Contratos**. |
|  | **Contratos Pagos** Estes valores são exibidos somente se o projeto estiver parametrizado para buscar apropriação no BackOffice.  **Gráfico Pago X Liberado:** Exibe o gráfico com o percentual equivalente à soma dos valores pagos em relação à soma dos valores liberados.  **Pago:** Exibe a soma dos valores pagos das movimentações de BackOffice, ou seja, ocorreu a baixa no financeiro.  **Liberado:** Exibe a soma dos valores medidos de contratos de serviços e insumos em que os respectivos períodos estejam com status de liberados.  **Saldo a pagar:** Saldo em aberto que deverá ser pago. O calculo é o valor **Liberado** menos o valor **Pago**. |

**DETALHAMENTO DO INSUMO NA TAREFA:**

**Filtro de Grupo de Custo:**Permite filtrar os insumos relacionados a tarefa pelos respectivos grupos de custos. São apresentados os grupos de custo do projeto corrente e do projeto global.

Para entender os valores apresentados do insumo acesse a aba "Informações e Gráficos dos Insumos".

Informações e Gráficos dos InsumosDetalhamento das informações relacionadas ao insumo.

**Ao informar um insumo no campo de pesquisa:**

* São exibidos os gráficos referentes aos valores do insumo.
* O nome do insumo, seu código e os gráficos de quantidade e valor são mostrados.

**O Cockpit também permite:**

* Buscar insumos usando o mesmo padrão de pesquisa da tarefa.
* Filtrar qual insumo deseja ver no detalhamento do cockpit usando a lupa de pesquisa.
* Carregar as informações do insumo na tela ao informar seu código ou descrição.

**DETALHAMENTO DE INFORMAÇÕES:**

|  |  |
| --- | --- |
|  | Exibe o nome e código do insumo. |
|  | **Custo** **Orçado:** Exibe a soma das quantidades e valores da curva ABC de insumos.  **Apropriado:** Exibe a soma das quantidades e valores apropriados no projeto.  **O que são valores apropriados?**  No Portal Obras e Projetos, valores apropriados referem-se a movimentações do BackOffice e apropriações que foram definidas como apropriações. Isso inclui itens como:   * **Notas fiscais:** Valores de produtos ou serviços adquiridos para a obra. * **Baixas de estoque:** Materiais utilizados na construção. * **Títulos financeiros:** Despesas com pagamentos a fornecedores, mão de obra, etc. * **Mão de obra:** Valor das horas apontadas. * **Equipamentos:** Valor dos apontamentos de uso dos equipamentos. * **Transporte:** Valor dos apontamentos dos ciclos de transporte.   **Onde encontrar mais informações sobre apropriações?**  Para obter mais detalhes sobre o processo de apropriação no Portal Obras e Projetos, consulte a documentação oficial: <https://tdn.totvs.com/x/MkLnHg>.  **Como os valores apropriados são atualizados?**  Os valores apropriados são atualizados automaticamente com base na data da última importação de movimentações do BackOffice. Isso garante que você sempre tenha acesso aos dados mais recentes.  **Observação**  Quando projeto estiver parametrizado para utilizar insumos somente para contratação, as quantidades e valores orçados serão apresentados nos insumos configurados como "somente orçamento / planejamento", e as quantidades e valores apropriados serão apresentados nos insumos configurados como "somente contratação". |
|  | **Pedido e Pedido Extra** **Gráfico Entregue X Pedido:** No gráfico exibe o percentual da soma das quantidades e valores entregues em relação à soma das quantidades e valores pedidos.  **Pedido:** Exibe a soma das quantidades e valores orçados de todos os pedidos que tenham sido enviados ao "Suprimentos / Faturamento" e não estejam associados a contratos.  **Entregue:** Exibe à soma das quantidades e valores dos itens pedidos que foram entregues à obra.  Será exibido somente se o projeto estiver parametrizado para buscar apropriação no BackOffice. Esse valor é atualizado automaticamente de acordo com a data da última importação de dados do BackOffice. |
|  | **Contratados e Medidos** São consideradas as quantidades e valores em contratos, considerando:   * Somente contratos de insumo, fornecimento de material e extra histograma; * Somente contratos do tipo a pagar; * Aditivos relacionados ao contrato são considerados; * Contratos com status em negociação ou cancelado não são considerados.   **Gráfico Medido X Contratado:** Exibe o gráfico com o percentual equivalente à soma das quantidades medidas e  valores medidos em relação à soma das quantidades e dos valores contratados.  **Medido:** Exibe a soma das quantidades e valores medidos para o insumo. Realiza o abatimento de valores em períodos de estornos.  **Contratado:**  Exibe a soma das quantidades e valores contratados para o insumo.  **Observação**  Quando projeto estiver parametrizado para utilizar insumos somente para contratação, as quantidades e valores medidos e contratados serão apresentados apenas nos insumos configurados como "somente contratação". |
|  | **Saldo** Exibe a diferença entre as quantidades e valores orçados em relação à soma de quantidades e valores pedidas e contratadas para o insumo.  **Observação**  Quando projeto estiver parametrizado para utilizar insumos somente para contratação, o saldo será apresentado apenas nos insumos configurados como "somente orçamento / planejamento". |

**DETALHAMENTO DA TAREFA DO INSUMO:**

**Filtro de Tarefas:** Permite realizar o filtro pelo código ou nome da tarefa.

Para entender os valores apresentados da tarefa acesse a página "Informações e Gráficos das Tarefas".

Onde Validar as InformaçõesOnde validar as informações de apropriações, entregas, devoluções e pagamentos.

Para facilitar a conferência dos valores de apropriações, entregues e pagos exibidos no cockpit, utilize a tela "Movimentações do BackOffice" do módulo de projetos.

* **Menu:** Módulo de Projetos > Controle > Consultas > Movimentações do BackOffice
* **Benefícios:**
  + Validação rápida e precisa dos dados do cockpit
  + Maior confiabilidade nas informações exibidas
  + Agilidade na tomada de decisões

Com essa nova funcionalidade, você garante maior precisão e confiabilidade nas informações do cockpit, otimizando seu processo decisório.
