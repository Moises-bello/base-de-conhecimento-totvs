---
content_hash: b1444614f1266b81e98de5485e3ecb682fb3452c384c0a031fca1b093ac83a0e
fetched_at: '2026-06-29T00:09:14.778369+00:00'
page_id: '421385252'
product: rm
source: tdn-rm
title: Folha Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/Folha+Tarefa
version: 42
---

---

A Folha Tarefa foi criada com o objetivo de agilizar o direcionamento de tarefas nas frentes de obra e acompanhar os projetos através de envio/recebimento de informações sobre o andamento das tarefas com o uso de coletores móveis, podendo ser considerada como um planejamento a curto prazo. Trata-se de uma planilha em que é possível visualizar as tarefas a serem realizadas em um dado intervalo de tempo, distribuir os planejamentos entre as equipes/usuários das diversas frentes de obras, receber/gerir os apontamentos e atualizar o TOP com tais informações após sua validação.

O usuário deve montar uma Folha Tarefa com as tarefas e seu planejamento a curto prazo e exportar suas informações para o coletor móvel. Outros usuários devem registrar, através dos coletores, as informações (apontamentos) sobre o andamento das tarefas exportadas, sendo que tais informações serão importadas para o Totvs Obras e Projetos para atualização do PERT.

**Observação:** A Folha Tarefa é criada por Projeto e sua inclusão, edição ou exclusão é feita em "Controle | Minha Obra| Folha Tarefa". A criação da Folha Tarefa faz validação com a Parametrização Projeto | Construção e Projeto | Projetos (ou atalho F6) | Mobilidade | 'Quebra por período do Cronograma'. Quando este parâmetro estiver habilitado a Data Inicio e Fim da Folha deve estar no período parametrizado. Caso o usuário queira fazer um intervalo fora deste período o sistema irá automaticamente dividir em duas ou mais Folhas Tarefa dentro da data dos períodos subsequentes.

**Os campos pertinentes ao cadastro de Folha Tarefa Padrão são:**

**Planilha de Origem para apontamentos:** Este campo virá preenchido com a planilha, de Atividades ou Executiva (conforme definido nos parâmetro Planilha para apontamentos veja em: ), na qual serão realizados os apontamentos.

