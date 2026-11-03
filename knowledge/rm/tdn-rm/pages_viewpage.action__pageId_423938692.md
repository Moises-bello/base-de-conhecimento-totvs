---
content_hash: b09eaceedf48217fd2aaaef63e3eddbeedd393ee0d3a05545e000f58874a6959
fetched_at: '2026-06-29T00:09:28.495932+00:00'
page_id: '423938692'
product: rm
source: tdn-rm
title: Contas de Aglutinação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938692
version: 2
---

As Contas de Aglutinação estabelecem uma relação entre as contas analíticas do plano de contas da empresa e as linhas de maior detalhamento a serem utilizadas na Demonstração de Resultado do Exercício (Registro J150) e no Balanço Patrimonial (Registro J100) recebendo a totalização dos valores movimentados. Para o Balanço Patrimonial, pode-se definir como Conta de Aglutinação a própria conta que recebe os lançamentos (analítica) ou definir um grau correspondente à conta sintética que será considerada como aglutinadora. Para a Demonstração de Resultado do Exercício, a totalização será na própria conta movimentada, tendo-se, porém, a opção de não mostrar as contas analíticas e, desta forma, as contas aglutinadoras serão as sintéticas de maior nível, ou seja, as contas sintéticas imediatamente superiores às contas analíticas.

**Como informar as contas de aglutinação:**

* Para geração da Demonstração de Resultado do Exercício (Registro J150):
  + Para este registro serão consideradas todas as contas do plano de contas cuja natureza seja "Contas de Resultado" informando na mesma o valor total da movimentação correspondente e a totalização dos valores nas contas sintéticas. Na geração do Sped foi acrescentada uma aba "Informações Complementares" com várias opções de parametrização. Marcando-se a opção "Não mostrar as contas analíticas na Demonstração de Resultado do Exercício (Registro J150)" serão consideradas como contas aglutinadoras para este registro as contas sintéticas de maior nível. Deixando desmarcada esta opção, a própria conta será considerada como conta de aglutinação, ou seja, serão geradas neste registro todas as contas classificadas como "Contas de Resultado", desde as sintéticas até as analíticas

* Para geração do Balanço Patrimonial (Registro J100):
  + Para este registro serão consideradas todas as contas do plano de contas cuja natureza seja "Contas de Ativo", "Contas de Passivo" ou "Patrimônio Líquido" informando na mesma o valor total da movimentação correspondente e a totalização dos valores nas contas sintéticas. Na aba "Informações Complementares" informar o "Grau de Aglutinação (Balanço Patrimonial)". Cada grau corresponde a um nível de quebra do plano de contas. Informando-se o grau TOTAL a própria conta analítica será a conta aglutinadora, ou seja, serão geradas neste registro todas as contas conforme a natureza própria para este registro, desde as sintéticas até as analíticas.   
    As Contas de Aglutinação escolhidas conforme as opções parametrizadas na aba "Informações Complementares" serão informadas no Registro I052 do Sped Contábil como a seguir:   
    Registro I052

|I050|01012001|01|S|1|1||1 ATIVO|

|I050|01012001|01|S|2|1.1|1|1.1 TESTE|

|I050|01012001|01|A|3|1.1.01|1.1|1.1.01 CAIXA|

|I051|10||1.01.01.01.00|

|I052||1.1.01|

|I050|01012001|02|S|1|2||2 PASSIVO|

|I050|01012001|02|S|2|2.1|2|2.1 PASSIVO|

|I050|01012001|02|A|3|2.1.01|2.1|2.1.01 FORNECEDORES|

|I051|10||2.01.01.01.00|

|I052||2.1.01|

|I050|01012001|03|S|2|2.2|2|2.2 PATRIMÔNIO LÍQUIDO|

|I050|01012001|03|A|3|2.2.01|2.2|2.2.01 LUCRO/PREJUIZO ACUMULADO|

|I051|10||2.07.07.01.00|

|I052||2.2.01|

|I050|01012001|04|S|1|3||3 DESPESAS|

|I050|01012001|04|S|2|3.1|3|3.1 TESTE|

