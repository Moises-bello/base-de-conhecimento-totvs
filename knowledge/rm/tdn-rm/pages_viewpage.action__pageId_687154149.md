---
content_hash: ff00cf41d9624cda42dba77c2befcc8a7afdc6e753e3cce400ccd98bfe6da2d1
fetched_at: '2026-06-29T00:11:20.587106+00:00'
page_id: '687154149'
product: rm
source: tdn-rm
title: Lançar feriados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687154149
version: 6
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. ****Tela Cálculo de Produção Agrária****
   1. **Principais Campos e Parâmetro**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Nesse parâmetro será lançada a tarefa de cálculo para o feriado, de acordo com o calendário associado a seção do funcionário, na linha de produção quando não existe produção, afastamento, férias. A verificação do feriado também considerará o horário planejado do funcionário quando tiver integração com o sistema de Automação de ponto.

No parametrizador / Folha Agrária / Parâmetros da Filial / Cálculo devem ser preenchidos os parâmetros “Tarefa para feriado normal” e “Tarefa para feriado em dobro”.

**Observações:**

01 - Se não houve registro de tarefa de produção dentro do período global de apuração não poderá gerar uma linha de ‘Feriado Normal’

02 - Quando o funcionário tem falta durante o período global, o sistema deve inibir qualquer lançamento de feriado Normal. Por exemplo, no período de 01 a 31/05/2021 teve uma falta no dia 17/05/2021 e tinha dois feriados normais sem pagamento de produção, então seria lançado o evento de feriado normal nos dois dias, mas como teve a falta não será pago nenhum feriado.

03 - Quando houver registro de tarefa de produção no dia do feriado, deverá ser somada todas as tarefas do dia de feriado (independente se é produção ou não, como por exemplo Complementos e pausas) e lançado na tarefa de feriado em dobro.

## **02. EXEMPLO DE UTILIZAÇÃO**

01 - Funcionário com horário de segunda a sexta com descanso sábado e domingo

Feriados cadastrados

* 14/05/2021 - sexta-feira
* 15/05/2021 - sábado
* 19/05/2021 - quarta-feira

Não existia produção lançada para o funcionário para esses dias, então foi lançado tarefa de feriado para os dias 14/05 e 19/05 que eram trabalhados de acordo com o horário planejado e não foi lançado no dia 15/05 que era folga do funcionário de acordo com o horário planejado.

02 – Funcionário com horário de sábado a quarta com descanso quinta e sexta

Feriados cadastrados

* 14/05/2021 - sexta-feira
* 15/05/2021 - sábado
* 19/05/2021 - quarta-feira

Não existia produção lançada para o funcionário, então foi lançado tarefa de feriado para os dias 15/05 e 19/05 que eram trabalhados de acordo com o horário planejado e não foi lançado no dia 14/05 que era folga do funcionário de acordo com o horário planejado.

03 - Funcionário com os seguintes valores pagos em dia de feriado:

**Produção Agrária (05/05/2022 - Feriado):**

| Nome da Tarefa | Tarefa | Quantidade | Horas |
| --- | --- | --- | --- |
| COMPLEMENTO | 90279 | 1,0000 | 00:00 |
| PAUSAS | 90304 | 1,0000 | 00:30 |
| DESCAR MANUAL | 90317 | 1.008,00 | 01:00 |
| REC PLANT MANUAL | 90319 | 0,5455 | 01:00 |
| FERIADO EM DOBRO | 90339 | 1,0000 | 00:00 |

Valores calculados **(Cálculo da produção)**:

| Data Produção | Tarefa | Nome tarefa | Valor |
| --- | --- | --- | --- |
| 05/05/2022 | 90279 | COMPLEMENTO | 2,5600 |
| 05/05/2022 | 90304 | PAUSAS | 1,8837 |
| 05/05/2022 | 90317 | DESCAR MANUAL | 19,5552 |
| 05/05/2022 | 90319 | REC PLANT MANUAL | 26,5477 |
| 05/05/2022 | 90339 | FERIADO EM DOBRO | 46,1100 |

Valores lançados no envelope **(Lançamento da Produção para a Folha)**:

