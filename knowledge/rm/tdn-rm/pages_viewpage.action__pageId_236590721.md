---
content_hash: 7bb2722a4acff751bb4afa38c5100f63c077ac4ad6539726239ff1d65bef7f76
fetched_at: '2026-06-29T00:08:06.285018+00:00'
page_id: '236590721'
product: rm
source: tdn-rm
title: TSRMCN DT Inclusão de Movimento através de XML TOTVS Colaboração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236590721
version: 132
---

# INCLUSÃO DE MOVIMENTO ATRAVÉS DE XML - TOTVS COLABORAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | Recebimento de Materiais |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Inclusão de Movimento através de XML - TOTVS Colaboração | MovTraducaoXMLTOTVSColabProcAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Criação de Fórmulas | GlbFormulaAction | | Definições de Cli/For - TOTVS Colaboração | MovDefinicoesCliForTOTVSColabAction | | Natureza Inversa TOTVS Colaboração | MovNaturezaColabAction | | Parâmetros da Filial | MovFilialInfoNeoGridParamsForm | | Produtos TOTVS Colaboração | EstPrdCfoTOTVSColaboracaoAction | | Unidades TOTVS Colaboração | MovUndCfoColabAction | |
| **Chamados Relacionados** | TSRMCN |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL e Oracle |
| **Tabelas Utilizadas:** | DCFOP - Naturezas Fiscais (CFOP);  DREGRAICMS - Regras de ICMS;  DREGRAIPI - Regras de IPI;  GFORMULA - Fórmulas;  TDEFINICOESCFOCOLAB - Definições de Cli/For - TOTVS Colaboração;  TITMMOV - Itens de Movimento;  TLOGCOMPIMPOSTOCOLAB - Diferenças de Tributos Calculados x Tributos XML;  TMOV - Movimentos;  TNATUREZACOLAB - Naturezas Inversas TOTVS Colaboração;  TNFEENTRADA - Notas Fiscais (NF-e) Recebidas;  TPARFILIAL - Parâmetros da Filial;  TPRDCFOCOLAB - Produtos TOTVS Colaboração;  TTRBMOV - Tributos do Movimento;  TUNDCFOCOLAB - Unidades Totvs Colaboração;  TXMOCOLAB - XML Recebidos pelo TOTVS Colaboração. |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Todas as rotinas responsáveis pelo recebimento de nota fiscal eletrônica foram reescritas, com o objetivo de melhorar a performance e tornar o processo mais simples e estável. Também foram refeitas todas as telas do processo atual, a fim de aprimorar a usabilidade do mesmo.

Todas as melhorias de performance e de usabilidade das telas estão disponíveis tanto para o TOTVS Colaboração 2.0 como para o TOTVS Colaboração 1.0.

É importante salientar que para a utilização do TOTVS Colaboração é indispensável a contratação dos serviços da NeoGrid que é a responsável pelo processamento da leitura dos arquivos XML, pela comunicação com os webservices da SEFAZ e pelo retorno às consultas destes documentos. Estes, por sua vez, serão lidos e interpretados através da execução de JOBs específicos pelo TOTVS Gestão de Estoque, Compras e Faturamento para a devida atualização dos dados no sistema.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

## Procedimento para Utilização

### 1. Cadastros

Para o correto funcionamento da rotina de *"Inclusão de Movimento Através do XML - TOTVS Colaboração"* devemos ficar atentos ao preenchimento de alguns cadastros. São eles:

### 1.1. Natureza Fiscal (CFOP)

Quando uma nota fiscal eletrônica é enviada por um fornecedor, ela contém, para cada um dos seus itens, uma natureza fiscal (CFOP) de saída, que caracteriza a operação desse fornecedor. Para a empresa que recebe esse documento entretanto, devemos encontrar a natureza fiscal (CFOP) de entrada correspondente. Essa ‘Natureza Inversa’ é indispensável para a criação de um movimento de NFe.

Para definir a Natureza Inversa de forma automática na geração do movimento de entrada, o TOTVS Gestão de Estoque, Compras e Faturamento utilizará os seguintes recursos:

### 1.1.1. Regra de Seleção da Natureza (RSN)

Para cada movimento de NF-e a ser incluído, o sistema irá encontrar a Natureza Inversa do CFOP constante do arquivo XML. Para isso, é necessário saber, através das parametrizações vigentes do tipo de movimento, se o movimento a ser criado seleciona a Natureza de Operação somente para o movimento, ou se deve ser selecionada também uma Natureza para o item de movimento. Para ambos os casos, será utilizada em primeiro lugar a Regra de Seleção da Natureza (RSN), rotina hoje já existente e que tem a finalidade de encontrar a Natureza de Operação baseada nas informações do movimento e parametrizações de várias tabelas tais como: Parâmetros do Tipo de Movimento, Produto, Classificação de Produto, Naturezas Fiscais, Regras de ICMS, Regras de IPI, etc..

Para verificar como está a parametrização da sua empresa vá na etapa *"Fis - Natureza"* dos Parâmetros dos Tipos de Movimento que serão utilizados na Inclusão de Movimento através de XML e verifique o preenchimento do campo 'Seleção Automática da Natureza'.

Detalharemos a seguir como o sistema procederá conforme o tipo de Seleção Automática da Natureza definido para o tipo de movimento.

### 1.1.1.1. Seleção Automática da Natureza por Movimento

