---
content_hash: 19c864ba5768892068aae805602755bc99b04c9e768404cf2de9d79e9e573ead
fetched_at: '2026-06-29T00:08:20.180498+00:00'
page_id: '268570059'
product: rm
source: tdn-rm
title: TVJULV_DT_Legislação_ECF_Automatismo_Lançamentos_Lalur_B
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268570059
version: 7
---

### ECF - Escrituração Contábil Fiscal

### Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Fiscal* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *ECF* | *Escrituração Contábil Fiscal* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Contas* | *Cadastro Contas Lalur parte B* | | *Lançamentos* | *Cadastros de Lançamentos Lalur parte B* | | *Encerramento* | *Encerramento do Período de Apuração* | | *Evento Tribuário* | *Cadastro do Evento Tributário* | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** | *Não se Aplica* |
| **Ponto de Entrada:** | *Não se Aplica* |
| **Chamados Relacionados** | *TVJULV* |
| **Requisito (ISSUE):** | *FIS000428* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server; Oracle* |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** | Windows |

# Legislação

## Descrição

O presente documento presta-se a especificar os automatismos do Lalur – Parte B passíveis de implementação no sistema de Gestão Fiscal – Linha RM.

## Introdução

Primeiramente, é preciso esclarecer que nem todo valor adicionado ou excluído na apuração do lucro real, precisa ser controlado na Parte B do Lalur.  

Devem ser controlados na Parte B do LALUR os valores que irão influenciar a determinação do lucro real em períodos de apuração futuros e que não constem na escrituração contábil *(lista exemplificativa, não taxativa):*  

* Prejuízos a compensar em períodos subsequentes,
* Lucro não realizado decorrente de contratos com órgãos públicos,
* Perdas excedentes aos ganhos auferidos no mercado de renda variável,
* Provisões não dedutíveis,
* Depreciação acelerada incentivada,
* Exaustão mineral com base na receita bruta,
* Valores excedentes das contas de despesas com programas de alimentação do trabalhador.

 

*Art. 262.  No LALUR, a pessoa jurídica deverá (Decreto-Lei nº 1.598, de 1977, art. 8º, inciso I):*

 

*III - manter os registros de controle de **prejuízos fiscais a compensar** em períodos de apuração subsequentes, do **lucro inflacionário a realizar**, da **depreciação acelerada incentivada**, da **exaustão mineral**, com base na receita bruta, bem como dos **demais valores que devam influenciar a determinação do lucro real de períodos de apuração futuros e não constem da escrituração comercial**;* 

*IV - manter os registros de controle dos valores excedentes a serem utilizados no cálculo das deduções nos períodos de apuração subsequentes, dos dispêndios com **programa de alimentação ao trabalhador**, **vale-transporte** e **outros previstos neste Decreto**. (RIR/99) (grifo nosso)*

 

Em segundo lugar, é primordial entender que:

 

* Um valor **adicionado** na Parte A em determinado período de apuração e que precisa ser controlado na Parte B, será utilizado nos períodos subsequentes para **EXCLUSÃO**, ou seja, vão reduzir o lucro;
* Inversamente, um valor **excluído** na Parte A que precisa ser controlado na Parte B, será utilizado como **ADIÇÃO** nos períodos subsequentes, aumentando o lucro.

Portanto, via de regra, no período de apuração em que ocorreu o **fato contábil**, ou seja, o registro na escrituração comercial, a origem da adição/exclusão na Parte A é o registro contábil, a contabilidade. **Nos períodos subsequentes**, ao reverter aquele lançamento, a origem da exclusão/adição será a Parte B do Lalur. Existem exceções.

 

Por fim, mas, não menos importante, é preciso conhecer a sistemática dos débitos e créditos que se aplica ao Lalur:

|  |  |  |
| --- | --- | --- |
| **Efeito na Parte A** | **A Conta na Parte B possui Natureza:** | **Lançamento na conta da**  **Parte B** |
| **ADIÇÕES** | **Credora** |  |
| Constituição de saldo para posterior adição \* |  | Lançamento à CRÉDITO \* |
| Utilização de saldo para adição (baixa do saldo) |  | Lançamento à DÉBITO |
|  |  |  |
| **EXCLUSÕES e COMPENSAÇÃO DE PREJUÍZO** | **Devedora** |  |
| Constituição de saldo para posterior exclusão/compensação \* |  | Lançamento à DÉBITO \* |
| Utilização de saldo para exclusão (baixa do saldo) |  | Lançamento à CREDITO |

 

*\* No sistema de Gestão Fiscal da Linha RM, o Tipo “**Constituição de Saldo**” possui exatamente este comportamento.*

 As situações que passamos a discorrer são apenas algumas das mais comuns, não sendo o objetivo exaurir o assunto, mas, listando e entendendo estes casos, ter a noção do que pode ser feito no sistema de Gestão Fiscal para automatizar os lançamentos que serão necessários na Parte B do Lalur.

1. 1. ## ADIÇÕES (controle de valores a serem adicionados)

As adições equivalem a despesas contabilizadas (que reduziram o lucro contábil), mas, que são consideradas como indedutíveis pela legislação tributária, portanto, precisam ser adicionadas novamente ao lucro para anular o efeito anterior.

* + ### Ajuste a Valor Presente de Passivo - AVP (IN RFB nº 1.515/14, arts. 37 à 39)

Todos os elementos do passivo quando originados de operações a longo prazo devem ser ajustados a valor presente de forma a possibilitar o reconhecimento de despesas financeiras embutidas nessas operações pela sua competência. O mesmo tratamento deve-se dar às operações de curto prazo quando o efeito for relevante.

*Art. 37. Os valores decorrentes do ajuste a valor presente, de que trata o inciso III do caput do art. 184 da Lei nº 6.404, de 1976, relativos a cada operação, somente serão considerados na determinação do lucro real no período de apuração em que:*

**Nota:** Lei 6.404/76, Art. 184. No balanço, os elementos do passivo serão avaliados de acordo com os seguintes critérios: [...] III – as obrigações, os encargos e os riscos classificados no passivo não circulante serão ajustados ao seu valor presente, sendo os demais ajustados quando houver efeito relevante.

*I - o bem for revendido, no caso de aquisição a prazo de bem para revenda;*

