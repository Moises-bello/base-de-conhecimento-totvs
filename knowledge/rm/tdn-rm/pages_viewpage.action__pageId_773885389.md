---
content_hash: 2663f192cae46fe0b0d695a4d7139dea750aee5e211f41526751e6254bed2a7a
fetched_at: '2026-06-29T00:11:36.938382+00:00'
page_id: '773885389'
product: rm
source: tdn-rm
title: 'TCGI - Comissão - Metas - 2ª Forma: Recalcular Comissão'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773885389
version: 6
---

Para utilizar o cálculo do prêmio meta direto no valor da comissão durante o lançamento da comissão padrão, as regras da modalidades devem ter o **tipo de valor** como **fórmula** percentual ou fórmula valor, conforme a regra abaixo

Na fórmula foi implemento que: se os subordinados do diretor venderem no mínimo:

* 2 unidades para o empreendimento 27 e;
* 1 unidade para o empreendimento 28.  
  + A comissão total será de 2%, sendo que 1% da comissão padrão e  1% do prêmio por ter alcançado a meta
  + Se não atingir a meta, o valor será apenas de 1% da comissão

Após os ajustes das regras e das fórmulas com as metas de cada comissionado/função, o sistema irá calcular os valores de acordo com a performance de vendas lançadas na competência da comissão.

Ao final de cada mês, todas as comissões do mês deverão ser recalculadas e seus valores serão alterados de acordo com a faixa da meta. Nesse opção, a comissão **NÃO** pode estar integrada.

Não utilizar a geração da meta associada ao mesmo comissionado para não pagar a meta duplicada.

Veja o log da comissão recalculada para a meta do diretor que a meta foi atingida e definido o percentual de 2%

O log da fórmula mostra ainda que o empreendimento 27 teve três vendas e o 28 uma venda.

Se quiser conferir as vendas realizadas para o comissionado na competência da comissão, basta editar o item da comissão e clicar no menu vertical Comissões Relacionadas, onde será apresentado todas as comissões que este comissionado participou na competência da data da comissão
