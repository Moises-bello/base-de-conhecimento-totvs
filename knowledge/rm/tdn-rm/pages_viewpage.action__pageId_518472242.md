---
content_hash: 9b1ff697767bdcb0635662a7e4753d95ce02ee87d97650f60ba2da79ed271c8e
fetched_at: '2026-06-29T00:10:29.983822+00:00'
page_id: '518472242'
product: rm
source: tdn-rm
title: Apropriações e Movimentações do Backoffice no TCOP - Totvs Construção Obras
  e Projetos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=518472242
version: 42
---

A partir da ativação do parâmetro de projeto (Importar Apropriações do Backoffice), todas as apropriações serão recuperadas do BackOffice e armazenadas no Totvs Construção Obras e Projetos (Tabela MMOV ou View MAPROP). Serão consideradas também no TOP as apropriações de serviços/insumos e/ou liberações de medição de contrato. Esses dados também serão mostrados no CockpitTCOP de Insumos e Tarefas mais informações sobre o Cockpit em: . Mais detalhes sobre informações especificas referente ao BackOffice ou parametrização necessárias de acordo com o BackOffice em:  [BackOffice Protheus](https://tdn.totvs.com/x/davxIQ) - [BackOffice Nucleus](https://tdn.totvs.com/x/ZavxIQ)

Importante ressaltar que para visualização das apropriações e movimentações é necessário a liberação de permissão no sistema.

Acessando o perfil de usuario .

Selecione a opção Acesso a Menus / Obras e Projetos / Controle / Consultas / Movimentações do Backoffice e Apropriações

(somente após a liberação de permissão que ficará visivel no anexo da planilha de atividades.)

Vale ressaltar que se o parâmetro "Utiliza processo de Importar Apropriações Backoffice"  não estiver habilitado não é exibido os valores apropriados no cockpit. Para visualiza-los no coockpit certifique se o parâmetro esta realmente habilitado nos parâmetros do projeto (tecla de atalho F6)

# Apropriação de Serviços / Insumos

As apropriações são visualizadas no cronograma da planilha de atividades / relatórios e utilizadas no cálculo do processo de análise de valor agregado.

No cadastro da “Apropriação de Serviços / Insumos” disponível no TOP em ***“Controle"*** , está disponível a origem da apropriação. Esta informação permite ao usuário identificar a origem e aplicar filtros. A origem denominada “Padrão” é para itens cadastrados por esta interface de apropriações.

# Movimentações do Backoffice e Apropriações

No menu da aba Controle encontra-se disponível a consulta de movimentações do Backoffice (Pagamento, Entrega e Apropriação).

# UTILIZAÇÃO DO PROCESSO:

O processo poderá ser realizado das seguintes maneiras:

1 - Agendando o processo de importar apropriações e movimentações do BackOffice da Planilha de Atividades para cada projeto. Por exemplo mensalmente ou diariamente. 

2 - Executando manualmente o processo importar apropriações e movimentações do BackOffice na Planilha de Atividades.  
  
Neste processo o sistema selecionará durante a execução todas as tarefas da planilha de atividades e o intervalo de períodos definidos nos parâmetros de projeto.

Caso o parâmetro de projeto defina a evolução automática do intervalo de períodos e a execução ocorra com sucesso, os períodos inicial e final serão alterados com base na data de fechamento contábil retornada pelo BackOffice.

3 - Executando o processo com parâmetro "Importar toda a Planilha" desmarcado.

Neste processo é permitido informar tarefas e períodos inicial e final.

4 - Executando através do botão "Importar Apropriações e Movimentações do BackOffice" do cronograma

Este processo é executado somente para a tarefa relacionada ao cronograma e considerando a faixa de períodos dos .

Quando executado para obra ou etapa, o sistema considera o primeiro e o último serviço na hierarquia do código da tarefa.

Lançamentos Financeiros

Os Lançamentos Financeiros que são exibidos no Dashboard de Indicadores são importados, também, através da execução desse processo, portanto para visualizar os Valores Previstos, Pendentes e Pagos no dasboard é necessário sua execução. O filtro de data para os respectivos lançamentos, também considera a data de fechamento.
