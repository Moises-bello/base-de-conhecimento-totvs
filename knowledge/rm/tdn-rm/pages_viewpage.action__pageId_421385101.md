---
content_hash: c4e276c2a7f3136d274b0a42b06a7a0a5a094faeb58271bb0d288b66b141f019
fetched_at: '2026-06-29T00:09:13.754481+00:00'
page_id: '421385101'
product: rm
source: tdn-rm
title: Apontamentos 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385101
version: 5
---

---

Após os recursos estarem alocados nas tarefas, e as respectivas equipes criadas, os usuários (pessoas membros de equipe), poderão iniciar os apontamentos nas tarefas.

O apontamento poderá ser realizado de três formas distintas: através da Visão de Apontamentos em Tarefas , através da Execução da própria tarefa ou pelo processo de apontamentos por período.Em ambas as possibilidades, deverão ser considerados alguns parâmetros e regras de consistência do apontamento.

Cada apontamento terá uma classificação em relação à sua origem, podendo ser "Avulso" que são originários do cadastro a partir da visão de apontamentos ou do processo de inclusão por período ou "Padrão" que são incluídos através da execução de tarefas.

**Parâmetros de Apontamentos**

Em  é possível parametrizar os apontamentos dos recursos, a fim de limitar a inclusão, ou alteração desses apontamentos.

Na visão de apontamentos (Menu Controle | Timesheet | Apontamento em Tarefas) são exibidas as tarefas onde os membros (pessoas) estão alocados e seus respectivos apontamentos. E nesta visão, o usuário pode incluir, editar e excluir os apontamentos. A tela de apontamentos é exclusiva para lançamentos de apontamentos de usuários alocados em tarefas de timesheet, tanto para responsáveis por equipes que gerenciam os membros, quanto para os próprios membros. Usuários responsáveis por equipes podem lançar apontamentos para outros usuários que são membro da equipe.

As colunas padrões da visão do anexo (a exibição das mesmas pode ser editada pelo usuário), são as seguintes:

* Código do Projeto;
* Descrição do Projeto;
* Código da Etapa;
* Nome da Etapa;
* Código da Tarefa;
* Nome da Tarefa;
* Membro do apontamento;
* Data do Apontamento (o valor padrão será a data atual);
* Hora Inicial do Apontamento;
* Hora Final do Apontamento;
* Tempo (Hora Final – Hora Inicial);
* Quantidade de Horas Apontadas;
* Desconto em horas do apontamento (considerando o parâmetro);
* Percentual de Completude;
* Percentual Concluído da Tarefa;
* Origem do apontamento (Padrão (execução da tarefa) ou Avulso (inclusão manual));
* Tipo do apontamento (Produtivo ou Improdutivo);
* Status do apontamento (Concluído ou Execução);
* Motivo de Improdutividade (No caso de apontamentos Improdutivos);
* Descrição da Equipe.

A tela de edição de apontamentos deverá considerar as seguintes regras:

* O lookup de projetos só deverá listar projetos onde o usuário está alocado ou onde é responsável por equipe;
* O lookup de membros só estará habilitado se o usuário do sistema for um responsável por equipe. Os membros exibidos serão os pertencentes às equipes do usuário responsável;
* O lookup de tarefas só exibirá as tarefas do tipo Timesheet;
* Marcando o checkbox "Tarefas alocadas para o membro", só serão exibidas as tarefas destinadas ao membro selecionado;
* A data do apontamento não poderá ser maior que a data atual;
* As horas inicial e final do apontamento não poderão ser iguais;
* O motivo de improdutividade só estará habilitado se o tipo for "Improdutivo";
* Apenas os motivos de improdutividade do tipo Mão de Obra serão considerados;
* O parâmetro de Intervalo de Desconto será considerado na inclusão/edição do apontamento caso o parâmetro esteja dentro do intervalo de apontamento e se a "Quantidade mínima de horas" for atendida;
* O parâmetro "Quantidade de dias" será considerado na inclusão/edição do apontamento se o parâmetro "Permitir apontamentos retroativos" estiver marcado;
* No caso de a data do apontamento ser diferente da data de parada de execução da tarefa, uma mensagem de alerta será exibida informando ao usuário se deseja parar a execução. Caso confirme, a tela de edição de apontamentos será exibida com a diferença que o campo "Data Final" estará visível, para que possa ser informado em qual data o apontamento deve ser encerrado, e se esta data for maior que a data do apontamento, outros apontamentos serão inseridos considerando as horas iniciais e finais, como no exemplo:
  + Apontamento:
    - Início: 01/01/2014 15:00
    - Fim: 02/01/2014 06:00
    - Dois apontamentos inseridos:
      * Apontamento 1: 01/01/2014 15:00 – 23:59
      * Apontamento 2: 02/01/2014 00:00 – 06:00
