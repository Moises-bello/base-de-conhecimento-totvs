---
content_hash: a74e7e9adac427200969ef62fc779f706537bb1f14c5850c818a9503c517d46e
fetched_at: '2026-06-29T00:08:28.953130+00:00'
page_id: '271873588'
product: rm
source: tdn-rm
title: 551460 MEDU-2821 DT Excluir Certificado vinculado à livro de registro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271873588
version: 107
---

# CERTIFICADO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Atividades Acadêmicas* |
| **Função:** | *Diplomação/Certificado* |
| **Situação/Requisito:** | *Não era permitido excluir certificado vinculado à um livro de registro. Emitia mensagem de erro na chave* ForeignKeyConstraint SCertificado\_SRegistroLivro |
| **Solução/Implementação:** | Alterado comportamento do sistema para permitir excluir Certificado que esteja vinculado à um livro de registro. Caso tenha participantes incluído neste certificado, deverá ser excluído primeiro os participantes. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
