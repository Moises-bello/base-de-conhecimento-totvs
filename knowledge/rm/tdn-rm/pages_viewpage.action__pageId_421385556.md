---
content_hash: 75912af559fea98f3325d2cdee3f36a76482ffdaf38580d96b2e01205c6d2615
fetched_at: '2026-06-29T00:09:16.781546+00:00'
page_id: '421385556'
product: rm
source: tdn-rm
title: Relatório de Composição do Projeto 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385556
version: 2
---

**Relatório de Composição do Projeto** ----   
Relatórios de Composições do Projeto utilizando o Gerador.NET.   
O Relatório de Composições do Projeto exibe todas as composições utilizadas no projeto. Haverá seis tipos de relatórios:  
• Composições de Custo Unitário utilizadas no Projeto; • Composições por Produção utilizadas no Projeto; • Planilha de composição analítica por tarefas considerando BDI diferenciado; • Planilha de composição analítica de preços unitários por produção; • Planilha de composição analítica de custo unitários; • Planilha analítica de CPUs por tarefas com descr. Composição auxiliar.  
Os relatórios poderão ser acessados de duas maneiras no sistema. No RM Reports dentro do TOTVS Construção e Projetos na área Sistema e no menu Relatórios -> Composições no Projeto.  
Restrições  
• Estes relatórios serão padrões no sistema e o usuário não poderá editar ou excluir os mesmos. • Em contra partida o usuário poderá realizar uma cópia ou exportar o relatório para um novo e editando-o assim para as suas necessidades. • O relatório não estará disponível para projetos globais.  
Filtros  
• Escolha do relatório entre Totvs Reports(novo) e Gerador de Relatório(antigo) • Escolha do relatório no campo de relatório • Por cenário e tipo de planilha • Faixa de tarefas (tarefa inicial e tarefa final) • Imprimir composições auxiliares • Flag (Imprimir Composições auxiliares)  
Tabelas Utilizadas  
• MRELRECURSO – Relatório de recursos • GCOLIGADA – Coligadas • MCMP – Composições • MISM – Insumos • MRECCMP – Recursos da Composição • MPRJ – Projetos • GIMAGEM – Imagens  
**Composições de Custo Unitário utilizadas no Projeto:** Ele irá exibir as composições de custo unitário que estão sendo utilizadas no Projeto, utilizadas como próprio recurso da tarefa, ou sendo auxiliar de outra composição (marcar a flag de imprimir composições auxiliares neste caso)  
**Composições por Produção utilizadas no Projeto:** Ele irá exibir as composições por produção que estão sendo utilizadas no Projeto, utilizadas como próprio recurso da tarefa, ou sendo auxiliar de outra composição (marcar a flag de imprimir composições auxiliares neste caso).Os Recursos da Composição será agrupado por Grupo DNIT utilizando os seguintes defaut:

* A: Equipamento;
* B: Mão de Obra;
* C: Material;
* D: Atividades Auxiliares;
* E: Tempo Fixo;
* F: Momento de Transporte;
* P: Produção da Equipe;
* U: Custo Unitário da Execução - (A+B)/P

**Planilha de composição analítica por tarefas considerando BDI diferenciado:** Ele exibirá uma planilha com as composições utilizadas no projeto por tarefa considerando BDI diferenciado.  
**Planilha de composição analítica de preços unitários por produção:** Ele exibirá uma planilha analítica com as composições de preços unitários por produção utilizadas no projeto agrupadas pelo grupo DNER.   
**Planilha de composição analítica de custo unitários:** Ele exibirá uma planilha analítica com as composições de custos unitários utilizadas no projeto agrupadas pelo grupo de custo.   
**Planilha analítica de CPUs por tarefas com descr. Composição auxiliar:** Ele exibirá uma planilha analítica com as composições de preços unitários e suas composições auxiliares utilizadas no projeto por tarefas.  
**Observações:**   
Os relatórios serão gerados da mesma forma tanto para Totvs Reports como para Gerador de Relatórios e possuirão as mesmas escolhas de filtros.
