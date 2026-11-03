---
content_hash: 003abc4210a4bc3ab3d361632b61639ad7942856638e50595451d4c0a04e2229
fetched_at: '2026-06-29T00:08:36.839522+00:00'
page_id: '284477119'
product: rm
source: tdn-rm
title: 440238 MATESTCNTFTOF01-362 DT - Alteração do Tamanho do Campo Nome Fantasia
  no Cadastro de Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284477119
version: 106
---

# Alteração do Tamanho do Campo Nome Fantasia no Cadastro de Produto

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | ***Construção e Projetos**.* |
| **Módulo:** | ***T**OTVS Gestão de Estoque Compras e Faturamento.***** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Produto* | *Cadastro de Produtos* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Cadastros | Produtos e Serviços* | *Cadastro de Produtos* | |  |  | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Tickets relacionados** | *440238.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [MATESTCNTFTOF01-362](http://jiraproducao.totvs.com.br/browse/MATESTCNTFTOF01-362) |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *SQL e Oracle.* |
| **Tabelas Utilizadas:** | *TPRODUTO, TPRD (VIEW).* |
| **Sistema(s) Operacional(is):** | *Windows.* |

## Descrição

Alterado o tamanho máximo permitido a ser digitado no campo Nome Fantasia (**TPRODUTO.NOMEFANTASIA**) no cadastro de produto para 120 caracteres.

Esta alteração se fez necessária pois no [Manual de Orientação do Contribuinte](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=) (Documento que rege os padrões técnicos de comunicação para o sistema de Nota Fiscal Eletrônica) a SEFAZ aceita a descrição do produto ou serviço com um tamanho de 1-120 caracteres, e este campo (**TPRODUTO.NOMEFANTASIA**) é usado no envio de NF-e para a montagem da tag **xProd** no XML da nota fiscal pela Linha RM.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.18.

## Procedimento para Utilização

1. Acessar Cadastros | Produtos e Serviços.
2. Realizar a Inclusão ou a Alteração de um determinado Produto ou Serviço.

* Verificar que o campo Nome Fantasia permitirá a digitação de até 120 caracteres conforme descrição supracitada.  
    
  **Exemplo:**xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxY.

divs
