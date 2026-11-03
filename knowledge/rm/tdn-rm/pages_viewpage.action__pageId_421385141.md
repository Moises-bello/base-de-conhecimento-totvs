---
content_hash: 9225218b7fc0abbda305017060a3aab13b47f10ce2a3c8552121683ae62e1bdb
fetched_at: '2026-06-29T00:09:14.155880+00:00'
page_id: '421385141'
product: rm
source: tdn-rm
title: Atualização das Datas do PERT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385141
version: 2
---

Após o envio de movimento e associação do movimento a ordem de produção, é necessário verificar se a data prevista de fabricação do produto atende o planejamento da tarefa no Pert. Para que o TOP consiga identificar qual será a data prevista de fabricação, é disparado no RMFactor no momento da seleção do processo "Analise de ordem de produção" um serviço que busca qual é a data prevista de conclusão da fabricação.   
 Após executar o processo de "Análise de ordem de produção" no Pert, o TOP consulta se existe alguma ordem de produção para as tarefas que possuem recurso associado e esse recurso tenha produtos manufaturados. A atualização de datas do Pert apenas ocorre se o produto manufaturado associado ao insumo receber uma data de fabricação posterior a data de conclusão (data fim programado) da tarefa, caso ocorra este cenário, é disparada uma mensagem de alerta ao usuário solicitando que o mesmo defina se as datas das tarefas deverão ser atualizadas ou não.  
 Após a alteração das datas das tarefas pelo processo "Análise de ordem de produção", o TOP dispara automaticamente a funcionalidade de programar do Pert, para manter o planejamento das datas e sucessões de todas as tarefas.   
 **Observação**  
 Caso o parâmetro "Atualiza automaticamente pela ordem de produção" estiver selecionado, as datas das tarefas são atualizadas de acordo com a data programada da ordem de produção, sem a necessidade do alerta, tornando este processo automático.  
    
 Passo - a - passo para atualização das datas do PERT:  
 1) Acessar o RMSOLUM;  
 2) Selecionar o Projeto;  
 3) Acessar o menu: CADASTROS|PERT|ATIVIDADES e/ou SERVIÇOS;  
 4) Acessar o menu: FUNÇÕES DO PLANEJAMENTO|ANÁLISE DE ORDEM DE PRODUÇÃO;  
 Caso o produto manufaturado associado ao insumo receber uma data de fabricação posterior a data de conclusão (data fim programado) da tarefa, ao executar o processo de Análise de Ordem de Produção será disparado uma mensagem de alerta solicitando que o mesmo defina se as datas das tarefas deverão ser atualizadas ou não.  
 Se o produto manufaturado associado ao insumo NÃO receber uma data de fabricação posterior a data de conclusão (data fim programado) da tarefa, a mensagem de alerta disparada será outra: "Nenhuma das ordens de produção solicitadas estão com datas superiores ao planejado. "
