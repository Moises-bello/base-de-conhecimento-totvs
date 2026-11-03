---
content_hash: cb6f29c95765465bc48f531369ca47249850bf26f412da200dfa20da23a59338
fetched_at: '2026-06-29T00:12:02.389730+00:00'
page_id: '900742720'
product: rm
source: tdn-rm
title: Relatório Folha Tarefa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=900742720
version: 4
---

---

**Relatório Folha Tarefa**

* Campos da Folha Tarefa impressa:
  + Número da Folha Tarefa;
  + Nome da Folha Tarefa;
  + Data de Criação;
  + Data da Carga no Coletor;
  + Data de Início da Execução;
  + Coletor;
  + Código da Tarefa;
  + Nome da Tarefa;
  + Centro de Custo;
  + Quantidade no Período;
  + Quantidade Total;
  + Saldo a Executar;
  + Unidade de serviço;
  + Executado 100% (Checkbox);
  + Código de barras;
  + Responsável pela Execução.
* O código de barras contém informações suficientes para que em sua leitura o sistema consiga identificar de qual projeto/obra/tarefa está se referindo o valor do apontamento e seja capaz de gravá-lo.

* + **Interface de Coleta Via Código de Barras**
    - Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa \ Anexos \ Interface de Coleta Via Código de Barras;
    - O menu de acesso à Interface de Coleta via Leitura de Código de Barras somente está disponível para Folhas Tarefa com o status “Pronta para Impressão”, ou seja, ao selecionar na visão, uma folha com o status diferente do citado, o menu ficará desabilitado. Além disso, o processo só pode ser acessado caso a folha tenha o tipo de apontamento manual;
    - O anexo de Tarefas da Folha Tarefa já possui uma série de informações sobre as tarefas e será disponibilizada uma área com controles e tratamentos específicos para se efetuar a leitura dos códigos de barra e atualização do sistema a partir dos dados informados nesta área;
    - Nela contém um indicador de 100%, um campo para o código de barras e botões com percentuais de completude (0%, 25%, 50%, 75%);
    - Esta interface será apresentada de acordo com perfil do usuário que indica os usuários que irão realizar a leitura do código de barras, direto no sistema, terão de ter permissão para fazê-lo;
    - O usuário marca o indicador de 100% e realizará a leitura do código de barras. Em seguida, o sistema irá interpretar este código de barras identificado a qual tarefa se refere e atualizará o campo de apontamento com o 100%;
    - Pode ocorrer da tarefa não estar com 100% de completude, então o usuário pode desmarcar o indicador de 100%, efetuar a leitura do código de barras e selecionar o percentual de completude (0%, 25%, 50%, 75%). Ao efetuar esta seleção o sistema irá interpretar este código de barras identificando a qual tarefa se refere e atualizará o campo de apontamento de acordo com o percentual selecionado. As informações serão gravadas em uma tela de validação, não atualizando diretamente o PERT.

A geração do relatório é através do menu Projetos \ Construção e Projetos \ Relatórios \ Minha Obra\ Folha tarefa.

O relatório **TOPREL0031 - Folha Tarefa (Mobilidade) - com filtro.TotvsReport** pode ser encontrado no book de relatórios e sua geração disponibiliza as folhas tarefas para serem utilizados no APP Minha Obra.

O relatório **TOPREL0031.1 - Folha Tarefa (Atividades Executiva) - com filtro.TotvsReport** pode ser encontrado no book de relatórios e sua geração disponibiliza as folhas tarefas para serem utilizados no APP Minha Obra.
