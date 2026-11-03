---
content_hash: b9c3f3b804b2eb615155620a77fee5d2a5aade3797d2bf193d796ef203eed838
fetched_at: '2026-06-29T00:11:48.885228+00:00'
page_id: '828854431'
product: rm
source: tdn-rm
title: Atestado/Afastamento - Cálculos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=828854431
version: 29
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros**
3. **Informações**

## **01. VISÃO GERAL**

Este documento tem como objetivo apresentar o comportamento do cálculo de dias de atestado/Afastamento com relação aos parâmetros disponíveis no parametrizador. Os parâmetros documentados estão em TOTVS Folha de Pagamento | Configurações | Parametrizador | 06.01 - Folha de Pagamento | 06.01.03 - Folha Normal | Afastamento 1/2.

## **02. PARÂMETROS**

Considera divisor pelo número de dias do mês na remuneração de funcionários com afastamento

Com este parâmetro marcado será considerando como divisor a quantidade real dos dias do mês em que o funcionário estiver afastado pela previdência, ou seja, com afastamento maior que 15 dias. Este parâmetro terá efeito para funcionário mensalista.

**Exemplo de Utilização com o** **parâmetro marcado**

Mês com 31 dias - Atestado < 15 dias

Funcionário com atestado de 3 dias no mês de Janeiro, logo o mesmo não foi afastado pela previdência:

No cálculo de dias trabalhados (CC2) e de atestado (CC145) foi considerado como divisor 30 dias:

Mês com 31 dias - Atestado > 15 dias

Funcionário com 16 dias de atestado. Neste caso a empresa paga os 15 primeiros dias e 1 dia é pago pela previdência:

No cálculo de dias trabalhados (CC2) e de atestado (CC145) foi considerado como divisor 31 dias:

Mês com 29 dias - Atestado < 15 dias

Funcionário com atestado de 3 dias no mês de Fevereiro, logo o mesmo não foi afastado pela previdência:

No cálculo de dias trabalhados (CC2) e de atestado (CC145) foi considerado como divisor 30 dias:

Mês com 29 dias - Atestado > 15 dias

Funcionário com 17 dias de atestado. Neste caso a empresa paga os 15 primeiros dias e 2 dia é pago pela previdência:

No cálculo de dias trabalhados (CC2) e de atestado (CC145) foi considerado como divisor 29 dias:

Mês com 29 dias - Atestado sem retorno

Funcionário com atestado iniciando dia 08/02 sem retorno. Neste caso a empresa paga os 15 primeiros dias e os demais dias foram pagos pela previdência:

No cálculo de dias trabalhados (CC2) e de atestado (CC445) foi considerado como divisor 29 dias:

Afastamento iniciando em Fevereiro e finalizando em Março - 15 dias de atestado

Colaborador tem 15 dias de atestado, iniciando dia 17/02 e finalizando dia 02/03, totalizando 15 dias:

Em Fevereiro, como foi o inicio do atestado e não tem afastamento pela previdência (Maior que 15 dias), considerou 17 dias trabalhados no mês:

E de atestado pagou 13 dias:

Em Março, como teve 2 dias de atestado sem afastamento pela previdência, foi pago 28 dias trabalhados:

E pago 2 dias de atestado médico:

Afastamento iniciando em Fevereiro e finalizando em Março - Atestado > 15 dias 

Colaborador com afastamento iniciando dia 17/02 e finalizando dia 07/03, com 20 dias de atestado:

Em fevereiro pagou 17 dias trabalhados, pois o mesmo não teve afastamento pela previdência em Fevereiro:

E 13 dias de atestado médico:

Em março pagou 23 dias trabalhados, pois 5 dias foi para previdência e 2 de atestado, totalizando 30 dias. Porém para calcular o salário dia usou como divisor 31, pois o mês de março tem 31 dias, parâmetro está marcado e o colaborador teve afastamento pela previdência em Março:

Da mesma forma usou como divisor 31 para calcular o atestado:

Afastamento iniciando em Fevereiro e com mais de 15 dias e finalizando em Março

Colaborador com afastamento iniciando dia 12/02 e finalizando dia 02/03:

