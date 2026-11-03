---
content_hash: f0b2e428cd545acceb8c875233454339e8559b888ab3f46ef992c3c28f51ace1
fetched_at: '2026-06-29T00:05:59.475741+00:00'
page_id: '191463467'
product: rm
source: tdn-rm
title: Cálculo de atestados médicos (Lei 13.135/2015)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=191463467
version: 2
---

|  |  |  |
| --- | --- | --- |
| Produto | : | Gestão de Folha de Pagamento |
| Processo | : | Cálculo da Folha de Pagamento |
| Subprocesso | : | Cálculo de Atestados Médicos |
| Data da publicação | : | 29/06/2015 |

Novas Regras – Benefícios Previdenciários

Foi publicado no DOU em 18/06/2015 a Lei nº 13.135/2015, disciplinando as novas regras para os benefícios previdenciários, dentre elas citamos:

. O retorno da obrigatoriedade ao empregador de pagar o salário ao empregado correspondente aos 15 primeiros dias consecutivos aos do afastamento da atividade por motivo de doença ou de acidente de trabalho ou de qualquer natureza;

Para consultar as alterações por completo acesse o link abaixo.

<http://www.planalto.gov.br/ccivil_03/_Ato2015-2018/2015/Lei/L13135.htm>

 

## Desenvolvimento/Procedimento

Foi criado o parâmetro “Data final do período em que o auxílio doença teve duração de 30 dias (MP 664)” para o usuário informar a data final que será de responsabilidade da empresa o pagamento de 30 (trinta) dias do afastamento por motivo de doença ou acidente de trabalho.   
O valor sugerido para esse parâmetro é “17/06/2015”, data anterior à publicação da Lei 13.135/205 que retornou o número de dias pagos pela empresa para 15 dias.   
  
Com isto passam a existir 3 cenários:

* Para afastamentos iniciados antes de 01/03/2015:

A empresa é responsável pelo pagamento de 15 dias de atestado médico.

* Para afastamentos iniciados no período entre 01/03/2015 até a data informada no novo parâmetro:

A empresa é responsável pelo pagamento de 30 dias de atestado médico.

* Para afastamentos iniciados a partir do dia seguinte ao informado no novo parâmetro:

A empresa é responsável pelo pagamento de 15 dias de atestado médico.

Ao calcular os dias de atestado médico/dias trabalhados a serem pagos pela empresa o produto seguirá os seguintes passos:   
1) Identificar a data de início do afastamento;   
2) Verificar em qual dos 3 cenários se encaixa o afastamento e obter o número de dias de atestado a ser pago pela empresa;   
3) No caso de afastamento pelo mesmo motivo dentro do período de carência, obter o número de dias já pagos pela empresa;   
4) Com as informações das datas do afastamento, e os valores obtidos nos itens 2 e 3 calcular o número de dias de atestado a ser pago pela empresa.

Estudo de casos:   
  
Caso 1:   
Funcionário com afastamento de 14 dias no mês de janeiro, com prorrogação do afastamento em 10 dias no mês de abril, totalizando 24 dias de atestado já pagos pela empresa.   
Funcionário tem nova prorrogação do afastamento em 20 dias, com data de início do afastamento antes da entrada em vigor da lei 13.135/2015, conforme imagem abaixo:   
  

Nesse caso, na data de início do terceiro afastamento a empresa é responsável pelo pagamento de 30 dias de atestado médico, como a empresa já havia pago 24 dias de atestado, ficará responsável pelo pagamento de mais 6 dias de atestado médico, completando assim os 30 dias, de acordo com a lei vigente na época.   
  
Caso 2:   
Funcionário com afastamento de 14 dias no mês de janeiro, com prorrogação do afastamento em 10 dias no mês de abril, totalizando 24 dias de atestado já pagos pela empresa.   
Funcionário tem nova prorrogação do afastamento em 20 dias, com data de início do afastamento após a entrada em vigor da lei 13.135/2015, conforme imagem abaixo:   
   
Nesse caso, na data de início do terceiro afastamento a empresa é responsável pelo pagamento de 15 dias de atestado médico, como a empresa já havia pago 24 dias de atestado, não será responsável pelo pagamento de nenhum dia de atestado.   
Um ponto a ser observado é que não existe nenhum tipo de estorno de dias de atestado a ser calculado nessa situação.
