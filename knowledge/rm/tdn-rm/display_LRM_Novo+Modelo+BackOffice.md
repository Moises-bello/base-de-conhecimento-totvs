---
content_hash: b3df97b3a633211d0cbbd21cb73d104690ed9d79b26c7faab1be377db45260eb
fetched_at: '2026-06-29T00:09:24.538155+00:00'
page_id: '423937945'
product: rm
source: tdn-rm
title: Novo Modelo BackOffice
type: documentation
url: https://tdn.totvs.com/display/LRM/Novo+Modelo+BackOffice
version: 19
---

Estas funcionalidades só estão disponíveis para as bases já migradas para o Novo Modelo do BackOffice. Citamos como principais processos migrados:

* Movimento .NET;
* Faturamento Parcial;
* Conclusão de Movimento;
* Tabela de Preço.

***Observação***: Ao acessar o aplicativo neste novo modelo, na barra de título estará identificada como Novo Modelo do Backoffice.

Se você ainda não conhece as novidades do Novo Modelo do BackOffice, não perca tempo! Acesse o portal do cliente ([www.totvs.com/suporte](http://www.totvs.com/suporte)) e faça download do documento 'Novo Modelo BackOffice.rar'.

* **Lançamento Financeiro por Item**

1
incomplete
Implementado o processo de geração de lançamentos financeiros por item. Este processo permite ao usuário gerar lançamentos financeiros personalizados que poderão ser informados manualmente ou automaticamente, usando a data de entrega do item do movimento como base para o vencimento dos lançamentos financeiros a serem gerados.

2
incomplete
Implementada rotina de faturamento/cancelamento automáticos de movimentos relacionados ao processo de aprovação por workflow. A partir desta versão, será possível o Faturamento/Cancelamento automáticos de Movimentos relacionados a Atendimentos do processo de Aprovação por WorkFlow diretamente no TOTVS Gestão de Relacionamento com o Cliente. Desta forma, o processo torna-se autônomo e transparente ao Usuário 'aprovador', agilizando os processos e aumentando a eficiência rotina de Aprovação.

***Observação***: Para o correto funcionamento, existem parametrizações a serem feitas no sistema TOTVS Gestão de Relacionamento com os Clientes. Para isto, deve ser consultado o documento 'Como Fazer' desta rotina para orientações de parametrizações dos sistemas para o devido funcionamento.

* **Função de Fórmula: TABMOVRELACPEDIDO e TABITMRELACPEDIDO**

Criada a função de fórmula TABMOVRELACPEDIDO E TABITMRELACPEDIDO que tem como finalidade buscar informações referentes aos dados informados no movimento de origem. Esta fórmula deverá ser cadastrada no movimento de destino onde se deseja fazer tal consistência.

* **Cadastro de Tabela de Preços por Produto**

Disponível no sistema o cadastro de várias tabelas de preços de produtos, sendo suas atualizações baseadas em critérios pre-definidos conforme regras de negócio de cada cliente, tendo ainda vinculação com Filial, Cliente/Fornecedor, Condição de pagamento, Representante, Estado e Município.

* **Conclusão de Pedido**

Com a migração do movimento para .NET, foi criado um novo processo, "Conclusão de Pedido", que terá como finalidade a finalização de um ou mais pedidos que tenham sido faturados parcialmente e que não serão mais faturados. Este novo processo será criado pois não haverá mais movimento desdobrados.

* **Alteração de dados dos lançamentos financeiros através do TOTVS Gestão de Estoque, Compras e Faturamento**

A partir desta versão, os lançamentos financeiros gerados no RM Fluxus através da inclusão de movimentos do RM Nucleus, poderão ser editados; com isto alguns campos do lançamento poderão sofrer alterações no momento da inclusão do movimento.

* **Tabelas de Orçamento**

Implementado a partir desta versão, no processo do controle orçamentário, dois novos cadastros: Grupo Orçamentário sendo uma tabela intermediária entre o Centro de Custo e a Natureza Orçamentária/Financeira que defini um agrupamento dos valores orçados e a tabela de Classificação dos Períodos onde ao criar Períodos de Orçamentos com periodicidades coincidentes, poderemos classificar estes períodos com uma forma diferenciada.

* **Assistente de Cópia de Movimentos**

A partir desta versão, o Assistente de Cópia de Movimentos por Referência vem com algumas novidades; dentre elas um design inovador e mais intuitivo, conta também com funcionalidades mais aprimoradas, como a pesquisa pelos movimentos que serão referenciados, já que permite o Usuário criar um filtro com o critério desejado, sem induzir a utilização somente de determinados campos de pesquisa. Com isto, as pesquisas por movimentos poderão ser mais criteriosas, tornando a rotina mais simples e ágil.

* **Aprovação de Movimentos**

Nesta versão, o processo de Aprovação de Movimentos passa a ser mais intuitivo e ter um design inovador. Assim, além do processo ter sido revisado, foram aprimoradas algumas funcionalidades, como a utilização do processo de Aprovação por 'Tolerância no Recebimento', que apresenta, na mesma tela de Aprovação, a rotina de 'Desaprovação', que identificará quais os Itens estão 'Aprovados' para que sejam 'Desaprovados'. Utilizando este tipo de Aprovação, a rotina de Desaprovação, do Menu Movimentos, passa a não ter usabilidade, já que a rotina de Aprovação funciona para as duas rotinas.

* **Inativar eventos contábeis**

A partir desta versão ao migrar a base de dados para o novo modelo contábil e de faturamento - Back office - alguns eventos contábeis poderão apresentar inconsistências em relação a parametrização dos Itens do Evento Contábil aplicado em: Movimento, item, em relação aos Itens Gerenciais aplicado em: Rateio de C.Custo Mov ou Item, Lançamento entre outros. Neste caso, os eventos contábeis que apresentarem tais inconsistências serão inativados. Para ativá-los o usuário deverá acessar os eventos inativos e reajustar as validações citadas acima.

* **Conversor de Dados para Faturamento Parcial**

A partir desta versão será disponibilizado em Utilitários o Processo de Conversão de Dados para Faturamento Parcial que visa auxiliar o usuário na decisão de modificar o conteúdo de determinadas Consultas SQL, Relatórios e Fórmulas baseados no novo conceito do Faturamento Parcial e também possibilita a atualização de Filtros de Movimentos, Filtros de Relatórios e Filtros de Usuários de acordo com este novo conceito.

* **Corrigir Movimentos**

A rotina de correção de movimentos foi migrada e estará disponível nesta versão. Caso o usuário tenha a necessidade de, após gerarem movimentações no sistema, alterar alguns dados referentes à Inserção ou Exclusão de tributos, alteração do conteúdo da fórmula da base de cálculo ou Alíquota dos tributos associados aos parâmetros do tipo de movimento que foram gerados os respectivos movimentos, poderão fazer através desta opção.

* **Produto Substituto**

É possível fazer a troca do produto originalmente informado no movimento pelo seu substituto ou Similar. Para tal, será necessário informar previamente no cadastro do produto os seus substitutos ou similares através do anexo "Produto Substituto/ Similar", e nos parâmetros do tipo de movimento informar o tipo de tratamento que será utilizado no movimento: Similar, Substituto ou Ambos.

* **Implementada a cópia do campo TMOV.NORDEM nos processos de cópia de movimentos**

Ao efetuar uma Cópia de Movimentos por Referência ou a geração de movimentos a partir de um movimento selecionado, o TOTVS Gestão de Estoques, Compras e Faturamento passa a copiar o campo NORDEM (Nº no Cliente) para os movimentos gerados.

* **Filtro de números de série na edição de itens de movimento**

O sistema permite a utilização de filtros para pesquisa de Números de Séries a serem utilizados no Item de Movimento. Com isto, o sistema fica mais dinâmico na pesquisa e agiliza a informação dos dados dos Itens de Movimento. Os campos Lote e Data de Fabricação podem ser pesquisados, além do campo de Número de Série.

* **Melhoria no processo de Gerar, Excluir e Estornar Contabilidade pela visão de movimentos.**

O sistema passa a executar a rotina de Geração, Exclusão e Estorno de Contabilização de Movimentos como um processo, mostrando log de cada movimento, sem depender que todos os movimentos sejam contabilizados para que o processo seja finalizado.

* **Implementado o recurso de filtro por status do Produto (Ativo/Inativo) na consulta de saldos e custos.**

O sistema passa a permitir que o Usuário possa efetuar um filtro, na consulta de saldos e custos, para a identificação de Produtos inativos, evitando perda de tempo na análise de informações dos produtos que não mais são movimentados pela empresa.

* **Contabilização de movimentos 'Offline', com possibilidade de agendamento**

O sistema passa a contar com o processo de agendamento de Contabilização de movimentos quando a contabilização está definida como 'offline', facilitando no processo de execução da contabilização dos movimentos. Desta forma, poderá garantir que a contabilização de movimentos ocorra em um período em que a utilização do sistema é alta, evitando a queda de performance na execução de outras rotinas no sistema.

* **Geração do INSS pessoa física**

Foram realizadas alterações para permitir que, ao se configurar a fórmula para valor de serviço, o TOTVS Gestão de Estoque, Compras e Faturamento permita incluir itens de movimento (servições e/ou produtos) com deduções (sempre a mesma alíquota) ou sem deduções (nenhuma alíquota).

Essa implementação permite que seja identificado o total do valor de serviço do movimento e que o mesmo seja rateado nos lançamentos financeiros gerados pelo TOTVS Gestão Financeira. Caso a fórmula do valor de serviço não seja parametrizada, o sistema atuará da forma anterior, ou seja, impedindo a inclusão de itens de movimento com diferentes deduções (produtos ou serviços) e gerando o valor de serviço no financeiro com o valor original da parcela.

* **Implementado o recurso de 'Agendar Financeiro' por períodos.**

Foi disponibilizado o recurso de agendamento do Financeiro, com a utilização da execução de JobServer em ambiente 3 camadas. Desta forma, o processo de execução do Financeiro poderá ser executado em datas e horários específicos, conforme necessidade do Usuário.

* **Implementada a gravação da informação no campo 'Seleção de Preço' no item de movimento.**

O sistema passa a armazenar a informação selecionada no campo 'Seleção de Preço' do Item de Movimento. Desta forma, o sistema passará a identificar qual foi o preço selecionado no Item de Movimento para controle das informações, mantendo o histórico da origem do preço do Item de Movimento.

* **Disponibilidade do recurso de ordenação de Campos Complementares**

Com este recurso, o Usuário tem a possibilidade de ordenar a apresentação dos Campos Complementares dentro da edição do Item/Movimento, com total flexibilidade, fazendo com que as informações sejam apresentadas de forma coesa com o processo do sistema.

* **Implementado o recurso de visualização de consultas SQL como anexo de visões.**

O sistema permite que o Usuário configure uma Consulta SQL como Anexo da Visão de Movimentos, podendo, inclusive, retornar informações presentes nos Itens de Movimento. Com isto, a verificação rápida de dados dos Itens de Movimentos passa a ser possível, aumentando a eficiência na consulta de dados relacionados aos Movimentos.

* **Melhorado o processo de cópia de movimentos por referência, com a opção para eliminar os movimentos que não possuem Itens para devolução**

Ao efetuar a Cópia por Referência, o sistema permite que, após filtrar os movimentos que se deseja copiar, sejam excluídos os movimentos que não possuem Itens pendentes para Devolução.

* **Implementado o cálculo de peso bruto e peso líquido do movimento através de fórmulas**

A partir desta versão, o sistema permite que o Usuário defina uma fórmula para o cálculo de Peso Bruto e Peso Líquido, de acordo com as informações dos Itens de Movimento.

* **Implementada a utilização da data de entrega do item de movimento como data default do orçamento**

O sistema passa a permitir a utilização da Data de Entrega do Item como Data default para o Controle Orçamentário, diversificando as informações de controle da rotina de Orçamento.

* **Consulta de naturezas de operação dentro das movimentações**

Com a migração de movimentos para a nova tecnologia, a pesquisa no cadastro de Naturezas ocorre de modo diferente do processo anterior, permitindo uma maior interatividade entre o Usuário e o sistema, inclusive com a pesquisa rápida sem a necessidade de navegar no cadastro de Naturezas de Operação.

* **Consulta de Movimentos**

A partir desta versão, a visão de Movimentos passa a contar com os novos recursos tecnológicos da TOTVS. Assim, o sistema permite uma maior interação do Usuário com o sistema, com a criação de filtros mais dinâmicos e intuitivos, agrupamentos por campos desejados, utilização de Consultas SQL e Gráficos como anexos da visão, entre muitos outros.

* **Novas Funções de Fórmula**

Criadas funções de fórmula EXISTERELACMOVIMENTO, EXISTERELACITEM, TABITMRELACPED e TABMOVRELACPED para consistir valores do movimento e dos itens de movimento de origem com o de destino.

* **Alteração de campos após gerar ordem de produção no TOTVS  Planejamento e Controle da Produção**

Após gerar a ordem de produção no TOTVS Planejamento e Controle da Produção, aparecerá a seguinte mensagem de consistência para os campos que não são passíveis de alteração após OP criada: "Item já programado pelo módulo de Produção não pode ser alterado".

Os campos que não poderão ser alterados são os seguintes:

3
incomplete
Sequencial do Item

4
incomplete
Local de Estoque (Do movimento e do item)

5
incomplete
Filial (Do movimento e do item)

6
incomplete
Data de Emissão

7
incomplete
Data de Saída

8
incomplete
Data de Programação

9
incomplete
Centro de Custo

10
incomplete
Unidade de medida do produto

11
incomplete
Lotes (Validade, data de entrada e fabricação de lote)

12
incomplete
Números de série

13
incomplete
Grade - Item de grade

14
incomplete
IDPRD (O produto não pode ser alterado nem excluído)

15
incomplete
Quantidade

16
incomplete
Todos os demais campos poderão ser alterados após ordem de produção criada.

* **Inclusão de números de série no movimento**

O sistema, desde que parametrizado para "Aceitar Números de Série", ao incluir um movimento com um produto que os utilize, somente irá aparecer na grid os números de série que ainda não foram utilizados.

* **Filtros para número de série e lote na visão do movimento**

O sistema agora possui a funcionalidade de filtrar os números de série e lotes pela validade, de modo que não apareçam aqueles já vencidos.

* **Cópia dos dados da aba importação no movimento ao utilizar natureza de operação igual a 3 ou 7**

Ao executar os processos de cópia simples, cópia por referência ou faturamento, os dados da aba importação ao utilizar natureza de operação igual a 3 ou 7, serão copiados.

* **Ordenação por colunas através da grid dos itens de movimento**

A partir de agora, na grid dos itens de movimento, será possível realizar a ordenação dos mesmos através das colunas visíveis. Esta melhoria facilita a busca e ordenação dos itens da forma mais adequada ao usuário.

* **Faturamento de movimentos sem dados de orçamento**

Otimizado a rotina de faturamento para que movimentos sem dados de orçamento, feitos anteriormente a parametrização do movimento sejam impedidos de serem faturados.

* **Parametrização de NF-e**

O parâmetro "NF-e Estadual"  do tipo de movimento agora será visível nas seguintes condições:

17
incomplete
Tipos de Movimentos '2.2.XX' ou,

18
incomplete
Tipos de Movimentos '3.1.XX' ou,

19
incomplete
Motivo referencia for Devolução de venda (Valor = 5) ou,

20
incomplete
Motivo referencia for Devolução de Compra (Valor = 4) ou,

21
incomplete
Tipos de movimentos '1.2' e emitente e destinatário como "Empresa".

* **Atualização na visão de movimentos**

O campo "Razão Social" da visão de movimentos foi alterado para "Nome Fantasia Cli/for" para ficar igual ao mesmo campo no TOTVS Gestão Financeira. A padronização irá facilitar a criação de filtros evitando confusão entre nomes diferentes.

* **Associar um conhecimento de transporte à uma NF**

Com a migração do movimento, foi criado um filtro para a associação dos conhecimentos de transporte. O recurso agilizará o processo de emissão do conhecimento de transportes.

* **Número de Lote de e Série**

Para os movimentos que utilizam lote e série passam a consistir o número de itens para o lote e o número de séries vinculados no movimento.

* **Dados de importação no movimento e no item**

Melhoria realizada no envio de dados de importação do movimento nas rotinas de cópia e recebimento.

* **Itens de movimentos - ordenação por colunas**

Na grid dos itens de movimento será possível realizar a ordenação dos mesmos através das colunas visiveis. Esta melhoria facilita a busca e ordenação dos itens da forma mais adequada ao usuário

* **Alteração no calculo dos tributos do movimento**

Alterada a forma como é feito o calculo dos tributos. Antes o calculo era feito item por item, agora o calculo será feito somando todos os itens que tenha a mesma alíquota e que seja da mesma natureza fiscal.

* **Defaults Contábeis**

A partir de agora é possível buscar o default contábil para cliente/Fornecedor de Origem/destino

* Outras Atualizações:

22
incomplete
Atualização no processo de cópia por referência de movimentos que utilizam funcionários 1 e 2;

23
incomplete
Inclusão de rateio utilizando fórmulas no movimento;

24
incomplete
É possível inserir fórmulas para calcular o rateio do item de movimento e do movimento ao selecionar o tipo "Valor" para os rateios de centro de custo e departamento;

25
incomplete
Atualização realizada no envio de dados de importação do movimento nas rotinas de cópia e recebimento;

26
incomplete
Atualização na performance do movimento, ajustes realizados nas rotinas utilizadas pelo sistema para inclusão de movimentos no novo modelo Back-Office.

* **Cancelamento de Movimentos**

Disponibilizado o processo de Cancelamento de Movimentos na nova arquitetura dos sistemas na linha RM da TOTVS.

* **Números de Série**

A partir desta versão, com a migração do movimento para a plataforma .NET será possível filtrar os números de série que se deseja, por Número de série, lote e data de fabricação.

* **Associar CTRC ao Movimento**

A partir dessa versão é possível ordenar as colunas ou procurar por um campo específico do movimento que se deseja associar ao CTRC

* **Desconto em todos os itens do movimento**

Para utilizar este processo, deve-se clicar com o botão direito do mouse em cima da Grid de itens de movimento e escolher dentre as opções de Desconto: se por Produtos, Serviços ou Ambos, se por Percentual ou Valor e qual será o desconto. O sistema estará aplicando o valor para todos os itens, independente do item possuir desconto previamente ou não. Se o item já possuir desconto, este valor deverá ser SUBSTITUIDO pelo novo.

* **Desmembramento de Produto Composto**

Realizada melhoria no desmembramento de produtos compostos nos casos em que o movimento está parametrizado para utilizar integração com Projetos e foram informados projeto e tarefa no item de movimento.

* **Fórmula do rateio por valor{ }**

Melhoria realizada no rateio por centro de custo e departamento, quando os mesmos utilizam fórmulas para calculo do valor total do rateio.

* **Fórmula para rateio do movimento e item de movimento**

Implementado o recurso de fórmula para os rateios por valor do Departamento e Centro de Custo. Ao informar a fórmula o sistema estará consistindo o rateio de acordo com a fórmula informada.

* **Parametrização da data de cotação da moeda no movimento de origem**

Criação do parâmetros Data Base em Mov - Valores Financeiros para o tipo de movimento de origem onde é possível informar a data da cotação da moeda para que seja feita a conversão durante o faturamento.

* **Não manter histórico do pedido**

Com o parâmetro "Não Manter Histórico do Pedido" marcado, o sistema não cria o log do faturamento no movimento de origem .

* **Geração de contabilidade de lançamentos financeiros Através do TOTVS Gestão de Estoque, Compras e Faturamento**

A partir desta versão, o TOTVS Gestão de Estoque, Compras e Faturamento poderá executar a contabilidade de lançamentos financeiros, vinculados aos movimentos, mesmo quando a contabilização do lançamento financeiro for parametrizada, no Evento Contábil, para ser executada por fórmulas. Com isto, a contabilidade dos lançamentos vinculados aos movimentos poderá efetuar o mesmo processo contábil executado diretamente no TOTVS Gestão Financeira, aumentando a usabilidade do recurso e melhorando a integração com o sistema financeiro.

* **Integração TOTVS Gestão de Estoque, Compras e Faturamento X TOTVS Educacional**

Quaisquer movimentos gerados pelos módulos do RM Classis: Básico, Superior e NET não poderão ser alterados, cancelados ou excluídos pelo RM Nucleus.

* **Melhoria realizada no processo de cópia de movimentos por referência.**

Na migração do processo de cópia por referência serão copiados apenas os dados parametrizados no movimento de destino. Dados não parametrizados não serão salvos no Banco de dados, e caso haja algum campo default no movimento de destino este deverá ser respeitado e não será sobrescrito.

* **Novas variáveis para o complemento de histórico financeiro**

As seguintes variáveis estão disponíveis para o Complemento de Histórico Financeiro:

27
incomplete
\[NUM\] para o Número do Documento

28
incomplete
\[HIS\] para o Histórico

29
incomplete
\[SER\] para a Série

30
incomplete
\[EMI\] para a Data de Emissão

31
incomplete
\[ORD\] para o Número da Ordem

32
incomplete
\[NOM\] para o Nome Fantasia do Cli/For

33
incomplete
\[RAZ\] para a Razão Social do Cliente/Fornecedor

34
incomplete
\[OBS\] para Observação do Movimento

35
incomplete
\[TDO\] - Código do Tipo de Documento

36
incomplete
\[DTD\] - Descrição do tipo de Documento

37
incomplete
\[CTT1\] - Código da tabela de classificação 1 do faturamento

38
incomplete
\[CTT2\] - Código da tabela de classificação 2 do faturamento

39
incomplete
\[CTT3\] - Código da tabela de classificação 3 do faturamento

40
incomplete
\[CTT4\] - Código da tabela de classificação 4 do faturamento

41
incomplete
\[CTT5\] - Código da tabela de classificação 5 do faturamento

42
incomplete
\[DTT1\] - Descrição da tabela de classificação 1 do faturamento

43
incomplete
\[DTT2\] - Descrição da tabela de classificação 2 do faturamento

44
incomplete
\[DTT3\] - Descrição da tabela de classificação 3 do faturamento

45
incomplete
\[DTT4\] - Descrição da tabela de classificação 4 do faturamento

46
incomplete
\[DTT5\] - Descrição da tabela de classificação 5 do faturamento

47
incomplete
\[CTF1\] - Código da tabela de classificação 1 do financeiro

48
incomplete
\[CTF2\] - Código da tabela de classificação 2 do financeiro

49
incomplete
\[CTF3\] - Código da tabela de classificação 3 do financeiro

50
incomplete
\[CTF4\] - Código da tabela de classificação 4 do financeiro

51
incomplete
\[CTF5\] - Código da tabela de classificação 5 do financeiro

52
incomplete
\[DTF1\] - Descrição da tabela de classificação 1 do financeiro

53
incomplete
\[DTF2\] - Descrição da tabela de classificação 2 do financeiro

54
incomplete
\[DTF3\] - Descrição da tabela de classificação 3 do financeiro

55
incomplete
\[DTF4\] - Descrição da tabela de classificação 4 do financeiro

56
incomplete
\[DTF5\] - Descrição da tabela de classificação 5 do financeiro

* **Processo referente ao estoque DE/COM terceiros**

Tratar estoque em poder de terceiros com custo por filial.

Permitir transferência entre estoque de/com terceiros.

Cancelar/excluir automaticamente movimentos adicionais do processo de retorno de industrialização gerados automaticamente quando movimento de retorno for cancelado/excluído.

* **Realocação Orçamentária**

Os movimentos que sofreram uma Realocação Orçamentária passam a respeitar algumas regras quando são alterados. Caso alguma regra seja violada, o movimento volta ao status "Bloqueado" e a realocação deve ser feita novamente. Alguns campos que regem esta regra: Quantidade, Data Orçamento, Código da Tabela do Orçamento, Centro de Custo, Rateios do item e movimento.

* **Movimento - associar CTRC**

A partir dessa versão é possível ordenar as colunas ou procurar por um campo específico do movimento que se deseja associar ao CTRC.

* **Implementados novos relatórios do modelo Backoffice**

A partir da versão intermediária 10.80.1 do TOTVS Gestão de Estoques, Compras e Faturamento, novos relatórios foram produzidos para atender as necessidades deste novo modelo, conforme podem ser vistos na lista abaixo:

57
incomplete
01.03.001 - Rastreia Movimento.rrmx: Relatório de Rastreamento que exibe toda a árvore para saber qual é a origem e/ou destino que foi gerado.

58
incomplete
01.03.002 - Quantidade Pedida X Recebida.rrmx: Relatório de quantidade pedida e recebida, esse relatório trará a quantidade dos itens que foram solicitados em um pedido e o que foi atendido. Para isso será necessário buscar a quantidade do movimento de origem e a quantidade do movimento de destino.

59
incomplete
01.03.003 - Pedidos Pendentes.rrmx: Relatórios de pedidos pendentes considerando status do movimento A e G.

60
incomplete
01.03.004 - Relatório de Quantidade por Status: Teremos os dois campos de quantidade, Quantidade e Quantidade Total.

61
incomplete
01.03.005 - Relatório de quantidades, esse relatório trará a Quantidade Total (desconsiderando o faturamento parcial).

***Observação***: Estes novos relatórios devem ser importados no novo modelo do Gerador de Relatórios - Gerador .NET.
