---
content_hash: 0d8c157bb9384e80cbf9dcb5df3473868650e2cc9d96425fba47aeb1f47349f9
fetched_at: '2026-06-29T00:10:58.977329+00:00'
page_id: '608171251'
product: rm
source: tdn-rm
title: Mão de Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=608171251
version: 53
---

---

**Conceito:** O apontamento de mão de obra refere-se ao processo de monitoramento, registro e controle da presença, atividades e produtividade dos trabalhadores envolvidos no projeto.

Esse processo é essencial para manter o controle sobre as horas trabalhadas, tarefas executadas, e custos com mão de obra.

No apontamento de mão de obra, são registrados dados como:

* **Jornada de Trabalho**: Controle das horas de entrada, saída e intervalos de cada trabalhador.
* **Atividades Realizadas**: Registro das tarefas desempenhadas por cada trabalhador (ex.: escavação, concretagem, armação de ferragens).
* **Equipe e Local de Trabalho**: Identificação da equipe e setor onde o trabalho foi realizado.
* **Produtividade**: Medição do desempenho em relação às metas estabelecidas para cada atividade.
* **Custos**: Cálculo dos custos de mão de obra associados a cada atividade.

**Objetivo**: O objetivo é permitir uma gestão eficiente, ajudando a reduzir desperdícios, aumentar a produtividade e fornecer uma base confiável para a medição de desempenho e controle de custos.

Esses dados são, geralmente, registrados diariamente e organizados em relatórios para que os gestores da obra possam tomar decisões e fazer ajustes no cronograma e orçamento.

Para uma exemplificação visual desse processo acesse o video :

How To | TOTVS Construção Obras e Projetos | App Minha Obra - Apontamento de Mão de Obra - <https://www.youtube.com/watch?v=6NthywZ6EgE>

Abaixo documentado em abas todas as  funcionalidades que são utilizadas no processo de Mão de Obra.

Mão de ObraParâmetros

**Parâmetros Mão de Obra:**

---

Nessa tela são citados todos os parâmetros que tem relação ao apontament de mão de obra ou algum processo que tenha vinculo com o mesmo tema.

Para mais detalhes de parâmetros que envolve Mobilidade acesse:  e  e

* O parâmetro “Ratear horas improdutivas para a tarefa” é utilizado nos processos de rateio e revaloração de apontamentos de equipamentos e mão de obra. Caso esteja habilitado, as horas improdutivas apontadas serão apropriadas de acordo com a tarefa e motivo de improdutividade informados;
* A inclusão de apropriação que representa a improdutividade, somente acontecerá se o parâmetro de "Motivo de Improdutividade Mão de Obra" estiver definido;
* Para maiores detalhes sobre o parâmetro “Enviar e-mail de log de erros” vide Parametrização Geral;

* O parâmetro para definição de “Eventos/ Verbas” é utilizado no processo de rateio e revaloração de mão de obra para buscar o custo. Quando informado o sistema busca somente os custos dos eventos/verbas informados para o funcionário. Caso contrário, o sistema busca o custo total. Aplicável somente quando integrado com Folha de Pagamento do PROTHEUS;

* Para que seja permitido o cadastro de funcionários como membros de equipe o projeto deve estar integrado com o TOTVS Folha de Pagamento.
* O parâmetro "Considerar funcionário/terceiro de:" serve para filtrar os funcionários/terceiros.

Nos parâmetros de Mobilidade no grupo "Tratamento para sincronismo de equipe em apontamentos" existem dois parâmetros:

* **Tipo de envio de equipe para apontamentos:** Define como será a seleção de equipe e membros de equipe que serão enviados para o coletor;
* **Desconsiderar situação do funcionário/terceiro ao enviar para o coletor:** Define a restrição de situação de funcionários/terceiros que serão enviados para o coletor. Se estiver marcado, não haverá restrição, caso contrário, as situações de pessoas com Aposentadoria por Invalidez(I), Demitido(D),  com Demissão no mês(X) e Contrato de Trabalho Suspenso(C) serão retiradas da lista de envio. Esse parâmetro influencia nas seguintes funcionalidades:
  + Cadastro de Equipe e Membros de Equipe;
  + Cadastro de Folha Tarefa de Produtividade;
  + Alocação de Mão de Obra na Folha Tarefa;
  + Sincronismo de Membros para o Coletor;
  + Sincronismo de Equipes para o Coletor (se o parâmetro **não estiver marcado,** não serão sincronizadas as equipes cujos responsáveis estejam nas situações de pessoas com Aposentadoria por Invalidez(I), Demitido(D), Demissão no mês(X) e Contrato de Trabalho Suspenso(C)).

