---
content_hash: d1ba4f8d10336bd4f4ed51bda83b315c6a94b92e06eee20541693af39211c6f3
fetched_at: '2026-06-29T00:08:11.463265+00:00'
page_id: '243010138'
product: rm
source: tdn-rm
title: DT_CPMOV001-267_Melhorias_Nos_Itens_Da_Cotação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243010138
version: 117
---

# MELHORIAS NOS ITENS DA COTAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoques, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cotação | *CmpCotacaoAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Parâmetros do sistema* |  | | *Orçamento / Negociação* | CmpCotacaoOrcamentosAction | |
| **Cadastros Iniciais:** | *Campos Complementares, Tabelas de Classificação, Item de Movimento(Solicitaçao de Compras da Cotação)* |
| **Parâmetro(s):** | *Conforme citado abaixo* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados Relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | 1. [CPMOV001-267](http://jiraproducao.totvs.com.br/browse/CPMOV001-267 "Melhoria nos Itens de Cotação - Documentação") |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *TCITMORCAMENTO, TCPARAMETROS* |
| **Sistema(s) Operacional(is):** | *Windows XP SP2 ou superior* |

## Descrição

Durante o processo de Cotação de produtos, em alguns momentos é necessário que os usuários verifiquem informações complementares sobre os produtos que compõe a Cotação, como por exemplo verificar informações dos Itens de Movimento ou do cadastro do Produto para que complemente as informações que serão enviadas aos fornecedores.

Sendo assim, será disponibilizado através de parâmetros específicos uma forma para que o comprador possa incluir informações complementares nos itens de orçamento para agilizar o processo de Cotação.

## Procedimento para Configuração e Utilização

Para disponibilizar os novos campos para visualização nos itens de orçamento é necessário realizar as seguintes configurações:

# **Parâmetros da Cotação**

Acesse os Parametros do Módulo de compras em: **Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.06.02 - Cotação** e selecione a filial desejada e vá para **Definições Gerais 5/5**. Neste passo será apresentado ao usuário todos os campos disponíveis para que ele selecione quais ficarão visíveis na tela de Itens de Orçamento. 

As campos que serão disponibilizados para escolha do usuário são: 

| Entidade | Campo | Descrição | Regra |
| --- | --- | --- | --- |
| TPRODUTO | CODIGOPRD | Código do Produto | Será exibido somente se o **Código do Produto** estiver diferente de **Código Principal** (Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.06.02 - Cotação | Definições Gerais 3/5). |
| TPRODUTO | CODIGOREDUZIDO | Código Reduzido | Será exibido se o **Usa Código Reduzido** for diferente de **Não Utilizar** (Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.01 - Definições Gerais | Definições de Produto 2/3)  Será exibido somente se o **Código do Produto** estiver diferente de **Código Reduzido** (Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.06.02 - Cotação | Definições Gerais 3/5). |
| TPRODUTO | CODIGOAUXILIAR | Código Auxiliar | Será exibido somente se o **Código do Produto** estiver diferente de **Código Auxiliar** (Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.06.02 - Cotação | Definições Gerais 3/5). |
| TPRODUTO | NOMEFANTASIA | Nome Fantasia | Será exibido se a **Descrição do produto** for diferente de **Nome Fantasia** (Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.01 - Definições Gerais | Definições de Produto 1/3) |
| TPRODUTO | DESCRICAO | Descrição | Será exibido se a **Descrição do produto** for diferente de **Descrição** (Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.01 - Definições Gerais | Definições de Produto 1/3) |
| TPRODUTO | DESCRICAOAUX | Descrição Auxiliar | Será exibido se a **Descrição do produto** for diferente de **Descrição Auxiliar** (Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.01 - Definições Gerais | Definições de Produto 1/3) |
| TPRODUTO | CAMPOLIVRE | Campo Livre | Será exibido a informação do campo: **Nome do campo livre 1 do produto** (Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.02 - Campos Opcionais | Campos Opcionais) |
| TPRODUTO | CAMPOLIVRE2 | Campo Livre 2 | Será exibido a informação do campo: **Nome do campo livre 2 do produto** (Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.02 - Campos Opcionais | Campos Opcionais) |
| TPRODUTO | CAMPOLIVRE3 | Campo Livre 3 | Será exibido a informação do campo: **Nome do campo livre 3 do produto** (Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01.04.07.02 - Campos Opcionais | Campos Opcionais) |
| TPRODUTODEF | NUMNOFABRIC | Número do Produto no Fabricante | Será exibido somente se o **Código do Produto** estiver diferente de **Número Fabricante** (Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.06.02 - Cotação | Definições Gerais 3/5) |
| TITMMOV | CAMPOLIVRE | Campo Livre | Não se aplica. |
| TITMMOVHISTORICO | HISTORICOCURTO | Histórico Curto | Não se aplica. |
| TITMMOVHISTORICO | HISTORICOLONGO | Histórico Longo | Não se aplica. |
| TTB1 | DESCRICAO | Descrição | Será exibido a descrição da tabela de classificação 1 informada no Item de Movimento da Solicitação de Compras. Mesmo que o tipo de movimento de solicitação de compras não trabalhe com Tabela de Classificação, caso seja parametrizado a coluna será exibida na grid porém sem a informação do dado. |
| TTB2 | DESCRICAO | Descrição | Será exibido a descrição da tabela de classificação 2 informada no Item de Movimento da Solicitação de Compras. Mesmo que o tipo de movimento de solicitação de compras não trabalhe com Tabela de Classificação, caso seja parametrizado a coluna será exibida na grid porém sem a informação do dado. |
| TTB3 | DESCRICAO | Descrição | Será exibido a descrição da tabela de classificação 3 informada no Item de Movimento da Solicitação de Compras. Mesmo que o tipo de movimento de solicitação de compras não trabalhe com Tabela de Classificação, caso seja parametrizado a coluna será exibida na grid porém sem a informação do dado. |
| TTB4 | DESCRICAO | Descrição | Será exibido a descrição da tabela de classificação 4 informada no Item de Movimento da Solicitação de Compras. Mesmo que o tipo de movimento de solicitação de compras não trabalhe com Tabela de Classificação, caso seja parametrizado a coluna será exibida na grid porém sem a informação do dado. |
| TTB5 | DESCRICAO | Descrição | Será exibido a descrição da tabela de classificação 5 informada no Item de Movimento da Solicitação de Compras. Mesmo que o tipo de movimento de solicitação de compras não trabalhe com Tabela de Classificação, caso seja parametrizado a coluna será exibida na grid porém sem a informação do dado. |
| TITMMOVCOMPL | Todos | Todas | Todos os campos da tabela **GDEFCOMPL**, filtrados pela **Coligada**, sistema **Compras** e a tabela de dados **TITMMOVCOMPL**  Serão exibidos somente os Campos Complementares Visíveis dos Tipos de Movimento de Solicitação de Compras (**Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros do Tipo de Movimento |****Etapa Compras/Venda - Outros Dados - Tipo de Movimento de Compra = Solicitação de Compras**). |

# **Registro de Orçamento**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e clicar em **Editar** é apresentada a janela de **Cotação**. Na pasta **Orçamentos**, clique no botão **Registrar Orçamento** e acesse a pasta **Produtos**. Os campos configurados nos parâmetros da Cotação serão disponibilizados na Grid somente se existir algum campo parametrizado em **Campo Item Orçamento/Negociação Visíveis**. Estes novos campos não poderão ser editados, ou seja, ficarão esmaecidos.

# **Registro de Negociação**

Ao acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação** e clicar em **Editar** é apresentada a janela de **Cotação**. Na pasta **Orçamentos**, clique no botão **Registrar Negociação**e acesse a pasta **Produtos**. Nesta pasta serão apresentado os campos na Grid somente se existir algum campo parametrizado em **Campo Item Orçamento/Negociação Visíveis** nos parâmetros da Cotação. Estes novos campos não poderão ser editados, ou seja, ficarão esmaecidos.

# **Restrições e Pontos de Atenção**

* Não será considerado na Cotação Web e Quadro Comparativo, Relatórios Simples e Detalhado, Planilha de Comunicação de Fornecedores.

divs
