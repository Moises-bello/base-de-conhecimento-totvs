---
content_hash: f5971cb6c9e369d8c6b807a9ce18aca419f9a96fcd810b8a92120517252fa0a6
fetched_at: '2026-06-29T00:08:10.093982+00:00'
page_id: '240301120'
product: rm
source: tdn-rm
title: ER_CPMOV001-6_Melhorias_Itens_Cotacao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPMOV001-6_Melhorias_Itens_Cotacao
version: 135
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
| **Requisito1** | CPMOV001-6 | **Subtarefa1** | CPMOV001-128 |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Permitir que o usuário defina quais campos serão exibidos no item de orçamento da cotação.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros de Cotação | Alteração | Gestão de Estoque, Compras e Faturamento \ Ambiente \ Parâmetros \ Gestão de Estoque, Compras e Faturamento \ Gestão de Compras \ Cotação | - |
| Cotação | Envolvida | Gestão de Estoque, Compras e Faturamento \ Compras \ Cotação | - |

Durante o processo de Cotação, caso o usuário precise identificar informações complementares sobre os produtos que compõe a Cotação, o comprador pode precisar de informações de Item de Movimento, Produto para que complemente as informações que serão enviadas aos fornecedores. Sendo assim, iremos realizar a seguinte melhoria na Cotação para que o comprador possa ter mais informações para agilizar o processo.

# **Parâmetros da Cotação**

Disponibilizar nos parâmetros da Cotação um recurso para que o usuário possa selecionar quais as colunas ele deseja visualizar nos Itens de Orçamento. Criar o passo **Definições Gerais 5/5**nos parâmetros da Cotação (Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.06.02 - Cotação). Neste passo será apresentado ao usuário todos os campos disponíveis para que selecione quais ficarão visíveis no Item de Orçamento. 

As campos que serão disponibilizados para escolha do usuário são: 

| Entidade | Campo | Descrição | Regra |
| --- | --- | --- | --- |
| TPRODUTO | CODIGOPRD | Código do Produto | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.06.02 - Cotação | Definições Gerais 3/5  Será exibido somente se o **Código do Produto** estiver diferente de **Código Principal**. |
| TPRODUTO | CODIGOREDUZIDO | Código Reduzido | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.01 - Definições Gerais | Definições de Produto 2/3  Será exibido se o **Usa Código Reduzido** for diferente de **Não Utilizar**  Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.06.02 - Cotação | Definições Gerais 3/5  Será exibido somente se o **Código do Produto** estiver diferente de **Código Reduzido**. |
| TPRODUTO | CODIGOAUXILIAR | Código Auxiliar | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.06.02 - Cotação | Definições Gerais 3/5  Será exibido somente se o **Código do Produto** estiver diferente de **Código Auxiliar**. |
| TPRODUTO | NOMEFANTASIA | Nome Fantasia | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.01 - Definições Gerais | Definições de Produto 1/3  Será exibido se a **Descrição do produto** for diferente de **Nome Fantasia** |
| TPRODUTO | DESCRICAO | Descrição | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.01 - Definições Gerais | Definições de Produto 1/3  Será exibido se a **Descrição do produto** for diferente de **Descrição** |
| TPRODUTO | DESCRICAOAUX | Descrição Auxiliar | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.01 - Definições Gerais | Definições de Produto 1/3  Será exibido se a **Descrição do produto** for diferente de **Descrição Auxiliar** |
| TPRODUTO | CAMPOLIVRE | Campo Livre | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.02 - Campos Opcionais | Campos Opcionais  Será exibido a informação do campo: **Nome do campo livre 1 do produto** |
| TPRODUTO | CAMPOLIVRE2 | Campo Livre 2 | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.02 - Campos Opcionais | Campos Opcionais  Será exibido a informação do campo: **Nome do campo livre 2 do produto** |
| TPRODUTO | CAMPOLIVRE3 | Campo Livre 3 | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.02 - Campos Opcionais | Campos Opcionais  Será exibido a informação do campo: **Nome do campo livre 3 do produto** |
| TPRODUTODEF | NUMNOFABRIC | Número do Produto no Fabricante | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.06.02 - Cotação | Definições Gerais 3/5  Será exibido somente se o **Código do Produto** estiver diferente de **Número Fabricante**. |
| TITMMOV | CAMPOLIVRE | Campo Livre | N/A |
| TITMMOVHISTORICO | HISTORICOCURTO | Histórico Curto |  |
| TITMMOVHISTORICO | HISTORICOLONGO | Histórico Longo |  |
| TTB1 | DESCRICAO | Descrição | Será exibido a descrição da tabela de classificação 1 informada no Item de Movimento da Solicitação de Compras. Mesmo que o tipo de movimento de solicitação de compras não trabalhe com Tabela de Classificação, caso seja parametrizado a coluna será exibida na grid porém sem a informação do dado. |
| TTB2 | DESCRICAO | Descrição | Será exibido a descrição da tabela de classificação 2 informada no Item de Movimento da Solicitação de Compras. Mesmo que o tipo de movimento de solicitação de compras não trabalhe com Tabela de Classificação, caso seja parametrizado a coluna será exibida na grid porém sem a informação do dado. |
| TTB3 | DESCRICAO | Descrição | Será exibido a descrição da tabela de classificação 3 informada no Item de Movimento da Solicitação de Compras. Mesmo que o tipo de movimento de solicitação de compras não trabalhe com Tabela de Classificação, caso seja parametrizado a coluna será exibida na grid porém sem a informação do dado. |
| TTB4 | DESCRICAO | Descrição | Será exibido a descrição da tabela de classificação 4 informada no Item de Movimento da Solicitação de Compras. Mesmo que o tipo de movimento de solicitação de compras não trabalhe com Tabela de Classificação, caso seja parametrizado a coluna será exibida na grid porém sem a informação do dado. |
| TTB5 | DESCRICAO | Descrição | Será exibido a descrição da tabela de classificação 5 informada no Item de Movimento da Solicitação de Compras. Mesmo que o tipo de movimento de solicitação de compras não trabalhe com Tabela de Classificação, caso seja parametrizado a coluna será exibida na grid porém sem a informação do dado. |
| TITMMOVCOMPL | Todos | Todas | Todos os campos da tabela **GDEFCOMPL**, filtrados pela **Coligada**, sistema **Compras** e a tabela de dados **TITMMOVCOMPL**  Serão exibidos somente os Campos Complementares Visíveis dos Tipos de Movimento de Solicitação de Compras (Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros do Tipo de Movimento | Etapa Compras/Venda - Outros Dados - Tipo de Movimento de Compra = Solicitação de Compras). |

