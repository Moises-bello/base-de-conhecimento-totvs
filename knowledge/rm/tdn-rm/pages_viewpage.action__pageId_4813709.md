---
content_hash: 2275781b042f4251226c4ba91c6054969b05318692e4aa3560073df599ea05f0
fetched_at: '2026-06-29T00:10:19.449879+00:00'
page_id: '4813709'
product: rm
source: tdn-rm
title: Comprador não aparece no Assistente de Sugestão de Compras do Ressuprimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813709
version: 4
---

BLOCK

Comprador não aparece no Assistente de Sugestão de Compras do Ressuprimento

FAQ: **Comprador não aparece no Assistente de Sugestão de Compras do Ressuprimento**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.00 |

Sintoma

* **Sintoma**

Comprador não aparece no “*Assistente de Sugestão de Compras*” do Ressuprimento

Causa

* **Causas**

1. O Comprador não atende a opção definidas nos campos “Comprador Por[[1]](http://totvsconnect.blogspot.com/2010/10/dica-comprador-nao-aparece-no.html#_ftn1_4887)”e “Lista de Comprador” defino na etapa Movimentos de Sugestão dos parâmetros do Ressuprimento.
2. O Comprador cadastrado no cadastro de Funcionários **NÃO** é do tipo “Comprador” ou Comprador/Vendedor”.

---

[[1]](http://totvsconnect.blogspot.com/2010/10/dica-comprador-nao-aparece-no.html#_ftnref1_4887) - Este campo poderá ter os seguintes valores para seleção “Coligada, Filial, Local”, porem a apresentação dos mesmos irá depender do “Nível de Gestão” definido nos parâmetros da “Gestão de Estoque / Definições de Estoque / Nível de Gestão de Estoque.

Solução

* **Solução**

1- Se nos parâmetros do Ressuprimento estiver defino no campo “***Comprador Por***” como “***Coligada”***, deverá ser verificado se existe algum funcionário definido do tipo de “Comprador” ou “Comprador/Vendedor”.

2- Se nos parâmetros do Ressuprimento estiver defino no campo “***Comprador Por***” como “***Filial***”, deverá ser verificado se existe algum funcionário do tipo “Comprador” ou “Comprador/Vendedor” que seja da filial utilizada no Assistente de Sugestão de Compras.

3- Se nos parâmetros do Ressuprimento estiver defino no campo “***Comprador Por***” como “***Local de Estoque***”, deverá ser verificado se existe algum funcionário do tipo “***Comprador***” ou “***Comprador/Vendedor***” que seja do local de estoque do Assistente de Sugestão de Compras. Lembrando que até esta versão não é possível definir Local de Estoque para funcionário.

4- Se nos parâmetros do Ressuprimento estiver defino no campo “Lista de Comprador” como Produto, deverá se certificar que existe um funcionário definido como comprador dentro do cadastro do produto no anexo “Funcionários/Responsáveis”.

Observações

O documento em questão está postado no blog da Totvs e pode ser consultado através do link : <http://totvsconnect.blogspot.com/2010/10/dica-comprador-nao-aparece-no.html>
