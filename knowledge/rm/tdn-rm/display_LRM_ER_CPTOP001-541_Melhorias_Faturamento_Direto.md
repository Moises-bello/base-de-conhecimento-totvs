---
content_hash: c7e3ec08df1d5c5dce4f6ae7bb578041369cef35157a36c70eded5f86a03de0e
fetched_at: '2026-06-29T00:08:18.886192+00:00'
page_id: '266972966'
product: rm
source: tdn-rm
title: ER_CPTOP001-541_Melhorias_Faturamento_Direto
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPTOP001-541_Melhorias_Faturamento_Direto
version: 147
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | CPTOP001 | **IRM1** |  |
| **Requisito1** | CPTOP001-541 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### 

### Objetivo

Atender a demanda de clientes e praticas comuns do mercado para atender contratos de serviços com cláusula de faturamento direto, podendo ser necessário a utilização de pedidos onde estes passarão por fluxo de aprovação ou sem a necessidade dos pedidos, quando os materiais  são lançados diretamente a partir da nota fiscal,  gerando o Pedido de Faturamento Direto diretamente do módulo de engenharia (TOP). Desta forma, é possível realizar  a apropriação diretamente nas tarefas, aplicando os valores e percentuais correspondentes a cada tarefa.

# CADASTRO DE FATURAMENTO DIRETO

O cadastro de faturamento direto se faz necessário para atender as diversas realidades do mercado:

* Alguns clientes recebem diretamente o orçamento, já com a indicação de onde comprar e o preço; Neste caso, conforme processo do cliente, poderá ser necessário criar o pedido para disparar o processo de compra ou até mesmo, passar por processo de aprovação do pedido.
* Há situações onde o material é entregue na obra, junto da Nota Fiscal e o cadastro é feito através desta, no módulo de suprimentos ou na forma de recebimento de pedido, gerado pelo módulo de engenharia (TOP).

O cadastro do faturamento direto é feito através do anexo "Faturamento Direto", disponível no módulo de contrato. Tal cadastro, utiliza-se da mesma estrutura do cadastro de Pedido de Material Extra, porem possui um identificador que distingue o que é Pedido de Material Extra do que é Faturamento Direto.

Para o Faturamento Direto, o usuário irá selecionar qual o fornecedor em uma lista; os fornecedores serão exibidos para seleção:

* Apenas os clientes e fornecedores associados ao contrato selecionado, caso o contrato em questão possua associação de clientes / fornecedores para Faturamento Direto.
* Serão exibidos todos os Clientes / Fornecedores existentes no sistema, caso o contrato não possua o “Cadastro de clientes/fornecedores para Faturamento Direto” definido.

O campo "Tipo de Movimento" é apenas para leitura, não permitindo que o usuário altere seu valor para cada cadastro. Seu valor, será definido conforme definido nos "Parâmetros de projeto" do TOP.

* Caso não esteja definido o "Tipo de Movimento" necessário nos "Parâmetros de projeto", será exibida uma mensagem de erro, informando que é necessário realizar tal configuração.

### Itens do Faturamento Direto:

Para garantir o controle do contrato, algumas validações serão realizadas:

* Ao incluir um item, será verificado o saldo do contrato, os valores de itens incluídos em "Faturamentos Diretos" que ainda não tenham sido considerados e os valores de Movimentos associadas ao contrato, que também não tenham sido consideradas na Liberação do período. Tal validação é realizada para que não seja possível, através de um Faturamento Direto, ultrapassar os valores do contrato (exemplo A).
  + Esta consistência será realizada também ao executar os processos de Geração do movimento (do Faturamento Direto) e na Liberação dos Períodos.
  + A validação irá respeitar o parâmetro "Habilita Medição Acima de 100%" e não será realizada caso este parâmetro esteja marcado.
* Ao incluir um Item cujo produto possua "insumo", o campo "Preço Unit. Orçado" irá permitir alteração do valor, pois este pode ser diferente do preço cadastrado para o item no início no contrato e deve ser lançado o valor correto.
  + Verificar a busca de preço quando não possuir insumo e uso do parâmetro Integração > Suprimento / Faturamento > Pedido de Material Extra > "Permite alterar preço em Pedido Extra para produtos sem insumo.".
  + Verificar Fluig e processos de aprovação.
