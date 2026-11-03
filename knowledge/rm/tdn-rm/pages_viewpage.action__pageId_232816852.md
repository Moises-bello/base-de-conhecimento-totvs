---
content_hash: 11250a7764b6a73253ccb9a9cc6b03f5952a85c89f35d170b33cd8fc64171aa5
fetched_at: '2026-06-29T00:06:27.274727+00:00'
page_id: '232816852'
product: rm
source: tdn-rm
title: DT_PCREQ-8867_Importar_Cotações_via_Planilha_Excel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232816852
version: 121
---

# IMPORTAR COTAÇÕES VIA PLANILHA EXCEL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Compras* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cotação* | *CmpCotacaoAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Planilha Net | GlbPlanilhaNetAction | | Consultas SQL | GlbConsSqlAction | |
| **Cadastros Iniciais:** | *Gestão de Estoque, Compras e Faturamento | Gestão | Planilha Net | Importar o objeto gerencial da Planilha Net*  **Integração | Integração | Conceito | Importar o objeto gerencial do Conceito** |
| **Parâmetro(s):** | *Citados abaixo, no documento.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Chamados Relacionados** | *Não se aplica.* |
| **Requisito (ISSUE):** | *Não se aplica.* |
| **País(es):** | *Todos.* |
| **Banco(s) de Dados:** | *Oracle ou SQL Server.* |
| **Tabelas Utilizadas:** | *Não se aplica.* |
| **Sistema(s) Operacional(is):** | *Windows.* |

## Descrição

Uma planilha de Pedido de Orçamento que será enviada para os fornecedores escolhidos na cotação para preenchimento das informações de orçamento ou negociação. Após preenchida e devolvida pelos fornecedores, a planilha será importada no módulo de cotação para registro dos orçamentos ou negociações e continuidade do processo.

## Procedimento para Utilização

## Exportação de Planilha de Orçamento ou Negociação

Para realizar a exportação de planilha de orçamento ou negociação, os passos abaixo deverão ser realizados.

#### Importar Planilha Net

1. Acessar **Gestão de Estoque, Compras e Faturamento | Gestão | Planilha Net.**
2. Ir até **Processos | Importação de Planilha.NET** e importar o objeto gerencial da Planilha Net (*extensão: .PlanNetTotvs*).

#### Exportar Planilha de Orçamento/Negociação

1. Acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação**.
2. Selecionar uma cotação e ir até **Processos | Comunicar Fornecedores**.
3. Na tela de Principais Parâmetros, escolher Enviar Orçamento via E-mail.
4. No lookup de Planilha Orçamento que será exibido, selecionar a planilha que foi importada no passo anterior.
5. Selecionar o tipo de exportação (orçamento ou negociação).
6. Selecionar os fornecedores que receberão a planilha.
7. Seguir com o processo normalmente.

No processo de comunicação com os fornecedores, uma planilha relacionada será criada e anexada ao e-mail que o fornecedor receberá.

Para saber mais sobre os campos que serão exportados e suas respectivas regras, acesse a **Especificação de Requisitos** ().

## Importação de Planilha de Orçamento ou Negociação

#### Importar Conceito

1. Acessar **Integração | Integração | Conceito.**
2. Ir até **Processos | Importar Conceito** e importar o objeto gerencial do Conceito (*extensão: .TotvsConcept*).

#### Importar Planilha de Orçamento/Negociação

1. Acessar **Gestão de Estoque, Compras e Faturamento | Compras | Cotação.**
2. Ir até **Processos | Importar Planilha de Orçamento/Negociação**.
3. Selecionar o conceito importado no passo anterior e avançar.
4. Informar o caminho do diretório que contém as planilhas de orçamento e/ou negociação.
5. Seguir com o processo normalmente.

O processo irá percorrer todos as planilhas da pasta informada, importando as informações para a base de dados e atualizando as cotações.

## Customização da Planilha

Para customizar uma planilha, basta que o usuário insira ou exclua as colunas de informação que ele deseja na planilha. Caso as informações inseridas ou excluídas sejam geradas pelo sistema, o usuário deverá editar a consulta SQL associada a planilha para inserir ou excluir as informações desejadas. Posteriormente, deverá editar o conceito de importação para associar ou desassociar os dados que foram customizados.

Segue um exemplo de exclusão de informações de negociação. Em nossa planilha modelo, iremos excluir a informação de Unidade Orçada.

* Excluindo a coluna de Unidade Orçada

Em seguida, editaremos a consulta SQL que está associada a planilha e que gerará os dados a serem enviados para o fornecedor.

* Verificando a consulta SQL associada à planilha

* Editando e excluindo a linha referente a CODUNDORC, na consulta SQL associada à planilha

O próximo passo é desassociar a informação no conceito de importação.

* Editando o conceito de importação de negociação

* Desassociada a ligação de Unidade Orçada.

Verifique que a ligação do conceito foi desfeita.

Para maiores informações técnicas e detalhadas, acesse a **Especificação de Requisitos** ().

divs
