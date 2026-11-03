---
content_hash: 2da38ff822414d7a24ffc7e3e4bdcd3ecda56503d09684e4dda61312ee5f1aba
fetched_at: '2026-06-29T00:09:20.118263+00:00'
page_id: '422545670'
product: rm
source: tdn-rm
title: Cenários Atividade Rural
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545670
version: 3
---

**1º Cenário - Lucro/Lucro**

No caso das duas atividades processarem lucro, os Grupos que compõem a parte A do Lalur serão processados em sua totalidade para as duas atividades  
 (Resultado Contábil, Adições do Lucro, Adições por Doação, Exclusões do Lucro e Compensação de Prejuízos).   
 O Lucro Real do período, ou seja, a base de cálculo do tributo será o somatório dos dois lucros. De posse desse valor, o sistema deve continuar a apuração do tributo,  
 apurando os Grupos de Adicionais, Deduções e Compensações do Tributo do evento "pai".

**2º Cenário - Lucro/Prejuízo**

Quando a atividade **geral** obtiver lucro e a atividade **rural** prejuízo, este poderá ser compensado em sua totalidade com o primeiro, limitado ao valor do lucro. Neste caso, o  
 Grupo de Compensação de Prejuízos do evento da atividade rural não deve ser processado uma vez que não há lucro dessa atividade para compensação.   
 Se o lucro da atividade geral for maior que o prejuízo da atividade rural, o Lucro Real do período, ou seja, a base de cálculo do tributo, será o lucro da atividade geral  
 subtraído do prejuízo da atividade rural. O sistema continua a apuração, processando os Grupos de Adicionais, Deduções e Compensações do Tributo do evento "pai".   
 Entretanto, se o prejuízo da atividade rural for maior que o lucro da atividade geral, a compensação daquele prejuízo deve ficar limitado ao valor do lucro e, neste caso, interrompe-se,  
 também, o cálculo do evento tributário "pai", ou seja, a Compensação de Prejuízos anteriores não será realizada em nenhuma das atividades. O prejuízo residual da atividade  
 rural deve ser controlado na Parte B do Lalur para compensação nos períodos de apuração subsequentes.   
 ***Atenção!*** Na apuração pelo lucro real anual, o prejuízo só é enviado para a Parte B no ajuste anual.

**3º Cenário - Prejuízo/Prejuízo**

Apurando prejuízo nas duas atividades, a apuração é interrompida e os valores devem ser registrados em contas da parte B do Lalur para compensação em períodos de apuração posteriores.   
 ***Atenção!*** Na apuração pelo lucro real anual, o prejuízo só é enviado para a Parte B no ajuste anual.

**4º Cenário - Prejuízo/Lucro**

Este cenário é inverso ao apresentado no 2º caso. A atividade geral apura prejuízo e a rural, lucro. O prejuízo da primeira pode ser compensado com o lucro da segunda, limitada  
 ao valor do lucro. Se o prejuízo exceder o valor do lucro da atividade rural, interrompe-se a apuração no período e o prejuízo residual da atividade geral deve ser  
 controlado na Parte B do Lalur para compensação nos períodos de apuração subsequentes.   
 Se o lucro da atividade rural for maior, então a apuração continua sendo, o Lucro Real do período, ou seja, a base de cálculo do tributo, o lucro da atividade rural subtraído  
 do prejuízo da atividade geral. Em seguida, deve-se processar os Grupos de Adicionais, Deduções e Compensações do Tributo do evento "pai".
