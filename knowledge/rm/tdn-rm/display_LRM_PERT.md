---
content_hash: 794f41973e90f4b71ec246dd9b5c361cd7aff1c5b5a086dbc272f1d96660cd5e
fetched_at: '2026-06-29T00:09:14.280645+00:00'
page_id: '421385178'
product: rm
source: tdn-rm
title: PERT
type: documentation
url: https://tdn.totvs.com/display/LRM/PERT
version: 39
---

---

O **PERT** na Gestão de Projetos de Construção permite ter controle do desempenho das equipes e identificar em quais Atividades elas precisam focar para que não ocorram atrasos na Obra. As informações geradas utilizando essa metodologia podem ser usadas para melhorar o direcionamento da obra e a produção, sendo que toda o acompanhamento se dá por datas programadas, realizada e percentual concluído. Possibilitando também verificar predecessor e sucessão de Tarefas.

Para dispor desta funcionalidade no sistema é necessário que o parâmetro de projeto do PERT esteja marcado como **"Utiliza"**em **Menu Projeto | TOTVS Construção Obras e Projetos | Projetos (ou atalho F6) | PERT / Alocação de Recursos**. 

Parâmetro DesabilitadoCaso o parâmetro esteja assinalado com a opção **"Não utiliza"**, o sistema **não** irá exibir esta opção no menu assim como as opções de Sincronismo com o Project e o processo de Exportar PERT para o Cronograma.PERT WebCaso o parâmetro esteja assinalado com a opção **"PERT Web"**, o sistema irá exibir esta opção no menu. Para mais informações acesse a documentação do .

Após a Parametrização, é possível acessar o PERT no **Menu Planejamento | PERT** e escolha a Planilha que deseja visualizar - As Planilhas disponíveis são de Atividades, Serviço e seus respectivos cenários.

* **Campos**

**Código da Tarefa:** Código da tarefa da planilha  
**Nome:** Nome da tarefa da planilha  
**Quantidade:** Quantidade da tarefa da planilha  
**Unidade:** Unidade da tarefa da planilha  
**Data Início Programado:** Data de início programada para a tarefa  
**Data Fim Programado:** Data fim programada para a tarefa  
**Duração Programado** Dias: Dias programados da tarefa  
**Predecessoras:** Atividades anteriores ou sucessoras a tarefa   
**Percentual Concluído:** Percentual concluído da tarefa  
**Saldo Quantidade:** Saldo de quantidade ainda disponível  
**Data Início Real:** Data início real da tarefa  
**Data Fim Real:** Data fim real da tarefa  
**Duração Real Dias:** Duração em dias entre a data início e data fim real  
**Folga (dias):** Dias de folga definidos nos **parâmetros do projeto (Não trabalha sábado/domingo etc)**  
**Data Início Cedo:** Data início cedo da tarefa  
**Data Fim Cedo:** Data fim cedo da tarefa  
**Data Início Tarde:** Data início tarde da tarefa  
**Data Fim Tarde:** Data fim tarde da tarefa  
**Data Início Base:** Data início base da tarefa  
**Data Fim Base:** Data fim base da tarefa

* **Acompanhamento e Controle**

Ao acessar a visão do PERT onde se acompanhamento e controle, é possível visualizar algumas informações das Tarefas, como o **Código da Tarefa, Nome, Quantidade e Unidade.**

Além disso, é possível informar as datas de execução das Atividades, são elas:

* **Data Início Programado:**Data Prevista para o início da execução das Atividades;
* **Data Fim Programado:**Data Prevista para o fim da execução das Atividades;
* **Duração Programado Dias:**Duração em dias do intervalo de tempo Previsto para a execução das Atividades;
* **Data Início Real:**Data que iniciou a execução das Atividades;
* **Data Fim Real:**Data que finalizou as Atividades;
* **Duração Real Dias:**Duração em dias do intervalo de tempo real da execução das Atividades;

Através do acompanhamento destas datas é possível visualizar a diferença entre o Previsto e Realizado em datas da execução da Tarefa.

É possível informar no planejamento as atividades **Predecessoras/Sucessoras.**A definição é realizada conforme as ligações:

