---
content_hash: 3cc378a02b612e2f80a6db513bd8e7bc269fff04903fef022427c6efadb0bcc9
fetched_at: '2026-06-29T00:11:48.495278+00:00'
page_id: '82477122'
product: rm
source: tdn-rm
title: Conceito - Como parametrizar
type: documentation
url: https://tdn.totvs.com/display/LRM/Conceito+-+Como+parametrizar
version: 13
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Conector                       **Versão:**11.50 |
| **Processo** | **:** | Conceito - Parametrização |
| **Subprocesso** | **:** |  |
| **Data da publicação** | **:** | 07/10/2013 |

        No TOTVS Business Conector existe uma ferramenta chamada Conceito. Por meio dela é possível importar e exportar dados de uma conexão origem para uma conexão destino. Também guarda quais campos de cada sistema estão envolvidos na integração, e quais as correspondências entre os atributos de origem e destino.

**Identificação**

Na aba Identificação existem diversos campos a serem preenchidos, com o objetivo de configurar e identificar o conceito que esta sendo criado.

No canto esquerdo da visão, estão disponíveis para configuração os campos:

**- Nome do Conceito:** nome do conceito que está sendo criado. O nome facilita a identificação do conceito a partir da tela de visão.

**- Código do Sistema:** É possível relacionar um sistema a um determinado conceito, por exemplo, o conceito que trabalha rotinas financeiras pode ser relacionado ao sistema financeiro.

**- Descrição/Observações:** Pode-se informar uma breve descrição sobre o conceito criado.

Abaixo destes campos, se encontram os botões:

**- Carregar:** permite importar um conceito a partir de um arquivo no formato \*.icp.

**- Gravar:** permite exportar o conceito para um arquivo no formato \*.icp.

Na parte direita da visão, estão disponíveis os campos:

**- Registros por transação:** determina quantos registros da tabela raiz devem ser processados antes de se atualizar o banco destino.

**- Substituir Registros:** indica se a importação deve atualizar registros existentes ao invés de somente incluir novos registros.

**- Excluir Registros:** indica se a importação deve excluir registros na base destino.

**- Marca de Exclusão:** valor a ser pesquisado em campos de controle de exclusão para se apagar um registro.

*Observação:* estas configurações terão impacto apenas na Conexão Origem.

**- Filtro:** filtro incremental do processo de importação.

*Observação:* esta configuração terá impacto apenas na Conexão Origem.

**- Versão:** versão do conceito.

**- Início da Validade:** data de início da validade do conceito.

**Conexões Origem**

---

Na aba Conexões Origem são criadas as conexões com a aplicação origem. Estão disponíveis os botões:

**- Criar:** Para inserir uma conexão de origem.

**- Excluir:** Para excluir uma conexão de origem.

**- Testar:** Para testar se a conexão de origem está válida, após finalizar a configuração da mesma

Ao criar uma conexão, é necessário informar o nome da mesma e o tipo, e preencher as propriedades correspondentes de cada um.

A conexão de origem pode ser do tipo:

* Arquivo Texto
* Arquivo XML
* Banco de Dados
* Data Server
* MS CRM (Microsoft CRM)

A Seguir será mostrado todos os tipos de Conexões de Origem e suas devidas Configurações e a Saída de cada uma respectivamente.

**1º Exemplo agora é de uma Conexão Origem ( Banco de Dados )**

**Conexão Destino ( Arquivo TXT )**

**Clicar em Criar**

**1º ) Conexão Origem ( Banco de Dados )**

Busca os dados de um determinado banco de dados.

Queries

Informa a consulta SQL que será executada no Banco de Dados – Neste exemplo é uma consulta que informa os dados de um Cliente Fornecedor.

Clicar no Loockp Box

Selecionar o primeiro campo : SQL

SELECT CODCOLIGADA, CODCFO, NOME , ESTADOCIVIL FROM FCFO

Consulta inserida

Informa a Coligada , o código do Cliente fornecedor , nome e Estado civil do Cliente fornecedor.

Nome : Informar o nome da Query , neste exemplo : qry\_Fornecedor

Provedor : Selecionar a opção ( SqlClient Data Provider )

