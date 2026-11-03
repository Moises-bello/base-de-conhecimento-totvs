---
content_hash: 9a3d89772fc1d3ff5048c7243a4e60b010a948919126ab2e13ac44fc9b5b72b7
fetched_at: '2026-06-29T00:09:28.558674+00:00'
page_id: '423938706'
product: rm
source: tdn-rm
title: Exemplo 1 - Transferência de Grupos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938706
version: 4
---

**Exemplos de transferências do tipo Origem -> Destino -> Receptoras**:

Contas de origem:

      3.1.1.1.001 – Papelaria  
      3.1.1.1.002 – Material de Escritório

Conta de destino:

      2.3.1.2.001 – Apuração de Resultado do Exercício

Conta receptora de saldo a débito/crédito:

      2.3.1.2.002 – Lucro/Prejuízo do Exercício

Movimentações no valor de R$ 400,00 cada:

a) D - 3.1.1.1.001 - Papelaria (Conta Origem)  
    C - 1.1.1.1.003 - Caixa Filial Fortaleza

b) D - 3.1.1.1.002 - Material de Escritório (Conta Origem)  
    C - 1.1.1.1.001 - Caixa Filial Matriz

Lançamentos gerados pela transferência:

a) D - 2.3.1.2.001 – Apuração de Resultado do Exercício (Conta Destino)  
    C - 3.1.1.1.001 – Papelaria =>R$ 400,00.

b) D - 2.3.1.2.001 – Apuração de Resultado do Exercício (Conta Destino)  
    C - 3.1.1.1.002 – Material de Escritório => R$ 400,00.

c) D - 2.3.1.2.002 – Lucro/Prejuízo do Exercício (Conta Receptora de saldo a débito)  
    C - 2.3.1.2.001 – Apuração de Resultado do Exercício (Conta Destino) => R$ 800,00.
