---
content_hash: dee9c50d3d6568df82b42efc59cc1b17a50443250ce19d331f8c259be8ecdd88
fetched_at: '2026-06-29T00:10:11.094259+00:00'
page_id: '452719937'
product: rm
source: tdn-rm
title: Código de Cálculo 145 - Atestado Médico Afastado por Previdência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719937
version: 7
---

Este código é utilizado para o pagamento do atestado médico relativo aos primeiros quinze dias de afastamento pela previdência.   
É do tipo provento, podendo ser tipo hora ou dia, com porcentagem de incidência igual a 1,00.   
Este evento deve ser informado em Opções | Parâmetros | RM Labore | Parâm. Cálculo | Parâmetros, nos campos 'Evento para atestado médico (mensalista)' e/ou 'Evento para atestado médico (horista)'.

**Observações quando utiliza Cálculo .Net:**

1. Quando em Opções | Parâmetros | RM Labore | Parâm. Cálculo | Parâmetros o parâmetro 'Lança o evento de atestado médico via grupo de eventos' está desmarcado, o sistema somente lança o evento com código de cálculo 145 automaticamente, no momento do lançamento do evento com código de cálculo 1 ou código de cálculo 2.  
   
2. Retirado o parâmetro 'Soma dias afastados dentro período de carência pelo mesmo motivo' existente em Opções | Parâmetros | RM Labore | Parâm. Cálculo | Parâmetros. Não fica mais visível e o sistema verifica quantidade de dias de atestado pagos pela empresa de acordo com o período de carência e paga até um total de 15 dias.  
   
**Exemplo:**  
Período de carência 60 dias.  
   
**Período de afastamento         Qt dias             Tipo      Motivo**  
01/11/2009 a 10/11/2009              10                     P           3  
02/12/2009 a 03/12/2009              02                     P           3  
05/12/2009 a 09/12/2009              05                     P           3  
   
No exemplo acima o sistema paga 5 dias de atestado médico na competência 12, pois na competência 11 já foi pago 10 dias de atestado.

**Observação:** Caso exista o [código de cálculo 445 - ATESTADO MÉDICO COM INCIDÊNCIA SOMENTE SEGURADO](https://tdn.totvs.com/pages/viewpage.action?pageId=589761956) no movimento do funcionário o código de cálculo 145 não será lançado automaticamente. Caso seja necessário o lançamento dos dois códigos de cálculo simultaneamente, o código de cálculo 145 deverá ser lançado manualmente.

Códigos de Cálculo
