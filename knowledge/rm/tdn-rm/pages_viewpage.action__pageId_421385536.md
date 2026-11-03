---
content_hash: 5126c434a4aabaff7cca8c44331b3241fb892d8a9b8827a0462678237f23cc25
fetched_at: '2026-06-29T00:09:16.418643+00:00'
page_id: '421385536'
product: rm
source: tdn-rm
title: Revisão Múltipla 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385536
version: 8
---

---

**Revisão de Projeto**  
No Totvs Obras e Projetos é possível realizar revisão de um projeto. A revisão implica na criação de um novo projeto a partir de um projeto origem, onde informações do projeto origem serão copiadas para o projeto destino (projeto filho) e o projeto origem será modificado para o status revisado, status que impossibilita a alteração das informações do projeto. O projeto destino será o novo projeto em execução.

**Observação:**  
As funcionalidades de mobilidade também são consideradas na revisão de projetos, serão replicados para o novo projeto os dados de: Folhas tarefa, equipes do projeto, coletores móveis associados ao projeto, alocação de mão de obra, ciclos de transporte, apontamentos de mão de obra, apontamentos de ciclos de transporte, apontamentos de equipamento, custos diretos e indiretos de equipamentos.  
Ao realizar a revisão de um projeto automaticamente são atualizados os identificadores de projeto e tarefa para o projeto de destino em:

* Movimentos
  + Rateio de Projeto e Tarefa do Movimento
  + Itens de Movimento
  + Rateio de Projeto e Tarefa do Item de Movimento
* Lançamentos Financeiros - Rateio de Projeto e Tarefa
* Lançamentos Fiscais
* Tabela Saldo ISS por Obra

**Revisão Múltipla**

A Revisão Múltipla é um processo da visão de projetos e parte do mesmo princípio da revisão que já existia no Totvs Obras e Projetos, porém possibilitará à criação de quatro tipos de revisões distribuídas em fases, por default a descrição das fases é: Orçamento, Venda, Planejamento e Execução, que são identificadas por símbolos e através da coluna Fase do Projeto na Visão de Projetos.  
**Observação:**  
A descrição das fases pode ser parametrizada, em parâmetros gerais do projeto.  
Para alteração de fases do projeto, deverá ser acessado o processo  na visão de projetos. A execução do processo de "Revisão Múltipla" que gera as revisões de projeto só é feita quando o projeto esta definido em alguma fase e um projeto tenha sido selecionado.   
Geradas as revisões, a visualização dos projetos revisados é feita através do Anexo .  É através do processo de "Revisão Múltipla" deste anexo que são geradas revisões a partir dos novos projetos.

**Exemplo:** Considere os seguintes projetos:

Projeto Orçamento 1 (principal)

Projeto Revisão Vertical de Orçamento 1.1 (revisão múltipla)

Para gerar a Revisão Horizontal de Orçamento a partir da Revisão Vertical de Orçamento 1.1 é necessário acessar o  Processo "Revisão Múltipla" do Anexo Projetos de Revisão Múltipla.   
Para o cenário de Revisão Múltipla surge os conceitos Revisão Horizontal e Revisão Vertical:

* + **Revisão Horizontal**: Gera um novo cenário de projeto copiando os dados de uma revisão e permitindo que as duas estejam ativas, ou seja, o projeto origem e o projeto destino permanecem no mesmo status.
  + **Revisão Vertical**: Gera uma nova revisão copiando os dados do projeto e coloca as revisões da fase anterior no status revisado, não permitindo mais alterações nas mesmas, ou seja, o projeto origem e os projetos que foram gerados a partir deste serão colocados como revisados e apenas o novo projeto ficará ativo.
* **Revisão Múltipla em projetos na fase Orçamento**

Nesta fase busca-se chegar ao custo e preço de venda, em alguns casos possui a necessidade de realização de simulação até que se encontre um formato adequado em termos de custo, prazo, escopo e preço.   
A partir de projetos nesta fase podem ser geradas Revisões Horizontais de Orçamento, que irão copiar as informações do projeto origem, mas o projeto origem continua ativo, esta opção pode ser utilizada caso queira salvaguardar as informações do projeto origem. Pode ser gerada a Revisão Vertical de Orçamento onde as informações do projeto origem são copiadas, mas o projeto origem não fica mais ativo, se torna revisado e não passível de alterações.  
Também podem ser geradas revisões de Venda e Planejamento a partir do projeto na fase de Orçamento, isto é feito escolhendo a revisão de orçamento aprovada e usando o processo de revisão vertical, ou seja, as revisões horizontais de orçamento se existirem são passadas como revisadas assim como o projeto origem e as novas revisões geradas serão os projetos em execução.  
Para geração de revisões de Venda e Planejamento pode-se optar por gerar revisão de Venda e depois revisão de Planejamento, mas também pode-se gerar simultaneamente as revisões.  
**Observações:**  
Após geração da revisão de Planejamento ou Venda não é possível gerar revisões horizontais e verticais de Orçamento, porém se for gerada a revisão de Planejamento ainda é possível gerar a revisão de Venda e vice-versa.  
A criação de cenários de Venda e Planejamento a partir do cenário de Orçamento deve ser necessariamente gerada a partir do mesmo projeto de Orçamento.  
**Atenção:**  
Não é possível criar contratos em projetos na fase Orçamento.  
Ao passar um projeto para a fase de Orçamento e este possuir contrato, uma mensagem de aviso ao usuário deve ser emitida, pois projetos na fase de Orçamento não permitem o cadastro de contratos.

