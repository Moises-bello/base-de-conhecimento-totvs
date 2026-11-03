---
content_hash: fc36915731ef9dc631b42be56f44be76cff1ac368493b599889f35f8107ee0bf
fetched_at: '2026-06-29T00:09:16.992006+00:00'
page_id: '421388544'
product: rm
source: tdn-rm
title: Novo Fluxo de Caixa
type: documentation
url: https://tdn.totvs.com/display/LRM/Novo+Fluxo+de+Caixa
version: 212
---

Atualmente as empresas necessitam de um fluxo de caixa que apresente informações não só para o controle da capacidade de liquidez da empresa, mas também informações que irão auxiliar na tomada de decisões gerenciais e estratégicas.

As informações existentes no fluxo de caixa podem ser utilizadas para várias análises, como por exemplo, a identificação de despesas desnecessárias, a identificação das receitas mais importantes, etc.

Visando atender às demandas atuais, de um fluxo de caixa analítico e flexível que permita aos gestores a realização de projeções que possibilitarão um melhor planejamento financeiro da empresa, é que a funcionalidade do Fluxo de Caixa do TOTVS Gestão Financeira está sendo evoluída.

Tipo de Planejamento

Representa o tipo de valor para um determinado planejamento de fluxo de caixa no TOTVS Gestão Financeira.  
Todo e qualquer planejamento do fluxo de caixa estará vinculado a um tipo de planejamento, permitindo categorizar os valores de forma flexível.

**Obs:**O cadastro, inclusão, edição e exclusão dos tipos de planejamento será condicionado à permissão de perfil, localizado em [05.02] Gestão de Caixa. É possível também inativar um determinado tipo de planejamento.

**Cadastro de Planejamento**

O cadastro de planejamento permite ao usuário informar valores para que possam ser levados para um fluxo de caixa e posteriormente auxiliar na definição de diversos cenários, isto é, estimar e planejar os gastos e recebimentos da empresa, em determinado período e de acordo com as informações deste planejamento.  
Este cadastro é composto dos seguintes campos:

* Permite Multicoligada: Define se o cadastro de planejamento poderá ser incluído para N coligadas caso marcado ou somente para a coligada corrente, caso desmarcado. Observação: Caso a flag "Permite Multicoligada" de um cadastro de planejamento esteja marcada e neste planejamento existir itens para diferentes coligadas, o sistema não permitirá a alteração deste parâmetro;
* ID. Planejamento: Identificação única do planejamento;
* Tipo Planejamento: Determina o tipo de planejamento ao qual o planejamento está associado;
* Descrição: A descrição do planejamento;
* Data Início: Data inicial do planejamento;
* Data Final: Data final do planejamento;
* Itens do planejamento: Cadastro de itens de planejamento. São definidos como itens do planejamento os seus valores, natureza (pagar ou receber), bem como uma data, um histórico que facilite sua identificação, além dos campos de filial, centro de custo e natureza orçamentária financeira. Será permitida a edição do item de planejamento, mas o campo de coligada ficará desabilitado se a opção "Permitir Multicoligada" estiver marcada.

**Observações:**

* Caso a opção "Permite Multicoligada" de um cadastro de planejamento for marcada e neste planejamento existirem itens para diferentes coligadas, o sistema não permitirá a alteração deste parâmetro;
* Para os itens do planejamento há a possibilidade de edição dos campos, bem como inclusão e exclusão (botão novo de inclusão / x vermelho) de itens de acordo com o planejamento. Poderão ser inseridos vários itens para um determinado planejamento. Quando desmarcada a opção de Multicoligada da tela de planejamento, o campo “Coligada” do item de planejamento ficará desabilitado para edição.
* O campo "Natureza Orçamentária" tem ligação com o campo "Natureza", respeitando sua classificação (pagar ou receber). A natureza orçamentária "Ambos" poderá ser selecionada tanto para natureza de classificação "Receber" quanto para "Pagar".
Planejamento de Fluxo de Caixa

O cadastro de planejamento permite ao usuário informar valores para que possam ser levados para um fluxo de caixa e posteriormente auxiliar na definição de diversos cenários, isto é, estimar e planejar os gastos e recebimentos da empresa em determinado período e de acordo com as informações deste planejamento.

**Procedimento para Utilização**

* Deverá ser habilitada no perfil do usuário a permissão do cadastro de planejamento, disponível em Gestão Financeira | Gestão de Caixa | Fluxo de Caixa | Cadastros de planejamento:

**Obs**: O planejamento deverá estar atrelado a um tipo de planejamento que foi cadastrado previamente.

Poderão existir vários planejamentos para um determinado tipo de planejamento.

**Descrição dos campos**

Interface de Planejamento de Fluxo de Caixa:

Este cadastro é composto dos seguintes campos:

