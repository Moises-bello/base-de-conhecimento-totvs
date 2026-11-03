---
content_hash: 90650a12187b4996453ddf7df48ad8958fb5afe59aecaff886af9667fe678cec
fetched_at: '2026-06-29T00:11:22.363121+00:00'
page_id: '701684268'
product: rm
source: tdn-rm
title: Ler registros de uma tabela dinâmica usando fórmula visual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=701684268
version: 10
---

## Objetivo:

---

     Este documento tem por objetivo especificar como criar uma fórmula visual para obter dados de uma tabela dinâmica.

## Especificação:

---

     Criaremos uma formula visual para obter registros de uma tabela dinâmica usando o Data Server GlbItemDinamData. Devido a sua complexidade, esta atividade exige um nível de conhecimento avançado em Fórmula Visual e em codificação.

## Criando tabela dinâmica no RMcriando-tabela-dinamica

---

Criaremos uma tabela dinâmica no RM e adicionaremos registros na mesma para consultar em nossa formula visual.

**Dados para criar a Tabela Dinâmica**

|  |  |  |
| --- | --- | --- |
| **Campos do formulario** | **Descrição de cada campo** | **Valor Inserido** |
| **Código** | Nome da Tabela | "TBTESTE" |
| **Descrição** | Descreve da tabelas | "Tabela dinâmica de teste" |
| **Finalidade** | Determina a finalidade da tabela | 1 |

 

**Bando de dados**

Os registros de Tabela Dinâmica são armazenados na tabela **GDINAM**

Executando a seguinte query: *SELECT CODCOLIGADA, APLICACAO, CODIGO, FINALIDADE, DESCRICAO, NOMETABELA FROM GDINAM ORDER BY RECCREATEDON DESC;*

Conseguimos localizar os dados de nossa tabela **TBTESTE**

**Dicionário de dados da tabela GDINAM**

|  |  |
| --- | --- |
| **COLUNA** | **Descrição de cada campo** |
| CODCOLIGADA | Código da coligada, se valor for 0 todas as coligadas poderão ver esse registro |
| APLICACAO | Código da aplicação que esta usando no RM. |
| CODIGO | É o nome da tabela dinâmica. |
| FINALIDADE | Determina qual a finalidade da tabela |
| DESCRICAO | Descreve a tabela |
| NOMETABELA | Nome da tabela que armazenará os itens da tabela dinâmica. Essa tabela e determinada pela finalidade escolhida para a tabela dinâmica |

 

## Adicionando registro na Tabela dinâmica

---

Criaremos um item na tabela dinâmica que criamos.

Na visão de Tabelas Dinâmicas onde criamos a tabela, selecione o registro com o Código da tabela criada anteriormente, no caso a **TBTESTE** e clique no menu **Anexos** na toolbar acima da listagem ou use o atalho CTRL+A.

Ao Selecionar a opção **Item de Tabela Dinâmica,** ao lado da listagem principal será exibido a tela de **Anexos** onde adicionaremos um registro a tabela que criamos.

Banco de dados

Para localizar os itens da tabela precisamos saber onde os itens foram salvos essa informação fica salva na tabela GDINAM na coluna NOMETABELA.

Sabendo a tabela que será armazenados os itens, podemos consultar no banco de dados o novo registro que criamos, usaremos como condição na cláusula where o código da tabela, como nesse exemplo:

Query: SELECT CODCOLIGADA, APLICACAO, CODCLIENTE, CODTABELA, CODINTERNO, DESCRICAO, PODEALTERAR FROM **PSERVBANCO** WHERE **CODTABELA** = '**TBTESTE**';

Finalidade

Cada Finalidade selecionada na tabela dinâmica, define o nome da tabela no banco:

* Códigos de Serviços Bancários → Tabela **PSERVBANCO**
* Validação de Campos Complementares → Tabela **GCONSIST**

Portanto de acordo com a finalidade usada por sua tabela dinâmica, a tabela usada no filtro deve ser a correspondente.

## Criando a formula visual

---

Ainda no modulo de **Serviços Globais** selecione o menu **Gestão** e localize o combobox com o nome **Fórmula visual** exiba as opções e selecione **Fórmula visual**

Siga os passos abaixo para criar uma nova formula visual, informe os dados de **Identificação** como o exemplo:

