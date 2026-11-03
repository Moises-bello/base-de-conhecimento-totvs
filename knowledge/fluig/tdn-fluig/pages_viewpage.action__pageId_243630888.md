---
content_hash: bd69e4872381a9c78af4cc4062c237204882d7b0fa56c6c968b619609004f19b
fetched_at: '2026-06-28T21:35:22.987774+00:00'
page_id: '243630888'
product: fluig
source: tdn-fluig
title: Criação de Relatórios no Analytics
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243630888
version: 65
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é demonstrar como é feita a criação de um relatório no Analytics, utilizando as métricas e atributos disponibilizados por padrão pela plataforma. Apresentar também informações sobre os datasets que recebem informações de forma incremental do TOTVS Fluig Plataforma, dashboards e painéis KPIs.

Quer conhecer ainda mais sobre o **Analytics**? Assista o treinamento de **[Gestão de Indicadores - Analytics](http://academy.fluig.com/courses/gestao-de-indicadores-analytics)** disponível no **[Fluig Academy](http://academy.fluig.com/)**.

# Conceitos

| Termo | Descrição | Exemplo |
| --- | --- | --- |
| Fatos | Medida numérica individual relacionada a um Data Set. São dados quantitativos, ou seja, campos que tem operações matemáticas.  São a menor unidade de dados e sempre são números. | Apoios (Ex.: 325)  Documentos (Ex.: 2650) |
| Atributos | Descritores usados para delimitar métricas e contextualizar os dados em um relatório. São dados qualitativos, ou seja, que classificam os dados.  Podem ser textos ou números. | por Mês, Marca  por Solicitante |
| Métricas | Agregação de fatos ou contagem de atributos, que são exibidos como números em relatórios. São definidas por cálculos de agregação.  Métricas representam o que está sendo medido em um relatório. | Espaço ocupado  Solicitações em atraso |
| Relatório | Visualização de dados em tabelas ou gráficos.  Contém pelo menos uma métrica (o que está sendo medido), geralmente classificada por atributos (que dividem a métrica). | Posts / Mês  Páginas mais acessadas |

# Alterando o Idioma

Se desejar mudar o idioma da página do seu projeto, acesse o Analytics e siga os passos abaixo:

0.5falseReport\_1fade1Passo 1

* Na barra superior da página, clique sobre o **Nome do Usuário** logado (ao lado do botão Help);
* Após clique em **Account;**

2Passo 2

* Clique sobre o link **Change Language**;

3Passo 3

* Clique sobre a listagem e **selecione o idioma** desejado (Exemplo: Português Brasileiro);
* Após clique em **Save**.

4Passo 4

* **Pronto!** Note que todas palavras da interface da página, passíveis de tradução, foram alteradas para o idioma selecionado.

# Datasets

No Analytics apenas os dados da plataforma TOTVS Fluig são enviados para análise. Confira abaixo como consultar as informações de cada dataset no Analytics:

0.5falsedatasetsfadetrue1Passo 1

* Na barra superior do Analytics, clique na opção **Administrar** (*Manage*). Nesta tela será apresentado a listagem de **datasets** do projeto selecionado, a data e hora do último *upload* de dados da plataforma, o autor e o Status.

Para consultar os campos de cada dataset acesse a página .

2Passo 2

* Clicando sobre cada dataset é possível consultar o histório de *uploads* que exibe as últimas atualizações enviadas pela plataforma para os datasets do Analytics. Também são apresentados os  separados por Atributos e Fatos.
* Entendendo os Objetos que compões cada dataset fica mais simples desenvolver relatórios e KPIs personalizados gerando conhecimento relevante para tomada de decisão do seu negócio.
* Siga os tópicos abaixo e veja como é simples e rápido criar relatórios no Analytics.

# Criando o Relatório

Para iniciar a criação de um novo relatório, acesse o Analytics e siga os passos abaixo:

0.5falseIdiomafade1Passo 1

* Na barra superior do Analytics, clique na opção **Relatórios** (*Reports*).

2Passo 2

* Nesta página serão exibidos todos os relatórios existentes na ferramenta, inclusive aqueles disponibilizados por padrão, como TOP Usuários, Acessos, Número de Solicitações, etc.

* Para criar um novo relatório, clique no botão **Criar Relatório** (*Create Report*).

3Passo 3

* Será exibida a página padrão para criação dos relatórios no Analytics. A partir deste momento, o administrador poderá selecionar as métricas, atributos e filtros que deseja incluir no relatório.

* Para isso serão utilizados os painéis (*What*), **Como** *(How*) e  (*Filter*).

# Definindo as Métricas (What)what

Neste painel é realizada a seleção das métricas, ou seja, dos números que o administrador deseja exibir no relatório.

0.5falseReport\_2fade1Passo 1

* Ao clicar no botão O Quê (*What*), todas as métricas são exibidas na coluna central, pois por padrão a pasta Todas as Métricas (*All Metrics*) virá selecionada.

* Na coluna à esquerda, é possível filtrar pelas pastas (Documentos, Processos, Social e WCM) as métricas que são incluídas por padrão no Analytics.

2Passo 2

* Para escolher uma métrica, basta marcar a caixa de seleção que fica ao lado do nome.

* Clicando diretamente sobre o nome da métrica é possível visualizar detalhes sobre o cálculo dos fatos que a compõe e o formato de exibição da métrica no relatório.

3Passo 3  

* Nesse ponto já é possível gerar um relatório simplificado, apenas com métricas. Basta clicar no botão **Concluído** (*Done*) e o relatório exibirá os dados das métricas selecionadas em formato de tabela.

* Contudo, para criar relatórios mais elaborados e relevantes, convém aplicar os atributos disponíveis no painel  (*How*).

# Definindo os Atributos (How)how

Neste painel é realizada a seleção dos atributos, ou seja, como os dados do relatório serão segmentados.

0.5falseReport\_3fade1Passo 1

* Ao clicar no botão **Como** (*How*) será exibido o painel com os atributos disponíveis de acordo com a métrica escolhida na seção **O Quê** (*What*).

Veja o detalhamento dos atributos existentes.

Atributos incompatíveis com a métrica selecionada não serão habilitados.

2Passo 2

* Clicando sobre o nome do atributo é possível obter mais informações, bem como mais opções de visualização no relatório.

* O botão **L/T** determina se o atributo será exibido à esquerda (*Left*) ou no topo (*Top*), caso o modo de visualização do relatório esteja definido como tabela (*Table*).

3Passo 3

* Após selecionar o atributo desejado, clique no botão **Concluído** (*Done*)para aplicar as configurações ao relatório. O resultado deverá ser exibido em formato Tabela.

* Para alterar o formato, utilize os botões no canto superior direito para exibir gráficos de linha, barras, pizza, etc.

**Tabela**

**Gráfico de Linha**

**Gráfico de** **Barras**

**Gráfico de Pizza**

# Adicionando Filtros (Filter)filter

O painel de filtros possibilita a inclusão e remoção de determinados conjuntos de dados do relatório. É possível escolher entre os seguintes tipos de filtros:

0.5falseReport\_4fade1List of Values  

* Permite filtrar os dados do relatório por subcategorias de um atributo. Pode-se optar por valores específicos (Ex.: Abr 16) ou relativos (Ex.: 3 meses atrás).

* No exemplo abaixo, o filtro será configurado para exibir apenas solicitações cujo nome do solicitante é John Steel (solicitacaoNomeSolicitante *is* "John Steel"):

**Seleção do atributo solicitacaoNomeSolicitante e condição *is* (1) e do valor "John Steel" (2)**

**Com o filtro aplicado, apenas os processos abertos por este usuário serão considerados no relatório.**

2Ranking Filter

* Permite escolher os dados exibidos no relatório com base na classificação dos valores de determinado atributo: os maiores (*Top*) ou os menores (*Bottom*).

* No exemplo abaixo, o filtro será configurado para exibir apenas os 3 meses com maior quantidade de solicitações abertas (*Top* 3).

**Seleção da quantidade de resultados que será exibida no relatório (1); atributo createDate (2); ordenação pelo Número de Solicitações (3).**

**Com o filtro aplicado, apenas o três meses com o maior número de solicitações abertas são exibidos no relatório.**

3Numeric Range

* Permite definir um critério para inclusão de dados no relatório, excluindo aqueles que não se encaixam no valor estipulado.

* No exemplo abaixo, o filtro será configurado para exibir apenas os meses em que o número de solicitações abertas foi maior ou igual a 10.

**Seleção do atributo createDate (1) onde a métrica Número de Solicitações é maior ou igual (*is greater than or equal to*) a 10 (2).**

**Com o filtro aplicado, apenas os meses em que 10 ou mais solicitações tenham sido criadas são exibidos no relatório.**

# Finalizando o Relatório

Após selecionar as métricas, atributos e filtros, o relatório já pode ser salvo e disponibilizado para visualização em um dashboard.

0.5falseReport\_5fade1Passo 1

* Informe um título para o relatório clicando sobre a caixa de texto **Untitled report** e clique **Save.**

2Passo 2  

* Clique sobre o botão **Create** para informar os últimos parâmetros para a criação do relatório.

3Passo 3  

* Na janela que será exibida informe:

1. Tags e a pasta em que o relatório será armazenado (opcional);
2. Visibilidade do relatório: ao marcar esta opção, o relatório poderá ser visualizado por todos os usuários do Analytics;
3. Permissão de edição: define que tipo de usuário pode editar o relatório. Por padrão, administradores e editores possuem permissão, mas é possível limitar a edição apenas aos administradores.

* Por fim, clique no botão **Create** na parte inferior para concluir a criação do relatório.

# Incluindo o Relatório em um Dashboard

**Relatórios** são tabelas ou gráficos que apresentam informações sobre uma ou mais métricas, ou seja, sobre os dados que se deseja medir.

***Dashboards*** são utilizados para exibir e organizar relatórios, de forma a tornar o acesso à estas informações simples e ágil.

Para incluir um novo relatório em um *dashboard*, siga as instruções abaixo:

0.5falseReport\_6fade1Passo 1  

* Na barra superior do Analytics, clique na opção **Dashboards**.

2Passo 2

* Selecione em qual aba do *dashboard* deseja incluir o relatório. No exemplo abaixo, a aba será **Processos** (1).

* Em seguida, clique no botão com ícone de engrenagem, no canto superior direito (2) e selecione **Edit** (3).

3Passo 3

* Na barra superior que será exibida, clique sobre a opção **Report** (1).

* Serão listados todos os relatórios disponíveis. Selecione o relatório desejado (2).

4Passo 4

* O relatório será adicionado ao *dashboard*.

5Passo 5

* Utilize as bordas da caixa de seleção para ajustar o tamanho dos relatórios. Desmarque a seleção para movê-los para o lugar apropriado.

6Passo 6

* Clique sobre o botão **Save** no canto superior direito para salvar as alterações ao *dashboard*.

# Sobre KPIs

#FFFFFFAcesse o link <https://help.gooddata.com> e conheça a documentação completa sobre [painéis KPI](https://help.gooddata.com/display/doc/KPI+Dashboards).
