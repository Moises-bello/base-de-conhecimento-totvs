---
content_hash: 8edf19b8fd5b03cd50ab75c343f5e702d5065c7e67221afbcd933cc4baaa34de
fetched_at: '2026-06-29T00:09:47.664889+00:00'
page_id: '435105041'
product: rm
source: tdn-rm
title: Seguro - Anexo - Despesa do Seguro
type: documentation
url: https://tdn.totvs.com/display/LRM/Seguro+-+Anexo+-+Despesa+do+Seguro
version: 9
---

Para que possa ser gerado os lançamentos financeiros das apólices de seguro, tanto de pagamento quanto de reembolso, é necessário que seja realizado a associação a uma despesa.   
Essa associação é realizada através do anexo "Despesa de Seguro", no qual só é permitido inserir apenas uma despesa por seguro.   
A despesa cadastrada através desse anexo terá o campo "Origem" preenchido com o valor "Seguro", e automaticamente será preenchido o campo "Seguro", com o seu respectivo código.   
   
**Restrições:**

* Se houver mais de um imóvel associado a apólice de seguro não será permitido a inclusão de mais despesa de seguro para a apólice de seguro. Será apresentada a seguinte mensagem ao usuário: "O seguro já possui despesa associada e não é possível criar mais de uma despesa por apólice".
* Quando o seguro tiver como origem **Imóvel**, se mais de um imóvel for associado a apólice não será permitido a geração de reembolso. o botão "Permite reembolso ficará desabilitado". Caso a apólice de seguro possua apenas um imóvel, a inclusão de reembolso será permitida. No caso de seguro com origem Contrato de Locação, mesmo se o contrato de locação tiver mais de um imóvel associado a ele, não existira restrição para geração de reembolso.

Observações

* O sistema permite somente o cadastro de uma despesa para cada Apólice de Seguro;
* O sistema somente permitirá a integração de uma despesa após a efetivação do Seguro.
Veja Também