Agora que foi criada a formula podemos editar o Workflow clicando duas vezes sobre o registro na listagem:

Será exibido a tela de RMSWorkflow que permite a execução de um grupo de atividades em uma sequência.

Nessa tela existem 3 abas:

1. **Propriedades**: Onde encontramos as propriedades globais do Workflow como Nome, Classe Base, Descrição, Contexto entre outros.
2. **Atividades**: É uma toolbox com uma serie de atividades que podemos incluir ao nosso Workflow, arrastando o componente para a area de fluxo de trabalho sequencial.
3. **Estrutura**: Onde é exibido uma arvore de dados os recursos usados pelo Workflow.

## Construindo o Workflow que consultar os registros da tabela dinâmica.

---

Agora construiremos nosso Fluxo de trabalho.

Primeira atividade que adicionaremos ao Workflow é uma Expressão que armazenara a chave do registro que iremos consultar na tabela dinâmica.

Para adicionar a atividade basta pesquisar na aba "Atividades" por Expressão e arrastar o componente para o Fluxo de Trabalho Sequencial.

Nesse exemplo a chave é armazenada na coluna **CODCLIENTE** da tabela **PSERVBANCO** **(**Conforme selecionada na **)**

Consultaremos o registro que incluímos nos passos anteriores, o código do registro é **1**então na propriedade "Expressões" digitaremos o valor 1:

A segunda atividade que adicionaremos ao fluxo é "Ler registro"

Em atividades pesquise por Ler Registro

Arraste o componente ao Fluxo de trabalho logo abaixo do primeira Atividade que adicionamos no passo anterior, clique na atividade de Ler Registro(**rmsReadRecordActivity1**) adicionada ao fluxo, e no menu lateral esquerdo selecione a aba **Propriedades**.

A primeira propriedade que deve ser preenchida é Nome do **DataServer**, o data server que gerencia os itens de tabelas dinâmicas é o **GlbItemDinamData**para localizar esse data server basta clicar no botão ao lado da propriedade, uma tela de pesquise será exibida, pesquise por "Item de tabela Dinamica" e clique no item com o mesmo nome na listagem.

A próxima propriedade que devemos informar é os **Dados de Usuario(OwnerDara)**

Essa propriedade recebe um Array de String com as seguintes informações:

1. O nome da tabela onde os itens da tabela dinâmica são salvos, no caso a tabela "**PSERVERBANCO" (**Conforme selecionada na **)**
2. Condições para uma clausula where localize os dados da table **" AND CODCOLIGADA = 0 AND APLICACAO = 'G' AND CODTABELA = 'TBTESTE'"**

Para informar esses dados criaremos uma nova atividade acima da atual **rmsReadRecordActivity1**

Em atividades pesquise por **Executar Código** arraste o componente para o fluxo de trabalho logo acima de **rmsReadRecordActivity1,** clique duas vezes sobre a nova atividade para editar o código:

Agora iremos informar os **Dados de Usuario(OwnerDara)** através de um bloco de código:

Dentro do bloco **codeActivity1\_ExecuteCode** crie um array com os dados informado anteriormente e atribua esse array a propriedade **OwnerData** da atividade **rmsReadRecordActivity1**

c#

**(**Conforme selecionada na , utilize a tabela correspondente**)**

Agora iremos informar a propriedade **Código** da sessão **Chave Primaria da Leitura,** esse campo só exibido após informar o **Nome do DataServer**

Associaremos o valor da **rmsExpressionActivity1** convertendo o valor para string:

Para exibir os dados da consulta convertermos o resultado em XML e exibiremos em uma exceção.

Para converter os dados da consulta em XML adicionaremos uma nova atividade em nosso fluxo **Transformar Registro em XML,** na propriedade tabela associaremos o valor da **rmsReadRecordActivity1****:**

Para obter somente o dados do **DataTable** selecione a opção **IgnoreSchema** na propriedade **ModoXml** na sessão **Diversos** dessa atividade:

Agora adicionaremos a atividade Gerar Exceção para exibir os dados do XML da etapa anterior

Nas propriedades dessa atividade associaremos o valor da **rmsRegistroXmlActivity1****:**

Agora basta **Salvar e Executar** o sistema gera uma Exceção e em sua mensagem exibe os dados os dados da tabela dinâmica comprovante que a consulta foi realizada com sucesso.