* **FI -**Fim – Início: A tarefa sucessora inicia quando termina sua tarefa predecessora. (Cálculo: Data Fim da sucessora = Data início da predecessora + defasagem + 1)
  + Observação: Só deve somar 1 dia caso a duração da tarefa predecessora seja em dias e não em horas.
* **FF -**Fim – Fim: A tarefa sucessora termina quando termina sua predecessora. (Cálculo: Data Fim da sucessora = Data Fim da predecessora + defasagem)
* **II -**Início – Início: A tarefa sucessora inicia quando começa sua predecessora. (Cálculo: Data Início da sucessora = Data Início da predecessora + defasagem)
* **IF -**Inicio – Fim: A tarefa sucessora termina quando começa sua predecessora. (Cálculo: Data Início da sucessora = Data final da predecessora + defasagem - 1)

Ao incluir uma tarefa sucessora é verificado se a atividade principal está com o seu período preenchido,   
caso esteja o lançamento das datas da atividade sucessora será feito automaticamente.

**Defasagem:** diferença em dias, entre o início da sucessora e o término da atividade corrente (não é uma   
folga).

Caso a data real for igual a data programa o processo "Programar" não alterará a data programada para aquela tarefa. Sábados, Domingos e Feriados, definidos nos parâmetros do projeto. Caso os parâmetros ‘Trabalho aos Sábados’, ‘Trabalho  os Domingos’ e ‘Trabalho aos Feriados’ estejam desmarcados, no momento do lançamento de datas é verificado se as datas são finais de semana ou feriados e é impedido o lançamento.

* **Vínculo entre etapas - PERT**

No geral, todas as obras têm um prazo para entrega estipulado antes do começo das etapas construtivas. Mas só a data final não é suficiente, é preciso que todas as atividades sejam descritas e planejadas de forma detalhada, com prazos para começo e término, além de uma ordem definida para cada uma. Criar etapas com filhos com diversos níveis e efetuar o vínculo entre elas através da edição da coluna Predecessora ou através do botão Vincular Tarefas; Efetuar vínculos entre etapas e tarefas desde que não exista parentesco entre elas.

Caso seja solicitado o vínculo uma mensagem deverá aparecer; Vincular uma etapa a uma etapa predecessora. Caso aconteça toda árvore da etapa deverá sofrer alteração, considerando a regra dos vínculos já existentes; Caso uma etapa receber o vínculo de uma predecessora, visivelmente, apenas a linha da etapa deverá ser alterada com a ligação de predecessão, sendo que os filhos terão também a predecessora informada, mas não estará visível ao usuário; Ex: 2FI O cálculo das datas dos filhos da etapa que recebe a predecessora e que já tenham alguma ligação deverá ser feito normalmente, considerando a predecessora da etapa pai.

Esta informação ajuda ao PERT/CPM a replanejar as datas das demais atividades usando as informações de predecessão das demais atividades e o impacto que a data real trará nelas.  
Mesmo quando a atividade não estiver terminada é possível realizar o controle de percentual concluído. Este controle dará também ao Totvs Obras e Projetos informações valiosas que serão utilizadas no próprio PERT/CPM, no cronograma, controle de avanço físico entre outros.

Após o preenchimento do Percentual Concluído aproveitar os dados lançamentos no PERT para fazer outros acompanhamentos pode-se converter  dados do PERT para o Cronograma.

* **PERT/CPM - Cálculo do Caminho Crítico**

O caminho crítico é a sequência de tarefas que leva mais tempo para ser terminada. Essa sequência determinará o tempo total do projeto de construção e não haverá folgas nas atividades. É a informação mais importante porque, a partir dela, é possível identificar quais serviços devem ser priorizados e finalizados no prazo para que a obra não sofra atrasos.

Para calcular o PERT o plano programado das atividades precisa estar definido.

O plano cedo e o plano tarde (datas início e fim) das tarefas é calculado considerando a data início do projeto, a duração e a dependência das tarefas.

A folga é o número de dias que uma atividade pode ser atrasada sem impactar no término do projeto. Dessa forma, quando uma tarefa possui uma folga zero ela é crítica.

