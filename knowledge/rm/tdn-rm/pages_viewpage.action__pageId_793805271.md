---
content_hash: 49f878a1f347a9c71a28edcd06e525a6eb916b4ecec0018c10147773b91387ea
fetched_at: '2026-06-29T00:11:40.000387+00:00'
page_id: '793805271'
product: rm
source: tdn-rm
title: 'Função de Fórmula: NDDSRHOR'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=793805271
version: 2
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Retorna os dias de compensado, descanso e feriado verificando o histórico do horário do funcionário no mês competência.

NDDSRHOR (STRING)

Sendo STRING informado na fórmula com parâmetro 0 (zero) ou 1 (Um).

Onde:

* Se o parâmetro passado na fórmula for igual a ‘0’  os dias de compensação NÃO serão contabilizados no retorno da função.
* Se o parâmetro passado na fórmula for igual a ‘1’  os dias de compensação serão SIM contabilizados no retorno da função.

**Atenção:**

* A variável verifica admissão, demissão, afastamento, férias, histórico de seção e histórico de horário.
* Na rescisão para o próximo mês verifica os dias da competência da rescisão.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados fictícios da base exemplo

Histórico de horário do funcionário 00001

Cadastro de horário para os horários do histórico do funcionário 00001:

HORÁRIO 0001 - 1 DIA DE COMPENSAÇÃO E 1 DIA DE DESCANSO

HORÁRIO 0002 - 2 DIAS DE COMPENSAÇÃO E 1 DIA DE DESCANSO

Na demonstração do horário do funcionário 00001 temos os dias de descanso e compensação da seguinte forma:

Veja nos links abaixo os resultados da função de fórmula de acordo com a parametrização acima e os cenários descritos:

* CENÁRIO 1 - COM APENAS COMPENSAÇÃO E DESCANSO
* CENÁRIO 2 - COM COMPENSAÇÃO E DESCANSO ACRESCENTANDO 1 DIA DE FERIADO EM 15/08
* CENÁRIO 3 - COM COMPENSAÇÃO, DESCANSO E FERIADO ACRESCENTANDO AFASTAMENTO DE 08/08 A 12/08
* CENÁRIO 4 - COM COMPENSAÇÃO, DESCANSO, FERIADO E AFASTAMENTO ACRESCENTANDO FÉRIAS DE 14/08 A 18/08
* CENÁRIO 5 - COM COMPENSAÇÃO, DESCANSO, FERIADO, AFASTAMENTO E FÉRIAS ACRESCENTANDO DEMISSÃO EM 25/08

11CENÁRIO 1

 

2CENÁRIO 2

   

3CENÁRIO 3

   

4CENÁRIO 4

   

5CENÁRIO 5

   

## **03.** **TABELAS UTILIZADAS**

* PFUNC
* PFHSTAFT
* PFUFERIASPER
* PSECAO
* PFHSTHOR
