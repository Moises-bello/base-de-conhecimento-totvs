---
content_hash: b1fa61ca40de25eac1512fac1fb38a6e7571ad95bc8cadbdefc7aaa77e2042f9
fetched_at: '2026-06-29T00:09:13.708963+00:00'
page_id: '421385093'
product: rm
source: tdn-rm
title: Atualização do PERT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385093
version: 2
---

Foi criado no TOTVS Obras e Projetos o processo de atualização de PERT e pode ser visualizado e executado na visão principal ou na edição da Folha Tarefa. O processo é responsável por atualizar o percentual do PERT de acordo com os dados coletados via coletor móvel ou manualmente. Esse não é um processo automático e somente poderá ser executado para Folhas Tarefas que estejam com os apontamentos validados e o status como 'Apontada'.   
 **Atenção:** Em caso de projetos com revisão, as atualizações serão enviadas para o último projeto em andamento.  
 Qualquer alteração nos dados devem ser feitas antes da atualização do PERT, já que depois de executado o processo nenhum dado pode ser alterado.  
 Depois de executado o processo, o PERT assumirá a Data Início Real como a Data Início Programada e a Data Fim Real como a data da execução do processo, caso o percentual de completude seja 100%, caso contrário, o campo ficará em branco.   
 Caso exista algum percentual de completude lançado para a tarefa no PERT, o novo percentual lançado será lançado ao percentual existente, não podendo ultrapassar 100%.  
 Após a execução do processo, o status da Folha Tarefa será alterado para 'Encerrada' e o campo 'Data de Atualização do PERT' no Relatório de Status de Carga será atualizado com a data de execução do processo.
