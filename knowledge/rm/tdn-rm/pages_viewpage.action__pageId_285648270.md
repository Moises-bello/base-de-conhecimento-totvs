---
content_hash: f2ae0ee04b8a00e8a472f982b1223b01c261c527e6638cf63d60086c3735344d
fetched_at: '2026-06-29T00:08:38.325401+00:00'
page_id: '285648270'
product: rm
source: tdn-rm
title: 865476 PORTALMOBILE01-540 DT Histórico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285648270
version: 101
---

# HISTÓRICO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Histórico |
| **Situação/Requisito:** | Ao entrar no portão do aluno e tentar acessar a funcionalidade de histórico, o sistema apresenta mensagem informando "Referência de objeto não definida para uma instância de um objeto". |
| **Solução/Implementação:** | Verificado que a inconsistência ocorria devido à falta de verificação de nulidade do objeto e por decorrência de tamanho do campo na tabela de histórico. |

divs
