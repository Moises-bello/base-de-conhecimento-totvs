---
content_hash: a17bcd040088a60a64e420e30ce6ff88cd07d57822a82afc68b6ad75ca8b8c60
fetched_at: '2026-06-29T00:06:13.145456+00:00'
page_id: '208340058'
product: rm
source: tdn-rm
title: DT_Melhorias na Qualificação de Fornecedores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=208340058
version: 4
---

# MELHORIAS NO PROCESSO DE QUALIFICAÇÃO

# 

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Qualificação de Fornecedores | Qualificação de Fornecedores |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Qualificação de Fornecedores | Qualificação de Fornecedores | | Qualificação de Produtos/Fornecedores | Qualificação de Produtos/Fornecedores | |
| **Cadastros Iniciais:** | Requisitos de Qualificação |
| **Parâmetro(s):** | N/A |
| **Requisito (ISSUE):** | * [PCREQ-7757](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-7757 "PCREQ-7757") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas utilizadas:** | * TQUALIFICACAOCFO * TQUALIFICACAOPRDCFO |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superior. |
| **Versões/Release:** | 12.1.8 |

## Descrição

Melhorias realizadas no processo de qualificação de fornecedores liberado na release 12.1.4.

## Procedimento para Utilização

```
As melhorias realizadas no processo de qualificação foram as seguintes:
```

 

1. O Nome Fantasia do Cli/For será adicionado nos anexos de qualificação e requisitos do produtos /fornecedor.
2. Incluir as informações de CNPJ e Estado do fornecedor na tela do processo de análise de requisitos.
3. Serão Disponibilizados no relatório detalhado do QCP (Report), e também na exportação de QCP para excel o (Excel de modelo detalhado) a informação de qualificação do fornecedor conforme foi feito na tela do quadro comparativo na visão do mesmo pelo sistema. (OBS: Durante a conversão se o cliente tiver customizado os objetos gerenciais, será necessário realizar o backup das alterações para que o mesmo não corra o risco de ser sobrescrito)
4. A qualificação do fornecedor será tratada por coligada. Este comportamento será alterado para tratar por coligada como é feito na qualificação de produtos/fornecedor. Neste caso o campo CODCOLCFO será incluído na tabela TQUALIFICACAOCFO e os tratamentos necessários serão realizados no serviço de qualificação de fornecedores.  
     
   Na conversão de base de dados o campo CODCOLIGADA da tabela TQUALIFICACAOCFO será alterado para CODCOLCFO e o campo CODCOLIGADA será criado e preenchido da seguinte forma:

* Caso a coligada do fornecedor (CODCOLCFO) for global, os dados da qualificação serão replicados para todas as coligadas que estiverem parametrizadas para qualificação de fornecedores.
* Caso contrario (fornecedor não global) o campo CODCOLIGADA será preenchido com a mesma informação do campo CODCOLCFO.
* O campo CODCOLIGADA criado terá uma forengkey com a tabela global GCOLIGADA
* A chave primária da tabela TQUALIFICACAOCFO será alterado para incluir o campo CODCOLCFO

divs
