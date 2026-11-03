---
content_hash: 5450ca7effe3f447447808d385b629c1c813ed2ada1d67bc370158a03e4f1e73
fetched_at: '2026-06-29T00:10:57.975706+00:00'
page_id: '601701583'
product: rm
source: tdn-rm
title: Painel de Cirurgias
type: documentation
url: https://tdn.totvs.com/display/LRM/Painel+de+Cirurgias
version: 27
---

1. **Visão Geral**
2. **Folha de Sala**
3. **Registro de informação cirúrgica**

falsepaineltrueVisão Geral

## **01. VISÃO GERAL**

A tela pode ser acessada através de Cuidados com o Paciente > Painel de Cirurgias.

Ao acessar a opção Painel de Cirurgias a seguinte tela é apresentada com os dados das cirurgias agendadas para a data do filtro selecionado:

Os campos a serem exibidos são:

* tipo do agendamento : eletivo e não eletivo (com ícones)
  + Os pacientes com agendamento eletivo são os que foram agendados na agenda cirúrgica, até o dia anterior
  + Os pacientes com agendamento não-eletivo, são os que foram agendados na agenda cirúrgica no mesmo dia do procedimento
* Status do procedimento: programado, em andamento, liberado, concluído e cancelado.
  + 0 - Procedimentos com status programado são aqueles agendados, que ainda não chegaram no serviço/não tem atendimento aberto.
  + 2 - Procedimentos com status em andamento são aqueles que já chegaram, foram acomodados em sala de cirurgia e já possuem contas para faturamento em aberto; e não tiveram ainda folha de sala concluída e devolução pela farmácia concluída.
  + 1 - Procedimentos com status cancelado são aqueles que tiveram o agendamento cancelado, na função agenda cirúrgica.
* Data
* Sala de agendamento;
* Nome do paciente;
* Nome do procedimento principal;
* Nome do procedimento secundário: caso mais de um, separados por ;
* Kit associado (se houver): caso mais de um, separados por ;
* Tempo previsto: cadastro do procedimento

Filtros:

* Data: por padrão, deverá ser visualizada a data atual. Os demais filtros deverão ser exibidos em sua totalidade.
* Unidade de atendimento: por padrão a tele é aberta sem nenhuma unidade selecionada, para recuperar as informações é necessário selecionar uma unidade ou a opção todos.
* Sala de agendamento, com botão ... para busca das salas disponíveis, exibição de grid com as salas.
* Nome do paciente.
* Status do procedimento: programado, em andamento, liberado, concluído e cancelado.

Caso o usuário sinta necessidade há um temporizador para que a tela seja atualizada a cada intervalo escolhido.

Duas telas podem ser acessadas através dos botões apresentados abaixo:

Esses botões são habilitados de acordo com os itens que estão selecionados na tela:

* **Folha de sala:** Habilitado quando somente um registro estiver selecionado e o status desse seja **Em andamento** ou **Recusada**;
* **Registro de informação cirúrgica:** Habilitado quando somente um registro estiver selecionado, essa opção está disponível independente de status;

A função **Folha de sala** só estará disponível caso o parâmetro **Unidade utiliza fluxo de folha de sala no centro cirúrgico**, estiver habilitado na unidade de atendimento do agendamento selecionado.

Quando a agenda está com o status de fechada o usuário não conseguirá abrir a tela folha de sala

### **01.1 Controle de Acesso a etapa da Gestão de Cirurgia**

Para garantir a integridade do fluxo o RM fornece um controle de acesso à etapa do processo de gestão de cirurgias onde 2 usuários não podem acessar a mesma agenda por etapa ao mesmo instante. O controle é similar ao conceito de sessão e é aplicado nos processos de Folha de sala, Dispensação e Registro de devolução.  
A sessão tem um timeout de 1h e a cada 30m o RM atualiza a validade da sessão, caso o usuário fique sem interagir com o tela e não atualize a validade da sessão outro usuário poderá acessar o fluxo normalmente.  
A mensagem é exibida ao tentar abrir a tela e outro usuário com sessão ativa esteja acessando ou caso o usuário fique sem interação no período estabelecido.

### **01.2 Anexo log painel de cirurgia**

Foi criado um anexo onde o usuário poderá visualzar todos os processos que foram realizados na cirurgia.

Folha de sala

## **02. FOLHA DE SALA**

Para acessar folha de sala, basta clicar no botão **Folha de sala**. O botão estará habilitado quando o status for **Em andamento**.

A seguinte tela é apresentada:

Todos os itens confirmados na tela "Dispensar" da farmácia serão mostrados no grid.

### **02.1 Botão Limpar**

Para facilitar a a checagem dos itens foram desenvolvidos alguns recursos entre eles o botão limpar que limpa na tela todos os controles de identificação do item para a confirmação do mesmo.

Ao acioná-lo os campos ao lado esquerdo da tela do grupos de informações **Checar o uso dos itens** voltam ao estado inicial.

### **02.3 Botão Usar item**

Este botão consiste em explicitar que o item informado foi realmente utilizado na cirurgia. 

As validações serão consistidas no momento que o botão for clicado e caso não exista nenhuma inconformidade, o item ficará marcado com check na listagem da direita.

### **02.4 Botões OK e Salvar**

Os botões OK e Salvar permitem que o usuário possa gravar o status atual da Folha de Sala persistindo no banco de dados os itens já confirmados para que não sejam perdidas as alterações, nesse momento a quantidade confirmada e o status do item é alterado para Usado ficando um check de cor verde no grid. A diferença entre os botões é que o botão OK ao finalizar a gravação fecha a tela que poderá ser aberta novamente em outro momento.

### **02.5 Botão Cancelar**

O botão cancelar desfaz todas as alterações realizadas desde a última gravação ou abertura da tela, caso não tenha ocorrido nenhuma gravação.

### **02.6 Retirar da folha de sala**

O botão retirar da folha de sala é responsável por retornar os itens que estão marcados como usado para não usado.

Pra retirar um item é necessário primeiramente marca o item que deseja retirar, após a seleção clicar no botão retirar da folha de sala, o item retornará para o status de não usado.

### **02.7 Botão Fechar folha de sala**

O botão fechar folha de sala é responsável por concluir todo os processos que foram realizados na folha de sala, as alteração realizadas no grid serão salvas e a cirurgia terá o seu status alterado para liberado. Após fechar folha de sala, a tela será fechar e o usuário não poderá voltar a utilizar até que no processo de devolução a folha de sala seja reaberta.

No momento de fechar a folha de sala será validado se foi confirmado algum item novo, caso tenha não será possível fechar a folha de sala, a tela será recarregada e o grid atualizado com o(s) item(s) que foi inserido durante o processo. Quando a agenda está com o status de fechada o usuário não conseguirá fechar a folha de sala.Registro de informação cirúrgica

## **03. REGISTRO DE INFORMAÇÃO CIRÚRGICA**

Através do botão **Registro de informações cirúrugica** é possível abrir o respectivo registro relacionado a agenda selecionada, para que esta opção esteja disponível, é necessário selecionar apenas uma linha da listagem.

Caso não exista nenhum registro de informação cirúrgica relacionado a agenda, será aberto o formulário de inclusão com o dados principais já preenchidos.
