---
content_hash: 1715e58e8318618bd4a267160951c68ca4aa8494e43a9c462c53f97263f311c8
fetched_at: '2026-06-29T00:10:10.003883+00:00'
page_id: '452719779'
product: rm
source: tdn-rm
title: Concluir Requisição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719779
version: 3
---

**Concluir Requisição**

O objetivo desta funcionalidade é permitir a alteração do status da requisição para "Concluída", além do registro da data de conclusão.

Somente requisições "Em andamento" ou "Aprovadas" podem ser concluídas.

Ao executar o processo "Concluir Requisição", e a requisição possuir progressões relacionadas, o sistema terá o seguinte comportamento:

* Possuindo apenas uma progressão, o processo irá efetivar a progressão e também irá concluir a requisição.
* Possuindo mais de uma progressão, o processo irá efetivar apenas a próxima progressão e não irá concluir a requisição, pois a requisição só pode ser concluída depois de todas as progressões efetivadas. No caso de ser a última progressão, o processo irá efetivar a progressão e também irá concluir requisição.

**Observação:**

Para as requisições de Alteração de Dados Funcionais e Transferência com Alteração de Dados Funcionais é apresentado uma tela para que seja definida a data da efetivação da requisição.
