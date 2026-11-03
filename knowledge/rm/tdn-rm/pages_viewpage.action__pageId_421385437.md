---
content_hash: 3869643fdc54dc195b47810aa6a31c0ba494aebdc92fb0c3d7e039550934871b
fetched_at: '2026-06-29T00:09:16.003267+00:00'
page_id: '421385437'
product: rm
source: tdn-rm
title: Integração com Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385437
version: 2
---

O orçamento é uma ferramenta que possibilita apurar os limites por Centros de Custos, para prover controle dos recursos financeiros gastos.

O seguintes passos devem ser seguidos:  
 Definir que utiliza essa integração através do Menu Opções | Parâmetros | Totvs Obras e Projetos | Projetos, grupo Integração, Orçamento, marcando o campo "Utilizar controle orçamentário";  
 É necessário definir a "Opção de controle", se o orçamento será controlado por Período ou por Projeto. Caso opte por controlar por período, o orçamento será subdividido por períodos do orçamento. Caso contrário o controle orçamentário será feito para toda a duração do projeto.  
  
 Preencher as tabelas do Orçamento do módulo de Orçamento do Gestão de Estoques, Compras e Faturamento (linha RM) no menu Cadastros:  
 Natureza Orçamentária Financeira (obrigatório)  
 Classificação Período do Orçamento   
 Período do Orçamento (podem ser cadastrados pelo Totvs Gestão de Estoques, Compras e Faturamento (linha RM) através do menu Cadastro | Tabelas de Orçamento | Período do Orçamento), caso não sejam criados, o próprio Totvs Obras e Projetos irá criar de acordo com a opção de controle do orçamento)  
 Vínculo do Usuário e Centro de Custo (obrigatório)  
 Vínculo da Natureza do Orçamento e Centro de Custo (obrigatório)  
 Vínculo do Centro de Custo e Classificação Período  
 Vínculo do Centro de Custo Agrupador  
 Cadastro do Grupo Orçamentário (podem ser cadastrados pelo Totvs Gestão de Estoques, Compras e Faturamento (linha RM) ou através da edição de Tarefa no campo de Grupo Orçamentário).  
  
 Pré-requisitos para gerar o Orçamento:  
 Associar obras e  tarefas a um Grupo Orçamentário ou a uma Natureza Orçamentária/Financeira,  sendo que esta última vinculação será necessária para as tarefas de serviço com valor cotado, que não possuem insumos associados. Associar Insumos a uma Natureza Orçamentária ou o seu produto principal associado deve possuir Natureza orçamentária.  
 Calcular o projeto  
 Definir o cronograma previsto  
 Calcular a Curva S  
 Calcular o Cronograma de Desembolso  
  
 O orçamento deve ser gerado através do menu Opções | Integração com o Orçamento e pode ser visualizado através da visão de Tarefas, grupo Outros, opção Visão Orçamento.  
  
 É possível parametrizar o movimento do Totvs Gestão de Estoques, Compras e Faturamento (linha RM) para que não será permitido receber pedidos de compra além do valor orçado, dentro dos períodos do orçamento.  No grupo Orçamento, marque as opções "Controla Orçamento", defina o efeito a ser provocado no Orçamento e qual a ação quando exceder o Orçamento.  
  
 Caso o projeto seja replanejado, o orçamento deverá ser regerado. As datas anteriores à data corrente não sofrerão alteração caso os pedidos tenham sido efetivados.   
  
 Caso a estrutura do projeto tenha sido modificada o orçamento deverá ser regerado. Se a alteração for para menor, não será feita nenhuma alteração no Orçamento.  
  
 O saldo de um orçamento pode ser visualizado através do menu Utilitários | Consultar Valores de Orçamento do Totvs Gestão de Estoques, Compras e Faturamento (linha RM).

**Importante:**  
   
Para realizar o controle orçamentário de multiplos projetos é necessário que seja configurada a classificação de períodos no Nucleus.  
Cada "classificação" é vinculada a um único centro de custo. Portanto, para utilizar a integração com orçamento, cada projeto deverá possuir seu próprio centro de custo.
