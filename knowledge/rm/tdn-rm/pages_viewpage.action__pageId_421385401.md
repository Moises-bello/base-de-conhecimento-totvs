---
content_hash: c546b16b763eca8a63605bd08ac0118cb875936da0f126dd420a35f3fdaef7f4
fetched_at: '2026-06-29T00:09:15.516233+00:00'
page_id: '421385401'
product: rm
source: tdn-rm
title: Cálculo do Peso e Cálculo do Avanço Físico 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385401
version: 2
---

---

Na visão da Planilha de Atividades, são apresentados dois processos "Calcular Peso", "Calcular Avanço Físico".

Para visualização dos cálculos realizados por estes processos foram criados 6 colunas:

 - Coluna Valor de referência - Fórmula definida pelo usuário. A fórmula poderá ser definida em:

* Quantidades em composição: dado um serviço, um grupo de custo ou um insumo, a fórmula retorna a quantidade existente para o serviço na composição associada.
* Valor da Tarefa: Com uma sentença SQL associada a uma fórmula é possível trazer o valor da tarefa.

**Observação:**

Para o cálculo do valor referência quando for utilizada uma fórmula que retorna valores sobre o recurso(composição e insumos), serão considerados os valores de acordo com a curva ABC, em caso dos recursos não se encontrarem na Curva ABC, o sistema irá realizar o cálculo automaticamente ao se calcular o Peso.

 - Coluna Unidade - Exibe a unidade associada ao resultado da fórmula, pode ser informada no parâmetro ou diretamente na obra.

 - Coluna Peso Referente ao Nível - É calculado para estabelecer o percentual da atividade em relação ao valor total do nível. Para o cálculo do Peso no Nível considera o conjunto de todas as atividades que estão no mesmo subprojeto.

**Observações:**

Este campo pode ser informado manualmente e neste caso o sistema não calcula quando acionado o cálculo do Peso para a atividade em questão.

Existe uma opção que fica habilitada exibindo que a tarefa ou obra é informada, ou seja, não entra no cálculo.

A fórmula do cálculo é:

Valor de Referência da Atividade / (soma dos valores de todas as atividades, que não foram informados pelo usuário)) \*Percentual Considerado.  
  
  - Coluna Peso no projeto - Para o cálculo desta coluna é realizado a seguinte conta: Multiplicar o Peso No Nível da tarefa \* o peso no nível da sua etapa \* peso no nível da etapa superior e assim sucessivamente até chegar a multiplicar pelo Peso no Nível do SubProjeto .  
  
  - Coluna Realizado(Nível) - Exibe o percentual realizado por nível.

* Será calculado:

 Para serviço: Peso Nível \* %Concluído (Segundo informação do Percentual Concluído do Pert).

 Para Etapas/SubProjetos : Somatório de (Peso de cada atividade do nível inferior (inclusive etapas se existirem) \* o Percentual Concluído(Segundo informação do Percentual Concluído do Pert)) \* o Peso Nível da Etapa e SubProjeto.

 - Coluna Realizado(Projeto) - Exibe o percentual realizado por projeto.

* Será calculado:

 Para serviços: Peso Projeto \* %Concluído (Segundo informação do Percentual Concluído do Pert).

 Para Etapas: Somatório do Peso do projeto para cada atividade do nível inferior (inclusive etapas se existirem).

O processo "Calcular Peso", realiza o cálculo e demonstra os resultados nas colunas "Valor de Referência", "Peso Nível", "Peso Projeto".

**Observação:**

Quando o parâmetro "Bloquear alterações nos pesos das atividades" estiver marcado, não serão permitidas alterações nos campos: "Valor de Referência", "Peso Nível" e "Peso Projeto".

O processo "Avanço Físico" realiza o cálculo e demonstra os valores nas colunas, "Real Nível", "Real Projeto", para serem exibidos valores nestas colunas é necessário que os pesos tenham sido calculados, pois estes são utilizados no cálculo.

**Observações:**

O percentual considerado é 100%, caso nenhuma atividade de mesmo nível tenha o seu peso referente ao nível informado. Caso tenha sido informado ele soma o percentual até chegar em 100%

Para conseguir estabelecer um peso de atividade é necessário informar uma fórmula para que tenha o resultado esperado, a fórmula será definida em  Parâmetros do Projeto - Cálculo – Outros.

Existe um campo Avanço Físico onde deve ser informada a fórmula de Peso e a Unidade Referência para o cálculo da planilha de tarefas.

Existe também a possibilidade de considerar atividades de custo indireto no cálculo do avanço físico, para isso marque o parâmetro "considera atividades de Custo Indireto" no campo Avanço Físico, que deverá ser marcado.

A fórmula para o cálculo do Avanço Físico pode ser informado diretamente na Obra, neste caso o sistema considera esta fórmula em prioridade. Caso não exista fórmula para a obra, o sistema irá realizar a verificação conforme o parâmetro do Projeto - Cálculo – Outros.

Para o cálculo do Peso no Nível considera-se o conjunto de todas as atividades que estão no mesmo subprojeto. Além disto, haverá a necessidade de informar para cada tarefa Obra uma fórmula e uma unidade de calculo do Valor de Referência de suas atividades e etapas. O somatório do campo Peso Nível, de todas as atividades em um nível deve fechar sempre em 100%.

Caso haja a necessidade de mais de uma Unidade de Peso o projeto deverá ser dividido em mais de um Subprojeto e para cada Subprojeto deverá ser informado o Peso no Nível Manualmente, pois não haverá como calculá-lo visto que se trata de unidades diferentes de comparação.

---
