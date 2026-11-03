---
content_hash: 0e8dccf6f2ccc80335ed0476ce76a7cc7617ad1d5ab519df1381bc2e036cc64a
fetched_at: '2026-06-29T00:08:10.552750+00:00'
page_id: '240305479'
product: rm
source: tdn-rm
title: ER_CPMOV001-12_Melhoria_Utilizacao_Marca_Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPMOV001-12_Melhoria_Utilizacao_Marca_Produto
version: 174
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_CP\_MOV 2016/2017 | **IRM1** | CPMOV001-4 |
| **Requisito1** | CPMOV001-12 | **Subtarefa1** | CPMOV001-368 |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Permitir que o usuário possa cadastrar marcas para um determinando produto, e no momento da cotação ter a possibilidade de utilizar escolher/trocar a marca do produto.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de Marca | Criação | BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Mais \ Tabelas Auxiliares \ Marca | - |
| Parâmetros Gerais | Alteração | BackOffice \ Gestão de Estoque, Compras e Faturamento \ Ambiente \ Parâmetros \ Parâmetros Gerais \ Tabelas \ Marca | - |
| Produto | Envolvida | BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Produto | - |
| Cotação | Envolvida | BackOffice \ Gestão de Estoque, Compras e Faturamento \ Ambiente \ Parâmetros \ Gestão de Estoque, Compras e Faturamento \ Gestão de Compras \ Cotação | - |
| Parâmetros de Tipo de Movimento | Alteração | BackOffice \ Gestão de Estoque, Compras e Faturamento \ Parâmetros do Tipo de Movimento. |  |
| Movimento | Envolvida | BackOffice \ Gestão de Estoque, Compras e Faturamento \ Ambiente \ Parâmetros \ Gestão de Estoque, Compras e Faturamento \ Gestão de Compras \ Solicitação de Compras e Ordem de Compra | - |

### Cadastro de Marca

**Parâmetros**

Criar um novo item em **Parâmetros Gerais \ Tabelas** com o código \ nome **04.01.04.11 - Marca**. Nesta etapa devem ser criados os parâmetros:

* **Máscara:** campo para o usuário definir a máscara a ser aplicada no campo Código da Marca. Neste campo serão aplicados as seguintes regras:
  + Será permitido utilizar os caracteres "**#lLaAQ**" e como separadores os caracteres "**.,-:/**". Caso seja utilizado um carácter diferente destes, ele será considerado como um carácter vazio.
  + A máscara default será composta pelos caracteres "**#####**".
  + Este campo não poderá ser atualizado caso já exista algum registro cadastrado na base para a coligada logada.
  + Quando usar marca global, a mascará deverá ser a mesma para as coligadas configuradas como marca global.
* **Nome Marca:** campo para o usuário definir o nome da entidade que será exibida no sistema, similar ao Fabricante, Transportadora e Representante. O nome default deste campo será "**Marcas**".
* **Usa Marca Global:** campo para definir se o cadastro de Marca será Global. O valor default deste campo será "**marcado**". Ao salvar as definições para Tabela de Marca , caso a Coligada esteja  configurada para **Central de Compras** ou **Participante de Central de Compras** será exigido configurar a Marca como Global, ou seja, **Usa Marca Global** deverá ser marcado.

**Atenção:**ao habilitar a opção de **Usa Marca Global**, caso já exista algum registro cadastrado como marca global, não será permitido alterar a configuração.

****Parâmetros de**** **Cotação**

Ao configurar a Cotação como **Central de Compras** ou **Participante de central de compras** é obrigatório configurar a tabela de Marca para **Usar marca global** em **Parâmetros Gerais \ Tabelas \ Marca**.

**Cadastro de Marca**

Criar o cadastrado de Marca. Este cadastro ficará disponível no menu **Cadastros \ Mais \ Tabelas Auxiliares \ Marca**. Esta entidade deve respeitar as definições parametrizadas em **Parâmetros Gerais \ Tabelas \ Marca.**

