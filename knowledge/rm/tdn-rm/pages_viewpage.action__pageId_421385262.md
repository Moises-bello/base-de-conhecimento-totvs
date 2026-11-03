---
content_hash: 573998d9574a7c9d1a8bbea1e74d0015c606893845ce6415f726e078c18050c7
fetched_at: '2026-06-29T00:09:14.811357+00:00'
page_id: '421385262'
product: rm
source: tdn-rm
title: Timesheet Executar/Parar Apontamento de Atividade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385262
version: 4
---

---

Esse processo permite 'Executar/Parar' tarefas do tipo Timesheet. A execução só será permitida para apenas uma tarefa por vez, e no caso de já existir alguma em execução, somente será possível pará-la para poder iniciar uma outra.

Para parar a tarefa não será necessário selecioná-la pois existe apenas uma em execução.

Ao parar a tarefa, a tela de apontamento será exibida para que o percentual de completude seja informado.

**EXECUÇÃO PADRÃO VIA BARRA DE FERRAMENTAS**

Uma das opções para execução de tarefas está no menu de notificação do sistema. Nele serão exibidos projetos e suas respectivas tarefas onde o usuário corrente estará alocado. O menu de notificação pode ser acessado através do ícone presente na barra de ferramentas (canto direito inferior da tela), clicando com o botão direito.

**Observação:**  
 Deverão ser exibidas apenas as tarefas onde o percentual concluído em relação às horas alocadas para o recurso é menor que 100%.

**Exemplo:** Recurso 1 – JOSÉ DA SILVA

Projeto R\_TOP003: Tarefa 001.01.01 – Ajustar backup (% Concluído = 40%) Tarefa 001.01.12 – Importação de arquivo texto (% Concluído = 50%)

Projeto R\_TOP004: Tarefa 001.02.05 – Elaborar capacitação (% Concluído = 10%) Tarefa 001.03.01 – Melhorar performance cálculo (% Concluído = 25%)

Considerando o exemplo acima, o "Recurso 1" poderá executar qualquer tarefa que desejar, antes de iniciar os trabalhos, sendo que será possível executar apenas uma tarefa por vez. Ao iniciar a execução, será incluído um novo apontamento com data do apontamento e hora de início, onde o mesmo só será efetivamente confirmado quando o usuário parar a execução da tarefa.

A partir do momento em que uma tarefa se encontrar em execução, será possível pará-la e as demais tarefas não serão disponibilizadas para visualização enquanto isso não ocorrer. Após parar a tarefa, a tela de edição de apontamentos será exibida para que o usuário confirme a inclusão do mesmo. Apenas o campo percentual de completude estará disponível para ser informado. As regras de salvamento serão as mesmas destacadas para a inclusão de apontamentos.  
    
 **Importante:**

A exibição das tarefas no ícone do RM na barra de ferramentas, segue as seguintes regas:

* Parâmetro Utilizar Alocação de Membros de Equipes nas Tarefas de Timesheet:
  + Marcado: Exibe somente as tarefas alocadas para o usuário do sistema;
  + Desmarcado: Exibe as tarefa onde o insumo relacionado ao membro, que representa o usuário do sistema, está associado.

**EXECUÇÃO PADRÃO VIA PROCESSO**

Na planilha de atividades e no monitor de tarefas, há o processo "Timesheet - Executar/Parar Atividade" da tarefa. A execução é permitida para apenas uma tarefa por vez, e no caso de já existir alguma em execução, somente será possível pará-la para poder iniciar uma outra. Para parar a tarefa, não será necessário selecioná-la, pois, existe apenas uma em execução. Ao parar a tarefa, a tela de apontamento será exibida assim como descrito no item Execução Padrão: Barra de Ferramentas. Algumas regras para a execução do processo deverão ser seguidas, conforme quadro abaixo:

|  |  |  |
| --- | --- | --- |
| **Tarefa marcada no grid** | **Existe tarefa em execução?** | **Retorno do sistema** |
| Uma | Não | Executa a tarefa marcada e exibe uma tela de progresso ao usuário. Este progresso fecha automaticamente. |
| Uma | Sim | Mensagem é exibida solicitando a confirmação de parada da tarefa que se econtra em execução. |
| Nenhuma | Não | Gera alerta avisando que é necessário marcar uma tarefa para que ela possa ser executada. |
| Nenhuma | Sim | Executa processo para parar tarefa em execução. |
| Mais de uma | Não | Gera alerta avisando que é permitido executar somente uma tarefa por vez. |
| Mais de uma | Sim | Mensagem é exibida solicitando a confirmação de parada da tarefa que se econtra em execução. |

   
   Informações Complementares

---

   
   
    
[Alocação de Recurso](http://tdn.totvs.com/pages/viewpage.action?pageId=421385140)  
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
  Como Fazer

---