*II - o bem for utilizado como insumo na produção de bens ou serviços, no caso de aquisição a prazo de bem a ser utilizado como insumo na produção de bens ou serviços;*

*III - o ativo for realizado, inclusive mediante depreciação, amortização, exaustão, alienação ou baixa, no caso de aquisição a prazo de ativo não classificável nos incisos I e II do caput;*

*IV - a despesa for incorrida, no caso de aquisição a prazo de bem ou serviço contabilizado diretamente como despesa; e*

*V - o custo for incorrido, no caso de aquisição a prazo de bem ou serviço contabilizado diretamente como custo de produção de bens ou serviços.*

*§ 1º Nas hipóteses previstas nos incisos I, II e III do caput, os valores decorrentes do ajuste a valor presente deverão ser evidenciados contabilmente em **subconta** **vinculada ao ativo**.*

[...]

*Art. 38. Na aquisição a prazo sujeita ao ajuste a valor presente a que se refere o art. 37, os valores decorrentes do ajuste a valor presente serão registrados a débito em conta de juros a apropriar ou equivalente.*

*§ 1º Nas hipóteses previstas nos incisos I, II ou III do caput do art. 37, os valores decorrentes do ajuste a valor presente serão registrados a crédito na subconta mencionada no § 1º do mesmo artigo, em contrapartida à conta de juros a apropriar ou equivalente mencionada no caput deste artigo.*

***§ 2º Os valores apropriados como despesa a partir da conta de juros a apropriar ou equivalente serão adicionados ao lucro líquido na determinação do lucro real nos períodos de apuração relativos às apropriações.***

*§ 3º Na hipótese prevista no inciso I do caput do art. 37, o valor evidenciado na subconta de que trata o § 1º deste artigo será baixado no período de apuração em que o bem for revendido.*

*§ 4º Na hipótese prevista no inciso II do caput do art. 37, o valor evidenciado na subconta de que trata o § 1º deste artigo será baixado no período de apuração em que o bem for utilizado como insumo na produção de bens ou serviços.*

*[...]*

***§ 6º O valor da subconta baixado conforme os §§ 3º ou 4º poderá ser excluído do lucro líquido na determinação do lucro real no período de apuração relativo à baixa.***

**Nota**: A exclusão dos valores na Parte A terá como origem a subconta vinculada à conta de ativo quando da baixa do mesmo.

*§ 7º Na hipótese prevista no inciso III do caput do art. 37, o valor evidenciado na subconta de que trata o § 1º deste artigo será baixado à medida que o ativo for realizado, inclusive mediante depreciação, amortização, exaustão, alienação ou baixa.*

*§ 8º No caso de ativo depreciável, amortizável ou exaurível, em que o controle é feito com a utilização de uma subconta para cada conta conforme disposto no § 2º do art. 33, a baixa relativa à depreciação, amortização ou exaustão a que se refere o § 7º deste artigo será feita por meio de registro a débito na subconta vinculada à conta de depreciação acumulada, amortização acumulada ou exaustão acumulada.*

***§ 9º Caso o valor realizado do ativo seja dedutível, o valor da subconta baixado conforme o § 7º poderá ser excluído do lucro líquido na determinação do lucro real no período de apuração relativo à baixa.***

**Nota**: A exclusão dos valores na Parte A terá como origem a subconta vinculada à conta de depreciação acumulada.

*[...]*

***§ 11. Na hipótese prevista no inciso IV do caput do art. 37, caso a despesa seja dedutível, os valores decorrentes do ajuste a valor presente de que trata o caput deste artigo poderão ser excluídos do lucro líquido na determinação do lucro real no período de apuração em que a despesa for incorrida.***

*[...]*

***§ 13. Na hipótese prevista no inciso V do caput do art. 37, os valores decorrentes do ajuste a valor presente de que trata o caput deste artigo poderão ser excluídos do lucro líquido na determinação do lucro real no período de apuração em que o custo for incorrido.***

***§ 14. As adições e exclusões relativas às hipóteses previstas nos incisos IV e V do caput do art. 37 serão controladas na Parte B do Lalur.***

Aspecto Contábil

As normas contábeis determinam que o reconhecimento inicial das dívidas em operações de longo prazo deve se dar pelo seu valor justo. Dessa forma, é possível adequar os encargos financeiros da operação ao regime de competência.

O registro contábil deve ser feito a débito de conta redutora da conta de **Fornecedores a Pagar** e a crédito de conta redutora do **ativo** ou da **despesa** equivalente (art. 38 e § 1º do art. 37 da IN nº 1.515/14).

|  |  |  |  |
| --- | --- | --- | --- |
| Exemplo: | | | |
| D | Ativo / Resultado | Imobilizado/Despesa | 120.000,00 |
| C | Ativo / Resultado | (-) Ajuste a valor presente | 20.000,00 |
| C | Passivo | Fornecedores a pagar | 120.000,00 |
| D | Passivo | (-) Provisão de ajuste a valor presente | 20.000,00 |

Aspecto Fiscal

Para fins tributários, **o valor do ajuste a valor presente contabilizado em conta redutora da despesa deve ser excluído do lucro líquido no mesmo período do reconhecimento da despesa**. Já os valores contabilizados em conta redutora do ativo, serão excluídos do lucro líquido quando o ativo for realizado, inclusive por depreciação, amortização, exaustão, alienação ou baixa.

Os valores apropriados como despesa financeira a partir da conta de provisão para AVP devem ser **adicionados** ao lucro líquido uma vez que sua dedutibilidade já foi registrada anteriormente.

Para a adição dos valores na Parte A, a origem desses valores será contábil no caso de adoção de subcontas. Se não for adotada subconta, o valor do ajuste a valor presente precisa ser controlado na Parte B do Lalur, em conta com natureza de adição. Daí a origem dessa adição passa a ser a Parte B.

* + 1º momento (período do reconhecimento da despesa): **exclusão**.
    - Origem do lançamento na Parte A: Contábil
    - Efeito na Parte B: constituição de saldo em conta de adição.

* + 2º momento (períodos posteriores, quando da apropriação da despesa financeira): **adição**.
    - Origem do lançamento na Parte A: Contábil
    - Efeito na Parte B: baixa de saldo em conta de adição.

A legislação tributária dispensa o controle na Parte B do Lalur nos casos de utilização de subconta para itens do ativo e passivo:

