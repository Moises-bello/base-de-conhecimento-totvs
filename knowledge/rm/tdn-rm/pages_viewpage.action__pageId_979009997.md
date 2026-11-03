---
content_hash: b53d0e351a3c857b58950cc4c8d7e888ffa434124896b62bb0ef07685bf7ea6e
fetched_at: '2026-06-29T00:12:15.419868+00:00'
page_id: '979009997'
product: rm
source: tdn-rm
title: Diferenças entre as funções NDTRAB e NJTRAB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=979009997
version: 1
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Mais Informações**

## **01. VISÃO GERAL**

Existem diferenças entre as funções NDTRAB e NJTRAB, embora ambas estejam relacionadas à jornada de trabalho. A função NDTRAB é mais utilizada em processos administrativos ou operacionais, para cargos com carga horária fixa, como controle de frequência mensal e cálculo de vale-transporte proporcional por dias úteis. Já a função NJTRAB é mais utilizada no Módulo Educacional, especialmente para professores, pois considera a quantidade de aulas/jornadas efetivamente atribuídas ao docente, sendo fundamental quando o docente tem aulas diferentes em dias distintos e o pagamento é feito com base em aulas ministradas.

## **02. EXEMPLO DE UTILIZAÇÃO**

Um funcionário possui 15 dias trabalhados conforme o histórico de horário da jornada de trabalho. Mas as funções estão retornando valores diferentes: NJTRAB = 5 e NDTRAB = 25

O que cada função está retornando no seu caso:

|  |  |  |
| --- | --- | --- |
| Função | Valor | Explicação |
| NJTRAB | 5 | Considera apenas os dias com jornada atribuída (como aulas ou turnos específicos) — típico para professor ou regime de carga horária parcial. |
| NDTRAB | 25 | Considera o número de dias úteis do mês, independentemente do que foi efetivamente trabalhado. |

Mas por que o RM está mostrando esses valores?

* A função NJTRAB está consultando a quantidade de "jornadas atribuídas" no contrato, geralmente para cargos de carga horária variável (ex: professores).
* Já o NDTRAB está consultando o calendário do colaborador (ou tabela de dias úteis) e não o ponto ou jornada real registrada.

O ponto mostra 15 dias com marcações reais, mas o sistema não usa o ponto diretamente nessas funções — a menos que estejam integradas as tabelas de jornada do Ponto com o contrato (o que geralmente não ocorre de forma direta).

**Mas e o que pode ser feito para resolver isto?**

#### 1. Rever a jornada contratada (PJORNADA)

Verifique se a jornada semanal está definida corretamente no contrato do colaborador. Se estiver usando um tipo de contrato com jornada variável (ex: professores), o sistema pode estar entendendo que ele só tem 5 dias previstos.

#### 2. Verificar a tabela de escalas e os dias atribuídos

O NJTRAB depende da escala atribuída ao colaborador, e não do que está no ponto. Use a tela de escalas atribuídas (RH ou Educacional) para ver se só 5 dias estão previstos como jornadas válidas.

#### 3. Se quiser calcular com base no ponto efetivo (os 15 dias com marcação)

Não use NDTRAB nem NJTRAB — em vez disso, crie uma consulta (ou script) baseado nas marcas do ponto (RHPONT\_HORA\_FUNC, RHPONT\_MARCA ou similar), fazendo um "count(distinct data)" das marcações.

## **03.****MAIS INFORMAÇÕES**

[Administração de Pessoal - Funções](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719526)

[FOP - Fórmulas / Funções – N](https://tdn.totvs.com/pages/releaseview.action?pageId=452719295)
