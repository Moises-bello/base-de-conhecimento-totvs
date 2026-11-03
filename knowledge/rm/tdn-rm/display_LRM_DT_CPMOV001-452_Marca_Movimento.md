---
content_hash: 1c0ae81ac969afcc110d583692c80006b1f0771d5d9398ec06104cf3c5823e91
fetched_at: '2026-06-29T00:08:17.046076+00:00'
page_id: '249957008'
product: rm
source: tdn-rm
title: DT_CPMOV001-452_Marca_Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Movimento
version: 117
---

# MARCA NO MOVIMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Parâmetro de Tipo de Movimento | RMSParamsWizardAction. | | Item de Movimento | MovMovimentoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro de Produto | EstPrdAction | | Parâmetros Gerais | RMSParamsWizardAction | | Cadastro de Marca | EstMarcaAction | | Marcas do Produto | EstPrdMarcaAction | |
| **Cadastros Iniciais:** | Cadastrar marcas;  Vincular marcas ao produto.  Parametrizar tipo de movimento para usar marca. |
| **Parâmetro(s):** | Parâmetros de Tabela de Marcas. |
| **Ponto de Entrada:** | Não se aplica. |
| **Chamados Relacionados** | Não se aplica. |
| **Requisito (ISSUE):** | CPMOV001-452 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | Oracle ou SQL Server. |
| **Tabelas Utilizadas:** | TITMTMV – Tipos de Movimento - Complemento  TITMMOV– Item de Movimento |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Permitir que o usuário possa utilizar as marcas de um determinando produto em suas movimentações.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **RM**, acesse **BackOffice/Gestão de Estoque, Compras e Faturamento/Ambiente/Parâmetros/**Gestão de Estoque, Compras e Faturamento****. Na janela de **Assistente de Implantação de Processos** selecione um Tipo de Movimento e configure o parâmetro **Edita Marca** na **Etapa Item - Identificação 1/2**:

Este parâmetro terá as seguintes opções:

* + - **Não Edita:** não usa marca no item de movimento.
    - **Edita:** usa marca no item de movimento. Campo não obrigatório.
    - **Edita Obrigatoriamente:** usa marca no item de movimento. Informação obrigatória.
    - **Mostra:** exibe a marca no item de movimento. Neste caso será considerado como valor default a marca definida para o produto no cadastro de Produtos.

## Procedimento para Utilização

### **Cadastro de Marca e Vinculo de Marcas ao Produto**

1. Consulte o documento técnico:

### **Marca no Item de Movimento**

1. No Gestão de Estoque, Compras e Faturamento, acesse Compras / Solicitação de Compras  
   O sistema apresenta a janela de Solicitação de Compras (Gestão de Compras).
2. Informe o Tipo de Movimento parametrizado para editar marca e informe também a Filial.  
   O sistema apresenta a janela de Filtros - Solicitação de Compras (Gestão de Compras). Selecione um filtro e confirme.
3. Clique em Incluir  
   O sistema apresenta a janela de edição de Movimento. Informe os dados solicitados.
4. Na pasta Itens clique em Incluir.  
   O sistema apresenta a janela de inclusão de item de movimento.
5. Informe o Produto.  
   Ao incluir um item de movimento na pasta **Identificação\Tabelas** o sistema carrega automaticamente para o campo a Marca Default do Produto. Caso deseje alterar informe no campo **Marca** o código que será utilizado na solicitação.
6. Confira os dados e confirme.

divs
