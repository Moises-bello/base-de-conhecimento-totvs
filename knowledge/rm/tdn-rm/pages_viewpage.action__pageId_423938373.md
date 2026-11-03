---
content_hash: 4209429961f16c076ef7473a38b3c8b766628d041aec9c680ed1e307fc8ca03d
fetched_at: '2026-06-29T00:09:26.694916+00:00'
page_id: '423938373'
product: rm
source: tdn-rm
title: Alíquota Fixa Diferencial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938373
version: 3
---

Há determinados itens em que a alíquota é fixa, como é o caso de itens da construção civil por exemplo. É possível definir no sistema quando o item de orçamento da cotação vai trabalhar com alíquota diferencial fixa ou não.

Para isso, o parâmetro da cotação "Permite Alíquota Fixa Diferencial" precisa estar marcado em [Ambiente | Parâmetros  | Gestão de Estoque, Compras e Faturamento | Gestão de Compras | Cotação no passo Definições Gerais 2/4](http://tdn.totvs.com/pages/viewpage.action?pageId=423938121).

Com o sistema devidamente parametrizado, ao acessar a tela para informar o orçamento do item da cotação, será exibido a opção **"Alíquota Fixa Diferencial"**, onde o usuário poderá marca-la para indicar que a alíquota do item será fixa ou deixar desmarcada para indicar que a alíquota não será fixada.

Ao se marcar essa opção, o sistema irá entender que a Alíquota é fixa e portanto não haverá Diferencial de ICMS nessa cotação.  Deixando a opção desmarcada o sistema irá calcular normalmente o Diferencial de ICMS de acordo com os outros parâmetros da Cotação (Estado, Margem ICMS, etc).

**Exemplo 1:**

**Valor do Campo ICMS/ISS:**  12,00%

**Valor do Campo Alíquota da tabela DALIQINTERESTADUAL para os Estados envolvidos:** 18,00%

**Alíquota****Fixa Diferencial:** Desmarcado

**Diferencial de ICMS :** 1,06

**Exemplo 2:**

**Valor do Campo ICMS/ISS:**  12,00%

**Valor do Campo Alíquota da tabela DALIQINTERESTADUAL para os Estados envolvidos:** 18,00%

**Alíquota****Fixa Diferencial:** MARCADO

**Diferencial de ICMS :** 1 (ou seja, sem diferencial)
