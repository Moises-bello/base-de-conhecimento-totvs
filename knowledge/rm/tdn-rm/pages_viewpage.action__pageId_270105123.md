---
content_hash: dcfa6ab4d974b8564ca651e63fcf160020c460c37221c4acfa09f5a8a65bb791
fetched_at: '2026-06-29T00:08:24.131593+00:00'
page_id: '270105123'
product: rm
source: tdn-rm
title: Ordem de produção - Fornecedor relacionado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270105123
version: 2
---

# Ordem de produção - fornecedor relacionando / Factor - Estoque de Terceiros

# 

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | **RM** | | |
| ****Segmento Executor:**** | **Construção e Projetos** | | |
| **Módulo:** | **Gestão Planejamento e Controle da Produção** | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Fornecedor vinculado a ordem de produção* | **PCPOrdemTerceiro*.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Controle de estoque de terceiro*.* | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | | | |
| **Chamado:** | *N/A* | | |
| **Requisito (ISSUE):** | CPMOV001-877*.* | | |
| **País:** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

### (Obrigatório)

## Objetivo

 

Permitir que o usuário configure os fornecedores (terceiros) vinculados a ordem de produção quando estiver parametrizado para utilizar  estoque de terceiros no processo produtivo.

### (Obrigatório)

### Definição da Regra de Negócio

Caso nos parâmetros gerais esteja parametrizado para controlar Estoque de Terceiros, , é possível chamar o cadastro de fornecedores (terceiros) para que sejam informados quais o clientes/fornecedores terão os seus produtos utilizados na Ordem de Produção.

 

Poderá ser excluído um cliente/fornecedor que tenha sido informado, desde que não tenha ocorrido consumo do produto desse cliente/fornecedor. Esse campo é apenas informativo.

Na aba Itens, na **edição** do item da ordem de produção, em Necessidade de Materiais, caso nos parâmetros “Gerais” esteja parametrizado para controlar Estoque de Terceiros, deverá ser exibida uma coluna com o quantitativo dos produtos em estoque de terceiros.

Esse quantitativo em estoque terceiros deverá ser o somatório das quantidades do produto, independentemente do cliente/fornecedor.

 

As demais regras dessa tela permanecem inalteradas.

TABELA:

* KORDEMTERCEIRO Fornecedores terceiros associados a ordem de produção

 

     CAMPOS:

* CODCOLIGADA DCODCOLIGADA 02 NOT NULL Codigo da Coligada
* CODFILIAL SmallInt 02 NOT NULL Código da filial

* CODORDEM DKCODIGO 10 NOT NULL Codigo da Ordem

* CODCOLCFO DCODCOLIGADA 02 NOT NULL Codigo coligada fornecedor

* CODCFO varchar 25 NOT NULL Código do Fornecedor

* SOLICITANTE DLOGICONULL 02 NULL Terceiro solicitante da produção

 

PK ->

* CODCOLIGADA, CODFILIAL, CODORDEM, CODCOLCFO, CODCFO

 

FK

* KORDEMTERCEIRO (CODCOLIGADA, CODFILIAL, CODORDEM) com

* KORDEM (CODCOLIGADA, CODFILIAL, CODORDEM)

 

*<Regra de negócio é o que define a forma de fazer o negócio, o processo definido e/ou as regras que devem ser contempladas. Devem ser descritas restrições, validações, condições e exceções do processo. *Incluir as telas do sistema com o objetivo de facilitar o entendimento do requisito, apresentar conceitos e funcionalidades do software.*Caso necessário, incluir neste capítulo também regras de integridade que devem ser observadas no momento do desenvolvimento - ***É o Detalhamento das Story linkadas no Epic***>.*

*<Na tabela abaixo informe quais são as rotinas envolvidas, o tipo de operação, a opção de menu e se necessário uma breve descrição das regras de negócio relacionadas a rotina>.*

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

***Exemplo de Aplicação:***

