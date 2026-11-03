---
content_hash: 1312e85ae330772b1689711b6946f19c957567e39d2c30a6e9e6d72a48c9248c
fetched_at: '2026-06-29T00:08:09.336281+00:00'
page_id: '239034110'
product: rm
source: tdn-rm
title: ER_CPMOV001-5_Grid_Monitor
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPMOV001-5_Grid_Monitor
version: 109
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Segmento Executor** |  | | |
| **Projeto1** | R\_CP\_MOV 2016/2017 | **IRM1** | CPMOV001-3 |
| **Requisito1** | CPMOV001-5 | **Subtarefa1** | CPMOV001-13 |
| **Chamado2** |  | | |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Visando uma melhor usabilidade no processo de compras será criada o Grid Monitor onde será possível a visualização de solicitações de compra e ordens de compra, sendo de acordo com os tipos de movimento parametrizado, e cotações.

## Definição da Regra de Negócio

O Grid Monitor facilitará a visualização de todas as movimentações de Solicitação de Compra, de acordo, com a sua regra de disponibilidade para serem utilizadas na Cotação, e caso, a Cotação esteja parametrizada para Central de Compras, todas as movimentações das Coligadas e Filiais que participam da Central de Compras serão exibidas na visão de Solicitações de Compras. A Ordem de Compra serão exibidas todas as movimentações, independente se forem provenientes de Cotação. Todas as Cotações serão exibidas sem restrição.

No filtro da visão da Solicitação de Compras serão exibidos os campos de Centro de Custo, Projeto e Tarefa, somente, se houver algum tipo de movimento parametrizado na Etapa 71 - Projeto o campo "Usa Rateio de Tarefa" como Obrigatório ou Opcional.

Para a Cotação todos os seus respectivos anexos e processos estarão disponíveis na visão do Grid de Monitor. As Solicitações de Compras e Ordens de Compra serão apresentados os processos **apenas** aqueles que possuem permissão por perfil, ou seja, processos com permissão por tipo de movimento e usuário não estarão disponíveis.

Os anexos de Solicitação de Compras e Ordem Compra  que estarão disponíveis para o Grid Monitor são:

* Campos Complementares
* Rastreabilidade de Movimento
* Log de Comparação de Impostos do Totvs Colaboração
* Itens de Movimento
* Itens de Contrato Relacionado
* NF-e
* Itens de Movimento - Workflow Fluig

Os processos de Solicitação de Compras que estarão disponíveis para o Grid Monitor são:

* Aprovação por Workflow.
* Estornar Item não recebido.
* Processa Grupo.
* Finalizar Separação com divergência.
* Incluir / Editar / Excluir Filtros.
* Desaprovar Movimentos / Item de Compra.
* Colocar Movimento em Separação
* Iniciar Separação
* Ativar / Inativar
* Liberar Desconto Máximo por Senha
* Voltar ao Status de Separação Anterior
* Concluir Pedido
* Alterar Movimentos em Aprovação por Workflow
* Alterar Movimentos Aprovados por Workflow do Fluig

Os processos de Ordem de Compras que estarão disponíveis para o Grid Monitor são:

 

* Aprovação por Workflow.
* Estornar Item não recebido.
* Processa Grupo.
* Finalizar Separação com divergência.
* Envio de Ordem de Compra por E-mail
* Incluir / Editar / Excluir Filtros.
* Desaprovar Movimentos / Item de Compra.
* Colocar Movimento em Separação
* Iniciar Separação
* Ativar / Inativar
* Liberar Desconto Máximo por Senha
* Concluir Pedido
* Alterar Movimentos em Aprovação por Workflow
* Alterar Movimentos Aprovados por Workflow do Fluig
* Exportar para XML (EDI Compra)
* Integrar Pedido com Portal de Compras Paradigma
* Consultar Aceite do Fornecedor no Portal Paradigma

Todas as visões do Grid Monitor devem ter a possibilidade de configuração de colunas, permitindo ao usuário definir o posicionamento das colunas e definir quais colunas serão apresentadas, podendo incluir outras colunas que sejam pertinentes à funcionalidade da visão e que estejam disponíveis para exibição. Na visão de Solicitação de Compra o usuário poderá ter opção de visualização por Movimento ou Item de Movimento.

Os campos que estarão disponíveis na visão de Solicitação de Compras com a visualização por Movimento em suas respectivas ordens para o Grid Monitor são: 

* **Criticidade**
* Status
* Coligada
* Filial
* Local de Estoque
* Tipo de Movimento
* Identificador do Movimento
* Número do Movimento
* Solicitante
* **Itens de Movimento Pendentes**
* Data de Emissão
* Data de Entrega
* Valor Líquido
* Centro de Custo
* Departamento.

Os campos que estarão disponíveis na visão de Solicitação de Compras com a visualização por Item de Movimento em suas respectivas ordens para o Grid Monitor são:

* **Criticidade do Item**
* Status do Item
* Coligada
* Filial
* **Tipo de Movimento**
* Local de Estoque
* Solicitante do Movimento
* Código do Produto
* Nome Fantasia
* Descrição
* Fabricante
* Unidade
* Quantidade
* Preço Unitário
* Histórico do Item
* Centro de Custo
* Departamento

Os campos que estarão disponíveis na visão de Ordem de Compras em suas respectivas ordens para o Grid Monitor são: 

* Status
* Coligada
* Filial
* Local de Estoque
* Tipo de Movimento
* Identificador do Movimento
* Número do Movimento
* Nome Fantasia Fornecedor
* CNPJ Fornecedor
* Data de Emissão
* Data de Entrega (data de entrega do movimento)
* Valor Líquido
* **Solicitante**
* Centro de Custo
* Departamento.

Os campos que estarão disponíveis na visão de Cotação para o Grid Monitor são:

* Status
* Filial
* Código Cotação
* Data Cotação
* Data Limite Resposta
* Comprador
* Quantidade de Fornecedores
* Custo Financeiro
* Tipo de Julgamento
* Tipo de Comunicação
* **Cotação WEB (Coluna com link para visualização da cotação web)**
* Solicitante

Na opção de configuração de colunas devem ser apresentadas todas as colunas default da visão e as colunas que hoje já são possíveis serem exibidas na visão de Solicitação de Compra, Cotação e Ordem de Compra.

As respectivas telas de edição, para os cadastros de Solicitação de Compra, Cotação e Ordem de Compra, estarão disponíveis para inclusão, edição e exclusão de acordo com a permissão de usuário 

## Protótipo de Tela

**Protótipo 01 - Visão de Solicitação de Compra**

****Protótipo 02 - Visão de Cotações****

******Protótipo 03 - Visão de Ordem de Compra******

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

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
