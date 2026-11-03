---
content_hash: af85bae755dee11290b74d426173180cb2201a545d6d9c5d7a071c44e1dfd480
fetched_at: '2026-06-29T00:08:16.881709+00:00'
page_id: '248581614'
product: rm
source: tdn-rm
title: ER_CPMOV001-12_Melhoria_Utilizacao_Marca_Produto_Fase2
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPMOV001-12_Melhoria_Utilizacao_Marca_Produto_Fase2
version: 140
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
| Copiar Marca entre Coligadas | Inclusão | BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Mais \ Tabelas Auxiliares \ Marca \ Processos \ Copiar Marca entre Coligadas. |  |
| Marca | Envolvida | BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Mais \ Tabelas Auxiliares \ Marca. |  |
| Cotação | Envolvida | BackOffice \ Gestão de Estoque, Compras e Faturamento \ Ambiente \ Parâmetros \ Gestão de Estoque, Compras e Faturamento \ Gestão de Compras \ Cotação | - |
| Parâmetros de Tipo de Movimento | Alteração | BackOffice \ Gestão de Estoque, Compras e Faturamento \ Parâmetros do Tipo de Movimento. |  |
| Movimento | Envolvida | BackOffice \ Gestão de Estoque, Compras e Faturamento \ Ambiente \ Parâmetros \ Gestão de Estoque, Compras e Faturamento \ Gestão de Compras \ Solicitação de Compras e Ordem de Compra | - |

### Copiar Marca entre Coligadas

Será criado um processo para que seja permitido realizar a Cópia de Marca entre Coligadas. Este processo ficará disponível no cadastro de Marca quando o perfil do usuário possuir permissão para Incluir Marca.

Ao realizar a Cópia será validado se a máscara de origem e destino são iguais.

### Substituição de Marca na Cotação

**Substituição para Todos Fornecedores**

Na grid de orçamentos da tela de edição da cotação, será exibido um botão **Alterar Marca do(s) Produto(s)**. Este botão irá respeitar as seguintes regras:

1. **Visível:** perfil do usuário possuir permissão para trocar marca na cotação e cotação estiver configurada para **Usar Marca na Cotação** (Parâmetros de Cotação).
2. **Habilitado:** quandostatus da cotação for **Composição, Aguardando Resposta Fornecedores** ou ****Negociação da Melhor Oferta********.****
3. Será necessário selecionar pelo menos um fornecedor na grid de Orçamentos.

Ao clicar no botão será aberto a janela do processo de **Alterar Marca do Produto** para que o usuário escolha a nova marca e selecione quais os itens que esta nova marca será aplicada.

**Regras da Interface:**

**Lookup de Marca:** campo para que seja selecionado o novo valor para marca do produto. As marcas exibidas pelo lookup irá respeitar os itens de orçamento selecionados. Caso não selecione registros, serão retornadas todas as marcas iguais referente a todos os produtos do item de orçamento.

**Botão Alterar:** preenche a coluna Nova Marca para todos os registros selecionados no grid. Caso a marca informada não esteja vinculada ao produto, ela não será preenchida.

**Grid Itens de orçamento** irá exibir os campos:

* **Código do Produto:** irá respeitar a configuração definida no campo **Código do Produto** (Parâmetros de Cotação \ Etapa Definições Gerais 3/5).
* **Descrição do Produto:** irá respeitar a configuração definida no campo **Descrição do Produto** (Parâmetros Gerais \ Tabelas \ Produtos \  Etapa Definições de Produto 1/3).
* **Marca Orçada:** sempre será apresentado.
* **Marca Negociada:**ficará disponível somente quando status da cotação for ****Negociação da Melhor Oferta********.****
* ****Nova Marca:****campo poderá ser editável no grid e seu nome será alterado conforme o status da Cotação. Valores de texto para o campo: Nova Marca Orçada ou Nova Marca Negociada.

Após aplicar a alteração e clicar em **Executar** será feita a troca de cada item da cotação que foi selecionado, para cada fornecedor selecionado, conforme o status da cotação:

