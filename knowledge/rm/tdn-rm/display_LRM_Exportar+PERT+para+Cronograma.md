---
content_hash: b56ff2a6888bec32906f494bff9409b7d132ee8588da6fbdb305883bdbe80a97
fetched_at: '2026-06-29T00:09:14.726879+00:00'
page_id: '421385241'
product: rm
source: tdn-rm
title: Exportar PERT para Cronograma
type: documentation
url: https://tdn.totvs.com/display/LRM/Exportar+PERT+para+Cronograma
version: 6
---

---

Exportar PERT para o Cronograma: Exporta o PERT para o cronograma de acordo com as opções selecionadas na Data de Origem, Cronograma de Destino, Converter Medições e Escopo da Conversão.

Lança no cronograma as informações que estão armazenadas no PERT.

Executa-se esse processo para todas as atividades, inclusive as tarefas que possuem divisão de tarefas. Para mais detalhes sobre tarefas que possui divisão veja em: [Dividir Tarefa](https://tdn.totvs.com/display/LRM/Dividir+Tarefa)

Para Exportar PERT para Cronograma, acesse o Cronograma | Processos | Exportar PERT para o Cronograma, neste momento as opções abaixo são fornecidas:

**Data de Origem**

* Base: É o ponto de referência a partir do qual você mede as alterações efetuadas no projeto.
* Programada: São as datas em que foram planejadas as execuções das atividades.
* Real: São as datas nas quais as atividades serão realizadas.

**Cronograma de Destino**

* Base: É o ponto de referência a partir do qual você mede as alterações efetuadas no projeto, Cronograma Base.
* Previsto: Planejamento das atividades a serem realizadas na Obra.
* Realizado: Realização das atividades por período nas obras.
* Medido: Medição das atividades que serão realizadas.

**Converter Medições Para**

* Percentual:  A conversão de valores será realizada levando em consideração o percentual.
* Quantidade: A conversão de valores será realizada levando em consideração a quantidade.
* Valor: A conversão de valores será realizada levando em consideração o valor.

**Escopo da Conversão**

* Escopo da Conversão Todas as Tarefas:
* Esta opção já vem marcada por default.

**Observação:**  
Somente é possível editar uma célula de cada vez no PERT. Assim, ao alterar uma célula deve-se salva-la antes de alterar outra, pois o sistema não permite a edição de outras, enquanto as alterações já feitas não forem atualizadas.

Exemplo de Exportações do PERT para o Cronograma:

Exemplo 1:

Data de Origem: Base, Cronograma de Destino: Previsto, Converter Medições para: Percentual

Quando essas informações são definidas, será considerada a Data Base para Exportação, onde o cronograma previsto irá receber a exportação, e a grandeza utilizada é Percentual (de acordo com o percentual a quantidade e o valor da atividade é calculado).

Exemplo 2:

Data de Origem: Programada, Cronograma Destino: Realizado, Converter Medições para: Quantidade

Neste cenário, a Data Programada será considerada para Exportação, o cronograma realizado será o cronograma de destino, quando cronograma realizado é a opção selecionada, são habilitadas as opções abaixo:

Considerar % Concluído: Este percentual é o percentual concluído informado no PERT

Exportar % Concluído para o primeiro período em aberto: Esta opção só é ativada quando a opção Considerar % concluído é marcado, esta é utilizada, quando em Parâmetros do Projeto -> Cronograma -> Gerais definimos os períodos passíveis de alteração, com isso o período para recebimento da exportação pode ser diferente do primeiro período, não sendo esse o período inicial.

Recalcular Planejamento: Caso não tenha sido realizado todo o percentual do período planejado, o replanejamento deve ter sido realizado, distribuindo os valores restantes para os outros períodos, que não receberão o realizado.

Caso tenha sido realizado um percentual maior que o planejado no período que recebeu a exportação, o replanejamento deve ter sido realizado, distribuindo os valores para os outros períodos de forma que estes irão diminuir.

Exemplo 2.1:

Foi planejado os períodos em Percentual, no primeiro período foram planejados 10%, no segundo 20%, no terceiro 50% e no quarto 20%.

No PERT foi inserido no realizado o percentual de 5%, e definida as datas de inicio e fim, no momento da Exportação do PERT para o Cronograma, foram definidos, Data Origem: Programada, Cronograma de Destino: Realizado (Serão habilitadas opções para Considerar % Concluído, Recalcular Planejamento e Exportar % concluído para o primeiro período aberto (Para esta opção ser simulada adequadamente, o período que já foi exportado, deve ser travado, para que na próxima exportação os valores sejam atualizados no próximo período), para este teste é necessário que todas estas opções estejam marcadas) e Converter Medições para: Quantidade.

No cronograma Previsto deve estar em negrito a grandeza percentual, definindo como este foi planejado, e no cronograma Realizado deve estar em negrito a grandeza quantidade, informando como foram definidos os valores para o realizado.

Nos períodos tanto planejado, quanto realizado, os valores devem ter sido replanejados, estando dispostos da seguinte forma:

Período 1: 5%, Período 2: 21,11, Período 3: 52,78, Período 4: 21,11

Obs. o cronograma previsto é modificado devido a utilização da opção Recalcular Planejamento que recalcula o cronograma planejado, de acordo com os lançamentos efetuados no cronograma realizado.

A conta para o replanejamento é realizada da seguinte forma:

Obtém-se a porcentagem que não foi utilizada no Primeiro período que é de 5%, é realizada a soma de quanto estava planejado antes da exportação, para os períodos restantes, no caso 90%, então realiza-se a conta:

Período 2: (20/90)\*5 = 1,11, ou seja este valor será acrescentado ao valor do planejado ficando então 21,11. Este processo será realizado para todos os períodos restantes.

Se tivesse sido realizado 5% a mais seria abatido do valor planejado os 1,11 ficando 18,89, no segundo período.

Exemplo 3:

Data de Origem: Real, Cronograma de Destino: Medido, Converter Medições para: Valor

Neste cenário a data levada em consideração é a Data Real, o cronograma de destino que irá receber a exportação é o Medido, a conversão será por valor, ou seja, serão enviados as informações com base na grandeza valor e a partir dela será calculado a quantidade e percentual.

É possível exportar a partir da data Real mesmo sem informar a Data Fim Real, o que possibilita a exportação de um percentual concluído menor que 100%, nesse caso a Data Fim Real que será considerada é a Data Início Real + Duração Programada.

---