*Art. 33. As subcontas de que trata esta Seção serão analíticas e registrarão os lançamentos contábeis em último nível.*

*[...]*

*§ 6º **O controle por meio de subcontas de que trata esta Seção dispensa o controle dos mesmos valores na Parte B do Lalur**. (IN RFB nº 1.515/14)*

* + ### Depreciação de Bens do Ativo Imobilizado (IN RFB nº 1.515/14, arts. 65 à 68)

A depreciação de um ativo consiste em registrar contabilmente a redução de valor do bem devido ao desgaste do mesmo no tempo, seja por uso, desgaste natural ou obsolescência. Essa redução é lançada como custo ou encargo e será dedutível para fins tributários.

A quota de depreciação será determinada com base nos prazos de vida útil e nas taxas de depreciação constantes dos anexos da Instrução Normativa SRF n° 162/98. Se a empresa utilizar cota de depreciação inferior àquela determinada pela IN a diferença poderá ser excluída do lucro líquido na apuração do lucro real com registro na Parte B do Lalur do valor excluído.

A partir do momento em que a depreciação fiscal do bem atingir 100% de seu valor de aquisição, o valor da depreciação contábil passa a ser adicionado ao lucro líquido para determinação do lucro real, com a respectiva baixa na conta da Parte B do Lalur.

*Seção XI - Da Depreciação de Bens do Ativo Imobilizado*

*Art. 65. Poderá ser computada como custo ou encargo, em cada exercício, a importância correspondente à diminuição do valor dos bens do ativo não circulante imobilizado resultante do desgaste pelo uso, ação da natureza e obsolescência normal.*

*[...]*

*§ 2º A quota de depreciação é dedutível a partir da época em que o bem é instalado, posto em serviço ou em condições de produzir.*

***§ 3º Em qualquer hipótese, o montante acumulado das quotas de depreciação não poderá ultrapassar o custo de aquisição do bem.***

*[...]*

*Subseção II - Da Quota de Depreciação*

***Art. 67. A quota de depreciação dedutível na apuração do imposto será determinada mediante a aplicação da taxa anual de depreciação sobre o custo de aquisição do bem.***

*[...]*

*Subseção III - Da Taxa Anual de Depreciação*

*Art. 68. A taxa anual de depreciação será fixada em função do prazo durante o qual se possa esperar a utilização econômica do bem pelo contribuinte, na produção dos seus rendimentos.*

***§ 1º O prazo de vida útil admissível é aquele estabelecido nos Anexos I e II da Instrução Normativa SRF nº 162, de 31 de dezembro de 1998, ficando assegurado ao contribuinte o direito de computar a quota efetivamente adequada às condições de depreciação dos seus bens, desde que faça a prova dessa adequação, quando adotar taxa diferente.***

*[...]*

***§ 4º Caso a quota de depreciação registrada na contabilidade do contribuinte seja menor do que aquela calculada com base no § 1º, a diferença poderá ser excluída do lucro líquido na apuração do lucro real com registro na Parte B do Lalur do valor excluído, observando-se o disposto no § 3º do art. 65.***

***§ 5º Para fins do disposto no § 4º, a partir do período de apuração em que o montante acumulado das quotas de depreciação computado na determinação do lucro real atingir o limite previsto no § 3º do art. 65, o valor da depreciação, registrado na escrituração comercial, deverá ser adicionado ao lucro líquido para efeito de determinação do lucro real com a respectiva baixa na Parte B do Lalur.***

* + 1º momento (durante o período de depreciação fiscal do bem): **exclusão**.
    - Origem do lançamento na Parte A: Patrimonial
    - Efeito na Parte B: constituição de saldo em conta de adição.

* + 2º momento (quando a depreciação fiscal atingir 100% de seu valor de aquisição): **adição**.
    - Origem do lançamento na Parte A: Patrimonial
    - Efeito na Parte B: baixa de saldo em conta de adição.
  + ### Custos de Empréstimos (IN RFB nº 1.515/14, art. 73)

Geralmente, custos com empréstimos são contabilizados como despesas financeiras. Entretanto, caso o empréstimo tenha sido tomado para aquisição, construção ou produção de ativo qualificável como estoque de longa maturação, propriedade para investimento, etc., estes custos podem ser contabilizados como parte do custo do bem, a débito no ativo imobilizado.

*Seção XV - Dos Custos de Empréstimos*

***Art. 73. Os juros e outros encargos, associados a empréstimos contraídos, especificamente ou não, para financiar a aquisição, construção ou produção de bens classificáveis como estoques de longa maturação, propriedade para investimento, ativo imobilizado ou ativo intangível podem ser registrados como custo do ativo adquirido, construído ou produzido.***

*[...]*

***§ 3º Os juros e outros encargos registrados como custo do ativo, conforme a hipótese prevista no caput, poderão ser excluídos na determinação do lucro real do período de apuração em que forem incorridos, devendo a exclusão ser feita na Parte A do Lalur e controlada, de forma individualizada para cada bem ou grupo de bens de mesma natureza e uso, na Parte B.***

***§ 4º Na hipótese prevista no § 3º, os valores excluídos deverão ser adicionados, na Parte A do Lalur, à medida que o ativo for realizado, inclusive mediante depreciação, amortização, exaustão, alienação ou baixa.***

Aspecto Contábil

De acordo com o CPC 20, os custos de empréstimos incorridos com ativos qualificáveis devem ser capitalizados, ou seja, contabilizados a débito no ativo imobilizado.

Aspecto Fiscal

Para alinhamento do tratamento fiscal às normas atuais de contabilização dos custos de empréstimos, a legislação tributária fornece ao contribuinte duas opções de dedução dos custos dos encargos com empréstimos quando os mesmos forem tomados para aquisição, construção ou produção de ativo qualificável:

* + **Através da realização do ativo** – neste caso, a dedução fiscal dos custos acontece na realização do ativo (depreciação, amortização, exaustão, alienação ou baixa). Não são necessários ajustes na apuração do lucro real.

* + **Quando incorridos os custos (competência)** – neste caso, deve-se excluir os custos quando da ocorrência dos mesmos e adicioná-los quando ocorrer a realização do ativo:

ü  1º momento (quando da ocorrência dos custos): **exclusão**.

* + Origem do lançamento na Parte A: Contábil
  + Efeito na Parte B: constituição de saldo em conta de adição.

