---
content_hash: d3188a0f7890615e159db466ffd0a80b33e4c665ec2be1791a10a706ea399af0
fetched_at: '2026-06-29T00:08:18.867212+00:00'
page_id: '266972528'
product: rm
source: tdn-rm
title: TVVBL0_DT_Liberacao_Comp_Atualizar_SituacaoY_Para_Ativo
type: documentation
url: https://tdn.totvs.com/display/LRM/TVVBL0_DT_Liberacao_Comp_Atualizar_SituacaoY_Para_Ativo
version: 2
---

# LIBERAÇÃO DA COMPETÊNCIA DEVE ATUALIZAR SITUAÇÃO DE FUNCIONÁRIO COM LICENÇA PATERNIDADE FINALIZANDO NO MÊS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Liberação da Competência* |
| **Situação/Requisito:** | *No processo da Liberação de Competência não está retornando o funcionário afastado com o tipo Y (Licença Paternidade) para Ativo, mesmo quando o afastamento está com o campo Data Final no mês que está sendo finalizado.* |
| **Solução/Implementação:** | *Ajuste na Liberação de Competência para verificar os funcionários com Licença paternidade (tipo Y) sendo finalizada no mês, e alterar automaticamente a situação para Ativo (A), inserindo o registro no histórico de mudança de situação.* |
| **Chamados   relacionados:** | *TVVBL0, TVX101* |
| **Versões/Release:** | *11.82.46, 12.1.14* |
