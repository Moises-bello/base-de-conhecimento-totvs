---
content_hash: a1c9477aa3e52d5822c83cf060ff29b9058a71ab9efa85eedad94e1c33a71783
fetched_at: '2026-06-29T00:10:24.978470+00:00'
page_id: '500295829'
product: rm
source: tdn-rm
title: Contribuição Previdenciária sobre a Receita Bruta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=500295829
version: 41
---

Conforme Legislação, as Empresas submetidas ao regime de tributação com base no lucro presumido que tenham adotado o regime de caixa como critério de apuração tributária para IRPJ, CSLL e para as Contribuições de PIS e COFINS, poderão adotar o mesmo critério para a CPRB.

Empresas submetidas ao regime de Tributação do Lucro Real, deve apurar a CPRB pelo Regime de Competência.

**Regime de competência**: as apurações são feitas com base na prestação do serviço/venda independentemente de terem sido recebidos.

**Regime de caixa**: As receitas e despesas da empresa só são contabilizadas quando ocorrer recebimento ou pagamento e não quando são negociadas, compradas ou vendidas. Dessa forma a empresa só é tributada pelos valores recebidos e não os valores registrados no momento de emissão da Nota Fiscal.

Mais informações

[http://www.receita.fazenda.gov.br/publico/Legislacao/SolucoesConsultaCosit/2014/SCCosit402014.pdf](http://www.receita.fazenda.gov.br/publico/Legislacao/SolucoesConsultaCosit/2014/SCCosit402014.pdf "Follow link")

[http://www.planalto.gov.br/ccivil\_03/\_ato2011-2014/2011/lei/l12546.htm](http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12546.htm "Follow link")

**Regime de Competência:**

**Regime de Caixa:**

# Período de Apuração

false1true1Período de Apuração

A apuração da CPRB será feita através do processo de encerramento do Período de Apuração do referido Tributo.

Não é necessário que o encerramento seja feito em cada filial. Ao encerrar o Período de Apuração da CPRB na Matriz o períodos de todas as outras serão encerrados também.

No Período de Apuração da CPRB da Matriz serão mostrados os valores apurados para ela (Aba Contribuição Previdenciária) e os valores consolidados (Contribuição Previdenciária Consolidada). Nas demais Filiais serão demonstrados somente seus respectivos valores.

O processo de reabertura dos Períodos de Apuração abrirá somente o da Filial corrente. Os demais deverão ser reabertos um a um. Caso se tratem de muitas Filiais o processo Reabrir Múltiplos Períodos e Apuração poderá ser utilizado.

2Código de Atividade Econômica

A partir da **12.1.27** na apuração do tributo CPRB Regime de Competência será considerado o código da atividade vinculado ao lançamento de outros débitos e créditos CPRB.

Quando não informado, o código de atividade econômica no lançamento de outros débitos e créditos, o lançamento de ajuste não será agrupado e ficará sem o código de atividade no Período de Apuração.

O Lançamento de Ajuste afetará a Base de Cálculo na apuração da atividade e consequentemente o Valor da Contribuição.

NotaA implementação tem efeito em períodos CPRB a partir de 01/2020.Imagem3Caso onde há Proporção das Receitas Desoneradas

O cálculo da proporção será realizado através da soma do campo “**Valor Total do Faturamento**” subtraída da soma do campo “**Valor Exclusões Faturamento**” informados no Período de Apuração de cada filial, **ANTES** do encerramento do período, em relação ao somatório das receitas correspondente a cada Código de Atividade gerado no Detalhamento do período e possíveis valores a serem deduzidos do faturamento conforme orienta a [Instrução Normativa RFB nº 1436, de 30 de dezembro de 2013 Art. 3º](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=48917&visao=anotado) .

De posse desse fator, o sistema terá dois comportamentos distintos[[1]](#_ftn1):

1. Se o total da **Receita Desonerada for maior ou igual a 95%** do total das receitas:
   1. Caso o total da Receita Desonerada não seja 100% do total do faturamento informado no Período, o sistema deve inserir mais um registro no Detalhamento da Filial Matriz com o Código de Atividade "**99999999**" com o valor da diferença entre o total das receitas desoneradas e o valor total do faturamento consolidado informado no Período de Apuração. Esse detalhamento será inserido para o Código de Receita informado no Cadastro do Tributo e alíquota será aplicada conforme informado previamente no período de apuração da contribuição previdenciária.

1. O valor do **Saldo Devedor** do Tributo no Período deve corresponder ao somatório da **Contribuição Previdenciária**, mais **ajustes de acréscimos**, menos **ajustes de redução**, consolidados no detalhamento da Filial Matriz. No Exemplo acima, o saldo devedor retornaria o valor de **$ 716,00** (431,00 + 300,00 – 15,00).

1. Se a **Receita Desonerada for inferior a 5%** do total da receita:

1. O Saldo Devedor do Tributo é zero.

Alteração: O código de atividade do caso I. a será gerado conforme regra abaixo.

Preenchimento do Código da Atividade:

**Se** Alíquota Apuração igual a 1% **Então** "99990010"

**Senão** **Se** Alíquota Apuração igual a 1.5% **Então** "99990015"

**Senão** **Se** Alíquota Apuração igual a 2.5% **Então** "99990025"

**Senão** **Se** Alíquota Apuração igual a 3% **Então** "99990030"

**Senão** **Se** Alíquota Apuração igual a 4.5% **Então** "99990045"

**Senão** "99999999".

Nota

###### [[1]](#_ftnref1) Comportamento necessário para tratar as alterações da Lei nº 12.715/2012 que retira, totalmente, a aplicação da desoneração da folha para as empresas que se dediquem a outras atividades, além das previstas no Anexo da Lei 12.546/2011, cuja receita bruta decorrente dessas outras atividades seja igual ou superior a 95% da receita bruta total.
