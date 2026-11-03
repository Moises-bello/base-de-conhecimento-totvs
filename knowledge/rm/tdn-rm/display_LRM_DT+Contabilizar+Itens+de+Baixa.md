---
content_hash: 884a8bbde76ee7419abf548a99976a1b0a9c9369ade33aa36343252728e55f25
fetched_at: '2026-06-29T00:09:24.012509+00:00'
page_id: '422546677'
product: rm
source: tdn-rm
title: DT Contabilizar Itens de Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Contabilizar+Itens+de+Baixa
version: 2
---

# CONTABILIZAR ITENS DE BAIXA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Contabilizar Itens de Baixa | Contabilizar Itens de Baixa | |
| **Tickets relacionados** | 3954923 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-9118> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL, Oracle |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.23 |

## Descrição

Processo para permitir contabilizar os itens de baixa de lançamentos baixados, parcialmente baixados ou baixados por acordo que não foram contabilizados no momento da baixa.

## Procedimento para Utilização

Acesse o menu *Contas a Pagar / Receber | Operações Financeiras | Contabilizar Itens de Baixa:*

Deve ser informado os seguintes parâmetros:

* Filtro: deve ser informado um filtro que será usado para selecionar os itens de baixas para contabilização.
* Data de contabilização: deve ser informado a data de contabilização
* Pasta compartilhada para salvar o log do processo: deve ser informado um diretório onde será gravado o log do processo.
* Enviar e-mail para: lista de e-mails separados por ponto e virgula. Caso seja informada será enviado um e-mail com as informações do processo e o caminho onde foi gerado o log.

Esse processo pode ser agendado caso seja utilizado o ambiente de 3 camadas.

**Importante**: Caso esteja utilizando um ambiente 3 camadas a pasta onde será gravado o log deverá ser uma pasta compartilhada e com permissão para o conta/usuário que esta executando o RM.Host.Service.exe ou RM.Hos.exe.
