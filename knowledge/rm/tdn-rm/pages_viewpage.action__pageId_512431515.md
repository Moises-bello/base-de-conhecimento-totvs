---
content_hash: ec98f64b34060b0af38262fc041371b477f4a02a1a3998d0c49dbb36a08f7b20
fetched_at: '2026-06-29T00:10:26.118229+00:00'
page_id: '512431515'
product: rm
source: tdn-rm
title: Processo - Equivalência Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=512431515
version: 41
---

Através deste processo será possível realizar lançamentos de equivalências patrimoniais de forma automática. Para isso basta apenas selecionar um [cadastro](https://tdn.totvs.com/x/jRWLHg) previamente feito e acionar o processo.

Informações para processamento:

-Intervalo de datas: este período será levado em consideração para que o movimento/saldo das contas de resultado da(s) investida(s) sejam apurados. O processo irá considerar as movimentações dentro da data informada e assim encontrar os valores para realizar os lançamentos de equivalência.

-Documento: Número de documento que será colocado nos lançamentos gerados pelo processo.

Basicamente o processo encontra os saldos das contas de resultado no período informado e multiplica pelo percentual de participação que a investidora detém sob a investida, e, com o valor encontrado o lançamento de equivalência é gerado. Vale lembrar que o ajuste que a investidora fará na sua conta de investimento e no seu resultado pode ser um lucro ou um possível prejuízo da investida.

Atenção

Caso a Moeda Corrente da Investida seja diferente da Moeda Corrente da Investidora os saldos das contas serão calculados de acordo com o valor existente na aba de [MultiMoedas](https://tdn.totvs.com.br/display/LRM/Multimoedas+-+Partida) das Partidas para a Moeda Corrente da Investidora. Os valores não serão convertidos durante esse processo, eles já estarão calculados previamente quando da inclusão das partidas.

Exemplo:

**1 -** Moeda Corrente da Investida **igual** à Moeda Corrente da Investidora

               O processo irá buscar os valores no "valor principal" da partida, como já era feito anteriormente.

**2 -** Moeda Corrente da Investida **diferente** da Moeda Corrente da Investidora

               O processo irá procurar na aba "[MultiMoeda](https://tdn.totvs.com.br/display/LRM/Multimoedas+-+Partida)" da partida o valor já calculado para a Moeda Corrente da Investidora e irá utilizar esse valor ao invés do "valor principal" da partida.

Caso a Moeda Corrente da Investidora não seja a Moeda Corrente da Investida e nem esteja parametrizada como uma das [MultiMoedas](https://tdn.totvs.com.br/display/LRM/Moedas)desta, o processo não será executado pois não será possível identificar os valores a serem recuperados!

Após execução do processo, os lançamentos de equivalência serão incluídos e será gerado um histórico que poderá ser acessado através dos anexos, lá será possível verificar os lançamentos que foram gerados e também será possível [desfazer a equivalência](https://tdn.totvs.com/x/qBWLHg) caso tenha que ser realizado algum ajuste que não havia sido observado antes.

Abaixo segue alguns exemplos de equivalência patrimoniais:

Exemplos de EquivalênciaExemplo: Equivalência Patrimonial PositivaExemplo: Equivalência Patrimonial Positiva, utilizando uma investidaExemplo: Equivalência Patrimonial PositivaDescrição do Exemplo

* A investidora participa em 75% em uma investida;
* A investidora está realizando o MEP para o período até ;
* A investida apurou R$ 1.500,00 de receitas e R$ 0,00 de custos e despesas, totalizando um lucro de R$ 1.500,00 ao final de dezembro de 2011.
1- Tela - Percentual de Participação

Os percentuais devem ser definidos através dos [Investimentos Societários](https://tdn.totvs.com/pages/viewpage.action?pageId=627971088) e então [Movimentações dos Investimentos Societários](https://tdn.totvs.com/pages/viewpage.action?pageId=629738960) do [Grupo empresarial](https://tdn.totvs.com/display/LRM/Grupo+Empresarial).

2 - Tela - Cadastro da Apuração da Equivalência3 - Tela - Cadastro dos Dados da Apuração

OBS: Essa tela está presente dentro da tela de cadastro da apuração. É uma tela "Filha".

4 - Tela - Gerando o Processo5 - Tela - Lançamentos Gerados

R$ 1.125,00 corresponde a 75% dos R$ 1.500,00 apurados.

6 - Tela - HistóricoExemplo: Equivalência Patrimonial NegativaExemplo: Equivalência Patrimonial Negativa, utilizando uma investidaExemplo: Equivalência Patrimonial NegativaDescrição do Exemplo

* A investidora participa em 50% em uma investida;
* A investidora está realizando o MEP para o período até 31/12/2021.
1- Tela - Percentual de Participação2 - Tela - Cadastro da Apuração da Equivalência3 - Tela - Cadastro dos Dados da Apuração

OBS: Essa tela está presente dentro da tela de cadastro da apuração. É uma tela "Filha".

4 - Tela - Gerando o Processo5 - Tela - Lançamentos Gerados6 - Tela - HistóricoVeja Também

* [Cadastro - Equivalência Patrimonial](https://tdn.totvs.com/pages/viewpage.action?pageId=512431501)
* [Desfazer Equivalência Patrimonial](https://tdn.totvs.com/pages/viewpage.action?pageId=512431528)
