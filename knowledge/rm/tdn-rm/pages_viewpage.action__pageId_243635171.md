---
content_hash: a0298315c13457e820caf8cc1c2d504e88af4ca68bb7488a3cd1b25fbe7af977
fetched_at: '2026-06-29T00:08:12.109649+00:00'
page_id: '243635171'
product: rm
source: tdn-rm
title: DT_CPMOV001-357_Condição_Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243635171
version: 114
---

# CONDIÇÃO DE PAGAMENTO NA COTAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **Gestão de Compras*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cotação.* | *CmpCotacaoAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Parâmetros da Cotação* | *Não se aplica.* | | *Assistente de Geração de Cotação* | *CmpAssistenteCotacaoAction* | | *Registrar Orçamento* | *CmpCotacaoAction* | | *Registrar Negociação* | *CmpCotacaoAction* | |
| **Cadastros Iniciais:** | *Condição de Pagamento.* |
| **Parâmetro(s):** | *Condição de Pagamento obrigatório na Inclusão de Cotação.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados Relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | *PCREQ-9558 e CPMOV001-357* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *Oracle ou SQL Server.* |
| **Tabelas Utilizadas:** | *TCPARAMETROS - Parâmetros da Cotação*  *TCCOTACAO - CotaçõesInforme as tabelas utilizadas.* |
| **Sistema(s) Operacional(is):** | *Windows 7 SP1 ou superior.* |

## Descrição

Criado o parâmetro **Condição de Pagamento obrigatório na Inclusão de Cotação,** em parâmetros da Cotação, que terá como valor default: marcado. Desta forma o comportamento da Cotação continuará sendo executado normalmente.

Quando parâmetro **Condição de Pagamento obrigatório na Inclusão de Cotação** estiver **desmarcado**, será permitido:

* Incluir Cotação sem informar condição de pagamento.
* **Incluir Fornecedor na Cotação**sem informar a condição de pagamento.
* Ao **Registrar Orçamento** e **Registrar Negociação** a Condição de Pagamento será obrigatória.

Para obter maiores detalhes acesse a .

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

**Atenção:** a configuração abaixo deve ser realizada somente quando se deseja trabalhar sem informar condição de pagamento na cotação.

1. No **Gestão de Estoque, Compras e Faturamento**, acesse **Ambiente/Parâmetros/**Gestão de Estoque, Compras e Faturamento/Gestão de Compras/Cotação****. Na **Etapa 2 - Definições Gerais**desmarque o parâmetro **Condição de Pagamento obrigatório na Inclusão de Cotação.**

## Procedimento para Utilização

**Assistente de Inclusão de Cotação**

1. No Gestão de Estoque, Compras e Faturamento, acesse **Compras / Cotação**.

O sistema apresenta a janela de **Filtros - Cotação - Composição.**

2. Selecione uma opção de filtro e clique em Executar.

3. Na visão de Cotação clique em **Incluir**.

O sistema apresenta a janela **Assistente de Cotação.**

4. Preencha os dados nas etapas do Assistente e avance até a etapa **Informações Gerais.**

Na etapa **Informações Gerais** caso deseje incluir a cotação sem Condição de Pagamento, apague a informação no campo **Condição de Pagamento** e avance.

5. Clique em **Executar**para concluir o assistente de geração de cotação.

****Incluir Fornecedor na Cotação****

1. No Gestão de Estoque, Compras e Faturamento, acesse **Compras / Cotação**.

O sistema apresenta a janela de **Filtros - Cotação - Composição.**

2. Selecione uma opção de filtro e clique em Executar.

3. Na visão de Cotação selecione um registro e clique em **Editar**.

O sistema apresenta a janela de **Cotação:....**

4. Na pasta **Orçamentos**clique em**Incluir Fornecedor na Cotação.**O Pesquise e selecione o(s) registro(s) e confirme.

divs