As coligadas que estiverem usando marca global, poderão visualizar os seus registros em outras coligadas que usam marca global. Exemplo: Coligada 1 não usa marca global; Coligada 2 e Coligada 3 usam marca global. Ao abrir o cadastro de Marca na coligada 2 serão exibidos os registros cadastrados nas coligadas 2 e coligada 3. Ao abrir o cadastro de Marca na Coligada 1 serão exibidos somente os registros da Coligada 1, pois ela não trabalha com marca global.

**Cadastro de Produto**

Criar o campo Marca no cadastro de Produto. Este campo deve ser um lookup para a entidade Marca.

Este campo será considerado um default da marca e sempre que for alterado, deve-se alimentar a tabela de Anexo de Marcas do Produto, assim como é feito para o anexo Unidades de Medidas de um Produto.

Não será possível associar uma marca Inativa como default de um produto.

**Anexo de Produto**

Criar um anexo do cadastro de Produtos para que sejam vinculados marcas a um determinado Produto.

Não será possível Inativar uma marca configurada como a marca default do produto. Não será permitido excluir uma marca configurada como default do produto.

**Conversão de Produto Global**

Ao realizar o Processo de Conversão para Produto Global o novo Identificador do Produto será alterado para o Anexo de Marcas para que aquelas associadas a Coligada e Produto permaneça com as Marcas associadas.

**Cópia de Produto entre Coligadas**

Para o processo de Cópia de Produtos entre Coligadas as Marcas serão copiadas entre as Coligadas que utilizam Marca Global e Não Global, ou seja, as Marcas Associadas ao Produto serão incluídas\atualizadas da Coligada Origem para Destino, tal como, o Default utilizado pela Produto.

A cópia de Produto da Coligada que utilizar Marca Global para Não Global o processo irá buscar a Marca correspondente de acordo com o Código da Origem para o Destino. Para Marca Global entre entre Coligadas Globais não será necessário realizar a busca sendo a Marca idêntica entre Coligadas.

**Cópia de Produto Global para Não Global**

Serão realizadas as cópias do Anexo de Marcas relacionadas ao Produto  da Coligada Global **apenas** para a Coligada Não Global.

**Cópia de Produto Não Global para Global**

Será realizada a cópia de do Anexo de Marcas relacionadas ao Produto da Coligada Não Global para a **todas** as Coligadas Globais.

**Movimento**

**Parâmetro por Tipo de Movimento**

Será criado parâmetro por tipo de movimento para o campo Marca no Item de Movimento. Este parâmetro terá as seguintes opções:

* **Não Edita:**não usa marca no item de movimento.
* **Edita:**usa marca no item de movimento. Campo não obrigatório.
* **Edita Obrigatoriamente:**usa marca no item de movimento. Informação obrigatória.
* **Mostra:** exibe a marca no item de movimento. Neste caso será considerado como valor default a marca definida para o produto no cadastro de Produtos.

Este parâmetro deve ser criado na tabela Tipos de Movimento - Complemento (TITMTMV) e ficará disponível na Etapa Item - Identificação 1/2.

**Item de Movimento**

Será criado na tabela de Item de Movimento (TITMMOV) o campo para armazenar a marca do produto solicitado (CODCOLMARCA, IDMARCA). Este campo deverá respeitar a parametrização realizada por tipo de movimento, conforme detalhado acima.

Serão filtrados apenas as marcas definidas no anexo de marcas do produto.

O comportamento de Default para o campo Marca do Item será aplicado nos seguintes processos:

1. Inclusão de Movimento: caso o parâmetro por Tipo de Movimento for diferente de Não Edita, deve-se buscar a marca definida no cadastro de Produto.
2. Faturamento de Movimento: caso o parâmetro por Tipo de Movimento for diferente de Não Edita, deve-se copiar a informação de marca do item de movimento origem.  
   2.1 - Caso o Tipo de movimento esteja parametrizado para agrupar quantidades de itens repetidos, será adotado o comportamento já existente no sistema, ou seja, o primeiro item a ser agrupado será utilizado como base. Sendo assim a todos os itens serão agrupados e a marca que prevalecerá será a do primeiro item.
3. Cópia de Movimento a partir de Outro
4. Cópia por Referência
5. Cópia de Itens não Cotados

