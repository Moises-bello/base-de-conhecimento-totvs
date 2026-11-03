---
content_hash: b8d853a4dc2694bed521ce7994236a39c4a0dc504123665db7c76e90922818ed
fetched_at: '2026-06-29T00:08:30.549925+00:00'
page_id: '272696881'
product: rm
source: tdn-rm
title: Baixa de matéria prima (com terceiros e normal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272696881
version: 8
---

# BAIXA COM TERCEIROS E NORMAL / FACTOR - ESTOQUE DE TERCEIROS

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| **Segmento Executor:** | Construção e Projetos. | | |
| **Módulo:** | Gestão Planejamento e Controle da Produção | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Baixa de Matéria Prima | *Informe o nome técnico da rotina.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Informe a(s) rotina(s) envolvidas*.* | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | | | |
| **Chamado/Ticket:** | Não se aplica. | | |
| **Requisito/Story/Issue:** | MATESTCNTFTOF01-61*.* | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

### Objetivo

 

Permitir ao usuário a realização da baixa de estoque de materiais de terceiros e próprio durante o processo de produção.

### Definição da Regra de Negócio

A baixa de materiais busca do local de estoque o material necessário para produção de uma ou mais ordens e transfere esses recursos para o chão de fábrica. Nesse momento os materiais não aparecem mais listado na ficha física financeira ou locais de estoque.

Se estiver trabalhando com empenho são os materiais empenhados que vão estar disponíveis para baixa, o acesso aos locais de estoque quando se trabalha com empenho ocorre depois que a atividade está concluída.

O processo de baixa de materiais consiste em calcular a necessidade de matéria prima necessária a ordem de produção, consultar os materiais disponíveis no estoque e se estiver utilizando empenho o local parametrizado de empenho.

É exibida uma lista de materiais que deve ser baixado, sua necessidade com informações dos materiais a quantidade necessária e a quantidade a baixar.

Se estiver trabalhando com estoque de terceiros cada fornecedor exibe seu material em uma linha separada, os fornecedores que podem aparecer na lista são definidos na visão da ordem ao configurar a lista de fornecedores da ordem de produção.

Ao editar o registro pode-se visualizar a quantidade do material em cada local de estoque assim como a sugestão do que baixar.

Os materiais em seus locais podem ser facilmente selecionados e movidos entre “Disponíveis” e “Associados”, na edição também seleciona-se os lotes e séries.

O cliente pode baixar parte do material de estoque próprio e parte do estoque de terceiros.

Na página de críticas é exibido informações relacionada ao produto a ser baixada que não está em conformidade.

Ao confirmar a baixa os materiais serão transferidos do local de estoque e(ou) empenho para o chão de fábrica e as quantidades nos locais de origem serão deduzidas.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Baixa estoque de matéria prima para a ordem selecionada | Alteração | Produção \ Ordem de Produção \ Baixa estoque de matéria prima para a ordem selecionada. | Efetua a baixa de estoque de matéria prima no no TOTVS Gestão de Estoque, Compras e Faturamento, considerando a quantidade de cada item da ordem selecionada. A ordem deve estar com o status igual a **Aguardando recursos** ou **Pronta para Iniciar**. |
| Baixa estoque de matéria prima para todas as ordens | Envolvida | Produção \ Ordem de Produção \ Baixa estoque de matéria prima para todas as ordens | Efetua a baixa de estoque de matéria prima no TOTVS Gestão de Estoque, Compras e Faturamento, considerando a quantidade de cada item de todas as ordens cadastradas. As ordens devem estar com o status igual a **Aguardando recursos** ou **Pronta para Iniciar.** |

**Visibilidade dos Materiais**

A baixa tem acesso aos locais configurados (Materiais, Materiais de Terceiros, Subproduto e Semiacabados) e se estiver utilizando empenho os locais de empenho (próprio e terceiros).

Do local de empenho a visibilidade dos materiais é limitada ao que foi solicitado e reservado para a ordem de produção.

Cada um desses locais tem um local padrão, o local padrão é preferencial aos demais locais ao determinar a sugestão dos materiais que serão empenhados.

Os locais reservados são exclusivos na visibilidade dos materiais, a baixa não visualiza locais de empenho além do que a ordem executora da baixa reservou no empenho. A baixa não visualiza locais de perda de materiais (Próprio e Terceiros)

A sugestão de matérias pode variar conforme parametrização do usuário em relação a preferência de uso de material próprio, terceiros ou ambos.

**Baixa de Materiais**

Caso nos parâmetros **Gerais** esteja parametrizado para Controlar Estoque de Terceiros, na tela Baixa de Materiais, em Locais de Estoque/Lotes Disponíveis deverão ser apresentados os produtos de terceiros existentes nos locais de estoque em que foram definidos o Estoque de Terceiros do TOTVS Gestão de Estoque, Compras e Faturamento (Nucleus) e que fazem parte da estrutura a ser produzida.

A exibição dos produtos de terceiros deverá ser por cliente/fornecedor dos produtos e deverão ser exibidas suas respectivas informações de Filial, Local de Estoque, Número do Lote e Saldo Físico.

Na tela Baixa de Materiais, em Locais de Estoque/Lotes Associados, nos casos em que forem associados produtos de terceiros,  a exibição dos produtos deverá ser por cliente/fornecedor dos produtos e deverão ser exibidas suas respectivas informações de Filial, Local de Estoque, Custo e Custo Total.

Quando o produto for do estoque próprio, a informação do cliente/fornecedor deverá ser apresentada em branco.

Após associação dos produtos disponíveis, para os produtos de terceiros deverá ser gerada uma movimentação para cada cliente/fornecedor do produto, do tipo de movimento que foi definido no parâmetro **Movimentação de Estoque | Baixa de Matéria Prima de Terceiros**.

 As demais funcionalidades dessa tela permanecem inalteradas.

**Restrição / Ponto de Atenção:**

* Ao efetivar a baixa de terceiro não será considerado o saldo de estoque reservado (reservados pelo planejamento, reserva de OP e reserva do TOTVS Gestão de Estoque, Compras e Faturamento).

**Parâmetros que alteram o comportamento da baixa de materiais**

Parâmetros do RMFactor influenciam a forma de trabalho da baixa de materiais, alguns que afetam o comportamento estão listados abaixo:

 **Página Gerais**

**·** **Empenha Matéria-prima**

Quando se utiliza empenho de materiais a baixa considera esses materiais com preferência aos demais e a sugestão para baixa é de acordo com o material empenhado. 

**·** **Utiliza Estoque de Terceiros**

Indica que o sistema está trabalhando com estoque de terceiros, no entanto a ordem de produção precisa definir fornecedores para que tenha sugestão de estoque de terceiros do contrário é como se estive-se trabalhado apenas com estoque próprio.

**·** **Consistir baixa de matéria prima**

Indica o momento em que deve ser consistido a necessidade de baixa para a ordem de produção, ver mais detalhes na parametrização.

**·** **Baixa Material Consumido no Apontamento**

Ao marcar este parâmetro, o RM Factor irá considerar apenas as quantidades de matéria-prima consumidas no apontamento, desconsiderando o que foi previsto. Só será permitido marcá-lo se a parametrização “Consistir Baixa de matéria prima” estiver “Não realizar consistência” ou “Antes de dar entrada na produção”.

**·** **Carrega Lotes mais antigos na escolha do Lote**

Quando este parâmetro estiver marcado, o RM Factor irá selecionar os lotes de materiais mais antigos – baseando-se na data de validade – para serem baixados. Os lotes disponíveis para seleção serão os que se encontram no local de estoque selecionado na baixa, que possuem saldo positivo e que não estejam bloqueados. Caso o lote não tenha data de validade, o sistema irá ordená-los pelo identificador do lote.

Caso esta opção esteja desmarcada, o sistema efetuará está seleção pelo Identificador do Lote.

 

**Página Apontamento**

·         **Default: Calcula Prop. Qtde. de Material Consumido**

Esse parâmetro indica que no apontamento ao informar a quantidade apontada o sistema calcula a necessidade de materiais da estrutura para a quantidade informada e lança o consumo do material.

Quando está trabalhando com estoque de terceiros é habilitado uma nova regra que é aplicada tanto para o apontamento quanto na sugestão do material a ser empenhado e baixado:

**Regra de proporcionalização deve priorizar:**

**1.** **Estoque próprio**

Os materiais sugeridos para a ordem serão sempre do estoque próprio, faltando material do estoque próprio é sugerido material do estoque de terceiros (considerando apenas os terceiros configuradas na ordem)

**2.** **Estoque de terceiros**

Os materiais sugeridos para a ordem serão sempre do estoque de terceiros, faltando material do estoque de terceiros é sugerido material do estoque próprio.

**3.** **Estoque ambos**

Os materiais sugeridos para a ordem serão sempre do estoque próprio, faltando material do estoque próprio é sugerido material do estoque de terceiros (considerando apenas os terceiros configuradas na ordem).

A diferença ocorre para produtos controlados por lote onde é considerado a data de validade, tendo estoque próprio e de terceiros validos os lotes com validade mais próximas de vencer são utilizados primeiro independente da origem (próprio ou terceiros)

**Listagem dos serviços do que precisam ser revisado no Factor para atender à baixa de terceiros:**

* *Insere/Atualiza quantidade no Estoque Intermediário:**q***uando a matéria prima for de terceiro, ao salvar os dados na tabela KESTQDETALHEQTDE  deverão ser gravados os campos CodColCfo e CodCfo.
* *Busca dados da tabela KESTQDETALHEQTDE:*deverá ser acrescentado o retorno dos campos CodColCfo e CodCfo.
* *Consistências:* se produto pode ser movimento e quantidade negativa.
* *Busca de material consumido e Recupera Quantidade Prevista e Efetivada.*
* *Lote apontando e número de série apontado;*
* *Realiza Quebra de Matéria Prima*
* *Carrega produtos empenhados*
* *Carrega dataset da Baixa.*
* *Associa Saldo Local estoque lote:*o custo para terceiro deve ser o custo médio.
* *Busca números de séries*
* *Busca números de séries associados*
* *Salvar Baixa:*
  + *MontaListaMovimento e InclusaoMovimento;*
  + *Serviços de inclusão de movimento verificar os métodos  (SalvaDadosKMovEstoqueBaixaMaterial, SalvaDadosKEmpenhoMPBaixaMaterial, SalvaDadosEstIntermediario)*
  + *Serviço que salva os dados na tabela KMOVESTOQUE (SalvaDadosKMovEstoque).*

**Tabelas Utilizadas**

* KESTQDETALHEQTDE – Estoque Detalhe Quantidade.
* KMOVESTOQUE – Registro de Movimentação de Estoque.

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
| **Tabela** | KESTQDETALHEQTDE |
| **Campo** | CODCOLCFO |
| **Tipo** | DCODCOLIGADANULL |
| **Tamanho** | 2 |
| **Valor Inicial** | Nulo. |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Coligada do Fornecedor. |
| **Help de Campo** | Informar a coligada do fornecedor. Este campo será preenchido quando for material de terceiro. |

|  |  |
| --- | --- |
| **Tabela** | KESTQDETALHEQTDE |
| **Campo** | CODCFO |
| **Tipo** | VARCHAR |
| **Tamanho** | 25 |
| **Valor Inicial** | Nulo. |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Código do Fornecedor. |
| **Help de Campo** | Informar o código do fornecedor. Este campo será preenchido quando for material de terceiro. |

Permitir ao usuário a realização da baixa de estoque de materiais de terceiros e próprio durante o processo de produção.
