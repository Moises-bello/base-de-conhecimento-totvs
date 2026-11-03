---
content_hash: 483232df6e17f86ff1d598225579de0d5179bb6c2ce1db2ed7d2e7d4553670c5
fetched_at: '2026-06-29T00:08:35.341128+00:00'
page_id: '279164590'
product: rm
source: tdn-rm
title: Função de Fórmula Encargos Reoneração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=279164590
version: 3
---

Para provisionar os valores de encargos de INSS de 13º salário referente ao período desonerados, foi criado duas funções de fórmulas, a saber :

VALENCARGO(mês, ano, CodEncargo): essa função retorna o valor de um encargo em uma data competência para o funcionário corrente;

VALPROVISAO13(mês, ano): essa função retorna o valor da provisão do 13º salário somado à média de 13º salário para o funcionário corrente.

Exemplo de cálculo usando as novas funções:

Para um dado funcionário com salário de R$ 1.200,00 e que o percentual de INSS é de 20% segue a tabela dos cálculos:

```
Observe que a partir de julho, quando a competência volta a ser 100% reonerada, o valor pode ser obtido pelo seguinte cálculo: 
```

Encargo em Jun + ((Prov 13º Jul - Prov 13º Jun) \* 20%).

Usando as novas funções de formula seria:

Exemplo de uso das novas funções de fórmula utilizando variáveis:
