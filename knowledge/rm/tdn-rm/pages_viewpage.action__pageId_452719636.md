---
content_hash: 365826f0a992d2db1265ed770ea4ca9ecf3cc7e6be37965acf9a52849043759d
fetched_at: '2026-06-29T00:10:09.343936+00:00'
page_id: '452719636'
product: rm
source: tdn-rm
title: Código de Cálculo 336 - IRRF Férias Transferido Para Outra Fialial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719636
version: 3
---

Evento Base de cálculo do tipo Valor e sem incidência.   
 Este evento é lançado automaticamente no movimento do funcionário demitido ao calcular uma rescisão por transferência com o parâmetro **"Transfere Movimentação do Mês Atual**"  marcado e quando existir eventos na movimentação mensal com data de pagamento no caixa anterior .  
 Neste caso a data de pagamento não será mais alterada para a data da transferência e será lançado  no movimento do funcionário demitido o **valor do evento de IRRF de férias** que foram movidos para a filial destino para que sejam considerados na DIRF da filial de origem do funcionário.  
    
**Exemplo:**  
 **Período de gozo**: 01.01.2014 a 20.01.2014   
 **Demissão(Transferência):** 21.01.2014  
 **Data de Pagamento das Férias**:30.12.2013  
 O sistema irá lançar no movimento do funcionário Demitido o evento com Código de cálculo 336 - IRRF FÉRIAS TRANSFERIDO PARA OUTRA FILIAL com data de pagamento **30.12.2013**.  
    
 **Observação:**  
 Caso existam eventos de folha de pagamento com data de pagamento anterior à data de admissão do novo registro do funcionário mas com o mesmo mês caixa, a data de pagamento desses eventos continuará sendo alterada para a data de admissão do novo registro, nesse caso, o cálculo do IRRF de folha não é afetado uma vez que o mês caixa de pagamento não é alterado.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
