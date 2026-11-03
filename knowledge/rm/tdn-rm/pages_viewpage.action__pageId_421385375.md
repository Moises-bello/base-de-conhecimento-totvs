---
content_hash: f55d0b0f4d9166b12e79e5486776e818bea1c718863e711981d688078e32cc5f
fetched_at: '2026-06-29T00:09:15.414153+00:00'
page_id: '421385375'
product: rm
source: tdn-rm
title: Cenários 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385375
version: 4
---

---

Cenários é uma funcionalidade no TOTVS Obras e Projetos que permite o cadastro de 4 planilhas idênticas às planilhas de Atividades e Serviços já existentes facilitando o processo de orçamento e criação de cenários tornando mais fácil determinar o custo final do projeto.   
   
Disponibilizou-se 5 cenários. O primeiro é o cenário default/especial que não poderá ser alterado e será chamada de cenário principal. Os demais podem ter apenas alterações no campo Ativo sendo marcado ou desmarcado.  
   
Para cada Cenário é possível utilizar uma Planilha de Atividade e uma Planilha de Serviço, totalizando 10 planilhas, assim como é possível alterar as tarefas de todas as formas possíveis e sem nenhuma restrição (alterar quantitativos, modificar a associação tarefa-composição). Mas o cadastro de composição, insumos e preços é único, o que significa dizer que qualquer alteração irá refletir em todos os cenários.  
   
Para serem utilizados, é necessário que os Cenários estejam ativos. Para isso é necessário acessar cada  associado ao usuário e permitir ou proibir o acesso à funcionalidade. O controle de segurança é unificado, ou seja, o que for permitido para um cenário será permitido para os demais.   
   
Depois dar acesso no controle de segurança, cada Cenário precisa ser ativado para que possa ser utilizado. Para isso acesse Orçamento | Cenários. Nessa opção é possível alterar o nome do Cenário e ativar/desativá-lo.

**Observação:**

A opção de ativar ou desativar é disponibilizado apenas para os Cenários, sendo que para a Planilha de Atividades e Planilha de Serviço não é possível alterar os campos Nome ou Ativo.  
A edição de Cenário deve ser feita Cenário por cenário, já que as informações não serão replicadas. Assim que ativos, os Cenários ficarão disponíveis para edição em Orçamento | Planilhas | Cenários. A estrutura, assim como a utilização, corresponde à mesma da Planilha de Atividades e Planilha de Serviços, ou seja, é possível cadastrar Obras, Etapas e Tarefas.   
   
Os processos e anexos também correspondem aos mesmos presentes nas Planilhas de Atividades e Serviço, exceto os processos de "Cálculo de Peso" e "Avanço Físico" que continuarão ser exclusivos da Planilha de Atividades.  
Todos os cenários deverão gerar registro no log de usuários, conforme parametrização definida no menu  nos . Toda a parametrização definida será aplicada para todo Cenário ativo, assim como para as planilhas de Atividade e Serviço.

**Observações:**

Todos os cenários poderão ser utilizados na integração com MS-Project. É possível importar tarefas através de arquivos Excel ou arquivos texto. Em Anexo / Impacto em tarefas, será visualizado em quais tarefas e de qual(ais) planilhas/cenários, o insumo ou a composição estão impactando.   
   
Em alguns processos já utilizados anteriormente pelos Cenários Principais (Planilha de Atividade e Planilha de Serviço) passaram a ser utilizadas por Cenários com algumas diferenças. Tais mudanças podem ser verificadas no help de cada funcionalidade:  e   
   
Para relatórios já existentes como , , , , , , Planilhas de Tarefas, Tarefas por Grupo de Custo, Composições do Projeto (somente Relatórios de Modelo Fixo), Composições de Custo Horário, Insumos do Projeto, Relatórios de Curvas ABC, assim como para Cronograma Desembolso, Concorrência Eletrônica, Composições e Insumos Utilizados e BDI Diferenciado, não tiveram seu funcionamento alterado, sendo que em todos é possível definir a Origem da Informação como Planilha de Atividades, Planilha de Serviços ou algum dos Cenários ativos.

A Planilha Executiva não poderá ser habilitada em Projetos que utilizam **Cenários**, pois a planilha executiva permite vincular apenas **tarefas da Planilha de atividades principal.**

---
