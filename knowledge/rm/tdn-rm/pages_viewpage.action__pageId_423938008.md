---
content_hash: 4f6fd2dcf459d903f95e1935318976c81477284e084bf60f429be33e2dd37808
fetched_at: '2026-06-29T00:09:24.719630+00:00'
page_id: '423938008'
product: rm
source: tdn-rm
title: Transferência Monetária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938008
version: 3
---

Este processo permite transferir monetariamente os valores dos patrimônios de forma parcial (retirando somente o valor definido durante o processo) ou total (retirando todo o valor do mesmo). O sistema permite que a transferência monetária seja realizada de forma individual (somente um patrimônio selecionado) ou simultaneamente (definindo uma faixa de patrimônios).

**Regras para execução da ocorrência**

A transferência monetária não será realizada nas situações abaixo:

* Em patrimônios inativos;
* Em patrimônios totalmente baixados em período anterior;
* Valor da transferência maior que o valor corrigido do patrimônio de origem: recurso disponível somente para transferência monetária parcial;
* Data da transferência menor que a última ocorrência existente para o patrimônio envolvido;
* Data do processo fora do período de cálculo. Exemplo: Data da transferência (parcial ou total) 01/02/2010, período de cálculo do sistema patrimonial 01/2011.
* Data da transferência menor que a data de aquisição do patrimônio;
* Patrimônios de origem e destino com cenários diferentes;
* Patrimônio de origem igual ao patrimônio de destino.

**Procedimentos para realização da Transferência Monetária**

A Transferência pode ser executada a partir do menu Operações Patrimoniais|Transferência Monetária por dentro do patrimônio ou pela visão de patrimônios. Neste último caso deve-se selecionar o(s) patrimônio(s) desejado(s) e escolher a opção Transferências Monetárias em Processos (na barra de ferramentas).

Seleção de Patrimônios de Origem

Nesta etapa devem ser selecionados um ou mais patrimônios, definindo os como origem, a serem utilizados na transferência. Caso seja selecionado apenas um patrimônio o sistema permitirá desmembrá-lo. Selecionando vários patrimônios o sistema permitirá unificá-lo.

Seleção do patrimônio de destino e dos dados complementares

O patrimônio informado neste campo receberá os valores transferidos do(s) patrimônio(s) de origem dependendo do tipo de transferência utilizada (total ou parcial). Patrimônios totalmente baixados e/ou totalmente depreciados não poderão ser considerados como de destino.

Observações:

**Patrimônios Avaliados**

Quando um dos patrimônios motivo da transferência estiver avaliado, a transferência monetária somente poderá ser efetuada de/para outro patrimônio avaliado pois ambos devem possuir a mesma quantidade de cenários de cálculo.

**Cota Integral**

Quando uma transferência monetária é executada no sistema, o valor transferido do bem de origem para o bem de destino passa a sofrer depreciação conforme a taxa presente no bem de destino. O bem de origem continua depreciando normalmente pelo o seu valor ajustado, ou seja, subtraindo o que foi transferido.

**Unificação de Patrimônio**

Na prévia seleção de vários patrimônios como origem, ao avançar para etapa de seleção do patrimônio de origem e dos dados complementares, o sistema permitirá a seleção ou cadastro de um novo patrimônio como destino para unificação.  Ou seja, o sistema irá transferir valores e quantidades, unindo dois ou mais patrimônios em um novo ativo imobilizado, seja ele já existente no sistema ou cadastrado no momento do processo. O Patrimônio de destino só poderá receber a unificação caso tenha os mesmos cenários, moedas e cálculos dos patrimônios de origem.

Caso o usuário opte por cadastrar um novo patrimônio, esta ação poderá ser feita através da própria tela de seleção do patrimônio de destino clicando em "Incluir" por dentro do lookup de patrimônio de destino. O cadastro de patrimônio se abrirá como ativo, data de aquisição igual ao primeiro dia do mês de cálculo atual, valor de aquisição e valor base de depreciação iguais a zero e não permitindo a contabilização de aquisição. Todos estes dados estarão desabilitados nesta tela de cadastro de patrimônio.

O sistema processará a unificação como uma transferência monetária de dois ou mais patrimônios de origem para o patrimônio informado como destino transferindo valor e quantidade de acordo com o tipo de transferência informado pelo usuário, total ou parcial.

**Desmembrar patrimônio de origem**

