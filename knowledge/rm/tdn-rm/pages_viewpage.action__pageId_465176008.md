---
content_hash: de7b2e234963948d688304ee6c8adfec4bd316c56a2caf34c111d59b5fab517d
fetched_at: '2026-06-29T00:10:15.783245+00:00'
page_id: '465176008'
product: rm
source: tdn-rm
title: Anexos (Tipos de Objeto de Manutenção)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465176008
version: 3
---

Esta tela permite inserir/editar o(s) produto(s) que poderá(ao) ser apropriados pelo(s) objeto(s) de manutenção do sub-modelo corrente.

**Código Produto**: Numero de identificação do Produto. A descrição do produto será automaticamente informada após a inserção do código do produto.

**Quantidade**: Quantidade máxima do produto que será apropriado pelo objeto de manutenção.

**Cód. Unidade**: Código da unidade de medida do produto

**Obriga Vida útil na OS**: Caso marcado o check box, cada vez que você inserir um item para um Tipo de Objeto/Modelo/Sub-Modelo na OS, e este item for um produto, será obrigado informar a vida útil do produto.

**% da vida útil**: Este campo usa como base a vida útil recomendada pelo fabricante e que deve ser informada em Opções | Parâmetros | Produtos/Serviços. Assim, deve ser informada a porcentagem de vida útil do produto para que seja trocado, ou seja, ao preencher o campo, o produto irá vencer quando atingir X% da vida útil recomendada pelo fabricante.  
***Observação***: Ao preencher o campo "%da vida útil" nesta tela o sistema passa a adotar para os objetos de manutenção do "Sub-Modelo" corrente a porcentagem da vida útil do produto informada nesta tela, desconsiderando o que foi parametrizado para o "Tipo de Objeto de Manutenção".

**Produto Apropriável Diretamente?**: Dá acesso aos campos que farão o controle de Apropriação Direta de Produtos. Mais detalhes no "Veja Também".

**Consumo médio**: Digite a quantidade média consumida deste produto. A quantidade destes campos a serem exibidos está relacionada à quantidade de Indicadores de Uso que você está utilizando. Por exemplo, se você usa Quilometragem e RPM, dois campos serão exibidos.

**Índice de Acompanhamento**: Defina qual Índice de Acompanhamento utilizar. Este Índice selecionado fará controle do consumo médio.  
***Observação***: Para que este campo seja exibido, é preciso marcar o check box "Apropriação Direta de Produto(s)?", na pasta identificação do Tipo de Objeto/Modelo/Sub-Modelo.

---