Neste caso, deverá ser encontrada obrigatoriamente uma Natureza de Operação analítica para o movimento.

Através dos dados do XML e das parametrizações e cadastros do sistema**,** a Regra de Seleção da Natureza irá encontrar a(s) natureza(s) possível(eis), de forma que:

* Se a RSN encontrar apenas uma Natureza de Operação (CFOP) possível, o movimento de NF-e será incluído com o CFOP encontrado;
* Se a RSN encontrar mais de uma Natureza de Operação (CFOP) possível, o sistema irá verificar as opções cadastradas como Natureza Inversa da CFOP extraída do XML.

No item 1.1.2 deste documento iremos detalhar como será o comportamento do sistema caso seja necessário utilizar o cadastro de Natureza Inversa do CFOP.

### 1.1.1.2. Seleção Automática da Natureza por Item de Movimento

Nesta situação, será realizado o mesmo procedimento já explicado anteriormente para encontrar a Natureza de Operação do movimento, com a diferença desta poder ser analítica ou sintética.

Se for encontrada uma Natureza analítica, sua ‘Raiz’ (Natureza Sintética) deve ser extraída e considerada como a Natureza do movimento enquanto que a Natureza analítica será atribuída ao item.

Caso sejam encontradas 2 naturezas sintéticas possíveis, os campos natureza 1 e natureza 2 do movimento serão preenchidos caso ambos estejam parametrizados para o tipo de movimento, mas se existirem mais de 2 naturezas sintéticas possíveis, o sistema não será capaz de solucionar o conflito e, neste caso a natureza não será identificada, sendo preenchida a natureza do movimento com um CFOP de primeiro nível, ou seja, 1 ou 2 conforme a UF de origem da NF-e.

Caso seja encontrada apenas a Natureza sintética, ela será atribuída ao movimento, e o procedimento de busca será realizado novamente para selecionar a Natureza do item. Para o item, a Regra de Seleção da Natureza irá considerar os dados do movimento e das demais tabelas citadas anteriormente (Parâmetros do Tipo de Movimento, Produto, Classificação de Produto, Naturezas Fiscais, Regras de ICMS, Regras de IPI, etc.).

Conforme já informado o sistema primeiramente executará as Regras de Seleção da Natureza, e caso as mesmas retornem mais de uma opção de CFOP para os itens do movimento, o sistema utilizará o cadastro das Naturezas Inversas que detalharemos a seguir:

### 1.1.2. Natureza Inversa

No cadastro de Natureza de Operação (CFOP), de responsabilidade do sistema TOTVS Gestão Fiscal, foi criado o anexo *"Natureza Inversa TOTVS Colaboração"*  onde deverão ser cadastradas as possíveis naturezas de operação inversas para uma determinada natureza sintética.

Uma natureza de operação sintética, poderá ter a ela vinculada várias naturezas de operação inversas, sejam elas sintéticas ou analíticas.

Entre as naturezas inversas cadastradas, o usuário poderá definir "Defaults", ou seja, registros que devem ser considerados prioritários caso existam várias naturezas possíveis para um determinado movimento.

Este cadastro será utilizado apenas caso através da aplicação das Regras de Seleção da Natureza tenha sido encontrada mais de uma natureza inversa possível para o item. Neste caso o sistema procederá da seguinte forma:

* Se apenas uma das naturezas selecionadas  estiver cadastrada como "Default", ela será utilizada para a criação de movimento;
* Se mais de uma das naturezas selecionadas estiver cadastrada como "Default", o sistema não saberá qual Natureza Inversa escolher e o movimento será criado com o Status do TOTVS Colaboração como 'Natureza Incompleta';
* Se apenas uma das naturezas selecionadas estiver cadastrada como Natureza Inversa, mesmo não sendo como "Default", ela será utilizada para a criação do movimento;
* Se mais de uma das naturezas selecionadas estiver cadastrada como Natureza Inversa mas nenhuma delas é "Default", o sistema não saberá qual Natureza Inversa escolher e o movimento será criado com o Status do TOTVS Colaboração como ‘Natureza Incompleta';
* Se nenhuma das naturezas selecionadas estiver no cadastro de Natureza inversa, o movimento será criado com o Status do TOTVS Colaboração como ‘Natureza Incompleta'.

É importante salientar que o Status TOTVS Colaboração 'Natureza Incompleta' não influencia no status do movimento que será criado conforme os parâmetros do Tipo de Movimento gerado, ou seja, mesmo estando com esse Status TOTVS Colaboração o movimento poderá gerar todas as demais integrações (financeira, contábil, estoque e de aprovações) se assim estiver parametrizado.

Os movimentos gerados com o Status TOTVS Colaboração 'Natureza Incompleta' deverão ter seus CFOP informados através de edição manual.

Uma natureza default pode ser sintética ou analítica, entretanto, poderá haver somente uma natureza analítica default de cada 'raiz' para uma mesma natureza sintética.

Exemplo:

No nosso exemplo acima a natureza 1.102.04 não pode ser default para a natureza 5.101 já que outra natureza que possui a sintética idêntica (1.102.03) já foi definida como default para a mesma.

No TOTVS Gestão de Estoque, Compras e Faturamento, o cadastro das naturezas inversas***,***está disponível em *“Cadastros > Fiscais > Natureza Fiscal > Anexos > Natureza Inversa TOTVS Colaboração”*.