| Evento | Descrição | Ref. | Valor |
| --- | --- | --- | --- |
| 90304 | PAUSAS | 4,00 | 5,5244 |
| 90279 | COMPLEMENTO | 1,00 | 2,5600 |
| 90339 | FERIADO EM DOBRO | 1,00 | 54,1873 |
| 90319 | REC PLANT MANUAL | 0,5455 | 26,5477 |
| 90317 | DESCAR MANUAL | 1.008,00 | 19,5552 |

Observação: Veja que o valor da tarefa 90339 - FERIADO EM DOBRO é a soma de todos os valores do dia, até mesmo complemento e pausas que não são tarefas de produção.

04 - Funcionário com os seguintes valores pagos incluindo em dia de feriado (Lançamento do valor da diária em dia de feriado):

**Produção Agrária:**

| Nome da Tarefa | Data da produção | Horas | Quantidade | Valor ganho |
| --- | --- | --- | --- | --- |
| **xxxxx TAREFA DIÁRIA** | **01/05/2021** | **02:00** | **0,2365** | **29,8400** |
| xxxxx TAREFA DIÁRIA | 02/05/2021 | 02:00 | 0,2365 | 29,8400 |
| xxxxx TAREFA DIÁRIA | 04/05/2021 | 02:00 | 0,2365 | 29,8400 |
| xxxxx TAREFA DIÁRIA | 05/05/2021 | 02:00 | 0,2365 | 29,8400 |
| xxxxx TAREFA DIÁRIA | 06/05/2021 | 02:00 | 0,1050 | 13,2500 |
| xxxxx TAREFA DIÁRIA | 07/05/2021 | 06:00 | 1.0000 | 126,1600 |
| xxxxx TAREFA DIÁRIA | 08/05/2021 | 02:00 | 0,2365 | 29,8400 |
| xxxxx TAREFA DIÁRIA | 10/05/2021 | 02:00 | 0,2365 | 29,8400 |
| xxxxx TAREFA DIÁRIA | 11/05/2021 | 02:00 | 0,2365 | 29,8400 |
| **xxxxx TAREFA DIÁRIA** | **21/05/2021** | **02:00** | **0,2365** | **29,8400** |
| xxxxx TAREFA DIÁRIA | 27/05/2021 | 02:00 | 0,2365 | 29,8400 |
| xxxxx TAREFA DIÁRIA | 28/05/2021 | 02:00 | 0,2365 | 29,8400 |
| xxxxx TAREFA DIÁRIA | 29/05/2021 | 02:00 | 0,2365 | 29,8400 |
| xxxxx TAREFA DIÁRIA | 31/05/2021 | 02:00 | 0,2365 | 29,8400 |

**Soma de todas as tarefas, inclusive do feriado (29,84+29,84+29,84+29,84+13,25+126,16+29,84+29,84+29,84+29,84+29,84+29,84+29,84+29,84 ) = 497,48**

Valores lançados no envelope **(Lançamento da Produção para a Folha)**:

| Evento | Descrição | Ref. | Valor |
| --- | --- | --- | --- |
| 0102 | DESCANSO SEMANAL REMUNERADO | 0,00 | 58,24 |
| 7003 | EVENTO SEM CÁLCULO INTERNO | 0,00 | 80,00 |
| 7004 | EVENTOS DEPENDENTE DE OUTRAS TAREFAS | 1,00 | 112,91 |
| **7771** | **EVENTO PARA LANÇAMENTO DA DIÁRIA** | 0,00 | **497,48** |
| 7772 | EVENTO PARA LANÇAR PREÇO INFORMADO | 0,24 | 10,64 |
| 9079 | FERIADO | 0,00 | 47,31 |
| 9279 | COMPLEMENTO | 0,00 | 1.453,47 |
| 9979 | FERIADO EM DOBRO | 0,00 | 29,84 |

Observação:  Veja que no EVENTO PARA LANÇAMENTO DA DIÁRIA, foi lançado o valor de R$497,48, que corresponde a todas as tarefas de diária, inclusive a de feriados.

## **03.** **TELA Cálculo de Produção Agrária**

**Principais Campos e Parâmetro**

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Selecione a quebra de seção |
| Seleção de Funcionários | Filtrar funcionários |
| Período | Período para o cálculo |
| Parâmetro | Lançar feriados |

## **04. TABELAS UTILIZADAS**

* + PPRODUCAOAGRARIA
