---
content_hash: 6a21946fa0e32067a377961a51ff3ae501d7e4fed049a7c8203ef7a9db42f3ac
fetched_at: '2026-06-29T00:09:16.787361+00:00'
page_id: '421385558'
product: rm
source: tdn-rm
title: Relatório de Planilha de Tarefas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385558
version: 1
---

**Relatório de Planilha de Tarefas**

---

Relatório de planilha de tarefas utilizando o Gerador.NET.  
   
O Relatório de planilha de tarefas exibe dados das estruturas de tarefas do projeto corrente. Haverá oito tipos de templates de relatórios, entre eles:  
   
• Estrutura de tarefas; • Estrutura de tarefas(totalizado por etapa); • Estrutura de tarefas (por extenso); • Estrutura de tarefas (cod do serviço sem cod. obra); • Planilha de preços 7 nivel (bdi sobre projeto); • Planilha de preços 7 nivel (bdi sobre serviço);  
Os relatórios poderão ser acessado de duas maneiras no sistema. No RM Reports dentro do TOTVS Construção e Projetos na área Sistema e no menu Relatórios -> Planilha de tarefas.  
   
Restrições  
   
• Este relatório será padrão no sistema e o usuário não poderá editar ou excluir o mesmo. • Em contra partida o usuário poderá realizar uma cópia ou exportar o relatório para um novo e editando-o assim para as suas necessidades. • Este relatório não poderá ser acessível para projetos globais.  
   
Filtros  
   
• Escolha do relatório entre Totvs Reports(novo) e Gerador de Relatório(antigo) • Relatório: informação do código do relatório a ser impresso. Nessa pesquisa aparecerão somente relatórios do tipo "Planilha de tarefas" • Imprimir direto para impressora (flag) • Recalcular a Curva ABC • Cenário: Informação do cenário; • Planilha: Informação do tipo de planilha; • Tarefa inicial e tarefa final: faixa de tarefas a serem impressas no relatório. • Disciplinas  
   
**Observações:**   
Nos filtros dos relatórios, haverá o seguinte filtro padrão "Código da tarefa >= 0 E Código da tarefa <= 999999".  Esse filtro não deve ser retirado e alterado pois a tela de geração de relatórios do Solum utiliza esse filtro para realizar a substituição dos dados informados pelo usuário na tela de filtro personalizada.  
   
**Estrutura de tarefas (relatórios de planilha)**  
Serão listados os dados das tarefas (código da tarefa, descrição da tarefa, unidade de medida, quantidade, valor unitário, valor total. Essas informações são buscadas da tabela MTarefa, filtrado pelo cenário   
informado, tipo de planilha, coligada e projeto corrente.  
   
**Estrutura de tarefas (totalizado por etapa e por obra)**  
Serão listados os dados das tarefas (código da tarefa, descrição da tarefa, unidade de medida, quantidade, valor unitário, valor total. Essas informações serão totalizadas por etapa / obra. Essas informações são buscadas da tabela MTarefa, filtrado pelo cenário informado, tipo de planilha, coligada e projeto corrente.  
   
**Estrutura de tarefas (por extenso)**  
Serão listados os dados das tarefas (código da tarefa, descrição da tarefa, unidade de medida, quantidade, valor unitário, valor total. Essas informações são buscadas da tabela MTarefa, filtrado pelo cenário informado, tipo de planilha, coligada e projeto corrente. O valor total da tarefa será informado por extenso.  
   
**Estrutura de tarefas (cód. serviço sem cód. obra)**  
Serão listados os dados das tarefas (código da tarefa, descrição da tarefa, unidade de medida, quantidade, valor unitário, valor total. Essas informações são buscadas da tabela MTarefa, filtrado pelo cenário informado, tipo de planilha, coligada e projeto corrente. O código do serviço será impresso sem o código da obra na máscara do código.  
   
**Planilha de preços 7 nível (BDI sobre projeto)**  
Serão listados os dados das tarefas (código da tarefa, descrição da tarefa, unidade de medida, quantidade, valor unitário, valor total. Essas informações são buscadas da tabela MTarefa, filtrado pelo cenário informado, tipo de planilha, coligada e projeto corrente. Com aplicação do BDI sobre o projeto.  
   
**Planilha de preços 7 nível (BDI sobre os serviços)**  
Serão listados os dados das tarefas (código da tarefa, descrição da tarefa, unidade de medida, quantidade, valor unitário, valor total. Essas informações são buscadas da tabela MTarefa, filtrado pelo cenário informado, tipo de planilha, coligada e projeto corrente. Com aplicação do BDI sobre os serviços.