Não será possível informar uma marca inativa na inclusão/ edição de um item de movimento.

### Substituição de Marca na Cotação

Será criado um parâmetro de cotação para que o usuário possa definir se irá trabalhar com marca de produtos na cotação. Quando este parâmetro estiver habilitado, existirão opções na cotação para que o usuário possa escolher/trocar a marca do produto, seja no orçamento ou na negociação, de acordo com a permissão de perfil do usuário. Haverá também uma opção para o usuário definir se o fornecedor poderá escolher/trocar a marca do produto, nos casos em que a cotação for exportada para o fornecedor preencher os dados, seja de orçamento ou negociação.

Quando este parâmetro estiver desabilitado, as opções não serão exibidas na cotação.

Não será possível informar uma marca inativa na inclusão/ edição de orçamento / negociação.

**Substituição por Fornecedor**

Quando o sistema for configurado para **Usar Marca de Produto na Cotação,** nas janelas de **Registrar Orçamento e Registrar Negociação**, pasta Produtos no grid de itens da cotação ficarão disponíveis os campos **Marca Solicitada,****Marca Orçada** e **Marca Negociada.**  A **Marca Solicitada** é a informação gravada na tabela de Item de Movimento, **Marca Orçada** e**Marca Negociada**serão um lookup para o cadastro de Marca e receberão a informação de marca informada no item de Solicitação de Compras. Estes campos deverão ser exibidos no grid imediatamente após os campos **Cod. Produto** e **Descrição Produto**. Os demais campos já existentes no grid de itens da cotação não mudarão de comportamento.

 Estes campos terão o seguinte comportamento:

* **Marca Solicitada:** somente visualização, ou seja, não permite edição. Disponível nas janelas de Registro de Orçamento e Registro de Negociação.
* **Marca Orçada:** disponível nas janelas de Registro de Orçamento e Registro de Negociação. Na janela de Registrar Orçamento permitirá edição somente quando o perfil do usuário possuir permissão de **Permite trocar marca dos produtos na cotação.** Caso o comprador deseje escolher/trocar a marca do produto ele deverá editar este campo, informando a nova marca. Na janela de Registrar Negociação este campo não poderá ser editado, ou seja, será apenas visualização.
* **Marca Negociada:** ficará disponível somente na janela de Registrar Negociação e permitirá edição quando o perfil do usuário possuir permissão para **Permite trocar marca dos produtos na cotação.** Caso o comprador deseje escolher/trocar a marca do produto ele deverá editar este campo, informando a nova marca.

Ao clicar nestes campos, serão exibidas as marcas dos produtos do item selecionado, que foram previamente cadastradas no anexo Marcas do Produto (cadastro de Produto).

Para termos registro da troca da marca, será criado o campo **Marca do Produto Orçado** (CODCOLMARCAORC, IDMARCAORC) e outro campo para gravar a **Marca do Produto Negociado** (CODCOLMARCANEG, IDMARCANEG) na tabela Itens de Orçamento (TCITMORCAMENTO).

 A substituição terá o seguinte comportamento:

1. No registro de orçamento, após alterar a marca do produto, será feita a substituição do item de cotação. Para isso, o identificador da marca do produto solicitado deverá ser gravado nos campos **Marca do Produto Orçado** e **Marca do Produto Negociado** do fornecedor que está em edição. Os demais fornecedores continuarão com a marca do produto original, a não ser que o processo de alterar marca seja realizado nos outros fornecedores. O campo **Marca Solicitada** deverá manter o valor gravado anteriormente.
2. No registro de negociação, após selecionar a nova marca, será feita a alteração do item de cotação. Para isso, o identificador da marca alterada deverá ser gravado no campo **Marca do Produto Negociado** do fornecedor que está em edição. Os demais fornecedores continuarão com o produto original, a não ser que o processo de alteração de marca seja realizado nos outros fornecedores. Os campos **Marca Solicitada** e ****Marca Produto Orçado****deverão manter o valor gravado anteriormente.

Para realizar a troca da marca nos campos **Marca Orçada** e **Marca Negociada** o usuário deve possuir permissão por perfil para trocar marca. Maiores detalhes consulte o item Segurança abaixo.

