---
content_hash: b2276ebaa952f2ed76af8d080ca80b1924afa5aef446d9b832cae1dfb829b31d
fetched_at: '2026-06-29T00:08:18.904615+00:00'
page_id: '266973725'
product: rm
source: tdn-rm
title: TVVQZY_DT_Informar_Data_De_Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266973725
version: 110
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Contabilização por competência* |
| **Situação/Requisito:** | *Ao gerar operações de estorno, pode ocorrer da data atual do sistema não refletir um data dentro do período em que se deseja fazer o ajuste, cujo o período contábil esteja aberto na contabilidade para este fim. Da mesma forma, pode ocorrer de um contrato não ter sido contabilizado para um determinado período e haver a necessidade de se contabilizar a competência para utilizando a data que o contrato deveria ter sido contabilizado, cujo o período esteja aberto na contabilidade.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de contabilização por competência de forma a permitir que durante a execução do processo de contabilização por competência, seja informada a data de contabilização dos lançamentos contábeis. A data não é obrigatória e caso não seja preenchida, as atuais regras continuam sendo respeitadas. Caso a data de contabilização seja informada e seja maior que a data atual do sistema, o sistema não permite a contabilização do contrato, emitindo mensagem  de erro.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.14* |
| **Versão Corrigida:** | *12.1.14* |
| **Versão Expedida:** | *12.1.14* |

divs
