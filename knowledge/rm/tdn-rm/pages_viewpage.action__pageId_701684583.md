---
content_hash: 082b2c59b24a4454954c93e33606c2709b864124ade8cc60d8dfbe46d602318e
fetched_at: '2026-06-29T00:11:22.372152+00:00'
page_id: '701684583'
product: rm
source: tdn-rm
title: Criar Item em uma Tabela Dinâmica usando fórmula visual.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=701684583
version: 3
---

# Objetivo:

---

     Este documento tem por objetivo especificar como criar uma fórmula visual para inserir dados em uma tabla dinâmica.

# Especificação:

---

     Criaremos uma formula visual para adicionar registros em uma tabela dinâmica usando o Data Server GlbItemDinamData. Devido a sua complexidade, esta atividade exige um nível de conhecimento avançado em Fórmula Visual e em codificação.

Pré-requisito: É necessário conhecimento de como  [Ler registros de uma tabela dinâmica usando fórmula visual.](https://tdn.totvs.com/pages/viewpage.action?pageId=701684268)

## **Criando a formula visual**

---

Ainda no modulo de **Serviços Globais** selecione o menu **Gestão**e localize o combobox com o nome **Fórmula visual** exiba as opções e selecione **Fórmula visual**

Siga os passos abaixo para criar uma nova formula visual, informe os dados de **Identificação**como o exemplo:

Agora que foi criada a formula podemos editar o Workflow clicando duas vezes sobre o registro na listagem:

Será exibido a tela de RMSWorkflow que permite a execução de um grupo de atividades em uma sequência.

Nessa tela existem 3 abas:

1. **Propriedades**: Onde encontramos as propriedades globais do Workflow como Nome, Classe Base, Descrição, Contexto entre outros.
2. **Atividades**: É uma toolbox com uma serie de atividades que podemos incluir ao nosso Workflow, arrastando o componente para a área de fluxo de trabalho sequencial.
3. **Estrutura**: Onde é exibido uma arvore de dados os recursos usados pelo Workflow.

## **Construindo o Workflow que consultar os registros da tabela dinâmica.**

---

Agora construiremos nosso Fluxo de trabalho.

Utilizaremos a tabela dinâmica criada nesse exemplo: [Ler registros de uma tabela dinâmica usando fórmula visual.](https://tdn.totvs.com/pages/viewpage.action?pageId=701684268) na sessão **Criando tabela dinâmica no RM**

Primeira atividade que adicionaremos ao Workflow é "Ler registro"

Em atividades pesquise por Ler Registro, arraste o componente ao Fluxo de trabalho.

Esse **rmsReadRecordActivity1** é utilizado para obter a estrutura da tabela que iremos inserir um novo item.

Clique na atividade de Ler Registro(**rmsReadRecordActivity1**) adicionada ao fluxo, e no menu lateral esquerdo selecione a aba **Propriedades**.

Informaremos no **Dados de Usuario(OwnerDara)** o nome da tabela que armazena os itens da tabela dinâmica, inserido nesse caso o nome **PSERVERBANCO**

Para compreender como conseguimos o nome da tabela que armazena os itens consulte esse documento: [Ler registros de uma tabela dinâmica usando fórmula visual.](https://tdn.totvs.com/pages/viewpage.action?pageId=701684268)

A primeira propriedade que deve ser preenchida é Nome do **DataServer**, o data server que gerencia os itens de tabelas dinâmicas é o **GlbItemDinamData**para localizar esse data server basta clicar no botão ao lado da propriedade, uma tela de pesquise será exibida, pesquise por "Item de tabela Dinâmica" e clique no item com o mesmo nome na listagem.

Agora iremos que **Nome do DataServer** foi selecionado, um novo item será inserido nas propriedades, a propriedade **Código**da sessão **Chave Primaria da Leitura.**

Atribuiremos valor 1 correspondente e um registro que já existe na tabela:

Query: *SELECT CODCOLIGADA, APLICACAO,CODCLIENTE, CODTABELA, CODINTERNO, DESCRICAO, PODEALTERAR FROM PSERVBANCO WHERE CODTABELA = 'TBTESTE' ;*

test

Caso não queira selecionar um registro especifico pode informar o valor -1 na propriedade **Código**da sessão **Chave Primaria da Leitura.** Dessa forma ele consulta todos os registros existentes ou não e obtém a estrutura da tabela(***CODCOLIGADA, APLICACAO,CODCLIENTE, CODTABELA, CODINTERNO, DESCRICAO, PODEALTERAR*** ) que será usada ao adicionar um novo registro.

Agora incluiremos uma atividade que preenchera essa estrutura(**DataSet**) que obtivemos no passo anterior.

Em atividades pesquise por Adicionar Registro, arraste o componente ao Fluxo de trabalho.

Esse **rmsAddTableRowActivity1** é utilizado para informar quais os dados serão inseridos na tabela preenchendo a estrutura obtida anteriormente:

Selecionando a atividade **rmsAddTableRowActivity1 na aba propriedades clique no ícone Ligações depois clique no botão que fica ao lado da propriedade Tabela**

Vamos associar o DataTable obtida na **rmsReadRecordActivity1** a propriedade **Tabela**

Após informar a tabela uma nova sessão nas propriedades é criada **GITEMDINAM,** nesse exemplo preenchemos os valores manualmente mas é possível criar **Atividades de Expressão** para armazenar os valores e associar as propriedades da **GITEMDINAM**

Respeite o tipo de dado e o tamanho suportado por cada propriedade consultando as informações da tabela no banco de dados.

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| **APLICACAO** | Código da aplicação que esta usando no RM. |
| **CODCOLIGADA** | Código da coligada. |
| **CODIGO** | Chave do item que será inserido na tabela dinâmica, como se trata de uma chave esse valor não pode ser duplicado, caso isso aconteça gera uma exceção: . ***Cannot insert duplicate key in object*** |
| CODINTERNO | Outro código para identificação internada. |
| DESCRICAO | Do item a ser inserido. |
| **CODTABELA** | Nome da tabela dinâmica que será inserido o item. |

Agora incluiremos uma atividade que salvara os dados.

Em atividades pesquise por **Salvar Registro**, arraste o componente ao Fluxo de trabalho.

Esse **rmsAddTableRowActivity1** é utilizado para informar quais os dados serão inseridos na tabela preenchendo a estrutura obtida anteriormente:

Selecionando a atividade **rmsSaveRecordActivity1** na aba propriedades **Atividade Ler Registro** selecione a **rmsReadRecordActivity1**

Precisamos informar a tabela que será inserido esse registro na propriedade **Dado de Usuário(OwnerData) = PSERVBANCO** e na propriedade **Nome do DataServer** = **GlbItemDinamData**

Agora basta clica em Salvar e Executar

Pronto o registro foi inserido na tabela dinâmica
