---
content_hash: eee9961a844f3f0d32b0db0c3a33031595df8fbeb159c1e68cdba21afb1492b8
fetched_at: '2026-06-29T00:09:16.155064+00:00'
page_id: '421385469'
product: rm
source: tdn-rm
title: Gerar Períodos conforme Planejamento do Cronograma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385469
version: 3
---

Para Gerar períodos conforme o planejamento do cronograma é necessário que o contrato possua um item associado e que este item tenha seu cronograma previsto cadastrado. Ao acionar o processo, são gerados períodos no contrato equivalentes aos períodos preenchidos no cronograma previsto e o campo "valor previsto" já virá preenchido com o valor lançado no cronograma.

Caso as datas de início/fim e periodicidade do contrato estiverem diferentes da periodicidade e datas início/fim dos períodos PREENCHIDOS no cronograma previsto será emitida mensagem de alerta "O contrato não está equivalente ao cronograma das tarefas contratadas." e "Deseja alterar o contrato e executar o processo?", ao executar o processo, é alterada a data de início e fim e a periodicidade do contrato para ficar igual ao cronograma. Caso os mesmos estejam iguais o processo ocorrerá normalmente.

O Cálculo do Valor Previsto do Período do Contrato é realizado da seguinte forma:

**= (Percentual Previsto x Valor Contratado) / 100 do cronograma.**

Caso haja mais de uma tarefa durante o período do contrato do cronograma, o valor total corresponderá à soma final de todas as tarefas nesse período.