**Wizard de Inclusão de Cotação**

Na inclusão de uma nova cotação será utilizada a informação da marca na solicitação de compras. A **Marca Solicitada** é a informação gravada na tabela de Item de Movimento e será copiada para os campos **Marca Orçada** e**Marca Negociada**. Quando o campo o código da marca do item da solicitação estiver nulo, ou seja, não tenha sido informado no item de movimento, será considerado a marca default informada no cadastro de Produto.

A **Marca Solicitada** será exibida no Wizard de Inclusão apenas se a Cotação for configurada para **Usar Marca de Produto na Cotação.**

**Agrupamento de Itens de Orçamento**

Caso a cotação esteja trabalhando com agrupamento de itens iguais e utiliza Marca na Cotação os Itens de Orçamento não serão agrupados.

### Segurança

Será criada a seguinte permissão de perfil:

* **Permite trocar marca dos produtos na cotação:** essa permissão servirá para definir se o usuário pode fazer a troca de marca de produtos na cotação. Quando não estiver habilitada, não será exibido na cotação o botão para trocar marca do produto na cotação.

### Portal

Não faz parte do escopo dessa funcionalidade a troca de marca de produtos pelo portal, mas será feita análise para liberar essa funcionalidade na revitalização do portal.

Para envio de orçamento para WEB, será exportado a marca do produto que estiver gravado na Solicitação de Compras.

### **Geração de Ordem de Compra**

Na geração da ordem de compra a partir da cotação, deverá ser observado se houve a troca da marca do produto na cotação. Caso isso tenha ocorrido, a marca do item da ordem de compra deverá corresponder à marca que foi negociada na cotação. Os demais campos continuarão com o mesmo comportamento. Conforme mencionado acima haverá um campo especifico no item de movimento para armazenar a marca do item de movimento.

* Na Geração da ordem de compra com Quebras: Como a quebra é feita por movimento e não por itens, e nesse caso não será necessário ajustes para adequar a marca na geração de pedidos.
* Na Geração da ordem de compra com inclusão de itens em ordem de compra existente: Esta rotina não agrupa os itens iguais no pedido, mesmo que esta esteje parametrizada para agrupar itens iguais. Neste caso a inclusão do campo marca não será afetada, e não necessitará de alteração.
* Na Geração da ordem de compra, onde o movimento esteja parametrizado para agrupar: Será adotado o comportamento já existente no sistema, ou seja, o primeiro item a ser agrupado será utilizado como base. Sendo assim a todos os itens serão agrupados e a marca que prevalecerá será a do primeiro item. Não será feita nenhuma alteração neste processo.

### Relacionamento de Movimentos

Não haverá impacto no relacionamento entre os movimentos e itens de movimento da ordem de compra e da solicitação de compra, pois no relacionamento são consideradas apenas as informações de IDMOV e NSEQITMMOV dos movimentos e itens de movimento.

### Estorno de Item não Recebido da Ordem de Compra

Não haverá impacto no estorno de itens de Ordem de Compra gerada a partir de cotação, pois no relacionamento são consideradas apenas as informações de IDMOV e NSEQITMMOV dos movimentos e itens de movimento.

### Histórico de Substituição na Cotação

Não faz parte do escopo dessa funcionalidade o histórico de alteração de marca de produtos na cotação, mas será feita análise para liberar essa funcionalidade junto com a funcionalidade de histórico de negociação da cotação.

**Cotação WEB e Julgamento da Melhor Oferta**

Esta fora de escopo nesta história tratar a cotação web e impacto no julgamento da melhor oferta no quadro comparativo. Ambos será tratado quando estivermos atuando neles durante o projeto UX. Vamos criar uma historia para eles no backlog para ser tratado.

**Tabelas Utilizadas**

* TPAR – Parâmetros Gerais
* TITMTMV – Tipos de Movimento - Complemento
* TCITMORCAMENTO – Itens de Orçamento
* TITMMOV– Item de Movimento
* TMARCA – Tabela de Marcas
* TPRODUTODEF – Dados dos Produtos Globais por Coligada
* TPRODUTODEFMARCA – Tabela de Produto x Marcas
* TCPARAMETROS – Parâmetros da Cotação

