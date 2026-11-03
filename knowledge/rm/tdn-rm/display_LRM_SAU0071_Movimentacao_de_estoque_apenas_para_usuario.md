---
content_hash: be3a927b1d0beacf5d1ba0cbcd7d1a11aec852fdcf5371d5827b79802f3839cf
fetched_at: '2026-06-29T00:06:25.158777+00:00'
page_id: '224395833'
product: rm
source: tdn-rm
title: SAU0071_Movimentacao_de_estoque_apenas_para_usuario
type: documentation
url: https://tdn.totvs.com/display/LRM/SAU0071_Movimentacao_de_estoque_apenas_para_usuario
version: 119
---

# Movimentação de estoque apenas para usuário.

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO HOSPITALAR |
| **Versões:** | Todas. |
| **Ocorrência:** | Realizando estes procedimentos, apenas o usuário terá como realizar movimentações de estoque. |
| **Passo a passo:** | **1º Passo)** Acessar o sistema TOTVS;  **2º Passo)** Acessar o módulo Saúde e o menu Utilitários -> Consultas SQL.  **3º** **Passo**) Para bases em Oracle, crie a seguinte consulta:  SELECT USERNAME FROM GLOGIN WHERE COMPUTERNAME IN  (SELECT USERENV(‘TERMINAL’) FROM DUAL) AND CODSISTEMA = ‘O’    Para bases em SQL Server  SELECT USERNAME FROM GLOGIN WHERE COMPUTERNAME = HOST\_NAME() AND CODSISTEMA = 'O'    **4º Passo)** Acessando o menu Estoques -> Movimentação de Estoque  Crie um filtro da seguinte forma:  Usuário IN (nome da consulta que criastes)    **5º Passo)** Agora o usuário somente vê suas próprias requisições |

divs