* Não será permitido excluir o movimento de um "Faturamento Direto", caso o valor de Faturamento Direto acumulado das liberações de período seja maior que o valor dos demais Pedidos (exemplo B).

As validações, serão realizadas para evitar situações semelhantes aos exemplos abaixo:

A -

Saldo do item no contrato: R$5.000,00

Faturamento Direto do item: R$2.000,00

Liberação: R$4.000,00 / Faturamento direto: R$500,00

Neste caso, o saldo ficaria em R$1000,00 porem teria ainda um valor de R$1.500,00 de Faturamento Direto a ser considerado, ultrapassando em R$500,00 o saldo do contrato para a próxima liberação.

B -

Saldo do item no contrato: R$1.000,00

Faturamento Direto do item já utilizado na liberação: R$500,00

A exclusão do movimento do Faturamento Direto apenas poderá ser realizada, se o somatório de todos os demais faturamentos diretos existentes for maior ou igual a R$500,00

# PARÂMETROS

O cadastro de Faturamento Direto terá tipos distintos de movimentos, "tipo de movimento para contratos a Pagar" e "tipo de movimento para contratos a Receber". Estes tipos de movimento serão carregados automaticamente ao se cadastrar o Faturamento direto, de acordo com o contrato em questão.

Para isto, existem dois novos campos no "Configurador", um para cada tipo de movimento:

* Tipo do movimento de Faturamento Direto para contratos do tipo "A pagar"
* Tipo do movimento de Faturamento Direto para contratos do tipo "A receber"

# CONTRATO

Para permitir que o usuário especifique quais são os fornecedores que poderão fornecer materiais e ser utilizados para a criação de um Faturamento Direto, no cadastro do contrato é possível associar e restringir a utilização de tais fornecedores. Esta restrição pode ser necessária para casos em que o usuário que irá criar o Faturamento direto é diferente do usuário que cria o contrato.

Para este controle, é preciso incluir quais são os fornecedores permitidos, através da aba “Cadastro de clientes/fornecedores para Faturamento Direto” no Cadastro do Contrato.

Caso não seja cadastrado nenhum fornecedor para o contrato, o faturamento direto permitirá a inclusão para qualquer fornecedor existente no sistema.

# LIBERAÇÃO DO PERÍODO

Os faturamentos diretos criados para o contrato serão considerados no momento da liberação dos períodos.

Ao gerar o movimento, os faturamentos diretos serão considerados em campos específicos no rateio de tarefas,  para a criação do movimento, considerando a dedução por item, para possibilitar que o cálculo do valor do faturamento seja flexível, permitindo que cada construtura / empreiteira defina qual a forma correta de considerar os Faturamentos Diretos.

Ainda na liberação, será possível definir qual o percentual / valor deverá ser considerado, possibilitando que o usuário divida os valores dos Faturamentos Diretos em mais de uma liberação.

O valor do item será considerado o valor total da liberação.

O valor do Faturamento Direto será enviado no campo Dedução do item (campo do Item do Movimento).

O valor no rateio de tarefas terá o desconto do Faturamento Direto por Tarefa, tornando a cargo do usuário alterar a fórmula de cálculo de rateio para considerar esta dedução.

Formula:

KQT \* KPU - TABITM('VALDEDUCAO','V')

# APROPRIAÇÃO

No cronograma apropriado serão considerados as deduções de Faturamento Direto que já foram deduzidas no Rateio de Tarefas.

Para os Faturamentos Diretos realizados diretamente pelo módulo de Suprimentos, será realizado o rateio proporcional, caso o usuário não informe a tarefa.

# CONTRA ESCOPO

Não faz parte do escopo da tarefa tratamentos específicos para atender a integração com Protheus e nem a realização de testes para avaliar a funcionalidade em ambiente integrado com Protheus.

O Backup de projetos não irá contemplar os faturamentos diretos cadastrados.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
