---
content_hash: bf49fe7654cc0bec1653f265303ecfe897712908715e768a262f6a0927d364d9
fetched_at: '2026-06-29T00:08:59.568311+00:00'
page_id: '364288616'
product: rm
source: tdn-rm
title: DT Desfazer Conciliação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364288616
version: 13
---

# DESFAZER CONCILIAÇÃO DE CARTÃO DE CRÉDITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cancelar Conciliação | Cancelar Conciliação |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Importação do Arquivo de Conciliação | Importação do Arquivo de Conciliação | | Conciliação Automática | Conciliação Automática | | Conciliação Manual | Conciliação Manual | |
| **Cadastros Iniciais:** | Importação do Arquivo de Conciliação |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FINANCEIRO01-7074 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server |
| **Tabelas Utilizadas:** | FCONCILCARTAO; FCONCILIACAOGRPOPER, FCONCILCARTAOTRANS, FXCX |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

O objetivo é cancelar a conciliação dos dados de pagamentos com cartão de crédito/débito, revertendo o que fora realizado nos processos de 'Conciliação Automática' e/ou 'Conciliação Manual'. Ao final do processo, executado com sucesso, a conciliação fica com o status 'Não conciliado'.

## Modo de usar

Para acessar a funcionalidade é necessário acessar o módulo Gestão Financeira em 'Menu Principal' → 'Backoffice' → 'Gestão Financeira'. Logo após siga para a aba 'Movimentações Bancárias' → 'Cartão de Crédito' → 'Conciliação'.

1. Selecione uma conciliação
2. Siga para 'Processos' e clique em 'Cancelar Conciliação'
3. Ao exibir a mensagem escolho 'Sim' para executar a conciliação; ou 'Não' para abortar a conciliação.
4. Se clicar em 'Sim', aguarde o processo de cancelamento finalizar e logo após será exibido uma mensagem expondo o status do processo

## Importante

O campo "Status de conciliação do cartão" representará o status da conciliação no extrato de caixa:

* Previsto (0);
* Pago (1);
* Rejeitado (2).