Observação: caso a base de origem ou destino seja MySql, deverá ser baixado o driver ADO.NET Driver for MySql pelo link <http://www.mysql.com/products/connector/>. Após a instalação do driver o computador deve ser reiniciado para que a opção MySql Data Provider seja disponibilizada no campo Provedor.

String de Conexão: Clicar no Loockp para selecionar a conexão com o banco de dados ( Servidor e Nome do Banco de dados )

Em Security , deve conter os seguintes dados:

**Password** : rm ( Senha do banco de dados )

**User ID** : rm ( Usuário do banco de dados )

Em Source , informar o Servidor e Banco de dados:

**Data Source:**  Servidor do Banco de Dados ... Exemplo ( T000000147\T000000147 )

**Initial Catalog:** Banco de dados ... Exemplo ( Exemplo1180 )

Após inserir as devidas configurações , clicar em Salvar e ( Testar )

**Conexão Destino**

Nesta aba serão informados todos os dados para estabelecer a conexão com a aplicação de destino. Semelhante a Conexões Origem, essa conexão poderá ser de diversos tipos, sendo necessário informar as propriedades correspondentes de cada um.

Estão disponíveis os botões:

**- Criar:** Para inserir uma conexão de destino.

**- Excluir:** Para excluir uma conexão de destino.

**- Testar:** Para testar se a conexão de destino está válida, após finalizar a configuração da mesma

Ao criar uma conexão, é necessário informar o nome da mesma e o tipo, e preencher as propriedades correspondentes de cada um. A conexão de destino pode ser do tipo:

* Arquivo Texto
* Arquivo XML
* Banco de Dados
* Data Server
* MS CRM (Microsoft CRM)
* Web Service

**Neste nosso exemplo a saída dos dados será arquivo TXT**

Tipo : Arquivo Texto

Parametrizações Necessárias

**Tipo :**  Pode ser Fixo ou Delimitado , no caso de Delimitado deve-se possuir um Delimitador de Campos

Neste exemplo o Tipo definido foi : Delimitado

Delimitador de campos : /

Em tabelas , Clicar no Loockp para que possa incluir as tabelas no arquivo TXT e possa ser feito depois o vínculo em Correspondências.

Nova

Lookup em Campos

Add

Inserido os quatro campos que estão na Query do Banco de Dados, observação importante , sempre lembrar de informar a Chave Primária Obrigatório para os campos, neste exemplo criado acima , a Chave Primária Obrigatória ficou em ( Codcoligada e Codcfo ).

Nome : FCFO

Ficou desta forma após salvar

Em Arquivo : Informar um caminho válido , neste exemplo C:\Astoni\ e o nome na qual será salvo o arquivo TXT após ser processado o conceito...

E em Nome : Informar o nome da Conexão destino.

**Estrutura Origem e Estrutura Destino**

Nas abas Estrutura Origem e Estrutura Destino estão disponíveis "Tabelas" das conexões (Origem e Destino) definidas nas abas anteriores. Elas deverão ser indicadas, bem como as propriedades de cada campo.

A visão da Estrutura (Origem e Destino) é dividida em:

* Tabelas Disponíveis
* Tabelas de Importação
* Campos de Configurações (Tabelas e Campos)

**Tabelas Disponíveis**

Todas as tabelas definidas na Conexão deverão ser apresentadas neste campo.

**Tabelas de Importação**

As tabelas selecionadas no campo Tabelas Disponíveis e que forem adicionadas à estrutura, podem ser visualizadas no campo Tabelas de Importação. Estão disponíveis os botões:

**- Adicionar:** Para adicionar uma tabela à estrutura, selecione a tabela desejada no campo Tabelas Disponíveis, e ao clicar no botão Adicionar será aberta uma janela onde é possível definir quais os campos da tabela serão adicionados.

**- Remover:** Remove um campo da tabela ou a tabela que foi adicionada ao campo Tabelas de Importação, de acordo com a seleção.

**- Limpar:** Limpa todas as Tabelas de Importação incluídas, deixando em branco para que uma nova seja criada.

**- Carregar:** Permite importar uma Estrutura a partir de um arquivo no formato \*.tst.

