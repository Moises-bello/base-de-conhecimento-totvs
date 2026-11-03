---
content_hash: 38a59fa94c08573a6029c5e26dc6c2a7a7300dcaf30ffc0a8374b50877dbd795
fetched_at: '2026-06-29T00:10:56.810016+00:00'
page_id: '593066040'
product: rm
source: tdn-rm
title: Atualizar valores das multimoedas
type: documentation
url: https://tdn.totvs.com/display/LRM/Atualizar+valores+das+multimoedas
version: 7
---

O processo de "Atualizar valor das multimoedas" tem como objetivo gerar os valores das partidas nas multimoedas parametrizadas no sistema.

A rotina se encarregará de recuperar o valor das partidas, efetuar o cálculo convertendo seu valor nas moedas previamente parametrizadas como multimoedas e então atualizar as tabelas do sistema com os valores obtidos nesta conversão.

Esse cálculo segue a mesma regra de conversão de multimoeda na inclusão/edição do Lançamento contábil (são utilizadas as mesmas rotinas) que em resumo são: recupera as contas da partida, recupera o [tipo de conversão](https://tdn.totvs.com/pages/viewpage.action?pageId=423938354) de multimoeda para tais contas e, caso os tipos de conversão indiquem que deve ser feito a conversão, então recupera o valor da partida. Para cada [multimoeda parametrizada](https://tdn.totvs.com/pages/viewpage.action?pageId=588681922) recupera a [cotação](https://tdn.totvs.com/pages/viewpage.action?pageId=421388646) cuja sua data seja imediatamente antes da data da partida, divide o valor da partida pelo valor da cotação encontrado, atualiza a tabela de multimoeda (tanto da partida quanto dos rateios das partidas) com a identificação da moeda e o valor calculado.

Caso a partida já tenha valores de multimoedas então estes darão lugar aos novos que serão gerados.

Este cálculo será realizado considerando todas as multimoedas parametrizadas no sistema e também conforme o tipo de conversão de cada conta contábil (cadastro de contas contábeis) pertinente à partida que se esta fazendo a conversão/cálculo.

As moedas são cadastradas através de "[Moedas e Índices](https://tdn.totvs.com/pages/viewpage.action?pageId=421388563)", originalmente do módulo do Financeiro mas podem ser acessados através do Contábil facilmente, e o pré-requisito é que aquelas a serem utilizadas como multimoedas devem ter o atributo "Símbolo de referencia padrão" como sendo a moeda padrão utilizada nas partidas caso contrário a rotina não será capaz de encontrar as cotações da multimoeda que se deseja efetuar a conversão.

O processo está disponibilizado no cadastro de "Lançamentos contábeis" na lista de processos.

Ele pode ser disparado com uma prévia seleção de lançamentos/partidas na visão de lançamentos e será executado apenas para os lançamentos/partidas selecionados.

 

Mas também pode ser iniciado sem a seleção de registros onde para este caso uma interface será apresentada para que o usuário informe filtros para a recuperação dos lançamentos/partidas a serem processadas. Tais filtros poderão ser pela seleção de lotes - serão processados lançamentos/partidas que sejam do lote selecionado - ou por período de datas - serão processados os lançamentos/partidas cuja data esteja em tal intervalo de datas (inclusive).

 

Com a opção de filtro não há possibilidade de selecionar algumas partidas em particular, todas as partidas dos lançamentos/partidas que combinarem com os filtros serão processados.

Ao final será gerado um Log informando qual lançamento foi processado com sucesso e qual teve uma ou mais partidas processadas com erro e, se for o caso, qual o erro.

   

No Log também apresentar as Partidas com Valor principal igual a R$ 0,00 que não foram necessário o processamento, além de ordenação.

Ao final do processo, para as partidas processadas com sucesso, as tabelas relativas a multimoeda (tanto da partida quanto dos rateios das partidas) estarão com os valores atualizados (ou criados) de acordo com as multimoedas parametrizadas, as cotações cadastradas, valores das partidas e as conversões considerando tais cotações.