ü  2º momento (quando da realização do ativo por depreciação, amortização, exaustão, alienação ou baixa): **adição**.

* + Origem do lançamento na Parte A: Contábil
  + Efeito na Parte B: baixa de saldo em conta de adição.

* + ### Contratos de Concessão de Serviços Públicos (IN RFB nº 1.515/14, art. 81 à 85)

Com o intuito de atrair o setor privado para participar do desenvolvimento, financiamento, operação e manutenção dos serviços públicos oferecidos, o governo tem celebrado contratos de prestação de serviços onde um concessionário constrói ou melhora uma infraestrutura já existente, operando-a e mantendo-a por determinado tempo recebendo por estes serviços.

*Seção XX - Dos Contratos de Concessão de Serviços Públicos*

*[...]*

*Subseção I - Do Diferimento da Tributação do Lucro - Ativo Intangível*

***Art. 82. No caso em que a concessionária reconhece como receita o direito de exploração recebido do poder concedente, o resultado decorrente desse reconhecimento deverá ser computado no lucro real à medida que ocorrer a realização do respectivo ativo intangível, inclusive mediante amortização, alienação ou baixa.***

*[...]*

***§ 2º O valor apurado na forma prevista no § 1º deverá ser excluído na Parte A do Lalur, na determinação do lucro real, e controlado na Parte B, para ser adicionado na proporção em que o ativo intangível for realizado, inclusive por amortização, alienação ou baixa.***

*Subseção II - Do Diferimento da Tributação do Lucro - Ativo Financeiro*

***Art. 83. O lucro decorrente da receita reconhecida na fase de construção cuja contrapartida seja ativo financeiro representativo de direito contratual incondicional de receber caixa ou outro ativo financeiro, poderá ser tributado à medida do efetivo recebimento.***

*[...]*

***§ 2º Para fins do diferimento de que trata o caput, a concessionária deverá realizar os seguintes ajustes no Lalur:***

***I - exclusão do lucro referido no § 1º, com registro na Parte B do valor excluído;***

***II - adição do lucro diferido conforme o inciso I, na proporção dos recebimentos, e respectiva baixa na Parte B;***

*§ 3º Em cada período de apuração, o valor a ser adicionado conforme o inciso II do § 2º será calculado pela aplicação da seguinte fórmula:*

*VALOR A SER ADICIONADO = LD X (R/V),*

*onde os símbolos significam:*

*LD = total do lucro diferido na fase de construção, conforme o inciso I do § 2º*

*R = valor do(s) pagamento(s) contratado(s), recebido(s) no período de apuração*

*V = valor total contratado*

*[...]*

Aspecto Contábil

De acordo com os procedimentos contábeis, a infraestrutura construída/melhorada não deve ser registrada como ativo imobilizado do concessionário.

Os custos com a obra e o reconhecimento das receitas correspondentes devem ser contabilizados à medida que a atividade de construção/melhoria da obra avança. No caso das receitas, o lançamento será em contrapartida do ativo financeiro (quando não assume o risco da demanda) ou intangível (quando assume o risco da demanda).

Aspecto Fiscal

O lucro reconhecido a partir das receitas apropriadas relativas ao direito de exploração recebido da concedente deve afetar o cálculo do lucro real apenas com a realização do respectivo ativo, financeiro ou intangível, inclusive por amortização, alienação ou baixa.

Portanto, o valor reconhecido como receita deve ser excluído do lucro líquido e controlado na Parte B do Lalur para ser adicionado à medida que o ativo for sendo realizado.

* + 1º momento (durante o avanço da obra de construção/melhoria): **exclusão**.
    - Origem do lançamento na Parte A: Contábil
    - Efeito na Parte B: constituição de saldo em conta de adição.

* + 2º momento (quando da realização do ativo): **adição**.
    - Origem do lançamento na Parte A: Contábil
    - Efeito na Parte B: baixa de saldo em conta de adição.
  + ### Investimentos avaliados pelo método de equivalência patrimonial (MEP) – (IN RFB nº 1.515/14, arts. 92 à 97)

**Incorporação**: uma ou mais sociedades são absorvidas por outra que lhes sucede em direitos e obrigações e a sociedade incorporada deixa de existir[[1]](file:///C:/Users/paulo.rocha.BH01/Desktop/Automatismo%20LALUR%20B/Lalur%20-%20automatismos_2.docx#_ftn1).

**Fusão**: duas ou mais sociedades se unem para formar uma nova sociedade que lhes sucederá em direitos e obrigações e as sociedades fusionadas são extintas¹.

**Cisão**: a companhia transfere parte de seu patrimônio para uma ou mais sociedades, extinguindo-se a sociedade cindida caso a totalidade de seu patrimônio seja transferido¹.

A avaliação de participações societárias pelo método de equivalência patrimonial (MEP) é obtida aplicando-se o percentual de participação que a investidora tem no capital social da investida sobre o valor contábil do patrimônio líquido desta.

Nesta operação pode ocorrer ágio, quando o preço de aquisição for superior ao valor patrimonial do investimento, ou compra vantajosa (deságio), quando o preço de aquisição for inferior ao valor patrimonial do investimento. A apuração se o investimento rendeu ágio ou deságio para a empresa, precisa ser efetuada no momento da aquisição do investimento.

*Seção XXII - Das Participações em Coligadas e Controladas*

*Subseção I - Do Desdobramento do Custo de Aquisição com Base em Laudo*

*Art. 92. O contribuinte que avaliar investimento pelo valor de patrimônio líquido deverá, por ocasião da aquisição da participação, desdobrar o custo de aquisição em:*

*I - **valor de patrimônio líquido** na época da aquisição, determinado de acordo com o disposto no art. 93;*

*II - **mais ou menos-valia**, que corresponde à diferença entre o valor justo dos ativos líquidos da investida, na proporção da porcentagem da participação adquirida, e o valor de que trata o inciso I; e*

*III - **ágio por rentabilidade futura (goodwill)**, que corresponde à diferença entre o custo de aquisição do investimento e o somatório dos valores de que tratam os incisos I e II do caput.*

***§ 1º Os valores de que tratam os incisos I a III do caput serão registrados em subcontas distintas.***

*[...]*

*§ 10. O ganho proveniente de compra vantajosa de que trata o § 9º, que corresponde ao excesso do valor justo dos ativos líquidos da investida, na proporção da participação adquirida, em relação ao custo de aquisição do investimento, será computado na determinação do lucro real no período de apuração da alienação ou baixa do investimento.*

***§ 11. O ganho proveniente de compra vantajosa registrado em conta de resultado deverá ser registrado no Lalur como:***

***I - exclusão ao lucro líquido para apuração do lucro real na Parte A e registro na Parte B do valor excluído, quando do seu reconhecimento; e***

***II - adição ao lucro líquido para apuração do lucro real na Parte A e respectiva baixa na Parte B, quando da apuração do ganho ou perda de capital na alienação ou baixa do investimento.***

*[...]*

Aspecto Contábil

O registro contábil do investimento no Balanço Patrimonial é feito pelo valor patrimonial somado ao ágio, ou subtraído do deságio.

A Lei nº 12.973/14 alterou a disposição do Decreto-Lei nº 1.598/77, determinando que os valores do i) patrimônio líquido a valor justo, ii) da mais ou menos-valia de ativos e iii) do ágio por rentabilidade futura (goodwill) devem ser registrados em subcontas distintas (Art. 20, § 1º).