### **Restrições e Pontos de Atenção**

* Não será considerado na Cotação Web e impacto no Julgamento da Melhor Oferta no quadro comparativo.
* Não será implementado estoque de Produtos por Marca.
* Não será implementado o vínculo entre Marca x Fornecedor.
* Não será implementado Marca na Importação e Exportação de Movimentos.

**Fabricantes:**

Neste tópico serão listados todos os pontos do sistema que utiliza dados de Fabricantes. São eles:

* + Na Cotação o código do fabricante é utilizado na grid de Produtos em Registro de Orçamento e Negociação, quando o parâmetro Código do Produto Utilizado na Cotação for igual a Número do Fabricante (Parâmetros >> Cotação >> Definições Gerais 3/5).
  + A descrição do fabricante é exibida ao Gerar Dados do QCP para Planilha.
  + Lookup Produto no Assistente de Inclusão da Cotação e lookup de produto no processo de Inserir Itens na Cotação.
  + Cadastro de Produto possui a informação de Código do Fabricante e Número do Produto no Fabricante.
  + Cadastro de Lotes de Produto possui a informação de Código do Fabricante e Número do Lote no Fabricante.
  + Lookup de Produto da rotina Consultar Saldos e Custos, para pesquisar o produto.
  + Processo de Atualizar Múltiplos Registros do cadastro de Produto pelo Código do Fabricante.
  + Atualização de produto de grade numerada pelo produto base, código do fabricante é um dos campos a atualizar.
  + Consistências do Código do Produto que verifica se o Número do Produto no Fabricante é único. Esta consistência é aplicada quando existe Código do Fabricante e Número do Fabricante informado no cadastro do Produto E é último nível OU tamanho do Código do produto é igual ao tamanho da máscara OU Opção de Máscara é diferente de Controla Níveis de Máscara.
  + Ao incluir/alterar Produto por Grade a informação de código do fabricante é considerada nos dados que são carregados do produto.
  + Ao incluir Produto Substituto/Similar pode-se pesquisar registros pelo Código do Fabricante e/ou Número do Fabricante.
  + Exportação de produto (gerador de saídas)
  + Exportação de lote de produtos (gerador de saídas).
  + Visão de Item de Movimento (anexos e edição de movimento grid de Itens).
  + O código do fabricante é copiado para os movimentos de destino ao executar os processos de Cópia de Movimento, Faturamento, Faturamento Medição de Contrato.
  + Ao selecionar um Produto Substituto/Similar no movimento o código do fabricante é retornado nos dados do produto.
  + No CTe para preencher as informações de dados de ICMS UF Fim (PreencheDadosICMSUFFim) - CT-e\_Notas\_Tecnicas\_2015\_003\_e\_004 - , são selecionados dados dos itens de movimento e é recuperado o Código do Fabricante. Não encontrei no código nenhum tratamento especifico para o Código do Fabricante no CTe.
  + Na Nota Fiscal Eletrônica (NFe) quando o Movimento é de Importação (CFOP 3.XX) são selecionados os dados de importação e a informação de código do fabricante é um dos dados selecionados para preencher informações no objetos "nfeDet.prod.DI" e também "TNFeInfNFeDetProdDIAdi.cFabricante".

**Integração com PROTHEUS:**

O BackOffice RM é integrado aos seguintes módulos do Protheus: Manutenção de Ativos, Gestão de Frotas e PDV Protheus (SigaLOJA). A utilização de marca não será considerada neste momento, pois os processos que são utilizados pelas integrações não serão impactados.

## Dicionário de Dados

**Arquivo ou Código do Script:** NU.2016.06\_08 

**Atualizar a tabela de Parâmetros Gerais(TPAR) com os seguintes campos:** 

|  |  |
| --- | --- |
| **Campo** | MASCMARCA |
| **Tipo** | VARCHAR |
| **Tamanho** | 15 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Descrição** | Máscara do Código da Marca |
| **Help de Campo** | Informar qual a máscara será aplicada ao campo o código da marca. |

