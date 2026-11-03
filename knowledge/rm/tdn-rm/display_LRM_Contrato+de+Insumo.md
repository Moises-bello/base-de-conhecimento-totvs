---
content_hash: 5cbe740a6c81849394ae89842c4817dd85f9d2b6d128f2ccd2b659e9f3ab1d87
fetched_at: '2026-06-29T00:09:15.358814+00:00'
page_id: '421385358'
product: rm
source: tdn-rm
title: Contrato de Insumo
type: documentation
url: https://tdn.totvs.com/display/LRM/Contrato+de+Insumo
version: 15
---

O contrato de Insumo tem como objetivo realizar o consumo dos objetos (insumos) associados ao contrato.

Para cadastrar um Contrato de Insumo é necessário selecionar a finalidade do contrato, dentro da inclusão de novos contratos. Tais contratos serão sempre do tipo "A pagar":

**Na pasta Identificação:**

Somente é obrigatório o preenchimento dos campos Número do Contrato, Código do Cliente / Fornecedor, Data do Contrato, Data Início, Data Término.

**Posição Atual:**

Inicialmente, ao inserir um novo contrato, a posição do mesmo será sempre "Em Andamento". Para alterar a posição do contrato, basta inserir uma nova posição através do anexo "Histórico do Contrato".

Quando o contrato está com a posição "Paralisado", "Cancelado" ou "Concluído" não é possível efetuar inclusões, alterações e exclusões dos dados do mesmo.

A associação de objetos é feita através do processo de Associação de itens ao contrato>**Associar objetos ao Contrato**. Através dele é possível associar insumos que estejam vinculados ao grupo de custo selecionado.

Na associação de objetos, foi incluído o conceito Prioridade de Consumo. A informação de prioridade de consumo dos objetos será considerada no momento da associação dos mesmos objetos em outros contratos.

Um objeto não pode ser associado mais de uma vez com um mesmo valor de prioridade de consumo. Caso tente fazê-lo, será informado que aquele objeto já esta associado com tal prioridade. Caso escolha prosseguir com a associação, o objeto na associação feita anteriormente terá a sua prioridade de consumo alterada.

É permitida a associação de percentuais do objeto do contrato assim como a definição do Valor a ser associado (Valor Unitário (com BDI), Custo Unitário).

Após já ter sido vinculado, não é possível alterar as informações de quantidade e valor do objeto. Apenas é possível atualizar a sua prioridade de consumo.

No processo, os objetos já associados ao contrato corrente serão exibidos na cor azul.

Através do Anexo 'Objetos do Contrato' é possível visualizar todos os objetos que estão associados ao contrato. Os objetos poderão ser excluídos do contrato também através desta funcionalidade, desde que não tenham sido consumidos e também podem ser visualizadas as quantidades consumidas de cada objeto:

**Associação de insumos para contratação**

A associação desomente será utilizada em contratos do tipo "Fornecimento de material" e "Contratos de insumo" que utilizem do processo de "Associar objetos ao contrato".

Ao acessar o processo de "Associar objetos ao contrato " serão exibidos na tela, os insumos que poderão ser associados ao contrato. Nesta visão, os insumos que forem do tipo Somente Orçamento/Planejamento serão apresentados com o símbolo de "+" habilitado; e para os insumos padrão, o símbolo não ficará habilitado:

Clicando neste símbolo, serão listados os insumos do tipo Somente Contratação vinculados a este insumo pai (Somente Orçamento/Planejamento):

Para o insumo de contratação o usuário irá informar a quantidade a ser associada, bem como o valor unitário do insumo (o preço vigente virá preenchido caso exista mas permite a alteração).

Ao final do processo associação é feita, e somente os insumos do tipo contratação que tiveram quantidades e valor unitário informados serão apresentados no anexo de "Objetos do contrato".

O insumo contratado e o insumo principal não terão a sua cor alterada para azul após serem associados como ocorre com os insumos padrão.

As colunas apresentadas para identificação dos insumos que possuam detalhamento são: Código do insumo, Objeto, Unidade, Valor unitário orçado, Quantidade contratada, Valor unitário contratado, e Total contratado.

Ao realizar a associação, soma do **valor total** de cada um dos insumos detalhados (Somente Contratação), deve ser igual ou menor do que o valor total do insumo pai (Somente Orçamento/Planejamento) dos mesmos e que foi vinculado à tarefa.

É possível vincular um insumo detalhado na tela de associação de objetos ao contrato. Para realizar o vínculo e necessário clicar duas vezes sobre a linha do insumo pai, e abrir o anexo de Insumos para Contratação (imagem abaixo), diretamente na tela de edição do insumo pai e realizar o vínculo. Após realizar o vínculo e salvar as alterações, é apresentada uma mensagem informando se deseja atualizar a tela de associação de objetos. Caso deseje atualizar a tela, serão apresentados todos os insumos cadastrados na visão de Associar Objetos ao Contrato de Insumo. Ao atualizar a tela, todas as informações preenchidas anteriormente ao vínculo serão perdidas e deverão ser preenchidas novamente.

