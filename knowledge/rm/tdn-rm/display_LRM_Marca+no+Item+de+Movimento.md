---
content_hash: 3092bd9de3b59588d9586f2082804c310ef7ad3204a7f896dc97e0d1a4d8adb3
fetched_at: '2026-06-29T00:09:25.255472+00:00'
page_id: '423938081'
product: rm
source: tdn-rm
title: Marca no Item de Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Marca+no+Item+de+Movimento
version: 2
---

Se trata de um campo para exibição da Marca informada no cadastro de produto. Serão filtradas apenas as marcas definidas no anexo de marcas do produto.   
 A exibição deste campo respeita a o parâmetro Edita Marca no tipo de movimento.  
 O comportamento de Default para o campo Marca no Item de Movimento será aplicado nos seguintes processos:

* **Inclusão de Movimento:** caso o parâmetro Edita Marca por Tipo de Movimento for diferente de Não Edita, deve-se buscar a marca definida no cadastro de Produto.
* **Faturamento de Movimento:** caso o parâmetro Edita Marca por Tipo de Movimento for diferente de Não Edita, deve-se copiar a informação de marca do item de movimento origem. Caso o Tipo de movimento esteja parametrizado para agrupar quantidades de itens repetidos, será adotado o comportamento já existente no sistema, ou seja, o primeiro item a ser agrupado será utilizado como base. Sendo assim a todos os itens serão agrupados e a marca que prevalecerá será a do primeiro item.
* **Cópia de Movimento a partir de Outro**
* **Cópia por Referência**
* **Cópia de  Movimento a partir de Itens não Cotados**

***Observação**:* Não será possível informar uma marca inativa na inclusão/edição de um item de movimento.