O Cálculo do PERT possibilitará o conhecimento do Caminho Crítico:

* Tarefas que atrasarem, por consequência atrasarão o projeto. Por isso o conhecimento prévio destas atividades permitirá ao gestor orientar as atenções e ter um maior cuidado com as tarefas mais importantes.
* Atividades que adiantam o seu término também podem alterá-lo basta calcular o PERT.
* Esse processo irá calcular as folgas, o plano cedo e o tarde.

Para reajustar o percentual concluído de uma tarefa que já possui Data início Real e Data Fim Real, deve ser removida a Data Fim Real para que o PERT permita que seja informado um novo percentual concluído.

* Selecione a pasta Tarefa, clique em Processos e selecione a opção  "Exportar PERT para Cronograma". Para que a conversão seja feita são necessárias algumas informações:
* Data de origem (base, programada ou real): qual data do PERT será exportada para o cronograma; Cronograma de destino (previsto, realizado ou medido): para qual cronograma os dados do Pert serão exportados; Converter medições para (percentual, quantidade ou valor): utilizado para indicar como será gravada a informação no cronograma, no campo percentual, quantidade ou valor; Escopo da conversão (tarefas marcadas ou todas as tarefas): quais tarefas terão o conteúdo convertido do PERT para o Cronograma. Funções do Planejamento
* Nas funções do planejamento ainda é possível: passar uma linha de base para salvar o estado de um planejamento. Posteriormente se for necessário recuperar este planejamento ele pode ser consultado nos campos de data de linha de base ou restaurado através da função Linha de Base como Planejamento.
* Programar: Para cada atividade de primeiro nível propaga sua data de fim para as sucessoras desde que a sucessora não esteja com data de fim realizada preenchida e calcula sua duração.
* Para calcular o PERT todas as atividades precisam estar com as datas programadas preenchidas.
* Atualizar linha de base: preenche o plano base: transfere as data início e fim do plano planejado para o plano base. Funciona como uma linha de base. Linha de base como planejamento:  transfere as datas de início e fim do plano base para o plano planejado. Plano tarde como planejamento: transfere as datas de início e fim do plano tarde para o plano planejado. Plano cedo como planejamento:  transfere as datas de início e fim do plano cedo para o plano planejado. Informações do Projeto: exibe a data início e fim do projeto e a duração em dias.

**Duração decorrida:** o período de tempo que uma tarefa levará para terminar, baseado em um dia de 24 horas e uma semana de 7 dias, incluindo feriados e outros dias de folga. Esta duração é baseada no cálculo de Trabalho (esforço) e não em datas corridas. Ou seja, **diasd** é uma medida de esforço traduzida em tempo.  
Na utilização de diasd, o Project calcula automaticamente o tempo em dias comuns e repassa esta informação ao TOP na sua integração.  
Assim sendo, como exemplo, 7 diasd correspondem a 168 horas de Trabalho. Na Integração, supondo 8 horas de Jornada, o Project calcula automaticamente 21 dias de duração (168 horas dividido por 8 horas).

**Atenção:**  
Para efeitos de duração, não recomendamos a utilização da unidade dias, em virtude do cálculo supracitado

**PERT- Demais Recursos e Funcionalidades**

