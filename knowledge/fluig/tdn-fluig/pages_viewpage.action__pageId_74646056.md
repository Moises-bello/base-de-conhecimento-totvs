---
content_hash: 7c57d23fbfde9b73bc6fa0b45120b6e8a46ee4c1c286e55ae4b520a0d25b506f
fetched_at: '2026-06-28T21:35:29.460578+00:00'
page_id: '74646056'
product: fluig
source: tdn-fluig
title: Desenvolvimento de relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=74646056
version: 89
---

# Índice

true.\*ndicenone

# Objetivo

O objetivo deste guia é descrever o desenvolvimento, publicação e visualização de relatórios no TOTVS Fluig Plataforma. Para facilitar a compreensão será detalhado um exemplo de relatório de usuários.

# Introdução

O TOTVS Fluig Plataforma utiliza o BIRT - *Business Intelligence and Reporting Tools* - como motor de execução de relatórios, por esse motivo para o desenvolvimento de relatórios deve-se utilizar o padrão e a metodologia do BIRT. O BIRT é uma plataforma *open source* que facilita a modelagem de relatórios dentro do Fluig.

A partir da plataforma, é possível criar relatórios com:

* Listagem
* Agrupamento
* Cálculos
* Cartas e Documentos
* Gráficos

Compatibilidade no modo escuro

