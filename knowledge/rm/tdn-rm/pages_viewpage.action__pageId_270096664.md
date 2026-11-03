---
content_hash: eb1a1d4483b9938401bf62c7582eba5b5c1b651d0cd0fd7e397ca400888dbedc
fetched_at: '2026-06-29T00:08:23.888962+00:00'
page_id: '270096664'
product: rm
source: tdn-rm
title: Criação de Parametros do Factor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270096664
version: 6
---

# Criação de Parametros do Factor / Factor - Estoque de Terceiros

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | **RM** | | |
| ****Segmento Executor:**** | **Construção e Projetos** | | |
| **Módulo:** | *Gestão Planejamento e Controle da Produção* | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Parâmetros* | *Não se aplica* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Parâmetros do RMFactor* | *Não se aplica* | |  |  | | | |
| **Chamado:** | *N/A* | | |
| **Requisito (ISSUE):** | CPMOV001-877 | | |
| **País:** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

### Objetivo

Permitir que o usuário configure o uso do estoque de terceiros no processo produtivo.

### Definição da Regra de Negócio

Para habilitar o controle do estoque de terceiros é necessário realizar algumas parametrizações no RMFactor, são elas:

Na página "Gerais", habilitar o parâmetro "Controla Estoque Terceiro", outros parâmetros serão liberados para configuração.

Na página "Movimentação de Estoque" no grupo "Movimentação Estoque de Terceiros" deve ser definido os movimentos utilizados para movimentação do estoque de terceiro, são eles:

1. Tipo de movimento de empenho de matéria-prima
2. Tipo de movimento de baixa de matéria-prima
3. Tipo de movimento de devolução de matéria-prima
4. Tipo de movimento de entrada de perda de material

Na página "Locais de Estoque":

* Na página "Matéria-prima Terceiro", configurar o local onde é armazenado as matérias-primas de terceiro (local padrão) e outros caso exista.
* No grupo "Matéria-Prima Empenhada", página "Empenho Terceiro" configurar o local de empenho utilizado para materiais de terceiros.
* No grupo "Matéria-Prima Empenhada", página "Perda Material Terceiro" configurar o local de destino de materiais perdidos.

Na página "Apontamento",

* Se estive controlando estoque de terceiro deve-se definir qual a prioridade de consumo dos matérias utilizados na ordem de produção, tem três possibilidades, sendo que o padrão é "Estoque próprio":  
    
  1. Estoque Próprio - Consome primeiro material próprio antes de consumir materiais de terceiros.
  2. Estoque Terceiro - Consome primeiro material de terceiro antes de consumir materiais do estoque próprio.
  3. Estoque Ambos - Para materiais que possuem regras de prioridade como validade-lote vai consumir o de maior prioridade considerando ambos os estoques, se não tem prioridade então consome primeiro o estoque próprio.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros do RMFactor | Alteração | RMFactor -> Opções -> Parâmetros -> Produção | - |
|  |  |  |  |

-   Baixa de Matéria-Prima de Terceiros: deverá permitir que sejam informados somente os tipos de movimento de baixa de Estoque de Terceiros do Nucleus.

* **Campo**: CODTMVSAIDATRCR
* **Tipo:** DKCODTIPOMOV
* **Aceita nulo:** Sim
* **Descrição:** Tipo de Movimento de Saída no Estoque Terceiro

-   Devolução de Matéria-Prima de Terceiros: deverá permitir que sejam informados somente os tipos de movimento de devolução de Estoque de Terceiros do Nucleus.

* Campo: CODTMVENTRADAMPTRCR
* **Tipo:** DKCODTIPOMOV
* **Aceita nulo:** Sim
* **Descrição:** Código Movimento entrada Materia Prima Terceiro

-   Empenho de Matéria-Prima de Terceiros: deverá permitir que sejam informados somente os tipos de movimento de transferência de Estoque de Terceiros do Nucleus.

* Campo: CODTMVTRANSFESTQRESERVATRCR
* **Tipo:** DKCODTIPOMOV
* **Aceita nulo:** Sim
* **Descrição:** Cód.mov.da transf.p/estoque de reserva terceiro

-   Entrada de Perda de Material de Terceiros: deverá permitir que sejam informados somente os tipos de movimento de devolução de Estoque de Terceiros do Nucleus.