**- Gravar:** Permite exportar uma Estrutura para um arquivo no formato \*.tst.

**- Atualizar:** Quando alguma alteração for feita via banco e um novo campo for incluído pra tabela já utilizada, deve-se clicar no ícone Atualizar para que seja carregado esse novo campo nas opções.

**Campos de Configurações**

Tabelas

Ao selecionar uma tabela, no quadro Tabelas de Importação, na parte inferior da visão são mostrados os campos para configuração da tabela selecionada. Alguns campos aparecem para todos os tipos de conexão:

**- Filtro Estático:** Filtro da tabela para importação.

**- Detalhes:** Tabelas selecionadas com detalhes da tabela ativa.

**- Mestre:** Tabela mestre da tabela ativa.

**- Alias:** Alias atribuído à tabela para o processo de importação.

**- Campos:** Campos selecionados da tabela.

**- Conexão:** Campo somente leitura, que informa a conexão de origem da tabela.

**- Nome**: Nome da tabela na fonte de dados. O nome deve sempre começar com " qry\_ ".

**- Tipo da Tabela:** Campo somente leitura que informa se a tabela é fonte ou origem de dados na importação.

Quando a Conexão criada (Origem ou Destino) for do tipo Banco de Dados, além dos campos citados, também está disponível nos campos da Estrutura (Origem ou Destino) o campo:

**- SQL:** Informe a sentença SQL.

Campos

Ao selecionar um campo da tabela em Tabelas de Importação, são apresentados na parte inferior da visão as opções para configuração do campo. As opções são iguais para todos os campos, independente do tipo da conexão. São elas:

**- Entrada:** Ponto de entrada da operação ou campo.

**- Controle de Exclusão:** Indica se o campo deve ser utilizado para controle de exclusão. Este parâmetro deve trabalhar em conjunto com o parâmetro Controle de Exclusão da aba Identificação.Ao informar no parâmetro da aba Identificação qual campo será utilizado como controle, é importante na aba Estrutura selecionar o campo informado e configurar este parâmetro como True. Caso contrário o conceito que utilizar este parâmetro não irá funcionar corretamente.

*Observação*: Importante observar que as propriedades “Entrada” e “Controle de Exclusão” embora disponíveis também na Estrutura Origem, fazem sentido serem configuradas apenas na Estrutura Destino.

**- Auto Incremento:** Informe se o campo é um campo de auto-incremento gerenciado pelo banco.

**- Chave Primária:** Informe se o campo é parte da chave primária da tabela.

**- Obrigatório:** Informe se o campo é obrigatório ou se pode receber valores nulos.

**- Somente Leitura:** Informe se o campo permite ou não gravação de dados.

**- Valor default:** Informe o valor assumido pelo campo quando nenhum outro valor for atribuído.

**- Alias:** Informe o alias atribuído ao campo no processo de importação.

**- Descrição:** Informe notas ou observações acerca do campo.

**- Nome:** Informe o nome do campo na fonte de dados.

**- Tabela:** Campo somente leitura, onde é possível visualizar o nome da tabela à qual o campo pertence.

**- Campo PK Referencia:** Determina o nome do campo PK referenciado por este campo.

**- Campo Referencia:** Determina o nome do campo referenciado por este campo.

**- Entidade Referencia:** Determina o nome da entidade referenciada por este campo.

**Neste nosso exemplo a Estrutura de Origem , encontramos a Query criada no Banco de Dados para consulta de FCFO com os campos ( CODCOLLIGADA – CODCFO – NOME – ESTADOCIVIL )**

Não esquecendo de Selecionar os campos principais e informar que são de Chave primária e Obrigatório, neste caso foram selecionados os campos : CODCOLIGADA e CODCFO

ESTRUTURA DESTINO

Mesmo processo , buscando os campos criados na hora de configurar a Conexão destino e com as devidas chaves primárias já cadastradas.

Efetuada as correspondências – Clicar em Salvar em Seguida

Processos > Processar conceito

Sim

Arquivo TXT criado corretamente no caminho selecionado nos parâmetros.

Delimitado com ( / ) como delimitador dos Campos conforme configuração

**2º Exemplo agora é de uma Conexão Origem ( Banco de Dados )**

