---
content_hash: a1f6d3786a712b7c062eb69f56b04d51837afa4d387ad0036c7eb08cc0129495
fetched_at: '2026-06-29T00:09:14.880490+00:00'
page_id: '421385292'
product: rm
source: tdn-rm
title: Encerrar Folha Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/Encerrar+Folha+Tarefa
version: 3
---

---

Foi criado no TOTVS Obras e Projetos o processo de Encerrar Folha Tarefa e pode ser visualizado e executado na visão principal ou na edição da Folha Tarefa.

O processo é responsável por atualizar o percentual do PERT de acordo com os dados coletados via coletor móvel ou manualmente.

Esse não é um processo automático e somente poderá ser executado para Folhas Tarefas que estejam com os apontamentos validados e o status como 'Apontada'.

**Atenção:**

Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa \ Processos \ Encerrar Folha Tarefa; 

* Esse processo altera o status da Folha Tarefa para "Encerrada";
* Em caso de projetos com revisão, as atualizações serão enviadas para o último Projeto em andamento.
* Qualquer alteração nos dados devem ser feitas antes do Encerramento da Folha Tarefa, já que depois de executado o processo nenhum dado pode ser alterado.
* Se o parâmetro de projeto "Atualizar o PERT automaticamente ao sincronizar e ao salvar o apontamento de Avanço Físico" estiver desmarcado, esse processo irá atualizar as informações do PERT (Program Evaluation and Review Technique), onde a atualização é sempre substituindo os valores existentes com os novos valores apontados.
* Esse processo somente poderá ser realizado para uma Folha Tarefa com status igual a “Apontada” e cujos apontamentos dos itens estejam validados;
* Ao integrar as informações da carga com o TOTVS Construção Obras e Projetos, o sistema terá o seguinte comportamento: A data início real da atividade deverá ser a data início planejada da atividade. A data fim real deverá ser a data do apontamento, caso o avanço apontado seja de 100%;
* O percentual concluído será dado por: (Quantidade planejada / Quantidade total da tarefa \* Percentual Apontado) + Valor Atual do PERT. Caso o percentual concluído seja superior a 100+variação aceitável o valor não será atualizado. Uma mensagem informativa será adicionada ao log. Após a execução do processo, o sistema atualiza o status da Folha Tarefa para “Encerrada” e atualiza o campo “data de atualização do PERT”, constante do cadastro de Folha Tarefa, com a data de execução do processo;
* Nesse processo, o parâmetro de medição acima de 100% também é verificado se existir contrato vinculado ao item, e se estiver diferente de SEMPRE PERMITIR, e a quantidade apontada do item da folha for maior que a quantidade do saldo do item no contrato, um alerta será exibido, não permitindo a execução. Caso as validações estejam aprovadas, a quantidade apontada do item será incorporada à medição do item no contrato, no respectivo período que corresponde à DATA DE APONTAMENTO do item da folha. Se o período do contrato estiver liberado, a medição não será inserida e o erro deverá ser exposto.

**Observação:**

Este processo verifica o Parâmetro de Projeto 'Atualizar o PERT automaticamente ao sincronizar e ao salvar o apontamento de Avanço Físico' em **"Projeto | Construção e Projetos | Projetos (ou atalho F6) | Mobilidade | Folha Tarefa"** onde o mesmo somente realiza a atualização do PERT se o mesmo estiver desmarcado.
