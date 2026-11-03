---
content_hash: 3c0df2167a2eaa09eccae0f9c3ec42f44fb2621ee3d1e4ca117c4fd1bfb04a24
fetched_at: '2026-06-29T00:10:21.978551+00:00'
page_id: '496009342'
product: rm
source: tdn-rm
title: DT TOP Mobile sem folha tarefa - Filtro
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+TOP+Mobile+sem+folha+tarefa+-+Filtro
version: 6
---

# DT TOP Mobile sem folha tarefa - Filtro

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Obras e Projetos. |
| **Função:** | TOP Mobile sem folha tarefa – Filtro de tarefas |
| **Situação/Requisito:** | Foi criado o filtro de tarefas para ser utilizado quando o projeto não utiliza folha tarefa |
| **Solução/Implementação:** | Foi implementado o filtro de tarefas no anexo do coletor “Associação de Projeto(s) a Coletor” para que ao sincronizar o projeto sejam enviadas para o coletor somente as tarefas filtradas. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | Totvs0c783de1-186e-383b-975c-a1acd7d76cb5TOPORCAPLAN001-7668Totvs0c783de1-186e-383b-975c-a1acd7d76cb5TOPORCAPLAN001-7543 Totvs0c783de1-186e-383b-975c-a1acd7d76cb5TOPORCAPLAN001-7767 |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |

Filtro:

* O Filtro criado segue o mesmo padrão de filtros do RM.
* Os campos passíveis a serem utilizados neste filtro são correspondentes as tabelas que se relacionam com as Tarefas, como.: Cronograma Previsto, Local de Serviço, Unidade de Serviço.

* Após definir o Projeto e o Filtro, é possível testar o mesmo e visualizar as tarefas que serão sincronizadas para o respectivo coletor, basta clicar no botão  que a tela de "Tarefas do filtro avançado a serem sincronizadas" será aberta com suas respectivas tarefas. Se nenhuma tarefa for exibida é porque nenhuma delas se encaixa nas condições definidas no filtro.
* Se o projeto associado ao coletor não utilizar folha tarefa, isto é, se o parâmetro de projeto "Utiliza Folha Tarefa" estiver desmarcado e na associação ao coletor não estiver definido nenhum filtro, o filtro padrão será considerado para que as tarefas possam ser selecionadas para envio ao coletor,. A condições do filtro padrão são as seguintes:
  + Tarefas que tem o cronograma planejado definido em períodos que correspondam ao intervalo da data corrente menos 15 dias e mais 15 dias;
  + Tarefas que não tem o cronograma realizado em 100%;
  + Se o projeto utiliza travamento de períodos do cronograma planejado, apenas os passíveis de utilização serão considerados.
