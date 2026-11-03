---
content_hash: 30a5a638c873ae067fc11c8a7911fbc9cc76fd8531a0730db47a688bbababe63
fetched_at: '2026-06-29T00:09:14.126578+00:00'
page_id: '421385135'
product: rm
source: tdn-rm
title: Alteração de Fase do Projeto 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385135
version: 5
---

---

**Objetivo**

* O objetivo desse processo é possibilitar, que para o projeto selecionado na visão, possa ser utilizado o processo de [Revisão Múltipla](https://tdn.totvs.com/pages/viewpage.action?pageId=421385536) onde é possível criar mais de uma revisão ativa e que as revisões sejam diferenciadas através das fases: “Orçamento”, ”Venda”, “Planejamento” e “Execução” de forma que cada fase tenha as tratativas mais adequadas.

**Parametrização**

* As descrições das fases podem ser parametrizadas através da opção, Aba Projeto | Grupo Parâmetros | TOTVS Construção Obras e Projetos | Gerais | Fases do Projeto.

**Processo**

* Ao acionar este processo será exibida uma tela onde serão apresentadas as opções: Sem Controle de Fases, Orçamento, Venda, Planejamento e Execução. Estas são as fases que podem ser atribuídas para o projeto. Um projeto que não possui fase pode ter a mesma alterada para qualquer uma das quatro citadas, porém o comportamento do processo de Revisão Múltipla vai depender da fase escolhida.
* **Fases:**
  + **Orçamento:**A fase de orçamento é considerada a primeira de um projeto e é através dela que buscamos o custo e o preço final de venda. Em alguns casos possui a necessidade de realização de simulação até que se encontre um formato adequado em termos de custo, prazo, escopo e preço de venda. Assim que uma proposta é escolhida teremos no sistema o que se chama de revisão orçamentária ativa. Esta revisão é a base para a criação da primeira versão de venda que será apresentada ao cliente. Também é a partir dela que será criada a primeira versão de planejamento do projeto que em muitos casos é a meta da equipe de planejamento e execução.
    - Permite a criação de novas revisões de orçamento horizontais para registrar as alterações caso queiramos salvaguardar informações do projeto anterior;
    - Permite a criação de novas revisões de orçamento verticais, a partir de uma revisão horizontal ou mesmo de uma vertical, para registrar as alterações caso queiramos salvaguardar o projeto anterior;
    - Não devem possuir nenhum tipo de contrato por se tratar somente de um orçamento.
  + **Venda:**A fase de venda pode ser considerada um ramificação da fase de orçamento, porém não obriga que o projeto tenha primeiro o orçamento e depois a venda. A revisão de projeto dessa fase representa a que vai ser apresentada ao cliente.
    - Permite a criação de novas revisões de venda horizontais para registrar as alterações caso queiramos salvaguardar informações do projeto anterior;
    - Não deverá permitir a criação de revisões de planejamento e nem de orçamento a partir dela;
    - Sempre existirá uma revisão de venda ativa;
    - Permite a criação de revisões horizontais de “Alteração de Escopo”;
    - Permite a “Aplicação da Alteração de Escopo” para revisões horizontais.
  + **Planejamento:** Planejamento é a fase que se segue quando o projeto é aprovado. Da revisão de orçamento é feita uma nova revisão para que se faça o planejamento do projeto. Nada impede de se criar um projeto já na fase de planejamento. Revisões de planejamento podem ser feitas também periodicamente para salvaguardar os dados de execução ou do próprio planejamento e re-planejar o projeto para o próximo período.  Para as revisões de planejamento também podem ser necessário o uso de cópias de projeto, de forma a escolher o planejamento a ser executado no próximo período (mês) que melhor se adeque a necessidade do projeto (escopo, prazo, custo). Escolhido este planejamento entre os vários possíveis chamaremos o mesmo de revisão de planejamento ativa. A fase de planejamento deverá permitir a criação de revisões horizontais de “Alteração de Escopo” e a “Aplicação da Alteração de Escopo”.
    - Não será permitido incluir contratos a receber, visto que eles devem ser incluídos nas revisões de venda.
  + **Execução:** A fase de execução é a promoção de um planejamento. Ela será utilizada pela equipe de obra para saber quais são as próximas atividades, quais os recursos necessários, como executar, para informar o avanço físico das atividades, dentre outros.  A revisão de execução atual chamará revisão de execução ativa.
    - Uma fase de execução pode ser criada somente a partir de um planejamento que tem origem de uma fase de orçamento ou outra fase de execução;
    - As revisões horizontais não estarão disponíveis para o projeto na fase de execução, salvo quando se tratar de Alterações de Escopo.

**Observações:**

* Se parametrizado, assim que executado o processo, o sistema dispara um workflow para o ECM gerando um atendimento.
* Para que o projeto assuma a nova fase escolhida é necessário que o atendimento seja concluído com aprovação. O workflow será disparado para que o atendimento seja criado apenas quando a  estiver habilitada.
* Enquanto o atendimento não for concluído, o projeto assume 'Posição Paralisado' e não pode ser editado.
* Caso o atendimento não seja aprovado, identifique quais mudanças devem ser efetuadas no projeto e acione novamente o processo de 'Alteração de Fases do Projeto' para que um novo atendimento seja aberto para aprovação.
* O atendimento poderá ser acessado pelo TOP através do Anexo > Fluxo de Atendimentos > Atendimento Relacionado ao Registro.
* Depois de aprovado o atendimento, o projeto assumirá a fase escolhida. É possível verificar na visão de projetos, pela coluna Fase do Projeto a fase assumida pelo mesmo.