* O Módulo PERT possui uma gama de recursos na barra principal e nos botões Anexos e Processos. Vamos agora falar de alguns deles:
  + **Posicionar:** Se estiver com dificuldade para visualizar a barra gráfica do Gantt posicione o cursor na tarefa desejada e clique no ícone "Posicionar". O posicionamento pode ser Automático ou Manual. Quando é marcado o posicionamento **Automatico**, ao clicar na tarefa e depois em "Posicionar" você visualiza a barra do Gantt do lado direito da tela. Quando o posicionamento é manual o usuário tem que localizar a barra através das datas
  + **Resumir**: Para visualizar somente as etapas do projeto clique em "Resumir".
  + **Expandir**: Para visualizar as tarefas e as etapas do projeto clique em "Expandir".
  + **Descrição Gantt**: Para definir se a Tarefa no gráfico de Gantt sairá sem descrição, com código ou com nome, clique em "Descrição Gantt".
  + **Escala** **de tempo**: Para definir a escala de tempo para visualização do gráfico de Gantt, clique no ícone "Escala de tempo" e escolha a que desejar: Dias, Semanas, Meses, Trimestres ou Anos.
  + **Diminuir** **largura** **da escala**: - Clique em "Diminuir largura da escala" quando desejar reduzir a largura da escala em tempo no gráfico de Gantt.
  + **Aumentar largura da escala**: - Clique em "Aumentar largura da escala" quando deseja aumentar a largura da escala em tempo no gráfico de Gantt.
  + **Configurador** **de** **Layout**: Existem diversas visualizações do PERT, que podem ser definidas através do ícone "Configurador de Layout". A qualquer momento você pode modificar a forma de visualizar o gráfico de Gantt. A configuração padrão é **Planejado** **x** **Real**, ou seja, o plano planejado e o plano real ao mesmo Anexos: Através dos anexos várias informações auxiliares são fornecidas para o planejador. Dentre elas:  
     Predecessoras  Sucessoras  Insumos  Composições  Datas da Atividade  Detalhes da Atividade  Detalhes do Recurso

* **Arraste para alterações de valores**

Caso algum valor (datas, percentual concluído, etc) de uma etapa for alterado, a alteração deverá ser replicada aos filhos de primeiro nível que não tenham filhos, considerando os vínculos existentes; Selecionar uma célula e replicar o seu valor às demais células da coluna corrente, arrastando com o mouse e soltando na última célula a ser alterada. Essa alteração deverá considerar o parâmetro, pois os valores de uma etapa só poderão ser alterados se o parâmetro estiver marcado como etapa; Alterar com arraste apenas na mesma coluna de seleção; As células selecionadas que estiverem nas colunas editáveis deverão ter cores diferentes das células das colunas não editáveis; Arrastar as células, selecionando para alteração, a cor deve ser a mesma da célula corrente, e ao soltar o clique do mouse os itens alterados devem mudar de cor, simplesmente para informar de uma forma visualmente melhor as alterações realizadas;

 Veja os parâmetros que podem interferir no cálculo do PERT. Somente é possível editar uma célula de cada vez no PERT. Assim, ao alterar uma célula deve-se salva-la antes de alterar outra, pois o sistema não permite a edição de outras, enquanto as alterações já feitas não forem atualizadas.

* **PERT - Cenários**

Para todos os Cenários é possível utilizar o PERT da mesma maneira que ele é utilizado na Planilha de Atividades. Para cada Cenário ativo será apresentado um PERT correspondente pelo menu  Cadastros | PERT | Cenários.

Aba GanttImpressão

**Imprimir Gantt**

Nesta funcionalidade é possível visualizar a impressão atual.

Grid Pert

**Vincular Tarefas**

**Desvincular Tarefas**

Nesta funcionalidade é possível realizar o vinculo de tarefas no PERT.

**Expandir** - Expande todas as tarefas

**Resumir** - Fecha todas as tarefas

**Posicionar** - Posiciona na tarefa desejada.

Gantt Pert

**Calculo do Pert**

Calculo do plano cedo , tarde, caminho crítico e folga.

**Descrição Gantt**

Descrição associada a barra no Gantt.

**Funções do Planejamento**

* **Análise de Ordem de Produção**

O processo de análise de ordem de produção será exibido apenas em ambientes integrados com Protheus e com o pacote PCP ou em ambientes com Backoffice RM. Este processo é responsável por buscar as datas de entrega das ordens de produção e atualizar o planejamento das tarefas no PERT.

Observações: Ao realizar o processo o mesmo irá atualizar as datas e Programar o PERT, levando em consideração as parametrizações de trabalho conforme imagem abaixo:

**Escala de tempo**

**Exibir caminho crítico**

Exibe as tarefas criticas

**Largura de escala**

**Configurador de Layout**

Troca a exibição do Gantt

Processos

Exportar Pert para o Cronograma

**Informações complementares**

 

[Insumo](http://tdn.totvs.com/display/LRM/Insumos)
