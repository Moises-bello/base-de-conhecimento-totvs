---
content_hash: 08909c916dde8e5cbd2f988240e0f7945cb8b2abeb3b14e54bc4777a4edfe13c
fetched_at: '2026-06-29T00:08:35.585461+00:00'
page_id: '281984027'
product: rm
source: tdn-rm
title: 654772 MATFATCMPCRM01-360 DT Motivo de Referência para Devolução de Emprestimo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=281984027
version: 106
---

# Motivo de Referência para Devolução de Emprestimo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | ***Construção e Projetos**.* |
| **Módulo:** | ***T**OTVS Gestão de Estoque Compras e Faturamento***** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *MOV 001* | INCLUSAO DE MOVIMENTO | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** | *.* |
| **Ponto de Entrada:** | *.* |
| **Tickets relacionados** | *654772* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *[MATFATCMPCRM01-360](http://jiraproducao.totvs.com.br/browse/MATFATCMPCRM01-360)* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | **SQLServer e Oracle** |
| **Tabelas Utilizadas:** | **TMOTIVOREFMOV** |
| **Sistema(s) Operacional(is):** |  |

## Descrição

Criado um novo motivo de referência chamado "Devolução de Empréstimo". Esse motivo é similar ao "Devolução por compra" porém permite a troca de Lote dos itens de movimentos do Movimento de Destino.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.16.124*

## Procedimento para Utilização

  1.  Acessar o cadastro de Motivo de Referência (Cadastros -> mais -> Tabelas Auxiliares -> Motivo Referência) e executar o processo "Inclusão de Motivo de Referência".

            Isso irá criar o novo Motivo de Referência.

  2.  Após isso, haverá o novo Motivo de referência (31 - Devolução de Empréstimo) que permitirá a troca de Lote dos itens de movimentos do Movimento de Destino.

divs
