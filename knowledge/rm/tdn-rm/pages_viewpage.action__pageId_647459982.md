---
content_hash: 9477e077a92905a1674a843e152a93255fd5ed2ef7ad18dd06c923a1138b3d6e
fetched_at: '2026-06-29T00:11:11.502114+00:00'
page_id: '647459982'
product: rm
source: tdn-rm
title: EXEMPLO LANÇAMENTO CC 29 – INSS Outro Emprego
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=647459982
version: 2
---

Lançamento de evento com código de cálculo 72 – Base de INSS Outro Emprego no envelope de pagamento onde já exista o evento de salário normal.

O evento de CC29 será calculado primeiro nas faixas de INSS quando o cálculo do INSS for executado.

Validando o valor no esocial – o retorno do governo fica igual ao calculado pelo sistema.

**Observação:** Pelo cálculo do eSocial o retorno é apenas nos valores da empresa, o valor retornado pelo Outro Emprego será na outra empresa. Também pelo cálculo do eSocial o valor será truncado, talvez haja divergência no teto descontado do funcionário.

**Consideração para lançamento de múltiplos vínculos e eventos de outro emprego junto:**

Os lançamentos devem seguir uma ordenação quando há lançamento de outro emprego junto com múltiplos vínculos, ou seja:

* Se for lançado no primeiro vínculo deve lançar folha e outro emprego e depois lançar folha do outro vinculo
* Se for lançado no segundo vínculo deve lançar folha do primeiro vinculo e depois folha e outro emprego no segundo vínculo

Não deve lançar as folhas dos dois vínculos e depois lançar outro emprego no primeiro vinculo porque ficará inconsistente.
