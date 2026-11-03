---
content_hash: d4265dbed7c4f3aa7e5e6ec1ff75ae87d5eeb060fd1983c95709c3d5b6bad19f
fetched_at: '2026-06-29T00:08:24.004494+00:00'
page_id: '270101795'
product: rm
source: tdn-rm
title: Item de Ordem de Produção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270101795
version: 6
---

# TRATAR ITEM DE ORDEM DE PRODUÇÃO / FACTOR - ESTOQUE DE TERCEIROS

## **Informações Gerais**

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| **Segmento Executor:** | Construção e Projetos. | | |
| **Módulo:** | Gestão de Planejamento e Controle da Produção. | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Item de Ordem de Produção | PCPItemOrdemAction. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Ordem de Produção. | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | | | |
| **Chamado:** | Não se aplica. | | |
| **Requisito (ISSUE):** | CPMOV001-875 | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

### Objetivo

 

Permitir que o usuário possa visualizar o quantitativo dos produtos em estoque de terceiros na pasta Necessidade de Materiais.

## Definição da Regra de Negócio

Quando o **Gestão de Planejamento e Controle da Produção** estiver configurado para **Controlar Estoque Terceiro**, na pasta Itens, na edição do Item da Ordem de Produção, em Necessidade de Materiais, será exibida uma coluna com o quantitativo dos produtos em estoque de terceiros. 

Esse quantitativo em estoque terceiros deverá ser o somatório das quantidades do produto, independentemente do Cliente/Fornecedor. 

As demais regras dessa tela permanecem inalteradas.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Item de Ordem de Produção | Alteração | RM Factor \ Produção \ Ordem de Produção \ Editar Ordem de Produção \ Itens | - |
| Ordem de Produção | Envolvida | RM Factor \ Produção \ Ordem de Produção | - |

* Criar o campo **Qtde. Estoque Terceiros** onde o usuário visualizará o somatório das quantidades do produto de estoque de terceiros necessária para ser utilizado na Ordem de Produção. Esta coluna será apresentada somente quando o sistema estiver configurado para Controlar Estoque Terceiro (Opções \ Parâmetros \ Produção \ Gerais).

**Cálculo do MRP**

Será necessário evoluir o serviço de cálculo do MRP - Material Requirements Planning, para que considere o estoque de terceiros. Abaixo são listados os pontos do serviço que precisam ser evoluídos:

* Adicionar ao serviço de Cálculo MRP a disponibilidade do produto de estoque de terceiros.
* Acrescentar ao método que *define o material consumido* a informação da quantidade total do produto em estoque de terceiros.
* Acrescentar o método que *escolhe entre o material disponível qual será consumido pela ordem*.
* A *quantidade de material considerado para a atividade* deve levar em consideração a quantidade total do material considerado do estoque de terceiros.

**Tabelas Utilizadas**

* KATVORDEMMP – Consumo de matéria prima da atividade.

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
