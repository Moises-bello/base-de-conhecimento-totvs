---
content_hash: 5afe785b0b6a8af0b453e146439a094b3c32903682e637615b6795fa0867974c
fetched_at: '2026-06-29T00:08:41.333745+00:00'
page_id: '286721159'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-273 DT Cancelamento de Lançamento (Proc -Alteração Situação
  Mat. e Cancelamento Contrato)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286721159
version: 102
---

# Cancelamento de Lançamento Financeiro

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cancelamento de Contrato | Cancelamento de Contrato | | Alteração da Situação de Matricula | Alteração da Situação de Matricula |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Serviço de cancelamento de Lançamento* | *Serviço de cancelamento de Lançamento* | |  |  | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Tickets relacionados** |  |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** |  |
| **País(es):** |  |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |

## Descrição

O processo de "Cancelamento de Contrato" e "Alteração da Situação de Matricula" quando marcamos a opção "Cancelar lançamentos em abertos e não vencidos", aplica a seguinte validação:

Durante o cancelamento do lançamento financeiro, se o boleto estiver com o status igual a Remetido ou Registrado o TOTVS Educacional não permite o cancelamento, sendo necessário realizar o cancelamento da remessa no TOTVS Financeiro.

Realizamos uma evolução para que o TOTVS Educacional realize automaticamente o cancelamento da remessa quando o boleto estiver com o status igual a Remetido ou Registrado.

Para que o sistema assuma o comportamento de realizar o cancelamento da remessa automaticamente, será necessário habilitar um parâmetro, caso este parâmetros não esteja marcado o sistema continuará impedindo o cancelamento de lançamento se o boleto estiver com status igual a Remetido ou Registrado.

| Atenção  Sempre que houver um cancelamento de remessa automaticamente o sistema irá apresentar um mensagem no LOG informando quais os Lançamento / Boletos tiveram sua remessa cancelada.  Para este cenário a remessa ficará como pendente no módulo TOTVS Financeiro, sendo necessário reenviar a remessa ao banco novamente para as devidas atualizações.  Ressaltamos que apenas cancelamos a remessa automaticamente como um facilitador tendo como objetivo não impedir a execução do processo, mas as operações e controle de pendências devem ser realizadas pelo TOTVS Financeiro.  Contate o Suporte EM CASO DE DÚVIDAS |
| --- |

## Procedimento para Implantação

Em parâmetros do sistema "***Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin - Geral 3/4***” marque o parâmetro "***Cancelar Remessa automaticamente ao cancelar o lançamento financeiro quando o boleto estiver com status Remetido ou Registrado***".

Agora ao cancelar o lançamento em que o boleto esteja com status de Remetido ou Registrado o sistema automaticamente cancelará a remessa.

* + Processo de Cancelamento de Contrato (Disponível *no anexo de processo do cadastro de contrato*)

* + Processo de Alteração da Situação de Matricula (*Disponível no anexo de processo do anexo de matriculas do período letivo)*

Observe que quando ocorrer o cancelamento de remessa automaticamente será apresentado no LOG.

## Vídeo

 

divs
