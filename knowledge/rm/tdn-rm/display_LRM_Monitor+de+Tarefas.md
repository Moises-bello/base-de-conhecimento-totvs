---
content_hash: 3773a9a7a0139dcb14469c08203b428bd8540c7676b0d04e275a616e0795cf35
fetched_at: '2026-06-29T00:09:14.668501+00:00'
page_id: '421385218'
product: rm
source: tdn-rm
title: Monitor de Tarefas
type: documentation
url: https://tdn.totvs.com/display/LRM/Monitor+de+Tarefas
version: 4
---

---

Nessa visão será possível utilizar o processo de execução de tarefas, basta apenas selecionar a tarefa desejada. Algumas regras dessa visão devem ser consideradas:

* Usuários responsáveis por equipes visualizarão as tarefas dos membros de suas equipes, porém só poderão executar tarefas que são de sua responsabilidade;
* Usuários membros de equipes somente visualizarão as suas respectivas tarefas;
* A execução de tarefas deverá considerar as regras estabelecidas no item Execução de Tarefas;
* Deverá ser criado um item de segurança para essa nova visão;
* As colunas exibidas são:
  + Código do Projeto
  + Descrição do Projeto
  + Membro(Nome do Membro de Equipe)
  + Etapa(Etapa pai da Tarefa)
  + Código da Tarefa
  + Nome da tarefa
  + Unidade (Unidade da Tarefa)
  + Quantidade Alocada (Quantidade necessária para realizar a completude da tarefa)
  + Quantidade Apontada (Quantidade que já foi realizada até o momento do apontamento)
  + Data de Inicio (Data de Inicio da Tarefa)
  + Data de Fim (Data de Fim da Tarefa)
  + % Completude (Percentual de Completude da Tarefa)

Deverá existir, nessa visão, um coluna com diferentes ícones que indiquem o status de execução da tarefa, considerando as possibilidades:

* (**Play/Stop**): Tarefa concluída com 100% de completude;
* (**Triângulo da cor verde**): Tarefa em execução;
* (**Quadrado Azul**) : Tarefa parada.

Deverá, também, existir nessa visão, outra coluna com diferentes ícones que indiquem o status de andamento da tarefa, considerando as possibilidades:

• Tarefa não iniciada: Percentual de completude igual a 0 (zero) e data de inicio da tarefa maior que a data atual;

V : Tarefa concluída: Tarefa com 100% de completude na quantidade alocada para o membro;

• : Tarefa dentro do prazo: Quantidade Agregada na tarefa deve estar entre 10% do previsto e 10% acoma do previsto;

• : Tarefa adiantada: Quantidade Agregada na tarefa deve estar acima de 10% do previsto;

• : Tarefa atrasada: Quantidade Agregada na tarefa deve estar abaixo de 10% do previsto.

 Informações Complementares

---

   
[Alocação de Recurso](http://tdn.totvs.com/pages/viewpage.action?pageId=421385140)  
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
  Como Fazer

---
