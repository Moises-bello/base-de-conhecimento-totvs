---
content_hash: bbc903e996a17dc46339d4fc5375f5ea08c1bf0bfabf1c31d7f337c74deb032d
fetched_at: '2026-06-29T00:09:49.449286+00:00'
page_id: '435105295'
product: rm
source: tdn-rm
title: Imóvel - Processo - Associar Seguros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105295
version: 4
---

Para usar o modulo de seguro integrado com o modulo de aluguel, se faz necessário que a apólice de seguro esteja associado pelo menos à um imóvel.  
Lembrando que uma apólice de seguro pode estar vinculado a mais de um imóvel, assim como um imóvel pode estar associada a várias apólices de seguro.  
Este processo possibilita a realização da associação de um ou mais seguros a um ou mais imóveis. Pode ser executado tanto na visão de Imóveis quanto na de Seguro.

**Figura 1 - Tela do processo de associação de Seguro e Imóvel**

Temos os seguintes campos:

* **Selecione as apólices de seguro:** Nessa grid é possível selecionar as apólices de seguros, no qual se deseja associar aos imóveis selecionados na grid "Selecione os imóveis". Nessa grid é possível incluir e excluir os registros, conforme desejado.
  + **Observação:** Caso o processo tenha sido executado na visão de Seguros, essa grid virá preenchida com os registros selecionados na visão.
* **Selecione os imóveis:** Nessa grid é possível selecionar os imóveis, no qual se deseja associar as apólices de seguro selecionadas na grid "Selecione as apólices de seguro". Nessa grid é possível incluir e excluir os registros, conforme desejado.
  + **Observação:** Caso o processo tenha sido executado na visão de Imóveis, essa grid virá preenchida com os registros selecionados na visão.

**Restrições:** Se já houver despesa de seguro vinculada ao imóvel selecionado não será permitido associar imóvel ao seguro. Será apresentada a seguinte mensagem ao usuário: "A apólice do seguro não poderá ser associada a novos imóveis pois já possui despesa cadastrada".  
 **Observação:** Para que o processo possa ser executado, é necessário que nas grid's citadas acima ,contenha pelo menos uma apólice de seguro e um imóvel.

As associações realizadas podem ser visualizadas através dos seguintes anexos:

* **Imóveis:** Este é um anexo da apólice de Seguro, onde é exibido todos os imóveis que estão associados ao mesmo. Nesse anexo é possível excluir a associação do Imóvel ao Seguro.
* **Seguros:** Este é um anexo do Imóvel, onde é exibido todos as apólices de Seguro que estão associadas ao mesmo. Nesse anexo é possível excluir a associação do Imóvel ao Seguro.

Veja Também

---
