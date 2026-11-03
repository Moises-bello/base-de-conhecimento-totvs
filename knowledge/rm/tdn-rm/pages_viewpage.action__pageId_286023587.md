---
content_hash: 58c5367a1f58fe02099e7f5565d2e1f17c7366ecab96635d21e1a2bc43f87503
fetched_at: '2026-06-29T00:08:39.872535+00:00'
page_id: '286023587'
product: rm
source: tdn-rm
title: DT Retorno de cobrança de cancelamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286023587
version: 113
---

# Retorno de cobrança de cancelamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | FIN000172 | *Retorno de cobrança eletrônica.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | FIN000073 | *Serviço de Cancelamento* | |
| **Cadastros Iniciais:** | *Incluir um novo boleto* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FINANCEIRO01-1141 |
| **País(es):** | *bra* |
| **Banco(s) de Dados:** | *SqlServer, Oracle* |
| **Tabelas Utilizadas:** | *FBOLETO, FBANCOLAYOUTS* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Ao realizar o retorno de cobrança eletrônica o sistema agora terá a possibilidade de realizar o cancelamento (normalmente o que é chamado de baixa pelo banco) dos boletos, alterando o campo StatusCNAB para cancelado.

## Procedimento para Implantação

O sistema terá disponibilidade de executar tal processamento a partir da versão 12.1.18.1.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

Cadastrar no Layout Bancário os valores referentes ao cancelamento de remessa bancária.

Estas informações devem ser buscadas dentro do manual de cada banco.

|  |  |
| --- | --- |
| **Nome da Variável:** | *FBANCOLAYOUTS.RETCOBCODCANCELAMENTO* |
| **Tipo:** | String |
| **Descrição:** | Código do Cancelamento no Retorno de Cobrança. |
| **Valor Padrão:** | Vazio |

## Procedimento para Utilização

       1.            Dúvidas sobre o processo de retorno de cobrança [clique aqui.](http://wikihelp.totvs.com.br/WikiHelp/FIN/FIN.RetornoCobranca.aspx)

## Vídeo

600400

divs
