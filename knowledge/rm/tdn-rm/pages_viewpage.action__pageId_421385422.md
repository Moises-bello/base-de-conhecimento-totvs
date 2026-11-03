---
content_hash: 6ce2225cee2159ac09980d1927a09799a1974b3c2ccb1120d8fdf15166b577a3
fetched_at: '2026-06-29T00:09:15.595148+00:00'
page_id: '421385422'
product: rm
source: tdn-rm
title: Lançamentos Múltiplos Cronograma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385422
version: 2
---

---

Através desta opção pode-se efetuar lançamentos múltiplos nos cronogramas das tarefas, converter lançamentos já existentes no cronograma e ratear os valores lançados para os períodos selecionados.  
  
 Opções:  
  
 Informar em qual grandeza será o lançamento: Listar as opções Percentual, quantidade e valor. Irá simular o lançamento de uma célula na grandeza escolhida.  
  
**Atenção:**

* Se o parâmetro "Alteração de cronograma (intervalos de períodos passível de alteração)" estiver marcado, não poderá receber lançamentos múltiplos e se já houver informações cadastradas na grid as mesmas não poderão ser alteradas pelos lançamentos múltiplos.
* Não será informado na janela .NET o nome da tarefa visto que o usuário poderá selecionar mais de uma tarefa para aplicar o processo.
* Informar o percentual lançado da tarefa - Informe o valor (Percentual ou Quantidade ou Valor) que será lançado no cronograma.
* Existi uma consistência respeitando que o cronograma previsto não ultrapasse 100%.
* Converter lançamentos Existentes – esta opção converterá os lançamentos já existentes nos períodos dos cronogramas para a grandeza de conversão selecionada. Quando esta opção for selecionada os campos de Quantidade, Grandeza e rateio ficarão desativados.
* Diferentemente da aplicação Delphi a execução do processo se dará somente nas atividades selecionadas. Por isso não se faz mais necessário avisar que a conversão se dará em todas as tarefas.
* É obrigatório escolher a conversão, informar no campo "Converter para".  Se não escolher, ao clicar em salvar será emitida a mensagem: "Informe o Percentual, quantidade ou valor do lançamento".    
  Converter para - Selecione para qual grandeza os lançamentos nos períodos dos cronogramas serão convertidos.
* A grandeza do lançamento dos valores deve ser diferente da grandeza de conversão.
* Este campo é obrigatório quando for escolhido converter lançamentos existentes.
* Selecionar os períodos - Marque em quais períodos do cronograma serão efetuados os lançamentos.
* Através do clique com o botão direito do mouse neste campo, pode-se marcar ou desmarcar todos os períodos disponíveis ao selecionar as opções "Marcar Todos" ou "Desmarcar Todos" respectivamente.
* Pode-se informar apenas um período para realizar lançamentos múltiplos, dependendo da necessidade do usuário.
* Ratear o percentual informado entre todos os períodos selecionados: Se esta opção estiver marcada, o sistema irá ratear o valor informado, seja ele em percentual ou quantidade ou valor, para todos os períodos selecionados do cronograma.
* Aplicar nos períodos do cronograma - Marque os cronogramas (Previsto, Realizado e/ou Medido) em que serão lançados ou convertidos os valores (Percentual ou Quantidade ou Valor) para cada período informado.
* A consistência para não permite lançar valor ou quantidade para Obras Ou Etapas é feita no servidor (Após solicitar para executar).
* Na opção de lançamento de valores novos, os valores de períodos não escolhidos, não são alterados. Exemplo: o cronograma planejado já possui valores do periodo 1 a 5. Caso execute um lancamento multiplo para o periodo 1 a 4, o período 5 ficará inalterado.
* Os botões de scroll foram retirados por não serem mais necessários.
* É necessário selecionar pelo menos um período e um cronograma.
