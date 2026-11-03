---
content_hash: f7d5b2162295173a91520d291927b392ad6ea8e2e3157a00b6df834fa79aadbc
fetched_at: '2026-06-29T00:05:48.863513+00:00'
page_id: '1032853579'
product: rm
source: tdn-rm
title: Contrato de Locação - Processo - Aplicar Regras Tributárias em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1032853579
version: 3
---

---

## 📌 O que esse processo faz?

Esse processo permite aplicar uma regra tributária de forma automática e em lote para vários contratos de locação ao mesmo tempo, evitando a necessidade de configurar contrato por contrato manualmente.

O usuário seleciona os contratos desejados, escolhe uma única regra tributária e o sistema se encarrega de aplicar essa regra somente onde for necessário.

---

## ⚙️ Como o processo funciona na prática?

1. O usuário acessa o **cadastro de contratos de locação** e seleciona **um ou mais contratos**.
2. O sistema exibe **apenas as regras tributárias disponíveis para a coligada** desses contratos.
3. O usuário escolhe a regra tributária desejada.
4. Ao executar o processo:

   * ✅ A regra é aplicada **somente aos contratos que ainda não possuem regra tributária**.
   * ⚠️ Contratos que **já possuem uma regra** não são alterados.
5. Durante a execução, o sistema registra todas as ações em um **log do processo**.

Mais informações acesse: [Cadastro de Regras Tributárias](https://tdn.totvs.com/pages/viewpage.action?pageId=939252927)
