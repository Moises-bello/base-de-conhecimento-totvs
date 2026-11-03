---
content_hash: c1ac0409ca3183a1c993bd19e3314315c022e82aeb34014865264023d4ff2860
fetched_at: '2026-06-29T00:09:21.085441+00:00'
page_id: '422545805'
product: rm
source: tdn-rm
title: Lucro Real por Estimativa
type: documentation
url: https://tdn.totvs.com/display/LRM/Lucro+Real+por+Estimativa
version: 8
---

O Lucro Real por Estimativa é devido mensalmente e efetivamente pagos no ano-calendário.  Na apuração pela estimativa utiliza-se a receita bruta, o cálculo segue as mesmas características do Lucro Presumido. Para a correta apuração por Estimativa deve ser seguido os seguintes passos:

1) Primeiramente deve ser criado os tributos IRPJ e CSLL com a periodicidade mensal, que serão vinculados aos eventos de Lucro Real por Estimativa e ao de Lucro Real;

2) Serão criados dois Eventos Tributários, um com a forma de tributação Lucro Real - Estimativa, onde o valor dos tributos serão calculados mensalmente. Para a apuração anual deve ser criado um segundo evento onde a forma de tributação será do tipo Lucro Real. Ambos devem ter vigências vinculadas;

3) Deve ser criado período de apuração mês a mês de Janeiro à Dezembro onde serão consideradas as Regras Tributárias do Evento por Estimativa;

4) Para apurar o Lucro Real Anual, faz necessário a criação de apenas um período de apuração com periodicidade anual, tendo a  data inicial 01/01/XXXX  e data final 31/12/XXXX, onde serão acumulados todos os valores apurados mês a mês através da Estimativa.

***Atenção!***A correta apuração dessa forma de tributação só ocorrerá se o parâmetro **"Cálculo Acumulativo"** estiver habilitado.

***Observações*:** Os pagamentos mensais podem ser suspensos ou reduzidos desde que demonstrados através da elaboração de balanço ou balancetes de suspensão ou redução, que o valor do imposto devido no período em curso, é igual ou inferior à soma do imposto devido por estimativa até o mês anterior àquele a que se refere o balanço ou balancete levantado. Caso haja Levantamento de Balanço/Balancete de Suspensão/Redução no intervalo da apuração do Lucro Real por Estimativa, deve-ser criar um novo evento com as Regras Tributárias devidamente parametrizadas e também a vigência corresponde ao período onde ocorrerá o levantamento de balanço. Neste evento as Regras Tributárias apresentadas serão idênticas ao do Lucro Real.

Os clientes que apuram o IRPJ/CSLL pelo Lucro Real Anual, devem cadastrar os tributos IRPJ e CSLL com periodicidade mensal. Entretanto, o sistema permitirá criar um Período anual. Este período só pode ser encerrado se todos os períodos mensais estiverem encerrados.

que compõem a Apuração.

---