Você poderá acessar este Anexo a partir da visão de Naturezas ou a partir da tela de edição de uma Natureza específica.

Acesso a partir da visão de Naturezas

Acesso a partir da tela de edição da Natureza:

O sistema irá verificar a Natureza Inversa do CFOP constante da NF-e, ou seja as Naturezas Inversas devem estar cadastradas nas naturezas sintéticas de Saída. Assim, selecione o CFOP sintético para o qual você irá cadastrar as Naturezas Inversas e clique em *"Anexos > Natureza Inversa TOTVS Colaboração"*.

Será apresentada a tela onde você poderá cadastrar as Naturezas Inversas a serem vinculadas à natureza sintética selecionada.

Informe a Natureza Inversa correspondente, marque o campo caso a mesma vá ser uma natureza 'Default' para esta natureza sintética e clique em 'Inserir'.

O sistema apresentará na tela a correspondência entre as naturezas inseridas, permitindo que as demais Naturezas Inversas dessa Sintética sejam incluídas, caso existam.

Informe todas as naturezas inversas de cada natureza sintética de saída e clique em*"OK"* ou *"Salvar"* para que o sistema as grave.

### 1.2. Produtos

Para efetuar a inclusão de um movimento através do XML é necessário que seja feita a correlação entre os produtos constantes dos XML e os produtos constantes da sua base de dados, ou seja, dos produtos do fornecedor com os produtos do seu estoque.

A tradução dos produtos contidos no XML, que anteriormente era feita com base nas informações da tabela Produtos por Fornecedor, a partir de agora será feita através da tabela Produtos TOTVS Colaboração.

Nesta nova estrutura, o usuário poderá definir um relacionamento de 1 x N, conforme exemplificamos abaixo:

Note que para o produto 100524 podemos ter N produtos vinculados como por exemplo os produtos Caneta Esferográfica Azul e Caneta Esferográfica Preta do fornecedor, correspondem a um só produto no estoque, Caneta Esferográfica.

As informações atualmente existentes na tabela Produtos por Fornecedor serão automaticamente inseridas na tabela  Produtos por Fornecedor TOTVS Colaboração através do atualizador da versão.

Para incluir novos produtos na tabela acesse *“Cadastros > Produtos > Anexos > Produtos TOTVS Colaboração”.*

Como todos os demais Anexos do sistema, você poderá acessá-lo a partir da visão de Produtos ou a partir da tela de edição de determinado Produto.

Acesso através da visão de Produtos.

Acesso a partir da tela de edição do produto:

Informe o 'Código do Fornecedor', o 'Código do Produto no Fornecedor' e se este for o único produto correspondente para este fornecedor, clique em*"Salvar"* ou *"OK"* para efetuar a gravação do registro ou no ícone *"Incluir"* caso queira gravar o registro e em seguida informar um novo fornecedor e código de produto correspondente para este produto.

Caso o produto possua mais de um produto correspondente no mesmo fornecedor, informe um deles no 'Cód. do Produto no Fornecedor' e clique em "Inserir Múltiplos" para utilizar esse recurso facilitador que permitirá que você inclua vários registros na mesma tela e grave-os de uma só vez.

No campo 'Código do Produto' informe o código do produto no fornecedor e em seguida clique em "Inserir", e assim sucessivamente até que todos os códigos no fornecedor tenham sido informados.

Após informar os códigos de todos os produtos correspondentes nesse fornecedor clique em *"Salvar"* ou *"OK"* para efetuar a gravação do registro ou no botão *"Incluir"* caso queira gravar o registro e em seguida informar um novo fornecedor e produto correspondente para este produto.

Após finalizar a inserção dos Registros Múltiplos, caso opte por "Salvar" o sistema lhe apresentará em tela a mensagem informando os registros que foram gravados.

Para encerrar a informação dos fornecedores e produtos correspondentes a este produto tecle "OK" e o sistema automaticamente sairá da tela de cadastro e exibirá a visão  dos Produtos TOTVS Colaboração cadastrados para o seu produto.

Vale salientar que caso tenha(m) havido inclusão(ões) a partir da inserção de múltiplos registros será necessário clicar no botão "Atualizar Informações" para que os mesmos sejam apresentados.

Caso nem todos os produtos constantes de um XML tenham sido vinculados com o respectivo produto da sua base de dados, você também poderá informar uma vinculação no momento da tradução do XML que é executada no processo *"Inclusão de Movimento através de XML - TOTVS Colaboração"*.

### 1.3. Unidades

Da mesma forma que com os produtos, para efetuar a inclusão via XML é necessário que seja feita a correlação entre as unidades de medida dos produtos constantes dos XML, ou seja das unidades do fornecedor com as unidades utilizadas na sua empresa.

O sistema realizará a tradução do campo Unidade de Medida ‘CODUND’ através da tabela ‘TUNDCFOCOLAB’, onde será possível cadastrar o código da unidade no fornecedor, e informar a unidade correspondente no sistema, podendo assim evitar a intervenção manual do usuário durante o processo de recebimento.

Para informar a correlação entre as unidades vá em *“Cadastros > Mais... > Tabelas Auxiliares > Unidade > Anexos > Unidades TOTVS Colaboração”.*

Você poderá acessar este Anexo exclusivamente da visão de Unidades.