* **Campo:** CODTMVENTRADAPERDAMATERIALTRCR
* **Tipo:** DKCODTIPOMOV
* **Aceita nulo:** Sim
* **Descrição:** Tipo Mov. Perda Material

Esses campos não devem ser obrigatórios, pois deverão ser preenchidos somente quando a empresa controla Estoque de Terceiros e realiza produção com produtos de terceiros.

O parâmetro “Controla estoque de terceiro” na página Gerais dos parâmetros do FACTOR habilita as parametrizações e uso do estoque de terceiros na produção.

* **Campo:** KPARAMETROSFACTOR.CONTROLAESTOQUETERCEIRO
* **Tipo:** SmallInt
* **Aceita nulo:** Sim
* **Descrição:** Controla estoque de terceiros

***Não é necessário parâmetro de “Saldo físico utilizado” ou “Origem do Custo” para estoque de terceiro pois ambos são fixos e não configuráveis no sistema de gestão de estoque e faturamento.***

* Locais de Estoque:

Deverá ser criado um campo para que seja informado o local de estoque em que se encontra o Estoque de Terceiros. Esse campo deverá ser informado somente quando a empresa controla Estoque de Terceiros e realiza produção com produtos de terceiros. Deverá ser informado mesmo que o local de estoque do Estoque de Terceiros seja o mesmo do Estoque Próprio.

Nos parâmetros de produção, na página “Locais de Estoque” deve ser criada uma nova página “Terceiros” (Visão/Edição) onde vai ser definido o local de estoque de terceiros padrão e secundários (Grid).

Nos parâmetros de produção, na página “Locais de Estoque”, na parte inferior onde já existe o controle do local de empenho e perda de material através de combo de seleção, vai ser adicionando “Empenho - Terceiros” e “Perda de Material – Terceiros”

Essas informações ficam registradas na tabela KLOCALESTOQUE e a diferenciação de cada um se dá pelo campo TIPOLOCAL

Os novos registros serão representados como:

| TipoLocal | Descrição | (enum) |
| --- | --- | --- |
| R | Estoque de Terceiros – Padrão | leMateriaPrimaTerceiroDefault |
| L | Estoque de Terceiros | leMateriaPrimaTerceiro |
| G | Empenho – Terceiros | leEmpenhoMPTerceiro |
| D | Perda de Material – Terceiros | lePerdaMaterialTerceiro |

Delphi

  TTipoLocalEstoque = (leMateriaPrimaDefault, leAcabadoDefault, leMateriaPrima,

    leAcabado, leEmpenhoMP, leInvalid, leSemiAcabadoDefault, leSubProdutoDefault,

    leSemiAcabado, leSubProduto, lePerdaMaterial);

* Custos | Custo de Subprodutos Gerados (**Apenas comportamento do parâmetro**):

Quando neste parâmetro estiver marcada a opção “Utilizar Custo RM Nucleus” e o parâmetro “Controla estoque de terceiro” estiver marcado, o cálculo de custo do subproduto deverá considerar o custo do Estoque de Terceiros, quando houver a utilização de produtos de terceiros na produção.

* Deverá ser criado um parâmetro relacionado o parâmetro Apontamento | Default: Calcula Prop. Qtde. de Material Consumido para definir a prioridade de consumo dos produtos na produção, se irá consumir primeiramente os produtos de terceiros ou os produtos próprios.
  + **Campo**: KPARAMETROSFACTOR.PRIORIDADECONSUMOMPTERCEIRO
  + **Tipo:** SmallInt
  + **Aceita nulo:** Sim
  + **Descrição:** Considerar primeiro o material de terceiros na proporcionalizarão

Esse parâmetro somente vai ter funcionalidade se o parâmetro Apontamento | Default: Calcula Prop. Qtde. de Material Consumido estiver marcado e o parâmetro “Controla estoque de terceiro” estiver marcado**.**

## Restrições ao Salvar

* Se definiu que vai trabalhar com estoque de terceiro e utiliza empenho:
  + Deve definir o local de empenho de terceiro.
  + Deve definir o movimento de empenho de terceiro.

* Se definiu movimento de perda de material de terceiro:
  + Deve escolher o local de perda de material de terceiro.

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
