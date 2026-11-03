---
content_hash: 5351495a7a0eaf0631eecea58893460bd352b28d9e35a8da92675b75183f75d3
fetched_at: '2026-06-29T00:10:57.819291+00:00'
page_id: '599859200'
product: rm
source: tdn-rm
title: Fechamento da conversão para multimoeda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=599859200
version: 28
---

Mensalmente, após a apuração dos resultados na moeda funcional da coligada, é preciso realizar também o Fechamento da Conversão para multimoeda considerando o método de conversão parametrizado para cada Conta Contábil.

Em vista disto é disponibilizado o processo **Fechamento da conversão de multimoeda**cujo objetivo é gerar lançamentos/partidas apenas com valores de ajustes para as multimoeda de maneira a equalizar seus saldos de acordo com as regras contábeis (NBC TG 02).

Este fechamento só é necessário, portanto só é executado, para as contas contábeis parametrizadas com os modelos de conversão **Taxa Média Histórica** e **Taxa de Fechamento**.

Durante este processo, de maneira geral, são executadas as seguintes atividades:

1. Calcula o saldo de cada conta na moeda funcional (1º valor);
2. Converte o saldo encontrado de acordo com o critério parametrizado na conta contábil para cada uma das moedas parametrizadas;
3. Calcula o saldo da Conta Contábil em cada uma das moedas parametrizadas (valor que está gravado no Anexo Multimoeda dos Lançamentos Contábeis);
4. Insere um Lançamento Contábil, no último dia do mês, para cada uma das contas contábeis que for processada com 1º Valor zerado e no anexo de Multimoeda os registros com a moeda “destino” contendo o valor da diferença da variação cambial considerando o saldo da conta na moeda e o valor da nova conversão na data do fechamento (Valor do Item 2 - Valor do Item 3). A diferença entre débito e crédito, resultante da variação dos métodos será lançada, a débito ou a crédito, nas contas previamente parametrizadas.

Fique atento!

