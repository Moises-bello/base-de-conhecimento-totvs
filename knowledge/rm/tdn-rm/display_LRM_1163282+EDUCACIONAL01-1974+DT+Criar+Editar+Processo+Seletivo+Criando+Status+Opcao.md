---
content_hash: fba2683aac92de1b43eb2d3b1f03007f14364e90374e7a816da13abcff1ba23c
fetched_at: '2026-06-29T00:08:40.881750+00:00'
page_id: '286515563'
product: rm
source: tdn-rm
title: 1163282 EDUCACIONAL01-1974 DT Criar Editar Processo Seletivo Criando Status
  Opcao
type: documentation
url: https://tdn.totvs.com/display/LRM/1163282+EDUCACIONAL01-1974+DT+Criar+Editar+Processo+Seletivo+Criando+Status+Opcao
version: 101
---

# PROCESSO SELETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Processo Seletivo |
| **Função:** | Processo Seletivo |
| **Situação/Requisito:** | Ao criar ou editar um processo seletivo o sistema está criando status de opções com o código da filial como sendo código do processo seletivo. |
| **Solução/Implementação:** | Foi identificado que sempre que a visão de processos seletivos é exibida o sistema valida se existem status de opções para a filial do contexto, ocorreu alguma alteração na execução da visão que afetou este comportamento, sendo assim foi feito uma alteração para o sistema sempre utilizar para a validação a coligada e filial do contexto, não a do filtro. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