O sistema abrirá o Anexo do lado direito da tela de visão das Unidades.

Clique no botão "Incluir" para inserir as Unidades dos Fornecedores que correspondem à sua Unidade selecionada.

Informe ou selecione o 'Fornecedor' (código ou nome), informe o  'Código da Unidade no Fornecedor' e se esta for a única correspondência para esta unidade, clique em *"Salvar"* ou *"OK"* para efetuar a gravação do registro. Caso existam outros fornecedores para o qual essa unidade será utilizada clique no ícone *"Incluir"* para gravar o registro e em seguida informar um novo fornecedor e código de unidade correspondente para esta unidade.

Para encerrar a informação dos fornecedores e unidades correspondentes a esta unidade tecle *"OK"* e o sistema automaticamente sairá da tela de cadastro e exibirá a visão  das Unidades TOTVS Colaboração cadastradas.

É importante salientar que caso o sistema não localize a unidade correspondente você poderá informá-la na tradução do XML que é executada no processo *"Inclusão de Movimento através de XML - TOTVS Colaboração"*.

Agora que já falamos sobre os cadastros necessários, vamos falar sobre o processo de importação do XML.

### 2. Parametrização

O processo *"Inclusão de Movimento através de XML - TOTVS Colaboração"* está disponível na visão de Movimentos (*"Compras > Recebimento de Materiais > Seleção do Tipo de Movimento e Filial > Processos"*) e na tela de cadastro dos XML (*"Compras > TOTVS Colaboração - Cadastro XML > Processos"*), sendo que o sistema se comportará de forma diferente dependendo da tela de onde o processo foi acionado, conforme detalharemos a seguir:

* Caso você acesse o processo diretamente da visão de movimentos  (*"Compras > Recebimento de Materiais > Seleção do Tipo de Movimento e Filial > Processos"*) o sistema entenderá que deve ser gerado um movimento do tipo que você informou ao entrar nesta tela, ou seja, o movimento será gerado de acordo com os parâmetros do tipo de movimento corrente;
* Caso você acesse o processo na tela de cadastro do XML (*"Compras > TOTVS Colaboração - Cadastro XML > Processos"*) a definição do tipo de movimento a ser gerado será através da fórmula informada no campo "Fórmula Tipo Mov. Recebimento NF-e".  Assim, optando por incluir o XML a partir desta tela o preenchimento da fórmula passa a ser obrigatório e iremos detalhá-lo a seguir:  
    
  Em*“Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > Integrações > Fiscal > Parâmetros por Filial > Informações TOTVS Colaboração”,* deverá ser preenchido por filial o campo "Fórmula Tipo Mov. p/Recebimento NF-e**"**.  
    
    
    
  Este novo parâmetro é do tipo fórmula, e assim, através do mesmo, o usuário poderá implementar uma regra específica para buscar o tipo de movimento que será utilizado tanto no recebimento automático como no recebimento manual das NF-e de cada filial.  
    
  Essa fórmula será executada para cada XML a ser recebido.  

  Foram criadas quatro novas funções de fórmula para auxiliar na criação dessa regra, são elas:

  + TABXMLCOLAB - Retorna o valor de um campo da tabela de XMLs do Totvs Colaboração (TNFEENTRADA);
  + DADOSXMLCOLAB - Retorna o valor de uma TAG de um XML;
  + QTDTAGSXMLCOLAB - Retorna o número de vezes que uma determinada Tag aparece no XML;
  + TABPRDCOLAB - Retorna o conteúdo de um campo do cadastro dos produtos vinculados aos itens constantes do XML.

  Explicaremos a seguir a sintaxe de cada uma dessas funções bem como daremos exemplos de utilização de todas elas.

  + TABXMLCOLAB ('NomeCampo', 'TipoRetorno') onde:
    - NomeCampo = Nome do Campo da Tabela TNFEENTRADA. Podemos citar como campos dessa tabela o código da coligada (CODCOLIGADA), o código da filial (CODFILIAL), o código da coligada do fornecedor (CODCOLCFO), o código do fornecedor (CODCFO), a data de emissão (DATAEMISSAO), etc.;
    - TipoRetorno = Informa o tipo de retorno relativo ao campo informado em NomeCampo, se S (string), V (valor), D (data) ou I (inteiro).

  Exemplo de fórmula de seleção do tipo de movimento utilizando a função TABXMLCOLAB:

  Neste exemplo o sistema irá verificar na tabela TNFEENTRADA (tabela que contém os XML importados) o registro gerado pelo XML e caso o código do fornecedor seja F00017 o movimento será gerado com o tipo 1.2.27, caso contrário o tipo do movimento será 1.2.20.

  + DADOSXMLCOLAB ('CaminhoTAG', 'NamespaceXML') onde:
    - CaminhoTAG = Caminho da TAG desejada, separado por barra ( / ). Exemplo: '/nfeProc/NFe/infNFe/det/prod/CFOP' para o CFOP do produto do XML;
    - NamespaceXML = <http://www.portalfiscal.inf.br/nfe>

  Exemplo de fórmula de seleção do tipo de movimento utilizando a função DADOSXMLCOLAB:

  Quando a tag possuir índice, basta informá-lo o entre colchetes ([ ]).

  No exemplo acima o sistema irá retornar a informação da TAG CFOP do primeiro item da NFe, já que não informamos nenhum índice.

  Veja abaixo um exemplo da mesma fórmula retornando o CFOP do 2º item da NFe:

  + QTDTAGSXMLCOLAB ('CaminhoTAG', 'NamespaceXML') onde:
    - CaminhoTAG = Caminho da TAG desejada, separado por barra ( / ). Exemplo: '/nfeProc/NFe/infNFe/det' para o produto do XML;
    - NamespaceXML = <http://www.portalfiscal.inf.br/nfe>

  Veja abaixo um exemplo de fórmula de seleção do tipo de movimento utilizando as funções QTDTAGSXMLCOLAB e DADOSXMLCOLAB:

  No exemplo acima através da função QTDTAGSXMLCOLAB o sistema irá identificar o número de itens constantes do XML. Após isso, através da função DADOSXMLCOLAB, irá percorrer todos os itens do XML e caso exista algum cujo CFOP seja 5.102 o tipo de movimento gerado será o 1.2.12.

  Assim, utilizando em uma mesma fórmula estas duas funções (QTDTAGSXMLCOLAB e DADOSXMLCOLAB), o sistema irá verificar determinado dado de todos os itens constantes de um XML.

  + TABPRDCOLAB ('CodigoProdutoColab', 'NomeCampo', 'TipoRetorno') onde:
    - CódigoProdutoColab = Código do Produto na tabela "Produtos TOTVS Colaboração";
    - NomeCampo = Nome do campo da tabela de Produtos;
    - TipoRetorno = Informa o tipo de retorno relativo ao campo informado em NomeCampo, se S (string), V (valor), D (data) ou I (inteiro).

  Veja abaixo um exemplo de fórmula de seleção do tipo de movimento utilizando as funções QTDTAGSXMLCOLAB, DADOSXMLCOLAB e TABPRDCOLAB:

  Neste exemplo, em primeiro lugar o sistema utilizará a função QTDTAGSXMLCOLAB para identificar o número de itens constantes do XML, logo depois, através da função DADOSXMLCOLAB irá percorrer todos os itens do XML e através da função TABPRDCOLAB irá identificar na tabela Produtos TOTVS Colaboração quais são os produtos vinculados aos itens do XML. Após verificar sua tabela de produtos e através  e irá analisar se algum deles possui a Tabela de Classificação 1 preenchida com 05. Em caso afirmativo o sistema irá gerar o movimento com o tipo 1.2.12, caso contrário o movimento será do tipo 1.2.11.

  Assim, utilizando em uma mesma fórmula estas três funções (QTDTAGSXMLCOLAB, DADOSXMLCOLAB e TABPRDCOLAB), o sistema irá verificar determinado dado de todos os itens constantes de um XML e ainda irá compará-lo com determinado campo do seu cadastro de Produtos.

    
  Caso para algum XML através da fórmula não seja possível definir o seu tipo de movimento, o XML será criado na base de dados com o status 'Inconsistente' e poderá ser recebido manualmente.  
    
  Este novo parâmetro somente será habilitado quando, no quadro “Tipo Documento Integração TOTVS Colaboração” pelo menos uma das opções, 'Todos' ou 'Recebimento de NF-e' estiver marcada.  
    
  Poderão ser definidas fórmulas diferentes para cada filial da empresa.