* São pré-requisitos para este processo:
  + Parametrização da [moeda corrente](https://tdn.totvs.com/pages/viewpage.action?pageId=588681922),
  + Parametrização das [multimoeda](https://tdn.totvs.com/pages/viewpage.action?pageId=588681922) a serem utilizadas,
  + Parametrização das contas débito/crédito e histórico padrão para ajustes ([Conversão de moedas](https://tdn.totvs.com/pages/viewpage.action?pageId=588682883)),
  + [Cadastro das cotações](https://tdn.totvs.com/pages/viewpage.action?pageId=421388646) para as multimoeda parametrizadas,
  + Definição do t[ipo de conversão de multimoeda de cada conta contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=423938354) envolvida.
* Não é permitida a execução do processo para um período (mês/ano) caso existam processamentos para tal período ou períodos posteriores. Se for realmente necessário tal reprocessamento então é preciso cancelar tais processamentos iguais ou posteriores para então reprocessar o período desejado ([Histórico e cancelamento de fechamento de conversão de multimoeda](https://tdn.totvs.com/pages/viewpage.action?pageId=598671229)).
* Caso não esteja seguro que os valores das multimoeda estão atualizados então é desejável que o processo de "[Atualização dos valores das multimoeda](https://tdn.totvs.com/display/LRM/Atualizar+valor+das+multimoedas)" seja executado antes da execução deste processo.

**Caso o TOTVS RM (ambiente do cliente) esteja configurado para trabalhar com o JobServer em modo 3 camadas, este processo poderá usufruir de todas as vantagens e conveniências de tal recurso, como agendamento de processos, possibilitando a execução em dia/horário específico, criar recorrências ou repetições para estes agendamentos.**

O processo está disponibilizado em *Escrituração Contábil | Operações contábeis | Multimoeda | Fechamento da conversão de multimoeda* e é controlado pelo perfil de segurança do TOTVS RM, portanto, é necessário conceder ao usuário as permissões adequadas no perfil para que seja possível o acesso ao processo.

Ao ser acionado o processo apresentará uma interface para que o usuário informe os filtros para a recuperação dos lançamentos/partidas a serem processadas. Tais filtros são de preenchimento obrigatório e competem de: seleção de coligadas e mês/ano referencia dos registros. Serão processados somente os lançamentos/partidas que sejam das coligadas selecionadas, do lote 0 e do período de datas formado pelo inicio do período contábil e último dia do mês/ano informado.

Figura

Ao final do processo será gerado um log informando qual lançamento e partidas de ajustes foram geradas no caso de sucesso ou, em caso de erro, os detalhes dos erros.

Atenção!

Cabe ressaltar que todas as partidas, de acordo com filtros e regras, serão processadas mesmo se houver erros (isto poupar tempo na operação/correção de erros) mas a geração e gravação de lançamentos/partidas de ajustes irá ocorrer apenas se todas as partidas forem processadas com sucesso, isto é, se uma partida apresentar erro o processamento continuará mas nenhuma partida de ajuste será gerada.

Figura 2

     

 Detalhando um pouco mais do processo e seus cálculos:

*Observações:*

1. Lembrando que valor multimoeda é aquele dado pelo valor da partida convertida para as multimoeda parametrizadas observando a cotação imediatamente antes ao do dia do lançamento/partida;
2. Para efeito de facilitar os cálculos estamos considerando débito positivo e crédito negativo;
3. Este processo é realizado pelo seguinte agrupamento: coligada, filial, conta contábil e conta gerencial.

none80

 O processo recuperará os saldos (partidas e multimoeda) do exercício anterior, os saldos (partidas e multimoeda) da movimentação atual (lote 0, inicio do período contábil e último dia do mês da data selecionada) e somará os saldos relativos às partidas e saldos relativos às multimoeda obtendo os saldos "finais" de cada um;

 O saldo relativo às partidas será convertido conforme a moeda e a cotação onde a cotação será recuperada conforme parametrizada na conta que poderá ser: média das cotações do mês (do mês/ano que se está processando) ou a cotação da última data do mês/data de fechamento (do mês/ano que se está processando);

**Importante**: Caso não haja cotação na ultima data do mês/data de fechamento então será considerada a ultima cotação imediatamente anterior.

 Com o saldo final das partidas convertido para a moeda desejada e o saldo final multimoeda, o processo subtrai uma pela outra obtendo assim qual será o valor do ajuste a ser feito;

 Uma vez com este ajuste criamos uma partida com valor zerado e apenas com o valor da respectiva multimoeda como sendo o valor do ajuste calculado. As partidas serão criadas e no quesito débito ou crédito, basicamente, conforme o tipo de saldo final multimoeda que calculamos anteriormente. Se o tipo do saldo for credor então a partida será devedora e se o tipo do saldo for devedor então a partida será credora;

 Isto é realizado para todas as contas identificadas no período definido (inicio do período contábil e último do mês/ano selecionados para o processo), que tenham movimentação e que estejam com o atributo "Tipo de conversão multimoeda" definidos como média ou data de fechamento.

Os passos acima vão gerar os ajustes nas multimoeda em cada uma das contas contábeis mas, como as contas utilizam métodos diferentes para efetuar a conversão (média ou data de fechamento), ocorrerá uma diferença entre o total de débito e o total de crédito no lançamento de ajuste. Essa diferença será informada em uma partida utilizando-se as contas de débito ou de crédito parametrizadas no sistema.

trueExemplo de processamentoa,b,c,d,eaLançamentos contábeis

Lançamentos contábeis com a lista de partidas que serão processadas:

bAcionamento do processo

Ênfase no mês/ano que é a data dos lançamentos/partidas e finalização de sua execução:

cAjuste de Conversão

Lançamentos contábeis e o novo lançamento/partidas de ajustes que foram criados pelo processo. Cada partida de ajuste tem a conta contábil de origem com as multimoedas e os valores de ajuste mas o valor da partida em si está zerado.

dAjuste de Fechamento

Observe que há uma partida que é o ajuste final, isto é, o ajuste relativo aos ajustes. Nesta partida a conta débito ou crédito e histórico padrão utilizado são aqueles previamente parametrizados.

ePlanilha de exemplo

O objetivo dessa planilha é auxiliar na compreensão dos cálculos envolvidos. **Todos os dados e valores são fictícios.**

250

A planilha será melhor visualizada se baixada.
