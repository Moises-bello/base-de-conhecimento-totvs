---
content_hash: 7b69c05c07465753cc55436ecbccc897054d2ea5f72ad9dbb8c36d6394b25214
fetched_at: '2026-06-29T00:10:19.067974+00:00'
page_id: '4813054'
product: rm
source: tdn-rm
title: Reajuste de Contrato por Faturamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Reajuste+de+Contrato+por+Faturamento
version: 7
---

BLOCK

Reajuste de Contrato por Faturamento

FAQ: **Reajuste de Contrato por Faturamento**

Avaliação

* ***Definição do Processo***

Tem por finalidade reajustar preço dos itens de contrato durante geração de movimento por faturamento. O reajuste é feito para itens de contrato do tipo “Periódico” onde o valor será reajustado obedecendo período de meses definidos na configuração deste item, tendo como referência, Índice da Moeda informado para reajuste.

Solução

* ***Parametrizações Necessárias***

Acessar **| Cadastro | Moedas e Índices | Incluir |** e fazer o cadastro do índice a ser considerado no reajuste do item de contrato onde deve informar:

Símbolo: informar o símbolo da moeda

Tipo: informar “Índice”

Descrição: informar descrição da moeda

Casas Decimais: informar número de casas decimais a serem consideradas para esta moeda

Defasagem em Meses: informar a defasagem em meses para esta moeda se houver

Acessar **| Cadastro | Cotações | Incluir |** e preencher:

Data: informar data de cotação da moeda

Símbolo: informar símbolo da moeda inclusa anteriormente (Ex: IGPM)

Valor: informar valor da cotação da moeda a ser inclusa (Ex: 2,00)

Símbolo de Referência: informar símbolo da moeda que será considerada para conversão. Como se trata de um “índice” deve ser informado mesmo símbolo definido anteriormente (Ex: IGPM)

Acessar o contrato, editar o item que possui **| Tipo de Faturamento : Periódico |**. A seguir acessar a aba **| Reajustes |** e preencher as informações:

Período: informar a periodicidade com que deve será feito reajuste no faturamento deste item, ou seja, de quantos em quantos meses o contrato deve ser reajustado ao faturar.

Defasagem da cotação da moeda (meses): se refere a quantidade de meses de defasagem da cotação da moeda a ser utilizada para o reajuste, ou seja, ao informar na “Defasagem em Meses” o conteúdo 2 o sistema vai buscar a cotação da moeda de (2) meses anteriores ao faturamento ou á ultima preenchida anterior a este período.

Dia da cotação da moeda a ser utilizado: informar o dia em que a cotação da moeda de reajuste será obtida

Reajustar sempre a última parcela: habilitar esta opção se desejada que a “última” parcela do item de contrato seja reajustada independente da informação preenchida no campo “Período”.

Exemplo:

Inclusão de item de contrato com 15 parcelas, onde o período de reajuste será de 12 meses. O reajuste será feito na 12º parcela considerando o acumulado das anteriores e na 15ª parcela considerando os percentuais acumulados posteriores á 12ª.

Cobrar resíduo de reajuste: ao marcar esta opção será calculado o resíduo das parcelas(resíduo corresponde ao valor acumulado do índice de reajuste durante o período de reajuste). Para isto é necessário que seja verificado código do produto informado no item de contrato e acesse **| Cadastro | Produto | Integração | Contrato |** onde deverá preencher **| Produto para Encargos |** com o código do produto pertinente resíduos a ser gerado.

Desta forma, será gerado movimento com dois itens, um com o valor do item informado no contrato outro com o item considerado para gravar os resíduos.

Exemplo:

Foi incluso contrato com 08 parcelas onde o reajuste será feito na 5ª parcela, ou seja, será apresentada diferença considerando o índice de cotação da moeda nos 04 meses anteriores ao reajuste.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Parcela** | **Mês** | **Índice** | **Vr da Parcela** | **Vr. c/ índ.Acumulado** | **Diferença** |
| 01 | Janeiro | 1,10% | 100,00 | 101,1000 | 1,10 |
| 02 | Fevereiro | 1,20% | 100,00 | 102,3132 | 2,31 |
| 03 | Março | 1,30% | 100,00 | 103,6433 | 3,64 |
| 04 | Abril | 1,40% | 100,00 | 105,0943 | 5,09 |
| 05 | Maio | 1,50% | 106,67 | 106,6707 |  |
| **RESIDUO** | **12,15** |
| 06 | Junho |  | 106,67 | 106,6707 |  |
| 07 | Julho |  | 106,67 | 106,6707 |  |

No mês 5, a parcela foi reajustada e o seu valor foi calculado baseado no acúmulo dos índices dos meses anteriores. Em cada mês em que a parcela não havia sido reajustada, houve uma diferença entre o valor cobrado e o valor com o índice acumulado do mês. O resíduo é então a soma destas diferenças que houveram entre o valor cobrado e o valor com o índice acumulado.

Moeda: informar qual moeda será considerada para reajuste do item do contrato. O reajuste será feito considerando cotação da moeda na data especificada, sendo assim, não é possível utilizar a moeda “R$”.

Data do Último: informar a data do último reajuste do item de contrato. Este campo será preenchido sempre que for efetuado reajuste do item em questão.

* ***Descrição do Processo***

O contrato será incluso como de costume, onde o usuário deverá editar o item de contrato e clicar na aba **| Reajustes |** para preencher os dados que serão considerados para este item em específico. O reajuste será feito apenas no momento do “faturamento” do item de contrato e vai obedecer as informações preenchidas na aba **| Reajuste |**.

Depois de concluído processo de faturamento ao editar o item de contrato na aba **| Reajustes |** o campo **| Data do Último |** estará preenchido e serão apresentadas linhas pertinentes valores reajustados | [![clip_image002](http://lh3.ggpht.com/_G7KXZLoZDsY/TKoyiXgf5WI/AAAAAAAABmI/Bnc8Z8Ythm8/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKoyhZVyEeI/AAAAAAAABmE/-ZsolLY0fTA/s1600-h/clip_image002%5B4%5D.jpg) |