**Conexão Destino ( Banco de Dados )**

Teste realizado primeiramente via SQL para verificar os dois Bancos de dados

**Consulta SQL inserida na Conexão Origem e Destino:**

SELECT CODCOLIGADA, CODCFO , NOME , ESTADOCIVIL, PAGREC, ATIVO,PESSOAFISOUJUR,IDCFO ,TIPOCONTRIBUINTEINSS FROM FCFO

Ao rodar na base de dados : Exemplo1180 a consulta teve o retorno de vários Clientes Fornecedores....

A Mesma consulta feita na base de dados : Vazia1180 não teve retorno algum.

O Conceito após pronto e processado , pegará todos os dados da consulta do Banco de dados Exemplo1180 e importará para o banco de dados Vazia1180.

Criar o novo conceito

**Clicar em Criar**

**1º ) Conexão Origem ( Banco de Dados )**

Busca os dados de um determinado banco de dados.

Queries

Informa a consulta SQL que será executada no Banco de Dados – Neste exemplo é uma consulta que informa os dados de um Cliente Fornecedor.

Clicar no Loockp Box

Selecionar o primeiro campo : SQL

SELECT CODCOLIGADA, CODCFO , NOME , ESTADOCIVIL, pagrec, ATIVO,PESSOAFISOUJUR,IDCFO ,TIPOCONTRIBUINTEINSS FROM FCFO

Consulta inserida

Nome : Informar o nome da Query , neste exemplo : qry\_FCFOBD

Provedor : Selecionar a opção ( SqlClient Data Provider )

Observação: caso a base de origem ou destino seja MySql, deverá ser baixado o driver ADO.NET Driver for MySql pelo link <http://www.mysql.com/products/connector/>. Após a instalação do driver o computador deve ser reiniciado para que a opção MySql Data Provider seja disponibilizada no campo Provedor.

String de Conexão: Clicar no Loockp para selecionar a conexão com o banco de dados ( Servidor e Nome do Banco de dados )

Em Security , deve conter os seguintes dados:

**Password** : rm ( Senha do banco de dados )

**User ID** : rm ( Usuário do banco de dados )

Em Source , informar o Servidor e Banco de dados:

**Data Source:**  Servidor do Banco de Dados ... Exemplo ( T000000147\T000000147 )

**Initial Catalog:** Banco de dados ... Exemplo ( Exemplo1180 )

Após inserir as devidas configurações , clicar em Salvar e ( Testar )

**Conexão Destino ( Informar neste campo a base de dados : Vazia1180 )**

Informar a Query para que seja feita a Correspondência

Query idêntica á criada na Base de dados : Exemplo1180 ( Conexão Origem )

Ficou desta forma o nome da Query da conexão Destino : FCFO1

Provedor  : SqlClient Data Provider

Observação: caso a base de origem ou destino seja MySql, deverá ser baixado o driver ADO.NET Driver for MySql pelo link <http://www.mysql.com/products/connector/>. Após a instalação do driver o computador deve ser reiniciado para que a opção MySql Data Provider seja disponibilizada no campo Provedor.

Em String de Conexão: Informar os dados para conexão com o Banco de dados na qual será importados os dados da Conexão Origem.

Security

**Password** : rm ( Informar a senha do Banco de dados Destino )

**User ID** : rm ( Informar o usuário do Banco de dados Destino )

Source

**Data Source** : Informar o Servidor na qual encontra-se restaurado o Banco de Dados ( Destino )

Exemplo : T000000147\T000000147

**Initial Catalog** : Nome do banco de dados ( Destino ) Exemplo : Vazia1180

Inserir o nome da Conexão Destino , Salvar e em seguida : Testar

Estrutura Origem

Na estrutura de origem , devemos localizar a Query criada nos parâmetros da Conexão de Origem e em seguida clicar em Adicionar.   
 Após feito isto , selecionar os campos principais e marcar como Chave Primária e Obrigatório.

Estrutura Destino

Na estrutura de Destino devemos localizar a Query criada nos parâmetros da Conexão destino e em seguida clicar em Adicionar.

Após feito isto , selecionar os campos principais e marcar como Chave Primária e Obrigatório.

