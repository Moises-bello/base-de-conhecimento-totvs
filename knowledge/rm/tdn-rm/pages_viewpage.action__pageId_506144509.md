---
content_hash: 4098e72e2d24fa7efd58ed4ce4efb8469384ffc5b6c9d7df1a8f623f5bd3f095
fetched_at: '2026-06-29T00:10:25.857481+00:00'
page_id: '506144509'
product: rm
source: tdn-rm
title: Importação de Funcionário por Conceito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506144509
version: 71
---

Veja como importar dados de funcionário por conceito.

## **Atenção**

Para importação de dados de funcionário a TOTVS recomenda o uso do módulo de Importação de Dados do RM.

Acessando: Configurações / Importações / Importação de Dados do Folha de Pagamento.

Se ainda for necessário o uso de importação por conceito, recomenda-se seguir com a leitura deste guia.

# Conhecendo a Ferramenta

O conceito é uma ferramenta do produto que tem como objetivo transportar dados de um local de origem para outro local de destino a escolha do usuário. Estes locais são tratados como uma conexão dentro do conceito e são divididas em:

* Conexão de Origem
* Conexão de Destino

Os dois tipos de conexão podem ser criadas em diferentes tipos:

* Arquivo Texto
* Arquivo XML
* Banco de Dados
* Data Server RM. NET
* DLL .NET
* Web Service

## 

As Conexões de Destino e Origem possuem as mesmas opções para tipos de conexão, conforme apresentado nas imagens. Cada um desses tipos tem suas particularidades, tornando o conceito uma ferramenta com várias possibilidades de configuração.

# Configurando a Conexão de Origem

A primeira ação a ser feita na criação de um conceito é a configuração da conexão de origem ela define como os dados de origem serão disponibilizados.

## Arquivo Texto

A conexão mais simples é do tipo arquivo de texto. Ao selecionar este tipo de conexão será apresentada a tela de parametrização da conexão por arquivo de texto, conforme a imagem a seguir.

A princípio existem dois tipos de arquivo a serem selecionados

* Arquivo separado por delimitador
* Arquivo de tamanho fixo

Essa configuração indica como cada cada campo de um registro é separado. Sabe-se que cada linha do arquivo texto é um registro que podem conter vários campos.

No caso de um arquivo separado por delimitador, deve ser informado o caractere delimitador. Comumente é um utilizado ponto-vírgula ( ; ).

Se houver campos que irão assumir valores decimais deve ser informado o caractere de separador decimal e ele deve ser diferente do delimitador escolhido na configuração anterior.

O próximo passo é acessar a aba Tabelas e criar estrutura que o arquivo texto representa, como na imagem a seguir.

Clicando no botão indicado para criar uma nova tabela, você deverá dar um nome para esta tabela e após esse processo é possível criar colunas para ela.

As colunas devem ter um nome, o tamanho do campo e o tipo de dado que ela representa. O tamanho do campo somente influência quando o for configurado como arquivo de tamanho fixo.

A correta parametrização da tabela gera uma visualização na tela conforme o exemplo a seguir:

Após a criação tabela visualiza-se nas propriedades do conceito a conexão de origem criada.

# Configurando a Conexão de Destino

O segundo passo a ser feito na criação de um conceito é a configuração da conexão de destino ela define como os dados de origem serão associados na conexão de destino.

## Arquivo Texto

A conexão de destino mais comumente usada é um Data Server RM.NET. Ao selecionar este tipo de conexão será apresentada a tela de parametrização da conexão por data server RM[.](http://rm.net)NET, conforme a imagem a seguir.

O primeiro passo dentro da configuração de conexão data server RM.NET é parametrizar o servidor de destino. Ele deve ser pesquisado conforme a imagem a seguir.

Após parametrizar o data server destino as tabelas envolvidas na execução do data server são apresentadas conforme mostra a imagem.

# Configurando as Ligações

As ligações são as pontes entre a conexão de origem e destino. Antes de criar qualquer ligação é preciso entender os relacionamentos entre as tabelas e também conhecer suas estruturas. Quando a conexão destino é um data server, deve ser considerado que as regras de negócio deste data server serão validadas na execução do conceito.

Um fator importantíssimo na configuração das ligações é o correto uso das chaves primárias, é muito comum confundir a parametrização delas. Para facilitar segue um exemplo.

## Exemplo

Deseja-se criar um conceito para importação de um funcionário. A tabela de cadastro de funcionários é a  PFUNC, portanto iremos arrastar esta tabela para a aba ligações.

Observe que os campos da tabela são listados, e agora é necessário ligar os campos da tabela de origem aos campos da tabela de destino.

Com as ligações feitas é necessário identificar quais são as chaves primárias da origem, para realização essa ação é necessário acessar o painel de opções de ligação.

A configuração das chaves fica conforme a próxima imagem:

# Validação do Conceito

Para verificar a construção de conceito em casos de execução com erros, deve-se observar os seguintes pontos:

**1 - Configurações das opções avançadas de ligação.**

No botão destacado em vermelho para acessar a janela de configurações avançadas.

Esta janela deve conter as corretas configurações de chaves primárias (PKs) para que durante o processo os registros sejam lidos corretamente em caso de atualização ou exclusão de registros.

Erros de violação de chave estrangeiras estão relacionados com essa configuração de PK.

**2 - Conexão de destino como um data server.**

Quando a conexão de destino é um data server como o FopFuncData, deve-se lembrar que as mesmas regras para salvar/alterar um registro no data server serão válidas na importação por conceito.

Isto significa que devem ser conferidos?

* Campos obrigatórios.
* Existência de outros cadastros necessários como coligada, seções, históricos, entre outros.

**3 - Tipos de dados dos campos importados.**

O tipo de dados dos campo importados devem estar corretamente configurados de acordo com seus correspondentes  na tabela de destino.

Você também pode usar painéis visuais para comunicar informações relacionadas, dicas ou recomendações de alerta ao usuário.

## Artigos relacionados

Os artigos relacionados aparecem aqui baseados nos rótulos que você selecionar. Clique para editar a macro e adicionar ou alterar os rótulos.

false5LRMfalsemodifiedtruepagelabel in ("funcionário","conceito") and type = "page" and space = "LRM"Funcionário Conceito

true

|  |  |
| --- | --- |
| Ocorrências relacionadas |  |