**a)** **Exemplo de menos-valia e ágio - registro inicial**[[2]](file:///C:/Users/paulo.rocha.BH01/Desktop/Automatismo%20LALUR%20B/Lalur%20-%20automatismos_2.docx#_ftn2)**:**

No reconhecimento inicial do investimento, o valor da menos-valia é registro em subconta redutora do investimento. Exemplo:

Alfa comprou 100% das ações do capital social de Beta por R$ 620 que possui a seguinte situação patrimonial:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Valor Contábil** | **Valor Justo** | **Menos-Valia** |
| Ativos | 500,00 | 450,00 | (50,00) |
| Passivos | (100,00) | (100,00) | 0 |
| Valor líquido | 400,00 | 350,00 | (50,00) |

A apuração do ágio se dá da seguinte for

|  |  |
| --- | --- |
| Custo de aquisição | 620,00 |
| Valor justo dos ativos líquidos de Beta | 350,00 |
| **Valor do ágio (custo – valor justo dos ativos)** | **270,00** |

O registro contábil inicial da aquisição em Alfa:

|  |  |  |  |
| --- | --- | --- | --- |
| Registro inicial da aquisição do investimento: | | | |
| D | Ativo | Investimento – valor patrimonial pela escrituração comercial | 400,00 |
| D | Ativo | Investimento – ágio | 270,00 |
| C | Ativo | (-) Investimento – menos valia de ativo | 50,00 |
| C | Ativo | Bancos | 620,00 |

O valor da mais ou menos-valia de ativos, está sujeito à depreciação, amortização ou exaustão, o que se aplicar.

**b)** **Exemplo de ganho proveniente de compra vantajosa**

O ganho proveniente de compra vantajosa, que é definido quando o valor dos ativos líquidos da investida é maior que o custo da aquisição, deve ser reconhecido no resultado do exercício, na data de aquisição.

Exemplo de contabilização:

Alfa comprou 100% das ações do capital social de Beta por R$ 500 que possui a seguinte patrimonial:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Valor Contábil** | **Valor Justo** | **Mais ou Menos Valia** |
| Ativos | 500,00 | 650,00 | 150,00 |
| Passivos | (100,00) | (100,00) | 0 |
| Valor líquido | 400,00 | 550,00 | 150,00 |

A apuração do ágio se dá da seguinte forma:

|  |  |
| --- | --- |
| Custo de aquisição | 500,00 |
| Valor justo dos ativos líquidos de Beta | 550,00 |
| **Compra vantajosa (custo – valor justo dos ativos)** | **(50,00)** |

O registro contábil inicial da aquisição:

|  |  |  |  |
| --- | --- | --- | --- |
| Registro inicial da aquisição do investimento: | | | |
| D | Ativo | Investimento – valor patrimonial pela escrituração comercial | 400,00 |
| D | Ativo | Investimento – mais valia de ativo | 150,00 |
| C | Ativo | Bancos | 500,00 |
| **C** | **Resultado** | **Ganho com compra vantajosa de investimento** | **50,00** |

**c)** **Redução da menos-valia**

A redução da menos-valia, seja por depreciação, amortização ou exaustão, deve ser feita em contrapartida no resultado da empresa.

Aspecto Fiscal

**a)** **Exemplo de menos valia de ativo e ágio - registro inicial:**

Neste caso, não há impacto fiscal.

**b)** **Ganho proveniente de compra vantajosa**

O ganho proveniente de compra vantajosa, registrado contabilmente no resultado na data de aquisição, deve ser excluído do lucro líquido para determinação do lucro real do período. Esse valor deve ser registrado na Parte B do Lalur para ser adicionado quando da alienação ou baixa do investimento (IN SRF nº 1.515/14, art. 92, §10).

**c)** **Redução da menos-valia**

No caso da redução da menos-valia, registrada no resultado do exercício, deve ser excluído do lucro líquido para apuração do lucro real. O valor excluído deve ser controlado na Parte B para adição quando da apuração do ganho ou perda de capital na alienação ou liquidação do investimento.

*Art. 96. A contrapartida da redução dos valores de que tratam os incisos II e III do caput do art. 92 registrada em conta de resultado não será computada na determinação do lucro real, observado o disposto no art. 98.*

*Parágrafo único. A contrapartida a que se refere o caput deverá ser registrada no Lalur como:*

*[...]*

***II - exclusão ao lucro líquido para apuração do lucro real Parte A, relativamente à menos-valia, e controlada na Parte B para adição futura quando da apuração do ganho ou perda de capital na alienação ou liquidação do investimento.***

Observação: a aquisição de Participação Societária em Estágios (art. 97) possui a mesma disciplina.

