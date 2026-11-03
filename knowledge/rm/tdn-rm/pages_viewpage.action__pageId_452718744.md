---
content_hash: 8e8e776df6511baf0f46b67f8492a9ca494f79dc9eeefda94849d25951204264
fetched_at: '2026-06-29T00:10:01.464293+00:00'
page_id: '452718744'
product: rm
source: tdn-rm
title: CÓDIGO DE CÁLCULO - 355 PRIMEIRA PARCELA 13° TRANSFERIDA PARA OUTRA FILIAL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718744
version: 1
---

**CÓDIGO DE CÁLCULO - 355 PRIMEIRA PARCELA 13° TRANSFERIDA PARA OUTRA FILIAL**

---

Provento do tipo valor.  
   
Foi criado um novo código de cálculo para levar para a chapa ativa no momento da transferência o valor pago no evento de CC 9.  
   
   
O evento com o CC 355 será inserido na movimentação do funcionário ATIVO somente se NÃO for marcado o parâmetro ''transferir movimento do mês atual'' no momento da transferência, pois caso esse parâmetro seja marcado ele já irá realizar o procedimento que sempre realizou, de levar as informações para a chapa ativa.  
   
No cálculo do CC 355 - ADIANTAMENTO PRIMEIRA PARCELA 13º SALÁRIO, será lançado o valor do CC 9, caso seja encontrado no ano corrente.  
   
Observação: A regra acima se aplica apenas para transferência do tipo 5, pois a do tipo 6 se trata de uma ''rescisão'' realizada na transferência e que nesse caso os eventos são calculados conforme uma rescisão.