O desmembramento de patrimônio fará o caminho inverso da unificação. O sistema processará a transferência monetária de um único patrimônio de origem para os patrimônios informados como destino, transferindo apenas valor e não transferindo a quantidade. Ou seja, a quantidade do patrimônio de origem não será transferida aos patrimônios informados como destino do desmembramento. Está opção somente é apresentada quando um único patrimônio for selecionado. Se optar por Desmembrar pela quantidade o sistema transfere também a quantidade e desconta a mesma na origem.

Marcando essa opção, o sistema irá desabilitar o patrimônio destino, e permitirá informar um ou mais patrimônios ao avançar etapa. Poderão ser selecionados patrimônios já cadastrados ou patrimônios incluídos através da própria tela de cadastro do patrimônio que será apresentada clicando em "Incluir". O cadastro de patrimônio se abrirá já com o tipo de patrimônio informado, ativo, data de aquisição igual ao primeiro dia do mês de cálculo atual, valor de aquisição e valor base de depreciação iguais a zero e não permitindo a contabilização de aquisição. Todos estes dados estarão desabilitados nesta tela de cadastro de patrimônio;

**Desmembrar por quantidade baseado no patrimônio de origem**

Esta opção somente será habilitada quando a opção acima estiver marcada. Este desmembramento gerará novos patrimônios automaticamente com os mesmos dados e de acordo com a quantidade do patrimônio de origem (em caso de transferência total), ou de acordo com a quantidade especificada na transferência (em caso de transferência parcial).

Por exemplo, se o patrimônio de origem possuir em seu cadastro quantidade 10, em caso de transferência total, o sistema gerará 10 novos patrimônios com os mesmos dados do patrimônio de origem, exceto:

* Data de aquisição: Será igual à data do primeiro dia do mês de cálculo em que está gerando a ocorrência de Transferência Monetária (por desmembramento);
* Valor de depreciação acumulada, valor base e valor de aquisição iguais a zero;
* Aquisição não será contabilizada

Tipo de transferência

Ao transferir totalmente o(s) patrimônio(s) o valor a ser considerado para cálculo será o valor corrigido do patrimônio de origem. Todos os ajustes serão realizados de forma que o(s) patrimônio(s) de origem fique(m) com saldo residual zerado(s).

Outro tipo de transferência monetária disponível é a parcial. O valor transferido do patrimônio de origem será igual ao informado no campo valor da ocorrência. Este valor será aplicado no valor base corrigido do patrimônio e servirá como base para os cálculos dos outros valores relacionados ao mesmo.

Para a transferência monetária parcial é necessário que se informe o "Valor da Ocorrência" (valor a ser transferido) e, opcionalmente, a "Quantidade" de itens referentes ao(s) patrimônio(s) que será(ão) transferido(s). As opções "Valor da Ocorrência" e "Quantidade" são validas somente para o tipo de transferência monetária Parcial.

Data da Transferência

A data a ser utilizada no processo deverá considerar a data base do patrimônio, a última ocorrência para este patrimônio e a data de aquisição do mesmo, ou seja, a data precisa estar dentro do período de cálculo, deverá ser maior que a última ocorrência cadastrada e maior que a data de aquisição.

Campo Observações

Campo livre que permite que sejam descritas informações que, posteriormente, podem ser visualizadas no histórico da ocorrência.

Log

Após cada execução da transferência (total ou parcial) será exibido um log contendo informações referentes ao processo. O resultado da transferência pode ser conferido a partir da aba Cálculo Razão na tela de edição do patrimônio.

Histórico de ocorrências realizadas

Após a execução com sucesso do processo, o sistema armazena as informações relacionadas a transferência monetária (total ou parcial) executada em Operações Patrimoniais|Ocorrências|Consulta/Cancela|Ver Transferência Monetária. Outra forma de visualizar as ocorrências realizadas é a partir da aba de ocorrências da tela de edição do patrimônio.

Excluir ocorrências

Para excluir as ocorrências pode-se selecioná-la na aba Ocorrências (tela de edição do patrimônio) e escolher a opção Exclusão de Ocorrências em Processos. Outra maneira de executar este processo é a partir da tela de ocorrências no menu Operações Patrimoniais. Para ocorrências de Transferência Monetária, sempre serão excluídas todas as ocorrências de origem e de destino envolvidas na transferência.

Índices

Para a base de dados que utilizam índice será respeitada a seguinte regra, caso a moeda não use índices todos os valores correspondentes a índices serão ignorados. Se a moeda utilizar índices e não for encontrada uma cotação na data informada o sistema buscará na data anterior mais próxima.

Veja também

* Consulta de Ocorrências
* Exclusão de Ocorrências
* Contabilização - Transferência Monetária
