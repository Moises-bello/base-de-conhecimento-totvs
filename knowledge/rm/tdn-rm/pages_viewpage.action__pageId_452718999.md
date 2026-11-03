---
content_hash: 66d4cdf7f3bc38f5cda9e81811f6cce525cc885f329498c695e73874ae25bd7f
fetched_at: '2026-06-29T00:10:03.088728+00:00'
page_id: '452718999'
product: rm
source: tdn-rm
title: Horários Alternativos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718999
version: 19
---

Este módulo permitirá o cadastro de um horário alternativo que possibilita ao funcionário efetuar um horário diferente do horário normal. O sistema não calculará extras e atrasos se efetuar o seu horário alternativo. Este horário alternativo torna-se útil para realizar alterações de horário eventuais.  
**Observações:**  
Em dias com ausência de batidas, o sistema irá considerar o horário normal do funcionário para calcular a falta.  
O horário alternativo não pode conter índice/jornada  de descanso/compensado, para que  sistema considere os dias descanso e compensado apenas do horário padrão. O sistema só irá considerar o horário alternativo para os dias em que o funcionário tem jornada a cumprir com base no horário padrão (Para alterar o comportamento vide : ) .  
Para saber qual horário alternativo o funcionário utilizará no dia, o sistema tratará o horário alternativo verificando qual a primeira batida feita pelo funcionário mais se aproxima do seu horário e dos seus horários alternativos. Deste modo, avaliará por proximidade e menor interseção qual horário a considerar para o cálculo.

**Exemplo:**  
Horário do funcionário: [08:00 12:00] [14:00 18:00]  
Horário alternativo 1:    [07:00 11:00] [13:00 17:00]  
Horário alternativo 2:    [12:00 18:00]

Batidas do funcionário: 05/10 08:05 12:00 14:01 18:06  
Horário Considerado:              08:00 12:00 14:00 18:00

Batidas do funcionário 06/10: 07:20 11:10 14:00 17:38  
Horário Considerado:              07:00 11:00 13:00 17:00

Batidas do funcionário 07/10: 07:35 11:30 13:30 17:48  
Horário Considerado:              08:00 12:00 14:00 18:00

Batidas do funcionário 08/10:  11:00 17:00  
Horário Considerado:               12:00 18:00

Caso os horários tenham tolerância para presença estas são consideradas para calcular a proximidade.  
**Exemplo com tolerância de 10 minutos para presença na primeira batida e 10 minutos para presença para a ultima batida da jornada:**

Horário padrão do funcionário:

[08:00 12:00] [14:00 18:00]  com a tolerância será considerado : [07:49 12:00] [14:00 18:11]

Horário alternativo 01:

 [07:00 11:00] [13:00 17:00]  com a tolerância será considerado : [06:49 11:00] [13:00 17:11]

Horário alternativo 02:

 [12:00 18:00]  com a tolerância será considerado : [11:49 18:11]

Batidas do funcionário 05/10:  08:05 12:00 14:01 18:06  
Considerado horário padrão:   [08:00 12:00] [14:00 18:00]

Batidas do funcionário 06/10:  07:20 11:10 14:00 17:38   
Considerado horário padrão:   [08:00 12:00] [14:00 18:00]

Batidas do funcionário 07/10:  07:25 11:30 13:30 17:48  
Considerado horário padrão:   [08:00 12:00] [14:00 18:00]

Batidas do funcionário 08/10:  07:35 11:30 13:30 17:48  
Considerado horário padrão:   [08:00 12:00] [14:00 18:00]

Batidas do funcionário 09/10:  07:15 11:30 13:30 17:48  
Considerado horário alternativo 01:  [07:00 11:00] [13:00 17:00]

Batidas do funcionário 10/10:  11:00 17:00  
Considerado horário alternativo  02:  [12:00 18:00]

Importante

**São levadas em consideração somente as tolerâncias de presença para definir qual horário deve ser considerado para o cálculo.**

**Exemplo de aproximação:**

* Horário oficial : 07:30 - 12:00 - 13:00 - 17:30  - Com tolerância de presença de 10 minutos será considerado : [07:19 12:00] [13:00 17:30]
* Horário alternativo : 08:00 - 12:00 - 13:00 - 18:00 - Com tolerância de presença de 10 minutos será considerado : [07:49 12:00] [13:00 18:00]

Batidas do funcionário: 07:40 - 17:38

Neste caso a marcação tem uma diferença de 9 minutos em relação ao horário alternativo e de 21 minutos em relação ao horário oficial.

O horário que tiver a menor diferença é usado no cálculo, ou seja, no caso acima se aproxima do horário alternativo.

Nos casos onde a diferença for igual em ambos os horários, o horário oficial é selecionado.

Parâmetro :  **Horário Alternativo Noturno:**

Quando este parâmetro está habilitado, é considerado o índice alternativo para o dia que iniciou a jornada e o dia seguinte. Desconsiderando qualquer jornada que seria iniciada no no dia seguinte, mesmo que as batidas registradas correspondam a jornada do próprio horário alternativo.

**Exemplo:**

*Horário do funcionário:*

    [08:00 12:00] [14:00 18:00]

*Horário alternativo:*

    [21:00 +02:00] [+03:00 +06:00]

*Resultado:*

    dia 01/11/2022:  Horário do funcionário: [08:00 12:00] [14:00 18:00]

    dia 02/11/2022 : Horário alternativo:       [21:00 +02:00] [+03:00 +06:00]

    dia 03/11/2022:  (Desconsidera a jornada planejada)

    dia 04/11/2022: Horário do funcionário:  [08:00 12:00] [14:00 18:00]