* **Revisão Múltipla em projetos na fase Venda**

A partir de projetos na fase de venda que estejam em andamento (faturando contrato com o cliente), podemos criar uma revisão vertical de venda normal, onde o projeto de Venda oficial passa a assumir o status Revisado e um novo projeto é criado com as mesmas informações do projeto oficial. Também pode ser gerada Revisão Horizontal de , onde será criado um novo projeto ativo.

* **Revisão Múltipla em projetos na fase Planejamento**

Nesta fase buscamos planejar as atividades para a execução física da obra e controlar os possíveis desvios de execução, poderemos gerar revisões horizontais de planejamento para gerarmos cenários de projeto e escolher o melhor.   
A partir do momento em que o planejamento é definido e aprovado pode ser gerada a versão de Execução, através da opção "Transformar em fase de Execução".  Esse processo só pode ser feito na Revisão de Planejamento oficial, e quando o processo é executado se existirem outras revisões de planejamento a partir da revisão oficial, estas são colocadas como revisadas. O processo transforma a fase do projeto oficial de Planejamento para Execução.  
**Observações:**  
Não será permitido incluir contratos a receber, visto que eles devem ser incluídos nas revisões de venda.  
Ao passar um projeto para a fase de Planejamento e este possuir contrato a receber, uma mensagem de aviso ao usuário deve ser emitida, pois projetos na fase de Planejamento não permitem o cadastro de contratos a receber.

* **Revisão Múltipla em projetos na fase Execução**

Ao final do período de execução, os dados se fazem necessários para o replanejamento. Pois para planejar é necessário ter o conhecimento do avanço real das atividades, custos realizados, entre outros. Para isto poderá ser criado uma revisão vertical de Planejamento a partir da execução ativa.

**Atenção:**  
Quando for gerada a nova revisão de planejamento a revisão de execução ficará desativada e um novo projeto na fase de planejamento é criado.  
Após a criação de um novo Planejamento, poderá ser utilizado o mesmo processo de planejamentos horizontais, que poderão ser utilizados apenas para efeito comparativo, em relação ao projeto de Planejamento gerado a partir da execução. Após as diversas comparações entre os diferentes cenários de projetos, uma nova fase de execução pode ser gerada.  
   
**Observações Gerais:**  
No processo de revisão múltipla, projetos de Licitação poderão ser criados somente a partir de um projeto que se encontra na fase de Planejamento ou Execução.    
As licitações do projeto que se encontra em fase de execução e que está ativo, serão consideradas inativas e desnecessárias a partir do momento em que seja criada uma revisão vertical de planejamento, pois o contrato da licitação só poderá ser criado apenas no projeto ativo.   
Ao realizar backups de projetos o backup somente será feito da revisão escolhida. Ao restaurar o backup ele será restaurado como um projeto qualquer na fase em que foi feito o backup.    
Nos processos de "Alteração geral de fases" e "Revisão Múltipla" pode ser utilizado o   que irá controlar a realização destes processos,  impedindo a execução dos processos enquanto o mesmo não for aprovado e permitindo quando for aprovado.

* **Revisão Múltipla considerando Mobilidade**

As funcionalidades de Mobilidade deverão estar disponíveis apenas nas fases de Planejamento e Execução e apenas para suas revisões verticais.    
Para projetos que possuem funcionalidades de mobilidade, tais como folhas tarefas, equipes de projetos do tipo mobilidade, etc., o processo de "Alteração de Fase do Projeto" só poderá ser concluído com sucesso se a fase selecionada for Planejamento, Venda ou Execução, ou Sem Controle de Fases desde que o mesmo não tenha "projetos filhos".    
Para todas as funcionalidades de mobilidade existentes no menu principal do sistema, deverá ser validado se a fase do projeto permite a utilização das mesmas.

**BIM:** Em ambas as revisões, tanto simples quanto múltipla, somente serão copiados os dados das associações do modelo BIM e também das associações de tarefas com objetos do modelo. Não serão copiadas informações para o projeto de Alteração de Escopo.

* **Revisão Múltipla em projeto de Revisão de Reprogramação**

O processo de revisão múltipla em projeto de Revisão de Reprogramação, irá criar uma cópia da Revisão de Reprogramação, dessa forma, o usuário poderá efetuar diferentes alterações em vários projetos antes de sincronizar e decidir melhor sobra a aplicação das alterações.

A Planilha Executiva não poderá ser habilitada nos **Projetos de Revisão Múltipla** nas fases de **Orçamento** e **Venda**

 Como Fazer

---
