---
content_hash: b78cb6bb55f151966370f3197a60d63708aa5a400ace0ad383af1e80fc8c3407
fetched_at: '2026-06-29T00:08:05.276934+00:00'
page_id: '235592320'
product: rm
source: tdn-rm
title: TUHKDX_DT_ATUALIZACAO_RNT
type: documentation
url: https://tdn.totvs.com/display/LRM/TUHKDX_DT_ATUALIZACAO_RNT
version: 120
---

# RNT - REGISTRO DAS NECESSIDADE DE TREINAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Cadastro de RNT |
| **Situação/Requisito:** | Ao realizar o fechamento de uma avaliação de conhecimento, sem informar a data de expiração (tanto no parametrizador, quanto manualmente), o sistema não atualiza o registro de RNT com a turma de treinamento que o funcionário participou. |
| **Solução/Implementação:** | Verificado que o sistema realizar a seleção dos registros a partir da data de expiração, para os casos em que não seja informada, o sistema irá trazer os registros anteriores a data d e encerramento da avaliação de conhecimento e atualizá-los com turma. |
| **Chamados relacionados:** | TUHKDX; TUSXR9 |

divs