Este recurso ainda não é compatível com o modo escuro lançado na atualização [Voyager 2.0](https://tdn.totvs.com/x/6HxjN).

# Exemplos de relatórios desenvolvidos

Você pode fazer o download de [exemplos de relatórios](https://git.fluig.com/projects/SAMPLES/repos/relatorios/browse) desenvolvidos para a plataforma no [Repositório Git](https://git.fluig.com/projects/SAMPLES).

Mais detalhes na página .

# Ambiente de desenvolvimento

Para o desenvolvimento de relatórios, é necessário instalar:

* Java™ JDK/JRE - versão superior a 1.6. Endereço para download: <http://java.sun.com/javase/downloads/index.jsp>.
* BIRT - Caso a plataforma esteja na atualização Lake (1.7.0) ou superior, a [versão 4.8](https://www.eclipse.org/birt/phoenix/project/notable4.3.php) do BIRT é compatível. Nas atualizações anteriores, utilize a versão 2.6.2 do BIRT.

Recomenda-se o uso do BIRT Report Designer para o desenvolvimento de relatórios. O BIRT pode ser integrado ao Studio ou Eclipse (já instalados para utilização do Fluig Studio, conforme ), basta instalar o plugin do BIRT.

O BIRT Report Designer conta com várias funcionalidades que auxiliam no desenvolvimento de relatórios. Entre elas destacam-se: ajuste de *layout*, configuração de acesso a dados e formatação do relatório.

## Como instalar o plugin

Cada versão do Eclipse possui um repositório, e com ele uma versão homologada do BIRT. Confira abaixo os passos necessários para instalar o plugin do BIRT:

falseVersaoA partir da atualização 2.0 (Voyager)

Plugin compatível até a versão **2019-03** do Eclipse. Caso não possua uma versão do Eclipse (se não estiver usando o TDS), é necessário baixar a versão igual ou inferior a 2019-03.

**01.** No Eclipse, acesse a opção**Help → Install New Software.**

**02**. Clique no botão **Add** (localizado ao lado do campo **Work with)** e na tela apresentada preencha as informações abaixo:

* Name: **birt - 4.13**
* Location: ****<https://download.eclipse.org/birt/updates/release/4.13.0/>****

**03**. Após listar as opções do BIRT, marque as opções:

* BIRT Reporting SDK
* BIRT Charting SDK
* BIRT Engine Runtime

**04**. Em seguida, clique em **Next** até concluir a instalação.

A partir da atualização 1.7 (Lake)

Plugin compatível até a versão **2019-03** do Eclipse. Caso não possua uma versão do Eclipse (se não estiver usando o TDS), é necessário baixar a versão igual ou inferior a 2019-03.

**01.** No Eclipse, acesse a opção**Help → Install New Software.**

**02**. Clique no botão **Add** (localizado ao lado do campo **Work with)** e na tela apresentada preencha as informações:

* Name: **birt**
* Location: **http://download.eclipse.org/releases/2019-09/201909181001**.

**03**. Após listar as opções do BIRT, marque a caixa de seleção de **Business Intelligence, Reporting and Charting**.

**04**. Em seguida, clique em **Next** até concluir a instalação.

1.6.5 ou anteriores

**01.** No Eclipse, acesse a opção **Ajuda → Instalar Novo Software.**

**02**. No campo **Work with**: Selecione **Indigo**.

**03**. Após listar as opções do BIRT, digite **Birt** no campo de busca.

**04**. Marque a caixa de seleção de **Business Intelligence, Reporting and Charting**.

**05**. Em seguida, clique em **Avançar** até concluir a instalação.

# Conexão direta com o banco de dados

É possível publicar relatórios que se comunicam diretamente com o banco de dados.

Utilize em seu relatório as configurações abaixo atentando para os valores das propriedades *'odaDriveClass'* e *'odaURL'.*

Para fazer conexão direta com banco de dados **SQLServer** é preciso utilizar o seguinte padrão:

html/xmlSQLServercom.microsoft.sqlserver.jdbc.SQLServerDriver
jdbc:sqlserver://IP:1433;databaseName=DATABASE
// Para a release 2.0.0, adicionar os seguintes parâmetros na URL:
jdbc:sqlserver://IP:1433;databaseName=DATABASE;encrypt=true;trustServerCertificate=true]]>

Para fazer conexão direta com banco de dados **MySQL** é preciso utilizar o seguinte padrão:

html/xmlMySQLcom.mysql.jdbc.Driver
jdbc:mysql://IP:3306/databaseName=DATABASE]]>

Para fazer conexão direta com banco de dados **Oracle**é preciso utilizar o seguinte padrão:

Oracleoracle.jdbc.OracleDriver
jdbc:oracle:thin:@IP:1521:databaseName=DATABASE]]>

# Desenvolvendo um relatório de Usuários

oculto

Esse passo a passo está duplicado no artigo <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360034289633> (Como desenvolver relatórios)

Caso tenha alguma alteração, lembrar de revisar esse artigo!

Através do BIRT Report Designer é possível criar vários relatórios para o TOTVS Fluig Plataforma, acessar dados do banco de dados do produto via consulta JPA, JDBC. É possível acessar os dados de outros produtos por conexão JDBC, Web Service ou arquivos XML.

Para facilitar a compreensão a respeito do desenvolvimento de relatórios, será demonstrado um exemplo de criação de relatórios. A seguir, os passos necessários para a criação do relatório de usuários, sendo este com dados providos da plataforma através da consulta via *dataset*. O fonte do exemplo citado pode ser baixado [clicando aqui](https://git.fluig.com/projects/SAMPLES/repos/relatorios/browse/ambient-reports).

### Criando um novo projeto e um novo relatório

Abra a ferramenta na qual instalou o plugin do BIRT Report Designer para acompanhar o passo a passo, no exemplo iremos utilizar o Fluig Studio.

* No projeto fluig previamente criado, clique com o botão direito do mouse na pasta *reports*, e em seguida em *Novo → Relatório fluig.*
* Em seguida basta informar o *Nome do Relatório* e clicar em *Concluir*.

**Figura 1 - Criação de relatório no projeto fluig.**

### Configurando o acesso aos dados

Um *Data Source* é o mecanismo que guarda os dados de conexão com a fonte de dados, por exemplo, configurações JDBC, Web Service, entre outros. No caso desse relatório, será utilizado o acesso aos dados via linguagem JavaScript.

Acompanhe os passos a seguir:

0.5falsesamplesfadetrue1Passo1

* Ao criar o novo relatório, selecione a perspectiva *Report Design* e em seguida a aba *Data Explorer*, clique com o botão direito do mouse sobre o item *Data Source* em seguida selecione a opção *New Data Source*.

**Figura 2 - Novo Data Source.**

2Passo 2

* Ao abrir a janela *New Data Source,* selecione a opção *Scripted Data Source* e define o nome *dsColleague* como *Data Source Name* em seguida clique no botão *Concluir.*

**Figura 3 - Tipo de Data Source.**

3Passo 3

* Na aba *Data Explorer* clique com o botão direito do mouse sobre o item *Data Sets* em seguida clique na opção *New Data Set* conforme figura 4. Data Set é uma tabela temporária do BIRT no qual os dados são armazenados do Data Source e renderizados no relatório.

**Figura 4 - Novo Data Set.**

4Passo 4

* Ao abrir a janela *New Data Set* defina *colleagueDataSet* como *Data Set Name*, clique no botão *Next* em *Output Columns,* clique no botão *Add* e adicione todas os registros do Data Set. Em seguida clique no botão Concluir.

**Figura 5 - Colunas do Data Set.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Column Name** | **Data Type** | **Column Alias** | **Display Name** |
| colleagueId | String | Vazio | Vazio |
| Login | String | Vazio | Vazio |
| colleagueName | String | Vazio | Vazio |
| mail | String | Vazio | Vazio |
| active | String | Vazio | Vazio |
| adminuser | String | Vazio | Vazio |

### Incluindo parâmetros no Relatório

É possível incluir parâmetros no relatório a serem solicitados para o usuário antes da sua renderização, auxiliando no filtro de consulta aos dados gerando um relatório específico. Siga os passos a seguir:

0.5falsesamplesfadetrue1Passo1

* Selecione a aba *Data Explorer*, em seguida clique com o botão direito do mouse no item *Report Parameters*, selecione a opção *New Parameter.*

**Figura 6 - Parâmetros do Relatório.**

2Passo 2

* A figura 7 ilustra a janela de inclusão de parâmetros.

**Figura 7 - Configuração de parâmetros.**

Ao abrir a janela New Parameter inclua os seguintes parâmetros:

**Matrícula**

| Campo | Valor |
| --- | --- |
| Name | Matricula |
| Prompt text | Matrícula do Usuário ou "\*" para mostrar todos |
| Data type | String |
| Display type | Text Box |
| Is Required | true |

**Mostra Usuários**

| Campo | Valor |
| --- | --- |
| Name | paramEnable |
| Prompt text | Mostrar usuários |
| Data type | String |
| Display type | List Box |
| Is Required | true |

*Selection Values*

| Value | Display Text |
| --- | --- |
| \* | Todos |
| true | Ativos |
| false | Inativos |

**Ordenar Por**

| Campo | Valor |
| --- | --- |
| Name | paramSort |
| Prompt text | Ordenar por |
| Data type | String |
| Display type | List Box |

*Selection Values*

| Value | Display Text |
| --- | --- |
| c.colleaguePK.colleagueId | Matrícula |
| c.collegueName | Nome |
| c.login | Login |

### TAG's

Disponibilizamos TAG’s de substituição que auxiliam no desenvolvimento e na segurança da geração das informações do relatório, são elas:

• **${WKCompany}**: substitui a variável pelo código da empresa autenticada na plataforma TOTVS Fluig.  
• **${WKUser}**: substitui a variável pelo código do usuário autenticado na plataforma TOTVS Fluig.

As TAG’s são úteis em casos de informações que só devem ser geradas a respeito da empresa em que o usuário está autenticado, ou em relatórios que mostrem somente informações a respeito do usuário autenticado.

### Como utilizar as TAG's

A *tag* utilizada deve estar entre aspas duplas, para que ocorra corretamente a substituição da *tag* pelo respectivo valor:

jsEclipseExemplo - Uso de TAG's

### Populando o Data Set

No exemplo apresentado neste documento, será populado o relatório através de dados providos de consultas JPA acessando o banco de dados, porém é possível utilizar outros recursos para popular o *Data Set*: XML, Web Service e JDBC.

O BIRT renderiza o relatório através da execução de seus eventos, são muitos os eventos disponibilizados pelo BIRT, nesse exemplo serão utilizados:

* *initialize:* primeiro evento disparado pelo BIRT, é recomendado utilizar esse evento para importação de bibliotecas e inicialização de variáveis;
* *beforeOpen*: evento disparado antes do BIRT abrir a conexão com a fonte de dados (*Data Source*);
* *fetch*: evento disparado pelo BIRT depois da busca de cada registro no Data Set e antes de aplicar os filtros e campos calculados.

Através dos eventos é possível desenvolver a lógica de consulta e geração de dados através da linguagem de programação JavaScript , além disso é possível fazer uso de vários recursos e bibliotecas da linguagem Java™.

0.5falsesamplesfadetrue1Initialize

* Selecione a aba *Script* na pagina do relatório e em seguida selecione o evento *initialize*, inclua o seguinte código conforme figura 8:

javascript

**Figura 8 - Evento initialize.**

O código a cima importa as bibliotecas Java™ e a biblioteca disponibilizada pelo fluig para consulta aos dados do produto, além de realizar a inicialização das variáveis utilizadas pelo relatório.

Detalhes sobre o código:

* + *importPackage*: comando responsável pela importação de bibliotecas Java™.
  + *Package.java.util*: biblioteca responsável pelas Classes *utils* do Java™.
  + *Packages.com.datasul.technology.webdesk.dataset.service*: biblioteca disponibilizada pelo fluig para consulta ao banco de dados do produto.
2BeforeOpen

* Selecione a aba *Data Explorer*, expanda o item *Data Sets* e clique no *colleagueDataSet em seguida clique na aba Script* então selecione o evento *beforeOpen* e inclua o seguinte código conforme a figura 9.

javascript

**Figura 9 - Evento BeforeOpen.**

O código acima monta a consulta do relatório através da consulta via dataset e inclui os filtros da solicitação de acordo com os parâmetros definidos pelo usuário.

Detalhes sobre o código:

* ${WKCompany}: TAG disponibilizada pelo fluig, retorna o código da empresa que o usuário está autenticado;
* params["Matricula"]: parâmetro de relatório, retorna o código da matricula definido pelo usuário;
* params["paramEnable "]: parâmetro de relatório, retorna o tipo de usuário;
* params["paramSort "]: parâmetro de relatório, retorna o modo de ordenação;
3Fetch

* Para incluir o resultado da consulta no *Data Set* e  formatar os dados do relatório, selecione o evento *fetch* na área de *Script* e inclua o seguinte códigoconforme figura 10.

javascript

**Figura 10 - Evento fetch*.***

### Obtendo dados via conexão JDBC

Uma forma alternativa de obtenção de dados para criação de relatórios é a utilização de JDBC. É necessário criar um *Data* *Source* que se conecte com o banco de dados, nele serão armazenados os dados para conexão, via JDBC, ao banco de dados.

0.5falsesamplesfadetrue1Passo 1

* Selecione a aba *Data Explorer*, clique com o botão direito do mouse sobre o item *Data Source* em seguida selecione a opção *New Data Source* conforme a figura 11.

  **Figura 11 – Novo Data Source**
2Passo 2

* Ao abrir a janela *New Data Source,* selecione a opção *JDBC DataSource* e define o nome *JDBC-DataSource* como *Data Source Name* em seguida clique no botão *Next*, conforme a figura 12.

  **Figura 12 – Tipo Data Source**
3Passo 3

* Na próxima janela a conexão com o banco de dados deve ser configurada.

  No campo *Driver* *Class* selecione o driver de conexão com o banco de dados, neste caso, a conexão será feita com o banco MySQL®. Se o driver necessário não estiver listado, basta adiciona-lo clicando em *Managed* *Drivers*...

  Informe também os valores para *Database URL, User Name*e *Password*de acordo com o banco de dados escolhido, conforme a figura 13.

  **Figura 13 – Configurando conexão com banco de dados.**
4Passo 4

* Na aba *Data Explorer* clique com o botão direito do mouse sobre o item *Data Sets* em seguida clique na opção *New Data Set*.

  **Figura 14 – Criando Novo Data Set.**
5Passo 5

* Selecione o *Data**Source* criado (*JDBC-DataSource*), no campo *Data Set Type* selecione SQL *Select Query*, informe um nome para o *Data Set*e clique em *Next, conforme a figura 15.*

**Figura 15 – Configurando Data Set.**

6Passo 6

* Na próxima tela informe a SQL que busca os dados no banco de dados, neste exemplo, serão buscados os volumes da empresa autenticada no fluig.

**Figura 16 – Criação da Query SQL**

* A *Query* abaixo busca no banco de dados todos os volumes da empresa do usuário autenticado no fluig, este código é obtido através da TAG ${WKCompany}.

javaNota

Poderá ocorrer um erro quando concluir a criação do *Data* *Set* pois a TAG  ${WKCompany} não existe no contexto do BIRT. A figura a seguir apresenta o erro devido à utilização da TAG, este é um erro de sintaxe no SQL e indica que ${WKCompany} não é um comando SQL. Porém quando o relatório for executado no fluig, ela retornará o código da empresa normalmente, com isso a TAG será substituída pelo código da empresa do usuário autenticado no fluig, corrigindo o erro de sintaxe.

**Figura 17 – Erro do Birt pelo uso da TAG ${WKCompany}**

7Passo 7

* Após concluir a criação do Data Set, na seção Data Explorer da IDE, clique com o botão secundário do mouse sobre o Data Set criado e escolha a opção **Editar**.
* Selecione a opção **Query**, escreva a query desejada e coloque o coringa **?** no valor dos campos que estão na cláusula **WHERE**.

Importante

A sintaxe da **query** deve ser a mesma do **SGBD** utilizado pelo **Fluig**.

8Passo 8

* + Ainda na tela de edição do DataSet, escolha o menu **Parâmetros.**
  + Nesta tela, adicionar os parâmetros através do botão **Novo**, oueditar os parâmetros existentes através do botão **Editar**.
  + Informar:
    - nome
    - tipo
    - direção
    - valor inicial
    - parâmetro do relatório

Passo 9

* Após o término da edição, o relatório deve ser exportado para o **Fluig**.
* Ao abrir o relatório no **Fluig**, será apresentada uma tela de filtro, na qual devem ser informados os parâmetros que foram configurados no **Fluig Studio**.

Atenção

A criação de relatório no BIRT utilizando conexão JDBC exige atenção com relação à segurança da publicação do relatório no fluig, uma vez que o arquivo .rptdesign (XML do relatório Birt) deixa exposto os parâmetros de conexão com o banco de dados, porém o campo senha fica ofuscado com base64. Por este motivo e pela facilidade de busca das informações do fluig, sempre recomendamos a criação de relatórios com fontes de dados via Dataset do fluig ou query JPA.

Se a criação de relatórios utilizando JDBC for necessária, recomendamos que ao publicar um relatório no fluig as configurações de permissão sejam definidas apenas para leitura. Usuários que possuem permissão de manutenção podem fazer o download dos anexos e com isso terão acesso aos dados de conexão com o banco de dados.

### Formatando a visualização do Relatório

É necessária a inclusão dos componentes de renderização do relatório. Clique na aba *Layout* para visualizar a página do relatório que está em branco e em seguida selecione a aba *Palette* conforme a figura 18.

**Figura 18 – Relatório em branco.**

Na aba Pallets é possível incluir vários componentes de visualização e renderização de dados entre eles destacam-se:

* Label: Texto curto e estático.
* Text: Texto longo é possível formatá-lo com TAG’s HTML.
* Dynamic Text: Texto dinâmico provido do Data Set.
* Image: Inclusão de imagens.
* Grid: Formatador de dados em Grid.
* Table: Tabela de dados.
* Chart: Gráficos de pizza, linha, tubo, etc.

0.5falsesamplesfadetrue1Componente Image

* É possível incluir imagens da internet, incluir imagens de arquivo ou ainda embutir a imagem no XML do relatório. Neste exemplo será usada uma imagem em anexo para posteriormente mostrar como publicar relatórios com anexo.

  Arraste um componente *Image* no relatório, ao abrir a janela *Edit Image*Item, selecione a opção *Image file in shared resources*, selecione o arquivo da imagem na opção *Enter resource file e*em seguida clique no botão *Insert*.

  **Figura 19 – Componente Image.**
2Componente Text

* Arraste um componente *Text* no relatório, ao abrir a janela *Edit Text Item* selecione a opção *HTML* e na área de texto inclua a seguinte informação formatada em HTML:

html/xml
<http://www.fluig.com/>
  
**E-mail:** [contato@fluig.com](mailto:contato@fluig.com)
  
**Telefone:** 0800 882 9191
  
]]>

