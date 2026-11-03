---
content_hash: a25f4be9d9d02d237922147923e831a70040db1bbbf39c8bdfce60072534a0f1
fetched_at: '2026-06-29T00:08:11.984616+00:00'
page_id: '243633023'
product: rm
source: tdn-rm
title: TVBZAB_DT_Cancelar_Inscricao_Processo_Seletivo_Fora_Periodo
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBZAB_DT_Cancelar_Inscricao_Processo_Seletivo_Fora_Periodo
version: 111
---

# CANCELAR INSCRIÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Cancelar inscrição* |
| **Situação/Requisito:** | *Ao tentar cancelar uma inscrição, o sistema não cancela e retorna um erro de referência de objeto.* |
| **Solução/Implementação:** | *Foi identificado que o sistema não está tratando o cancelamento corretamente, pois o processo seletivo utiliza controle de vagas, sendo assim, ao cancelar uma inscrição, o sistema tentará alterar os excedentes para inscritos, pois há vagas, porém, o processo seletivo está fora de um período válido, assim, o erro é retornado pois não pode "inscrever" candidatos em um processo seletivo que está fora do período de inscrição, pois a inscrição dos excedentes implica em geração de lançamento e alocação automática caso o processo seletivo esteja configurado para tal. Sendo assim, foi feito o ajuste da mensagem para que fique claro o motivo do não cancelamento da inscrição.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