* Ao salvar o apontamento, é verificado se o percentual informado é menor que o percentual lançado com a data mais recente. Uma mensagem de confirmação é apresentada perguntando ao usuário se deseja continuar o lançamento do apontamento;
* Ao salvar o apontamento, é verificado se o percentual informado é igual ao último percentual lançado com a data mais recente. Uma mensagem de confirmação é apresentada questionando se o percentual será o mesmo;
* Sempre que um apontamento for salvo, estando todas as consistências validadas, uma apropriação será inserida:
  + A apropriação terá a tarefa, o insumo do membro, a pessoa do apontamento, que pode ser um funcionário ou um terceiro, a quantidade de horas apontadas, o preço será preenchido de acordo com a parametrização definida nos parâmetros do projeto no menu principal do Totvs obras e Projetos | Projetos | Construção e Projetos | Projetos (F6) | Apropriação | Apropriação de Serviços e Insumos |
  + **Valor Mão de Obra do sistema de Folha de Pagamento (RM Labore) :** Marque essa opção caso queira que o preço unitário da apropriação seja lançado de acordo com o valor da hora do funcionário do RM Labore apropriado no Totvs Obras e Projetos. Ao buscar o valor no RM Labore será feita uma outra validação. Se o parâmetro "Fator lei social " estiver marcado e na tela do grupo de custo a lei social correspondente estiver marcada, será multiplicado o fator ao valor da mão de obra que foi informada pelo Labore.
  + **Valor Insumo Totvs Obras e Projetos:** Marque essa opção caso queira que o preço unitário da apropriação seja lançado de acordo com o valor do insumo com leis do Totvs Obras e Projetos, do insumo associado ao membro, em caso de vigência considerará a data do apontamento.
  + Se o apontamento estiver sendo alterado, a apropriação relacionada será excluída e uma nova será inserida;
  + Não é possível alterar informações de apropriações que tem vínculo com apontamentos, pois essa alteração deverá ser feita no próprio apontamento, para impedir inconsistências nas informações;
  + Não é possível excluir apropriações que tem vínculo com apontamentos.
* Os apontamentos só serão incluídos se não existir apontamentos do usuário para o período informado;
* Funcionário demitido não poderá ter apontamentos com data superior a data de demissão do mesmo.;
* O percentual de completude não pode ser maior que 100%;
* Após salvar o apontamento, o "Percentual Concluído" da tarefa no PERT deve ser alterado considerando a quantidade de horas alocadas para o recurso, como demonstrado no exemplo:

Ex.:        
Tarefa: 001.01.01 – Configurar Ambiente Integração – Total (Horas): 100 horas

JOSÉ DA SILVA:  60 horas alocadas

JOÃO DE SOUZA:  40 horas alocadas

Apontamento JOSÉ DA SILVA: 25% de completude

Apontamento JOÃO DE SOUZA: 30% de completude

Percentual Concluído da Tarefa:

JOSÉ DA SILVA: 25% \* 60 = 15 horas

JOÃO DE SOUZA: 30% \* 40 = 12 horas

Total: 27 horas concluídas => 27% da Tarefa concluída

