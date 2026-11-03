---
content_hash: bec6b70d64dc7ec07e15787970a6ae6861e0f5f4e110358f942605b3d7f05f69
fetched_at: '2026-06-29T00:12:00.030103+00:00'
page_id: '878909855'
product: rm
source: tdn-rm
title: 'Função de Fórmula: NDTRABPER2'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=878909855
version: 12
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Esta função calculará o número de dias que o funcionário deveria trabalhar considerando o seu horário, férias e afastamentos, porém, desconsiderando os feriados ocorridos dentro do período desejado de datas.

Sintaxe:  NDTRABPER2(Data, Data)

Quando o colaborador não utiliza cartão do ponto é verificado mesmo assim o sua jornada de trabalho conforme o horário vigente, porém não é considerado o descanso cadastrado no Grupo de descanso.

false

A função de fórmula verifica o horário do funcionário conforme o índice correspondente ao dia do mês, sendo de responsabilidade do usuário efetuar o cadastro das jornadas e informar o índice de horário/data base no cadastro do funcionário e/ou histórico de horário. Se um índice for trabalhado no sábado, será considerado como dia trabalhado, assim como um índice de descanso/compensado for segunda-feira será desconsiderado na contagem de dias trabalhados.  

## **02. EXEMPLO DE UTILIZAÇÃO**

NDTRABPER2('01/01/2023','31/01/2023')  
O sistema retornará o número de dias trabalhados do funcionário considerando o seu horário, férias e afastamentos, porém, desconsiderando os feriados ocorridos entre 01/01/2023 e 31/01/2023.

Considerando o colaborador com uma escala de trabalho semanal de 5 dias trabalhado, 1 dia compensado e 1 dia de descanso.

Cenário - Sem afastamento, férias ou feriado 

Considerando que no período do dia 01/01/2023 a 31/01/2023 não teve férias ou afastamento para o funcionário e nenhum feriado, será considerado 22 dias trabalhados, desconsiderando os dias de descanso e compensado:

Cenário - Com feriado

Considerando que no período do dia 01/01/2023 a 31/01/2023, onde existe 5 feriados em dias trabalhados conforme a escala de trabalho do colaborador:

Os feriados não forma considerados para abater de dias trabalhados:

Cenário - Com afastamento

**Afastamento iniciando na competência anterior e sem retorno**

Considerando que no período do dia 01/01/2023 a 31/01/2023, colaborador teve afastamento iniciando dia 29/12/2022 e sem retorno:

Retornou zero dias trabalhados:

**Com afastamento finalizando dentro do período informado**

Considerando que no período do dia 01/01/2023 a 31/01/2023, colaborador teve afastamento iniciando dia 29/12/2022 e com retorno dia 07/01/2023. Além dos  dias de descanso e compensado, foram desconsiderados 5 dias trabalhados que estão dentro do período de afastamento:

E retornou 17 dias:

Cenário - Com férias

Considerando que no período do dia 01/01/2023 a 31/01/2023, colaborador gozou de férias de 09/01/2023 a 19/01/2023:

A formula retornou 13 dias, pois desconsiderou 9 dias de férias que estavam compreendidos em dias trabalhados dentro da escala do horário do funcionário:

Cenário - Com férias, afastamento e feriado

Considerando que no período do dia 01/01/2023 a 31/01/2023 onde o colaborador teve férias, afastamento e possui ferido no calendário vinculado a sua seção:

Férias: 09/01/2023 a 19/01/2023

afastamento: 29/12/2022 a 07/01/2023

Calendário: com 5 feriados em dia de trabalho

A Fórmula retornou 8 dias, pois desconsiderou 9 dias de férias e 5 dias de atestado, além dos dias de descanso e compensado:

Cenário - Colaborador não bate ponto

Colaborador deixou de bater ponto a partir do dia 01/01/2023:

Retornou 8 dias, pois desconsiderou 9 dias de férias e 5 dias de atestado, além dos dias de descanso e compensado:

Cenário - Com grupo de descanso

Grupo de descanso criado com descanso programado para o dia 27/01/2023. O Colaborador foi associado ao Grupo de descanso:

Quando o colaborador utiliza o cartão de ponto, o dia de descanso cadastrado é abatido dos dias trabalhados. No cenário abaixo retornou 7 dias, pois além do dia de descanso do grupo de descanso, desconsiderou 9 dias de férias e 5 dias de atestado, além dos dias de descanso e compensado da jornada cadastrada no horário:

Quando o colaborador não utiliza o cartão de ponto, o dia de descanso cadastrado **não** é abatido dos dias trabalhados. No cenário abaixo retornou 8 dias, pois desconsiderou 9 dias de férias e 5 dias de atestado, além dos dias de descanso e compensado da jornada cadastrada no horário e não desconsiderou o dia de descanso do grupo de descanso:

## **03. TABELAS UTILIZADAS**

* GFORMULAS
* GCALENDARIO
* GFERIADO
* PFHSTAFT
* PFHSTHOR
* PFUNC
* PFUFERIASPER
* AHORARIO
* ATABFOLGA