Os campos selecionados e exibidos em **Campo Item Orçamento/Negociação Visíveis** serão gravados no campo CAMPOSITMORCNEGVISIVEIS da tabela de Parâmetros da Cotação (TCPARAMETROS) separados pelo carácter virgula ( , ). Os campos devem ser gravados junto com o nome da tabela, como por exemplo "TPRODUTO.NOMEFANTASIA, TITMMOV.CAMPOLIVRE...".

# **Registro de Orçamento**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e clicar em **Editar** é apresentada a janela de **Cotação**. Na pasta **Orçamentos**, clique no botão **Registrar Orçamento** e acesse a pasta **Produtos**. Os campos configurados nos parâmetros da Cotação serão disponibilizados na Grid somente se existir algum campo parametrizado em **Campo Item Orçamento/Negociação Visíveis.**Estes novos campos não poderão ser editados, ou seja, ficarão esmaecidos.

# **Registro de Negociação**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e clicar em **Editar** é apresentada a janela de **Cotação**. Na pasta **Orçamentos**, clique no botão **Registrar Negociação**e acesse a pasta **Produtos**. Nesta pasta serão apresentados os campos na Grid somente se existir algum campo parametrizado em **Campo Item Orçamento/Negociação Visíveis** nos parâmetros da Cotação. Estes novos campos não poderão ser editados, ou seja, ficarão esmaecidos.

**Tabelas Utilizadas**

* TCITMORCAMENTO – Itens de Orçamento
* TCPARAMETROS – Parâmetros da Cotação

**Restrições e Pontos de Atenção**

* Não será considerado na Cotação Web e Quadro Comparativo, Relatórios Simples e Detalhado, Planilha de Comunicação de Fornecedores.

## Protótipo de Tela

**Protótipo Parâmetros Cotação**

## Dicionário de Dados

**Arquivo ou Código do Script:** /\*$Versao=NU.2016.06\_05\*/

|  |  |
| --- | --- |
| **Tabela** | TCPARAMETROS |
| **Campo** | CAMPOSITMORCNEGVISIVEIS |
| **Tipo** | MEMO |
| **Tamanho** | 16 |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Campos de Item de Orçamento/Negociação Visíveis |
| **Help de Campo** | Informar quais campos ficarão disponíveis em Itens de Orçamento ou Itens de Negociação para visualização. |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