* Se o **status da cotação** for **Composição** ou **Aguardando Resposta Fornecedores**, o comportamento será o mesmo definido para a alteração de marca por fornecedor no orçamento, ou seja, serão alterados a Marca Orçada e Marca Negociada.
* Se o **status da cotação** for **Negociação da Melhor Oferta**, o comportamento será o mesmo definido para a alteração de marca por fornecedor na negociação, ou seja, será alterado a Marca Negociada.
* Deve constar no log do processo todas as alterações de marcas realizadas para cada produto.

**Protótipo da janela:**

**Permitir Substituição na Exportação do Orçamento/Negociação**

Será criado no assistente de inclusão da cotação, na tela de escolha de produtos para a cotação, uma opção (“Permite Fornecedor Troca Marca”) por produto para que o usuário possa definir se o fornecedor poderá fazer a troca de marca daquele produto na cotação. Para isso será criado um campo na tabela TCCOTACAOITMMOV para gravar essa informação (TROCAMARCA).

Essa opção virá marcada por padrão quando a cotação usar marca e o perfil do usuário comprador possuir permissão para trocar marca do produto e servirá para os casos em que o orçamento/negociação será enviado para o fornecedor através de planilha de exportação. Esta informação não será exibida no Portal.

Caso seja desmarcada, não será permitido ao fornecedor alterar a marca de um produto que está sendo solicitado no orçamento ou negociação.

Na edição da cotação no grid de **Itens de Movimento**, será exibida por produto a informação que estiver gravada no campo TCCOTACAOITMMOV.TROCAMARCA. Este campo ficará visível e editável quando perfil do usuário possuir permissão para trocar marca na cotação e cotação estiver configurada para **Usar Marca na Cotação** (Parâmetros de Cotação).

Será criado um botão no grid Itens de Movimentos para alterar a informação de **Permitir Fornecedor Trocar Marca**. As regras que serão consideradas para que este campo seja alterado são:

* Deve-se selecionar pelo menos um registro.
* Não tenha sido gerado ordem de compra para o item.
* A Situação do item for igual a Ativo.
* Tipo do Movimento de Compras for igual a Ativo (TIPOMOVCOMPRAS = 1).
* Se o parâmetro "Agrupar Não Agrupar Itens Iguais na Cotação" estiver desmarcado é obrigatório marcar os produtos iguais da Cotação.

A ação que será executada por este botão será atualizar a informação do campo TROCAMARCA da tabela TCCOTACAOITMMOV.

**Agrupamento de Itens de Orçamento**

Caso a cotação esteja trabalhando com agrupamento de itens iguais não será permitido alterar as marcas do orçamento ou negociação, sendo necessário utilizar o botão Aplicar em Selecionados através da seleção da Marca no Lookup. Os itens que possuem a mesma marca no orçamento ou negociação serão agrupados, ou seja, marcas diferentes não podem ser agrupadas.

A troca da marca será realizada buscando as marcas dos itens de orçamento selecionados ou, caso não selecione registros, serão retornadas todas as marcas iguais referente a todos os produtos do item de orçamento, porém ao aplica-las apenas serão permitidas aquelas associadas aos Produtos. Após a alteração das marcas no orçamento ou negociação será realizado o agrupamento dos itens de orçamento.

O agrupamento também deverá ser tratado ao Importar/Exportar Planilha na Cotação.

### **Geração de Ordem de Compra**

Na geração da ordem de compra a partir da cotação, deverá ser observado se houve a troca da marca do produto na cotação. Caso isso tenha ocorrido, se o tipo de movimento usar marca, a marca do item da ordem de compra deverá corresponder à marca que foi negociada na cotação. Para o agrupamento de itens na Ordem de Compra será respeitada a regra abaixo:

**Cotação utiliza marca e OC utiliza marca**

* + Itens de Cotação iguais com marcas iguais: A Ordem de Compra irá agrupar pela marca negociada na cotação.
  + Itens de Cotação iguais com marcas distintas: A Ordem de Compra não irá agrupar os produtos que ficaram com as marcas negociadas distintas na cotação.

**Cotação utiliza marca e OC não utiliza marca**