* **Controlar capacidade da equipe na alocação de mão de obra:** Este parâmetro controla a capacidade de alocação da equipe considerando o período para a capacidade do insumo, exibindo no anexo da equipe de mobilidade o insumo , o total alocado para o insumo , qual a sua capacidade total e saldo.
* **Campos Complementares a serem exibidos no App Minha Obra:**

  Permite parametrizar os Campos Complementares dos apontamentos de Mão de obra (máximo de 5 campos), cujo preenchimento será realizado no App Minha Obra e visualizado nos apontamentos de mão de obra.

  Este parâmetro somente estará habilitado se existirem campos complementares de Apontamentos de Mão de Obra cadastrados em "Cad. Gerais | Campos Complementares | Apontamentos de Mão de Obra". Saiba mais em [Campos Complementares - TOP](https://tdn.totvs.com/display/LRM/Campos+Complementares+-+TOP)

  Após realizado o cadastro dos campos complementares, basta informá-los nesse parâmetro, e ficarão disponíveis na tela de apontamento de mão de obra no App Minha Obra para preenchimento e no sistema na edição do apontamento de Mão de obra.

  A ordem dos campos complementares definirá a ordem de exibição no App, ou seja, o Campo Complementar 1 será o primeiro a ser exibido na tela do apontamento de Mão de obra do App Minha Obra, o Campo Complementar 2 será o segundo a ser exibido e assim, sucessivamente.

  Cada parâmetro pode ser preenchido com um campo complementar e, na tela de preenchimento dos apontamentos de Mão de obra do App Minha Obra, serão exibidos somente os 5 campos complementares informados nos parâmetros abaixo, conforme parametrizado em cada projeto, ou seja, podem ser parametrizados campos complementares diferentes em cada projeto.

  A limitação da exibição dos nomes dos campos no App Minha Obra é limitada a 30 caracteres.

* Para apontamentos retroativos há um parâmetro que determina o número máximo de dias que um usuário pode retroceder. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=421385196)

* O parâmetro do “Configuração de WebService para Folha de Pagamento de Ponto Protheus” é utilizado para buscar informações de folha de pagamento e folha de ponto no Protheus.

