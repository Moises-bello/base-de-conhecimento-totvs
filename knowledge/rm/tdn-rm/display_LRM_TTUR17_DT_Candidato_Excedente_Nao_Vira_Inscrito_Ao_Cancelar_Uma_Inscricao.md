---
content_hash: 6b0520c20d4a8427d3d0da2d5a1b1692d005e4b0d7ff4e1e958facc3b5a26124
fetched_at: '2026-06-29T00:06:20.049230+00:00'
page_id: '221546952'
product: rm
source: tdn-rm
title: TTUR17_DT_Candidato_Excedente_Nao_Vira_Inscrito_Ao_Cancelar_Uma_Inscricao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTUR17_DT_Candidato_Excedente_Nao_Vira_Inscrito_Ao_Cancelar_Uma_Inscricao
version: 124
---

# CANDIDATOS INSCRITOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Cancelamento de inscrição não altera candidatos excedentes.* |
| **Situação/Requisito:** | *Foi identificado que ao cancelar uma inscrição em um processo seletivo que utiliza controle de vagas e possui candidatos excedentes o sistema não esta alterando o candidato excedente para inscrito nem gerando o lançamento financeiro para o mesmo.* |
| **Solução/Implementação:** | *Foi identificado que o falha era causado pelo status da opção do candidato, que não retornava corretamente os candidatos excedentes dá área ofertada, não alterando seu status e nem gerando o lançamento, após a correção o sistema altera corretamente o status e gera o lançamento.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TTX123* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
