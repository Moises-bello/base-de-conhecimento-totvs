---
content_hash: 1e8a530ca238be31f9a6f894f4f2f18caaff42ef45e127d1c33841ba1732aacc
fetched_at: '2026-06-29T00:09:25.837819+00:00'
page_id: '423938175'
product: rm
source: tdn-rm
title: Condição de Pagamento (Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938175
version: 20
---

AbasIdentificação

**Código:**Informe o código que identificará a condição de pagamento.

**Descrição:**Informe a descrição da condição de pagamento.

**Deflator:**Neste campo, informe se houver, um fator de deflação para comissões em movimentos com esta condição de pagamento. Este fator poderá ser utilizado em fórmulas ou relatórios.

**Arredondamento**: Para pagamentos com mais de um vencimento, poderá ocorrer resíduos, portanto será necessário definir o tipo de arredondamento:

false

**Moeda:**Para pagamentos com mais de um vencimento, poderá ocorrer resíduos, portanto será necessário definir o tipo de arredondamento:

* Não Arredonda: Para esta condição não haverá arredondamento;
* Dezena: O arredondamento será por dezena;
* Centavos: O arredondamento será por centavos;

**Parcela:** Informe em qual parcela deverá ser lançado o resíduo, clique em , aparecerá então, as opções de lançamento (esta opção será apresentada apenas se o tipo de arredondamento for diferente de "Não Arredonda")

* Primeira Parcela: o resíduo será lançado na primeira parcela;
* Última Parcela: o resíduo será lançado na última parcela;

**Fórmulas de Preço:**Neste campo você poderá indicar duas fórmulas de preço e através destas o sistema retornará o preço do item do movimento.

Observação

Para que o sistema utilize a fórmula aqui indicada é necessário que no tipo de movimento na pasta itens, subpasta identificação no campo "buscar preço em" esteja indicado, "Fórmula de Preço 1" para buscar o preço de acordo com a fórmula indicada no campo preço 1 ou "Fórmula de Preço 2" para buscar para o preço o resultado da fórmula indicada no campo preço 2.

Exemplo de utilização

Um determinado produto, possui o preço de R$100,00 para pagamentos **À vista**, e um acréscimo de 20% sobre o seu preço à vista para pagamentos de **30/60 dias.**

Deverão ser criadas duas fórmulas, (1) que busque o preço à vista do cadastro do produto, (2) que busque o preço à vista e mulplique por 1,2;

No campo "Preço 01" na condição de pagamento **À vista**, deve ser informada a fórmula (1) criada acima;

No campo "Preço 01" na condição de pagamento **30/60 dias**, deve ser informada a fórmula (2) criada acima;

No tipo de movimento, parametrizamos o campo "**Buscar preço em**" a opção "**Fórmula de Preço 1**";

Ao realizar uma venda do produto em questão, utilizando a condição de pagamento **À vista**, o sistema buscará como preço do produto o resultado da fórmula (1) que é igual a **R$100,00**. Ao informar a condição de pagamento **30/60 dias**, o sistema buscará como preço do produto o resultado da fórmula (2) que é igual **R$120,00**.

**Taxa de Juros (a.m):**Informe neste campo o percentual mensal de juros que deverá ser cobrado nos lançamentos em atraso baixados no TOTVS Gestão Financeira e que possuam esta condição de pagamento informada.

**Juros Compostos**: Marque esta opção se desejar que os juros cobrados para os lançamentos em atraso sejam o juro composto. A taxa de juros utilizada para cálculo é a mesma informada no campo "Taxa de Juros (a.m)".

Observação

Se no tipo de movimento incluído estiver parametrizado na pasta faturamento/valores opcionais com "Calcular Juros de Acordo com os parâmetros gerais" , o percentual de juros considerado na baixa dos lançamentos em atraso será o informado nos parâmetros gerais/tabelas/ gerais campo "Juros ao Mês".

**Carência por Dias da semana**: Habilitando um dos dias da semana, ao incluir um movimento de entrada, o sistema irá incluir os lançamentos financeiros conforme as parcelas da condição de pagamento, calculando a data de vencimento de acordo com o dia da semana informado.

Observação

Para pagamentos de **compra** (movimento de entrada) será considerada a carência da **condição de pagamento**.

Para pagamentos de **venda** (movimento de saída) será considerada a carência configurada na pasta Outros dados do **cliente/fornecedor**.

Tanto na condição de pagamento quanto no cliente/fornecedor a carência poderá ser por dias fixos do mês ou por dias fixos da semana, mas somente uma delas pode ser usada;

Antes de configurar os dias de carência, deverá primeiramente verificar nos parâmetros do TOTVS Gestão Financeira, pasta Datas sub pasta Default se está configurado os campos sobre as Previsões, os Vencimentos e as Baixas em finais de semana, pois na geração do lançamento financeiro o sistema recalcula as datas.

**Capitalização Mensal:**A capitalização mensal também poderá ser feita no cadastro da condição de pagamento, anteriormente este recurso somente era feito por tipo de movimento. Será respeitado sempre o valor informado na capitalização do tipo de movimento, caso este não exista, será utilizado o valor cadastrado na condição de pagamento. Informe o percentual de capitalização mensal, juros, desconto que incidirão nos lançamentos gerados.

**Tipos de Planos:**O sistema vai filtrar na inclusão de movimentos de compra e venda, as condições de pagamentos de acordo com as opções de tipos de planos selecionadas: Compra e/ou Venda.

**Fórmula da 1ª Parcela:**Neste campo será informado a fórmula à ser utilizada no lançamento da primeira parcela do movimento.

Observação

Quando é utilizado 'Fórmula na 1ª Parcela', na aba 'Composição de Parcelas' o percentual deverá ser preenchido com 0(zero) e o número de vezes não poderá ser maior que 1.

Exemplo de utilização

Deseja-se que o Tributo ICMS-ST seja recolhido 20 dias após a emissão da nota fiscal. Para tal utilizaremos a formula do tributo no campo 'Formula da 1ª parcela' e na aba 'Composição de Parcelas', na 1ª parcela o percentual deverá ser preenchido com 0 (zero), o número de vezes igual a 1 e o prazo igual a 20. As outras parcelas serão preenchidas conforme desejado para as parcelas posteriores. Desta forma o lançamento do tributo será 20 dias após a emissão da nota fiscal e o lançamento das parcelas normais serão feitas conforme parametrizado nas outras parcelas.

**Meio de Pagamento**: Insira um valor default de meio de pagamento, para que seja utilizado no preenchimento da TAG <<**tPag**>> do XML da NF-e.

Observações

Para os movimentos de Nota que usam condição de pagamento, caso este campo não esteja preenchido a Nota será rejeitada.

**Disponível para Automação Comercial:**Habilitando esta opção, irá classificar as condições de pagamento para que possam ser exportadas e utilizadas pelo aplicativo de automação comercial integrado.

**Desconsiderar Limite de Crédito**: Na Inclusão de um movimento, caso utilize Cliente/Fornecedor parametrizado para utilizar **[Limite de Crédito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006432162-RM-FIN-Como-funciona-o-Limite-de-Cr%C3%A9dito-no-cadastro-de-Cliente-Fornecedor),** marque esta opção caso deseje que seja Desconsiderado o Limite de Crédito, esta nova tag terá mais usabilidade para as condições de pagamento á vista. 

**Inativo**: Marque esta opção caso deseje que a condição de pagamento não seja apresentada na inclusão de novos movimentos no sistema.

Observação

O sistema irá impedir inativar uma condição de pagamento, caso exista pelo menos um movimento, cujo tipo de movimento esteja parametrizado para **Gerar Movimento** (Etapa 'Compra/Venda - Características' → 'Gera Movimento de Compra') e com o status diferente de **Faturado** e **Cancelado**.

Ao inativar uma condição de pagamento (por tela), se houver movimentações pendentes o usuário será alertado podendo ver a quantidade de movimentos pendente e listar movimentos.

Ao inativar uma condição de pagamento (por DataServer), se houver movimentações pendentes o usuário vai ser alertado e informado sobre a quantidade de movimentos pendentes.

Os movimentos já incluídos com a condição de pagamento inativa não serão afetados, continuarão apresentar a condição de pagamento. Mas se este movimento for editado e a condição de pagamento for modificada não será possível selecioná-la novamente.

Observação

Nos layouts de integração existem definidos filtros onde somente as condições de pagamento compatíveis serão exportadas.

Composição de ParcelasObservação

Para o preenchimento do campo Data de Vencimento das parcelas de lançamento, o  sistema leva em consideração o calendário oficial que foi definido nos [parâmetros gerais](https://tdn.totvs.com/pages/viewpage.action?pageId=423938842), calendário oficial.

É possível cadastrar até 5 parcelas para cada condição de pagamento e são apresentadas cinco colunas para a informação das condições das parcelas, a seguir explicaremos cada uma delas:

**% do Valor Total:**Informe o valor em percentual do preço que será pago nesta parcela.

Observação

* Quando é utilizado 'Fórmula na 1ª Parcela', na aba 'Composição de Parcelas' o percentual deverá ser preenchido com 0 (zero) e o número de vezes não poderá ser maior que 1.

* A soma de todos os percentuais informados para as parcelas, não poderá ultrapassar a 100%.

Exemplo de utilização

Considerando que o valor do lançamento é de R$ 1.000,00, e no campo "% em relação ao Valor Total" da Linha 1, foi informado 50%, significa que a primeira parcela será de R$ 500,00.

**Número de vezes:**Informe o número de vezes que será dividido o pagamento do valor desta parcela, ou seja, o valor da parcela depois de calculada, de acordo com o percentual informado no campo "% em relação ao valor total".

Exemplo de utilização

Considerando que o valor total do lançamento é de R$ 2.000,00 e a primeira parcela desta condição é de 50 % do valor total e que esta será ainda facilitada em 2 vezes, neste caso, a parcela de R$ 1.000,00, que é 50% do valor total, ainda será dividida em 2 vezes, ou seja, serão mais duas parcelas de R$ 500,00.

**Prazo:**Informe o prazo em dias para o vencimento desta parcela. Se esta ainda for dividida, este é o prazo para o primeiro vencimento da mesma.

**Intervalo:**Informe o intervalo em dias que deverá ser calculado para o vencimento das parcelas.

**Tipo:**Escolha entre as opções, qual será o tipo de cálculo para o prazo da parcela a partir da data de emissão. As opções são:

* *Normal:* A partir da data de emissão.
* *Fora Semana:* Não considera a semana da data de emissão
* *Fora Mês:* Não considera o mês da data de emissão.
* *Fora Quinzena:* Não considera a quinzena da data de emissão
* *Fora Dezena:* Não considera a dezena da data de emissão.
* *Fora Ano:* Não considera o ano da data de emissão.

Exemplo de utilização

Data do Movimento: 26/08

Condição de Pagamento: À Vista - Fora Dezena  
Neste caso a primeira parcela vencerá em 01/09 pois, esta data já está na dezena seguinte à do dia 26/08.

**Contagem:**Informe como deverá ser feita a contagem dos dias para o prazo inicial e o intervalo entre as parcelas: As opções são:

* *Dias Corridos:* Para que a contagem seja feita a partir da data de emissão direto, isto é, sem saltar os sábados, domingos e feriados. Este campo será obrigatório sempre que houver algum percentual informado no campo '% o valor total' que seja diferente de zero.
* *Dias Fixos:* Para que as datas sejam exatamente iguais. Exemplo: se a primeira parcela vencer no dia 01, as demais também vencerão todo dia 01 dos meses subsequentes.
* *Dias Fixos com prazo:* As datas de vencimento serão fixas, levando em consideração o valor informado no campo prazo.

Exemplo de utilização

***Exemplo 1**:*Se for informado 15 no campo prazo e o campo "vencimento a partir" estiver setado com a data de emissão = 01/09, o primeiro vencimento será no dia 15/09 e as demais também vencerão todo dia 15 dos meses subsequentes.  
*Dias Úteis:* Somente os dias úteis serão contados para o cálculo das parcelas.  
*Dias de Carência:* Informe os dias de carência (dias fixos para vencimento) de cada parcela da condição de pagamento. Estas carências correspondem a dias fixos em que a parcela terá vencimento. O dia selecionado para o vencimento da parcela será o dia mais próximo após o seu vencimento original.

***Exemplo 2**:*Vamos supor que a 1a parcela da condição de pagamento tenha como carências os dias 05, 10 e 20. Se o vencimento original da parcela cair no dia 08, a carência mais próxima após esta data é utilizada, ou seja, o vencimento será jogado para o dia 10 do próprio mês. Caso o vencimento original caia no dia 25, o vencimento será jogado então para o dia 05 do próximo mês, que é a carência mais próxima desta parcela.
