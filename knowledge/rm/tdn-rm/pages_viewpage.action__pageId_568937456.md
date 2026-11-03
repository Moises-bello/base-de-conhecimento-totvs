---
content_hash: 2044b12603fdd1518f2dcb37d67017f833b2ac5e350c3163f1bc5517ba2dcf7e
fetched_at: '2026-06-29T00:10:51.544110+00:00'
page_id: '568937456'
product: rm
source: tdn-rm
title: MP 936 - Fórmula de redução da jornada/salário considerando aumento salarial
  por dissídio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568937456
version: 4
---

*Diferença Salarial por Dissídio x Fórmula redução de jornada/salário*

Atenção :

Para utilização deste recurso no produto,  a empresa deverá avaliar com o seu jurídico se a interpretação da lei é  diferente do entendimento TOTVS.

Entendimento Consultoria Segmentos TOTVS.

A MP 936 convertida em Lei n° 14.020 , foi criada com o objetivo de preservar o emprego e renda dos trabalhadores, garantir as atividades empresariais e laborais, e reduzir os impactos sociais da calamidade pública decorrentes ao COVID-19.

A MP com a conversão da Lei não traz a questão do dissídio retroativo, dessa forma o entendimento é que ela veio flexibilizar algumas regras trabalhistas, e devemos nos atentar o que diz o artigo 471 da CLT.

Art. 471 - Ao empregado afastado do emprego, são asseguradas, por ocasião de sua volta, todas as vantagens que, em sua ausência, tenham sido atribuídas à categoria a que pertencia na empresa.

Link Consultoria TOTVS - 

Roteiro

Para que o aumento salarial por dissídio tenha reflexo no evento de desconto redutor de jornada,  o usuário poderá customizar a fórmula de desconto de redução conforme passo a passo abaixo :

1 - Crie um evento Diferença desconto jornada/salário reduzida do tipo Desconto e Valor

2 - Inclua no cadastro de Eventos , campo "Evento de Diferença de Salário",  o evento diferença desconto jornada/salário reduzido.

3 - Altere a linha abaixo na fórmula de de desconto de redução conforme abaixo :

DE

SETVAR (ValorReduzido,resultsql('BEM','VALORREDUZIDOBEM'));

PARA

SETVAR (ValorReduzido, (RC \* (resultsql('BEM','PERCENTUALREDUCAOBEM')/100)));

Pronto,  ao calcular a diferença salarial,  o valor de desconto redutor de jornada/salario refletirá o valor do aumento salarial da época para cada mês considerado no "Acordo".
