---
content_hash: 675ab227ccc557ea9beb3620aff807ce31454ae16aa453a5987c56c8d1421000
fetched_at: '2026-06-29T00:10:10.487313+00:00'
page_id: '452719851'
product: rm
source: tdn-rm
title: Vale Transporte - Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719851
version: 2
---

Esta etapa tem como objetivo definir algumas opções de como será feito o cálculo de vale transporte  
    
 **Parâmetros**  
 Utiliza Histórico de Compra de Vale Transporte  
 Com este parâmetro marcado é habilitado o menu 'Gerar Compra de Vale Transporte' que fica em Folha Mensal | Processos | Lançamentos. Através desse processo é possível Gerar a Compra de Vale Transporte e o valor Calculado é armazenado no histórico de compra de vale transporte associado ao funcionário. Quando é feito o lançamento da Folha mensal através do grupo de eventos com o parâmetro 'Lançar Vale Transporte' marcado, será considerado o valor Gerado nesse processo de compra de vale transporte para o Lançamento dos eventos de Código de Cálculo 32 e 104 e, não será considerado as informações do cadastro do funcionário. 

**Observação**  
 Caso o parâmetro esteja marcado, mas não foi executado o processo de compra de vale transporte, no lançamento do grupo de eventos com o parâmetro marcado 'Lançar Vale Transporte', será considerado os parâmetros informados no cadastro de funcionários.   
 O cálculo de desconto de vale transporte (evento de código de cálculo 6) irá considerar o salário e/ou eventos lançados que incidem em vale transporte e, a partir do valor encontrado é lançado no envelope de pagamento do funcionário até o limite do valor de entrega de vale transporte.

Utiliza Salário Nominal  
 Com este parâmetro marcado, será considerado para cálculo da faixa de desconto de vale transporte, apenas o salário base do funcionário, ou seja, o salário informado no cadastro de funcionário na aba Salário/Jornada, campo 'Salário Mensal'.   
 Com o parâmetro desmarcado, será considerado para desconto os eventos que tem incidência de Folha 'Vale Transporte' marcado(s).

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<< Retornar para **Folha de Pagamento**  
 Gerar Compra de Vale Transporte
