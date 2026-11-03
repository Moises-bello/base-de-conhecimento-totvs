---
content_hash: 3519b8e3434183838c933f767515f445c4d940d1486b98ee917eeaafdf4e52f6
fetched_at: '2026-06-29T00:08:33.376810+00:00'
page_id: '274314908'
product: rm
source: tdn-rm
title: 717572 MATESTCNTFTOF01-159 DT Sped Fiscal - Geração do Bloco K200
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274314908
version: 104
---

# Sped Fiscal - Geração do Bloco K200

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Totvs Gestão de Estoque Compras e Faturamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *BLOCO K FIS 006* | *INTEGRACAO FISCAL* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Informe a(s) rotina(s) envolvidas*.* | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Tickets relacionados** | *717572* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *MATESTCNTFTOF01-159* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL e Oracle.* |
| **Tabelas Utilizadas:** | *Não se aplica.* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Melhoria ao gerar o Bloco K200. Para os registros que necessitam da consistência da "Situação da Mercadoria" em Anexos | Dados Fiscais do Produto, seja considerada também a consistência da aba Informações por Filial campo "Situação da Mercadoria". Isso porque em alguns casos um mesmo Produto pode ter classificação diferente por Filial. Primeiramente será verificado se existe a informação da situação da mercadoria na tabela de informações por filial. Caso não exista, será utilizado a informação disponível no cadastro de dados fiscais do produto.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.15*deste chamado.

## Procedimento para Utilização

* Entrar no  cadastro de Produtos e cadastrar a "Situação da Mercadoria" em Anexos | Dados Fiscais do Produto ou na aba Informações por Filial campo "Situação da Mercadoria".

* Feito o cadastro, o mesmo será utilizado na geração do SPED - BLOCO K200. Primeiramente será verificado se existe a informação da situação da mercadoria na tabela de informações por filial. Caso não exista, será utilizado a informação disponível no cadastro de dados fiscais do produto.

* Gerar o SPED e verificar se as informações geradas no arquivo estão corretas.

divs
