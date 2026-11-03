---
content_hash: b35e173e6dfbf768823f3421f84bcb6bb4b6cfade7b0eea24a0d8a0d4cf62d88
fetched_at: '2026-06-29T00:09:58.873545+00:00'
page_id: '452718226'
product: rm
source: tdn-rm
title: Código de Cálculo 337 - INSS Férias Transferido Para Outra Filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718226
version: 2
---

Evento Base de cálculo do tipo Valor e sem incidência.  
 Este evento é lançado automaticamente no movimento do funcionário demitido ao calcular uma rescisão por transferência com o parâmetro **"Transfere Movimentação do Mês Atual**"  marcado e quando existir eventos na movimentação mensal com data de pagamento no caixa anterior .  
 Neste caso a data de pagamento não será mais alterada para a data da transferência e será lançado  no movimento do funcionário demitido **o valor do evento INSS de férias**  que foram movidos para a filial destino para que sejam considerados na DIRF da filial de origem do funcionário.

**Exemplo:**  
 **Período** **de gozo**: 01.01.2014 a 20.01.2014  
 **Demissão(Transferência):** 21.01.2014  
 **Data de Pagamento das Férias**:30.12.2013  
    
 O sistema irá lançar no movimento do funcionário Demitido o evento com Código de cálculo 337 - INSS FÉRIAS TRANSFERIDO PARA OUTRA FILIAL com data de pagamento **30.12.2013**.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
