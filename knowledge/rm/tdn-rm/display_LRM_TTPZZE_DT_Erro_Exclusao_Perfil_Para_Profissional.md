---
content_hash: 473715536226699c2b29341a375a6a420307c84e7c1902099d9275d070901510
fetched_at: '2026-06-29T00:06:20.259736+00:00'
page_id: '221551067'
product: rm
source: tdn-rm
title: TTPZZE_DT_Erro_Exclusao_Perfil_Para_Profissional
type: documentation
url: https://tdn.totvs.com/display/LRM/TTPZZE_DT_Erro_Exclusao_Perfil_Para_Profissional
version: 1
---

# PROFISSIONAIS ALOCADOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Perfis de profissionais* |
| **Situação/Requisito:** | *O sistema estava retornando um erro não tratado quando era feita a exclusão de um perfil de profissional* |
| **Solução/Implementação:** | *Foi identificado que o erro era causado em uma validação no momento da exclusão, o sistema tentava acessar uma linha que foi marcada para exclusão, assim retornando o erro, foi feito o ajuste para identificar o status da linha e não executar a validação que de fato não é necessária no momento da exclusão.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
