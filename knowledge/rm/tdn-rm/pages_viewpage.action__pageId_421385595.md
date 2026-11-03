---
content_hash: 3c5361468b355ccce11f443e122b058d80232522334633e604e9ede8d0290b5f
fetched_at: '2026-06-29T00:09:16.872160+00:00'
page_id: '421385595'
product: rm
source: tdn-rm
title: Composição Turma Típica e Composição por Unidade de Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385595
version: 2
---

---

A Turma Típica representa os recursos de Mão de Obra que serão utilizados na execução de uma atividade, e será tratada como uma Composição no TOTVS Obras e Projetos. A principal diferença de uma turma típica comparada com uma composição de preço unitário é que a distribuição dos recursos é em percentual (%), representando a divisão das horas de execução do serviço.  
 Ao se cadastrar uma composição no Obras e Projetos o campo tipo da composição listará além das opções que existiam antes CPU e Por Produção, será exibido Turma Típica e Por unidade de Serviço.  
    
 Uma composição de turma típica por si só não gera custo para um projeto, já que ela trata do peso de cada mão de obra na execução de um serviço. Ela irá gerar custo quando estiver inserida em uma composição por unidade de serviço, e essa composição estiver inserida em alguma tarefa.  
    
 **Observações:**

* A composição do tipo Turma Típica só poderá ser utilizada como uma composição auxiliar dentro de uma "composição por unidade de serviço".
* Composição Turma Típica não poderá recurso de uma atividade.
* A soma dos coeficientes (quantidade) dos recursos de uma Turma Típica deverá ser  um (1), totalizando 100% (esses coeficientes representam o percentual que cada recurso demanda dentro de uma composição Turma Típica).
* Todos os recursos da composição de Turma Típica devem possuir a mesma unidade da unidade utilizada na composição de Turma Típica.
* Uma composição turma típica não poderá ter valor, mesmo após o cálculo.
* A composição Por Unidade de Serviço possui como diferencial o tratamento de valores Standard, que representa a quantidade de horas necessárias para se produzir uma unidade de um determinado serviço.
* É nesse tipo de composição que encontra-se o uso da turma típica.
* Em conjunto composição Por Unidade de Serviço temos a quantidade de horas que cada recurso que compõe a composição turma típica ligada a essa composição demandará.
* As horas definidas no campo Standard serão aplicadas à Turma Típica utilizada como composição auxiliar, portanto, composição por unidade de serviço deve possuir uma Turma Típica associada.
* O valor da composição por Unidade de Serviço somente terá o seu valor calculado, depois que o campo Standart for informado.
