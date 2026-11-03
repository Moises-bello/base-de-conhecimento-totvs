---
content_hash: 956b1574034f8baa9b11e9d92290419dd1dd5555330a677fd56e2eb077e618d4
fetched_at: '2026-06-29T00:09:29.223949+00:00'
page_id: '423938842'
product: rm
source: tdn-rm
title: 04.01 - Parâmetros Gerais - Gestão de Estoque, Compras e Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938842
version: 41
---

Definições GeraisDefinições GeraisDefinições Gerais 1/3Definições Gerais 1/3Definições Gerais 1/3

Campos que afetam o Cálculo do Movimento: Os campos marcados serão os que ao serem editados afetarão o resultado final do movimento.

**Usar em Produto, Item de Movimento e Movimento:**Defina em que locais as tabelas serão utilizadas.

Definições Gerais 2/3Definições Gerais 2/3

**Cálculo Financeiro:**Informe como o sistema deverá executar os cálculos financeiros:

* Arredonda: Os valores serão arredondados de acordo com o número de casas decimais informado nos parâmetros gerais.
* Trunca: Os valores serão truncados, ou seja, não serão arredondados.

**Período de Movimentação:**Informe o intervalo de datas que será o limite inicial e final para se incluir movimentos no sistema. Assim, quando for feita uma movimentação fora do período aqui indicado, o sistema não aceitará.

**Nº Máximo de Linhas na Visão:**Defina neste campo o número máximo de linhas que um filtro deverá retornar.

**Casas Decimais:**Defina o número de casas decimais para os campos Quantidade, Valores, Tributos, Pesos e Custos.

Definições Gerais 3/3Definições Gerais 3/3

**Permite Visualização dos Dados no Filtro por Usuário:**

* Desmarcando este Parâmetro o sistema obedecerá as restrições de acessos indicadas no Menu Cadastros/Segurança/Usuários/Associação de Filtros.
* Marcando este Parâmetro o sistema não obedecerá as restrições de acessos indicadas no Menu Cadastros/Segurança/Usuários/Associação de Filtros, exceto para impressões de relatórios ou outros Objetos Gerenciais que utilize campos da base. Em caso de relatórios desenvolvidos utilizando sentença SQL, vide documento .

**Buscar Defaults de Cliente/Fornecedor e de Representante:** Parâmetro responsável por flexibilizar o uso de default's na inclusão de movimentos, que podem ser informadas no cadastro de cliente/fornecedor e representante.

Campos Cliente/Fornecedor: Tabela opcional 1(CODTB1FLX), Tabela opcional 2(CODTB2FLX), Tabela opcional 3(CODTB3FLX), Tabela opcional 4(CODTB4FLX), Tabela opcional 5(CODTB5FLX), Centro de Custo(CODCCUSTO) , Funcionário(CODVEN), Representante(CODRPR), Transportadora(CODTRA), Transportadora 2(CODTRA2)

Campos Representante: Tabela opcional 1(CODTB1FLX), Tabela opcional 2(CODTB2FLX), Tabela opcional 3(CODTB3FLX), Tabela opcional 4(CODTB4FLX), Tabela opcional 5(CODTB5FLX), Percentual Comissão (COMISSAOREPRES)

Observação

Com este parâmetro marcado, o default informado no cadastro de cliente/fornecedor e representante terão **prioridade** na inclusão de movimento.

Nos processos de faturamento, cópia simples e cópia por referência, a prioridade do default irá prevalecer apenas se na origem não existir as informações, caso contrário, a origem dos dados terá prioridade sobre o default mesmo com o parâmetro marcado.

Exemplo de utilização

Cliente/Fornecedor - default centro de custo: 01.01

Parâmetros tipo de Movimento - default centro de custo: 02.02

XML - default centro de custo: 03.03

**Inclusão manual**: Na inclusão de um movimento, caso o centro de custo seja preenchido pelo default do tipo de movimento (02.02) ou informado pelo usuário manualmente, ao preencher o cliente/fornecedor, com o parâmetro **Buscar Defaults de Cliente/Fornecedor e de Representante** marcado o default informado neste cadastro (01.01) irá sobrepor as informações. No exemplo acima, o movimento será incluído com o centro de custo 01.01.

**Inclusão via webservice ou API**: Mesmo com o parâmetro marcado, os defaults não serão considerados na inclusão de movimentos via webservice ou api, pois as informações do xml serão sempre consideradas, estando em branco ou preenchidas.

