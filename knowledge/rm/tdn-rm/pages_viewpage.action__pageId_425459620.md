---
content_hash: 126c091f7748356864dfaee038cc1f308b53a7fcd6e513826095f59bb2048cae
fetched_at: '2026-06-29T00:09:37.495365+00:00'
page_id: '425459620'
product: rm
source: tdn-rm
title: TOTVS Business Analytics Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459620
version: 4
---

**Parâmetros**

---

A parametrização da Integração TOTVS Business Analytics é **obrigatória** e deve ocorrer **depois** da execução do Configurador. Todas as áreas da Stage Area precisam da parametrização.   
    
 Abaixo serão descritos todos os parâmetros disponíveis para a utilização na extração de dados ao BI.  
     
 **1 - Campos da visão de Parâmetros (Primeira Aba):**

* **Ativar Integração:** essa opção deverá ser selecionada para que a configuração das views seja realizada. Quando essa opção não estiver selecionada, as views que eventualmente já existirem serão excluídas.
* **Família Comercial**:\* selecionar, entre as opções disponibilizadas, qual a tabela que está configurada para o tratamento da família comercial. Entende-se por família comercial um conjunto de itens do estoque, agrupados segundo critérios comerciais, que possibilitam à área comercial um melhor gerenciamento sobre produtos vendidos.
* **Família Material**:\* selecionar, entre as opções disponibilizadas, qual a tabela que está configurada para o tratamento da família material. Entende-se por família material um conjunto de itens do estoque, agrupados segundo critérios técnicos de afinidade de materiais, como natureza, composição e aplicação, voltada para a área industrial.
* **Grupo de Estoque**:\* selecionar, entre as opções disponibilizadas, qual a tabela que está configurada para o tratamento do grupo de estoque. Entende-se por grupo de estoque um agrupamento de itens com características homogêneas, definidos segundo critérios contábeis.
* **Natureza da Operação**:\* selecionar, entre as opções disponibilizadas, qual a tabela que está configurada para o tratamento da natureza da operação. Entende-se por natureza da operação por permitir identificar as características fiscais dos itens referentes à operação fiscal que está sendo realizada.
* **Portador****:** selecionar, entre as opções disponibilizadas, qual a tabela que está configurada para o tratamento de portador. Entende-se por portador a entidade que movimenta valores, recebe a posse de títulos para efetuar a cobrança, executa pagamentos, entre outras coisas. Normalmente, o portador é uma entidade bancária, mas também podem ser portadores não bancários como o caixa da empresa, por exemplo.

**(\*****)**Atenção para as configurações acima, pois as mesmas tratam de campos complementares no Módulo de Gestão de Estoque, Compras e Faturamento. Estes campos normalmente são utilizados se relacionando ao cadastro de produto, e os mesmo são configurados na tela de Parâmetros do TOTVS Gestão de Estoque, Compras e Faturamento. Maiores detalhes consultar o help do produto.  
    
 **(\*\*****)**  Atenção para a configuração acima, pois a mesma trata de tabelas opcionais no Módulo de Gestão Financeira, e os mesmos são configurados na tela de Parâmetros do TOTVS Gestão de Financeira. Maiores detalhes consultar o help do produto.  
     
 **2 - Campos da visão de Parâmetros (Segunda Aba):**

* **Extração**: Informar o período inicial e o período final que será utilizado como parâmetro para a extração das informações no banco de dados (Neste momento a aplicação irá atualizar o período inicial e final referente à extração de todos os dados da View).

Nesta configuração temos a extração Fixa e Variável:

* + **Extração Fixa:** Para configurar a extração fixa somente devem ser preenchidos os campos Data Inicial e Final.
  + **Extração Variável:** Esta extração funciona se baseando na data atual. Para se configurar existem dois campos                     - Anterior a data atual{\*}: Neste parâmetro deve se definir a quantidade de dias ou meses que a extração de dados irá realizar a busca.

                                -  Posterior a data atual{\*}: Neste parâmetro deve se definir a quantidade de dias ou meses que a extração de dados irá realizar a busca

* + `Tipo`: Diário ou Mensal, sendo por default o tipo "Diário". Com estes parâmetros será calculado o período conforme os dados informados.

**Exemplo:**

Data Atual: 01/06/2011.  
 Anterior a data atual: 60 (Este parâmetro tem o intuito de subtrair ou acrescentar o valor informado junto a Data atual).  
 Posterior a data atual: 30 (Este parâmetro tem o intuito de subtrair ou acrescentar o valor informado junto a Data atual).  
    
 **Tipo: Diário.**  
    
 Período calculado:  
 Data Inicial: 01/04/2011.  
 Data Final: 01/07/2011.

