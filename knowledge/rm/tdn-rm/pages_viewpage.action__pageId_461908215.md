---
content_hash: bcfeda32010f6fce5367278673bba269fb1343fe241a0ec0f529aaf7ad81faac
fetched_at: '2026-06-29T00:10:14.554557+00:00'
page_id: '461908215'
product: rm
source: tdn-rm
title: 11.40.0 (Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461908215
version: 10
---

**Central de Compras**

Implementado a partir desta versão o processo Central de Compras. A Central de Compras é um recurso onde é possível cotar solicitações de N coligadas diferentes e gerar as ordens de compras para suas respectivas coligadas. Uma coligada parametrizada como Central de Compras poderá realizar cotações para todas as coligadas definidas como Participante de Central de compras da mesma. Assim, acessando o cadastro de Cotação, será possível selecionar as coligadas que serão cotadas, os tipos de movimentos de solicitação de compras, os produtos, os fornecedores, realizar o processo de Cotação e gerar as ordens de compras para todas as coligadas que estarão participando do processo.

**Produto Global**

Implementado a partir desta versão um novo conceito para o cadastro de produto na linha RM, Produto Global. Este recurso consiste em compartilhar o mesmo cadastro de produto com mais de uma coligada, desta forma não será mais necessário replicar o cadastro de produto entre coligadas. As informações comuns para todas as coligadas serão armazenadas em uma única tabela(TPRODUTO) visível a todas coligadas. O produto terá um único identificador (IDPRD) para todas as coligadas. Já as informações específicas de cada coligada serão armazenadas em outra tabela (TPRODUTODEF), e somente serão visualizadas na coligada corrente. Atenção ! A parametrização é opcional, mas também irreversível.

**Gestão de Compras – Cotação**

Dando continuidade ao processo de migração do produto TOTVS Gestão de Estoques, Compras e Faturamento informamos que a partir desta versão o processo de cotação passa a ter uma interface mais intuitiva, com um design inovador e algumas funcionalidades aprimoradas aumentando assim a eficiência e agilidade do processo de cotação dentro da gestão de compras.

**Rateio de Tarefa**

Implementado a partir desta versão um novo conceito para o Rateio na linha RM, Rateio de Tarefa. Consiste em um processo de integração com RM Solum, onde será possível associar um projeto e uma respectiva tarefa a cada centro de custo presente no rateio do item/movimento. Será possível ter no rateio, centro de custos repetidos desde que projeto e/ou tarefa sejam diferentes entre eles. Mesmo que o tipo de movimento não esteja parametrizado para integração com o RM Solum, será possível trabalhar com Rateio de Tarefa, porém os projetos e tarefas a serem informados no rateio devem estar previamente cadastrados no RM Solum.

**Adequação à Nova Cobrança de Impostos para Bebidas**

Melhorias no sistema para atender à nova cobrança de impostos para bebida:  
No cadastro de Tributos dos Itens nos Tipos de Movimentos foi disponibilizada a opção “Pauta do Produto” no campo “Procurar Alíquota em”. Esta nova opção estará disponível, a princípio, somente para os tributos PIS e COFINS.  
Foi criada uma nova função de fórmula (TABPRDPAUTA) que busca os dados da Pauta dos Produtos. Esta função de fórmula será utilizada para a determinação da Base de Cálculo dos tributos que serão calculados através de Preço de Referência.  
Alteração no serviço que retorna a alíquota do tributo para o item de movimento, para tratar a situação em que a alíquota é buscada na “Pauta do Produto”. nestes casos a alíquota retornada será em R$ e não em percentual.  
O Movimento foi alterado para receber a alíquota AD REM em formato de moeda ao invés de percentual. Além disso, a rotina de cálculo do tributo do movimento foi alterada para que calcule o valor do tributo como Quantidade da Mercadoria X Alíquota AD REM, neste caso a quantidade deverá ser convertida para a unidade existente no cadastro de Pautas do Produto. e a Base de Cálculo do Tributo não será calculada pois nessa situação ela não existe.  
Alteração da localização do parâmetro: “Produto Tipo Frete” e criação do campo “Natureza Frete”  
Nos parâmetros do Tipo de Movimento, Processo – Fiscal, Etapa 1 - Definições Fiscais, foi criado um campo para informar o Produto Tipo Frete. O parâmetro geral deixa de existir na conversão o seu valor deve ser copiado para os tipos de movimentos que estejam com a opção “Gera Escrituração” marcado.  
Na interface do Movimento, na pasta Fiscal, foi criado um novo campo para informar a natureza fiscal que será utilizada para a tributação do frete, Natureza Frete. A regra de seleção será a mesma usada para a natureza do movimento.

**Alteração das descrições dos motivos de referência relacionados ao estoque de terceiros para o processo de cópia por referência:**

Para um melhor entendimento das opções disponíveis para motivo da cópia por referência, foram alteradas as descrições dos motivos relacionados à estoque de terceiros:   
- IDMOTIVOREF: 10 - de "Retorno de Remessa" para "Retorno de Remessa - Estoque Terceiros";  
- IDMOTIVOREF: 11 - de "Retorno de Mercadoria não Aplicada na Industrialização" para "Retorno de Mercadoria não Aplicada na Industrialização - Estoque Terceiros";  
- IDMOTIVOREF: 12 - de "Retorno de Remessa para Industrialização" para "Retorno de Remessa para Industrialização - Estoque Terceiros";  
- IDMOTIVOREF: 13 - de "Devolução Simbólica de Mercadoria em Consignação" para "Devolução Simbólica de Mercadoria em Consignação - Estoque Terceiros";  
- IDMOTIVOREF: 14 - de "Venda Mercadoria Consignada" para "Venda de Mercadoria Consignada - Estoque Terceiros";  
- IDMOTIVOREF: 15 - de "Devolução Mercadoria Consignada não Comercializada" para "Devolução de Mercadoria Consignada não Comercializada - Estoque Terceiros".

**Atendimento à Portaria 79/2003 do Estado de São Paulo**

Foram acrescentados os campos TIPOASSINANTE (movimento), QTDECONTRATADA e CODETDHABILITACAOTEL (item movimento) nas abas de Integração Fiscal do movimento e item de movimento. Estes Campos serão apresentados ao usuário quando o código modelo do documento de escrituração for igual a 06, 21, 22.  
A implementação visa o atender à Portaria 79/2003 do Estado de São Paulo (adoção do Convênio ICMS 115/2003).

**Importação de arquivos XML**

Disponibilizado nesta versão a importação de arquivos XML que contempla a manipulação de arquivos Xml´s do tipo Notas Fiscais Eletrônicas (NF-e), Conhecimento de Transporte Eletrônico (CT-e), ou Notas Fiscais de Serviços (NFS-e). Este processo está disponível somente para clientes que trabalham com a parceria TOTVS Colaboração. Para maiores detalhes sobre a contratação dos serviços TOTVS Colaboração, contate seu AR.  
Atendendo a esta melhoria, estão disponíveis os seguintes processos:  
**Cadastro de XML**:  
O cadastro tem o objetivo de armazenar o arquivo XML no banco de dados, sendo utilizado para manutenção e controle dos processos executados sobre o arquivo.  
Inclusão de Movimento com base em uma NF-e Validada pela SEFAZ:  
É possível realizar a inclusão de um movimento utilizando um arquivo XML referente a uma NF-e, que tenha sido validado pela SEFAZ. A inclusão do movimento pode ser ocorrer de várias maneiras: Inclusão Direta ou Manual,Faturamento (Pedido de Venda) e Cópia por Referencia. Cancelamento/Exclusão de Faturamento e Exclusão de Movimento são alguns processos que também podem ser realizados através desta rotina.

**Cadastro de Redução Z**

Os campos "CNPJ/CPF do Adquirente" (CNPJCPFADQUIRENTE) e "Nome do Adquirente" (NOMEADQUIRENTE) foram implementados no cadastro de redução Z.

**Consistência de parâmetros para movimentos integrados com o Portal**

Ao utilizar um movimento integrado ao portal, algumas consistências de parâmetros devem ser feitas por questões de segurança. Uma delas é que o campo de edição do preço do item de movimento não poderá ser marcado como mostra. Portanto, ao salvar as alterações será apresentada uma mensagem consistindo a parametrização: Tipo de Movimento: O preço do item não pode ser configurado com 'Mostra', em Movimento Integrado ao RM Nucleus.NET.    
Ao utilizar um movimento integrado ao portal, algumas consistências de parâmetros devem ser feitas por questões de segurança. Uma delas é que o campo unidade de medida do item de movimento não poderá ser marcado como não permite alterar. Portanto, ao salvar as alterações será apresentada uma mensagem consistindo a parametrização: Tipo de Movimento: A Unidade de medida não pode ser configurada como 'Não permite Alterar' em Movimento Integrado ao RM Nucleus .NET.

**Digitação de texto no corpo do e-mail e anexo**

Atualizado o envio de e-mail para fornecedores. Agora é possível digitar um texto qualquer para que ele seja apresentado no corpo da mensagem. É possível também anexar outros arquivos no e-mail como documentos auxiliares, imagess e etc.

**Disponibilizado os campos Valor Bruto Original, Valor Líquido Original e SubTotal Original na visão dos movimentos**

Agora é possível configurar para que apareçam as colunas com o Valor Bruto Original, Valor Líquido Original e SubTotal Original na visão dos movimentos.

**ICMS Cobrado Anteriormente por Substituição Tributária**

Para produtos que tem como tipo de ICMS igual 60 em movimento de saída, será realizado o calculo do valor unitário da Base de calculo e do Valor do Imposto do ICMS-ST referente a o último movimento de entrada que tenha ICMS ST e que controle saldo de estoque.

**Inclusão do campo CHAVEACESSONFE no relatório de exportação de movimento**

O campo CHAVEACESSONFE agora está disponível no relatório de exportação de movimentos e no layout de importação de movimentos.   
   
**Migração das Tabelas de Contrato**

As telas dos cadastros das Tabelas de Contrato foram migradas para a plataforma .NET e agora também podem ser acessadas pela nova MDI do CorporeRM.   
   
**Novos campos “Tipo de Receita” e “Código do Terceiro”**

Criado dois novos campos que serão apresentados no Item de movimento>>Integrações>>Fiscal para atender demandas fiscais. “Tipo de Receita” e “Código do Terceiro”.   
   
**Lançamento Financeiro por Item**

Implementado o processo de geração de lançamentos financeiros por item. Este processo permite ao usuário gerar lançamentos financeiros personalizados que poderão ser informados manualmente ou automaticamente, usando a data de entrega do item do movimento como base para o vencimento dos lançamentos financeiros a serem gerados.

**Implementada rotina de faturamento/cancelamento automáticos de movimentos relacionados ao processo de aprovação por workflow**

A partir desta versão, será possível o Faturamento/Cancelamento automáticos de Movimentos relacionados a Atendimentos do processo de Aprovação por WorkFlow diretamente no TOTVS Gestão de Relacionamento com o Cliente. Desta forma, o processo torna-se autônomo e transparente ao Usuário 'aprovador', agilizando os processos e aumentando a eficiência rotina de Aprovação.  
***Observação***: Para o correto funcionamento, existem parametrizações a serem feitas no sistema TOTVS Gestão de Relacionamento com os Clientes. Para isto, deve ser consultado o documento 'Como Fazer' desta rotina para orientações de parametrizações dos sistemas para o devido funcionamento.

**Função de fórmula: TABMOVRELACPEDIDO e TABITMRELACPEDIDO**

Criada a função de fórmula TABMOVRELACPEDIDO E TABITMRELACPEDIDO que tem como finalidade buscar informações referentes aos dados informados no movimento de origem. Esta fórmula deverá ser cadastrada no movimento de destino onde se deseja fazer tal consistência.

**Cadastro de tabela de preços por produto**

Disponível no sistema o cadastro de várias tabelas de preços de produtos, sendo suas atualizações baseadas em critérios pre-definidos conforme regras de negócio de cada cliente, tendo ainda vinculação com Filial, Cliente/Fornecedor, Condição de pagamento, Representante, Estado e Município.

**Conclusão de pedido**

Com a migração do movimento para .NET, foi criado um novo processo, "Conclusão de Pedido", que terá como finalidade a finalização de um ou mais pedidos que tenham sido faturados parcialmente e que não serão mais faturados. Este novo processo será criado pois não haverá mais movimento desdobrados.

**Alteração de dados dos lançamentos financeiros através do TOTVS Gestão de Estoque, Compras e Faturamento**

A partir desta versão, os lançamentos financeiros gerados no RM Fluxus através da inclusão de movimentos do RM Nucleus, poderão ser editados; com isto alguns campos do lançamento poderão sofrer alterações no momento da inclusão do movimento.

**Tabelas de orçamento**

Implementado a partir desta versão, no processo do controle orçamentário, dois novos cadastros: Grupo Orçamentário sendo uma tabela intermediária entre o Centro de Custo e a Natureza Orçamentária/Financeira que defini um agrupamento dos valores orçados e a tabela de Classificação dos Periodos onde ao criar Períodos de Orçamentos com periodicidades coincidentes, poderemos classificar estes períodos com uma forma diferenciada.

**Assistente de cópia de movimentos**

A partir desta versão, o Assistente de Cópia de Movimentos por Referência vem com algumas novidades; dentre elas um design inovador e mais intuitivo, conta também com funcionalidades mais aprimoradas, como a pesquisa pelos movimentos que serão referenciados, já que permite o Usuário criar um filtro com o critério desejado, sem induzir a utilização somente de determinados campos de pesquisa. Com isto, as pesquisas por movimentos poderão ser mais criteriosas, tornando a rotina mais simples e ágil.

Aprovação de movimentos

Nesta versão, o processo de Aprovação de Movimentos passa a ser mais intuitivo e ter um design inovador. Assim, além do processo ter sido revisado, foram aprimoradas algumas funcionalidades, como a utilização do processo de Aprovação por ‘Tolerância no Recebimento’, que apresenta, na mesma tela de Aprovação, a rotina de ‘Desaprovação’, que identificará quais os Itens estão ‘Aprovados’ para que sejam ‘Desaprovados’. Utilizando este tipo de Aprovação, a rotina de Desaprovação, do Menu Movimentos, passa a não ter usabilidade, já que a rotina de Aprovação funciona para as duas rotinas.

**Inativar eventos contábeis**

A partir desta versão ao migrar a base de dados para o novo modelo contábil e de faturamento – Backoffice - alguns eventos contábeis poderão apresentar inconsistências em relação a parametrização dos Itens do Evento Contábil aplicado em: Movimento, item, em relação aos Itens Gerenciais aplicado em: Rateio de C.Custo Mov ou Item, Lançamento entre outros. Neste caso, os eventos contábeis que apresentarem tais inconsistências serão inativados. Para ativá-los o usuário deverá acessar os eventos inativos e reajustar as validações citadas acima.

**Conversor de dados para faturamento parcial**

A partir desta versão será disponibilizado em Utilitários o Processo de Conversão de Dados para Faturamento Parcial que visa auxiliar o usuário na decisão de modificar o conteúdo de determinadas Consultas SQL, Relatórios e Fórmulas baseados no novo conceito do Faturamento Parcial e também possibilita a atualização de Filtros de Movimentos, Filtros de Relatórios e Filtros de Usuários de acordo com este novo conceito.

**Corrigir movimentos**

Rotina de correção de movimentos foi migrada e estará disponível nesta versão. Caso o usuário tenha a necessidade de, após gerarem movimentações no sistema, alterar alguns dados referentes à Inserção ou Exclusão de tributos, alteração do conteúdo da fórmula da base de cálculo ou Alíquota dos tributos associados aos parâmetros do tipo de movimento que foram gerados os respectivos movimentos, poderão fazer através desta opção.

**Produto substituto**

É possível fazer a troca do produto originalmente informado no movimento pelo seu substituto ou Similar. Para tal, será necessário informar previamente no cadastro do produto os seus substitutos ou similares através do anexo "Produto Substituto/ Similar", e nos parâmetros do tipo de movimento informar o tipo de tratamento que será utilizado no movimento: Similar, Substituto ou Ambos.

**Implementada a cópia do campo TMOV.NORDEM nos processos de cópia de movimentos**

Ao efetuar uma Cópia de Movimentos por Referência ou a geração de movimentos a partir de um movimento selecionado, o TOTVS Gestão de Estoques, Compras e Faturamento passa a copiar o campo NORDEM (Nº no Cliente) para os movimentos gerados.

Filtro de números de série na edição de itens de movimento

O sistema permite a utilização de filtros para pesquisa de Números de Séries a serem utilizados no Item de Movimento. Com isto, o sistema fica mais dinâmico na pesquisa e agiliza a informação dos dados dos Itens de Movimento. Os campos Lote e Data de Fabricação podem ser pesquisados, além do campo de Número de Série.

**Melhoria no processo de Gerar, Excluir e Estornar Contabilidade pela visão de movimentos**.

O sistema passa a executar a rotina de Geração, Exclusão e Estorno de Contabilização de Movimentos como um processo, mostrando log de cada movimento, sem depender que todos os movimentos sejam contabilizados para que o processo seja finalizado.

**Implementado o recurso de filtro por status do Produto (Ativo/Inativo) na consulta de saldos e custos.**

O sistema passa a permitir que o Usuário possa efetuar um filtro, na consulta de saldos e custos, para a identificação de Produtos inativos, evitando perda de tempo na análise de informações dos produtos que não mais são movimentados pela empresa.

**Contabilização de movimentos 'Offline', com possibilidade de agendamento**

O sistema passa a contar com o processo de agendamento de Contabilização de movimentos quando a contabilização está definida como 'offline', facilitando no processo de execução da contabilização dos movimentos. Desta forma, poderá garantir que a contabilização de movimentos ocorra em um período em que a utilização do sistema é alta, evitando a queda de performance na execução de outras rotinas no sistema.

**Geração do INSS pessoa física**

Foram realizadas alterações para permitir que, ao se configurar a fórmula para valor de serviço, o RM Nucleus permita incluir itens de movimento (servições e/ou produtos) com deduções (sempre a mesma alíquota) ou sem deduções (nenhuma alíquota).  
Essa implementação permite que seja identificado o total do valor de serviço do movimento e que o mesmo seja rateado nos lançamentos financeiros gerados pelo RM Fluxus.   
Caso a fórmula do valor de serviço não seja parametrizada, o sistema atuará da forma anterior, ou seja, impedindo a inclusão de itens de movimento com diferentes deduções (produtos ou serviços) e gerando o valor de serviço no financeiro com o valor original da parcela.

**Implementado o recurso de 'Agendar Financeiro' por períodos**

Foi disponibilizado o recurso de agendamento do Financeiro, com a utilização da execução de JobServer em ambiente 3 camadas. Desta forma, o processo de execução do Financeiro poderá ser executado em datas e horários específicos, conforme necessidade do Usuário.

**Implementada a gravação da informação no campo 'Seleção de Preço' no item de movimento**

O sistema passa a armazenar a informação selecionada no campo 'Seleção de Preço' do Item de Movimento. Desta forma, o sistema passará a identificar qual foi o preço selecionado no Item de Movimento para controle das informações, mantendo o histórico da origem do preço do Item de Movimento.

**Disponibilidade do recurso de ordenação de Campos Complementares**

Com este recurso, o Usuário tem a possibilidade de ordenar a apresentação dos Campos Complementares dentro da edição do Item/Movimento, com total flexibilidade, fazendo com que as informações sejam apresentadas de forma coesa com o processo do sistema.

**Implementado o recurso de visualização de consultas SQL como anexo de visões**

O sistema permite que o Usuário configure uma Consulta SQL como Anexo da Visão de Movimentos, podendo, inclusive, retornar informações presentes nos Itens de Movimento. Com isto, a verificação rápida de dados dos Itens de Movimentos passa a ser possível, aumentando a eficiência na consulta de dados relacionados aos Movimentos.

**Melhorado o processo de cópia de movimentos por referência, com a opção para eliminar os movimentos que não possuem Itens para devolução**

Ao efetuar a Cópia por Referência, o sistema permite que, após filtrar os movimentos que se deseja copiar, sejam excluídos os movimentos que não possuem Itens pendentes para Devolução.

**Implementado o cálculo de peso bruto e peso líquido do movimento através de fórmulas**

A partir desta versão, o sistema permite que o Usuário defina uma fórmula para o cálculo de Peso Bruto e Peso Líquido, de acordo com as informações dos Itens de Movimento.

**Implementada a utilização da data de entrega do item de movimento como data default do orçamento**

O sistema passa a permitir a utilização da Data de Entrega do Item como Data default para o Controle Orçamentário, diversificando as informações de controle da rotina de Orçamento.

**Consulta de naturezas de operação dentro das movimentações**

Com a migração de movimentos para a nova tecnologia, a pesquisa no cadastro de Naturezas ocorre de modo diferente do processo anterior, permitindo uma maior interatividade entre o Usuário e o sistema, inclusive com a pesquisa rápida sem a necessidade de navegar no cadastro de Naturezas de Operação.

**Consulta de movimentos**

A partir desta versão, a visão de Movimentos passa a contar com os novos recursos tecnológicos da TOTVS. Assim, o sistema permite uma maior interação do Usuário com o sistema, com a criação de filtros mais dinâmicos e intuitivos, agrupamentos por campos desejados, utilização de Consultas SQL e Gráficos como anexos da visão, entre muitos outros.

**Novas funções de fórmula**

* Criadas funções de fórmula EXISTERELACMOVIMENTO, EXISTERELACITEM, TABITMRELACPED e TABMOVRELACPED para consistir valores do movimento e dos itens de movimento de origem com o de destino.
* Aproveitando o momento da migração do movimento para .NET, estamos aprimorando a performance e a padronização das funções globais na utilização do RM.
* As funções RATEIOVALORMOV e RATEIOVALORMOVARRED comprometiam significativamente a performance do movimento, pois elas eram executadas sempre que acionadas em algum processo ou relatório. Para resolver esta questão, criamos na função TABITM campos correspondentes ao valor do rateio para cada valor do movimento que são possíveis de serem rateados:

|  |  |
| --- | --- |
| **Função Antiga** | **Função Nova** |
| RATEIOVALORMOV (‘VLRDEDUCAOMATERIAL’) | TABITM ('RATEIODEDMAT','V') |
| RATEIOVALORMOV ('VLRDEDUCAOOUTRO') | TABITM ('RATEIODEDOUT','V') |
| RATEIOVALORMOV (‘VLRDEDCAOSUBEMPREITADA') | TABITM 'RATEIODEDSUB','V') |
| RATEIOVALORMOV (‘VALORDESC') | TABITM ('RATEIODESC','V') |
| RATEIOVALORMOV ('VALORDESP') | TABITM ('RATEIODESP','V') |
| RATEIOVALORMOV ('VALOREXTRA1) | TABITM ('RATEIOEXTRA1','V') |
| RATEIOVALORMOV ('VALOREXTRA2') | TABITM ('RATEIOEXTRA2','V') |
| RATEIOVALORMOV ('VALORFRETE') | TABITM ('RATEIOFRETE','V') |
| RATEIOVALORMOV ('VALORFRETECTRC') | TABITM ('RATEIOFRETECTRC','V') |
| RATEIOVALORMOV ('VALORSEGURO') | TABITM ('RATEIOSEGURO','V') |

Para utilizar estas novas funções, os tipos de movimentos devem ser alterados, habilitando o parâmetro Rateio Valor Financeiro para os valores que se deseja ratear para os itens. Com esta funcionalidade, o cálculo do rateio será executado ao salvar o movimento. Com isto os valores rateados já estarão gravados na TITMMOV, ganhando assim, na performance de relatórios, cálculo do custo médio, contabilização, etc..

***Atenção!***

* Foi desenvolvido um conversor que irá verificar na base de dados todas as fórmulas que utilizam as funções RATEIOVALORMOV e RATEIOVALORMOVARRED e substituí-las pela função TABITM.
* O cadastro de fórmula irá consistir e não permitir incluir novas fórmulas com estas funções;
* Será necessário analisar os tipos de movimentos parametrizados para trabalhar com desconto, despesas, valores extras, frete, seguro, dentre outros valores, para que seja habilitado o Rateio Valor Financeiro para o respectivo valor. Isto para que os novos movimentos tenham gravado na TITMMOV os valores devidamente rateados.
* Não consideramos viável a execução de um script para atualização dos campos de rateio da TITMMOV para todos os movimentos antigos (incluídos antes da conversão e parametrização dos tipos de movimentos), pois dependendo do volume de dados da base, sua execução poderia ser morosa. Para mantermos compatibilidade nos relatórios e processos como contabilização e atualização do estoque que podem utilizar fórmulas com a função de rateio, sempre que um relatório possuir uma fórmula com a função TABITM (RATEIO...) e o respectivo campo da TITMMOV estiver nulo, o sistema irá executar internamente a função RATEIOVALORMOV.

**Alteração de campos após gerar ordem de produção no TOTVS Planejamento e Controle da Produção**

Após gerar a ordem de produção no TOTVS Planejamento e Controle da Produção, aparecerá a seguinte mensagem de consistência para os campos que não são passíveis de alteração após OP criada: “Item já programado pelo módulo de Produção não pode ser alterado".  
Os campos que não poderão ser alterados são os seguintes:

* Sequencial do Item
* Local de Estoque (Do movimento e do item
* Filial (Do movimento e do item)
* Data de Emissão
* Data de Saída
* Data de Programação
* Centro de Custo
* Unidade de medida do produto
* Lotes (Validade, data de entrada e fabricação de lote)
* Números de série
* Grade - Item de grade
* IDPRD (O produto não pode ser alterado nem excluído)
* Quantidade

Todos os demais campos poderão ser alterados após ordem de produção criada.

**Inclusão de números de série no movimento**

O sistema, desde que parametrizado para "Aceitar Números de Série", ao incluir um movimento com um produto que os utilize, somente irá aparecer na grid os números de série que ainda não foram utilizados.

**Filtros para número de série e lote na visão do movimento**

O sistema agora possui a funcionalidade de filtrar os números de série e lotes pela validade, de modo que não apareçam aqueles já vencidos.

**Cópia dos dados da aba importação no movimento ao utilizar natureza de operação igual a 3 ou 7**

Ao executar os processos de cópia simples, cópia por referência ou faturamento, os dados da aba importação ao utilizar natureza de operação igual a 3 ou 7, serão copiados.

**Ordenação por colunas através da grid dos itens de movimento**

A partir de agora, na grid dos itens de movimento, será possível realizar a ordenação dos mesmos através das colunas visíveis. Esta melhoria facilita a busca e ordenação dos itens da forma mais adequada ao usuário.

**Faturamento de movimentos sem dados de orçamento**

Otimizado a rotina de faturamento para que movimentos sem dados de orçamento, feitos anteriormente a parametrização do movimento sejam impedidos de serem faturados.

Parametrização de NF-e Estadual

O parâmetro “NF-e Estadual” do tipo de movimento agora será visível nas seguintes condições:

* Tipos de Movimentos '2.2.XX' ou,
* Tipos de Movimentos '3.1.XX' ou,
* Motivo referencia for Devolução de venda (Valor = 5) ou,
* Motivo referencia for Devolução de Compra (Valor = 4) ou,
* Tipos de movimentos '1.2' e emitente e destinatário como "Empresa".

**Atualização na visão de movimentos**

O campo “Razão Social” da visão de movimentos foi alterado para “Nome Fantasia Cli/for” para ficar igual ao mesmo campo no TOTVS Gestão Financeira. A padronização irá facilitar a criação de filtros evitando confusão entre nomes diferentes.

**Associar um conhecimento de transporte à uma NF**

Com a migração do movimento, foi criado um filtro para a associação dos conhecimentos de transporte. O recurso agilizará o processo de emissão do conhecimento de transportes.

**Número de lote e série**

Para os movimentos que utilizam lote e série passam a consistir o número de itens para o lote e o número de séries vinculados no movimento.

**Dados de importação no movimento e no item**

Melhoria realizada no envio de dados de importação do movimento nas rotinas de cópia e recebimento.

**Itens de movimentos - ordenação por colunas**

Na grid dos itens de movimento será possível realizar a ordenação dos mesmos através das colunas visiveis. Esta melhoria facilita a busca e ordenação dos itens da forma mais adequada ao usuário

**Alteração no calculo dos tributos do movimento**

Alterada a forma como é feito o calculo dos tributos. Antes o calculo era feito item por item, agora o calculo será feito somando todos os itens que tenha a mesma alíquota e que seja da mesma natureza fiscal.

**Defaults contábeis**

A partir de agora é possível buscar o default contábil para cliente/Fornecedor de Origem/destino

**Cancelamento de movimentos**

Disponibilizado o processo de Cancelamento de Movimentos na nova arquitetura dos sistemas na linha RM da TOTVS.

**Números de série**

A partir desta versão, com a migração do movimento para a plataforma .NET será possível filtrar os números de série que se deseja, por Número de série, lote e data de fabricação.

**Associar CTRC ao movimento**

A partir dessa versão é possível ordenar as colunas ou procurar por um campo específico do movimento que se deseja associar ao CTRC

**Desconto em todos os itens do movimento**

Para utilizar este processo, deve-se clicar com o botão direito do mouse em cima da Grid de itens de movimento e escolher dentre as opções de Desconto: se por Produtos, Serviços ou Ambos, se por Percentual ou Valor e qual será o desconto. O sistema estará aplicando o valor para todos os itens, independente do item possuir desconto previamente ou não. Se o item já possuir desconto, este valor deverá ser SUBSTITUIDO pelo novo.

**Desmembramento de produto composto**

Realizada melhoria no desmembramento de produtos compostos nos casos em que o movimento está parametrizado para utilizar integração com Projetos e foram informados projeto e tarefa no item de movimento.

**Fórmula do rateio por valor**

Melhoria realizada no rateio por centro de custo e departamento, quando os mesmos utilizam fórmulas para calculo do valor total do rateio.

**Fórmula para rateio do movimento e item de movimento**

Implementado o recurso de fórmula para os rateios por valor do Departamento e Centro de Custo. Ao informar a fórmula o sistema estará consistindo o rateio de acordo com a fórmula informada.

**Parametrização da data de cotação da moeda no movimento de origem**

Criação do parâmetros Data Base em Mov - Valores Financeiros para o tipo de movimento de origem onde é possível informar a data da cotação da moeda para que seja feita a conversão durante o faturamento.

**Não manter histórico do pedido**

Com o parâmetro "Não Manter Histórico do Pedido" marcado, o sistema não cria o log do faturamento no movimento de origem .

**Geração de contabilidade de lançamentos financeiros Através do TOTVS Gestão de Estoque, Compras e Faturamento**

A partir desta versão, o RM Nucleus poderá executar a contabilidade de lançamentos financeiros, vinculados aos movimentos, mesmo quando a contabilização do lançamento financeiro for parametrizada, no Evento Contábil, para ser executada por fórmulas. Com isto, a contabilidade dos lançamentos vinculados aos movimentos poderá efetuar o mesmo processo contábil executado diretamente no RM Fluxus, aumentando a usabilidade do recurso e melhorando a integração com o sistema financeiro.

**Integração TOTVS Gestão de Estoque, Compras e Faturamento X TOTVS Educacional**

Quaisquer movimentos gerados pelos módulos do RM Classis: Básico, Superior e NET não poderão ser alterados, cancelados ou excluídos pelo RM Nucleus.

**Melhoria realizada no processo de cópia de movimentos por referência.**

Na migração do processo de cópia por referência serão copiados apenas os dados parametrizados no movimento de destino. Dados não parametrizados não serão salvos no Banco de dados, e caso haja algum campo default no movimento de destino este deverá ser respeitado e não será sobrescrito.

**Novas variáveis para o complemento de histórico financeiro**

As seguintes variáveis estão disponíveis para o Complemento de Histórico Financeiro:  
[NUM] para o Número do Documento  
[HIS] para o Histórico  
[SER] para a Série  
[EMI] para a Data de Emissão  
[ORD] para o Número da Ordem  
[NOM] para o Nome Fantasia do Cli/For  
[RAZ] para a Razão Social do Cliente/Fornecedor  
[OBS] para Observação do Movimento  
[TDO] - Código do Tipo de Documento  
[DTD] - Descrição do tipo de Documento  
[CTT1] - Código da tabela de classificação 1 do faturamento  
[CTT2] - Código da tabela de classificação 2 do faturamento  
[CTT3] - Código da tabela de classificação 3 do faturamento  
[CTT4] - Código da tabela de classificação 4 do faturamento  
[CTT5] - Código da tabela de classificação 5 do faturamento  
[DTT1] - Descrição da tabela de classificação 1 do faturamento  
[DTT2] - Descrição da tabela de classificação 2 do faturamento  
[DTT3] - Descrição da tabela de classificação 3 do faturamento  
[DTT4] - Descrição da tabela de classificação 4 do faturamento  
[DTT5] - Descrição da tabela de classificação 5 do faturamento  
[CTF1] - Código da tabela de classificação 1 do financeiro  
[CTF2] - Código da tabela de classificação 2 do financeiro  
[CTF3] - Código da tabela de classificação 3 do financeiro  
[CTF4] - Código da tabela de classificação 4 do financeiro  
[CTF5] - Código da tabela de classificação 5 do financeiro  
[DTF1] - Descrição da tabela de classificação 1 do financeiro  
[DTF2] - Descrição da tabela de classificação 2 do financeiro  
[DTF3] - Descrição da tabela de classificação 3 do financeiro  
[DTF4] - Descrição da tabela de classificação 4 do financeiro  
[DTF5] - Descrição da tabela de classificação 5 do financeiro

**Processo referente ao estoque DE/COM terceiros**

- Tratar estoque em poder de terceiros com custo por filial.

- Permitir transferência entre estoque de/com terceiros.  
- Cancelar/excluir automaticamente movimentos adicionais do processo de retorno de industrialização gerados automaticamente quando movimento de retorno for cancelado/excluído.

**Realocação orçamentária**

Os movimentos que sofreram uma Realocação Orçamentária passam a respeitar algumas regras quando são alterados. Caso alguma regra seja violada, o movimento volta ao status “Bloqueado” e a realocação deve ser feita novamente. Alguns campos que regem esta regra: Quantidade, Data Orçamento, Código da Tabela do Orçamento, Centro de Custo, Rateios do item e movimento.

**Movimento - associar CTRC**

A partir dessa versão é possível ordenar as colunas ou procurar por um campo específico do movimento que se deseja associar ao CTRC.

**Implementados novos relatórios do modelo Backoffice**

A partir da versão intermediária 10.80.1 do TOTVS Gestão de Estoques, Compras e Faturamento, novos relatórios foram produzidos para atender as necessidasdes deste novo modelo, conforme podem ser vistos na lista abaixo:

* NUCREL0001 - Rastreia Movimento: Relatório de Rastreamento que exibe toda a árvore para saber qual é a origem e/ou destino que foi gerado.
* NUCREL0002 - Quantidade Pedida X Recebida: Relatório de quantidade pedida e recebida, esse relatório trará a quantidade dos itens que foram solicitados em um pedido e o que foi atendido. Para isso será necessário buscar a quantidade do movimento de origem e a quantidade do movimento de destino.
* NUCREL0003 - Pedidos Pendentes: Relatórios de pedidos pendentes considerando status do movimento A e G.
* NUCREL0004 - Espelho do Movimento
* NUCREL0005 - Movimentos por Status

***Observação***: Estes novos relatórios devem ser importados no novo modelo do Gerador de Relatórios – Gerador .NET.

**Outras atualizações**

1. Ajustado o campo Filial de Saída na tela de movimento para apresentar corretamente descrição da Filial selecionada.
2. Ajustados os métodos responsáveis por retornar os valores defaults da natureza do movimento.
3. Ajuste na consistência feita para verificar se o CPF/CNPJ é válido.
4. Ajuste na rotina que recupera os dados referentes ao produto no item do movimento, quando o tipo de movimento utiliza código EAN.
5. Ajuste na rotina responsável por expandir ítens compostos do movimento.
6. Ajuste na rotina responsável por gerar lançamentos financeiros.
7. Ajuste no filtro de condição de pagamento do movimento quando a parametrização ‘Usa condição de Pagamento do Cli / For’ esta marcada
8. Ajuste no método responsável por tratar históricos de lançamentos financeiros.
9. Ajuste no processo de cópia por referência, de movimentos de importação / exportação.
10. Ajuste realizado na cópia dos dados dos lançamentos contábeis.
11. Ajustes nas rotinas de faturamento, cópia por referência e a partir de outro movimento, para movimentos que contenham dados de importação/exportação na origem.
12. Alterada a validação feita para exibir ou não o processo “Concluir Pedido” tanto na tela de visão dos movimentos quanto na tela de edição do movimento.
13. Atualização ao relacionar bem à um item em um movimento integrado com o TOTVS Gestão Patrimonial.
14. Atualização ao salvar parametrizações para um tipo de movimento integrado com nota fiscal eletrônica estadual.
15. Atualização da rotina responsável pela consistência de preço no ítem de movimento.
16. Atualização da rotina responsável por carregar o cliente / fornecedor da movimentação.
17. Atualização da rotina responsável por retornar os itens de movimentos disponíveis para seleção no processo de cópia por referência.
18. Atualização na abertura de um movimento ao alterar o tipo de movimento pelo filtro de tipos de movimento.
19. Atualização na aprovação no faturamento por tipo de movimento por perfil, de modo que as consistências da fórmula inserida sejam feitas no movimento de origem e não no de destino.
20. Atualização na edição dos campos complementares do movimento através do anexo campos complementares na visão de movimentos.
21. Atualização na execução e disposição dos botões dos processos de gerar financeiro, contabilidade e excluir contabilidade.
22. Atualização na geração do histórico dos lançamentos financeiros utilizando os mnemônicos do movimento.
23. Atualização na geração do número do documento dos lançamentos financeiros de acordo com as parametrizações definidas no tipo de documento utilizado no movimento.
24. Atualização na geração do segundo número do movimento de acordo com a parametrização definida.
25. Atualização na gravação do campo tipo de recolhimento nos tributos do item de movimento para o tributo ISS e tipo de recolhimento “nenhum”.
26. Atualização na gravação dos dados da aba solicitação de um atendimento gerado por um tipo de movimento integrado com o TOTVS Gestão de Relacionamento com o Cliente e inserido pela WEB.
27. Atualização na inclusão de condições de pagamento à um movimento pelo portal, de modo que se o movimento for de compra, somente as condições de compra apareçam disponíveis. O mesmo funciona para os movimentos de venda.
28. Atualização na inclusão de grupos de clientes/fornecedores que possuam código alfanumérico para um produto através da execução do processo relacionado.
29. Atualização na inclusão de movimentações com tributos que buscam defaults nas pautas do produto.
30. Atualização na inclusão de movimento via web com centros de custo diferentes no item e no movimento, de modo que o do movimento não subscreva o do item.
31. Atualização na inclusão de movimentos com itens que possuem o código das unidades do produto em minúsculo, diferentemente do código da unidade do item de movimento.
32. Atualização na inclusão de movimentos com tributos que estejam utilizando código de receita.
33. Atualização na inclusão de movimentos integrados com o TOTVS Gestão de Relacionamento com o Cliente, de modo que ao salvar o movimento o processo de aprovação tenha continuidade.
34. Atualização na inclusão de movimentos parametrizados para fazer tolerância por valor com e sem o parâmetro “edita preço total” marcado.
35. Atualização na inclusão de movimentos preenchendo o campo Cliente/Fornecedor de Origem/Destino na aba Tributos e Valores / Tributos.
36. Atualização na inclusão de movimentos via portal integrado com o TOTVS Gestão de Projetos.
37. Atualização na inclusão de movimentos via portal, de modo que o os produtos inativos da base não aparecem disponíveis para serem selecionados para o movimento.
38. Atualização no processo de cópia por referência de movimentos que utilizam funcionários 1 e 2.
39. Inclusão de rateio utilizando fórmulas no movimento
40. É possível inserir fórmulas para calcular o rateio do item de movimento e do movimento ao selecionar o tipo "Valor" para os rateios de centro de custo e departamento.
41. Atualização realizada no envio de dados de importação do movimento nas rotinas de cópia e recebimento.
42. Atualização na performance do movimento, ajustes realizados nas rotinas utilizadas pelo sistema para inclusão de movimentos no novo modelo Back-Office.
