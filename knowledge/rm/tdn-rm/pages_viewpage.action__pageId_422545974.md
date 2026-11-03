---
content_hash: 0a810fe8d7c14bb4fc32cb4ea445602791393c12ca6b63cd633989f425d04a8f
fetched_at: '2026-06-29T00:09:22.112975+00:00'
page_id: '422545974'
product: rm
source: tdn-rm
title: 'Tributação do Movimento: Buscar Alíquota no Serviço'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545974
version: 4
---

Para empresas que tem várias alíquotas vinculadas a um código de receita o Tipo de Movimento pode ser configurado para realizar a busca de alíquota do Serviço. Para realizar essa configuração deve-se realizar o seguinte processo:

* Vincular um código de receita nos dados fiscais do cliente/fornecedor
* Vincular um tributo no Anexo tributo do produto
* Na parametrização do Tipo de movimento na Etapa 63, deve-se incluir o tributo informando no cadastro do produto,  não informando alíquota e código de retenção.
* No campo Buscar alíquota em: informar "Serviço".

Realizando esse processo ao incluir um movimento ele irá trazer para a alíquota informada no produto/serviço e a receita do cliente/fornecedor.  
O processo acima é para o tributo IRRF, para os outros tributos deve ser informado o código de receita no tributo ou no tipo de movimento.
