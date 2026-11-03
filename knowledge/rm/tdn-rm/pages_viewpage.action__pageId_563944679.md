---
content_hash: cd91ee08df8443234ecf216b98a7cdfc627adb23852d63f475128f91a8fda9e3
fetched_at: '2026-06-29T00:10:50.863953+00:00'
page_id: '563944679'
product: rm
source: tdn-rm
title: Plano de Contas (Ernst & Young)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563944679
version: 5
---

Através desse layout é possível extrair dados das contas contábeis que foram referenciadas no arquivo de lançamentos do diário. Essas informações irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young.

| ID | Formato | Tamanho | Dec | Descrição | Origem de Dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico | 200 |  | Código da Conta Contábil | Conta contábil existente na partida do lançamento contábil. | Essa informação está presente no arquivo de lançamentos do diário. |
| 2 | Alfanumérico | 200 |  | Descrição da Conta Contábil | Descrição da conta contábil existente na partida do lançamento contábil. |  |
| 3 | Alfanumérico | 200 |  | Código da Empresa | Código da coligada que deu origem ao lançamento contábil. | Essa informação está presente no arquivo de lançamentos do diário. |