* *Criar o campo “% Mínimo Espécie” (AAA\_PERESP) onde o usuário informará o % que o aluno pagará em dinheiro. Esse % poderá ser alterado durante a negociação.*
* *Criar o campo “Referência Mínima para Cálculo” (AAA\_REFCAL) onde o usuário informará um dos 4 valores disponíveis para pagamento das mensalidades  como a referência mínima para calcular o débito total do aluno.*
* *Criar o parâmetro MV\_ACPARNE que definirá se as informações de “% Mínimo Espécie” e “Referência Mínima para Cálculo” serão obrigatórias.*
* *O parâmetro MV\_ACPARNE deve ter as seguintes opções: 1=Obrigatório e 2=Opcional. Deve ser inicializado como opcional>.*

***Tabelas Utilizadas***

* *SE2 – Cadastro de Contas a Pagar*
* *FI9 – Controle de Emissão de DARF>.*

### (Opcional)

## Procedimento para Utilização

*<Descreva os procedimentos, passo a passo (caso de uso), que serão realizados pelos usuários para que a melhoria seja visualizada identificando as seguintes informações;*

*Localização da rotina no menu;*

*Localização dos novos campos e/ou perguntas e respectivas pastas de cadastro que são visualizadas pelo usuário;*

*Caso seja necessário ter algum cadastro feito previamente, faça uma observação*

*Se necessário, utilizar prints de tela>.*

## Procedimento para Configuração

*(Estes procedimentos devem ser feitos quando for necessário configurar parâmetros e/ou  rotinas no menu).*

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Configurador (SIGACFG)**, acesse **Ambientes/Cadastros/Parâmetros (CFGX017)**. Crie/configure *(mantenha somente a instrução correspondente)* o(s) parâmetro(s) a seguir:  
   *(É necessário criar uma tabela para cada parâmetro descrito no item **Parâmetro(s)**, da tabela **Características do Requisito**)*

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** |  |
| **Tipo:** | *Informe o Tipo do parâmetro* |
| **Cont. Por.:** | *Informe o Conteúdo padrão* |
| **Descrição:** |  |

**CONFIGURAÇÃO DE MENUS**

2.  No **Configurador (SIGACFG),**acesse **Ambientes/Cadastro/Menu (CFGX013)**. Informe a nova opção de menu do *informe **o nome do módulo***, conforme instruções a seguir:

|  |  |
| --- | --- |
| **Menu** | *Informe o Menu em que estará localizada a rotina* |
| **Submenu** | *Informe o Submenu em que estará localizada a rotina* |
| **Nome da Rotina** | *Informe o Título da rotina* |
| **Programa** | *Informe o Fonte da rotina* |
| **Módulo** | *Informe o Nome do(s) produto(s) a ser utilizado ou “Todos”* |
| **Tipo** | *Informe a Função* |

### Opcional

## Fluxo do Processo

*<Nesta etapa incluir representações gráficas que descrevam o problema a ser resolvido e o sistema a ser desenvolvido. Exemplo: Diagrama - Caso de Uso, Diagrama de Atividades, Diagrama de Classes, Diagrama de Entidade e Relacionamento e Diagrama de Sequência>.*

### Opcional

## Dicionário de Dados

**Arquivo ou Código do Script:** AAA – Negociação Financeira / \*Versao=CP.2014.12\_03\*/

 

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | <FI9\_FILIAL+FI9\_IDDARF+FI9\_STATUS> |
| **02** | <FI9\_FILIAL+FI9\_FORNEC+ FI9\_LOJA+FI9\_EMISS+FI9\_IDDARF> |
| **03** | <FI9\_FILIAL+FI9\_FORNEC+ FI9\_LOJA+FI9\_PREFIX+FI9\_NUM+FI9\_PARCEL+FI9\_TIPO> |

|  |  |
| --- | --- |
| **Campo** | <AAA\_PERESP> |
| **Tipo** | <N> |
| **Tamanho** | <6> |
| **Valor Inicial** | <Varia de acordo com o tipo informado. Por exemplo, quando o campo “tipo” for date, neste campo pode ser informado uma data>. |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | <Referência Mínima para Cálculo> |
| **Título** | <Ref.Calc.> |
| **Picture** | <@E999.99> |
| **Help de Campo** | <Informar o % que o aluno pagará em dinheiro. Esse % poderá ser alterado durante a negociação> |