[[1]](file:///C:/Users/paulo.rocha.BH01/Desktop/Automatismo%20LALUR%20B/Lalur%20-%20automatismos_2.docx#_ftnref1) Conceitos extraídos do livro “**Regulamentação Fiscal das Normas Contábeis do IFRS e CPC**” – Almeida e Jachelli

[[2]](file:///C:/Users/paulo.rocha.BH01/Desktop/Automatismo%20LALUR%20B/Lalur%20-%20automatismos_2.docx#_ftnref2) Exemplo retirado do Livro “**Regulamentação Fiscal das Normas Contábeis do IFRS e CPC**” – Almeida e Jachelli (página 132)

* + ### Subvenções para investimento (IN RFB nº 1.515/14, art. 112)

Subvenção para investimento é a entrega de recursos públicos a entidade privada, concedido pelo governo com o objetivo de suportar determinado investimento em virtude do interesse público no desenvolvimento da atividade privada.

Aspecto contábil

Independente se a subvenção for recebida em dinheiro ou como redução do passivo, através da redução ou isenção de impostos, o valor recebido deve ser registrado no resultado do período como receita. Exemplo:

Considere:

|  |  |
| --- | --- |
| IR apurado antes do incentivo | 10.000,00 |
| Incentivo do Lucro da Exploração | (7.500,00) |
| Imposto a pagar | 2.500,00 |

Contabilização do imposto de renda:

|  |  |  |  |
| --- | --- | --- | --- |
| Registro inicial da aquisição do investimento: | | | |
| D | Resultado | Despesa de imposto de renda | 10.000,00 |
| C | Resultado | Receita de incentivo fiscal | 7.500,00 |
| C | Passivo | Imposto de renda a pagar | 2.500,00 |

Para que as subvenções para investimento não sejam tributadas, é imprescindível que os valores sejam registrados em conta de reserva de lucros específica. Exemplo do registro contábil:

|  |  |  |  |
| --- | --- | --- | --- |
| Registro inicial da aquisição do investimento: | | | |
| D | Patrimônio Líquido | Lucros Acumulados | 7.500,00 |
| C | Patrimônio Líquido | Reserva de incentivos fiscais | 7.500,00 |

Aspecto fiscal

Na apuração do lucro real, o valor registrado na conta de reserva de incentivos fiscais deve ser excluído da base de cálculo. O montante excluído deve ser controlado na Parte B do Lalur para serem adicionados ao lucro quando da utilizado do valor para aumento de capital ou nos casos previstos no § 2º do artigo 112 da IN RFB nº 1.515/14.

Observação: Comportamento similar possui o Prêmio na Emissão de Debêntures (art. 113).

* + ### Provisões não dedutíveis

As constituições de provisões são dedutíveis apenas quando o fato provisionado efetivamente ocorrer.

Neste caso, no período de apuração em que ocorrer o registro contábil da despesa, ela precisa ser adicionada ao lucro para que o efeito da despesa no resultado contábil seja anulado. Esse valor adicionado precisa ser registrado na Parte B do Lalur para ser excluído quando a perda provisionada ocorrer de fato.

Portanto, ao se criar a conta na Parte B para registro desse valor, ela terá Natureza de “**Exclusão**”. Seu saldo possuirá natureza devedora e os lançamentos nos períodos de apuração subsequentes, quando da utilização do saldo para diminuir o lucro, devem ser a crédito da conta. Esses lançamentos irão reduzir o saldo da conta, até que seja zerado.

* + ### EXCLUSÕES (controle de valores a serem excluídos)

As exclusões são valores que foram acrescentados ao resultado contábil, mas que pela legislação não devem compor a base de cálculo do imposto de renda e da contribuição social sobre o lucro líquido.

* + ### Ajuste a Valor Presente de ativos - AVP (IN RFB nº 1.515/14, arts. 34 e 35)

Todos os itens do ativo decorrentes de operações a longo prazo devem ser ajustados ao seu valor presente. As operações de curto prazo também devem ser ajustadas a valor presente quando seus efeitos forem relevantes.

*Art. 34. Os valores decorrentes do ajuste a valor presente, de que trata o inciso VIII do caput do art. 183 da Lei nº 6.404, de 1976, relativos a cada operação, somente serão considerados na determinação do lucro real no mesmo período de apuração em que a receita ou resultado da operação deva ser oferecido à tributação.*

**Nota:** Lei 6.404/76, Art. 183. No balanço, os elementos do ativo serão avaliados segundo os seguintes critérios: [...] VIII – os elementos do ativo decorrentes de operações de longo prazo serão ajustados a valor presente, sendo os demais ajustados quando houver efeito relevante.

*Art. 35. Na venda a prazo sujeita ao ajuste a valor presente a que se refere o art. 34, os valores decorrentes do ajuste a valor presente serão registrados a crédito em conta de juros a apropriar ou equivalente.*

*§ 1º Caso a receita da venda de que trata o caput deva ser classificada como receita bruta conforme previsto no art. 3º, os valores decorrentes do ajuste a valor presente deverão ser registrados a débito em conta de dedução da receita bruta, em contrapartida à conta de juros a apropriar ou equivalente mencionada no caput.*

***§ 2º Os valores apropriados como receita a partir da conta de juros a apropriar ou equivalente poderão ser excluídos do lucro líquido na determinação do lucro real nos períodos de apuração relativos às apropriações.***

***§ 3º Os valores decorrentes do ajuste a valor presente de que trata o caput serão adicionados ao lucro líquido na determinação do lucro real no período de apuração em que a receita ou resultado da venda deva ser oferecido à tributação.***

*§ 4º As adições e exclusões de que trata este artigo serão controladas na Parte B do Lalur.*

Aspecto Contábil

 De acordo com as normas contábeis, tanto as receitas como as contas a receber de clientes devem ser reconhecidas pelo valor justo. O objetivo do registro contábil do ajuste a valor presente é adequar os rendimentos financeiros das vendas a prazo ao regime de competência.

O registro contábil deve ser feito a débito de conta de resultado, redutora da conta de **Receita Bruta**, em contrapartida de conta de ativo, redutora da conta de **Contas a Receber**.

|  |  |  |  |
| --- | --- | --- | --- |
| Exemplo: | | | |
| D | Ativo | Contas a Receber | 120.000,00 |
| C | Ativo | (-) Provisão para ajuste a valor presente | 20.000,00 |
| C | Resultado | Receita Bruta | 120.000,00 |
| D | Resultado | (-) Ajuste a valor presente | 20.000,00 |

Aspecto Fiscal

A legislação tributária determina que o valor do ajuste a valor presente seja adicionado ao lucro líquido do período de apuração em que a receita equivalente foi oferecida à tributação (§ 3º, art. 35).

Determina, também, que o valor apropriado como receita a partir da conta de Provisão AVP seja excluído do lucro líquido, uma vez o valor cheio já foi oferecido à tributação no momento da venda (§ 2º, art. 35).

* + 1º momento (período do reconhecimento da receita): **adição**.
    - Origem do lançamento na Parte A: Contábil
    - Efeito na Parte B: constituição de saldo em conta de exclusão.

* + 2º momento (apropriação da receita a partir da provisão AVP): **exclusão**.
    - Origem do lançamento na Parte A: Contábil
    - Efeito na Parte B: baixa de saldo em conta de exclusão.
  + ### Despesas Pré-Operacionais ou Pré-Industriais (IN RFB nº 1.515/14, art. 72)

Todos os gastos realizados pela empresa a partir da data de sua constituição até a data de sua efetiva entrada em operação são denominadas despesas pré-operacionais ou pré-industriais.

***Art. 72. Para fins de determinação do lucro real, não serão computadas, no período de apuração em que incorridas, as despesas:***

*I - de organização pré-operacionais ou pré-industriais, inclusive da fase inicial de operação, quando a empresa utilizou apenas parcialmente o seu equipamento ou as suas instalações; e*

*II - de expansão das atividades industriais.*

***§ 1º As despesas referidas no caput poderão ser excluídas para fins de determinação do lucro real, em quotas fixas mensais e no prazo mínimo de 5 (cinco) anos, a partir:***

*I - do início das operações ou da plena utilização das instalações, no caso previsto no inciso I do caput; e*

*II - do início das atividades das novas instalações, no caso previsto no inciso II do caput.*

***§ 2º Os valores não computados no lucro real em decorrência do disposto no caput deverão ser adicionados na Parte A do Lalur e registrados na parte B para controle de sua utilização conforme previsto no § 1º.***

Aspecto Contábil

De acordo com os pronunciamentos contábeis, esses gastos são contabilizados diretamente na demonstração do resultado da empresa, como despesa.

Aspecto Fiscal

A legislação tributária permite que as despesas pré-operacionais ou pré-industriais sejam amortizadas no período de cinco anos contados a partir do início das operações da empresa. Portanto, o valor das despesas deve ser adicionado ao lucro líquido quando incorridas e controlado na Parte B do Lalur para ser excluído posteriormente.

* + 1º momento (período em que incorreram as despesas): **adição**.
    - Origem do lançamento na Parte A: Contábil
    - Efeito na Parte B: constituição de saldo em conta de exclusão.

* + 2º momento (no período de cinco anos contados a partir do início das operações da empresa): **exclusão**.
    - Origem do lançamento na Parte A: Parte B
    - Efeito na Parte B: baixa de saldo em conta de exclusão.

* + ### Redução ao valor recuperável de ativos (IN RFB nº 1.515/14, art. 74 e 75)

Em síntese, quando o valor contábil de um ativo (montante pelo qual está representando no balanço patrimonial) é superior ao valor de recuperação do mesmo, seja pelo seu uso ou pela sua venda, é necessário que a empresa faça o reconhecimento de perdas por desvalorização através de uma provisão.

*Seção XVI - Do Teste de Recuperabilidade*

***Art. 74. O contribuinte poderá reconhecer na apuração do lucro real somente os valores contabilizados como redução ao valor recuperável de ativos que não tenham sido objeto de reversão, quando ocorrer a alienação ou baixa do bem correspondente.***

*[...]*

***§ 3º A perda estimada de que trata o caput deverá ser adicionada na Parte A do Lalur no período de apuração em que for reconhecida, e registrada na Parte B para ser excluída conforme disposto no caput ou no § 1º, ou na reversão a que se refere o art. 75.***

*[...]*

Aspecto Contábil

O registro contábil do reconhecimento da provisão para perda do valor recuperável de ativos é realizado diretamente no resultado do período em contrapartida de conta redutora do ativo imobilizado.

Aspecto Fiscal

De acordo com o art. 74 da IN RFB nº 1.515/14, os valores equivalentes à perda com a redução ao valor recuperável de ativos devem ser reconhecidos na apuração do lucro real somente quando ocorrer a alienação ou baixa do bem correspondente.

Portanto, o valor da provisão para perda deve ser adicionado ao lucro na Parte A do Lalur no período em que for reconhecida. Esse valor deve ser controlado na Parte B do Lalur para ser excluído quando ocorrer a alienação ou baixa do ativo.

* + 1º momento (Teste de Recuperabilidade): **adição**.
    - Origem do lançamento na Parte A: Contábil
    - Efeito na Parte B: constituição de saldo em conta de exclusão.

* + 2º momento (na alienação ou baixa do ativo): **exclusão**.
    - Origem do lançamento na Parte A: Parte B
    - Efeito na Parte B: baixa de saldo em conta de exclusão.
  + ### Redução da mais-valia e do ágio por rentabilidade futura (goodwill) (IN RFB nº 1.515/14, art. 96, inc. I)

Mais-valia é a diferença positiva entre o valor justo dos ativos líquidos da investida e o valor do seu patrimônio líquido. O ágio, por sua vez, é considerado como valor adicional ao preço do patrimônio, na modalidade de "despesa", com base na previsão de lucros nos exercícios futuros.

*Redução da Mais-Valia ou Menos-Valia e do Goodwill*

*Art. 96. A contrapartida da redução dos valores de que tratam os incisos II e III do caput do art. 92 registrada em conta de resultado não será computada na determinação do lucro real, observado o disposto no art. 98.*

*Parágrafo único. A contrapartida a que se refere o caput deverá ser registrada no Lalur como:*

***I - adição ao lucro líquido para apuração do lucro real na Parte A, relativamente à mais-valia e ao ágio por rentabilidade futura (goodwill), e controlada na Parte B para exclusão futura quando da apuração do ganho ou perda de capital na alienação ou liquidação do investimento; e***

Aspecto Contábil

No reconhecimento inicial do investimento, o valor da mais-valia e do ágio são reconhecidos como subconta do investimento, sendo a mais-valia sujeita ao teste de recuperabilidade (impairment).

Exemplo: Alfa comprou 100% das ações do capital social de Beta por R$ 620 que possui a seguinte situação patrimonial:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Valor Contábil** | **Valor Justo** | **Mais-Valia** |
| Ativos | 500,00 | 650,00 | 150,00 |
| Passivos | (100,00) | (100,00) | 0 |
| Valor líquido | 400,00 | 550,00 | 150,00 |

A apuração do ágio se dá da seguinte forma:

|  |  |
| --- | --- |
| Custo de aquisição | 620,00 |
| Valor justo dos ativos líquidos de Beta | 550,00 |
| **Valor do ágio (custo – valor justo dos ativos)** | **70,00** |

O registro contábil inicial da aquisição em Alfa:

|  |  |  |  |
| --- | --- | --- | --- |
| Registro inicial da aquisição do investimento: | | | |
| D | Ativo | Investimento – valor patrimonial pela escrituração comercial | 400,00 |
| D | Ativo | Investimento – mais valia de ativo | 150,00 |
| D | Ativo | Investimento – ágio | 70,00 |
| C | Ativo | Bancos | 620,00 |

O valor da mais ou menos-valia de ativos, está sujeito à depreciação, amortização ou exaustão, o que se aplicar.

As amortizações da mais-valia e do ágio são contabilizadas como despesa em contrapartida das subcontas onde foram escriturados quando da aquisição do investimento.

 

Aspecto Fiscal

Os valores baixados das subcontas da mais-valia e do ágio, lançados como despesa no resultado contábil, devem ser adicionados no lucro líquido para apuração do lucro real e controlados na Parte B do Lalur para exclusão quando da apuração do ganho ou perda de capital na alienação ou liquidação do investimento (art. 96 da IN RFS nº 1515/14).

* + 1º momento (na depreciação, amortização ou exaustão do investimento): **adição**.
    - Origem do lançamento na Parte A: Contábil
    - Efeito na Parte B: constituição de saldo em conta de exclusão.

* + 2º momento (na apuração do ganho ou perda de capital na alienação ou liquidação do investimento): **exclusão**.
    - Origem do lançamento na Parte A: Parte B
    - Efeito na Parte B: baixa de saldo em conta de exclusão.

* + ### COMPENSAÇÃO DE PREJUÍZOS FISCAIS (IN RFB nº 1.515/14, arts. 115 à 120)

O lucro real, lucro líquido ajustado pelas adições e exclusões, pode ser reduzido pela compensação de prejuízos fiscais de períodos anteriores em até 30%.

Aspecto contábil

Não há.

Aspecto fiscal

O prejuízo fiscal/base negativa compensável para efeito de tributação é o que for apurado na demonstração do Lucro Real de determinado período.

Este prejuízo fiscal/base negativa deve ser registrado na Parte B do Lalur para controle da compensação nos períodos subsequentes, utilizando-se conta distinta para o prejuízo correspondente a cada período e tipo de prejuízo: Operacional ou Não Operacional.

No momento do encerramento do período de apuração, somente na apuração trimestral e anual (ajuste), ao ser processado lucro real negativo, ou seja, prejuízo, devem ser criadas contas na Parte B do Lalur, em função do:

a)      **Tributo**: IRPJ ou CSLL

b)      **Tipo de prejuízo**: operacional e não operacional (somente para IRPJ) e do

