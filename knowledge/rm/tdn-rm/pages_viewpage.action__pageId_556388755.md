---
content_hash: 26280b5d9b24d500007cd53b6a701dd27670ea04d0ed70a851a4ab7d7b277c0b
fetched_at: '2026-06-29T00:10:46.904304+00:00'
page_id: '556388755'
product: rm
source: tdn-rm
title: Visualização do Modelo 3D - Planilhas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=556388755
version: 17
---

---

Dentro da Visualização do Modelo 3D, é possível abrir Planilhas de Atividades, Serviços e seus respectivos cenários.

Com a visão das Planilhas abertas, é possível editar as Atividades.

Foi criado um campo novo na Tarefa, aba **Outros** que define o [Tipo da Tarefa](https://tdn.totvs.com.br/display/LRM/Tipo+de+Tarefa), veja:

Para associar Tarefas ao Objeto 3D, basta selecionar a(s) Tarefa(s) e o(s) objeto(s) a associar e, na parte inferior da Tela, selecionar a Opção **Associar**. Caso queira desassociar a Tarefa a um objeto opção **Desassociar**. Ou ainda utilizar as teclas de atalhos **Ctrl+1** ou **Ctrl+2** respectivamente.

* Após associado, na parte inferior o campo **Objetos** é incrementado com a quantidade de objetos associados a esta Tarefa;
* É possível associar vários objetos a uma Tarefa ou várias Tarefas para um mesmo objeto;
* Quando exite vínculo Tarefa X Objeto, ao selecionar a Tarefa, o objeto é selecionado de forma automática na Animação 3D;
* É possível ainda visualizar as Tarefas associadas ao Objeto na [Árvore de Objetos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=556388833) - Tarefas;

*"É possível abrir nessa visão mais de uma Planilha e navegar entre elas."*

Foi adicionado aos Processos da Planilha e Atividades (apenas com a Visualização do Modelo 3D aberta) o processo de [Extração de Quantitativos do Modelo 3D](https://tdn.totvs.com.br/pages/viewpage.action?pageId=556386415).

* Executando este Processo a partir dos [Modelos de Projeto](https://tdn.totvs.com.br/display/LRM/Modelos+de+Projeto) o sistema extrai os quantitativos para **todas**a atividades que possuírem vínculo no Modelo;
* Ao executar o Processo a Partir da [Visualização do Modelo 3D](https://tdn.totvs.com.br/pages/viewpage.action?pageId=556379451) o sistema extrai os quantitativos apenas para as tarefas selecionadas;

**Filtro Avançado**

Na Visualização do Modelo 3D, quando se tem as Planilhas de Atividades e Serviços abertas é possível realizar um Filtro Avançado para uma melhor visualização dos Objetos, veja:

* Tarefas Atrasadas;
* Tarefas em dia;
* Tarefas adiantadas;
* Tarefa com Pedido;
* Tarefas com Pedido Extra;
* Tarefas com Contrato;
  + Opção de filtrar por Tarefas medidas via Contrato informando o Contrato e/ou Fornecedor;
* Tarefas com objetos associados
* Tarefas sem objetos associados
* Limpar filtro - limpa os filtros aplicados e volta para visão original

O sistema permite que seja aplicado vários Filtros ao mesmo tempo, exemplo: Tarefas atrasadas que possuem Contrato;

Ao aplicar o filtro, o sistema verifica se o Projeto Utiliza PERT através dos [Parâmetros de Projeto (F6)](https://tdn.totvs.com/pages/releaseview.action?pageId=421385179), caso sim será considerada Data Programada, Percentual Concluído e Início Real e Final do PERT para Tarefas atrasadas, em dia e adiantadas. Caso não utilize será considerado o Cronograma Previsto e Realizado do [Cronograma](https://tdn.totvs.com/display/public/LRM/Cronograma+Anexos).

Uma vez aplicado o Filtro, o sistema irá apresentar as Tarefas conforme selecionado no Filtro assim como os objetos. Os objetos que **não** fazem parte do Filtro Aplicado, será exibido na tela com 90% de Transparência.

Veja:

Ao selecionar todas as Atividades da visão após a aplicação do Filtro é possível através do Botão **Selecionar Objetos das Tarefas Marcadas** que todos os objetos da visão sejam selecionados.

[Voltar](https://tdn.totvs.com.br/pages/viewpage.action?pageId=556379451)