* Em seguida clique no botão *OK* conforme figura 20.

**Figura 20 - Componente Text.**

3Componente Label

* Arraste um componente *Label* no relatório, clique duas vezes sobre o componente incluído  e digite *Relatório de Usuários,* na aba *Property Editor - Label -> G**eneral* defina a formatação da label, conforme figura 21.

**Figura 21 - Título do relatório.**

4Componente Table

* Arraste um componente *Table*, ao abrir a janela *Insert Table* defina 6 colunas e 1 detalhe e clique no botão *OK* conforme figura 22.

**Figura 22 - Configuração da Tabela.**

5Lables para Table

Na tabela adicionada ao relatório inclua um componente *Label* para cada coluna da linha *Header Row* defina os seguintes valores*:*

* Matrícula.
* Nome.
* Login.
* E-mail.
* Ativo.
* Administrador.

Formate as *labels* incluídas definindo cor da fonte e cor de fundo conforme figura 23.

**Figura 23 - Título das Colunas.**

### Renderizando dados do Data Set

Selecione a aba *Data Explorer* e expanda o *colleagueDataSet* criado anteriormente e em seguida arraste cada item do *Data Set* para a coluna *Detail Row* da tabela criada anteriormente conforme figura 24.

**Figura 24 - Data Set.**

