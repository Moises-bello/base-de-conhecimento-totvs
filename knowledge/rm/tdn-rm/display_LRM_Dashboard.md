---
content_hash: 9f00e32f657f869a91119872007b69f4e49ddd8a042842da9e78e54d33000d72
fetched_at: '2026-06-29T00:11:26.370165+00:00'
page_id: '716350522'
product: rm
source: tdn-rm
title: Dashboard
type: documentation
url: https://tdn.totvs.com/display/LRM/Dashboard
version: 34
---

## **ÍNDICE**

* 01. VISÃO GERAL
* 02. INDICADORES

## **01. VISÃO GERAL**

O Dashboard do ponto reúne alguns indicadores para sinalizar de que será necessário realizar alguma manutenção no ponto de um funcionário ou verificar a integração das marcações do Clock In. No total temos 8 indicadores, que são:

1. Total de funcionários  
2. Funcionários com o ponto completo  
3. Funcionários com o ponto incompleto  
4. Funcionários sem marcações  
5. Total de marcações no período  
6. Marcações processadas  
7. Marcações existentes para integração  
8. Marcações sem NSR

## **02. INDICADORES**

No Dashboard os indicadores estarão agrupados de acordo com seu grupo. Atualmente temos 2 grupos, que são os **Indicadores de Funcionários** e **Indicadores de Marcações do Clock In**.

Indicadores de Funcionários,Indicadores de Marcações do Clock Infuncionarios,clockinyesfuncionarios

O grupo Indicadores de Funcionários irá exibir informações dos funcionários cadastrados no Automação de Ponto . Com isso será possível identificar a quantidade de funcionários que utilizam o ponto eletrônico, funcionários com o ponto completo, incompleto e sem qualquer marcação realizada no período.  

Temos 4 indicadores que são:

**Total de funcionários:** É a quantidade total de funcionários que utilizam o ponto eletrônico conforme o período informado. Serão considerados funcionários Ativos no período    , Afastados parcialmente("Férias, Afastamento, Atestado"), cujo retorno/saída esteja dentro do período considerado, funcionários transferidos, funcionários demitidos ,porém, ativos no período filtrado.

**Funcionários com o ponto completo:** É a quantidade de funcionários com o ponto completo no período selecionado. Para esse indicador, serão considerados:

* Somente as marcações que já foram importadas para a tabela ABATFUN, sendo batidas importadas, lançadas ou inseridas manualmente.
* Funcionários que possuem o total de marcações pares e que sejam superiores ou igual a quantidade que ele precisa realizar de marcações nos dias do período.

**Exemplo :** Funcionário  possui o seguinte horário de segunda a sexta: 08:00-12:00-14:00-18:00 e precisa realizar a marcação do ponto 4 vezes ao dia (Entrada jornada, Saída/Entrada batidas de refeição e Saída da jornada). Na semana o funcionário trabalha de segunda à sexta, então teremos 5 dias trabalhados, onde cada dia o funcionário precisa bater o ponto 4 vezes totalizando 20 marcações na semana. Se o funcionário possuir 20 ou mais marcações o sistema irá contabilizar como ponto completo. 

* Funcionários que utilizam cartão de ponto.
* Funcionários que possuem horário com o cadastro de Ausência Planejada ou tempo mínimo por intervalo .Será considerado como ponto completo os funcionários que tiverem as batidas de entrada e saída da jornada do horário, duas batidas já será considerado como ponto completo.
* Funcionários que não possuem intervalo de ausência cadastrado no horário ou tempo mínimo, pois precisam ter as batidas de ausência registradas, o sistema deve considerar todas as batidas para considerar o ponto completo. Sempre batida par.
* Para os funcionários que no dia selecionado tiver em dia de Compensado, Descanso, Batida Nula ou feriado, o sistema considera como ponto completo, pois ele não precisa de marcação de ponto para este dia ou período;

**Funcionários com o ponto incompleto:** É a quantidade de funcionários com o ponto incompleto no período selecionado. Para esse indicador, serão considerados:

* Somente as marcações que já foram importadas para a tabela ABATFUN, sendo batidas importadas, lançadas ou inseridas manualmente.
* Funcionários que possuem o total de marcações ímpares e que sejam inferiores a quantidade que ele precisa realizar de marcações nos dias do período.

**Exemplo :**Funcionário  possui o seguinte horário de segunda a sexta: 08:00-12:00-14:00-18:00 e precisa realizar a marcação do ponto 4 vezes ao dia (Entrada jornada, Saída/Entrada batidas de refeição e Saída da jornada). Na semana o funcionário trabalha de segunda à sexta, então teremos 5 dias trabalhados, onde cada dia o funcionário precisa bater o ponto 4 vezes totalizando 20 marcações na semana. Se o funcionário possuir menos de 20 marcações o sistema irá contabilizar como ponto incompleto.

* Funcionários que utilizam cartão de Ponto.
* Se o primeiro dia do período o colaborador tiver batidas ímpares, será considerado como ponto incompleto.

**Funcionários sem marcações:** É a quantidade de funcionários que não possuem nenhuma marcação no período. Para esse indicador, serão considerados:

* Somente funcionários que não possuem nenhuma marcação na tabela ABATFUN do período, se houver uma marcação será considerado como Ponto Incompleto.

**Observações:**

* **Sem o cálculo**: A marcação será exibida no dashboard conforme a data da marcação.
* **Com o cálculo**: A marcação será exibida no dashboard conforme a data de referência.

Dashboard

Veja as **[Evoluções Dashboard](https://tdn.totvs.com/pages/viewpage.action?pageId=923182122)**

     

noclockin

O grupo Indicadores de Marcações do Clock In irá exibir informações referente a integração das marcações. 

Neste grupo teremos no total 4 indicadores que são:

**Total de marcações no Clockin:** É o total de todas as marcações existentes no Clock In no período selecionado.Serão consideradas marcações com e sem NSR zerado e se estão integradas ou não no ERP.

**Total de marcações Integradas:** É a quantidade total de marcações disponíveis com NSR e que foram integradas no ERP. 

**Total de marcações pendentes para integração:** É a quantidade total de marcações que estão disponíveis com NSR gerado para integração e que ainda não foram integradas no  ERP.

**Total de marcações sem NSR:** É o total de marcações existentes no clockin no período e que não possuem NSR gerado.