* + Itens de Cotação iguais com marcas iguais: A Ordem de Compra é gerada agrupando pelos produtos iguais, pois não é considerada a Marca na negociação devido o movimento destino não utilizar Marca.
  + Itens de Cotação iguais com marcas distintas: A Ordem de Compra é gerada agrupando pelos produtos iguais, pois não é considerada a Marca na negociação devido o movimento destino não utilizar Marca.

**Cotação não utiliza marca e OC utiliza marca**

* + Como o agrupamento na cotação considerará apenas se o item está repetido, a ordem de compra é gerada agrupando os itens repetidos, pois não há marca na cotação.

**Cotação não utiliza marca e OC não utiliza marca**

* + Como o agrupamento na cotação considerará apenas se o item está repetido, a ordem de compra é gerada agrupando os itens repetidos, pois não há marca na cotação.

### Quadro Comparativo de Preços

O campo **Marca Negociada** será adicionado à coluna que representa os dados da Solicitação de Compra e também aos dados exibidos por Fornecedor.

Exibir a informação de descrição da marca negociada (TCITMORCAMENTO.IDMARCANEG ). Hint para o campo: “**Marca Negociada**”.

Ao utilizar a opção ***CTRL + clique***, será apresentada a tela **Itens Detalhados** onde serão exibidos os campos **Marca Solicitada** e **Marca Negociada** na pasta **Identificação.** Na pasta **Últimas Compras** será exibida a marca das movimentações do tipo 1.2.XX.

As demais informações do quadro comparativo não terão o seu comportamento alterado.

Esse dado será meramente informativo e não influenciará no cálculo do QCP.

### Interferência

No processo de interferência não será permitido realizar a troca de marca de produto. Será adicionado à grid a informação de **Marca Negociada**logo após a descrição do produto. Este campo não poderá ser alterado na grid, ou seja, será meramente informativo. Caso o comprador deseje alterar a marca do produto ele deverá utilizar o Registro de Negociação.

### Relatórios da Cotação e QCP em Excel

Deverão ser tratados todos os relatórios de cotação e QCP em Excel para apresentar a informação da marca solicitada e marca negociada no(s) respectivo(s) fornecedor(es), quando houver a troca de marca.

**NUCREL0007 - Relatório de Cotação Simples**: este relatório não será alterado.

**NUCREL0006 - Relatório de Cotação Detalhada**: editar relatório para apresentar por fornecedor, a descrição da marca do produto negociado. Considerar o campo TCITMORCAMENTO.IDMARCANEG quando for diferente de TCITMORCAMENTO.IDMARCA. Atentar para a atualização da legenda da planilha.

**Planilha de Cotação Detalhada**: criar mnemônicos para exibir a descrição da marca negociada do produto, que deverá considerar o campo TCITMORCAMENTO.IDMARCANEG. Editar as planilhas para exibir a informação da marca negociada (descrição) disposta da mesma forma que for inserida no quadro comparativo, utilizando-se os mnemônicos criados.

**04.002 - Relatório de Pedido de Orçamento**: editar o relatório para que no produto seja considerado a descrição da Marca Negociada (TCITMORCAMENTO.IDMARCANEG).

**04.007 - Relatório de Pedido de Cotação - EMAIL**: editar o relatório para que no produto seja considerado a descrição da Marca Negociada (TCITMORCAMENTO.IDMARCANEG).

### Qualificação

Quando o sistema estiver parametrizado para utilizar a qualificação “Por Produto” ou “Ambos”, ao realizar a troca de marca de produtos, o usuário poderá criar uma fórmula com a TABPRD para que seja considerado a marca no fornecedor que estiver sendo qualificado.

### Planilha de Orçamento/Negociação

Caso a cotação esteja parametrizada para permitir a troca de marca do produto e a troca de marca de produto pelo fornecedor estiver habilitada, para os itens que estiverem com a opção “Trocar Marca” marcada, na geração da planilha de orçamento/negociação deverá ser criada uma coluna para que o fornecedor possa informar uma marca substituta ao(s) produto(s) solicitado(s).