# Publicando Relatórios

Após a conclusão do desenvolvimento do relatório, é necessário realizar a publicação do relatório no fluig. Essa ação pode ser feita via navegação de Documentos ([consulte aqui o passo a passo](https://tdn.totvs.com/x/VpxyDg#Relatório-Novorelatório)) ou por meio do fluig Studio.

### Publicação através do Studio

oculto

Esse passo a passo está duplicado no artigo <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360053078854> (Como publicar relatórios)

Caso tenha alguma alteração, lembrar de revisar esse artigo!

Após a conclusão do desenvolvimento do relatório, é necessário realizar a exportação do mesmo para a navegação de documentos fluig.

0.5falsesamplesfadetrue1Passo1

Para isso clique sobre o pasta do relatório com o botão direito do mouse e acione *Exportar*.

**Figura 25 – Exportação de Relatório.**

Nota

Os anexos são exportados junto ao relatório. Na exportação, o arquivo .rptdesign é automaticamente identificado como arquivo principal, e os demais arquivos são classificados como anexo.

2Passo 2

* Na tela de Exportação, clique sobre *Exportar para o servidor fluig* e em seguida acione *Avançar*.

  **Figura 26 – Exportação de relatório.**

3Passo 3

* Na tela *Exportar Relatório*, é necessário informar o nome do *Servidor*, identificar se está será a publicação de um *Novo Relatório*, definir o nome do relatório, a Pasta Destino (conforme imagem foi informado o código da pasta destino) e em seguida mencionar o tipo de *Versionamento* (como estamos fazendo uma nova publicação, selecionamos *Manter Atual*).

  **Figura 27 – Exportação de relatório.**
4Passo 4

* Na pasta*Relatório* da *Navegação de Documentos* será possível observar que o relatório foi publicado com sucesso.

**Figura 28 – Publicação de relatório.**

# Visualizador de Relatórios

Após concluir a publicação, para visualizá-lo, clique sobre o relatório na pasta onde foi feita a publicação no fluig.

Uma nova janela deverá abrir, para iniciar a execução do relatório de colaboradores desenvolvido anteriormente é necessária a inclusão de parâmetros, defina os seus valores e em seguida clique no botão *OK*.

**Figura 29 – Parâmetros do relatório.**

O relatório deverá mostrar todos os usuários cadastrados no fluig para a empresa em que o usuário está autenticado.

**Figura 30 – Relatório de Usuários– Resultado**.

Opções do visualizador

A ferramenta de visualização de relatório do fluig possui várias funcionalidades:

* *Verificar Indice*: Caso o relatório desenvolvido possua índice é possível listá-lo.
* *Executar relatório*: Permite que o relatório seja executado novamente.
* *Exportar dados:* Exporta os dados gerados do relatório em arquivo, permitindo selecionar as colunas desejadas e o separador de dados.
* *Exportar relatório*: Converte os dados do relatório em diferentes formatos de arquivos: Microsoft® Excel®, PostScript®, PDF, Microsoft® Word e Microsoft® Power Point®, permite também a seleção de páginas que serão exportadas.
* *Imprimir relatório*: Imprime relatório selecionando as impressoras instaladas no computador do usuário autenticado e permite imprimir em formato PDF ou HTML.
* *Imprimir relatório no servidor:* Imprime relatório a partir das impressoras instaladas no servidor do fluig.
* Navegação de páginas: permite a navegação entre as páginas do relatório.

**Figura 31 – Funcionalidades do visualizador de relatórios.**

# JPA - Funções de Agregação

### Funções de Agregação

O fluig suporta através de consultas JPA e seu banco de dados, o uso de funções de agregação, tais como: AVG, SUM, COUNT, MAX e MIN. Permite também utilizar agrupamentos: GROUP BY e HAVING

### Tabela de entidades

A tabela abaixo referencia a relação entre o código de dataset, a entidade de persistência JPA utilizada nas consultas, e a respectiva tabela no banco de dados. As colunas das entidades de persistência são as mesmas apresentadas no dataset.

|  |  |  |
| --- | --- | --- |
| **Código dataset** | **Entidade JPA** | **Tabela banco de dados** |
| **AccessLog** | AccessLog | HISTOR\_ACES |
| **ActivityDim** | ActivityDim | ACTIVITY\_DIM\_CAP |
| **advancedProcessProperties** | AdvancedProcessProperties | PROPRIED\_AVANCAD\_PROCES |
| **businessPeriod** | BusinessPeriod | PERIOD\_EXPED |
| **destinationArea** | DestinationArea | AREA\_DEST |
| **document** | Document | DOCUMENTO |
| **documentSecurityConfig** | DocumentSecurityConfig | CONFIGUR\_SEGUR\_DOCTO |
| **FactActivityCost** | FactActivityCost | FACT\_ACTIVITY\_COST\_CAP |
| **FactFlowVolume** | FactFlowVolume | FACT\_FLOW\_VOLUME\_CAP |
| **FactProcesCost** | FactProcesCost | FACT\_PROCES\_COST\_CAP |
| **FactProcesVolume** | FactProcesVolume | FACT\_PROCES\_VOLUME\_CAP |
| **FlowDim** | FlowDim | FLOW\_DIM\_CAP |
| **globalCalendar** | GlobalCalendar | CALEND\_GLOBAL |
| **knowledge** | Knowledge | CONHECIMENTO |
| **processAttachment** | ProcessAttachment | ANEXO\_PROCES |
| **processDefinition** | ProcessDefinition | DEF\_PROCES |
| **processDefinitionVersion** | ProcessDefinitionVersion | VERS\_DEF\_PROCES |
| **processHistory** | ProcessHistory | HISTOR\_PROCES |
| **processState** | ProcessState | ESTADO\_PROCES |
| **processTask** | ProcessTask | TAR\_PROCES |
| **ProcesVersionDim** | ProcesVersionDim | PROCES\_VERSION\_DIM\_CAP |
| **TimeDim** | TimeDim | TIME\_DIM\_CAP |
| **topic** | Topic | ASSUNTO |
| **UserDim** | UserDim | USER\_DIM\_CAP |
| **workflowProcess** | WorkflowProcess | PROCES\_WORKFLOW |

### Exemplo de Utilização

java

# Acessando dados de Formulários

### Importando bibliotecas

A partir da classe DatasetFactory é possível acessar dados de formulários publicados no fluig.

Para popular um relatório através de dados de formulários é necessário a importação das seguintes bibliotecas:

java

### Retornando dados do formulário

Através da classe DatasetFactory é possível buscar dados de formulários, incluir filtros e ordenação. Exemplo de utilização:

java

O exemplo acima invoca o método getDataset passando alguns argumentos extras como parâmetros:

* **Nome do Dataset:** Nome do serviço de dados do formulário;
* **Campos:** Retorna apenas os campos recebidos no array informado. Caso null, retorna todos os campos.
* **Constraints**: Vetor com as condições de busca do Dataset. Em cada condição de busca (constraint) deve-se informar o nome do campo do formulário que será filtrado, a faixa de valores inicial e final, e o tipo de Constraint. Os tipos podem ser:

* + **MUST:** Indica que todos os registros do Dataset devem satisfazer a esta condição.
  + **SHOULD:** Indica que os registros do Dataset podem ou não atender à condição. Este tipo é mais comum quando se necessita que um mesmo campo tenha valores A ou B (onde cada um será uma constraint SHOULD).
  + **MUST\_NOT:** indica que nenhum dos registros pode satisfazer a condição.
  + **Ordenação:** Vetor com a lista de campos que será utilizada para ordenação dos registros no Dataset.

Dica

O fonte do exemplo citado acima pode ser baixado a partir do seguinte link:

### Busca de dados de formulário com filtro por data

Para realizar consultas via Dataset com filtros do tipo Data, é necessário antes salvar o campo do formulário no formato **aaaa/mm/dd** (ano/mês/dia)  para que seja possível realizar a busca via Dataset.

Exemplo de consulta:

java

# Acessando documentação do BIRT Report Designer

Dica

Acesse [aqui](https://help.eclipse.org/mars/index.jsp?nav=%2F9_0) a documentação oficial do BIRT - Business Intelligence and Reporting Tools e saiba mais sobre desenvolvimento e modelagem de relatórios .

$("b:contains('oculto')").parent().parent().hide();
]]>