* **ID. Planejamento**: Identificação única do planejamento;
* **Tipo Planejamento**: Determina o tipo de planejamento ao qual o planejamento está associado;
* **Descrição**: A descrição do planejamento;
* **Data Início**: Data inicial do planejamento;
* **Data Final:** Data final do planejamento;
* **Permite Multicoligada:** Define se o cadastro de planejamento poderá ser incluído para N coligadas, caso marcado, ou somente para a coligada corrente, caso desmarcado. **Observação**: Caso a opção "Permite multicoligada" de um cadastro de planejamento estiver marcada e neste planejamento existirem itens para diferentes coligadas, o sistema não permitirá a alteração deste parâmetro.

                                                                                                                       

**Item de Planejamento**

Os itens do Planejamento podem ser inseridos e exibidos no anexo da visão ou no anexo do planejamento cadastrado

O cadastro de um item de planejamento é composto dos seguintes campos:

* **Valor**: onde será informado o valor do item
* **Data**: onde será informado a data de inclusão do item
* **Natureza**: onde será informado se o item é  a pagar ou a  receber
* **Aplicação Origem**: onde será informado qual o produto de origem do item
* **Histórico**: onde será informado um contexto que facilite sua identificação
* **Coligada**: onde será informada a coligada a qual pertence o item. Nesse caso, se no cadastro do planejamento a opção "Permite Multicoligada" estiver marcada, é possível a edição do campo. Caso esteja desmarcada, essa opção será preenchida com a coligada default de inclusão do item (coligada corrente)
* **Filial**: onde será informada filial a qual pertence o item de planejamento
* **Centro de custo**: onde será informado o centro de custo que irá compor o item de planejamento
* **Natureza orçamentária**: onde será informada a natureza orçamentária do item, podendo ser de classificação a pagar, a receber ou ambos

**Observações:**

* Há a possibilidade de edição dos campos diretamente nas grids, bem como inclusão e exclusão (botão verde de inclusão / x vermelho) de itens de acordo com o planejamento.
* Poderão ser inseridos vários itens para um determinado planejamento, como mostra a figura abaixo.
* Não será permitida a inclusão de item de planejamento de mesma Natureza, Aplicação de Origem, Centro de Custo, Filial e Natureza Orçamentária  dentro do mesmo período.
* Itens de planejamento sem a Filial informada sempre serão exibidos no fluxo de caixa. Já aqueles sem centro de custo serão exibidos quando a opção "Centro de custo por natureza" não marcada e o filtro selecionado contém todos os registros.

Visão do Planejamento:

                                                                                                                         

Planejamento:

                                                                                                                         

Edição de Itens de Planejamento

Importação dos dados de planejamento via conceito

É possível importar o planejamento a partir de um arquivo externo ou a partir do orçamento já cadastrado. Primeiramente é necessário importar o conceito disponível no TOTVS Compartilhamento (menu Gestão | TOTVS Compartilhamento):

**Conceito disponibilizados no TOTVS Compartilhamento**

**CONFIN0004** - Importação itens de planejamento fluxo de caixa.concept

Esse conceito tem o objetivo de importar itens de um planejamento no qual a origem é um arquivo texto.

* + O campos devem ser separados por ";" na seguinte ordem abaixo:
    - Tabela Destino - Será sempre FPLANEJAMENTOFLXCXITEM
    - Data - Formato (AAAA-MM-DD)
    - Valor - O separador de decimal deverá ser ","
    - Código da Filial
    - Histórico
    - Código do centro de custo
    - Código da coligada da natureza financeira
    - Código da natureza financeira
    - Natureza - (1 - Receber, 2 - Pagar)
    - Aplicação - (F - Financeiro, S - Educacional, M - Obras e Projetos)

Exemplo da linha: FPLANEJAMENTOFLXCXITEM;2023-09-30;100,00;1;teste conceito;01.4;1;006.001.001;1;F

Obs.: Caso algum campo seja nulo deverá deixar vazio:

Exemplo de linha com o campo natureza vazio FPLANEJAMENTOFLXCXITEM;2023-09-30;100,00;1;teste conceito;01.4;;;1;F

* + Execução do conceito:

Será necessário informar para qual planejamento deseja importar o conceito e o arquivo:

**CONFIN0003** - Importação do Plan. de Fluxo de Caixa com Itens do Plan.concept

Esse conceito tem o objetivo de importar itens de planejamento no qual origem é os dados das tabelas de orçamento.

Para realizar o processamento, será preciso importar o arquivo do conceito para a base de dados e seguir as informações conforme a documentação disponível no link abaixo *Informações Complementares* (DT - Planejamento do Fluxo de Caixa).

Na importação via conceito, ao executar *'Processar novo conceito'*em Processosna visão do conceito, o sistema atualiza os Itens do Planejamento do Fluxo de caixa. Neste caso, existem algumas observações na execução do processo:

**1-** Ao executar o processo para um planejamento já existente, os itens antigos importados que não sejam originados do TOTVS Gestão Financeira serão apagados e substituídos na nova importação, mesmo os que foram editados;

**Obs**: Os itens do Planejamento originado do TOTVS Gestão Financeira somente poderão ser incluídos manualmente.

**2-** No processo de importação, o sistema possibilita que seja criado um novo Planejamento para realizar a importação dos novos itens sem substituir nos planejamentos já existentes;

