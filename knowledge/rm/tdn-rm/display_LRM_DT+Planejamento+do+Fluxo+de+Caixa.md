---
content_hash: b484c2498b5ee8d0c004c4a3873da7b1162322d8cd4254b6125402dd0425ea78
fetched_at: '2026-06-29T00:09:11.467622+00:00'
page_id: '404915405'
product: rm
source: tdn-rm
title: DT Planejamento do Fluxo de Caixa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Planejamento+do+Fluxo+de+Caixa
version: 58
---

# Planejamento do Fluxo de Caixa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Planejamento de Fluxo de Caixa | Novo planejamento de fluxo de caixa |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Informe a(s) rotina(s) envolvidas. | Informe o nome técnico da(s) rotina(s) envolvidas. | |  |  | |
| **Cadastros Iniciais:** | Tipo de Planejamento. |
| **Parâmetro(s):** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7387> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQLServer e Oracle |
| **Tabelas Utilizadas:** | FTIPOPLANEJAMENTOFLXCX, FPLANEJAMENTOFLXCX |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.29 |

## Descrição

Implementação de um novo Fluxo de Caixa, utilizando padrões de Planejado, Previsto, e Realizado.

CadastrosTipos de planejamento

Representa o tipo de valor para um determinado planejamento de fluxo de caixa no TOTVS Gestão Financeira.  
Todo e qualquer planejamento do fluxo de caixa estará vinculado a um tipo de planejamento, permitindo categorizar os valores de forma flexível.

## Procedimento para Utilização

* O Cadastro de tipos de planejamento deve primeiramente ser habilitado no perfil do usuário:

* Após habilitação via perfil, o cadastro de tipos de planejamento estará localizado em Gestão Financeira | Tipos de planejamento:

Ao acessar este menu, será possível inserir um filtro, caso necessite realizar uma pesquisa sobre determinado campo, como descrição, código, data de alteração, etc.

* O cadastro de tipos de planejamento possui os campos:

Código: Código deverá ser único na base (Alfanumérico 3);

Descrição: A descrição do tipo de planejamento (Alfanumérico 100);

Inativo: Define se o tipo de planejamento estará ativo ou inativo no sistema, ou seja, se deverá ser utilizado ou não em novos planejamentos.

Planejamentos

O cadastro de planejamento permite ao usuário informar valores para que possam ser levados para um fluxo de caixa e posteriormente auxiliar na definição de diversos cenários, isto é, estimar e planejar os gastos e recebimentos da empresa em determinado período e de acordo com as informações deste planejamento.

## Procedimento para Utilização

* Deverá ser habilitado, no perfil do usuário a permissão do cadastro de planejamento, disponível em Gestão Financeira | Fluxo de Caixa | Cadastros de planejamento:

Obs: O planejamento deverá estar atrelado a um tipo de planejamento que foi cadastrado previamente.

Poderão existir vários planejamentos para um determinado tipo de planejamento.

## Descrição dos campos:

Interface de **Planejamento de Fluxo de Caixa**:

Este cadastro é composto dos seguintes campos:

* **ID. Planejamento**: Identificação única do planejamento;
* **Tipo Planejamento**: Determina o tipo de planejamento ao qual o planejamento está associado;
* **Descrição**: A descrição do planejamento;
* **Data Início**: Data inicial do planejamento;
* **Data Final:** Data final do planejamento;
* **Permite Multicoligada:** Define se o cadastro de planejamento poderá ser incluído para N coligadas, caso marcado, ou somente para a coligada corrente, caso desmarcado. Observação: Caso a opção "Global" de um cadastro de planejamento estiver marcada e neste planejamento houver itens para diferentes coligadas, o sistema não permitirá a alteração deste parâmetro.

**Item de Planejamento**

Os itens do Planejamento podem ser inseridos e exibidos no anexo da visão ou no anexo do planejamento cadastrado

O cadastro de um item de planejamento é composto dos seguintes campos:

* **Valor**: onde será informado o valor do item;
* **Data**: onde será informada a data de inclusão do item;
* **Natureza**: onde será informado se o item é  a pagar ou a  receber;
* **Aplicação Origem**: onde será informado qual o produto de origem do item;
* **Histórico**: onde será informado um contexto que facilite sua identificação;
* **Coligada**: onde será informada a coligada a qual pertence o item. Nesse caso, se no cadastro do planejamento a opção "Multicoligada" estiver marcada, é possível a edição do campo. Caso desmarcada, essa opção será carregada com a coligada default de inclusão do item (coligada corrente);
* **Filial**: onde será informada a filial a qual pertence o item de planejamento;
* **Centro de custo**: onde será informado o centro de custo que irá compor o item de planejamento;
* **Natureza orçamentária**: onde será informada a natureza orçamentária do item, podendo ser de classificação a pagar, a receber ou ambos.

**Observações:**

Há a possibilidade de edição dos campos diretamente nas grids, bem como inclusão e exclusão (botão verde de inclusão / x vermelho) de itens de acordo com o planejamento.

Poderão ser inseridos vários itens para um determinado planejamento, como mostra a figura abaixo.

Não será permitido a inclusão de item de planejamento de mesma Natureza, Aplicação de Origem, Centro de Custo, Filial e Natureza Orçamentária  dentro do mesmo período.

Visão do Planejamento:

Planejamento:

