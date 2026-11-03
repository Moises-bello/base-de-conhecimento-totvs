---
content_hash: d2478b0ac8c1a0195aa5b31292578fb12e80d9574917dd2c10149425fcdb79e6
fetched_at: '2026-06-29T00:06:05.585999+00:00'
page_id: '201724737'
product: rm
source: tdn-rm
title: TSVOVL_DT_ERRO_Exibir_Data_Prevista_Devolucao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVOVL_DT_ERRO_Exibir_Data_Prevista_Devolucao
version: 2
---

# RENOVAÇÃO DE EMPRÉSTIMO (WEB)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Bibliotecária* |
| **Função:** | *Renovação de Empréstimo* |
| **Situação/Requisito:** | *Ao realizar uma renovação do Empréstimo, o campo Data de Devolução no formato (DD/MM/AAAA HH:MM) é informado para o usuário com o formato DD/MM/AAAA.* |
| **Solução/Implementação:** | *Ajustado o comportamento do sistema ao recuperar as informações da data prevista de devolução.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.41* |

Ao realizar uma renovação do Empréstimo, o campo Data de Devolução no formato (DD/MM/AAAA HH:MM) é informado para o usuário a data DD/MM/AAAA, porém, as horas HH:MM ficam zerados (00:00), ou seja, indica que o usuário que está renovando o empréstimo deve realizar a devolução no primeiro minuto do dia estipulado pelo sistema (quando esse processo é realizado pelo TOTVS Gestão Bibliotecária o respectivo campo é preenchidocorretamente pelo sistema).
