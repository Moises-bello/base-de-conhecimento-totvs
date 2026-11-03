---
content_hash: e5098db58322175b3b629d896b91a7ad5399aab15597a9a1ffc27ff29a954a26
fetched_at: '2026-06-29T00:06:10.238830+00:00'
page_id: '203759265'
product: rm
source: tdn-rm
title: ER_PCREQ-7445_HTML_Framework_Timesheet_Apontamentos_em_Tarefas
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-7445_HTML_Framework_Timesheet_Apontamentos_em_Tarefas
version: 23
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Timesheet |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP008 | **IRM1** | PCREQ-7444 |
| **Requisito1** | PCREQ-7445 | **Subtarefa1** | PDR\_CP\_TOP008-14 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:  TOTVS HTML Framework - http://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&title=HTML+Framework&linkCreation=true&fromPageId=196053421  Fluig - <http://tdn.totvs.com/display/public/fluig/Sobre+o+Fluig>  Projetos - <http://wikihelp.totvs.com.br:1210/WikiHelp/PRJ/PRJ.Projetos.aspx>  Timesheet - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Timesheet.aspx> | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

 Migração da funcionalidade de Apontamentos de Tarefas de Timesheet para o ambiente Fluig utilizando o TOTVS HTML Framework. 

## Definição da Regra de Negócio

### **TOTVS HTML *Framework***

O TOTVS | HTML *Framework* foi concebido para tratar apenas a camada de interface das aplicações, confiando que os produtos por trás da interface irão conceder a infraestrutura e a implementação mínima dos serviços para utilização do*framework*. 

Ela tem como objetivo:  

* + Fornecer uma Infraestrutura de componentes visuais e de serviços (de interface) HTML5;