**Importante:**  
A disponibilidade e impacto do percentual de completude da tela de edição do apontamento nas tarefas deverá seguir as seguintes regras:

* Parâmetro Utilizar Alocação de Membros de Equipes nas Tarefas de Timesheet:
  + Marcado: Campo estará disponível somente para tarefas onde o usuário do apontamento estiver alocado e impactará na tarefa;
  + Desmarcado: Campo estará disponível sempre pra qualquer tarefa esteja o usuário associado ou não, e o valor impactará no avanço da tarefa.

Ao excluir um apontamento, o percentual concluído da tarefa não deverá ser alterado pois o impacto é apenas em relação ao andamento da tarefa no que diz respeito ao percentual de completude dos apontamentos, e quando um apontamento é excluído, não deve representar o retrocesso da tarefa.

Apontamentos com 100% de completude jamais poderão ser excluídos.

Tais apontamentos poderão ter seu percentual alterado, apenas pelo responsável da equipe e não pelo seus respectivos membros, porém os demais apontamentos relacionados com a mesma tarefa, não poderá ser editados, uma mensagem na tela de edição deverá ser exibida: "O apontamento não poderá ser editado pois a atuação na tarefa atingiu 100% de completude.".

Se o parâmetro de "Utilizar Alocação de Membros de Equipes nas Tarefas de Timesheet" não estiver marcado, somente será possível apontar 100% se não existir mais nenhum usuário executando a mesma tarefa.

Apontamentos retroativos não terão interferência sobre o percentual concluído da tarefa, isto é, o percentual considerado será o da data mais recente. No exemplo abaixo, os apontamentos A3 e A6 que deverão ser considerados, mesmo que os apontamentos A2 e A5 tenham sido lançados posteriormente.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tarefa: 001.01.01 - Configurar Ambiente Integração** |  |  |  |  |
| **Apontamentos** |  |  |  |  |
| **Recurso** | **Data** | **Data de Inclusão** | **Percentual** | **#** |
| JOSÉ DA SILVA | 01/01/2014 | 01/01/2014 | 10% | **A1** |
|  | 02/01/2014 | 04/01/2014 | 20% | **A2** |
|  | 03/01/2014 | 03/01/2014 | 25% | **A3** |
| JOÃO DE SOUZA | 01/01/2014 | 01/01/2014 | 15% | **A4** |
|  | 02/01/2014 | 04/01/2014 | 25% | **A5** |
|  | 03/01/2014 | 03/01/2014 | 30% | **A6** |

**Execução de Tarefas**

Esse processo permite 'Executar/Parar' tarefas do tipo Timesheet. A execução só será permitida para apenas uma tarefa por vez, e no caso de já existir alguma em execução, somente será possível pará-la para poder iniciar uma outra.

Para parar a tarefa não será necessário selecioná-la pois existe apenas uma em execução.

Ao parar a tarefa, a tela de apontamento será exibida para que o percentual de completude seja informado.   
   
A execução das tarefas pode ser realizada de duas maneiras, através de um processo na planilha de atividades ou através do ícone do sistema que encontra-se na barra de ferramentas (tray icon). Tarefas em execução não poderão ser alteradas.

**Importante:**

No caso de o projeto estar parametrizado para não utilizar a alocação de membro nas atividades, o mesmo deverá ser calculado para que as tarefas estejam disponíveis para execução através do menu de notificação, pois é o cálculo do projeto que organiza as informações da relação Tarefa-Insumo.

Agora também é possível fazer apontamento em tarefas online via Fluig. Todas as informações de , [Alocação de Recurso](http://tdn.totvs.com/pages/viewpage.action?pageId=421385140) são feitas normalmente no RM e apontamento e execução de tarefas feitas no fluig, permanecendo as mesmas regras de negocio. A única função ainda não disponível para a versão online são os apontamentos por período

Informações Complementares

---

   
  
   
[Alocação de Recurso](http://tdn.totvs.com/pages/viewpage.action?pageId=421385140)  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
 Como Fazer

---