Para os objetos associados ao contrato através do aditivo de valor, o tratamento será conforme já descrito acima.

Os insumos do tipo Somente Contratação, serão consistidos através do parâmetro de: **Permitir contratação com valor superior ao orçado (Contratos A Pagar: Serviços, Fornec. de Material e Insumos):** Caso este parâmetro esteja desabilitado, quando o tipo do insumo para contratação for Somente Contratação, na associação dos insumos ao contrato, não será permitida a associação com valores superiores ao valor total orçado para o insumo pai (Insumo Somente Orçamento/Planejamento).

Os insumos do tipo Somente Contratação **NÃO** serão validados através do parâmetro**Não associar itens/objetos em mais de 100% da quantidade orçada (Contratos A Pagar),** pois a associação desse tipo de insumo é validada somente por VALOR e não por QUANTIDADE.

**Consumo dos objetos do contrato:**

Nesta funcionalidade estão disponíveis duas abas, uma para quantidade contratada do objeto (Objetos a consumir do contrato) e outra para visualização da quantidade consumida (Objetos consumidos no período). Nestas abas é possível visualizar informações como: Quantidade contratada, Valor Contratado, Quantidade Consumida, Valor Consumido, Percentual Consumido e Saldo do Valor e da Quantidade. Na primeira aba os valores são dispostos levando em consideração todo o contrato e na segunda aba o período em questão.

O consumo dos objetos do contrato é realizado através dos períodos gerados, é selecionado o período para consumo e acionado o botão  'Consumir objetos do contrato'. Nesta opção será apresentada a lista de objetos vinculados ao contrato selecionado, sendo possível associar um objeto ou vários objetos de uma só vez, é necessária a confirmação da associação de vários objetos. Selecionados os objetos, aparecerá a opção para identificar em qual tarefa será consumido e a necessidade, nesta associação existe uma validação onde só poderão ser consumidos objetos que pertençam à tarefa na planilha de atividades e estão vinculados a tarefa na Curva ABC de Insumos, estando de acordo com a validação os objetos serão listados e necessariamente precisam ser selecionados para realização do consumo de objetos. Caso tenham sido selecionados objetos que não estão vinculados a tarefa indicada, uma mensagem informando os objetos e o motivo da não associação será apresentada.

Os períodos consumidos devem ser marcados pelo símbolo V na cor azul sobre o símbolo do período.

O Contrato de Insumo obedece a parametrização do contrato para consumo superior a 100%, para visualizar a regra acesse  .

O Contrato de Insumo utiliza o anexo Aditivos Contratuais. É possível criar um aditivo apenas de data ou também de valor, associando objetos ao aditivo. Os anexos Departamentos do Contrato, Centros de Custo do Contrato, Retenções Contratuais e Adiantamento de Contrato e os processos de Geração de Períodos, Renumerar Períodos Principais, Renumerar Períodos Complementares e Renumerar Períodos Estorno são utilizados como descrito no contrato de serviços.

O anexo Itens do Contrato, bem como os processos Associação de Itens ao Contrato, Associar Períodos do Contrato à Períodos do Cronograma, Atualiza Cronograma pelos Lançamentos de Medição, não são utilizados pelo Contrato de Insumo. Assim, o acesso à tais funcionalidades não é permitido.

É permitido a Liberação do contrato para o Totvs Obras e projetos e para o Financeiro e gerar integração com Suprimentos\Faturamento.

De forma semelhante, o campo "Medição de Item de contrato" não pode ser utilizado sendo emitida mensagem de aviso. Na geração de períodos do contrato não é permitida a utilização da opção contrato de parcela fixa.

Pode-se realizar a liberação do contrato do Totvs Obras e Projetos para o Financeiro. Na Geração de Integração com Suprimentos/Faturamento é respeitado o parâmetro do Contrato Considerar produtos associados no faturamento de contrato de insumo.

O conceito de 'Consumir objetos' do Contrato de Insumos e 'Medir Itens' do Contrato de Serviços são equivalentes.

Caso o projeto esteja parametrizado para utilizar o parâmetro Permitir que itens contratados sejam associados com outro preço unitário no aditivo, o consumo de objetos deverá ser feito selecionando o objeto no grid de objetos associados ao contrato e inserindo através do botão "novo", pois não será permitido a utilização do lookup do grid de consumo. Mais informações: 

**Status de Contrato**

Existe uma validação do status do contrato para inserção ou alteração de aditivos quando o status do contrato estiver em: "Paralisado", "Cancelado" ou "Concluído", não permitindo ser alterado ou inserir outro aditivo.

Caso exista algum aditivo de contrato, poderá visualizar o aditivo mais não poderá ser alterado. Ao tentar inserir uma aditivo será exibida a mensagem:

---
