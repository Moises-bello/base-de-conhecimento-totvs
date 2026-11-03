---
content_hash: 6f91b9f0027907be6ac4945122c6356e74a8e039f51b8e2e9124f8ee5d40a189
fetched_at: '2026-06-29T00:08:26.715926+00:00'
page_id: '271187801'
product: rm
source: tdn-rm
title: Empenho de Materiais
type: documentation
url: https://tdn.totvs.com/display/LRM/Empenho+de+Materiais
version: 5
---

# Empenho de Materiais / Factor - Estoque de Terceiros

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | **RM** | | |
| ****Segmento Executor:**** | **Construção e Projetos** | | |
| **Módulo:** | **Gestão Planejamento e Controle da Produção** | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Empenho* | *PCPEmpenhoVisaoAction.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Empenho de Materiais*.* | *PCPEmpenhoVisaoAction.* | |  |  | | | |
| **Chamado:** | *N/A* | | |
| **Requisito (ISSUE):** | CPMOV001-970 | | |
| **País:** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

## Objetivo

 Permitir que o usuário faça o empenho/desempenho de materiais, que reserva o material para produção movendo-o para um local de estoque exclusivo onde podemos considerar esses materiais reservados para a ordem que realizou o empenho.

## Definição da Regra de Negócio

Caso nos parâmetros gerais esteja parametrizado para utilizar empenho de matéria-prima então é possível empenhar materiais para uma ordem de produção.

Caso nos parâmetros gerais esteja parametrizado para controlar Estoque de Terceiros, [Criação de Parametros do Factor](http://tdn.totvs.com/pages/viewpage.action?pageId=270096664), e tenha fornecedor vinculado a  ordem de produção, [Ordem de produção - Fornecedor relacionado](http://tdn.totvs.com/pages/viewpage.action?pageId=270105123). Vai ser possível empenhar além do matérial próprio materiais de terceiros.

O  empenho de materiais é possível para ordem de produção que esteja com status em "aguardando recurso,  pronto para iniciar e parcialmente concluído";

O desempenho pode ser realizado em qualquer status da ordem, exceto criada,  desde que já tenha ocorrido empenho para ordem. O desempenho devolve o material empenhado para seu local de origem.

O empenho de material visualiza os locais de estoque parametrizados no sistema de produção, locais de matéria-prima, locais de subproduto e locais de semi-acabados, apenas materiais nesses locais são considerados para realização do empenho.

**Local de empenho:**

O local de empenho deve ser um local de acesso restrito, apenas o sistema de produção deve ter acesso a ele. Assim ao realizar o empenho o material que está no local de empenho é considerado como reservado ao sistema de produção.

**O que empenho faz?**

O empenho transfere o material do local de origem para o local de empenho deixando o material reservado para uma determinada ordem de produção, dessa forma quando a ordem entrar em produção pode baixar o material que já foi reservado para ela.

O empenho pode atuar tanto para material próprio quanto para material de terceiro, conforme parametrização do sistema.

O empenho não é um movimento de baixa, ele é um movimento de transferência. Isto significa que na ficha física financeira do produto empenhado, no saldo atual do produto continua exibindo a quantidade empenhada.

O empenho trabalha com todo tipo de material controlado no estoque, inclusive controlado por lote, série ou ambos.

## Procedimento para Utilização

Na visão da ordem de produção deve-se selecionar a ordem que deseja realizar empenho e então clicar no botão "Empenho de matéria-prima da ordem selecionada".

Vai ser exibida a visão do empenho de materiais contendo todos os produtos disponíveis para empenho considerando a necessidade da ordem de produção e os locais de estoque configurados.

Também vai ser exibido materiais que tenham sido previamente consumidos mas ainda não foram empenhados, só permitido para estoque próprio e quando parametrizado para permitir saldo intermediário negativo.

Um mesmo produto pode ter vários registros na visão quando:

1. É controlado por lote, cada lote um registro (linha).
2. É do local de estoque diferente.
3. É de terceiros, cada fornecedor um registro (linha).
4. Estoque de terceiro e próprio não se misturam, cada um em um registro separado.

O campo "Qtde. Disp" informa a quantidade do produto disponível e que pode ser empenhada.

O campo "Qtde. Necessidade" é o quando a ordem de produção necessita do produto.

O campo "Qtde Empenhado" é a quantidade que já foi empenhada do material em empenhos anteriores.

O campo "Qtde a ser Empenhado" é a quantidade do produto que vai ser empenhada. Se esse valor é **0.00** então nenhum empenho vai ser realizado para esse produto.

O campo "Qtde a ser Empenhado" pode ser negativo no caso de estar realizando desempenho de material.

**Sugestão:**

O campo "Qtde a ser Empenhado" é preenchido automaticamente gerando uma sugestão do que deve ser empenhado para a ordem, se estiver utilizando estoque de terceiros é possível alterar a prioridade da sugestão => parâmetros "Apontamento" alterar "Regra de proporcionalização deve priorizar";

As opções são:

1. Estoque próprio - O material de terceiros só é considerado quando não tem estoque próprio.
2. Estoque de terceiros - O material próprio só é considerado quando não tem material de terceiros.
3. Estoque de Ambos - O material é considerado em conjunto, a principal diferença é a consideração da validade de lote que vai preferir usar o de menor validade entre ambos.

Quando todos os registros do empenho estiverem corretamente configurados clique em "OK" para realização do empenho.

**Edição**:

Na edição é possível alterar a quantidade a empenhar alterando o campo "Quantidade" e clicando em "OK" ou "Salvar".

O campo Fornecedor só é exibido se o material editado for de um fornecedor.

**Tabelas:**

KESTQDETALHE - Necessidade

KESTQDETALHEQTDE, KESTQDETALHEQTDELOTE, KESTQDETALHEQTDESERIE - Saldo de materiais da ordem de produção

KEMPENHOMP, KEMPENHOMPLOTE, KEMPENHOMPSERIE - Materiais empenhado para a ordem de produção.

KMOVESTOQUE, KMOVESTOQUELOTE, KMOVESTOQUESERIE - Registro de todas as movimentações geradas pelo sistema de produção, o campo TIPOMOV = 'E' identifica os registros de empenho.

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