|I050|01012001|04|A|3|3.1.01|3.1|3.1.01 DESPESAS DE VIAGEM|

|I051|10||4.01.07.01.27.00|

|I052||3.1|

I050|01012001|04|S|1|4||4 RECEITAS|

|I050|01012001|04|S|2|4.1|4|4.1 RECEITAS DE VENDAS|

|I050|01012001|04|A|3|4.1.01|4.1|4.1.01 VENDAS|

|I051|10||3.01.01.01.01.07.00|

|I052||4.1|

Para geração das informações acima no registro I052, a parametrização utilizada foi:

"Grau de Aglutinação (Balanço Patrimonial)" = TOTAL

Veja que no registro I052, para as contas consideradas para o Balanço Patrimonial, a própria conta analítica é a conta aglutinadora, pois foi escolhido o grau TOTAL (exemplo: |I052||1.1.01| ). Esta escolha irá refletir no registro J100 onde serão consideradas, então, todas as contas, desde as analíticas até as sintéticas: Registro J100 (Balanço Patrimonial):

|J100|1|1|1|1 ATIVO|820,00|D|

|J100|1.1|2|1|1.1 TESTE|820,00|D|

|J100|1.1.01|3|1|1.1.01 CAIXA|820,00|D|

|J100|2|1|2|2 PASSIVO|820,00|C|

|J100|2.1|2|2|2.1 PASSIVO|500,00|C|

|J100|2.1.01|3|2|2.1.01 FORNECEDORES|500,00|C|

|J100|2.2|2|2|2.2 PATRIMÔNIO LÍQUIDO|320,00|C|

|J100|2.2.01|3|2|2.2.01 LUCRO/PREJUIZO ACUMULADO|320,00|C|

"Não mostrar as contas analíticas na Demonstração de Resultado do Exercício (Registro J150)" = Opção marcada Veja que no registro I052, para as contas de Resultado, estão informadas as contas sintéticas de maior nível como conta aglutinadora, pois foi escolhido não mostrar as contas analíticas

(exemplo: |I052||3.1| ). Esta escolha irá refletir no registro J150 onde serão mostradas somente até as contas sintéticas que receberão, então, o total das suas analíticas que, por sua vez, não aparecerão no registro:   
Registro J150 (Demonstração de Resultado do Exercício):

|J150|3|1|3 DESPESAS|1500,00|N|

|J150|3.1|2|3.1 TESTE|1500,00|D|

|J150|4|1|4 RECEITAS|1820,00|P|

|J150|4.1|2|4.1 RECEITAS DE VENDAS|1820,00|R|

As outras opções da aba "Informações Complementares" são:

* Mostrar o saldo final da "Apuração de Resultado do Exercício" (Registro J150):  
  Com esta opção marcada será incluída uma linha a mais no registro J150 com uma conta aglutinadora virtual cuja descrição será informada no campo abaixo e que armazenará o saldo final da Apuração de Resultado do Exercício:

  |J150|3|1|3 DESPESAS|1500,00|N|

  |J150|3.1|2|3.1 TESTE|1500,00|D|

  |J150|4|1|4 RECEITAS|1820,00|P|

  |J150|4.1|2|4.1 RECEITAS DE VENDAS|1820,00|R|

  |J150|ARE|1|APURAÇÃO DE RESULTADO DO EXERCÍCIO|320,00|N|
* Mostrar o código da conta na geração do registro J100 e J150:  
  (Com esta opção marcada, ao gerar as informações para os registros J100 (Balanço Patrimonial) e J150 Demonstração de Resultado do Exercício) será adicionado, na descrição das contas aglutinadoras, o código da conta contábil para facilitar a conferência:

  |J100|2.2.01|3|2|2.2.01 LUCRO/PREJUIZO ACUMULADO|320,00|C|

  |J150|4.1|2|4.1 RECEITAS DE VENDAS|1820,00|R|

Vale observar, também, que ao listar as informações dos registros J100 e J150 as mesmas serão mostradas ordenadas pelo código da conta contábil.
