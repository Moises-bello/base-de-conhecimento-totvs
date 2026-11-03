---
content_hash: f4b136507c54e9408f0cc9fa6e80a42aabf027e483634653629b3300f5e41fc3
fetched_at: '2026-06-29T00:09:50.184625+00:00'
page_id: '435105431'
product: rm
source: tdn-rm
title: Reorganizador de Vencimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Reorganizador+de+Vencimentos
version: 2
---

**Reorganizador de Vencimentos**

Esta opção, permite ao usuário re-organizar as datas de vencimento das parcelas após a geração do plano.  
 O usuário poderá re-organizar suas parcelas dando-lhes prioridades e incrementos, entre os componentes geradores de parcela, ou seja, componentes do tipo principal. Com o objetivo de não colocar mais de uma percela em um mesmo mês.  
 Parcelas geradas por componentes com mesma prioridade poderão ter datas de vencimento coincidentes.   
 Todos os componentes do tipo principal terão prioridade inicial 0, isto é, o sistema permite (comportamento padrão) a coincidência de datas de vencimento para qualquer componente.   
 Componentes com prioridade menor terão suas parcelas geradas primeiro e, caso exista uma parcela coincidente, será aplicado um incremento em meses para respeitar a configuração efetuada.   
 Parcelas com juros Price não podem ter o vencimento alterado. Parcelas pagas não serão alteradas.  
    
 Também é possível alterar a numeração das Notas Promissórias de acordo com a nova data de vencimento.   
 No campo "Reordenação do número de duplicatas", temos as seguintes opções:  
 **Padrão:** Nesta opção, o sistema irá numeras as notas de acordo com a configuração definida na venda.  
 **Por Grupo:** Nesta opção, o sistema irá numeras as notas agrupando-as parcelas de mesmo grupo..  
 **Geral:** Nesta opção, o sistema irá numeras as notas agrupando todas as parcelas da venda.
