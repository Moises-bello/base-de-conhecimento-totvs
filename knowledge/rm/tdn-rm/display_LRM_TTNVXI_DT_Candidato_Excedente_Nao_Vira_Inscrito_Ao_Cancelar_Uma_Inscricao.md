---
content_hash: 2fbb471f4bd17d47e38a30b8235352c83886ce1d52de28d3d4977ac5603fd62f
fetched_at: '2026-06-29T00:06:20.044330+00:00'
page_id: '221546881'
product: rm
source: tdn-rm
title: TTNVXI_DT_Candidato_Excedente_Nao_Vira_Inscrito_Ao_Cancelar_Uma_Inscricao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTNVXI_DT_Candidato_Excedente_Nao_Vira_Inscrito_Ao_Cancelar_Uma_Inscricao
version: 1
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
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *11.82.42* |
| **Versão Expedida:** | *11.82.41* |

divs