**3-** Todos os itens importados no processo serão de acordo com o período informado dentro de cada Planejamento de Fluxo de Caixa. Caso apresente diferença nos itens importados, deve ser observado o período informado.

**4-** O sistema valida se as informações dos itens do Planejamento são iguais dentro do mês e, neste caso, não permite a inclusão:

**Obs:**Pode ser criado um novo conceito a partir do modelo disponibilizado, com consulta SQL trazendo dados de outras entidades.

Cenários

O cenário no contexto do TOTVS Gestão Financeira corresponde à imagem do fluxo de caixa em um instante no tempo, ou seja, dada uma configuração e filtros parametrizados, as informações geradas a partir destes na data de geração do fluxo de caixa representa o que queremos descrever como um cenário.

**Exemplo:** Vamos supor que do dia 01/05/2019 seja gerado o fluxo de caixa para o período de 01/05/2019 a  31/05/2019, para a conta caixa "0001" da coligada "1", exibindo somente as naturezas financeiras que possuem valor maior que zero com uma periodicidade semanal. A exibição deste fluxo de caixa nesse dia com essas configurações e filtro corresponde ao que descrevemos como um cenário.

* **Incluir cenário:** Após a geração de um fluxo de caixa, será possível gravá-lo como um cenário através do botão "Incluir novo cenário".  A partir de um cenário já existente, o valor dos campos Planejado, Previsto e/ou Realizado, poderá ser alterado como forma de simulação e salvo em um novo cenário, a partir da inclusão de cenário.
* **Habilitar/Desabilitar configurações e filtro:** Esta opção está disponível na visão de cenários e poderá ser habilitada ou desabilitada quando necessário. Quando habilitada, ela permite que seja refeita a configuração e remarcados os filtros usados para geração de um novo cenário. Quando alteradas as configurações e filtros, um novo cenário poderá ser criado com essas novas configurações. Porém, quando habilitada, o botão "Salvar alterações" ficará desabilitado, permitindo que somente seja incluído novo cenário. As configurações do cenário anterior serão mantidas.
* **Exibir cenário:** Os cenários estão disponíveis em uma visão de cenários que pode ser acessada pelo menu Gestão Financeira | Gestão de Caixa | Fluxo de Caixa | Cenários, através de duplo clique . Ao exibir um cenário já gravado em base de dados, ele será apresentado no formulário de fluxo de caixa, não sendo possível nesse momento alterar configurações ou filtros.

                                                                                                                               

**Obs:** A partir de um cenário já gravado anteriormente, ao exibi-lo será possível gerar um novo fluxo de caixa e incluir  um novo cenário obedecendo a parametrização e filtro do cenário anterior. No exemplo do cenário citado acima, poderia no dia 15/05/2019 gerar um novo cenário baseado nas configurações e filtros utilizados no cenário do dia 01/05/2019 e acompanhar as alterações que ocorreram entre estas datas.

* **Editar, renomear cenário:**  será possível editar um registro de Cenário de fluxo de caixa a partir de sua visão através do ícone de atalho de "Editar". Serão exibidos os campos Id, Descrição, Versão, Data e Usuário da última edição e Histórico. Somente a Descrição e Histórico poderão ser alterados. Após carregar o cenário na saída do fluxo de caixa os valores podem ser alterados e salvos no mesmo cenário, permitindo também informar novos dados para a Descrição e Histórico.

**Observação**

As opções "Incluir, Excluir e Editar Cenário" terão controle de permissão de acesso. Através de Globais em Serviços Globais | Segurança | Perfis | Gestão Financeira | Gestão de Caixa | Fluxo de Caixa | Cenários, o Perfil deverá ser associado ao Usuário de acesso ao sistema.

* **Controlar revisões de cenários:** Quando incluído um novo cenário, será possível realizar alterações e salvá -las através do ícone de atalho "Salvar alterações". A alteração realizada será salva no próprio cenário, com a possibilidade de informar dados novos nos campos "Descrição e Histórico" ou manter os anteriores. As alterações realizadas no campo "Histórico" no momento de "Salvar Alterações" serão registradas no campo histórico do cenário, e não irão sobrepor o histórico anterior. Ao incluir um novo cenário a partir de um já existente, os campos de descrição e histórico do cenário base serão apresentados como default e poderão ser alterados ou mantidos.  
  Ao incluir um novo cenário a partir de um já existente, será gerada uma nova versão para esse novo cenário. A cada nova inclusão, a versão será incrementada.
Data de Corte

Para utilização do Fluxo de Caixa, é essencial que a base de dados esteja íntegra, com rateios por natureza e centro de custo obrigatórios. Muitas vezes, este tipo de restrição impossibilita, ou torna muito custosa, a implantação do processo. Visando tornar este procedimento mais simples, foi implementado o recurso de Definição de Data de Corte do Fluxo de Caixa.

A "Data de Corte" possibilita que o usuário defina uma data específica para que o sistema faça o cálculo de toda geração do fluxo de caixa a partir da data definida. O valor do saldo informado nas contas caixas e  toda geração do fluxo de caixa será a partir dessa data e desse saldo. A Data de Corte será única, válida para todas as coligadas e possui processo de habilitação com tratamento de segurança por perfil de usuário.

