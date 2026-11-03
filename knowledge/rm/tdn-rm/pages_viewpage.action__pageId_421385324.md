---
content_hash: 27c2e98f078c9302775f460687c3207ccabaedff6b8703177cb0492d5538447b
fetched_at: '2026-06-29T00:09:14.980188+00:00'
page_id: '421385324'
product: rm
source: tdn-rm
title: Desfaz a conversão para Preço Unitário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385324
version: 2
---

---

Este processo transforma um item de permanência rateado em um item de preço unitário.

O sistema irá gravar os dados de entrada (quais tarefas, percentual e critério de rateio) para que o processo de inversão da conversão para planilha de custo unitário seja possível. No processo de retorno para item de permanência, a composição original irá retornar como composição da tarefa e os itens de permanência serão ativados.

Será seguida uma ordem hierárquica para realizar o processo de inversão da conversão.

**Exemplo:**

Realizado o rateio da Tarefa 001.01.01 na Tarefa 001.01.02 e a Tarefa 001.01.02 na Tarefa 001.01.03.

Para realizar o processo inverso da conversão, deverá ser desfeito a conversão da Tarefa 001.01.02 depois a Tarefa 001.01.01.

---