|  |  |
| --- | --- |
| **Campo** | NOMEMARCA |
| **Tipo** | VARCHAR |
| **Tamanho** | 25 |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Nome da Tabela Marca. |
| **Help de Campo** | Informar qual será o nome da tabela Marca. |

|  |  |
| --- | --- |
| **Campo** | USAMARCAGLOBAL |
| **Tipo** | SMALLINT |
| **Tamanho** | 2 |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Usa Marca Global. |
| **Help de Campo** | Informar ser utilizará o cadastro de marca como global. |

**Arquivo ou Código do Script:** NU.2016.06\_07

**Criar tabela de marcas:**

|  |  |
| --- | --- |
| **Nome Tabela** | **TMARCA - Tabela de Marcas** |
| **Chave Primária** | IDMARCA, CODCOLIGADA |

|  |  |
| --- | --- |
| **Campo** | CODCOLIGADA |
| **Tipo** | DCODCOLIGADA |
| **Tamanho** | 2 |
| **Mandatório** | Sim ( x ) Não (  ) |
| **Descrição** | Código da Coligada |

|  |  |
| --- | --- |
| **Campo** | CODMARCA |
| **Tipo** | DTCODIGO |
| **Tamanho** | 15 |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Código da marca. |
| **Help de Campo** | Campo não poderá ser editado pelo usuário e será gerado automaticamente. |

|  |  |
| --- | --- |
| **Campo** | DESCMARCA |
| **Tipo** | DTDESCRICAO |
| **Tamanho** | 100 |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Descrição da marca |
| **Help de Campo** | Informar a descrição da marca.Campo poderá ser alterado pelo usuário. |

**Arquivo ou Código do Script:** NU.2016.06\_06; NU.2016.08\_07; NU.2016.08\_08; NU.2016.08\_15

**Atualizar a tabela de Produto para fazer o vinculo com a Marca:**

|  |  |
| --- | --- |
| **Tabela** | TPRODUTODEF |
| **Campo** | CODCOLMARCA |
| **Tipo** | DCODCOLIGADANULL |
| **Tamanho** | 4 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Descrição** | Coligada da Marca Default do Produto |
| **Help de Campo** | Informar o código coligada da marca associado ao Produto. |

|  |  |
| --- | --- |
| **Tabela** | TPRODUTODEF |
| **Campo** | IDMARCA |
| **Tipo** | DINTEGER |
| **Tamanho** | 4 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Descrição** | Marca Default do Produto |
| **Help de Campo** | Informar o código do marca associado ao Produto. |

|  |  |
| --- | --- |
| **Tabela** | TPRODUTODEF |
| **Campo** | INATIVO |
| **Tipo** | smallint |
| **Tamanho** | 2 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Valor Default** | 0 - desmarcado. |
| **Descrição** | Marca de Produto Inativa |
| **Help de Campo** | Informar que a Marca de Produto está Inativa. |

**Arquivo ou Código do Script:** NU.2016.07\_01

**Criar a tabela de Produto x Marcas:**

|  |  |
| --- | --- |
| **Nome Tabela** | **TPRODUTODEFMARCA - Tabela de Produto x Marcas** |
| **Chave Primária** | CODCOLIGADA,IDPRD,CODCOLMARCA,IDMARCA |
| **FK com TPRODUTODEF** | TPRODUTODEFMARCA.CODCOLIGADA, TPRODUTODEFMARCA.IDPRD |
| **FK com TMARCA** | TPRODUTODEFMARCA.CODCOLMARCA, TPRODUTODEFMARCA.IDMARCA |

|  |  |
| --- | --- |
| **Campo** | CODCOLIGADA |
| **Tipo** | DCODCOLIGADA |
| **Tamanho** | 2 |
| **Mandatório** | Sim ( x ) Não (  ) |
| **Descrição** | Código da Coligada |

|  |  |
| --- | --- |
| **Campo** | IDPRD |
| **Tipo** | int |
| **Tamanho** | 4 |
| **Mandatório** | Sim ( x ) Não (  ) |
| **Descrição** | Identificador do Produto |
| **Help de Campo** | Identificador do Produto. Campo atualizado conforme informação do usuário no anexo. |