c)       **Período de apuração**.

* + ### Fonte

**Imposto sobre a Renda Da Pessoa Jurídica - IRPJ e Contribuição Social sobre o Lucro Líquido CSLL: de Acordo com a Lei N° 12.973, de 2014.**

BRITO, Machado Segundo, HUGO d., Calcini, FÁBIO Pallaretti. Atlas, 2015.

**Regulamentação Fiscal das Normas Contábeis do IFRS e CPC – Lei nº 12.973/14.**

ALMEIDA, Marcelo Cavalcanti, ALMEIDA, Rafael Jachelli. Atlas, 2015.

**Lei nº 6.404, de 15 de dezembro de 1976.**

Dispõe sobre as Sociedades por Ações.

<http://www.planalto.gov.br/ccivil_03/leis/L6404compilada.htm>

**Lei nº 12.973, de 13 de maio de 2014.**

Altera a legislação tributária federal relativa ao Imposto sobre a Renda das Pessoas Jurídicas - IRPJ, à Contribuição Social sobre o Lucro Líquido - CSLL, à Contribuição para o PIS/Pasep e à Contribuição para o Financiamento da Seguridade Social - Cofins; revoga o Regime Tributário de Transição - RTT, instituído pela Lei no 11.941, de 27 de maio de 2009; dispõe sobre a tributação da pessoa jurídica domiciliada no Brasil, com relação ao acréscimo patrimonial decorrente de participação em lucros auferidos no exterior por controladas e coligadas; altera o Decreto-Lei no 1.598, de 26 de dezembro de 1977 e as Leis nos 9.430, de 27 de dezembro de 1996, 9.249, de 26 de dezembro de 1995, 8.981, de 20 de janeiro de 1995, 4.506, de 30 de novembro de 1964, 7.689, de 15 de dezembro de 1988, 9.718, de 27 de novembro de 1998, 10.865, de 30 de abril de 2004, 10.637, de 30 de dezembro de 2002, 10.833, de 29 de dezembro de 2003, 12.865, de 9 de outubro de 2013, 9.532, de 10 de dezembro de 1997, 9.656, de 3 de junho de 1998, 9.826, de 23 de agosto de 1999, 10.485, de 3 de julho de 2002, 10.893, de 13 de julho de 2004, 11.312, de 27 de junho de 2006, 11.941, de 27 de maio de 2009, 12.249, de 11 de junho de 2010, 12.431, de 24 de junho de 2011, 12.716, de 21 de setembro de 2012, e 12.844, de 19 de julho de 2013; e dá outras providências.

<http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/Lei/L12973.htm>

**Decreto-Lei nº 1.598, de 26 de dezembro de 1977.**

Altera a legislação do imposto sobre a renda.

<http://www.planalto.gov.br/ccivil_03/decreto-lei/Del1598.htm>

**Instrução Normativa RFB nº 1.515/2014.**

Dispõe sobre a determinação e o pagamento do imposto sobre a renda e da contribuição social sobre o lucro líquido das pessoas jurídicas, disciplina o tratamento tributário da Contribuição para o PIS/Pasep e da Cofins no que se refere às alterações introduzidas pela Lei nº 12.973, de 13 de maio de 2014, e dá outras providências.

<http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=58604&visao=compilado>