### 3. Importação e Gravação do XML

No processo de importação e gravação do XML o TOTVS Colaboração irá executar os seguintes procedimentos:

### 3.1. Importação de Arquivos - TOTVS Colaboração

Esse Job  é um Job Global, responsável por buscar os documentos enviados pelo ClientEDI Neogrid e distribuí-los por coligada. Neste momento, nenhuma validação é feita. Após a execução desse Job, os documentos lidos são exibidos no *“Monitor de Arquivos TOTVS Colaboração”* com o status **‘**Pendente’,  aguardando a ação do segundo Job.

O ideal é que a execução deste job seja agendada, assim, periodicamente o mesmo será executado de forma automática, buscando os XML disponibilizados.

Informamos que somente serão importados os XML que obedeçam totalmente a todos os requisitos do schema definido pela SEFAZ.

Para maiores detalhes acesse [http://tdn.TOTVS.com/display/public/LRM/CLB\_0002\_Jobs](http://tdn.totvs.com/display/public/LRM/CLB_0002_Jobs)

### 3.2. Serviço TOTVS Colaboração Consulta

Esse Job é responsável por validar o arquivo XML do documento enviado, de acordo com o tipo de documento em questão (CT-e, NF-e, NFS-e, etc.), através da chamada do serviço especifico para cada um deles. Serão verificados todos os documentos lidos pelo 1º Job. Caso o documento esteja válido, o registro do arquivo é excluído do monitor, e passa a ser exibido na tela de cadastro dos XML (*"Compras > TOTVS Colaboração - Cadastro XML"*), indicando que o mesmo foi incluído no sistema com sucesso.

O ideal é que a execução deste job seja agendada, assim periodicamente o mesmo será executado de forma automática.

Caso ocorra algum problema o XML será criado na base de dados com o status 'Inconsistente'. Para verificar o erro ocorrido, basta um duplo clique no registro para que seja exibido o seu Log onde o problema será demonstrado. Quando o arquivo está Inconsistente, é necessário corrigir a causa do erro para poder tentar incluí-lo no sistema. Após a correção do erro basta alterar o seu status para 'Pendente', através do processo *“Alterar status do arquivo TOTVS Colaboração”*e o Job tentará recebê-lo automaticamente em sua próxima execução. 

Estando o XML validado ele será incluído no cadastro de XML em *"Compras > TOTVS Colaboração - Cadastro XML"*.

### 4. Inclusão de Movimento Através de XML - TOTVS Colaboração

Conforme já dissemos o processo de Inclusão Manual de Movimento a partir de um XML  poderá ser acessado tanto a partir da visão dos movimentos de entrada como da tela do cadastro de XML. Detalharemos cada um deles a seguir.  
 

Para acessar o processo *"Inclusão de Movimento Através de XML - TOTVS Colaboração"* da visão de movimentos basta ir em *"Compras > Recebimento de Materiais > Seleção do Tipo de Movimento e Filial > Processos > Inclusão de Movimento através de XML - TOTVS Colaboração".*

   
  

O sistema irá lhe apresentar a tela de tradução do XML para que você informe quais são os XML cujos movimentos você deseja gerar. Para incluir os XML no processo basta clicar no botão *"Adicionar Nota"*.

  

O sistema lhe apresentará a tela onde você poderá filtrar os XML desejados, assim, informe o critério para seleção dos XML e atendendo ao mesmo, o sistema apresentará todos os XML válidos, do tipo NF-e, cujo destinatário é a filial informada na entrada da visão de movimentos e que ainda não geraram movimento. Marque os XML cujos movimentos você deseja gerar.

 

Você poderá selecionar vários XML para realizar suas devidas traduções, sendo que os mesmos serão apresentados ordenados através do seu ID (identificador do XML) e número da NF-e em um formato de lista. Ao navegar entre os registros, o sistema atualizará automaticamente as informações contidas nas abas *“Identificação”, “Tradução de Itens” e “Tributação”.*

  

  

Caso queira excluir algum movimento do processo, basta selecioná-lo e clicar no botão "Remover Movimento".

 

É importante salientar que quando o processo de Inclusão de Movimento Através do XML for acessado a partir da visão de movimentos, os novos movimentos serão gerados com o tipo de movimento corrente, ou seja, o tipo de movimento informado na entrada da visão.

 

Para acessar o processo *"Inclusão de Movimento Através de XML - TOTVS Colaboração"* a partir do cadastro de XML vá em *"Compras > TOTVS Colaboração - Cadastro XML" ,*selecione os XML cujos movimentos serão gerados e execute o processo *"Inclusão de Movimento através de XML - TOTVS Colaboração".*

 

Neste caso você poderá selecionar vários XML para realizar suas devidas traduções, inclusive de filiais diferentes, desde que o status dos mesmos seja 'Válido', o tipo dos mesmos seja 'NF-e' e que ainda não tenham gerado movimento. Tais XML serão apresentados na tela de tradução ordenados através do seu ID (identificador do XML) e número da NF-e em um formato de lista. Ao navegar entre os registros, o sistema atualizará automaticamente as informações contidas nas abas *“Identificação”, “Tradução de Itens” e “Tributação”.*

 

Além disso, da mesma forma que na visão de Movimentos aqui também você poderá optar por não selecionar nenhum XML específico e quando o sistema apresentar a tela de tradução você poderá informar quais são os XML cujos movimentos você deseja gerar, bastando para isso clicar no botão "Adicionar Nota", só que, neste caso, o sistema apresentará para sua seleção somente os XML que são da filial informada no contexto do sistema.

 

É importante salientar também que quando o processo de Inclusão de Movimento Através do XML for acessado a partir da tela de cadastro de XML, o tipo de movimento dos novos movimentos a serem criados será automaticamente definido pelo sistema com base na fórmula informada no campo 'Fórmula Tipo Mov. Para Recebimento de NF-e dos parâmetros de cada filial. Veja maiores detalhes no item 2 deste documento.

  

Os demais dados e procedimentos da "Inclusão de Movimento Através de XML - TOTVS Colaboração" independem de onde o processo foi acionado e iremos descrevê-los a seguir.

A aba *“Identificação”*, apresentará as informações gerais do movimento selecionado.

Serão apresentados os seguintes dados:

* Destinatário / Filial – Filial do movimento;
* Emitente / Fornecedor – Fornecedor dos produtos;
* Chave de Acesso da NF-e;
* Série da NF-e;
* Número do Documento - Número da NF-e;
* Data de Emissão da NF-e;
* Tipo de Movimento no qual a NF-e foi inserida.

Estes dados, em sua maioria, são importados do XML e nenhum deles poderá ser alterado.

Será possível vincular o XML a um movimento de pedido existente na base de dados, bastando para isso que você marque o campo 'Receber Pedido' e clique no ícone "Incluir" para informar o(s) pedido(s) que será(ão) recebido(s) para este XML.

O sistema apresentará uma tela de filtros para que você selecione o(s) pedido(s) a ser(em) vinculado(s) ao movimento, sendo que o sistema filtrará apenas os pedidos que geram movimentos do tipo de movimento que será criado.

No nosso caso, como o movimento que será gerado é do tipo 1.2.12, somente os pedidos que podem ser faturados para este tipo de movimento estarão disponíveis para realizar o vínculo.

Marque os pedidos que serão vinculados com a NF-e e clique em "OK".

O sistema irá associar os pedidos selecionados ao movimento que está sendo gerado e os apresentará na tela.

Ao ser(em) informado(s) o(s) pedido(s), o sistema imediatamente efetuará o vínculo entre a NF-e e o(s) mesmo(s), caso as informações de ambos sejam correspondentes. 

Outros pedidos de compras poderão ser adicionados a qualquer momento.

Na aba*"Identificação"*será informado ainda se a tela de edição do movimento será aberta ao fim do processo e se consequentemente o movimento poderá ser editado nesse momento.

Assim, caso queira optar por abrir o movimento automaticamente logo após a sua tradução basta deixar que o campo 'Abrir a Edição do Movimento', permaneça marcado, visto que o mesmo já virá assinalado por default.

do Movimento'.

Caso este campo seja desmarcado, o sistema efetuará a inclusão através do XML  e retornará para a tela do cadastro de XML ou para a visão de Movimentos conforme a tela de onde o processo foi acionado.

Vejamos as demais abas do processo:

Na aba *"Tradução de Itens"* serão apresentados os dados relativos aos itens da NF-e.  
Caso o XML não esteja vinculado a um pedido o sistema apresentará além dos dados do item no XML, a Unidade de Tradução, o Código do Produto de Tradução e o Nome do Produto de Tradução, ou seja os dados do produto correspondente em sua base de dados. O sistema verificará essas informações nas tabelas "Unidades TOTVS Colaboração" e "Produtos TOTVS Colaboração".

Caso ao verificar estas tabelas o sistema não encontre os dados correspondentes aos produtos constantes do XML, você poderá neste momento efetuar manualmente a tradução dos itens e as informações fornecidas por você serão automaticamente inseridas nestas tabelas. 

Para informar qual é o produto da sua base de dados que é correspondente ao produto constante do XML clique no campo 'Produto Tradução' e clique na seta da lista de opções. O sistema abrirá um lookup onde você poderá selecionar o produto desejado através da informação do código ou do nome do mesmo.

Conforme a informação fornecida o sistema lhe apresentará a lista dos produtos disponíveis na sua base de dados e que atendem à seleção informada.

O produto selecionado irá para a tela de*"Tradução de Itens"* e automaticamente será gravado pelo sistema na tabela*"Produtos TOTVS Colaboração"*.

O mesmo processo poderá ser efetuado para as unidades de medida existentes no XML e que não tenham sido traduzidas pelo sistema.

Além de incluir produtos e unidades que não foram traduzidos você poderá alterar os dados que o sistema trouxe na tradução optando por um outro produto ou unidade diferentes daqueles indicados pelo sistema, bastando para isso clicar nos campos 'Unidade Tradução' ou 'Produto Tradução' e fornecer as informações desejadas.

Caso o XML esteja vinculado a pedido(s) os campos 'Código do Produto de Tradução' e 'Produto Tradução' permanecerão em branco e o sistema apresentará além dos dados do item no XML, os campos relativos ao Pedido. Estes dados também serão preenchidos com base no conteúdo das tabelas*"Unidades TOTVS Colaboração"* e *"Produtos TOTVS Colaboração"*.

Assim, caso o campo "Receber Pedido" esteja marcado, os quatro campos referentes ao pedido (Número do Pedido, Código do Produto do Pedido, Número Sequencial do Item no Pedido e o Nome do Produto do Pedido) serão exibidos na aba*"Tradução de Itens".*

Caso durante o processo de Inclusão do Movimento via XML, o campo "Receber Pedido" seja, em algum momento, desmarcado, os campos referentes ao pedido (Número do Pedido, Código do Produto do Pedido, Número Sequencial do Item no Pedido e o Nome do Produto do Pedido) não mais serão apresentados em tela, já que não haverá a necessidade de utilização dos mesmos.

Você poderá alterar o produto do pedido que foi informado pelo sistema, bastando para isso, selecionar o item cujo produto do pedido deseja alterar, clicar no campo 'Produto no Pedido' e clicar na seta da lista de opções para que os produtos dos pedidos vinculados ao XML sejam apresentados.

 Clique então no botão do lookup do produto.

 O lookup exibirá o(s) produto(s) do(s) pedido(s) de compra vinculado(s) ao XML, e que ainda possuem saldo a receber, para que você selecione um deles.  
 

Se nesse momento ainda existir algum item no XML cuja tradução ainda não consta da tabela*"Produtos TOTVS Colaboração"*o sistema não conseguirá localizá-lo nos pedidos vinculados, mas você poderá informar a tradução diretamente nesta tela.

Caso selecione o produto a partir do campo  'Produto Tradução' o sistema exibirá todos os registros da base para que você possa definir qual produto será utilizado na amarração, já se o produto existir em um dos pedidos vinculados clique no campo 'Produto do Pedido' e o lookup exibirá todos os produtos do(s) pedido(s) de compra vinculado(s) ao XML, e à medida em que a tradução estiver sendo realizada, o sistema irá consumir o saldo dos pedidos até que os mesmos sejam zerados.

Outro recurso disponível na aba *"Tradução de Itens"*é o botão "Múltiplos".

O botão Múltiplos poderá ser utilizado quando o pedido selecionado pelo sistema não possuir quantidade suficiente para realizar a tradução do produto.

Assim, ao clicar no botão "Múltiplos", será criada uma réplica da linha selecionada para que o produto possa ser associado a outro registro.

Vamos considerar o nosso exemplo, onde o produto '6.0.0.01.8373'  no XML tem a quantidade 1,00, tendo sido 0,50 solicitada no pedido 26790 e mais 0,50 solicitada no pedido 111111 sendo que ambos os pedidos foram vinculados ao XML.

Na tela de *"Tradução de Itens"*o sistema relacionará o item sempre ao primeiro pedido vinculado ao XML.

Poderemos informar então que a quantidade restante no XML foi consumida no pedido 111111.

Para isso selecione o produto e clique no botão "Múltiplos".

 

No registro já existente o sistema irá alterar a quantidade recebida para o produto, informando a quantidade total do pedido vinculado ao item, e irá inserir um novo registro com o produto e sua quantidade restante.

A partir daí você irá proceder da mesma forma que na alteração do pedido, ou seja, clique no campo 'Produto no Pedido' e clique na seta da lista de opções.

Clique então no ícone do lookup do produto.

O lookup exibirá o(s) produto(s) do(s) pedido(s) de compra vinculado(s) ao XML, e que ainda possuem saldo a receber para que você selecione um deles.

Ao ser selecionado o pedido, seus dados automaticamente irão para a aba *"Tradução de Itens".*

Na aba *“Tributação de Itens”* serão exibidos todos os tributos parametrizados no tipo de movimento do movimento que será gerado.

Na parte superior da tela, em *“Tributação da Nota”* serão carregadas as informações relativas aos tributos do movimento.

Na parte inferior da tela a visão contida no grupo*“Tributação dos Produtos”*será responsável por exibir os impostos dos produtos (itens de movimento).

O preenchimento dos valores relativos aos tributos (base de cálculo, alíquota e valor) será efetuado obedecendo à configuração do campo 'Busca Valores TOTVS Colab' do respectivo tipo de movimento.

Para verificar a sua configuração vá em*"Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > 04.06 - Gestão Compras > 04.06.05 - Recebimentos de Materiais"*e no tipo de movimento desejado consulte este campo em*"Fis - Tributação - Item" e 'Fis - Tributação - Movimento"*.

O sistema informará os valores conforme o preenchimento do campo 'Busca Valores TOTVS Colab' com uma das opções a seguir:

* XML: Esta opção deverá ser selecionada caso deseje que os valores do tributo sejam aqueles recebidos do arquivo XML da NF-e, sem a necessidade de comparação com o tipo de movimento;
* Tipo de Movimento - Não comparar com XML: Esta opção deve ser selecionada caso deseje que todas as informações do tributo sejam calculadas/buscadas pelo sistema conforme a parametrização do tipo de movimento, sem a necessidade de comparação com os valores advindos do arquivo XML;
* Tipo de Movimento - Comparar com XML: Esta opção deve ser selecionada caso deseje que todas as informações do tributo sejam calculadas/buscadas pelo sistema, mas elas devem ser comparadas com as informações advindas do XML. Caso tenha optado por executar esse processo sem abrir a edição do movimento, caso existam diferenças entre os tributos calculados e os constantes do XML, ao final da execução o sistema irá lhe apresentar uma mensagem com essa informação, bastando que você vá à edição do movimento se quiser alterar os valores que foram calculados. Já caso tenha optado por executar esse processo e 'Abrir a Edição do Movimento' quando for solicitada a gravação do movimento o sistema abrirá a tela com a diferença dos tributos caso existam. Detalharemos essa opção mais a frente.

Para finalizar a execução da rotina *"Inclusão de Movimento através de XML - TOTVS Colaboração"* realizando a inclusão do movimento, basta em qualquer uma das telas do processo clicar no botão 'Executar'.

   
 

 Se o campo 'Abrir Edição do Movimento' não estiver marcado o sistema efetuará a execução do processo.

Caso tenha optado por não 'Abrir a Edição do Movimento' após a execução do processo o sistema apresentará a tela com o resultado do processamento:

Se os tributos do tipo de movimento estiverem parametrizados como "Tipo de Movimento - Comparar com XML" e for encontrada alguma diferença entre os valores calculados pelo sistema e os valores constantes do XML o movimento será incluído normalmente mas ao final do processo o sistema avisará e apresentará o identificador do movimento onde a divergência foi detectada.

Caso tenha optado por 'Abrir a Edição do Movimento', ao executar o processo, o sistema automaticamente abrirá a tela do movimento que está sendo gerado. 

Você poderá acessar as abas do movimento e conforme suas permissões de acesso poderá incluir dados ou alterar os dados existentes.

Após finalizar a visualização e/ou edição do movimento basta clicar em *"Salvar"* ou em *"OK"*.

Caso no tipo de movimento do movimento que está sendo gerado o campo 'Busca Valores TOTVS Colab' dos tributos esteja configurado para "Tipo de Movimento - Comparar com XML" o sistema abrirá a tela com as diferenças dos tributos caso existam.

Caso seja necessário basta clicar na coluna 'Valor Correto' e alterar para o valor constante do XML e clicar em Salvar.

Caso vá manter os valores que foram calculados pelo sistema conforme parametrizado no tipo de movimento basta clicar em 'Salvar' e o sistema finalizará a execução do processo efetuando a gravação do movimento.

Em caso de posterior exclusão do movimento de NF-e criado, o XML em questão será desvinculado do movimento e voltará ao status anterior à inclusão, para que seja possível vincular um novo movimento ao mesmo.

 

divs
