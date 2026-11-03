---
content_hash: a07ede79de2c0e932f8a748d8d0d63165ff81ef9da56c37c84d15d33bcc4a9f5
fetched_at: '2026-06-29T00:08:17.027063+00:00'
page_id: '249956823'
product: rm
source: tdn-rm
title: DT_CPMOV001-452_Marca
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca
version: 114
---

# MARCA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Parâmetro de Marca | RMSParamsWizardAction | | Cadastro de Marca | EstMarcaAction | | Marcas do Produto | EstPrdMarcaAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro de Produto | EstPrdAction | | Parâmetros Gerais | RMSParamsWizardAction | |
| **Cadastros Iniciais:** | Não se aplica. |
| **Parâmetro(s):** | Parâmetros Tabela de Marcas. |
| **Ponto de Entrada:** | Não se aplica. |
| **Chamados Relacionados** | Não se aplica. |
| **Requisito (ISSUE):** | CPMOV001-452 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | Oracle ou SQL Server. |
| **Tabelas Utilizadas:** | TPAR – Parâmetros Gerais  TMARCA – Tabela de Marcas  TPRODUTODEF – Dados dos Produtos Globais por Coligada  TPRODUTODEFMARCA – Tabela de Produto x Marcas |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Permitir que o usuário possa cadastrar marcas para um determinando produto.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **RM**, acesse **BackOffice/Gestão de Estoque, Compras e Faturamento/Ambiente/Parâmetros/**Gestão de Estoque, Compras e Faturamento****. Na janela de **Assistente de Implantação de Processos** selecione **Parâmetros Gerais/Tabelas/Marcas** e configure o(s) parâmetro(s) para a tabela de Marca a seguir:

**Atenção:**

1. **Recomendamos que seja utilizado Marca Global para facilitar o controle dos processos que irão utilizar a informação de Marca.**
2. Ao habilitar a opção de **Usa Marca Global**, caso já exista algum registro cadastrado como marca global, não será permitido alterar a configuração.

## Procedimento para Utilização

### **Cadastro de Marca**

1. No Gestão de Estoque, Compras e Faturamento, acesse Cadastros / Mais... / Tabelas Auxiliares / Marcas  
   O sistema apresenta a janela de Filtros - Marcas. Selecione um filtro e clique em Executar.
2. Na janela de Marcas clique em Incluir.
3. Informe os dados de Código e Descrição
4. Confira os dados e confirme.

### **Marca Default do Produto**

1. No Gestão de Estoque, Compras e Faturamento, acesse Cadastros / Produtos  
   O sistema apresenta a janela de Filtros - Produtos. Selecione um filtro e clique em Executar.
2. Na janela de Produtos clique em Editar.
3. Na pasta Identificação informe a Marca para o Produto.
4. Confira os dados e confirme.

### **Marcas do Produto**

1. No Gestão de Estoque, Compras e Faturamento, acesse Cadastros / Produtos  
   O sistema apresenta a janela de Filtros - Produtos. Selecione um filtro e clique em Executar.
2. Na janela de Produtos clique em Anexos / Marca do Produto.
3. Na janela de Marcas do Produto clique em Incluir.  
   O sistema apresenta a janela de Marca do Produto.
4. Informe o código da marca e confirme.

divs
