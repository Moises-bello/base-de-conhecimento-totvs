---
content_hash: 9511fbb0395fca41384891198a04fb0bd0c3085e29553fcc5d822935f599c86d
fetched_at: '2026-06-29T00:09:23.912565+00:00'
page_id: '422546153'
product: rm
source: tdn-rm
title: Tag's Pessoa Física e Produtor Rural
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546153
version: 2
---

* **TAG <VALR\_AQZ\_PESSOA\_FISICA>** - Entradas Pessoa Física ou Não Contribuinte

Serão tratados os Lançamentos Fiscais de entrada de dentro do Estado do Espírito Santo.   
 Será somado o valor da mercadoria informado nos itens dos Lançamentos Fiscais ((Quantidade \* Preço) – Desconto) e produto selecionado = P (produto).  
 Neste caso, o Cliente/Fornecedor não poderá ser contribuinte do ICMS ou sua categoria deverá ser definida como "Pessoa Física" no cadastro de Cliente/Fornecedor.  
 O cálculo será desmembrado por código de município do Lançamento Fiscal e acrescentado ao Quadros de Detalhamentos - Item 3, preenchendo com o valor da mercadoria.

* **TAG <VALR\_PROD\_RURAL\_PROPRIA>** - Entradas do Estado do Espírito Santo

Serão considerados os lançamentos de entrada cujo CFOP seja do grupo 1.xxx e possua o campo Origem/Destino marcado como "Dentro do Estado". Além disso no cadastro do Cliente/Fornecedor do lançamento deve possuir o ramo de atividade Produtor Rural selecionado.  
 Será somado o valor da mercadoria informado nos itens dos lançamentos ((Quantidade \* Preço) – Desconto) e produto selecionado = P (produto).
