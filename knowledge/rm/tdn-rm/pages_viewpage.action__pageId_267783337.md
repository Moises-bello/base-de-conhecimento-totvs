---
content_hash: 910c55a1f89b9df15d5393d1e80c5621be975d1e52dbd09b7a700d900000cd80
fetched_at: '2026-06-29T00:08:19.381762+00:00'
page_id: '267783337'
product: rm
source: tdn-rm
title: TVPGT0_DT_Geração_Lançamento_Data_Baixa_Fora_Periodo_de_Baixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267783337
version: 110
---

# Geração de Lançamento Financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Geração de Lançamento |
| **Situação/Requisito:** | Está ocorrendo uma não conformidade em anexo ao gerar lançamento do Educacional para o Financeiro.  Mensagem:  A data da baixa encontra-se fora do período para baixa.  Data Inicial: 01/01/2015  Data Final:   31/12/2016  Esta mensagem é apresentada somente quando temos a configuração de baixa automática configurada nos parâmetros do educacional e quando nos parâmetros do financeiro o período de baixa esta parametrizado. |
| **Solução/Implementação:** | Melhoria no serviço de geração de lançamento do educacional para que não seja apresentada nenhuma não conformidade quando o financeiro parametriza um período permitido para baixa. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TVPGT0 |
| **Requisito (ISSUE):** | N/A |

divs