***Observação:***

O período de 60 dias anterior a data atual e de 30 dias posterior será definido de maneira automática para esta integração, sendo assim este mecanismo é o **usual** para esta integração evitando que o usuário defina novos períodos. O usuário poderá definir somente a extração fixa **ou** variável.  
    
 **3 - Campos da visão de Parâmetros (Abas de Contas):**  
    
 Configurar os parâmetros abaixo, referentes ao Plano de Contas a serem utilizados na extração de dados:

* Contas - Ativo Total.
* Contas - Ativo Circulante.
* Contas – Clientes.
* Contas – Duplicadas Descontadas.
* Contas – Estoques.
* Contas – Realizável Longo Prazo.
* Contas – Ativo Permanente.
* Contas – Passivo Circulante.
* Contas – Fornecedores.
* Contas – Empréstimos e Financiamentos Curto Prazo.
* Contas – Empréstimos e Financiamentos Longo Prazo.
* Contas – Exigível Longo Prazo.
* Contas – Patrimônio Líquido.
* Contas – Receita de Vendas.
* Contas – Receita Operacional de Vendas.
* Contas – Custo.
* Contas – Devoluções.
* Contas – Resultado Operacional.
* Contas – Lucro líquido/Lucros e Perdas.
* Contas – Compras.
* Contas – Impostos sobre Vendas.
* Contas – Despesas Operacionais.
* Contas – Receitas Financeiras.
* Contas – Despesas Financeiras.

Selecionar entre os Planos de Contas quais serão considerados durante extração de dados. Vale lembrar que as Contas selecionadas devem corresponder a cada opção. Estes dados serão utilizados no Conceito "Fato - Controladoria - Indicadores Gerenciais" para que sejam enviados a Stage Area.  
    
    
 **4 - Campos da visão de Parâmetros (Abas de Eventos):**

* **Eventos para Hora Extra:** Selecionar entre os tipos de eventos para hora extra quais serão considerados durante extração dos dados.
* **Benefícios pagos pelos funcionários:** Selecionar entre os benefícios pagos pelos funcionários quais serão considerados durante extração dos dados.
* **Benefícios pagos pela empresa:** Selecionar entre os tipos de benefícios pagos pela empresa quais serão considerados durante extração dos dados.
* **Encargo Colaborador:** Selecionar entre os tipos de encargos por colaborador quais serão considerados durante extração dos dados.
* **Encargos Empresa:** Selecionar entre os tipos de encargos por empresa quais serão considerados durante extração dos dados.

**5 - Campos da visão de Parâmetros (Abas Tipo de Movimentos):**

* **Solicitação de Compras:** Selecionar entre os tipos de movimentos quais serão considerados durante extração dos dados sobre a solicitação de compras.
* **Pedido de Compras:** Selecionar entre os tipos de movimentos quais serão considerados durante extração dos dados sobre o pedido de compras. Estes dados serão utilizados no Conceito "Fato - Materiais - Gestão de Compras - Compras" para que sejam enviados a Stage Area.
* **Nota Fiscal de Compras:** Selecionar entre os tipos de movimentos quais serão considerados durante extração dos dados sobre as Notas Fiscais de compras. Estes dados serão utilizados no Conceito "Fato - Materiais - Gestão de Compras - Recebimentos Compras" para que sejam enviados a Stage Area.
* **Devolução de Compras:** Selecionar entre os tipos de movimentos quais serão considerados durante extração dos dados sobre a devolução de compras. Estes dados serão utilizados no Conceito "Fato - Materiais - Gestão de Compras - Devolução Compras" para que sejam enviados a Stage Area.
* **Faturamento:** Selecionar entre os tipos de movimentos quais serão considerados durante extração dos dados sobre o faturamento. Estes dados serão utilizados no Conceito "Fato - Comercial – Faturamento" para que sejam enviados a Stage Area.
* **Carteira de Vendas:** Selecionar entre os tipos de movimentos quais serão considerados durante extração dos dados sobre carteira de vendas. Estes dados serão utilizados no Conceito "Fato - Comercial - Carteira de Vendas" para que sejam enviados a Stage Area.
* **Vendas:** Selecionar entre os tipos de movimentos quais serão considerados durante extração dos dados sobre vendas. Estes dados serão utilizados no Conceito "Fato - Comercial - Vendas" para que sejam enviados a Stage Area.
* **Devolução de Vendas:** Selecionar entre os tipos de movimentos quais serão considerados durante extração dos dados sobre devoluções de vendas. Estes dados serão utilizados no Conceito "Fato - Comercial - Devolução de Vendas" para que sejam enviados a Stage Area.
