---
content_hash: 7aff9e426e49d986485b7937aaa8f0b2937b5750634385a28f3fecddea72f983
fetched_at: '2026-06-29T00:08:36.988261+00:00'
page_id: '284861841'
product: rm
source: tdn-rm
title: Melhoria na importação de movimento de devolução via conceito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284861841
version: 107
---

# T\_MATFATCMPCRM01-564\_Importacao\_Movimento\_Devolucao

## Importação de movimentos de devolução via conceito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Importação de movimento via conceito | ConConceptProcessAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Exportação de movimento através do Gerador de Saidas | GenExecucaoAction | |  |  | |
| **Cadastros Iniciais:** | Inclusão de movimento e exportação |
| **Parâmetro(s):** | Não se aplica. |
| **Ponto de Entrada:** | Não se aplica. |
| **Tickets relacionados** | *Não se aplica.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-564 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle ou SQL Server. |
| **Tabelas Utilizadas:** | TMOV, TITMMOV, TMOVRELAC e TITMMOVRELAC |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## **Descrição**

Melhoria na importação de movimento de devolução. Para fazer referência entre os itens do movimento de origem com destino no arquivo TXT, foi necessário incluir na estrutura de importação e exportação (Conceito e Gerador de Saídas) o campo NSEQITMMOVRELAC conforme imagem abaixo:  

**Conceito** 

 

 

**Gerador de Saídas** 

 

 

## Procedimento para Utilização

**1º** Inclusão do movimento de entrada  

 

**2º** Inclusão do movimento de devolução utilizando copia por referencia

 

 

 

**3º** Exportação do movimento de devolução utilizando o gerador de saídas

**Linha de código E** -  Relacionamento entre Movimentos 

**Linha de código X** - Relacionamentos entre Itens de Movimentos 

**Observação:**

 Este novo campo (Linha X - Item relacionado) terá valor idêntico ao sequencial do movimento a ser incluído, fazendo assim o devido relacionamento entre os itens.

 

divs