Correspondências

Após feitas todas as correspondências , clicar em Salvar e em seguida :

Processos > Processar Conceito

Após Processar , voltar a efetuar a Consulta SQL no Banco de Dados .. Vazia1180

Importado os campos da Base Exemplo1180 para Vazia1180

**3º Exemplo agora é de uma Conexão Origem ( Banco de Dados )**

**Conexão Destino ( XML )**

Nome do Conceito : Informar o nome do Conceito que será utilizado para envio de dados da Base de Dados para o arquivo XML.

Criada a Conexão Origem com a Query.

SELECT CODCOLIGADA, CODCFO , NOME ,  pagrec, ATIVO,PESSOAFISOUJUR,IDCFO ,TIPOCONTRIBUINTEINSS FROM FCFO

**Provedor** : Informar a opção :SqlClient Data Provider

**String de Conexão** : Informar o Servidor e Banco de Dados Origem ( Parametrização mostrada nos prints Anteriores )

**Nome** : Informar o nome do Conceito

Na conexão do tipo Arquivo XML estão disponíveis para parametrização os campos:

**- Texto XSD:** Informe o texto schema no formato XSD. Ao clicar no lookup para informar o texto XSD é aberta uma visão na qual é possível digitar o texto schema, ou abrir o arquivo XSD para que o texto seja carregado.

**- Arquivo XML:** Informe o caminho completo e o nome do arquivo XML.

**- Tabela Principal:** Selecione a tabela principal, apenas para conexão de origem.

**- Nó Raiz:** Caso a consulta de origem tenha como retorno múltiplo registros, informe neste campo o nó raiz.

Inserir o arquivo XSD

<?xml version="1.0" encoding="utf-8"?>

