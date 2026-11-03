---
content_hash: 765aaf9883c9d813f7f7be40a23873927dd8a2cf4864bcdbdbdfb8f6d42bbaa3
fetched_at: '2026-06-29T00:08:08.467232+00:00'
page_id: '238036964'
product: rm
source: tdn-rm
title: TTGNUV_DT_Recebimento_NFe_Base_CNPJ
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGNUV_DT_Recebimento_NFe_Base_CNPJ
version: 115
---

# Recebimento de Nota Fiscal Eletrônica

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Inclusão de Movimento através de XML - TOTVS Colaboração* | MovTraducaoXMLTOTVSColabProcAction | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *Parâmetro por Tipo de Movimento:*   * *Etapa 3 - Movimento - Emitente e Destinatário*   + *Mov-Emitente/Destinatario 2/2* *Consiste Fornecedor: Base CNPJ* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQLServer e Oracle* |
| **Tabelas Utilizadas:** | *TNFEENTRADA, FCFO e TMOV* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Esta implementação tem como objetivo permitir que sejam recebidas notas fiscais cujo pedido tenha sido feito por outro fornecedor, desde que a base do CNPJ seja a mesma.

### Parametrização

Nos parâmetros do Tipo de Movimento da NF-e "Etapa 3 - Mov-Emitente/Destinatário 2/2", deve ser utilizado o parâmetro "Consiste Fornecedor = Base CNPJ".

### Regra de Negócio

Ao receber a Nota Fiscal, durante a busca pelos pedidos de compra, se o parâmetro estiver marcado, o sistema pesquisará todos os fornecedores que possuem a mesma base de CNPJ, ex:

Fornecedor da NF:   
99.999.999/9999-01

Filiais do Fornecedor:   
99.999.999/9999-02  
99.999.999/9999-03  
  
Neste caso, o sistema seleciona os pedidos de compra de todos os fornecedores citados, caso encontre algum movimento do fornecedor 99.999.999/9999-01, o mesmo será utilizado, caso contrário serão analisados os fornecedores 99.999.999/9999-02 e 99.999.999/9999-03. 

Com o parâmetro desmarcado, a consulta é feita através do Código do Fornecedor, ou seja, não serão considerados os demais fornecedores que possuem a mesma base de CNPJ.

divs
