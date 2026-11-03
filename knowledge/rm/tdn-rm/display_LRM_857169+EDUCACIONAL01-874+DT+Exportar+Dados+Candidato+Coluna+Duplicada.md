---
content_hash: 57e86e588cd4cb1a57702d2f34f272a6bb102997b5c4a599076868dd039d0fe8
fetched_at: '2026-06-29T00:08:35.264751+00:00'
page_id: '275121235'
product: rm
source: tdn-rm
title: 857169 EDUCACIONAL01-874 DT Exportar Dados Candidato Coluna Duplicada
type: documentation
url: https://tdn.totvs.com/display/LRM/857169+EDUCACIONAL01-874+DT+Exportar+Dados+Candidato+Coluna+Duplicada
version: 96
---

# EXPORTAR DE DADOS DOS CANDIDATOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Exportar dados dos candidatos* |
| **Situação/Requisito:** | *Foi identificado uma falha no processo de exportação de dados de candidatos, ao executar o processo é retornado uma mensagem de nomes de colunas duplicadas, impedindo assim a execução do processo.* |
| **Solução/Implementação:** | *Foi identificado que a consulta sql responsável por carregar os dados dos candidatos possuía duas colunas "nome" e no momento de se executar a ordenação da consulta o sistema retornava o erro por não saber por qual coluna ordenar, sendo assim foi feito o ajuste para que o sistema identifique corretamente por qual coluna ordenar a lista de candidatos, durante a análise também foi identificado um erro na consulta que após alocar os candidatos e distribuir os cadernos de prova, os candidatos são repetidos na lista de exportação, foi feito também o ajuste na junção da consulta sql.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
