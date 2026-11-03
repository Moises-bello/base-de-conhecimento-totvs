---
content_hash: 2909f457045260e34cabfcb9cc1d54443077fecdc6b92f4df138787dbaafd438
fetched_at: '2026-06-29T00:11:20.610117+00:00'
page_id: '687155948'
product: rm
source: tdn-rm
title: Atualizar percentual de homem dia
type: documentation
url: https://tdn.totvs.com/display/LRM/Atualizar+percentual+de+homem+dia
version: 1
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. ****Tela Cálculo de Produção Agrária****
   1. **Principais Campos e Parâmetro**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Nesse parâmetro será calculada a fração do tempo trabalhado referente às tarefas executadas na unidade agrária. Deverá considerar apenas as tarefas em que a regra tenha sido marcada o campo “Incide no Cálculo do Homem-Dia”.

Para o calcular deve ser marcado na “Associação de Regra de Cálculo e Tarefa Agrária” o parâmetro “Incide no Cálculo do Homem-Dia”, ou seja, com o campo marcado, os valores participarão do total de rateio para o cálculo do homem-dia.

**Observação:** Será considerado para os eventos do tipo **(diárias e empreita)**.

## **02. EXEMPLO DE UTILIZAÇÃO**

Não foi lançado para Tarefa “B” as horas correspondente ao tempo trabalho em campo. Está sendo considerado uma jornada normal dentro da semana e três pausas realizadas normalmente (30 minutos).

* Tarefa A - 120 minutos R$ 15,22 (diária)
* Tarefa B - ? R$ 20,00 (empreita)
* Tarefa C - 30 minutos R$ ? (pausa)

Encontrando o número de horas para tarefa “B”, sendo:

[480] - [30min pausa] - [120 tarefa “A”] = 330.

Esse será o valor para a tarefa (produção) de não possui valor para campo “horas”. Distribuição homem dia:

120 / 480 = 0,2500

(480 - (120+30)) / 480 = 0,6875

30 / 480 = 0,0625

0,2500 + 0,6875 + 0,0625 = 1,00

Homem dia = 1,000

**Observação:** Caso tenha falta ou atraso que venha a diminuir o tempo de produção do funcionário, essa fração de homem-dia ficará menor que 1, mas via de regra será totalizado como 1 homem-dia.

## **03.** **TELA Cálculo de Produção Agrária**

**Principais Campos e Parâmetro**

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Selecione a quebra de seção |
| Seleção de Funcionários | Filtrar funcionários |
| Período | Período para o cálculo |
| Parâmetro | Atualizar percentual de homem dia |

## **04. TABELAS UTILIZADAS**

* + PPRODUCAOAGRARIA
