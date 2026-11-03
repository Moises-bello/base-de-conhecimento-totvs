---
content_hash: 10e17960162b0c183dd4dc4771d1013259a35ee5d5a64f375e6cd2e29a5fb830
fetched_at: '2026-06-29T00:09:24.779754+00:00'
page_id: '423938014'
product: rm
source: tdn-rm
title: Acréscimo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938014
version: 3
---

Este processo permite realizar acréscimo nos valores dos patrimônios de forma individual (somente um patrimônio selecionado) ou simultaneamente (definindo uma faixa de patrimônios).

***Observação:***

A depreciação sobre o valor acrescido será calculada somente a partir da data do Acréscimo.

**Parametrização**

Para que a contabilização da ocorrência de acréscimo seja realizada deve-se marcar o parâmetro "Contabilizar Ocorrências" e definir o código do Lote (do sistema contábil) que receberá os lançamentos correspondentes.

**O acréscimo não será realizado nas situações abaixo:**

* Em patrimônios considerados Títulos;
* Em patrimônios totalmente depreciados;
* Em patrimônios totalmente baixados em período anterior;
* Data do processo fora do período de cálculo. Exemplo: Data do acréscimo 01/01/2010, período de cálculo do sistema patrimonial 01/2011.

**Procedimentos para realização do Acréscimo**

O acréscimo pode ser executado a partir do menu Operações Patrimoniais/Acréscimo ou pela visão de patrimônios. Neste caso   
deve-se selecionar o(s) patrimônio(s) desejado(s) e escolher a opção Acréscimos em Processos (na barra de ferramentas).

**Seleção de Patrimônios**

Nesta etapa devem ser selecionados todos os patrimônios a serem utilizados no acréscimo. Esta opção será exibida caso o   
processo seja executado a partir do menu Operações Patrimoniais.  
   
**Seleção dos dados complementares:**

**Tipo de acréscimo**

* Ratear Valor: Nesta opção o valor da ocorrência será dividido pelo número de patrimônios envolvidos e posteriormente acrescentado a cada patrimônio.  
  Ao escolher este tipo será habilitado o campo Valor da ocorrência onde o valor do acréscimo deverá ser informado. Exemplo: Valor do acréscimo: R$ 1.000,00 Total de patrimônios selecionados: 5 Valor do acréscimo para cada patrimônio: R$ 200,00
* Por percentual Esta opção considerará o valor base corrigido do patrimônio como base para realização do cálculo do percentual. Ao escolher este tipo será habilitado o campo Percentual onde o percentual, menor ou igual a 100, deverá ser informado. Exemplo: Percentual: 10 % Valor corrigido do patrimônio: R$ 10.000,00. Valor do acréscimo a ser gerado para cada patrimônio: R$ 1.000,00

**Data**

A data a ser utilizada no processo deverá considerar a data base do patrimônio, a última ocorrência para este patrimônio e a data de aquisição do mesmo, ou seja, a data precisa estar dentro do período de calculo, deverá ser maior que a última ocorrência cadastrada e maior que a data de aquisição.

**Quantidade**

Quantidade de itens que serão acrescentados para os patrimônios.

**Contabilização**

A contabilização do acréscimo respeitará as informações definidas no Evento Contábil para criação dos lançamentos.

Ao marcar esta opção a contabilização do acréscimo ficará como pendente, podendo ser realizada posteriormente após a execução com sucesso do acréscimo.

***Observações:***

Para a contabilização o sistema considera a data do lote e a data da ocorrência, ou seja, o sistema não contabilizará ocorrência com data fora do período do lote contábil. A contabilização só será realizada caso seja marcada a opção Contabilizar Ocorrência.

**Campo Observações**

Campo livre que permite que sejam descritas informações que, posteriormente, podem ser visualizadas no histórico da ocorrência.

**Log**

Após cada execução do acréscimo será exibido um log contendo informações referentes ao processo.  
O resultado do acréscimo pode ser conferido a partir da aba Cálculo Razão no tela de edição do patrimônio.  
   
**Histórico de ocorrências realizadas**

Após a execução, com sucesso, do processo o sistema armazena as informações relacionadas ao acréscimo no menu Operações Patrimôniais.

Outra forma de visualizar as ocorrências realizadas é a partir da aba de ocorrências da tela de edição do patrimônio.

**Excluir ocorrências**

Caso deseje excluir as ocorrências pode-se selecioná-la na aba Ocorrências (tela de edição do patrimônio) e escolher a opção Exclusão de Ocorrências em Processos.

Outra maneira de executar este processo é a partir da tela de ocorrências no menu Operações Patrimoniais.

**Índices**

Para a base de dados que utilizam índice será respeitada a seguinte regra:

Caso a moeda não use índices todos os valores correspondentes á índices serão ignorados. Se a moeda utilizar índices e não for encontrada uma cotação na data informada o sistema buscará a data anterior mais próxima.

Processos



Veja Também

* Consulta de Ocorrências