* + Prover uma IDE de desenvolvimento HTML5, baseada no TDS ([TOTVS Developer Studio](http://ds.totvs.com/));

* + Disponibilizar um Template de CRUD responsivo com respectivo acelerador no TDS, baseado em Serviços providos pelos produtos;

* + Estruturar um ambiente de desenvolvimento compatível com o Fluig e que possa ser utilizados por todos os produtos TOTVS.

**Apontamentos em Tarefas de Timesheet**

Após a criação das equipes e a devida alocação dos recursos (membros) realizada, os usuários (pessoas membros de equipe), poderão iniciar os apontamentos nas tarefas. O apontamento poderá ser realizado de três formas distintas, através da Visão de Apontamentos em Tarefas através da Execução da própria tarefa ou pelo processo de apontamentos por período Em ambas as possibilidades, deverão ser considerados alguns parâmetros e regras de consistência do apontamento. Cada apontamento terá uma classificação em relação à sua origem, podendo ser “Avulso” que são originários do cadastro a partir da visão de apontamentos ou do processo de inclusão por período, ou podendo ser “Padrão” que são incluídos através da execução de tarefas, que é considerado a forma mais correta.

* **Parâmetros de Apontamento:**
  + Intervalo de Desconto (Horas): Intervalo padrão para que no momento da inclusão ou alteração de um apontamento possa ser considerado. Este parâmetro somente será considerado se o intervalo do apontamento estiver no período de desconto informado. O parâmetro “Quantidade mínima de horas” informa qual a quantidade mínima de horas do apontamento para que o intervalo seja considerado.
    - Ex.: Intervalo de Desconto: 12:30 – 13:30  
      Apontamento: 09:00 – 18:00 => 9 horas  
      Desconto: 01:00  
      Apontamento Real: 8 horas

* + Quantidade de dias: Será considerado se a opção “Permitir apontamentos retroativos” estiver marcada. A data limite anterior permitida será a data atual menos o valor do parâmetro.
    - Ex.: Data do apontamento (data atual): 29/11/2013  
      Quantidade de dias anteriores: 7  
      Data limite permitida para o apontamento: 22/11/2013

**Execução de Tarefas - Start/Stop**

Através da execução de tarefas, os apontamentos também poderão ser lançados, sendo que nesse processo, as alterações não serão possíveis. No TOP a execução de tarefas Start/Stop ocorre através do tray icon do sistema , onde são exibidas as tarefas alocadas para o usuário logado no sistema.

* + A exibição das tarefas no tray icon deverá seguir as seguintes regas:
    - Parâmetro Utilizar Alocação de Membros de Equipes nas Tarefas de Timesheet:
      * Marcado: Exibe somente as tarefas alocadas para o usuário do sistema;
      * Desmarcado: Exibe as tarefa onde o insumo relacionado ao membro, que representa o usuário do sistema, está associado.

**Migração para TOTVS HTML Framework**

**Apontamentos em Tarefas**

Para a funcionalidade de Apontamentos em Tarefas de Timesheet do TOTVS Obras e Projetos serão desenvolvidas telas Web utilizando o TOTVS HTML Framework.

Uma vez que as telas Web forem desenvolvidas, estas serão inserida na plataforma Fluig para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.

Serão desenvolvidas duas telas da seguinte forma:

* + Tela com a listagem dos apontamentos salvos na base de dados com opções para Adicionar, editar, visualizar e excluir um registro;
  + Tela com os detalhes de um registro;
  + Tela com um formulário para Adicionar ou Editar um registro.

Na tela de listagem de Apontamentos serão mostradas as seguintes informações (Protótipo 01):

* + Projeto;
  + Tarefa;
  + Membro do apontamento;
  + Data do Apontamento;
  + Hora Inicial;
  + Hora Final;
  + Tempo (Hora Final – Hora Inicial);
  + Percentual de Completude;
  + Origem do apontamento (Padrão (execução da tarefa) ou Avulso (inclusão manual));
  + Status do apontamento (Concluído ou Execução);
  + Equipe.

Ainda na listagem de Apontamentos ao clicar no link "Exibir detalhes...", serão exibidas as outras informações referente ao registro:

* + Etapa;
  + Quantidade de Horas Apontadas;
  + Desconto em horas do apontamento (considerando o parâmetro);
  + Percentual Concluído da Tarefa;
  + Tipo do apontamento (Produtivo ou Improdutivo);
  + Motivo de Improdutividade (No caso de apontamentos Improdutivos);
  + Observação.

A tela de Adicionar ou Editar um registro para o Apontamento irá conter as mesmas informações da listagem (Protótipo 02).

Algumas definição serão consideradas:

* + Deverá ser permitido a inclusão, edição e exclusão de apontamentos;
  + Essa tela deve ser exclusiva para lançamentos de apontamentos de usuários alocados em tarefas de timesheet, tanto para responsáveis por equipes que gerenciam os membros quanto para os próprios membros;
  + Usuários responsáveis por equipes poderão lançar apontamentos para outros usuários que são membro da equipe;

Para a tela de edição/inclusão de apontamentos (Protótipo 03) algumas regras serão consideradas:

* + Permitir a inclusão e edição de apontamentos;
  + O lookup de projetos só deverá listar projetos onde o usuário está alocado ou onde é responsável por equipe;
  + O lookup de membros só estará habilitado se o usuário do sistema for um responsável por equipe. Os membros exibidos serão os pertencentes às equipes do usuário responsável;
  + O lookup de tarefas só exibirá as tarefas do tipo Timesheet;
  + A data do apontamento não poderá ser maior que a data atual;
  + As horas inicial e final do apontamento não poderão ser iguais;
  + O motivo de improdutividade só estará habilitado se o tipo for “Improdutivo”;
  + Apenas os motivos de improdutividade do tipo Mão de Obra serão considerados;
  + O parâmetro de Intervalo de Desconto será considerado na inclusão/edição do apontamento caso o parâmetro esteja dentro do intervalo de apontamento e se a “Quantidade mínima de horas” for atendida;
  + O parâmetro “Quantidade de dias” será considerado na inclusão/edição do apontamento se o parâmetro “Permitir apontamentos retroativos” estiver marcado;
  + No caso de a data do apontamento ser diferente da data de parada de execução da tarefa, uma mensagem de alerta será exibida e dois apontamentos serão inseridos considerando as horas iniciais e finais, como no exemplo:
    - Apontamento:   
      Início: 01/01/2014 15:00  
      Fim: 02/01/2014 06:00  
      Dois apontamentos inseridos: Apontamento 1: 01/01/2014 15:00 – 23:59 e Apontamento 2: 02/01/2014 00:00 – 06:00
  + Ao salvar o apontamento será verificado se o percentual informado é menor que o percentual lançado com a data mais recente. Uma mensagem de confirmação deverá ser apresentada questionando se o usuário deseja continuar o lançamento do apontamento;
  + Ao salvar o apontamento deverá ser verificado se o percentual informado é igual ao último percentual lançado com a data mais recente. Uma mensagem de confirmação deverá ser apresentada questionando se o percentual será o mesmo;
  + Sempre que um apontamento for salvo, estando todas as consistências validadas, uma apropriação será inserida:

    - A apropriação terá a tarefa, o insumo do membro, a pessoa do apontamento, que pode ser um funcionário ou um terceiro, a quantidade de horas apontadas, o preço do insumo associado ao membro, em caso de vigência considerará a data do apontamento;
    - Se o apontamento estiver sendo alterado, a apropriação relacionada será excluída e uma nova será inserida;
    - Não deverá ser possível alterar informações de apropriações que tem vínculo com apontamentos, pois essa alteração deverá ser feita no próprio apontamento, para impedir inconsistências nas informações;
    - Não deverá ser possível excluir apropriações que tem vínculo com apontamentos.
  + Os apontamentos só serão incluídos se não existir apontamentos do usuário para o período informado;
  + O percentual de completude não pode ser maior que 100%;
  + Após salvar o apontamento, o “Percentual Concluído” da tarefa no PERT deverá ser alterado considerando a quantidade de horas alocadas para o recurso, como demonstrado no exemplo:

    - Ex.:   
      Tarefa: 001.01.01 – Configurar Ambiente Integração – Total (Horas): 100 horas  
      JOSÉ DA SILVA: 60 horas alocadas  
      JOÃO DE SOUZA: 40 horas alocadas

      Apontamento JOSÉ DA SILVA: 25% de completude  
      Apontamento JOÃO DE SOUZA: 30% de completude  
      Percentual Concluído da Tarefa:

      JOSÉ DA SILVA: 25% \* 60 = 15 horas  
      JOÃO DE SOUZA: 30% \* 40 = 12 horas

      Total: 27 horas concluídas => **27% da Tarefa concluída**

**Importante:**

* + - **O disponibilidade e impacto do percentual de completude da tela de edição do apontamento nas tarefas deverá seguir as seguintes regras:**
    - **Parâmetro Utilizar Alocação de Membros de Equipes nas Tarefas de Timesheet:**
      * **Marcado****: Campo estará disponível somente para tarefas onde o usuário do apontamento estiver alocado e impactará na tarefa;**
      * **Desmarcado****: Campo estará disponível sempre pra qualquer tarefa esteja o usuário associado ou não, e o valor impactará no avanço da tarefa.**
    - **Ao excluir um apontamento, o percentual concluído da tarefa não deverá ser alterado pois o impacto é apenas em relação ao andamento da tarefa no que diz respeito ao percentual de completude dos apontamentos, e quando um apontamento é excluído, não deve representar o retrocesso da tarefa;**
    - **Apontamentos retroativos não terão interferência sobre o percentual concluído da tarefa, isto é, o percentual considerado será o da data mais recente. No exemplo abaixo, os apontamentos A3 e A6 que deverão ser considerados, mesmo que os apontamentos A2 e A5 tenham sido lançados posteriormente.**

                              

**Start/Stop de Tarefas**

Para a funcionalidade de Execução de Tarefas - Start/Stop em HTML Framework, será desenvolvida considerando a mesma regra existente no TOP, possibilitando de forma ágil o início dos apontamentos e suas conclusões ao término do trabalho executado.

Essa implementação deverá permitir a utilização do Start/Stop em um Widget para fácil execução das tarefas.

**Importante:**

* + **Deverão ser exibidas apenas as tarefas onde o percentual concluído em relação às horas alocadas para o recurso é menor que 100%;**
  + **Exemplo de exibição: Protótipo 04**
    - **Recurso 1 – JOSÉ DA SILVA**

      * **Projeto R\_TOP003:**

        + **Tarefa 001.01.01 – Ajustar backup (% Concluído = 40%)**
        + **Tarefa 001.01.12 – Importação de arquivo texto (% Concluído = 50%)**
      * **Projeto R\_TOP004:**

        + **Tarefa 001.02.05 – Elaborar capacitação (% Concluído = 10%)**
        + **Tarefa 001.03.01 – Melhorar performance cálculo (% Concluído = 25%)**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Timesheet | Criação | Planejamento -> Timesheet -> Apontamentos em Tarefas | - |

## Protótipo de Tela

**Protótipo 01**

****Protótipo 02****

**Protótipo 03**

**Protótipo 04**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