Detalhamento do Processo : [Rateio e Revaloração](https://tdn.totvs.com/pages/editpage.action?pageId=421385566)

Equipes

**Equipe de Mobilidade**

---

A equipe é um conjunto de pessoas (funcionários e terceiros) que podem possuir diferentes funções para o cumprimento de tarefas de um determinado projeto.

Equipe de Mobilidade

Não é permitido que uma pessoa esteja ativa como funcionário e terceiro em uma mesma coligada.

Para incluir uma equipe de mobilidade o usuário deverá clicar em <Novo> e informar os dados necessários para o cadastro, conforme os campos mostrados abaixo:

* **Descrição:** nome da equipe responsável por um determinado projeto.
* **Ativa:** define que a equipe está ativa. Por default, este campo virá marcado. Deverá ser desmarcado caso se deseje desativar a equipe para que não possa ser associada a um projeto.
* **Tipo do Responsável pela Equipe:** define a origem do usuário cadastrado.
* **Usuário (encarregado) responsável pela equipe:** visão de usuários do TOTVS Folha de Pagamento.

Será possível alterar ou excluir uma equipe. Para o caso de exclusão, o sistema irá validar se foi dada carga no coletor com algum membro da equipe.

Caso tenha carga em coletor pendente de apontamento de mão-de-obra, o sistema exibirá mensagem informativa e não permitirá a exclusão da equipe.

Em seguida, será exibida ao usuário a pergunta "Deseja desativar a equipe para lançamentos futuros?".

Caso o usuário confirme, a equipe será desativada e apontamentos desta equipe feitos após esta data não serão mais apropriados e a equipe não estará mais disponível para associação a nenhuma Folha Tarefa.

A equipe somente poderá ser excluída após retorno dos apontamentos do coletor e após apropriação dos apontamentos retornados.

Caso não tenha sido dada carga em coletor, todos os membros da equipe serão desassociados e a equipe será excluída.

**Importante:**

* Não existirão restrições sobre a quantidade de membros associados às equipes.
* Se após enviar a equipe para um coletor o encarregado for excluído, o responsável poderá fazer o apontamento no coletor normalmente e estas informações ficarão gravadas e disponíveis no TOP. Como a apropriação de mão de obra não leva em consideração o usuário que executou a tarefa e sim a equipe, estes dados poderão ser apropriados normalmente.
* No processo de admissão de um funcionário no TOTVS Folha de Pagamento, este irá gerar um registro no cadastro de pessoas do TOP. Este funcionário ficará "Ativo" e disponível para vínculo à equipe de mobilidade.
* No processo de demissão de um funcionário, caso ele seja um membro de equipe de projeto, este terá seu status modificado para "Inativo" e não poderá ser vinculado a nenhuma  equipe de projeto de mobilidade.
* A partir da data de sua demissão, o funcionário não poderá ter nenhum apontamento apropriado.
* Apontamentos retornados do coletor com data posterior à demissão serão desconsiderados. Os apontamentos com data anterior à demissão e ainda não importados do coletor serão importados e apropriados normalmente.
* Só estarão disponíveis os funcionários definidos no momento da entrada do Apontamento, que não possuem pendências no Encerramento.

Para esta funcionalidade existe uma aba dentro da edição da equipe chamada **'Mapa'**, durante o registro dos apontamentos informações da localização são coletadas e enviadas no sincronismo para o sistema, com isso é possível verificar as posições dos apontamentos do coletor.

Para habilitar esta funcionalidade é preciso configurar em menu Ambiente > Parâmetros > Parâmetros Globais > aba Google, e preencher o campo 'Chave de identificação para o Google Maps'.

Anexos

---

[Alocação de Mão de Obra da Equipe](https://tdn.totvs.com/pages/viewpage.action?pageId=421385139)

[Tarefas Associadas à Equipe](https://tdn.totvs.com/pages/viewpage.action?pageId=421385511)

 

[Apontamento de Mão de Obra](https://tdn.totvs.com/pages/viewpage.action?pageId=421385097)

[Histórico de Membros de Equipe (Folha de Produtividade)](https://tdn.totvs.com/pages/viewpage.action?pageId=886653264)

Processos

---

 

[Gerar Relatório de Membros de Equipe](https://tdn.totvs.com/pages/viewpage.action?pageId=555869084)

[Ativar/Desativar Membros de Equipe](https://tdn.totvs.com/pages/editpage.action?pageId=886646094)

Terceiros

**Terceiros:**

---

Também conhecido como[Cadastro de externos](https://tdn.totvs.com.br/display/public/LRM/Cadastro+de+Externos)

* O cadastro de terceiros do TOTVS Obras e Projetos é utilizado para permitir a montagem das equipes do projeto;
* Um terceiro pode ser cadastrado no TOTVS Obras e Projetos será cadastrado como uma pessoa no TOP e deverá ser informado o campo Cód. Externo e os demais dados da aba “Dados Externo” para que ele seja considerado uma pessoa;
* Os dados deste cadastro servirão para vincular o membro a uma equipe de projeto. O usuário deverá informar os seguintes campos para cadastro de um terceiro:

  + Na tela Identificação:

    - Identificador;
    - Nome;
    - Estado Natal.
  + Na tela Dados Externo:

    - Cód. Externo;
    - Cód. Situação;
    - Data Início (Data de início das atividades do terceiro).
* Os demais campos não são de preenchimento obrigatório, porém o preenchimento do campo “Cód. CFO” será importante para o caso de pagamento dos serviços do terceiro a um fornecedor ao qual o mesmo está vinculado. É possível, via parametrização, tornar este campo obrigatório.
* Para mais detalhes acesse:
Detalhamento dos Cálculos

**Detalhamento de Cálculos**

---

* **Insumos**
  + Quantidade Total do Insumo na Tarefa: Quantidade a ser executada na tarefa X Horas necessárias do insumo na tarefa;
  + Horas necessárias para realização da tarefa no período da Folha Tarefa: Deve considerar o calendário do projeto e parametrização de sábados, domingos e feriados.
    - (Dias úteis da Folha Tarefa X Quantidade Total do Insumo na Tarefa) / Dias úteis da Tarefa.
  + Capacidade Real: Para o cálculo da capacidade real do insumo, o sistema levará em consideração, em primeiro momento, o Calendário do Recurso da Tarefa. Caso não esteja preenchido irá considerar o Calendário da Atividade, aba "Mão de Obra", que retornará quantos turnos estão sendo considerados, no período, para a execução da tarefa e a quantidade de dias úteis (dias úteis - dias parados) programados para a tarefa selecionada no período. Caso a aba "Mão de Obra" não esteja preenchida, o sistema irá verificar na aba "Geral".  Caso não encontre informações, será verificada a jornada do próprio insumo e pôr fim a jornada informada nos parâmetros do projeto. Ao verificar a capacidade, será consultada a existência da equalização de insumos. Caso exista percentual de horas adotado, para o referente insumo, então a capacidade será calculada considerando-se o referido valor que consta na equalização (o campo “H.E. Adotado %”), podendo ser alocada a quantidade de horas extras até o limite máximo definido na equalização, se necessário. Caso não exista equalização ou o seu percentual seja zero significa que não será permitido à utilização de horas extras do insumo na tarefa;
  + Quantidade Alocada: Soma de toda quantidade alocada para o insumo da equipe na tarefa item da Folha Tarefa;
  + Saldo: Diferença entre Horas necessárias para realização da tarefa no período da Folha Tarefa e a Quantidade Alocada;
    - Horas Necessárias - Quantidade Alocada.
* **Tarefas**
  + Diferente dos insumos da tarefa, onde os valores são baseados em homem-hora, os valores das tarefas para o anexo de Alocação de Mão de Obra serão definidos em relação à unidade da tarefa, tendo como exemplo uma tarefa que possui unidade “M3” e insumos com unidade “HH”;

    - Quantidade Alocada no Item: Horas totais de mão de obra alocadas no item da Folha / Necessidade total de mão de obra da tarefa;
    - Quantidade Total Necessária na Folha Tarefa: (Dias Úteis da Folha \* Quantidade da Tarefa) / Dias Úteis da Tarefa;
    - Saldo no Item: Quantidade Total Necessária na Folha Tarefa - Quantidade Alocada no Item;
    - Saldo Total da Tarefa: Quantidade da Tarefa – Quantidade Total Alocada para a Tarefa.
Motivos de Improdutividade

**Motivos de Improdutividade**

---

Caso seja necessário realizar um apontamento improdutivo, deverá informar um motivo de improdutividade para mão de obra.

Os motivos de improdutividade são informados nos apontamentos e apropriações de horas improdutivas, tanto para recursos de mão de obra quanto para equipamentos.

Para mais detalhes acesse:

Apontamento de Mão de Obra - APP

**Apontamentos de Mão de Obra no app Minha Obra**

---

Após realizar as configurações para utilizar o app Minha Obra já é possivel realizar apontamentos.

Informações de como configurar o app:

Como realizar apontamentos no app de Mão de Obra :

Para visualizar o(s) apontamento (s) no sistema acesse aqui:

Apontamentos de Mão de Obra - RM

**Apontamentos de Mão de Obra no RM**

---

O apontamento de Mão de obra é realizado pelo app Minha Obra veja os detalhes em :

A visão|tela "Apontamento de Mão de Obra"  exibe o apontamento da mão de Obra retornado pelo app sem inconsistências.

Na visão|tela Folha Tarefa, também será possível visualizar os apontamentos de mão de obra e também no menu Anexos | Apontamentos de Mão de Obra.

Apropriação de Mão de Obra

**Gerar Apropriação de Mão de Obra**

---

O processo realiza a apropriação de mão de obra de apontamentos de mobilidade originados do coletor móvel confrontados com as horas registradas na folha de ponto. Para cada apontamento é gerado uma apropriação com o preço do insumo, obedecendo as regras de vigência e de preço ativo.

A funcionalidade está disponível em "Totvs Construção Obras e Projetos| Controle | Apropriações | Apropriações de Insumos / Serviços | Processos | Mobilidade | Gerar Apropriação de Mão de Obra".

Ao executar o processo o sistema solicita que seja informada uma data limite para apropriação e, de acordo com a data informada, são exibidas as tarefas que possuem apontamentos pendentes de apropriação. Caso não existam apontamentos validados, o sistema emitirá uma mensagem informando que não existem apontamentos validados até a data limite informada.

Acesse a documentação completa:

Rateio e Revaloração de Mão de Obra

Para mais informações sobre esse processo, acesse o link abaixo:

[Rateio e revaloração de mão de obra](https://tdn.totvs.com/pages/viewpage.action?pageId=421385566)Relatórios 

**Relatório Membros de Equipe**

---

O relatório**TOPREL0032 - Membros de Equipe.TotvsReport** pode ser encontrado no book de relatórios e sua geração disponibiliza os códigos de barras para serem utilizados no APP Minha Obra. A geração do relatório é através do menu Projetos \ Construção e Projetos \ Relatórios \ Mobilidade \ Membros de Equipe.

Os campos Relatório, Folha Tarefa e Equipe devem estar preenchidos para geração do relatório.

* Este relatório possibilita ao encarregado apontar as horas do funcionário sem a necessidade do crachá/identificação do mesmo. Por exemplo, o funcionário está trabalhando em um local de difícil acesso e o encarregado pelo apontamento necessita fazer a entrada, saída ou fechamento do apontamento do mesmo. Neste caso ele poderá utilizar o coletor para fazer a leitura da identificação do funcionário via código de barras impresso no relatório, realizando assim o apontamento necessário;
* Para emissão é necessário informar a folha tarefa, a equipe e o tipo de relatório. Os tipos de relatório serão os seguintes:
  + Funcionário: Exibe todos os membros da equipe, que são funcionários e que estejam associados à equipe informada pelo usuário;
  + Terceiros: Exibe todos os membros da equipe, que são cadastrados no cadastro de terceiros TOP, e que estejam associados à equipe informada pelo usuário;
  + Ambos: o sistema irá exibir todos os membros da equipe, que são funcionários ou que são Terceirizado e que estejam associados à equipe informada pelo usuário.
* Para qualquer tipo acima informado, o membro deverá estar ativo no cadastro de membros da equipe;
* A montagem dos códigos de barras é feita de forma incremental com 14 caracteres;
* Os campos a serem exibidos neste relatório são:
  + Identificador;
  + Nome;
  + Função;
  + Tipo de Membro;
  + Código de Barras.

**Relatório Feedback**

* Opção de Menu: Projetos \ Construção e Projetos \ Relatórios \ Mobilidade \ Feedback;
* Utilizado para análise das metas versus realizado de cada frente de obra de cada encarregado, com o objetivo de permitir discussões de desempenho de forma consistente e regular;
* As fontes de informação para preenchimento deste relatório são:
  + Informações de serviço, meta, e frente são retiradas do planejamento atualizado da obra (módulo planejamento), a mesma fonte das folhas semanais, quinzenais ou mensais;
  + Os status das frentes de trabalho são atualizados da mesma forma que as folhas semanais, quinzenais ou mensais de planejamento; pelo processo de apropriação e validação previsto no projeto mobilidade;
  + O feedback é feito pelos líderes responsáveis pelas frentes, assim como os planos de ação para aumentar a produtividade.
* Este relatório deve ser gerado um por encarregado, que consolidará as tarefas, metas, e resultados do encarregado. Os registros do relatório são restringidos de acordo com o contexto do TOTVS Construção Obras e Projetos, ou seja, o projeto selecionado;
* As informações são filtradas pelos campos:
  + “Mês/Ano” – Período de datas a ser considerado na busca dos registros do relatório observando o início e fim da folha tarefa. Caso seja o mês atual, então o início será o primeiro dia do mês até a data de emissão do relatório. Caso seja de um mês anterior, então englobará todos os dias do mês (ex. seleção do mês de janeiro/2013, então teremos tarefas do dia 01/01/2013 até 31/01/2013);
  + “Encarregado” – Responsável pela equipe associada a tarefa. Neste filtro podem ser selecionados mais de um encarregado e são emitidos tanto relatórios quanto o número de encarregados selecionados;
  + “Serviço” – São as tarefas constantes nas folhas tarefas e podem ser selecionadas várias tarefas para a emissão do relatório. O relatório é emitido fazendo o agrupamento das tarefas selecionadas de acordo com o encarregado;
  + “Percentual da Meta Atingida” – Significa o percentual concluído da tarefa no período da Folha Tarefa.
  + “Engenheiro” – Engenheiro responsável pelo centro de custo.
* A seleção dos registros para o relatório é com base nos filtros acima citados e agrupados pelo campo “Encarregado” e ordenadas pelo campo “Código”. Caso queira fazer outros filtros neste relatório, o usuário deve exportar o mesmo para a planilha Excel e assim efetuar os filtros conforme disponíveis;
* Não há visão semana a semana e sim, o resultado acumulado do mês. O resultado apresentado será o acumulado total no momento da geração do relatório, isto é, se o relatório for gerado ao final da primeira semana, então o acumulado será da primeira semana. Se emitido ao final da terceira semana, então o acumulado será primeira + segunda + terceiras semana.
* Exemplo para “Mês anterior” e “Mês atual”:
  + Temos uma tarefa de 100 m;
  + No primeiro mês foi programado na Folha Tarefa 30 m para serem executados, porém a equipe só fez 15 m;
  + No segundo mês foi programado em nova Folha Tarefa 50 m para serem executados dos quais foram feitos 40 m;
  + No relatório aparecerá na coluna mês anterior 50% (15 / 30) e no mês atual 80% (40/50).
