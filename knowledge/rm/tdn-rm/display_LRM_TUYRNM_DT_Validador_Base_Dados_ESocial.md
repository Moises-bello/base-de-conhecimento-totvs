---
content_hash: 4b7f93c19daa8aa5853157aca419fb62d2dab270ff08ce350bcb52a692c1954f
fetched_at: '2026-06-29T00:08:11.200422+00:00'
page_id: '241701762'
product: rm
source: tdn-rm
title: TUYRNM_DT_Validador_Base_Dados_ESocial
type: documentation
url: https://tdn.totvs.com/display/LRM/TUYRNM_DT_Validador_Base_Dados_ESocial
version: 115
---

# VALIDADOR DA BASE DE DADOS - ESOCIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Validador da base de dados - eSocial |
| **Situação/Requisito:** | Ao executar o validador da base de dados do eSocial para funcionários do tipo temporário, com rateio de tomadores, o sistema está apresentando mensagem informando que a coluna 'TELEFONE' não pertence à tabela Resultado. |
| **Solução/Implementação:** | Verificado que a mensagem ocorre, pois na consulta base de tomadores de serviços, não é retornado o campo TELEFONE. Foi realizada a alteração da consulta para que a mesma retorne o campo TELEFONE. |
| **Chamados relacionados:** | TUYRNM |

divs
