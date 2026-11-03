---
content_hash: b410f03a5004edb8234aed9984e94a3b177f7eade11d62d9fe41f38eb29d604f
fetched_at: '2026-06-29T00:10:09.969602+00:00'
page_id: '452719760'
product: rm
source: tdn-rm
title: Código de Cálculo 339 - Abono Férias Transferido para outra filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719760
version: 2
---

Evento Base de cálculo do tipo Valor e sem incidência.  
 Este evento é lançado automaticamente no movimento do funcionário demitido ao calcular uma rescisão por transferência com o parâmetro **"Transfere Movimentação do Mês Atual**"  marcado e quando existir eventos na movimentação mensal com data de pagamento no caixa anterior .  
 Neste caso a data de pagamento não será mais alterada para a data da transferência e será lançado  no movimento do funcionário demitido o **valor dos eventos de abono férias,1/3 abono, abono em dobro e 1/3 de abono em dobro**   (como base de cálculo) que foram movidos para a filial destino para que sejam considerados na DIRF da filial de origem do funcionário.  
    
**Exemplo:**  
 Período de gozo: 01.01.2014 a .20.01.2014   
 **Demissão(Transferência):** 21.01.2014  
 **Data de Pagamento das Férias**:30.12.2013  
    
 O sistema irá lançar no movimento do funcionário Demitido o evento com Código de cálculo 339 - ABONO FÉRIAS TRANSFERIDO PARA OUTRA FILIAL com data de pagamento **30.12.2013**.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