O preenchimento deste campo obedecerá ao que esta definido no campo Planilha Origem dos parâmetros do projeto (F6 > Mobilidade > Folha Tarefa).  [Saiba mais.](https://tdn.totvs.com/pages/viewpage.action?pageId=421385212)

**Número:** Código identificador da Folha Tarefa.

**Status da Folha Tarefa:** Identifica em que etapa está a Folha Tarefa:

* **Em processamento:** A folha está sendo preparada para ser gerada, porém ainda não disponibilizada para os dispositivos de coleta de dados;
* **Gerada:** folha cadastrada e não associada a nenhum coletor;
* **Encerrada:** quando o PERT já foi atualizado; ou
* **Cancelada:** após executar o processo de Cancelamento da Folha Tarefa.

**Tipo:** Define o tipo da folha gerada

* **Padrão:** que é o tipo já conhecido e utilizado no App Minha Obra, ou
* **Produtividade:** refere ao [Pacote de Serviços](https://tdn.totvs.com/display/LRM/Folha+Tarefa#:~:text=Pacote%20de%20Servi%C3%A7o%20%2D%20Folha%20de%20Produtividade), e faz com que a Folha Tarefa assuma algumas características específicas, conforme detalhando neste tópico.

**Descrição:** Nome resumo da Folha Tarefa para facilitar a sua identificação.

**Data Criação:** Exibe a data do dia em que a Folha foi criada, buscando da data do servidor.

**Data Apontamento:** Data em que foram realizados os apontamentos.

**Data de Atualização do PERT:** Data gravada após a execução do processo de atualização do PERT.

**Período das Tarefas da Folha:** Determinará a data final do planejamento, podendo ser "Semanal", "Quinzenal", "Mensal" ou "Personalizada".

**Data Início:** Início do intervalo de tempo da Folha Tarefa, será utilizado como filtro para a associação de tarefas o cronograma da Planilha de Atividades.

**Data Fim:** Data final do intervalo de tempo da Folha Tarefa.

**Tipo de Apontamento:** Define se o apontamento será feito através de coletor móvel, manual (leitor de código de barras) ou avulso.

* **Coletor Móvel:**  Os registros são efetuados nos coletores associados durante o intervalo definido para a folha de tarefa.
* **Manual:** É possível inserir registros manualmente no sistema.
* **Avulso:** Uma folha do tipo avulsa é gerada exclusivamente para sincronizar os registros feitos de forma avulsa no aplicativo Minha Obra com o RM. Neste caso, as datas estabelecidas no período da folha não são consideradas durante a realização dos apontamentos, sendo assim, o apontamento avulso pode ser realizado fora do período da folha avulsa, desde que sua data seja entre as datas de início e fim do projeto.

**Folhas Tarefas** do tipo **Avulso** não são sincronizadas para o aplicativo Minha Obra, com isso após sua criação ela permanece com status de Em Processamento. A criação dessa folha é necessária para que seja possível a sincronização dos apontamentos avulsos de Mão de obra  que foram realizados no coletor.

**Pronto para impressão:** Após marcar este campo, nenhuma alteração poderá ser realizada na Folha Tarefa, pois esta opção habilita a impressão da mesma.

Após o cadastro da Folha Tarefa é preciso associar as tarefas da Planilha de Atividades ou Planilha Executiva (Conforme parâmetro **Planilha para Apontamentos [Mobilidade (F6)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385196))** . Tal associação será feita através do anexo "Itens da Folha Tarefa" e poderá ser executada de três maneiras diferentes:

* Uma Folha Tarefa, representada principalmente por suas tarefas, pode ser considerada como um planejamento em curto prazo. Através desta Folha será possível ter o conhecimento das tarefas a serem realizadas em um dado intervalo de tempo bem como distribuir estes “planejamentos” entre as equipes/usuários das diversas frentes de obra, receber/gerir os apontamentos para diversas funções que as tarefas podem representar;
* Permite a alocação de equipes para a execução. Após o término da alocação, a mesma fica disponibilizada para ser sincronizado pelo coletor e posterior registro e envio dos apontamentos referente as frentes de execução;
* O objetivo desta funcionalidade é maior agilidade no direcionamento de tarefas nas frentes de obra e acompanhamento dos projetos através do envio/recebimento de informações sobre o andamento das tarefas (e atualização no TCOP) com o uso de coletores móveis (a princípio smartphones). Para isso **a folha tarefa a ser disponibilizada para o coletor deve ser a folha tarefa do tipo Coletor Móvel;**
* Permite o sincronismo de informações para o coletor móvel e o gerenciamento dos apontamentos realizados e sincronizados;
* Depende do cadastro do projeto;

Uma Folha Tarefa poderá se encontrar em uma das seguintes **Situações**:

* **Em Processamento**: Folha Tarefa criada, porém ainda não disponibilizada para os dispositivos de coleta de dados;
* **Disponível para Coletor (Gerada)**: Folha Tarefa cadastrada e disponível para o coletor;
* **Pronta para Impressão**: Folha Tarefa disponível para impressão e coleta através do leitor de código de barras;
* **Encerrada**: Folha Tarefa encerrada. O PERT já foi atualizado. Esta situação significa que todos os dados dos coletores já foram recebidos para todas as tarefas, validados e atualizados no PERT;
* **Cancelada**: Folha Tarefa cancelada. Não permite qualquer outra operação. Os dados das tarefas (por exemplo, oriundos de coletores) desta Folha não poderão gerar atualização no PERT e não poderão ser importadas informações dos coletores;
* **Associada ao coletor**: Folha Tarefa foi enviada ao coletor móvel;
* **Apontada**: Folha Tarefa possui apontamentos em seus itens após a mesma ter sido fechada no coletor.

A data fim da Folha é calculada conforme a periodicidade informada e o valor do parâmetro “Quebra por períodos do Cronograma”, exceto quando a periodicidade é definida como **Personalizada**;

Primeiramente determina-se o valor da data fim de acordo com a periodicidade:

* **Semanal**: Se Soma seis dias a data inicial;
* **Quinzenal**: Se Soma quatorze dias a data inicial;
* **Mensal**: Se Soma trinta dias a data inicial;
* **Personalizada**: Permite a alteração manual das datas início e fim.

Posteriormente, caso o parâmetro “Quebra por períodos do Cronograma” esteja selecionado, será verificado se existe algum fim de período no cronograma entre as datas inicial e final informadas na Folha. Caso exista, o valor encontrado será utilizado como data fim da folha e será exibida uma mensagem contendo informações sobre a quebra. Posteriormente, o usuário poderá cadastrar um novo item a fim de complementar o período. Caso contrário, será exibida uma mensagem de erro, informando que não foi possível encontrar um intervalo de cronograma. Esse parâmetro somente estará habilitado se a periodicidade padrão for diferente de Personalizada.

* Ao habilitar o Parâmetro 'Utiliza Folha Tarefa', a Folha Tarefa será exibida no Menu de Mobilidade e em todos os locais no app Minha Obra.
* Ao realizar o sincronismo com o app Minha Obra, todas as Folhas Tarefas associadas ao coletor, serão enviadas para o mesmo e ficarão disponíveis para apontamento.

---

**Processo Associar Tarefa à folha**

---

O usuário deve selecionar a Folha Tarefa a qual deseja associar tarefas e executar o processo Associar Tarefa à Folha, o sistema filtra as tarefas da Planilha de Atividades ou Planilha Executiva (Conforme parâmetro **Planilha para Apontamentos )** que condizem com o período da Folha e as exibe para que o usuário selecione as que serão associadas.

---

**Associação Manual de Tarefas**

---

Clicando no botão Incluir do anexo Itens da Folha Tarefa, o sistema exibe uma tela para seleção da tarefa/obra/Item que deseja associar à Folha Tarefa. O sistema só permite a associação se a tarefa estiver dentro do período da Folha Tarefa.

**Observação:** - Se uma tarefa estiver associada a uma Folha Tarefa, o sistema só permitirá associar a uma nova Folha Tarefa caso a primeira esteja com situação "Cancelada" ou "Encerrada", e neste segundo caso apenas de houver saldo a realizar.

* As tarefas da Folha Tarefa podem ser excluídas através do botão Excluir do Anexo Itens da Folha Tarefa, desde que a Folha Tarefa não tenha sido associada a algum coletor.
* Se o parâmetro Planilha para apontamentos  estiver definido como Planilha Executiva ,na seleção de itens, somente devem ser apresentados itens que estejam vinculados a pelo menos 1 tarefa da Planilha de Atividades.
* A possibilidade de vincular um contrato a tarefa associada na folha tarefa só será permitida apenas para Planilha de Atividades.

---

**Drag-and-Drop com a Planilha de Atividades**

---

Com o anexo Itens da Folha Tarefa e a Planilha de Atividades abertos, o usuário deve posicionar as duas janelas lado a lado, e arrastar/soltar as tarefas da Planilha de Atividades para o anexo Itens da Folha Tarefa. Na visão da Planilha de Atividades é possível fazer um filtro das tarefas por período, através do menu Outros | Por Período, que fica no combo de menus da visão Funções Principais | Visualizar. O uso do filtro facilita o processo de associação, pois mostrará a visualização somente das tarefas que fazem intercessão com o período da Folha Tarefa. O usuário poderá também selecionar uma obra ou etapa da Planilha de Atividades e arrastá-la para a Folha Tarefa. Neste caso o sistema irá inserir todas as tarefas filhas relativo ao registro agrupador selecionado (Obra ou Etapa), respeitando o período da Folha Tarefa, ou seja, tarefas filhas que não façam parte do período da Folha Tarefa em questão não poderão compor a Folha Tarefa.

**Observação:**

As tarefas inconsistentes são as que estejam com quantidade zerada ou com cronograma diferente da periodicidade da folha tarefa. Ao associar tarefas manualmente ou pelo processo da folha tarefa serão exibidas somente as tarefas que não possuam inconsistência.

* Ao realizar o drag-and-drop com a planilha de atividades não há como filtrar da mesma maneira que a associação manual ou do processo, portanto, quando o usuário arrastar as tarefas que estejam inconsistentes com a folha tarefa e informar que deseja associá-las, uma mensagem de log será exibida informando o motivo da sua inconsistência.
* Não é possível associar "Obras" e nem "Etapas" na folha tarefa.
* Essa funcionalidade drag-and-drop só está disponível para Planilha de atividades.
* É possível cancelar a Folha Tarefa, o que irá alterar o status da associação aos coletores para "Cancelada" e implicará que os dados das tarefas (por exemplo, oriundos de coletores) desta Folha não poderão gerar atualização no PERT e não poderão ser importadas dos coletores. As tarefas associadas a uma Folha cancelada poderão ser associadas a outras Folhas. O cancelamento é feito através do menu "Processos | Cancelamento de Folha Tarefa".

**Atenção:** Caso a Folha Tarefa esteja com o status "Associada ao coletor" a mesma poderá ser cancelada ou sincronizada. Somente quando a Folha Tarefa não estiver com status de associada ela será liberada para alteração ou exclusão.

**Observações:** Durante o registro dos apontamentos, informações da localização são coletadas e enviadas no sincronismo para o sistema, o que possibilita verificar as posições dos apontamentos do coletor referentes a Avanço Físico e Mão de Obra através da aba "Mapa" localizada na tela de edição da Folha Tarefa. Para habilitar esta funcionalidade é preciso configurar "Chave de identificação para o Google Maps" em "Ambiente| Parâmetros| Parâmetros Globais| Google".

## **Pacote de Serviço - Folha de Produtividade**

O cadastro do Pacote de Serviço é realizado no cadastro da Folha Tarefa, onde a mesma pode assumir dois tipos distintos, o tipo **"Padrão"**, que é o tipo já conhecido e utilizado no App Minha Obra, e o tipo **"Produtividade"**, que se refere ao pacote de serviços, e faz com que a Folha Tarefa assuma algumas características específicas:

* Ao selecionar o tipo da Folha Tarefa como Produtividade, além da Descrição e Tipo de Apontamento é necessário preencher a equipe do Pacote de Serviço;
* Não é necessário preencher a Periodicidade e Datas de Início e Fim, essas serão preenchidas automaticamente como **Personalizada**, **Data Inicial do Projeto** e **Data Final do Projeto** respectivamente. Recomendamos manter sempre essas datas, porém, caso opte por alterá-las, é importante atentar-se ao fato de que a Folha de Produtividade possui regras específicas e somente considera tarefas que se enquadrem nas situações abaixo:
  + Data de início da tarefa >= Data de início da Folha de Produtividade e
  + Data de início da tarefa <= Data fim da Folha de Produtividade.
* Anexos e Processos que não estão disponíveis para esse tipo de folha:
  + Programado X Alocado;
  + Alocação de Mão de Obra;
  + Equipes Associadas à Folha Tarefa;
  + Recalcular Planejamento das Tarefas;
  + Alocar Mão de Obra na Folha Tarefa.
* **Itens da Folha Tarefa:**Para esse tipo de folha, a associação de Tarefas à mesma, deve obedecer algumas regras que não são consideradas no tipo de folha tarefa "Padrão":

* No lookup da tarefa é possível filtrar por Unidade de Serviço, Local de Serviço e/ou a Equipe no qual a Tarefa está associada;
* As Tarefas que são exibidas são aquelas que ainda possuem saldo e que ainda não foram iniciadas, e uma tarefa considerada não iniciada deve ter as seguintes características:
  + Não ter sido apropriada;
  + Não ter realizado no cronograma;
  + Não ter medido no cronograma;
  + Não ter apontamento de folha tarefa;
  + Não ter medição de contrato.
* É necessário definir o Valor Alocado para a Tarefa na Folha de Produtividade. Ao defini-lo o saldo da tarefa em relação ao seu valor total é recalculado;
* Ao salvar o registro o Valor Alocado de todas as tarefas da folha são somados e distribuídos entre os membros da equipe associada à folha tarefa, onde o cálculo considera o peso definido no cadastro do membro, como por exemplo:
  + Total Alocado dos itens da folha = 500,00
  + Membros da equipe:
    - JOSÉ: Peso = 3
    - JOÃO: Peso = 1
    - MARIA: Peso = 1
  + Distribuição dos valores:
    - JOSÉ: 60% x 500,00 = 300,00
    - JOÃO: 20% x 500,00 = 100,00
    - MARIA: 20% x 500,00 = 100,00
* No anexo "Distribuição de Valores da Equipe" em Folha Tarefa, são exibidos os membros da equipe com seus valores devidamente distribuídos:

* **Validações:**
  + Processo de drag-and-drop não é permitido para esse tipo de folha;
  + O Valor Alocado não pode ser maior que o valor da tarefa ou o saldo;
  + O Valor Alocado não pode ser menor ou igual a zero.

**Processo de Associar Tarefas (Itens) na Folha Tarefa:**Para esse tipo de folha,  o processo de associar de Tarefas à mesma, deve obedecer as mesmas regras do anexo e que também não são consideradas no tipo de folha tarefa "Padrão":

* + Na tela do processo, também é possível definir alguns filtros para a seleção da Tarefa desejada, a Unidade de Serviço, o Local de Serviço e/ou a Equipe no qual a Tarefa está associada;
  + As Tarefas que são exibidas são aquelas que ainda possuem saldo e que ainda não foram iniciadas, assim como no anexo;
  + Se o tipo de folha definido for Produtividade é necessário definir o Valor Alocado para a Tarefa na Folha de Produtividade, basta editar o valor no grid na coluna Valor Alocado;
  + Se a folha for do tipo produtividade e possuir valor e quantidade alocado o processo verifica se tal quantidade ou valor é maior que a quantidade ou valor total planejado para a tarefa. O valor alocado não pode ser maior que o valor da mão de obra da tarefa.A menos que o parâmetro “Permite associação acima do valor orçado” estiver habilitado.

Quando a folha tarefa for do tipo padrão:

A quantidade programada e quantidade planejada, é calculada da seguinte forma:

(qtdeTarefa - (qtdeTarefa \* percConcluidoTarefa / 100) - qtdePlanejada) \* diasIntersecaoTarefaFolha / diasRestantesTarefa)

Onde:

**QtdeTarefa:** É a quantidade total da tarefa (Planejada na Planilha de atividades).

**PercConcluidoTarefa:**  É o percentual já concluído da tarefa.

**QtdePlanejada:** É a quantidade planejada dessa tarefa em qualquer outra folha ativa.

**DiasIntersecaoTarefaFolha:** São os dias da tarefa na folha.

**DiasRestantesTarefa:** São os dias uteis restantes na folha, lembrando que a definição de dias uteis pode ser parametrizada.

Quando a folha tarefa for do tipo de produtividade não será distribuída da mesma forma que na folha padrão não será aplicada a mesma formula de cálculo. Utilizando a quantidade informada pelo usuário e realizando as validações referentes a produtividade.

* Se o tipo de folha definido for Produtividade é necessário definir o Valor Alocado para a Tarefa na Folha de Produtividade, basta editar o valor no grid na coluna Valor Alocado;
* Se a folha for do tipo produtividade e possuir valor e quantidade alocado o processo verifica se tal quantidade ou valor é maior que a quantidade ou valor total planejado para a tarefa. O valor alocado não pode ser maior que o valor da mão de obra da tarefa.A menos que o parâmetro “Permite associação acima do valor orçado” estiver habilitado.

Saiba mais em: [Unidade de Serviço e Local de Serviço](http://tdn.totvs.com/pages/viewpage.action?pageId=451251865)

Anexos

---

 

 

 

 

 

   
   
  Processos

---

[Incluir Folha Tarefa](https://tdn.totvs.com/display/LRM/Incluir+Folha+Tarefa)

[Associar Coletor a Folha Tarefa](https://tdn.totvs.com/pages/viewpage.action?pageId=421385377)

[Alocar Mão de Obra na Folha Tarefa](https://tdn.totvs.com/pages/viewpage.action?pageId=421385144)

[Incluir membros de Equipes na Folha Tarefa](https://tdn.totvs.com/display/LRM/Incluir+membros+de+Equipes+na+Folha+Tarefa)

---

[Disponibilizar Folha Tarefa para apontamentos](https://tdn.totvs.com/display/LRM/Disponibilizar+Folha+Tarefa+para+Apontamentos)

[Retornar Folha Tarefa para em Processamento](https://tdn.totvs.com/display/LRM/Retornar+Folha+Tarefa+para+processamento)

---

[Gerar Relatório de Folha Tarefa](https://tdn.totvs.com/pages/viewpage.action?pageId=900742720)

Recalcular Planejamento das Tarefas

 

 

---