Esse campo deverá ser tratado por produto, pois nem todos os produtos poderão ter a marca substituída ***e deve considerar a tratativa de qualificação.***

Essa coluna deverá ter a opção de lista suspensa para apresentar as demais marcas associadas aos produto da solicitação. Essa lista suspensa deverá apresentar a opção “em branco” para os casos em que o fornecedor tiver informado uma marca erroneamente e quiser corrigir antes de enviar a planilha para o comprador.

Na importação da planilha de orçamento, se esse campo da planilha estiver em branco, o sistema deverá considera-lo, caso contrário o sistema deverá fazer internamente o processo de alteração da marca do produto e gravar o identificador da marca negociada nos campos TCITMORCAMENTO.IDMARCADORC e TCITMORCAMENTO.IDMARCANEG do fornecedor que está sendo importado. Os demais campos permanecem com o comportamento anterior.

Na importação da planilha de negociação, se esse campo da planilha estiver em branco, o sistema deverá considera-lo, caso contrário o sistema deverá fazer internamente o processo de alteração da marca do produto e gravar o identificador da marca negociada no campo TCITMORCAMENTO.IDMARCANEG do fornecedor que está sendo importado. Os demais campos permanecem com o comportamento anterior.

**Objetos Gerenciais**

* **Planilha:** está sendo disponibilizado uma planilha com as informações de Marca Orçada e Marca Negociada. Para utilizar este recurso será necessário importar a planilha que encontra-se disponível na pasta **Planilha**, interna à pasta **ObjetosGerenciais** no ambiente instalado do sistema (“../CorporeRM/ObjetosGerenciais/Planilha”).
* **Conceito:** também está sendo disponibilizado um novo layout de Conceito com as informações de Marca Orçada e Marca Negociada. Para utilizar este recurso será necessário importar este layout que encontra-se disponível na pasta **Layout**, interna à pasta **ObjetosGerenciais** no ambiente instalado do sistema (“../CorporeRM/ObjetosGerenciais/Layout”).

**Ponto de Atenção:** caso você tenha gerado a Planilha de Orçamento/Negociação que não possui os dados de marca, você deverá utilizar o Layout de Conceito que também não possui os dados de marca. Os cenários permitidos de Importação de Planilha via Layout do Conceito são:

* Planilha Modelo Antigo (sem marca) para Layout Conceito Antigo (sem marca);
* Planilha Modelo Novo (com marca) para Layout Conceito Antigo (sem marca);
* Planilha Modelo Novo (com marca) para Layout Conceito Novo (com marca).

### Histórico de Substituição na Cotação

Não faz parte do escopo dessa funcionalidade o histórico de alteração de marca de produtos na cotação, mas será feita análise para liberar essa funcionalidade junto com a funcionalidade de histórico de negociação da cotação.

**Tabelas Utilizadas**

* TCITMORCAMENTO – Itens de Orçamento
* TCCOTACAOITMMOV – Itens de Movimento Cotados

### **Restrições e Pontos de Atenção**

* Não será considerado na Cotação Web e impacto no Julgamento da Melhor Oferta no quadro comparativo.
* Não será implementado estoque de Produtos por Marca.
* Não será implementado o vínculo entre Marca x Fornecedor.
* Não será implementado Marca na Importação e Exportação de Movimentos.

**Integração com PROTHEUS:**

O BackOffice RM é integrado aos seguintes módulos do Protheus: Manutenção de Ativos, Gestão de Frotas e PDV Protheus (SigaLOJA). A utilização de marca não será considerada neste momento, pois os processos que são utilizados pelas integrações não serão impactados.

## Dicionário de Dados

**Arquivo ou Código do Script:** NU.2016.08\_10

**Atualizar a tabela de Itens de Movimento Cotados (TCCOTACAOITMMOV) com o seguinte campo:** 

|  |  |
| --- | --- |
| **Campo** | TROCAMARCA |
| **Tipo** | SMALLINT |
| **Tamanho** | 2 |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Descrição** | Permite fornecedor trocar marca. |
| **Help de Campo** | Informar se o fornecedor poderá realizar a troca de marca na Planilha de Orçamento/Negociação. |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