Uma vez configurada a data de corte, as [contas caixas](https://tdn.totvs.com/x/JeIdGQ) serão carregadas com o campo "Data de Corte", onde será possível informar o "Saldo Data de Corte" e a "Data de Corte" que será carregada automaticamente na execução do processo.

Quando informada uma data de corte por meio deste processo, esta data será considerada como ponto de partida para a movimentação do Saldo Inicial Realizado. Também para efeito de formação desse saldo, passa a ser considerado o Saldo na Data de Corte em cada Conta/Caixa, desde que a Data de Corte seja posterior à Data Base da Conta/Caixa. . Caso o processo seja executado novamente e outra data de corte seja  informada, é importante que o novo valor de saldo seja atualizado no campo da conta caixa. O saldo da conta/caixa na data de corte substitui o saldo na data base, se a data base for anterior à data de corte.

Quando definido no sistema uma data de corte, ao gerar a planilha de fluxo de caixa, o valor do campo "Data Inicial" só poderá ter valor igual ou maior que a data de corte. Ao gerar a planilha de dados, o sistema fará a validação da data informada, conforme tela abaixo:

Fluxo de Caixa

A visão do Fluxo de Caixa é baseada no modelo clássico de Fluxos de Caixa utilizando planilhas eletrônicas. O TOTVS Gestão Financeira, integrado ao Microsoft Excel, exibe e permite salvar o Fluxo de Caixa em planilha diretamente relacionada aos Lançamentos Financeiros e Extratos de Caixa. Na visão, também é possível visualizar gráficos de Entradas, Saídas e Saldo Final referente às informações geradas do Fluxo de Caixa. Para visualizar o Fluxo de Caixa, basta acessar o menu Gestão Financeira | Gestão de Caixa | Fluxo de Caixa e preencher os dados para sua geração.

**Arquivo  Excel**: O Fluxo de Caixa gerado poderá ser salvo com os mesmos dados configurados na visão em formato do arquivo em Excel, bastando gerar o Fluxo de Caixa e clicar no ícone "Salvar Planilha Excel".

**Fixa as colunas de datas e naturezas no fluxo de caixa:** É possível fixar as linhas do cabeçalho do fluxo de caixa (Datas, Planejado, Previsto, Realizado, Prev+Real) e as colunas responsáveis por exibir os nomes das naturezas financeiras e seus centros de custos, facilitando a visualização e conferência dos dados apresentados.

**Gerar planejado a partir do previsto:**

É possível realizar uma carga de planejamento a partir de informações de valores previstos, o que poderá facilitar o controle dos valores planejados quando o cliente já gera com antecedência as suas previsões de valores. Funciona da seguinte forma:

A partir da geração de um fluxo de caixa com qualquer periodicidade informada, o sistema irá apresentar na visão o ícone “Gerar planejado a partir do previsto”. Através dessa funcionalidade, será disponibilizada tela onde poderão ser informados o tipo de planejamento e sua descrição. A partir do preenchimento desses dados, será criado automaticamente um planejamento com itens de planejamento que serão os valores da coluna de previsto, que passam a compor o valor planejado. O preenchimento desses dados não é obrigatório, mas quando não preenchidos, corre-se o risco de perder o controle do que está sendo gerado.

Quando gerado o Fluxo de Caixa e selecionada a opção de gerar o planejado a partir do previsto, será gerado um novo registro de planejamento a partir das linhas geradas de previsto. O novo registro levará em conta a periodicidade informada, ou seja, cada uma das colunas de período, juntamente com a natureza financeira e centro de custo, irá gerar um novo item no planejamento. O campo Filial dos itens de planejamento não é preenchido já que o fluxo de caixa gerado não tem tal informação. Para que o campo Centro de Custo seja preenchido é necessário marcar a opção "Considerar centro de custo por natureza".

Após gerado o planejado a partir do previsto, basta gerar um novo fluxo de caixa e no campo "Planejamento" buscar o planejamento criado.

**Composição dos saldos iniciais**:

A rastreabilidade da origem do saldo inicial será por conta caixa e separada por "Previsto e Realizado", sendo composto das seguintes linhas:

**Previsto**

Lançamento

Será apresentado por linha o somatório dos lançamentos a receber e a pagar por conta caixa dos lançamentos que estão em aberto no sistema.

Extrato

Será apresentado o somatório dos extratos de caixa (não compensados) para a seguinte operação:

* Depósito de Baixa - somente para as baixa de pagamento com cartão. (Obs.: O Extrato será exibido na Data de Vencimento)

**Realizado**

Conta/Caixa

Será apresentado o saldo na data base de cada conta caixa e o somatório.

Extrato

Será apresentado o somatório dos extratos de caixa (compensados) para as seguintes operações:

* Saque Manual
* Depósito Manual
* Saque Transferência
* Depósito Transferência
* Saque CPMF
* Depósito Canc. CPMF
* [Rendimento Financeiro](https://tdn.totvs.com/x/hl6aHg) - esta operação de extrato de caixa é utilizado por rotina do fiscal e não se trata de rendimento de Aplicação Financeira.
* Depósito de Baixa - somente para as baixa de pagamento com cartão

Baixa

Será apresentado por linha o somatório dos lançamentos a receber e a pagar por conta caixa dos lançamentos que foram baixados ou parcialmente baixados.

* **Gráficos**:

* **Preferências do usuário:**

Se o usuário habilitar a opção de "Salvar os parâmetros utilizados" do Fluxo de Caixa, disponível no menu Utilitários | Usuário | Preferências de Usuário, as configurações utilizadas no último filtro do Novo Fluxo de Caixa ficarão armazenadas e serão carregadas na próxima chamada da funcionalidade.

Configurações

Periodicidade: Define o modo de exibição do Fluxo de Caixa dentro do período estabelecido, podendo ser:

* Diário: exibe no Fluxo de Caixa os valores totais diariamente;
* Semanal: exibe no Fluxo de Caixa os valores totais semanalmente;
* Mensal: exibe no Fluxo de Caixa os valores totais mensalmente;
* Trimestral: exibe no Fluxo de Caixa os valores totais trimestralmente;
* Anual: exibe no Fluxo de Caixa os valores totais anualmente;
* Semestral: exibe no Fluxo de Caixa os valores totais semestralmente;
* Quinzenal: exibe no Fluxo de Caixa os valores totais quinzenalmente;

Observação: 

* Todas as opções disponíveis de periodicidade exibem valores referentes às movimentações realizadas que estiverem classificadas com o Centro de custo e/ou Natureza financeira.

Saldo inicial previsto por naturezas e/ou centros de custo: Ao selecionar esta opção, será considerado o saldo previsto anterior ao período definido do fluxo de caixa. O Saldo Inicial Previsto terá seus valores zerados, pois serão rateados para as naturezas na coluna Previsto do Fluxo de caixa.

Não considerar natureza com valor zerado: Define que, quando marcado, o fluxo de caixa apresentará somente natureza que tenha valor e irá desconsiderar as naturezas cadastradas no sistema que não tenham valor. Quando desmarcado, o fluxo de caixa gerado apresentará todas as naturezas cadastradas no sistema, com ou sem valor atribuído.

Considerar lançamento com conta/caixa vazia: Quando marcado, no fluxo de caixa gerado serão considerados os lançamentos que não tenham conta/caixa informada.

Considerar centro de custo por natureza: Ao selecionar esta opção, serão exibidos no fluxo de caixa os valores por centro de custo de acordo com a natureza financeira. O centro de custo será exibido com as informações: Coligada + Cod. Centro de Custo + Descrição. Quando selecionado, para cada natureza financeira haverá o detalhamento dos centros de custos, demonstrando os valores de forma analítica por centro de custo, totalizando de forma sintética nas respectivas naturezas financeiras (agora tratadas como níveis sintéticos).

Considerar baixa não compensada como previsão: Ao selecionar esta opção, o valor previsto será calculado, considerado os lançamentos baixados com extratos ainda não compensados. Por exemplo, ao baixar um lançamento financeiro sem marcar a opção de "Compensar Extrato", a baixa será realizada e o extrato ficará com o status "Não compensado". Desta forma, se a baixa deste lançamento estiver no período selecionado e o parâmetro marcado, o valor será considerando no campo "Previsto". Se o lançamento estiver baixado e o extrato compensado, o valor será exibido no campo "Realizado", utilizando a data de compensação como referência. 

Considerar apenas código sintético para natureza: Ao selecionar esta opção, serão apresentados somente os códigos sintéticos do Centro de Custo e/ou Natureza Orçamentária Financeira no fluxo de caixa gerado. Quando gerado o fluxo de caixa, com o ou sem a opção marcada, será apresentado um agrupamento das naturezas a partir da natureza de 1° nível, englobando todas as suas naturezas filhas, seja ela analítica ou sintética. Ao gerar o fluxo de caixa com opção marcada, esse agrupamento aparecerá "colapsado" (recolhido), facilitando a visão das naturezas sintéticas de 1° nível, sendo necessário clicar no botão de agrupamento para estender e mostrar as outras naturezas pertencentes a natureza desejada.

Considerar somente os valores previstos na data prevista: Ao selecionar esta opção, o valor previsto será calculado considerando os valores dos lançamentos e extratos na data prevista. Exemplo: um lançamento no valor de R$100,00 com data de vencimento 01/07/2019. Ao emitir o fluxo de caixa com periodicidade diária, o valor deste lançamento somente será considerado para o dia 01/07/2019, não sendo considerado para os dias posteriores. O saldo inicial previsto virá com o valor zerado com este parâmetro marcado.

Considerar saldo final previsto nos períodos posteriores: Este parâmetro controla a exibição de valores do Previsto, seja item ou saldo (Saldo Inicial e Saldo Final). O mesmo reflete nos saldos dos períodos futuros como ocorre para a coluna Realizado.

Considerar saldo inicial conforme a coligada proprietária: Este parâmetro carrega os saldos das contas caixas globais considerando a coligada proprietária, realizando a carga do saldo inicial dos extratos de caixa de tal forma que traga os saldos dos extrato das coligadas selecionadas. 

Considerar valores com rateio incompleto ou sem rateio: Este parâmetro carrega os valores dos lançamentos, extratos e aplicações que não possuem natureza orçamentária e/ou centro de custo cadastrados. Uma linha passa a ser exibida com a informação "Sem Natureza Financeira".

Exibir diferença entre previsto e realizado: Ao selecionar esta opção, será exibida uma nova coluna no fluxo de caixa chamada "Diferença", que se refere a diferença de valores entre as colunas de "Previsto" e "Realizado". O modo como será representado a diferença entre as colunas será com um valor bruto ou com um percentual faltante ou excedente em relação a diferença entre os valores das colunas, que poderá ser selecionado no parâmetro "Modo de Exibição da Diferença".

Modo de Exibição da Diferença: Permite definir o modo de exibição que será utilizado na coluna de "Diferença", contendo as opções: "Valor" e "Percentual".

   Importante: Os parâmetros "Saldo inicial previsto por naturezas e/ou centros de custo" e "Considerar somente os valores previstos no vencimento" não podem ser marcados simultaneamente, ao selecionar um destes o outro fica desabilitado.

Data previsto: Permite definir a data previsto para o cálculo do valor original ou líquido no fluxo de caixa gerado.

* Data de previsão de baixa: Ao selecionar esta opção, o fluxo de caixa irá exibir as informações de registros considerando a data de previsão de baixa informada no lançamento financeiro.
* Data de vencimento: Ao selecionar esta opção, o fluxo de caixa irá exibir as informações de registros considerando a data de vencimento informada no lançamento financeiro.

Valor Previsto: Este parâmetro tem por função definir qual valor será exibido no fluxo de caixa como valor previsto. Sua influência está sobre os lançamentos financeiros, não afetando os valores provenientes de extratos, e aplicações financeiras.

* Valor Original: Será utilizado o valor original, ou seja, o valor  cadastrado na base de dados sem a execução de qualquer cálculo.
* Valor líquido na data atual: Para os lançamentos abertos e parcialmente baixados, será executado o cálculo do valor líquido utilizando como referência a data do dia que está sendo gerado o fluxo de caixa.  
  Como exemplo, vamos supor que estamos gerando um fluxo de caixa na data de  10/05/2019  para o período de   a  com periodicidade diária. Os valores dos lançamentos com vencimento anterior ao dia  serão apresentado com cálculo de juros, multa, etc, e os valores dos lançamentos com vencimento igual ou posterior  a esta data terão os respectivos descontos considerados.
* Valor líquido na data do previsto: Esta opção é dependente do parâmetro Data Previsto**.**Caso a opção selecionada neste parâmetro seja "Data Vencimento", a data utilizada como referência para o cálculo do valor líquido será  a data de vencimento cadastrada no lançamento. Se a opção selecionada for  "Data de Previsão de Baixa", a data de previsão de baixa cadastrada no lançamento será utilizada como referência para o cálculo do valor líquido.

**Observação**: O valor líquido calculado será rateado pelo percentual cadastrado nos rateios do lançamento para ser exibido no fluxo de caixa.

Planejamento: Pode ser selecionado um planejamento para compor os valores planejados do fluxo de caixa gerado de acordo com os itens de planejamento cadastrados.

Filtros

A geração do fluxo de caixa pode ser filtrada por Coligada, Conta Caixa, Filial, Centro de Custo e Naturezas Orçamentárias.

A cada geração do fluxo de caixa, estes parâmetros de filtro poderão ser alterados e um novo fluxo de caixa pode ser gerado de acordo com as alterações realizadas.

**Atenção**

Quando o preenchimento do rateio por centros de custo não for obrigatório (parâmetros do sistema), os lançamentos poderão ser apresentados no fluxo de caixa, mas é importante ressaltar que a opção de filtragem por centro de custo deverá ser desmarcada. Quando marcada, os lançamentos onde o rateio por centro de custo não estiver preenchido serão desconsiderados pelo fluxo de caixa.

Os "Tipos de Documento" que estiverem com a opção [Considerar no Relatório de Fluxo de Caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388695) habilitada e que forem usados nos lançamentos financeiros na geração do fluxo de caixa é que serão considerados para geração do Novo Fluxo de Caixa. Caso a opção acima esteja desabilitada, não serão considerados os lançamentos na geração.

**Lista conta/caixa inativa:**Este parâmetro define se serão listadas as contas/caixa inativas nos filtros para seleção no fluxo de caixa. Ao marcar ou desmarcar esta opção, a função de atualizar os filtros é executada automaticamente. 

                                                

**Observação: As coligadas que aparecem no filtro seguem as permissões do perfil associado ao usuário em cada coligada para o módulo 'Gestão Financeira'.**

Podendo ser restrito de duas formas:

* Removendo todos os perfis que tem acesso ao Fluxo de Caixa para uma coligada:

* Atribuindo um perfil que não tem acesso ao Fluxo de Caixa:

**Exemplo**: Caso estejam marcadas apenas as coligadas 6 e 7, o usuário deve visualizar apenas os dados das coligadas 0 (Global), 6 e 7.

Dados

Nessa aba, serão apresentados os dados dos Lançamentos Financeiros, Extratos de Caixa e Aplicações Financeiras com as seguintes Informações:

Coligada que poderá ser de lançamento, extrato de caixa ou aplicação financeira.

Referência que poderá ser de lançamento (IDLAN), extrato de caixa (ID) ou de aplicação financeira.

Valor que poderá ser de lançamento, da aplicação financeiro ou extrato de caixa.

Valor Baixado/Compensado que poderá ser de lançamento ou extrato de caixa.

Data de Vencimento que será a do lançamento.

Data baixa/Compensação que poderá ser de lançamento e/ou de extrato de caixa.

Histórico que será de lançamento.

Nome/Razão Social que será do cliente/fornecedor do lançamento.

Nome Fantasia do Cliente/Fornecedor que será do cliente/fornecedor do lançamento.

**Exportar dados:**Para facilitar a conferência/auditoria das informações financeiras do Fluxo de caixa, é possível exportar a lista de Lançamentos Financeiros a pagar e a receber, além dos extratos de caixa de movimentações financeiras. Para isso, clique na aba 'Dados' e posteriormente basta clicar com botão direito do mouse. Em seguida, clique na opção "Exportar dados" e  selecione o local que deseja salvar e o nome do arquivo. Por fim, clique em 'Salvar'. Confira abaixo uma demonstração do processo.

**Observação:**

* No caso da "Aplicação Financeira", será apresentado na aba "Dados" o campo "Referência da Aplicação", assim como valor do saldo da aplicação na sua data de vencimento. Para exemplificar, quando o vencimento da aplicação for em 31/12/2020, o sistema fará o cálculo até essa data (independente da data corrente) para apresentar o saldo.

         

Simulação

O Fluxo de Caixa disponibiliza a Simulação sobre a planilha que permite a digitação dos valores nos campos recalculando automaticamente os totalizadores.

Previsto

**Previsto:** É a soma do valor do rateio de Centro de Custo dos lançamentos em aberto mais a soma do valor em aberto para os lançamentos Baixado Parcialmente:

* Aplicando os filtros de conta caixa, centro de custo e período;
* Lançamentos com status “Em aberto” ou “Baixado parcialmente”;
* Lançamentos diferentes de faturado;
* Lançamentos com o tipo baixa pendente diferente de 'Bloqueado pela confissão de dívida';
* Lançamentos que possuem Natureza Financeira;
* Lançamentos com classificação diferente de “Parcialmente Adiantado”;

Saldo disponível das Aplicações financeiras com vencimento entre o período informado e saldo diferente de zero;

Extrato de caixa manuais:

* Aplicando os filtros de conta caixa, centro de custo;
* Não compensados;
* Tipo Saque manual, Deposito manual, Saque transferência, Deposito transferência, Saque CPMF e Dep. Canc CPMF.

**Composição dos valores previstos considerando retenções de tributos na emissão**

O pagamento das retenções é uma obrigação prevista, e como tal, é necessário que componha o fluxo de caixa.

Na configuração de geração do Fluxo de caixa, quando a opção "Valor Previsto" for marcada como "Valor Original", o valor apresentado na coluna "Previsto" será composto pelo valor original do(s) lançamento(s) subtraído dos valores das retenções.  
Exemplo:

* Marcação:

* Valor original do lançamento e valores retidos na emissão:

* Fluxo de Caixa gerado:

* O valor apresentado na coluna "Previsto" é composto do valor original do lançamento (R$3.000,00) subtraído do valor das retenções (R$106,92 + R$330,00) formando o valor real de R$2.563,08.

**Observação**:

* Impostos tratados como valores opcionais não serão destacados.
* Impostos tratados INSS PF e IRRF PF/PJ.
* Lançamento de INSS do Empregador não será subtraído do valor original, pois se trata de retenção devida do empregador.

**Composição dos valores previstos considerando retenção de tributos na baixa**

O tributo cuja geração ocorre no momento da baixa: Contribuições Sociais (PIS-RF, COFINS-RF, CSLL-RF, CS-RF), IRPF e IRPJ (estes dois últimos condicionado à configuração da Data de Geração na configuração por coligada), o fluxo de caixa irá tratar o valor previsto, quando originado a partir do Valor Original, descontados dos respectivos valores dos tributos.

* Marcação

* Valor original do lançamento e valores retidos na emissão:

* Fluxo de Caixa Gerado

* O valor apresentado na coluna "Previsto" em janeiro é composto do valor original do lançamento (R$10.000,00) subtraído do valor das retenções (R$500,00 e R$465,00), formando o valor real de R$9.035,00. Por outro lado, o valor apresentado na coluna "Previsto" em fevereiro corresponde à previsão de pagamento dos tributos. Vale observar que trata-se de valores previstos, caso o pagamento do lançamento ocorra na data de vencimento estipulada, desconsiderando eventuais efeitos de cumulatividade, que podem ocorrer no momento da baixa.

**Saldo Inicial Previsto:** Soma do valor original (Receber – Pagar) dos lançamentos com data de vencimento menor que a data inicial do período;

* Lançamentos com status “Em aberto” ou “Baixado parcialmente”;
* Lançamentos diferentes de faturado;
* Lançamentos que possuem natureza financeira;
* Lançamentos com classificação diferente de “Parcialmente Adiantado”.

Realizado

**Realizados:** É a soma do valor do rateio de centro de custo baixado:

* Aplicando os filtros de conta caixa, centro de custo e período;
* Lançamento Baixados;
* Lançamentos que possui natureza financeira;
* Lançamentos com classificação diferente de “Parcialmente Adiantado”;
* Lançamentos baixado por Acordo não são considerados;

Extratos de caixa manuais:

* Aplicando os filtros de conta caixa e centro de custo;
* Extratos compensado;
* Extratos do tipo saque manual, deposito manual, saque transferência, deposito transferência, saque CPMF e Dep. Canc. CPMF;
* Extratos que não possuem lançamento vinculado;
* Extratos que possuem Natureza Financeira;

**Saldo Inicial Realizado:** É a soma do valor do rateio de centro de custo baixado (Receber – Pagar) dos lançamentos baixado com data de baixa menor que a data inicial do período:

* Lançamento Baixados e baixado parcialmente;
* Lançamentos que possui natureza financeira;
* Lançamentos com classificação diferente de “Parcialmente Adiantado”;
* Lançamentos baixado por acordo não são considerados;

Saldo data base da conta caixa;

* Data base conta caixa menor que a data do termino do período informado.

Soma dos Extratos de caixa manuais;

* Aplicando os filtros de conta caixa e centro de custo;
* Extratos compensado;
* Extratos do tipo saque manual, deposito manual, saque transferência, deposito transferência, saque CPMF e Dep. Canc. CPMF;
* Extratos com data de compensação menor que a data inicial do período;
* Extratos que não possuem lançamento vinculado;
* Lançamentos que possuem natureza financeira;

O Saldo Inicial Realizado é composto pelo Saldo Final Realizado do período anterior. Caso o parâmetro "Saldo inicial previsto por naturezas e/ou centros de custo" esteja selecionado, os valores do Saldo Inicial Realizado poderão sofrer alterações por filtrarem valores fora do período informado no processo.

Caso o extrato da baixa esteja como ***Compensado***, a data utilizada no filtro será a data de compensação do extrato, e não a data de baixa.

Planejado

**Planejado:** É a soma do valor dos itens do planejamento selecionado agrupado em cada um dos períodos de acordo com a periodicidade.

Os itens de planejamento que não tenham o campo Filial preenchido também serão considerados. Já os registros com o campo Centro de Custo em branco serão selecionados somente se a opção "Considerar centro de custo por natureza" desmarcada e no filtro por centro de custo todos os registros estão marcados. O filtro por natureza orçamentária sempre será aplicado para carregar os itens de planejamento considerados para cálculo do valor.

O Saldo Inicial Planejado é composto pelo Saldo Inicial Realizado. Nos períodos de meses posteriores ele será composto pelo Saldo Final Planejado do mês anterior.

Prev. + Real. (Somatório de valores)

**Prev. + Real.:** É o somatório dos valores dos itens previstos e realizados.

Previsto/Realizado

**Exemplo:**

Na exibição dos valores no fluxo de caixa, o saldo Inicial só será preenchido com valores que não são apresentados nas linhas, ou seja, dentro do período informado. Os valores previstos de linha, das naturezas que estão dentro do período, não serão repassados para o saldo inicial dos próximos períodos, facilitando assim o discernimento de valores na apresentação do relatório.

Criado lançamento a receber de valor 100,00 no dia 12/09/2018. Criado um lançamento a receber de valor 100,00 no dia 13/09/2018. Baixado um lançamento a receber no valor 100,66 no dia 14/08/2018.

A partir dessas informações, perceba que ao gerar o relatório no período do dia 12/09/2018 até 16/09/2018,  poderemos visualiza-lo da com o seguinte resultado:

* O valor 100,00 constará de uma operação do dia 12/09/2018 e que resulta então, no saldo final de 100,00, para este dia.
* O saldo final do dia 12/09, não será repassado para o saldo inicial do dia 13/09. O valor de 200,00 já contará em seu valor **previsto**.
* O valor de 100,66 será representado de forma diferente dos valores previstos, no exemplo acima, por constar somente o saldo **realizado** daquela data em questão, no dia 14/09/2018.

Desta forma, o valor final é sempre reexibido no saldo inicial do próximo dia, 15/09/2018.

 Informações Complementares

* DT - P[lanejamento do Fluxo de Caixa](http://tdn.totvs.com/display/LRM/DT+Planejamento+do+Fluxo+de+Caixa#Cadastros-613304763)
* [DT - Novo Fluxo de Caixa](https://tdn.totvs.com/x/FiXvH)
