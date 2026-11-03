---
content_hash: 820360c924a35d35ba44a56fae18a238dde2141ab0be35ebebe05a95c464023a
fetched_at: '2026-06-29T00:09:28.560459+00:00'
page_id: '423938707'
product: rm
source: tdn-rm
title: Exemplo 2 - Transferência de Grupos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938707
version: 4
---

**Exemplos de transferências do tipo Origem -> Receptoras:**

Contas de origem:

      3.1.1.1.001 – Papelaria  
      3.1.1.1.002 – Material de Escritório

Conta de destino:

      2.3.1.2.001 – Apuração de Resultado do Exercício

Conta receptora de saldo a débito/crédito:

      2.3.1.2.002 – Lucro/Prejuízo do Exercício

Movimentações no valor de R$ 400,00 cada:

a) D - 3.1.1.1.001 – Papelaria (Conta Origem)  
    C - 1.1.1.1.001 – Caixa Filial Matriz

b) D - 3.1.1.1.002 – Material de Escritório (Conta Origem)  
    C - 1.1.1.1.003 – Caixa Filial Fortaleza

Lançamentos gerados pela transferência:

a) D - 2.3.1.2.002 - Lucro/Prejuízo do Exercício (Conta receptora de saldo a Débito/Crédito)  
    C - 3.1.1.1.001 - Papelaria => R$ 400,00

b) D - 2.3.1.2.002 - Lucro/Prejuízo do Exercício (Conta receptora de saldo a Débito/Crédito)  
    C - 3.1.1.1.002 - Material de escritório => R$ 400,00
