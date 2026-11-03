---
content_hash: c735cb0267f619cb9ed4c3f89b0fda6a6b42418c6dfb2988807720737b8cc021
fetched_at: '2026-06-29T00:09:24.795000+00:00'
page_id: '423938017'
product: rm
source: tdn-rm
title: Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/Baixa
version: 9
---

Este processo permite baixar os valores dos patrimônios de forma parcial (retirando somente o valor definido durante o processo) ou total (retirando todo o valor do mesmo). O sistema permite que a baixa seja realizada de forma individual (somente um patrimônio selecionado) ou simultaneamente (definindo uma faixa de patrimônios).

**Parametrização** Para que a contabilização da ocorrência de baixa seja realizada deve-se marcar o parâmetro "Contabilizar Ocorrências" e definir o código do Lote (do sistema contábil) que receberá os lançamentos correspondentes.

**Situações em que a baixa não será realizada:**

* Em patrimônios inativos;
* Em patrimônios considerados Títulos;
* Em patrimônios totalmente depreciados;
* Em patrimônios totalmente baixados em período anterior;
* Valor da baixa maior que o valor corrigido do patrimônio;
* Data da baixa menor que a última ocorrência existente para o patrimônio envolvido;
* Data do processo fora do período de cálculo. Exemplo: Data da baixa  01/02/2010, período de cálculo do sistema patrimonial 01/2011.

**Procedimentos para realização da Baixa:**

A Baixa pode ser executada a partir do menu Operações Patrimoniais/Baixa ou pela visão de patrimônios. No ultimo caso deve-se selecionar o(s) patrimônio(s) desejado(s) e escolher a opção Baixa em Processos (na barra de ferramentas).

**Seleção de Patrimônios**

Devem ser selecionados todos os patrimônios a serem utilizados na baixa. Esta opção será exibida caso o processo seja executado a partir do menu Operações Patrimoniais.  
   
**Seleção dos dados complementares**

Ao baixar totalmente o(s) patrimônio(s) o valor a ser considerado para cálculo será o valor corrigido do patrimônio. Todos os   
ajustes serão realizados de forma que o(s) patrimônio(s) fique(m) com **saldo residual** zerado(s).

A baixa total permite que seja informado um valor de venda para cada patrimônio selecionado, caso sejam escolhidos mais de um patrimônio. Para isto deve-se marcar a opção "Informar valor de venda por patrimônio".

Outro recurso disponível para baixa total é a opção que permite baixar patrimônios agregados. Desta forma cada patrimônio agregado ao patrimônio informado no processo será baixado totalmente. Este recurso é valido apenas ao selecionar a opção "Baixar Agregados".

Outra maneira de baixar o patrimônio é parcialmente. O valor baixado no patrimônio será igual ao informado no campo valor da ocorrência. Este valor será aplicado no valor base corrigido do patrimônio e servirá como base para os cálculos dos outros valores relacionados ao mesmo. Para a baixa parcial é necessário que se informe o "Valor da Ocorrência" (valor a ser baixado) e, opcionalmente, a "Quantidade" de itens referentes ao(s) patrimônio(s) que será(ão) baixado(s).

***Observações:***

As opções "Baixar agregados" e "Informar valor de venda por patrimônio" são validas somente para o tipo de baixa Total.  
Se o campo "Informar valor de venda por patrimônio" não estiver marcado as informações da baixa (valor, data, etc.) irão valer para todos os patrimônios (patrimônios principais e patrimônios agregados). Caso contrário irá valer para todos os patrimônios (patrimônios principais e patrimônios agregados), exceto o valor, pois cada um possuíra o próprio.

**Informar valor de venda por patrimônio**

Caso a baixa contenha mais de um patrimônio a ser baixado totalmente, é possível informar o valor de venda para cada patrimônio, para isso basta marcar esse campo que uma nova aba "Patrimônios" irá ser exibida.

**Informar valor de venda por cenário**

Caso os patrimônios a serem baixados totalmente tenham mais de um cenário de cálculo, é possível informar o valor de venda para cada cenário, para isso basta marcar esse campo que uma nova aba "Patrimônios" irá ser exibida.

**Apura perda e ganho**

[Mais informações](https://tdn.totvs.com/x/BOQPHw)

**Data da baixa**

A data a ser utilizada no processo deverá considerar a data base do patrimônio, a última ocorrência para este patrimônio e a   
data de aquisição do mesmo, ou seja, a data precisa estar dentro do período de calculo, deverá ser maior que a última ocorrência cadastrada e maior que a data de aquisição.

**Valor da venda**

Opcionalmente, pode-se informar o valor da venda dos patrimônios a ser aplicado para cada patrimônio baixado automaticamente

**Motivo de Baixa**

O motivo de baixa deve estar previamente cadastrado antes da execução do processo. Para maiores informações sobre o cadastro do motivo de baixa.

**Contabilização**

A contabilização da baixa respeitará as informações definidas no Evento Contábil para criação dos lançamentos.  
Ao marcar esta opção a contabilização da baixa ficará como pendente, podendo ser realizada posteriormente após a execução com sucesso da baixa.

***Observações:***

Para a contabilização o sistema considera a data do lote e a data da ocorrência, ou seja, o sistema não contabilizará ocorrência com data fora do período do lote contábil.  
A contabilização só será realizada caso seja marcada a opção Contabilizar Ocorrência.

**Campo Observações**

Campo livre que permite que sejam descritas informações que, posteriormente, podem ser visualizadas no histórico da   
ocorrência.  
   
**Log**

Após cada execução da baixa (total ou parcial) será exibido um log contendo informações referentes ao processo.  
   
O resultado da baixa pode ser conferido a partir da aba Cálculo Razão no tela de edição do patrimônio.  
   
**Histórico de ocorrências realizadas**

Após a execução, com sucesso, do processo o sistema armazena as informações relacionadas as ocorrências no menu Operações Patrimoniais.  
Outra forma de visualizar as ocorrências realizadas é a partir da aba de ocorrências da tela de edição do patrimônio.

**Excluir ocorrências**

Caso deseje excluir as ocorrências pode-se selecioná-la na aba Ocorrências (tela de edição do patrimônio) e escolher a opção Exclusão de Ocorrências em Processos. Outra maneira de executar este processo é a partir da tela de consulta de ocorrências no menu Operações Patrimoniais.

**Índices**

Para a base de dados que utilizam índice será respeitada a seguinte regra: Caso a moeda não use índices todos os valores correspondentes a índices serão ignorados. Se a moeda utilizar índices e não for encontrada uma cotação na data informada o sistema buscará na data anterior mais próxima.

Veja Também