**Faturamento**: No movimento a ser faturado está informado o centro de custo (04.04).  Quando este movimento é faturado, as informações da origem prevalecem, neste caso o movimento será incluído com o centro de custo (04.04).

**Remetente do envio de E-mail:**Informe neste campo qual e-mail o sistema deve considerar como remetente para o envio de orçamento, ordem de compra, movimento ou cotação. São três opções:

* Funcionário logado
  + Neste caso o remetente vai ser o e-mai será o da pessoa que estará relacionada com o funcionário.
* Usuário logado
  + No caso de escolha do "usuário logado", o remetente vai ser o e-mai do usuário que estiver logado no sistema, e-mail registrado na tabela GUSUARIO.
* Parâmetros globais
  + Neste caso o remetente vai ser o e-mail cadastrado para a coligada, a origem deste e-mail é a tabela GCOLIGADA.

**Juros ao Mês (%):**Informe neste campo qual a taxa de juros ao mês a ser calculada sobre os lançamentos gerados para o TOTVS Gestão Financeira.

**Id da Empresa Centralizadora do Workflow do Fluig:**Informe neste campo o Id da Empresa do Fluig utilizado na integração e definido nos Parâmetros Globais | Aba Integração Fluig.

**Utilizar usuário para cancelamento de Workflow no Fluig:**Marcando este parâmetro será possível definir um usuário específico para ser utilizado no cancelamento de Workflows no Fluig. Para maiores informações, [consulte aqui](http://tdn.totvs.com.br/pages/releaseview.action?pageId=381037182).

**Usar inteligência artificial para auxiliar no preenchimento de cadastro:** Marcando este parâmetro é habilitado o botão **Extrair Dados Doc** dentro do cadastro de Fabricantes. Para mais informações [consulte aqui](https://tdn.totvs.com/x/XsdEGQ).

Calendário OficialCalendário Oficial

**Calendário:**Informe o calendário que será utilizado como padrão para os controles de datas do sistema.

Numeração do MovimentoNumeração do MovimentoNumeração GeralNumeração Geral

**Série:**Escolha a Série para definir Número em que começará a numeração dessa Série.

**Número:**Informe o Número que será o contador inicial para os movimentos com a Série em questão, desta forma todos os movimentos com a mesma, terão os números seqüenciais a partir do informado neste campo.

Numeração por FilialNumeração por Filial

**Série:**Escolha uma Série para que sejam apresentadas todas as filiais cadastradas e então definido qual será a numeração inicial dos movimentos para esta Série e Filiais específicas.

**Usar Máscara:**Marcando este campo as tabelas cadastradas obedecerão a máscara informada no campo Máscara. Caso o mesmo esteja desmarcado, mesmo estando o campo preenchido ele não será levado em consideração na inclusão das tabelas.

TabelasTabelasTabelas 1, 2, 3, 4 e 5Classificação

**Nome:**Informe o nome default para a tabela.

**Máscara:**Informe a máscara do código das mesmas. Todas as máscaras a serem cadastradas/definidas, ou, editáveis dentro dos parâmetros do sistema, podem ser constituídas por um conjunto de caracteres pré-definidos, cujos significados são:

* # → Numéricos (0 a 9);
* Q → Alfanuméricos (0 a 9 - A até Z - a até z);
* L → Alfabéticos Maiúsculos;
* l → Alfabéticos Minúsculos;
* A → Alfanuméricos Maiúsculos;
* a → Alfanuméricos Minúsculos;
* Separadores → ( '.', ',', '-', ':', '/', ' ', '(', ')' );

**Usar em Produto, Item de Movimento e Movimento:**Defina em que locais as tabelas serão utilizadas.

**Tipo de Produto fornecido pelo Fornecedor:** Define qual tabela de classificação será utilizada para essa funcionalidade. Quando não houver tabela parametrizada, a funcionalidade não ficará visível nos anexos do cadastro de Cliente / Fornecedor. Para sua utilização, é necessário selecionar uma tabela válida.

FabricantesFabricantes

**Máscara:**Defina a máscara para o Cadastro de Fabricantes.

**Nome Fabricante:**  Defina qual será o nome dado ao campo Fabricantes.

**Usa Tabela de Classificação:**Ativando a opção "Usar Tabelas de Classificação", na janela de edição Fabricante aparecerá a opção Tabelas que não é parametrizada aqui, e sim, em Parâmetros das Tabelas de Classificação.

FilialFilial

**Campo que descreve a Filial:**Defina o nome que descreverá a Filial: Nome Fantasia ou Nome.

FuncionárioFuncionário

**Máscara:**Defina a máscara para o Cadastro de Funcionários.

**Nome da Tabela:**  Defina qual será o nome dado ao campo Funcionários.

**Vincular Funcionário a Filial:**Marcando esta opção, quando se estiver fazendo uma movimentação em que o campo funcionário é editado, somente os funcionários da filial do movimento poderão ser informados no movimento.  
***Observações**:*

* A utilização do campo funcionário no movimento é determinada através dos tipos de movimentos Pasta Identificação/Funcionários.
* A informação de qual filial pertence o funcionário é feita no Cadastro de Funcionário, campo "Filial".
* Se este campo for marcado, a informação da filial no cadastro dos funcionários deve ser preenchida, pois, sem ela não será possível se informar funcionários nos movimentos.
Local de EstoqueLocal de Estoque

**Máscara:**Defina a máscara para o Cadastro de Local de Estoque.

**Nome da Tabela:**Defina qual será o nome dado ao campo Local de Estoque.

**Usar Local Único:**Marque esta opção se a empresa possui um único local físico de estoque.  
***Observação**:*Para utilizar esse recurso é necessário criar um local de estoque para cada filial existente.

MensagemMensagens do Sistema

**Nome da Tabela:**Defina qual será o nome dado ao campo Mensagem.

Definições de Produto 1/3Definições de Produto 1/3

**Nome da Tabela:**Defina qual será o nome dada a Tabela Produto.

**Máscara:**Informe a Máscara para o Código do Produto.  
***Observações**:*As máscaras para produto só poderão ser alteradas se aumentadas, nunca diminuídas. Para configuração da máscara do produto base para grade numerada, será aceito os seguintes formatos: A ou Q para campo alfanumérico, # Para números.

**Opções para a Máscara:**Não controla níveis de máscara. Neste caso o sistema não fará qualquer controle dos níveis de máscara do produto, o campo último nível no cadastro de produtos é desabilitado e será possível a inclusão e movimentação de qualquer produto, com qualquer código, desde que este é claro, esteja cadastrado.  
Exemplo*:*Se a máscara indicada no campo anterior for #.##.## e cadastramos direto o produto 1.01, o sistema aceitará sem conferir se o primeiro nível ainda não foi incluído.

**Controla Níveis de Máscara**: Escolhendo esta opção, o sistema passará a controlar os níveis de máscara dos produtos cadastrados no sistema da seguinte forma:

* No caso do exemplo anterior, não seria possível cadastrar o produto 1.01 sem antes ter cadastrado o de código 1 e não seria possível cadastrar o de código 1.01.01 sem antes ter cadastrado os de código 1 e 1.01.
* Caso estejam cadastrados os produtos 1, 1.01 e 1.01.01, não será permitida a alteração do código 1.01 para 1.02, por exemplo, pois este tem produtos ligados ao mesmo.
* No momento da digitação do item de movimento, o sistema só apresentará na lista de produtos para consulta aqueles que são de último nível.
* Na edição dos itens de um contrato, só exibirá produtos cujo tamanho do código é igual ao da máscara ou onde o campo último nível está marcado.
* Na importação de produtos, só importará o produto se o de nível anterior já existir e se este produto de nível anterior não tem a marca de "Último Nível".

**Completa com zeros à esquerda**: Neste caso, ao digitar parte do código do produto e ir para o próximo campo, o valor digitado será completado com zeros à esquerda até atingir o tamanho da máscara, o mesmo acontecendo no cadastro de produtos ao preencher o campo "Código do produto para encargos" na pasta Dados do Contrato. Ao inserir um item de movimento, o parâmetro 'Completa com zeros à esquerda' será considerado somente para os casos em que a máscara do produto tenha apenas um nível (Ex.: ######). Não terá efeito quando a máscara tiver 2 ou mais níveis.

**Descrição do Produto:**De acordo com as opções, selecione a forma que deseja consultar os produtos: Nome Fantasia, Descrição ou Descrição Auxiliar.

**Descrição com Limitação de Tamanho:**Informando uma das opões, o sistema irá limitar o tamanho dos caracteres do cadastro de produto para que possa ser utilizado em impressoras fiscais, que normalmente apresentam um tamanho bastante reduzido da descrição do produto. O objetivo do campo é limitar na interface do usuário de forma que o produto seja cadastrado da forma correta. Será apresentando as seguintes opções:

* Não Utiliza: o sistema não irá consistir a limitação de caracteres.
* Descrição Principal: O sistema irá limitar o tamanho da descrição Principal  do cadastro de produto quando informado o tamanho desejado.
* Nome Fantasia: O sistema irá limitar o tamanho do Nome Fantasia do cadastro de produto quando informado o tamanho desejado.

**Tamanho:**É o tamanho dos caracteres estabelecidos para o cadastramento.

**Unidade Padrão:**Informe aqui a unidade default para o produto, ou seja, sempre que incluir um novo produto, a unidade aqui informada será a que preencherá os campos para informações de unidade no mesmo, porém, o campo poderá ser alterado.

**Código Auxiliar Único para Produtos:**Marcando este parâmetro não será permitida a inclusão de produtos com código auxiliar iguais.

**Complementa o Último Nível do Código do Produto:**Marcando este parâmetro, na inclusão de um novo produto pelo menu cadastro, o sistema irá completar o último nível do código. Para isso, deverá ser informado o primeiro nível do código do produto, clicar na tabela TAB, que o sistema irá completar sequencialmente este código, respeitando a máscara do produto.

**Não Modificar Código do Produto:**

* Habilite este campo, caso deseja que o código do produto não seja alterado. Se incluir um produto com código errado não será possível a alteração do mesmo, deve-se então cancelar o produto cadastrado e incluir o novo.
* Com esta opção desmarcada, o campo código do produto poderá ser alterado a qualquer momento, desde que não tenha sido movimentado, integrado ao TOTVS Gestão Fiscal pela escrituração de movimentos, integrado ao TOTVS Gestão Patrimonial, ao EPI, quando há incompatibilidade de máscaras, pois o sistema não conseguirá atualizar os códigos dos produtos que já tenham sido movimentados e ao sistema de Manutenção de Ativos (SigaMNT).

**Usa Funcionário Responsável do Produto:**Habilitando esta opção, será apresentada no cadastro de produto a pasta "Funcionário Responsável" pelo produto.

**Campo Complementar na visão:**Marcando esta opção os campos complementares de produtos aparecerão no ícone configurar campos na visão de produtos.

Definições de Produto 2/3Definições de Produto 2/3

**Usa Código Reduzido:**

* Não Utiliza: o código reduzido não será utilizado para os produtos.
* Sequencial: utilizará o código reduzido e este terá uma numeração sequencial.
* Não Sequencial: utilizará o código reduzido, porém, este não será sequencial.

**Copiar para Código Principal:**Caso esteja marcado, ao incluir um produto, se o código principal não for informado, o código reduzido será copiado para este.  
***Observações**:*Este parâmetro somente pode ser marcado se o código reduzido for 'Sequencial' e a máscara do código reduzido for igual à máscara do código principal. Como o código reduzido sequencial é gerado somente ao salvar o registro, a cópia somente será feita ao salvar o registro. Vale frisar que a cópia não é feita quando for realizada alteração do registro.

**Máscara:**Informe a Máscara para o Código Reduzido.

**Sequência****Atual:**Defina qual será a Sequência Atual.

**Tipo Histórico:**

* Histórico Curto: Marcando esta opção, o histórico a ser informado no contrato e no item poderá conter no máximo 255 dígitos.
* Histórico Longo: Marcando esta opção, o histórico a ser informado poderá conter um número indeterminado de dígitos, dependendo da capacidade de armazenamento de seu equipamento.

***Observação**:*Após a definição de utilização de "Histórico Longo", não será possível o retorno à opção "Histórico Curto". Já a alteração do histórico curto para o longo é possível, portanto, aconselhamos primeiro definir o trabalho utilizando o histórico curto. Se posteriormente houver necessidade de se informar para os contratos históricos com mais de 255 dígitos, isto poderá ser revertido. A utilização de histórico curto ocupará menos espaço em sua base de dados.

Definições de Produto 3/3Definições de Produto 3/3

**Características Físicas:**Será apresentada uma pasta no cadastro do produto, para que informe as características físicas do mesmo, tais como, peso líquido, peso bruto, comprimento, etc.

**Dados Fiscais:**Na inclusão do produto, você poderá cadastrar os dados fiscais do mesmo, tais como, procedência, Nomenclatura Comum do Mercosul.

**Casas Decimais:**Habilite este parâmetro se desejar informar um número de casas decimais diferente da indicada na Pasta Gerais dos Parâmetros Gerais/Tabelas para cada Produto, este habilitará no Cadastro de Produto, Pasta Preços , o campo "Nº de Casas Decimais".

**Produto Composto:**Marcando esta opção, o sistema habilitará a pasta Produtos Compostos no Cadastro de Produtos.

**Produto Similar:**Marcando esta opção, o sistema habilitará a pasta Produtos Similares no Cadastro de Produtos.

**Fornecedores:**Para cadastrar para cada produto incluído os fornecedores do mesmo.

**Conta Trabalho:**Marcando esta opção, o sistema habilitará a pasta Conta Trabalho no Cadastro de Produtos.

**Tabela de Classificação Utilizada para Aplicar Fornecedores a um Grupo de Produtos:**Indique neste campo a tabela de classificação que deverá ser utilizada para aplicar a um grupo de produtos um determinado fornecedor.

Campos OpcionaisCampos Opcionais

**Nome do Campo Livre 1, 2 e 3 do Produto:**Defina os nomes dos Campos Livres.

Datas OpcionaisDatas Opcionais 1/2

**Edita Data Extra 1 e 2 do Produto:**Marque caso deseje utilizar Datas Extras.

**Nome Data Extra 1 e 2 do Produto:**Defina um Nome paras as Datas Extras.

Grade NumeradaGrade Numerada

**Habilita Grade Numerada:**Habilitando esta opção será apresentada no cadastro das Tabelas Auxiliares a Grade Numerada por Produto que será incluída à partir de um produto base.

**Grade Numerada Original: (Cadastro Descontinuado não será possível ser habilitado)**

* Não utilizar: O sistema nem habilitará o campo de grade numerada no cadastro do produto e nos parâmetros de tipos de movimentos.
* Utilizar com controle de estoque: Além de o sistema habilitar o campo de Grade Numerada no Cadastro do Produto e nos Parâmetros de Tipos de Movimentos, marcando esta opção, as grades terão Controle de Estoque, ou seja, se o Tipo de Movimento afeta o estoque aumentando ou diminuindo, os saldos dos itens das Grades também aumentarão ou diminuirão.
* Utilizar sem controle de estoque: Marcando esta opção, o sistema também habilitará o campo Grade Numerada no Produto e nos Tipos de Movimentos, porém, os itens  de Grade não terão Controle de Estoque.

**Nome da Grade:**Defina um nome para a Grade.

**Separador Código de Barras:**Defina um separador para o Código de Barras.

LoteLote

**Permite Lote e Número de Série Simultaneamente:**Marcando este campo na inclusão do Movimento o Item poderá utilizar Número de Série e número de Lote simultaneamente. Caso este parâmetro não esteja marcado e o item possua Número de Série e Lote simultaneamente, somente a pasta Lote estará habilitada no movimento. Caso este parâmetro esteja marcado, não será permitido cadastrar intervalos de Número de Série na tela do Item de Movimento, sendo desabilitada a opção "Gerar nº de série sequencial" (para cada novo Número de Série deverá ser informado um Lote relacionado).

**Permite Número de Lote Repetido:**Marcando este campo, será permitido cadastrar um lote de produto com o mesmo número para uma mesma filial e local.

**Gera Número de Lote** **Sequencial****:**Marcando este parâmetro, o campo "Número Lote" ficará desabilitado e sua numeração será gerada sequencialmente. Este número respeitará a máscara cadastrada no campo "Máscara número lote".

**Máscara:**Defina uma Máscara para o Lote Sequencial.

**Uso Códigos EAN:**

* Não Usa: Marcando essa opção, a aba "Código de Barras" não é visualizada na grid do Produto.
* Usa Opcional: Marcando essa opção, a aba "Código de Barras" é visualizada na grid do produto, mas não é obrigatório informar o Código de Barras para salvar o Produto.
* Obrigatório Sempre: Marcando essa opção, a aba "Código de Barras" é visualizada na grid do produto, sendo obrigatório informar o Código de Barras para salvar o Produto.
* Obrigatório para Tipo Produto: Marcando essa opção, a aba "Código de Barras" é visualizada na grid do produto, sendo obrigatório informar o Código de Barras para salvar o Produto.

***Observação**:*Marcando a opção 'Obrigatório para Tipo Produto', é obrigatório informar código de barras para cadastrar Produtos. Para cadastrar Serviços o preenchimento não é obrigatório.

Preços 1/3Preços 1/3

**Usa Preço 1 e 2 de Produtos:**Defina se utilizará Preços.

**Nome do Preço 1 e 2:**Defina um nome para o Preço.

**Código da Moeda do Preço 1 e 2:**Defina qual será a moeda para os Preços.

Preços 2/3Preços 2/3

**Usa Preço 3 e 4 de Produtos:**Defina se utilizará Preços.

**Nome do Preço 3 e 4:**Defina um nome para o Preço.

**Código da Moeda do Preço 3 e 4:**Defina qual será a moeda para os Preços.

Preços 3/3Preços 3/3

**Usa Preço 5 de Produtos:**Defina se utilizará Preço.

**Nome do Preço 5:**Defina um nome para o Preço.

**Código da Moeda do Preço 5:**Defina qual será a moeda para os Preço.

RepresentanteRepresentante

**Máscara:**Defina a máscara para o Cadastro de Representantes.

**Nome Fabricante:**Defina qual será o nome dado ao campo Representantes.

**Descrição Representante:**Defina se a descrição dos Representantes será pelo Nome ou Nome Fantasia.

TransportadoraTransportadora

**Nome Transportadora:**Defina qual será o nome dado ao campo Transportadora.

**Descrição Representante:**Defina se a descrição da Transportadora será pelo Nome ou Nome Fantasia.

Natureza Orçamentária/FinanceiraNatureza Orçamentária/Financeira

**Utiliza Natureza Orçamentária/Financeira:**Defina se será possível utilizar Natureza Orçamentária/Financeira.

**Máscara:**Defina uma máscara para as Naturezas Orçamentárias/Financeiras.

Produto GlobalProduto Global

**Usa Produto Global:**Se uma coligada não possui nenhum produto cadastrado, ou seja, uma coligada nova, podemos iniciar o cadastro de produtos já trabalhando com produto global marcando este campo.

Grupo de ProdutoGrupo de Produto

**Máscara:**Defina uma máscara para os Grupos de produtos.

Atenção:

Após inserir registros no Cadastro de Grupo de Produtos a máscara não poderá ser alterada.

MarcaMarcas

**Máscara**: Defina uma máscara a ser aplicada no código da Marca. Neste campo serão aplicadas as seguintes regras:

* A máscara default será composto pelos caracteres "#####".
* Será permitido usar os caracteres e como separadores os caracteres. Caso seja utilizado um caracter diferente destes, ele será considerado como um caracter vazio.
* Este campo não poderá ser alterado caso já existe algum registro já cadastrado na base para coligada logada.

**Nome da Marca:** defina qual o nome será exibido no sistema. Comportamento similar ao do Fabricante, Representante e Transportadora. O nome default deste campo será "Marca".

**Usa Marca Global:** campo para definir se o cadastro de Marca será Global. O valor default deste campo é "marcado".

**Importante:** quando existirem cadastros de marca globais, o parâmetro "Usa marca Global" não poderá ser desmarcado. Da mesma forma, quando o parâmetro está desmarcado e existirem marcas cadastradas por coligada, não é possível alterar o parâmetro. Caso a Coligada esteja  configurada para Central de Compras ou Participante de Central de Compras será obrigatório habilitar o parâmetro Usa Marca Global.

***Observações**:*As coligadas que estiverem usando marca global, poderão visualizar os seus registros em outras coligadas que também usam marca global.   
Exemplo: Coligada 1 não usa marca global; Coligada 2 e Coligada 3 usam marca global. Ao abrir o cadastro de Marca na coligada 2 serão exibidos os registros cadastrados nas coligadas 2 e coligada 3. Ao abrir o cadastro de Marca na Coligada 1 serão exibidos somente os registros da Coligada 1, pois ela não trabalha com marca global.

Segundo Número

**Segundo Número geral:**Informe o número que será o contador inicial a ser seguido para sequencializar o Segundo Número nos Movimentos, isto se, nos Parâmetros do Tipo de Movimento escolher a seqüência do Segundo Número pelo "Segundo Número Geral".

**Filial:**Informe o primeiro número que será o contador inicial a ser seguido para sequencializar o Segundo Número nos Movimentos para cada Filial, isto se, nos Parâmetros do Tipo de Movimento escolher a seqüência do Segundo Número por "Filial".
