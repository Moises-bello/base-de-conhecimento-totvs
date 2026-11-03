---
content_hash: b888d4fee1a917f93f316e2172417c5aced6fc3292f15ba89403edbdcf913a0b
fetched_at: '2026-06-29T00:09:14.893302+00:00'
page_id: '421385297'
product: rm
source: tdn-rm
title: Equalização de Insumos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385297
version: 3
---

---

Esta funcionalidade possibilita dimensionar, com base na Jornada de Trabalho e % Máximo e Mínimo de Horas Extras, a necessidade do recurso, período a período, permitindo um uso mais linear dos Insumos dentro de cada período do cronograma.

A Equalização de recursos trabalha com os Insumos do tipo Mão de Obra (produção e administrativa) e Equipamentos.

É adotado o mesmo modelo de equalização para os dois tipos, a única diferença será a necessidade de criar um Insumo derivado por Insumo do Tipo Equipamento.

Importante!

Para a utilização do recurso é necessário que o grupo de custo do mesmo esteja com a opção **Equalizável** marcada.

Para a utilização do recurso é necessário acessar o Cadastro de Grupo de Custo, em seguida editar o Grupo de Custo do qual o Insumo está associado e marcar a opção Equalizável.

No cadastro destes Insumos, são informadas as premissas relevantes para equalização:

* **Jornada de Trabalho no período (Jornada Pdo.):**Número de horas efetivamente trabalhadas no período do cronograma;
* **% Máximo e Mínimo de Horas Extras (% máx. e % min.):**Limitam o cálculo de alocação indicando quantas horas extras podem ser programadas. Neste caso é a quantidade de horas que o sistema usa para o primeiro cálculo das horas extras, que estarão dentro deste limite, antes da equalização. Depois do Insumo equalizado, estes limites poderão ser ultrapassados;
* **% Fixo de Horas Extras:**Caso este campo seja utilizado, a equalização irá desconsiderar o % Máximo e Mínimo de Horas Extras e programar sempre o valor Mínimo informado em "% Fixo de Horas Extras";

**Exemplo:**

**Equalização do Comprador:** No caso deste campo o valor de horas normais não deve ser diminuído. Deve ser incluída uma quantidade de horas extras que irá aumentar a quantidade total de horas.

**Valor Unitário de Hora Extra (% valor unit.):** Apesar de não influir no cálculo da equalização, será usado para calcular o valor das horas extras programadas. O custo é informado em percentual em relação ao custo original do Insumo.

**Atenção**

Nos Paramentos do Projeto, existe a opção de definir as Opções de Equalização de Insumo Por Projeto ou Por Obra.

* Por Projeto, os campos informativos da Equalização consideram o total do Projeto.
* Por Obra, os campos informativos levam em consideração o total por Obra.  
  Também nos Parâmetros do Projeto, existe a opção de habilitar o calculo automático da equalização. Habilitada esta opção, qualquer alteração referente ao recurso, tanto na atividade associada quanto ao cadastro do mesmo, ao selecioná-lo, automaticamente a Equalização será calculada.

 Como Fazer

---

[Utilizando a Equalização de Insumos](http://tdn.totvs.com/pages/viewpage.action?pageId=421385296)