|  |  |
| --- | --- |
| **Campo** | CODCOLMARCA |
| **Tipo** | DCODCOLIGADA |
| **Tamanho** | 2 |
| **Mandatório** | Sim ( x ) Não (  ) |
| **Descrição** | Código coligada da marca |
| **Help de Campo** | Código coligada da marca que será associada ao produto. |

|  |  |
| --- | --- |
| **Campo** | IDMARCA |
| **Tipo** | DINTEGER |
| **Tamanho** | 4 |
| **Mandatório** | Sim ( x ) Não (  ) |
| **Descrição** | Código da marca |
| **Help de Campo** | Selecionar o código da marca que será associada ao produto. |

**Arquivo ou Código do Script:** NU.2016.08\_01

**Atualizar a tabela de parâmetros de item de movimento:**

|  |  |
| --- | --- |
| **Tabela** | TITMTMV |
| **Campo** | EDITAMARCA |
| **Tipo** | varchar |
| **Tamanho** | 1 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Valor Default** | N |
| **Descrição** | Edita marca de produto. |
| **Help de Campo** | Informe qual será o comportamento do campo Marca no item de movimento.  As opções do campo são: Não Edita (valor default), Edita, Mostra e Edita Obrigatoriamente. |

**Arquivo ou Código do Script:** NU.2016.08\_06

**Atualizar a tabela de Item de Movimento:**

|  |  |
| --- | --- |
| **Tabela** | TITMMOV |
| **Campo** | CODCOLMARCA |
| **Tipo** | DCODCOLIGADA |
| **Tamanho** | 2 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Descrição** | Coligada da marca do item de movimento |
| **Help de Campo** | Informe qual será a coligada da marca associado ao item de movimento. |

|  |  |
| --- | --- |
| **Tabela** | TITMMOV |
| **Campo** | IDMARCA |
| **Tipo** | DINTEGER |
| **Tamanho** | 4 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Descrição** | Marca do item de movimento. |
| **Help de Campo** | Informe qual será a marca associado ao item de movimento. |

**Arquivo ou Código do Script:** NU.2016.08\_04; NU.2016.08\_09

**Atualizar a tabela de parâmetros da cotação:**

|  |  |
| --- | --- |
| **Tabela** | TCPARAMETROS |
| **Campo** | USAMARCA |
| **Tipo** | smallint |
| **Tamanho** | 2 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Valor Default** | 0 - Desmarcado. |
| **Descrição** | Usa Marca de Produto na Cotação. |
| **Help de Campo** | Indica que será possível utilizar Marca na cotação. |

**Arquivo ou Código do Script:** NU.2016.08\_05; NU.2016.08\_11

**Atualizar a tabela de itens de orçamento:**

|  |  |
| --- | --- |
| **Tabela** | TCITMORCAMENTO |
| **Campo** | CODCOLMARCAORC |
| **Tipo** | smallint |
| **Tamanho** | 2 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Valor Default** | N |
| **Descrição** | Coligada da Marca Orçada. |
| **Help de Campo** | Marca orçada na cotação. |

|  |  |
| --- | --- |
| **Tabela** | TCITMORCAMENTO |
| **Campo** | IDMARCAORC |
| **Tipo** | DINTEGER |
| **Tamanho** | 4 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Valor Default** | N |
| **Descrição** | Identificador da Marca Orçada. |
| **Help de Campo** | Marca orçada na cotação. |

|  |  |
| --- | --- |
| **Tabela** | TCITMORCAMENTO |
| **Campo** | CODCOLMARCANEG |
| **Tipo** | smallint |
| **Tamanho** | 2 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Valor Default** | N |
| **Descrição** | Coligada da Marca Negociada. |
| **Help de Campo** | Marca negociada na cotação. |

|  |  |
| --- | --- |
| **Tabela** | TCITMORCAMENTO |
| **Campo** | IDMARCANEG |
| **Tipo** | DINTEGER |
| **Tamanho** | 4 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Valor Default** | N |
| **Descrição** | Identificador da Marca Negociada. |
| **Help de Campo** | Marca negociada na cotação. |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
