---
content_hash: 8f7fb3e2a9039e5d2f95250d8ae7c90b76208a252cbdcb5b6103d3b323c3505c
fetched_at: '2026-06-29T00:11:50.501285+00:00'
page_id: '841679935'
product: rm
source: tdn-rm
title: Saldo do Projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/Saldo+do+Projeto
version: 5
---

Através da seleção da **forma de cálculo do Projeto** pelo **Saldo da Tarefa** (parâmetro destacado na imagem), será possível efetuar o cálculo do projeto com base no saldo das tarefas que o compõe, e não mais pela quantidade total da tarefa como é feito na forma default (**Padrão**):

Importante!

Essa forma de cálculo é recomendada somente para projetos que irão utiliza-la desde o início e preenchendo o cronograma pela grandeza percentual. A alteração no meio do projeto poderá acarretar na alteração dos valores do cronograma.

Na planilha, a coluna Saldo Qtde. (Cronograma Realizado), permite a visualização do saldo em quantidade de cada tarefa do projeto, e se aplica tanto à planilha de serviço quanto atividade. Conforme destacado na descrição do campo, esse saldo é calculado com base no cronograma realizado da tarefa subtraído da quantidade total da mesma:

Assim a cada avanço das tarefas e atualização do cálculo do projeto, será exibido o saldo, em quantidade, que resta para conclusão da mesma.

Quando o parâmetro da forma de cálculo do projeto estiver pelo saldo da tarefa, ao invés de considerar a coluna da **Quantidade** da tarefa na Planilha de Atividades, irá considerar a coluna de **Saldo Qtde. (Cronograma Realizado)** .

Consequentemente, a barra de cálculo do projeto irá exibir o **Saldo do Projeto** e não mais o total do projeto calculado anteriormente. Da mesma forma, todos os registros de Histórico de valores do Cálculo do Projeto passarão a exibir os saldos.

Assista ao **vídeo Howto** da funcionalidade
