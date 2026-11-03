---
content_hash: 24d3a37b2bfe10046d843d12493ca601fb95c04e23e1117da4e2c17b6cf70657
fetched_at: '2026-06-29T00:08:11.933476+00:00'
page_id: '243631244'
product: rm
source: tdn-rm
title: DT_CPMOV001-357_CNPJ_NomeFantasia_RazaoSocial_Fornecedor
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CPMOV001-357_CNPJ_NomeFantasia_RazaoSocial_Fornecedor
version: 115
---

# VISUALIZAR CNPJ, NOME FANTASIA E RAZÃO SOCIAL DO FORNECEDOR

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Proejtos.* |
| **Módulo:** | **Gestão de Compras*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cotação.* | *CmpCotacaoAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cliente/Fornecedor | FinCFOAction | | Assistente de Cotação | CmpAssistenteCotacaoAction | | Incluir Fornecedor na Cotação | CmpLookupFornecedoresCotacaoAction | |
| **Cadastros Iniciais:** | *Usuário possuir permissão para Incluir/Editar Cotação.* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados Relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | *PCREQ-9558 e CPMOV001-357* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *Oracle ou SQL Server.* |
| **Tabelas Utilizadas:** | *FCFO - Clientes/Fornecedores*  *TCORCAMENTO - Orçamentos* |
| **Sistema(s) Operacional(is):** | *Windows 7 SP1 ou superior.* |

## Descrição

Ao compor a cotação, na etapa de seleção do fornecedor foi disponibilizado a informação de CNPJ do Fornecedor. Ao incluir um novo fornecedor o CNPJ irá aparecer como primeira opção de filtro. Os campos **Nome Fantasia** e **Razão Social**tambémpoderão ser utilizados como filtros na busca de novos registros.

## Procedimento para Configuração

**Definir a ordem do campo CNPJ/CPF na visão de Fornecedores**

Para que as informações de **CNPJ/CPF** fique disponíveis na visão, no passo de  **Escolha de Fornecedores** ou ****Escolha de Fornecedores -**** **Qualificação**, clique em **Configurar Colunas** e selecione a coluna **CNPJ / CPF**ou clicar na opção**Restaurar configuração padrão**da janela**Selecionar colunas**:

Após escolher a coluna e definir a sua ordem de exibição, ela ficará disponível na visão de fornecedores conforme imagem abaixo:

**Escolha de Fornecedores**:

**Escolha de Fornecedores - Qualificação:**

## Procedimento para Utilização

**Assistente de Cotação**

1. Acesse **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**

   O sistema apresenta a janela de **Filtros - Cotação - Composição.**
2. Selecione uma opção de filtro e clique em Executar.
3. Na visão de Cotação clique em Incluir.  
   O sistema apresenta a janela de **Assistente de Cotação.**
4. No passo para **Escolha de Fornecedores**e/ou**Escolha de Fornecedores - Qualificação** serão exibidos na grid os campos **CNPJ/CPF, Nome Fantasia e Razão Social** do fornecedor.
5. Neste passo clique em Incluir. O campo **CNPJ/CPF** será apresentado como primeira opção para pesquisar um registro. Os campos **Nome Fantasia** e **Razão Social**tambémpoderão ser utilizados como filtros na busca de novos registros.

**Incluir Fornecedor na Cotação**

1. Acesse **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**

   O sistema apresenta a janela de **Filtros - Cotação - Composição.**
2. Selecione uma opção de filtro e clique em Executar.
3. Na visão de Cotação clique em Editar.  
   O sistema apresenta a janela de **Cotação:... .**
4. Na pasta **Orçamentos** clique em **Incluir Fornecedor na Cotação.**O campo **CNPJ/CPF** será apresentado como primeira opção para pesquisar um registro. Os campos **Nome Fantasia**e**Razão Social**tambémpoderão ser utilizados como filtros na busca de novos registros.

divs
