---
content_hash: 0345e699744cc9d7734775480ce8c818ff471202a0cbcee8c237b6be5192750b
fetched_at: '2026-06-29T00:09:16.360136+00:00'
page_id: '421385519'
product: rm
source: tdn-rm
title: Atividade Sucessora
type: documentation
url: https://tdn.totvs.com/display/LRM/Atividade+Sucessora
version: 2
---

Nesta tela é possível visualizar as tarefas que são sucessoras da tarefa selecionada.

As tarefas sucessoras possuem quatro tipos de ligações:  
 -    Fim – Início: A tarefa sucessora inicia quando termina sua tarefa predecessora.  
 -    Cálculo: Data Fim da sucessora = Data início da predecessora + defasagem + 1  
 -    Fim – Fim: A tarefa sucessora termina quando termina sua predecessora.  
 -    Cálculo: Data Fim da sucessora = Data Fim da predecessora + defasagem  
 -    Início – Início: A tarefa sucessora inicia quando começa sua predecessora.  
 -    Cálculo: Data Início da sucessora = Data Início da predecessora + defasagem  
 -    Inicio – Fim: A tarefa sucessora termina quando começa sua predecessora.   
 -    Cálculo: Data Início da sucessora = Data final da predecessora + defasagem - 1

Ao incluir uma tarefa sucessora é verificado se a atividade principal está com o seu período preenchido,   
caso esteja o lançamento das datas da atividade sucessora será feito automaticamente.

Defasagem: diferença em dias, entre o início da sucessora e o término da atividade corrente (não é uma   
folga).

Sábados, Domingos e Feriados, definidos nos parâmetros do projeto. Caso os parâmetros ‘Trabalho   
aos Sábados’, ‘Trabalho aos Domingos’ e ‘Trabalho aos Feriados’ estejam desmarcados, no momento   
do lançamento de datas é verificado se as datas são finais de semana ou feriados e é impedido o   
lançamento.