Edição de Itens de Planejamento

                                                                                

Importação via conceito

## Importação dos dados do planejamento via Conceito

Criado novo conceito para poder realizar importação dos dados do orçamento, itens de orçamento e períodos de orçamento previamente cadastrados no TOTVS Gestão Estoque Compras e Faturamento.

### **Novo planejamento**

Ao executar a importação de dados do planejamento utilizando o conceito, deve-se criar as informações de identificação do planejamento através da seleção de planejamento disponível na tela de processo de execução do conceito.

Ao incluir um novo planejamento, o usuário poderá informar uma descrição para o planejamento, um tipo de planejamento, o período do planejamento e se o planejamento terá escopo de multi-coligada.

Obs.: O período informado nesse cadastro será utilizado pelo conceito como o período de busca de informações de planejamento na base de dados.

Após o cadastro destas informações, ao selecionar este planejamento e executar o processo de importação, os itens do planejamentos serão inseridos.

Obs.: Caso haja itens de planejamentos duplicados, ou seja, com a mesma Natureza, Aplicação de Origem, Coligada, Centro de Custo, Natureza Orçamentária  e Filial dentro do mesmo período(Mês/Ano) , na importação do conceito haverá agrupamento para que não sejam gerados itens duplicados.

### **Planejamento existente**

No formulário de conceito em execução, informar o planejamento que deve ser atualizado, executar o processo.

Todos os itens de planejamento já existentes na base de dados serão excluídos, com exceção dos itens de planejamento do TOTVS Gestão Financeira. Os novos dados provenientes dessa nova importação serão inseridos ao planejamento informado.

Obs: A mesma regra de itens duplicados será aplicada nesta nova importação.

## **Edição para funcionamento**

Para realizar o processamento, faça a importação do Conceito na sua base de dados e faça as seguintes alterações.

Primeiro edite a conexão de origem para modificar a string de conexão. Faça em todas as conexões de Origem que forem relacionadas a banco de dados. Neste exemplo, edite ITEMPLANEJAMENTO e DADOSPLANEJAMENTO conforme animação abaixo.

A CONEXÃO DE DESTINO não precisa ser modificada, pois será utilizado um RMSDataServer que utiliza a conexão do RM.

Os dados informados devem ser os mesmos que estão sendo utilizados no Alias conectado.

Os dados de usuário e senha são os responsáveis para conectar na instância do SQL. Lembrando que existe a possibilidade de fazer várias conexões, como Oracle, e até mesmo existe a possibilidade de buscar dados via arquivo e etc.

Exemplo de string de conexão: Data Source=NOMEMAQUINA;Initial Catalog=NOMEBD;User ID=rm;Password=\*\*;Enlist=False

## **Como o Conceito funciona**

No cadastro de conexão de origem foi criado uma consulta SQL para trazer os dados do orçamento (como exemplo) para ser enviado para o novo cadastro do planejamento de fluxo de caixa.

Lembrando que a fonte de dados pode ser a que o usuário necessitar, não necessariamente uma consulta SQL. O importante é ter os dados/campos necessários para fazer a importação.

A Consulta SQL pode conter parâmetros para sua execução que pode ser informado durante o processamento do conceito.

Com a conexão de origem parametrizada vamos preencher a conexão de destino que será o RMSDataServer FinPlanejamentoImportacaoData.cs .

**IMPORTANTE:** Lembrando sempre de utilizar o DataServer pois o mesmo passa por diversas validações dos dados que serão cadastrados. Caso seja enviado diretamente no banco de dados, não haverá garantia que os dados estão corretos.

## **Ligações**

As ligações são as parametrizações do que corresponde um dado da conexão de origem para os dados de destino.

Tudo se baseia em clicar e arrastar para adicionar os valores.

## **Execução**

Com tudo parametrizado, vamos fazer a execução.

O Tipo de Planejamento deve ser selecionado no processo ou cadastrado um novo, para que os itens possam ser carregados através de consulta SQL e a data informada, como mostrado anteriormente:

**Tipo de Planejamento:** deve ser informado ou cadastrado previamente na execução.

Cenários Fluxo de CaixaCenários Fluxo de CaixaCenários Fluxo de Caixa

Ao gerar o Fluxo de Caixa e realizar a conferência dos dados gerados o sistema possibilita salvar os dados criando um Cenário de Fluxo de Caixa. Na aba "Configurações", o usuário deve informar a descrição do cenário e clicar no botão "Gravar Cenário", assim as informações geradas e as parametrizações serão salvas no sistema.

Para poder ter acesso a funcionalidade de cenários, é necessário conceder permissão ao perfil do usuário.

Visualizar Cenários

É possível criar vários cenários com diferentes parametrizações no sistema para posterior visualização pela visão de Fluxo de Caixa. Após gerado um cenário poderá ser editado, mas ao salvar as alterações, será criada uma nova versão do mesmo que poderá ser usada para posterior comparação de diferentes versões (somente entre cenários de mesma origem).

**Obs:** Importante ressaltar que os dados visualizados irão seguir toda parametrização informada no momento em que este foi salvo.

O sistema permite visualizar todos os cenários salvos existentes na base.

 Informações Complementares

[DT - Novo Fluxo de Caixa](https://tdn.totvs.com/display/LRM/DT+Novo+Fluxo+de+Caixa+-+12.1.26)