Como houve mais de 15 dias de atestado dentro do mês de fevereiro, logo os dias que excedem aos 15 dias deveriam ser pagos pela previdência. Neste caso ele usa o como divisor os dias do mês na remuneração:

Assim também para o evento de atestado médico pago em fevereiro:

No mês de março, como teve 2 dias de afastamento pela previdência e sem pagamento de atestado, pois os 15 dias foram todos pagos em Fevereiro, os dias trabalhados foram calculados considerando 28 dias, porém usou como divisor para o salario dia 31 dias do mês, mediante ao parâmetro marcado:

**Exemplo de Utilização com o** **parâmetro desmarcado**

Mês com 31 - Atestado < 15 dias

Funcionário com atestado de 3 dias no mês de Janeiro, logo o mesmo não foi afastado pela previdência:

No cálculo de dias trabalhados (CC2) e de atestado (CC145) foi considerado como divisor 30 dias:

Mês com 31 - Atestado > 15 dias

Funcionário com 16 dias de atestado. Neste caso a empresa paga os 15 primeiros dias e 1 dia é pago pela previdência:

No cálculo de dias trabalhados (CC2) e de atestado (CC145) foi considerado como divisor 30 dias:

Mês com 29 - Atestado sem retorno

Funcionário com atestado iniciando dia 08/02 sem retorno. Neste caso a empresa paga os 15 primeiros dias e os demais dias foram pagos pela previdência:

No cálculo de dias trabalhados (CC2) e de atestado (CC445) foi considerado como divisor 30 dias:

Afastamento iniciando em Fevereiro e finalizando em Março - 15 dias de atestado

Colaborador tem 15 dias de atestado, iniciando dia 17/02 e finalizando dia 02/03, totalizando 15 dias:

Em Fevereiro, como foi o inicio do atestado e não tem afastamento pela previdência (Maior que 15 dias), considerou 17 dias trabalhados no mês:

E de atestado pagou 13 dias:

Em Março, como teve 2 dias de atestado sem afastamento pela previdência, foi pago 28 dias trabalhados:

E pago 2 dias de atestado médico:

Afastamento iniciando em Fevereiro e finalizando em Março - Atestado > 15 dias 

Colaborador com afastamento iniciando dia 17/02 e finalizando dia 07/03, com 20 dias de atestado:

Em fevereiro pagou 17 dias trabalhados, pois o mesmo não teve afastamento pela previdência em Fevereiro e foi considerado como divisor para o salário dia 30 dias:

E 13 dias de atestado médico também considerando como divisor 30 dias:

Em março pagou 23 dias trabalhados, pois 5 dias foi para previdência e 2 de atestado, totalizando 30 dias. Porém para calcular o salário dia usou como divisor 30, pois o  parâmetro está desmarcado:

Da mesma forma usou como divisor 30 para calcular o atestado:

Afastamento iniciando em Fevereiro e com mais de 15 dias e finalizando em Março

Colaborador com afastamento iniciando dia 12/02 e finalizando dia 02/03:

Como houve mais de 15 dias de atestado dentro do mês de fevereiro, logo os dias que excedem aos 15 dias de atestado deveriam ser pagos pela previdência. Como o parâmetro está desmarcado, o cálculo considera 30 dias como divisor para o cálculo do salário dia do mês:

Assim também para o evento de atestado médico pago em fevereiro:

No mês de março, como teve 2 dias de afastamento pela previdência e sem pagamento de atestado, pois os 15 dias foram todos pagos em Fevereiro, os dias trabalhados foram calculados considerando 28 dias e considerou como divisor para o salario dia 30 dias do mês, mediante ao parâmetro desmarcado:

Independente do parâmetro 'Considera divisor pelo número de dias do mês na remuneração de funcionário com afastamento' sempre será considerado o mês comercial (30 dias) para o cálculo de dias trabalhados para mensalistas.IMPORTANTE!

## **03. INFORMAÇÕES**

[Orientações Consultoria de Segmentos - Salário Proporcional – Cálculo nos Meses de 28, 29 ou 31 dias – Empregado Mensalista](https://tdn.totvs.com/pages/releaseview.action?pageId=631324291)