<[xs:schema](http://xsschema) xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" xmlns:msprop="urn:schemas-microsoft-com:xml-msprop" xmlns:xs="http://www.w3.org/2001/XMLSchema">

    <[xs:element](http://xselement) name="FCFO">

        <[xs:complexType](http://xscomplexType)>

            <[xs:all](http://xsall)>

                <[xs:element](http://xselement) name="CODCOLIGADA"></[xs:element](http://xselement)>

                <[xs:element](http://xselement) name="CODCFO"></[xs:element](http://xselement)>

                <[xs:element](http://xselement) name="NOME"></[xs:element](http://xselement)>

                <[xs:element](http://xselement) name="PAGREC"></[xs:element](http://xselement)>

                <[xs:element](http://xselement) name="ATIVO"></[xs:element](http://xselement)>

                <[xs:element](http://xselement) name="PESSOAFISOUJUR"></[xs:element](http://xselement)>

                <[xs:element](http://xselement) name="IDCFO"></[xs:element](http://xselement)>

                <[xs:element](http://xselement) name="TIPOCONTRIBUINTEINSS"></[xs:element](http://xselement)>

            </[xs:all](http://xsall)>

        </[xs:complexType](http://xscomplexType)>

    </[xs:element](http://xselement)>

</[xs:schema](http://xsschema)>

Esquema inserido

Detalhes Principais do Esquema...

<[xs:element](http://xselement) name="FCFO">  **( Tabela FCFO que ficará visível em Estrutura Destino )**

        <[xs:complexType](http://xscomplexType)>

            <[xs:all](http://xsall)>

    <[xs:element](http://xselement) name="CODCOLIGADA"></[xs:element](http://xselement)>           ( Campo da Tabela )

    <[xs:element](http://xselement) name="CODCFO"></[xs:element](http://xselement)>                ( Campo da Tabela )

    <[xs:element](http://xselement) name="NOME"></[xs:element](http://xselement)>                  ( Campo da Tabela )

    <[xs:element](http://xselement) name="PAGREC"></[xs:element](http://xselement)>                ( Campo da Tabela )

    <[xs:element](http://xselement) name="ATIVO"></[xs:element](http://xselement)>                 ( Campo da Tabela )

    <[xs:element](http://xselement) name="PESSOAFISOUJUR"></[xs:element](http://xselement)>        ( Campo da Tabela )

    <[xs:element](http://xselement) name="IDCFO"></[xs:element](http://xselement)>                 ( Campo da Tabela )

    <[xs:element](http://xselement) name="TIPOCONTRIBUINTEINSS"></[xs:element](http://xselement)>  ( Campo da Tabela )

O esquema foi criado com a Tabela **FCFO** e os campos **CODCOLIGADA , CODCFO, NOME , PAGREC, ATIVO , PESSOAFISOUJUR, IDCFO E TIPOCONTRIUINTEINSS** , pois a consulta SQL ( Query criada na Conexão Origem ( Banco de dados ) foi : SELECT **CODCOLIGADA,CODCFO,NOME,PAGREG,ATIVO,PESSOAFISOUJUR,IDCFO ,TIPOCONTRIBUINTEINSS**  FROM FCFO

Desta forma no ato da Correspondência ocorre sem inconsistências.

Em : Arquivos XML , deve-se colocar um caminho válido da Rede e o nome do Arquivo XML conforme é visualizado abaixo e lembrando que o caminho tem que estar compartilhado.

O Arquivo X1.XML criado tem que estar com a seguinte formatação ..

<?xml version="1.0"?>

<FCFO>   ( Tabela Criada )

    <CODCOLIGADA></CODCOLIGADA>                                   ( Campo da Tabela )

    <CODCFO></CODCFO>                                                              ( Campo da Tabela )

    <NOME></NOME>                                                                       ( Campo da Tabela )

    <PAGREC></PAGREC>                                                               ( Campo da Tabela )

    <ATIVO></ATIVO>                                                                      ( Campo da Tabela )

    <PESSOAFISOUJUR></PESSOAFISOUJUR>                            ( Campo da Tabela )

    <IDCFO></IDCFO>                                                                       ( Campo da Tabela )

    <TIPOCONTRIBUINTEINSS></TIPOCONTRIBUINTEINSS>( Campo da Tabela )

</FCFO>

**Observação1 :** Por ser um arquivo XML de Destino , os campos devem estar em branco , apenas abrindo e fechando em seguida como é visualizado abaixo:

<CODCOLIGADA>( **Espaço tem que ficar em Branco**)</CODCOLIGADA>

**Observação2:** A estrutura do Arquivo XML , tem que estar da mesma forma da estrutura do Esquema : Arquivo XSD

**Visualizar exemplo abaixo :**

<[xs:element](http://xselement) name="FCFO">  **( Tabela FCFO que ficará visível em Estrutura Destino )**

        <[xs:complexType](http://xscomplexType)>

            <[xs:all](http://xsall)>

    <[xs:element](http://xselement) name="CODCOLIGADA"></[xs:element](http://xselement)>           ( Campo da Tabela )

    <[xs:element](http://xselement) name="CODCFO"></[xs:element](http://xselement)>                ( Campo da Tabela )

    <[xs:element](http://xselement) name="NOME"></[xs:element](http://xselement)>                  ( Campo da Tabela )

    <[xs:element](http://xselement) name="PAGREC"></[xs:element](http://xselement)>                ( Campo da Tabela )

    <[xs:element](http://xselement) name="ATIVO"></[xs:element](http://xselement)>                 ( Campo da Tabela )

    <[xs:element](http://xselement) name="PESSOAFISOUJUR"></[xs:element](http://xselement)>        ( Campo da Tabela )

    <[xs:element](http://xselement) name="IDCFO"></[xs:element](http://xselement)>                 ( Campo da Tabela )

    <[xs:element](http://xselement) name="TIPOCONTRIBUINTEINSS"></[xs:element](http://xselement)>  ( Campo da Tabela )

**<FCFO>**   ( Tabela Criada )

    <CODCOLIGADA></CODCOLIGADA>                                   ( Campo da Tabela )

    <CODCFO></CODCFO>                                                              ( Campo da Tabela )

    <NOME></NOME>                                                                       ( Campo da Tabela )

    <PAGREC></PAGREC>                                                               ( Campo da Tabela )

    <ATIVO></ATIVO>                                                                      ( Campo da Tabela )

    <PESSOAFISOUJUR></PESSOAFISOUJUR>                            ( Campo da Tabela )

    <IDCFO></IDCFO>                                                                       ( Campo da Tabela )

    <TIPOCONTRIBUINTEINSS></TIPOCONTRIBUINTEINSS>( Campo da Tabela )

**</FCFO>**

Em Tabela Principal : é visualizada a Tabela no arquivo XML criada e neste nosso exemplo é a Tabela FCFO

Nó Raiz , é informado um Campo da Tabela pois a  consulta de origem tenha como retorno múltiplo registros e é informado o campo : CODCOLIGADA

E abaixo o Nome da Conceito ( Conexão Destino ).

Após efetuar a configuração , clicar em Salvar e Testar em Seguida...

Estrutura Origem

Pesquisa a Query inserida no Conexão de Origem ( Banco de Dados ) Adicionar e em seguida Selecionar os principais campos e informar que são de Chave Primária e Obrigatório.

Estrutura Destino

Aparece a Tabela FCFO criada no início do arquivo XML e os campos ao lado , e após adicionar não esquecer de marcar os principais campos e selecionar quais são Chave Primária e Obrigatório.

Correspondências

Após efetuar todas as correspondências e Salvar ..

Clicar em : Processos > Processar conceito

Criado o arquivo XML : X11.XML

Arquivo carregado com a informação da Base de Dados Origem corretamente ..

**4º Exemplo agora é de uma Conexão Origem ( XML )**

**Conexão Destino ( Banco de Dados )**

Criar um novo Conceito , e em seguida selecionar a Opção : Conexão Origem

Inserir o arquivo XSD.

Arquivo inserido e validado ..

Conforme os testes anteriores , Esquema criado com a estrutura :

Tabela : FCFO

Campos : CODCOLIGADA – CODCFO – NOME – PAGREC – ATIVO – PESSOAFISOUJUR – IDCFO – TIPOCONTRIBUINTEINSS

Arquivo XML : Informar o Caminho completo onde encontra-se o Arquivo XML

Neste caso o arquivo XML tem que estar preenchido , por se tratar de Conexão Origem

Neste exemplo os campos são preenchidos com as seguintes informações.

CODCOLIGADA = 1

CODCFO = F02235

NOME = TESTE CONCEITO ASTONI

PAGREC = 2

ATIVO = 1

PESSOAFISOUJUR = F

IDCFO = 2974

TIPOCONTRIUINTEINSS = 0

Importante lembrar que : CODCFO / ICDFO neste caso não pode existir na Base de Dados Destino  como é mostrado abaixo por consulta SQL..

Não  existe no Banco de dados..

A seguir configurar os campos : Tabela Principal que é criada no Arquivo XML o campo principal CODCOLIGADA em Nó Raiz e o Nome da Conexão Origem.

Conexão Destino

Inserido os dados de configuração do Banco de Dados Destino.. ( Configuração já mostrada nos passos anteriores para Banco de Dados )

**Queries** : Inserida a Query

SELECT CODCOLIGADA,

       CODCFO ,

       NOME ,

       pagrec,

       ATIVO,

       PESSOAFISOUJUR,

       IDCFO ,

       TIPOCONTRIBUINTEINSS

FROM FCFO

**Provedor** : SqlClient Data Provider

**String de Conexão** : Informar o Servidor e Banco de Dados que irá receber os dados do arquivo XML

**Nome :** Nome da Conexão Destino

Estrutura Origem

Tabela Disponíveis , é informada a Tabela FCFO que foi criada no arquivo XML .. Adicionar , após selecionar os campos principais e em seguida marcar como Chave Primária e Obrigatório.

Estrutura Destino

Localizar a Query com a consulta SQL que busca os campos a serem preenchidos , Adicionar, após isto , selecionar os campos que serão Chave Primária e Obrigatórios.

Correspondências

Após efetuar as correspondências , salvar e em seguida : Processos > Processar conceito

Importado para o Banco de Dados com sucesso.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/CON3/INT.conceito.aspx)

**COMUNIDADE **[@TBC e Microsoft Dynamics CRM](https://totvs.byyou.com/?space=rintegraoecrm)****

 **Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 2 – (CRM), 3 - (Vendas e CRM) e 3 –  (Microsoft CRM).
