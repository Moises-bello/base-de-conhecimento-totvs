---
content_hash: 20e31e21c2f3b1e97ba2b1619941b081624e4747bff6a15f712686da7b1b604c
fetched_at: '2026-06-29T00:09:14.240761+00:00'
page_id: '421385164'
product: rm
source: tdn-rm
title: Atividade Predecessora
type: documentation
url: https://tdn.totvs.com/display/LRM/Atividade+Predecessora
version: 2
---

A tela permite visualizar todas as ligações de precedência da atividade selecionada.

A definição é realizada conforme as ligações:

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

Caso a data real for igual a data programa o processo "Programar" não alterará a data programada para aquela tarefa.

Sábados, Domingos e Feriados, definidos nos parâmetros do projeto. Caso os parâmetros ‘Trabalho   
aos Sábados’, ‘Trabalho aos Domingos’ e ‘Trabalho aos Feriados’ estejam desmarcados, no momento   
do lançamento de datas é verificado se as datas são finais de semana ou feriados e é impedido o   
lançamento.
