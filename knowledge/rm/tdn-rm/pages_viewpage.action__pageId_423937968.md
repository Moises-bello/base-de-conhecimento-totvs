---
content_hash: 137330131a564987a8664eef0a67dd7386b10b91bb65afd02e51c6cb750f044d
fetched_at: '2026-06-29T00:09:24.597812+00:00'
page_id: '423937968'
product: rm
source: tdn-rm
title: Distribuição de Valores por Filial - Gestão Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937968
version: 3
---

A distribuição de valores por filial tem como objetivo ratear, para cada filial, todos os valores previamente calculados para os patrimônios de acordo com o período em que eles permaneceram nas filiais.   
Para que seja possível utilizar a distribuição de valores por filial o parâmetro "Contabilizar por tempo em cada filial" deverá estar marcado, disponível em Ambiente | Parâmetros | Gestão de Patrimônio | Integração | Integração contábil.  
Esse processo deve ser executado para geração do relatório "Depreciação/Correção por tempo em Filial" e para realização da contabilização por tempo de permanência dos patrimônios em cada filial.  
A distribuição de valores por filial poderá ser realizada para todos os patrimônios, para os patrimônios determinados automaticamente pelo sistema ou para os patrimônios selecionados pelo usuário. Para dar continuidade ao processo será necessário informar uma destas opções.  
Caso o usuário opte por selecionar os patrimônios, ao avançar será necessário incluí-los. O sistema exibirá para seleção apenas patrimônios que não foram baixados em período anterior.

Ao ratear para patrimônios determinados automaticamente pelo sistema, a distribuição será realizada apenas para patrimônios que não sofreram o processo, que está com o rateio por depreciação ainda pendente ou desfeito.

Exemplo: Quando realizamos o recálculo da depreciação a distribuição do período de cálculo vigente é apagada para todos os patrimônios recalculados. Neste caso eles precisarão passar pela distribuição novamente.  
No cadastro tem os patrimônios A, B, C, D, E, F e G. Foram distribuídos os valores dos patrimônios A, B e C. Marcando esta opção serão distribuídos os valores dos patrimônios restantes, ou seja, D, E, F e G.  
Para realizar o cálculo de rateio de depreciação por filial o sistema percorre toda a movimentação entre filiais, existente no período de cálculo vigente, verificando as datas em que os patrimônios entraram e saíram delas.

As movimentações irão se enquadrar nas seguintes situações:

**Entrada anterior ao período inicial do módulo de gestão patrimonial e saída posterior a este período.**  
Vale ressaltar que o período inicial é o primeiro dia do mês e ano de cálculo vigente, e o período final é o último dia do mês e ano de cálculo vigente.

Exemplo: Mês de cálculo igual a 01 e ano de cálculo igual a 2012. O período inicial será 01/01/2012 e o período final será 31/01/2012. Se não houver saída ou a data de saída for maior que o período final então o patrimônio permaneceu 100% do seu tempo na filial. Porém, se da data de saída for maior que o período inicial e a data de saída for menor ou igual ao período final então será necessário calcular o percentual de dias em que esse patrimônio permaneceu na filial.

Exemplo 1 - mês de 30 dias: Saída no dia 16 – O patrimônio ficou 15 dias inteiros na filial, não considerando o dia 16, logo ficou 50% do mês na filial  
Exemplo 2 - mês de 30 dias: Saída no dia 01 – O patrimônio não ficou nem 1 dia inteiro na filial, não considerando o dia 1, logo ficou 0% do mês na filial.  
Exemplo 3 - mês de 30 dias: Saída no dia 30 – O patrimônio ficou 29 dias inteiros na filial, não considerando o dia 30, logo ficou 96,67% do mês na filial.

**Entrada e saída dentro do período do módulo de gestão patrimonial.**  
Se for a primeira movimentação da filial, ou seja, o patrimônio acabou de ser adquirido e a data de entrada for igual à data de início de vigência, então será necessário calcular o percentual de dias em que esse patrimônio permaneceu na filial levando em consideração o dia de início de vigência.

Exemplo - mês de 30 dias: Entrada no dia 11 com saída no dia 15 – O patrimônio ficou na filial nos dias 11, 12, 13 e 14, saindo no dia 15, logo ficou 13,33% do mês na filial Porém, se não for à primeira movimentação da filial deverá ser verificado se mês de entrada é igual ao mês de início de vigência e o ano de entrada é igual ao ano de início de vigência. Se esta condição for verdadeira o cálculo do percentual deverá ser proporcional ao número de dias que o patrimônio permaneceu na filial e não ao total de dias no mês, senão será necessário calcular o percentual de dias em que esse patrimônio permaneceu na filial.  
Exemplo – mês de 30 dias: Um patrimônio adquirido no dia 11, permaneceu por 20 dias na filial e não 30.

**Entrada no período de cálculo vigente e saída após esse período.**  
Se for a primeira movimentação da filial, ou seja, o patrimônio acabou de ser adquirido e a data de entrada for igual à data de início de vigência, então será necessário calcular o percentual de dias em que esse patrimônio permaneceu na filial levando em consideração o dia de início de vigência.

Porém se não for à primeira movimentação da filial deverá ser verificado se mês de entrada é igual ao mês de aquisição e o ano de entrada é igual ao ano de aquisição. Se esta condição for verdadeira o cálculo do percentual deverá ser proporcional ao número de dias que o patrimônio permaneceu na filial e não ao total de dias no mês, senão será necessário calcular o percentual de dias em que esse patrimônio permaneceu na filial.

No caso de entradas e saídas de filiais no mesmo dia a ocorrência deverá ser registrada na filial em que o patrimônio estava no final do dia. Ao final da execução será gerado um log informando o status da execução.

Se a contabilização da depreciação já tiver sido contabilizada, o sistema exibirá a mensagem abaixo ao executar o processo: A depreciação/correção foi contabilizada. Exclua a contabilização para possibilitar a redistribuição de valores por filial. Essa situação ocorrerá quando o parâmetro "Contabilizar por tempo em filial" for marcado posterior à contabilização.

Veja Também

* Transferência de Controle
