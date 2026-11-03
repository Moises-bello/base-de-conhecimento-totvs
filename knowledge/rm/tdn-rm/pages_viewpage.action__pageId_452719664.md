---
content_hash: c909a7eb0e3f62f432d5154476c4e7c27320fe4773daa7e9c7d9ddda27f5a516
fetched_at: '2026-06-29T00:10:09.422262+00:00'
page_id: '452719664'
product: rm
source: tdn-rm
title: Limite de Tolerância
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719664
version: 78
---

O limite de tolerância serve para limitar dentro do período, da semana ou do dia o número de vezes ou o número de horas que será aplicada a tolerância cadastrada no Horário por Intervalo, ou no sindicato. O mesmo deve ter um tipo de ocorrência associado e deve ser associado a um horário.  
  
**Tipo:** Diária - Limita a tolerância a ser aplicada no dia. Semanal - Limita a tolerância a ser aplicada na Semana. Período - Limita a tolerância a ser aplicada no Período.  
**Quantidade**: Número de vezes que será aplicada a tolerância, após atingir o valor informado não será mais aplicada a tolerância cadastrada nos Intervalos Planejados da Jornada.  
**Número de horas** : Número de horas que será aplicada a tolerância, conforme as formas de aplicação abaixo descritas.  
Forma de aplicar Tolerância - (Somente disponível quando preenchido o campo Número de horas)   
**Integralmente ou Nada**: Se o número de horas a tolerar ultrapassar o número de horas do limite de tolerância cadastrado, as horas não serão toleradas.  
**Parcialmente até o Limite**: Se o número de horas a tolerar ultrapassar o número de horas do limite de tolerância cadastrado, as horas a tolerar serão abatidas ao número de horas do limite de tolerância.

**Exemplo**:   
Intervalos Planejados da Jornada  
(Intervalos de Trabalho)  08:00 12:00 - 14:00 18:00

Tolerâncias para todas as batidas do intervalo planejado. Presença: 00:10 -Ausência: 00:10 Abater: 00:05 - Abater: 00:05.  
Funcionário executou as batidas: 08:05 11:55  14:05 17:55

* Cálculo com o Limite de Tolerância abaixo cadastrado e associado ao horário do funcionário.  
  Tipo: Diária Quantidade: 0   
  Número de Horas: 00:15  
  Parcialmente até o Limite   
  Será calculado 00:05 minutos de atraso, pois conforme os limites cadastrados foram tolerados 00:15 minutos.
* Cálculo sem Limite de Tolerância  
  Funcionário não terá atrasos, pois todos os minutos serão tolerados conforme tolerâncias cadastradas nos Intervalos Planejados da Jornada.

**Observações:**  
Para que seja considerada a extra de refeição no limite de tolerância vinculado ao horário do funcionário, será necessário incluir o Tipo de ocorrência ERN-Extra de Refeição Não autorizada.

Quando se utiliza valor no campo (Quantidade) maior que zero, será aplicada a tolerância da jornada, - o cálculo sempre irá tolerar por batida o número de horas definido na tolerância do horário -, nessa recorrência de vezes definida e verifica a cada recorrência se o numero de horas já tolerado ultrapassou o número de horas definido no campo (Número de horas). Desta forma enquanto não ultrapassou o número de horas, será aplicada a tolerância estabelecida no horário. A forma de aplicar tolerância, definida como integralmente ou nada está condicionada se ultrapassou o valor definido no campo número de horas.

**Exemplo1:**  
Intervalos Planejados da Jornada (Intervalos de Trabalho) 08:00 12:00 - 14:00 18:00. Tolerâncias para todas as batidas do intervalo planejado.  
Presença: 00:05 -Ausência: 00:05 Abater: 00:00 - Abater: 00:00.   
Funcionário executou as batidas: 07:53 - 12:00 - 14:00 - 18:03

* Cálculo com o Limite de Tolerância cadastrado e associado ao horário do funcionário.  
  Tipo: Diária Quantidade: 4  
  Número de Horas: 00:10 e Integralmente ou nada.  
  Será calculado 00:01 minutos de extras autorizada na entrada de 07:53 a 07:54,   
  Será tolerado 00:06 minutos 07:54 a 08:00.  
  Será tolerado 00:03 minutos 18:00 a 18:03.   
  No cenário acima como foi tolerado 00:09 minutos, caso existisse algum outro intervalo de 5 minutos de extras a ser tolerada nenhum intervalo seria tolerado pois ultrapassaria o número de horas definido no limite.

Quando estiver com a quantidade igual a zero, irá verificar todas as marcações da jornada planejada.

Será verificada a tolerância cadastrada em cada batida do horário e irá utilizar o campo "Numero de horas" para definir o limite.

**Exemplo 2:**

Intervalos Planejados da Jornada (Intervalos de Trabalho) 08:00 12:00 - 14:00 18:00. Tolerâncias para todas as batidas do intervalo planejado.  
Presença: 00:05 -Ausência: 00:05   
Funcionário executou as batidas: 07:55 - 12:00 - 14:00 - 18:00

* Cálculo com o Limite de Tolerância cadastrado e associado ao horário do funcionário.  
  Tipo: Diária Quantidade: 0  
  **Número de Horas: 00:10** e Integralmente ou nada.  
  Será tolerado 00:05 minutos 07:55 a 08:00.

**Exemplo 3:**

Intervalos Planejados da Jornada (Intervalos de Trabalho) 08:00 12:00 - 14:00 18:00 - 18:30 20:00. Tolerâncias para todas as batidas do intervalo planejado.  
Presença: 00:05 -Ausência: 00:05   
Funcionário executou as batidas: 07:55 - 12:00 - 14:00 - 18:00 - 18:35 - 20:00

* Cálculo com o Limite de Tolerância cadastrado e associado ao horário do funcionário.  
  Tipo: Diária Quantidade: 0  
  **Número de Horas: 00:10** e Integralmente ou nada.
* Será tolerado 00:05 minutos 07:55 a 08:00.
* Será tolerado 00:05 minutos 18:30 a 18:35.

**Exemplo 4:**

Intervalos Planejados da Jornada (Intervalos de Trabalho) 08:00 12:00 - 14:00 18:00 - 18:30 20:00. Tolerâncias para todas as batidas do intervalo planejado.  
Presença: 00:05 -Ausência: 00:05   
Funcionário executou as batidas: 07:55 - 12:00 - 14:05 - 18:00 - 18:35 - 20:05

* Cálculo com o Limite de Tolerância cadastrado e associado ao horário do funcionário.  
  Tipo: Diária Quantidade: 0  
  **Número de Horas: 00:20** e Integralmente ou nada.
* Será tolerado 00:05 minutos 07:55 a 08:00.
* Será tolerado 00:05 minutos 14:00 14:05.
* Será tolerado 00:05 minutos 18:30 a 18:35.
* Será tolerado 00:05 minutos 20:00 a 20:05.

Caso exista outra extra a ser tolerada **que ultrapasse os 20 minutos estipulados de limite**, nenhum intervalo seria tolerado.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Tipo da Ocorrência
