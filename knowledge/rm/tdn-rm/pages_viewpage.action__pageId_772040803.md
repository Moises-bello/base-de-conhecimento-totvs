---
content_hash: 725a72c0cda1f5fa3e04d3e03fa588b6c7d927757c7ee4983c69ca5510c8bb9f
fetched_at: '2026-06-29T00:11:36.463422+00:00'
page_id: '772040803'
product: rm
source: tdn-rm
title: 'Função de Fórmula: NDTRABPXMES'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772040803
version: 40
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Função de Fórmula que retorna o número de dias que o funcionário deverá trabalhar no próximo mês conforme calendário, afastamento, férias, admissão, demissão, aviso prévio e histórico de horário.

Sintaxe: NDTRABPXMES

## **02. EXEMPLO DE UTILIZAÇÃO**

Estando na competência 03/2023, foi executado a função retornando o dias trabalhados da competência 04/2023 conforme os cenários abaixo:

Horário atual, Horário Futuro, Afastamento com retorno, Afastamento sem retorno, Calendário, Admissão próximo mês, Mudança de Horário após dia 01, Férias, Demissão, Aviso Préviopasso1,passo2,passo3,passo4,passo5,passo6,passo7,passo8,passo9,passo10yespasso1

Funcionário possui o horário abaixo com Jornada de 7 dias sendo 5 dias trabalhado e 2 dias de descanso/compesado:

Ao executar a fórmula, retornou 20 dias trabalhados:

nopasso2

Funcionário possui o horário abaixo com Jornada de 7 dias sendo 5 dias trabalhado e 2 dias de descanso/compesado informado no cadastro de funcionário, porém a data da mudança do horário está para 01/05/2023.

Ao executar a fórmula, retornou 30 dias trabalhados, pois considerou o horário anterior conforme o histório. E neste horário estava configurada somente uma jornada de 1 dia trabalhado:

nopasso3

Funcionário com afastamento iniciando dia 30/03/2023 e finalizando dia 03/04/2023 e com o horário com Jornada de 7 dias sendo 5 dias trabalhado e 2 dias de descanso/compesado:

A Função de fórmula irá considerar 19 dias trabalhados, desconsiderando o dia 03/04 na contegem de dias trabalhados, pois os dias 01 e 02 de Abril não são considerando como trabalhados conforme o horário do funcionário:

Outro cenário apresentado é quando o funcionário possui mais de um afastamento no mesmo mês, são somandos os dias de afastamento e desconsiderados nos dias trabalhados. Neste cenário o funcionário ainda está com o horário 0001 apresentado acima, com Jornada de 7 dias sendo 5 dias trabalhado e 2 dias de descanso/compesado:

nopasso4

Funcionário com 2 afastamentos, sendo o ultimo sem retorno e com o horário com Jornada de 7 dias sendo 5 dias trabalhado e 2 dias de descanso/compesado:

A Função de fórmula irá considerar 6 dias trabalhados, desconsiderando o dia 03/04 e a partir do dia 12/04 na contegem de dias trabalhados, pois os dias 01 e 02 de Abril não são considerando como trabalhados conforme o horário do funcionário:

nopasso5

No calendário vinculado a seção do funcionário foi cadastrado o fériado nacional do dia 07/04/2023:

A Função de fórmula irá considerar 5 dias trabalhados, desconsiderando o dia 03/04 pois os dias 01e 02 de Abril não são considerando como trabalhados conforme o horário do funcionário, o dia 07/04 pois é feriado e a partir do dia 12/04 na contegem de dias trabalhados:

nopasso6

Funcionário com admissão para o dia 10/04/2023 e com o horário com Jornada de 7 dias sendo 5 dias trabalhado e 2 dias de descanso/compesado:

A Função de fórmula retornou 15 dias trabalhados, pois começou a contar a partir do dia 10/04 e desconsiderou os dias de descanso/compensando do horário do funcionário:

nopasso7

O Horário do funcionário foi alterado no dia 05/04:

O horário 0020 só tem uma jornada e é trabalhada.

O horário 0001 com Jornada de 7 dias sendo 5 dias trabalhado e 2 dias de descanso/compesado:

O funcionário tem um afastamento sem retorno iniciando dia 12/04:

E tem um feriado no dia 07/04:

Executando a fórmula retornou 8 dias, pois foi considerado 4 dias (de 01 a 04 de abril) do horário 0020, sendo o dia 01 e 02 trabalhado conforme a jornada do horário 0020 e 4 dias do horário 0001 (dia 05, 06, 10 e 11), desconsiderando os dias 07 (Fériado), 08 (compensado), 09 (descanso) e a partir do dia 12 (afastamento sem retorno):

nopasso8

Funcionário com férias marcadas, finalizando dia 05/04:

Funcionário possui o horário com Jornada de 7 dias sendo 5 dias trabalhado e 2 dias de descanso/compesado, retornando 20 dias trabalhados de acordo com o índice de horário/Data Base:

E também tem um fériado no dia 07/04:

Ao executar a fórmula, retornou 16 dias, pois foi desconsiderado 3 dias de férias e 01 dia de fériado dos dias trabalhados do horário:

nopasso9

Funcionário com demissão cadastrada e calculada para o dia 14/04:

Funcionário possui o horário com Jornada de 7 dias sendo 5 dias trabalhado e 2 dias de descanso/compesado, retornando 20 dias trabalhados de acordo com o índice de horário/Data Base:

E também tem um fériado no dia 07/04:

Ao executar a fórmula, retornou 9 dias, pois foi desconsiderado como trabalhado a partir do dia 15/04 e 01 dia de fériado dos dias trabalhados do horário:

falseAtenção

Só é desconsiderado os dias após a data de demissão/cálculo se a rescisão estiver **calculada**.

nopasso10

Funcionário com aviso prévio trabalhado finalizando dia 18/04:

Funcionário possui o horário com Jornada de 7 dias sendo 5 dias trabalhado e 2 dias de descanso/compesado, retornando 20 dias trabalhados de acordo com o índice de horário/Data Base:

E também tem um fériado no dia 07/04:

Retornou 11 dias, pois foi desconsiderado como trabalhado a partir do dia 19/04 e 01 dia de fériado dos dias trabalhados do horário:

Dica

A função de fórmula verifica o horário do funcionário conforme o indice correspondente ao dia do mês, sendo de responsabilidade do usuário efetuar o cadastro das jornadas e informar o índice de horário/data base no cadastro do funcionário e/ou histórico de horário. Se um índice for trabalhado no sabado, será considerado como dia trabalhado, assim como um índice de descanso/compensado for segunda-feira será desconsiderado na contagem de dias trabalhados.

## **03. TABELAS UTILIZADAS**

* GFORMULAS
* GCALENDARIO
* GFERIADO
* PFHSTAFT
* PFHSTHOR
* PFUNC
* PFUFERIASPER
