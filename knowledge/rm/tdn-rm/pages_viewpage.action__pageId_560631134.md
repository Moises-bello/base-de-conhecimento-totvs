---
content_hash: 5afa957048ea2ec930e723fc022914cb212c6f3a3b9659670b8ca92b6d768f64
fetched_at: '2026-06-29T00:10:47.631698+00:00'
page_id: '560631134'
product: rm
source: tdn-rm
title: Detalhamento do Cálculo da Parcela por Disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560631134
version: 9
---

---

Durante o processo de geração do lançamento o TOTVS Educacional gravará o detalhamento do cálculo da parcela conforme as disciplinas matriculadas, levando em consideração a parametrização que define como os crédito serão processados.

Após a geração do lançamento financeiro será possível identificar através de uma nova tabela, quais foram as disciplinas consideradas no cálculo e como o seu valor foi composto.

Tabela: SCALCULOPARCELAPORCREDITO

## Estrutura de Dados

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Campo** | **Obrigatório** | **Descrição** | **Observação** |
| **PK** | CODCOLIGADA | Sim | Coligada |  |
| **PK** | IDPARCELA | Sim | Id. parcela |  |
| **PK** | SEQUENCIAL | Sim | Nº sequencial | Sequencial do cálculo por parcela |
|  | ORIGEM | Sim | Origem do item de cálculo | * 1 - Cobrança por crédito * 2 - Cobrança por faixa de crédito (valor fixo) * 3 - Abatimento de valor de parcela fixa * 4 - Crédito em função do cancelamento de disciplina Quando houver um cancelamento de disciplina em que os sistema identificar que tem que devolver o valor pago para o aluno, esse valor será abatimento nas próximas parcelas.  * 5 - Credito em função da alteração da disciplina  Quando houver alteração no parâmetro “Considerar no cálculo de cobrança somente para parcelas com vencimento igual ou posterior a data da matricula”, em que o parâmetro passa a ser igual a “Sim” e já houver parcelas geradas e baixadas, pode ser que o sistema gere abatimento de valores nas próximas parcelas. * 6 - Aumento do valor da disciplina Quando houver alteração no número de crédito ou valor do crédito e já existirem parcelas geradas ou baixadas, pode ser que o sistema gere cobrança nas próximas parcelas. * 7 - Redução no valor da disciplina Quando houver alteração no número de crédito ou valor do crédito e já existirem parcelas geradas ou baixadas, pode ser que o sistema gere abatimentos nas próximas parcelas. * 8 - Cobrança retroativa Quando houver lançamentos gerados e baixados, e posteriormente realizar matricula e a data de matricula da disciplina seja inferior a data de vencimento destes lançamentos, pode ser que o sistema gere cobranças retroativas referente a disciplinas.  Esta origem é aplicada quando parâmetro “Considerar no cálculo de cobrança somente para parcelas com vencimento igual ou posterior a data da matricula” for igual a “Sim”. |
|  | TIPOITEM | Sim | Tipo do item de cálculo | * C - Cobrança * A - Abatimento |
|  | IDTURMADISC |  | Id. turma disciplina |  |
|  | CODDISC |  | Cód. da disciplina |  |
|  | NUMCREDITOCOB |  | Nº de créditos cobrados |  |
|  | VALORCREDITO |  | Valor do crédito |  |
|  | VALORTOTALCONTRATO |  | Valor total da disciplina calculado para o contrato |  |
|  | QTDPARCELASCONSIDERADA |  | Quantidade de parcelas consideradas | Quantidade de parcelas consideradas para dividir pelo valor total da disciplina calculado para o contrato, dando origem ao valor total da parcela (VALORTOTALPORPARCELA) |
|  | VALORTOTALPORPARCELA |  | Valor total da disciplina para a parcela |  |
|  | IDFAIXACREDITO |  | Id. Faixa de Crédito | Identificador do cadastro da faixa de crédito que foi utilizado.  Será preenchido somente quando o parâmetro "Utilizar Faixa de Crédito" estiver marcado. |
|  | INCONSISTENTE |  | Inconsistente | * S - Sim * N - Não |

Informação sobre o campo "INCONSISTENTE"

Quando o sistema identificar que o valor do detalhamento do cálculo não está conforme o valor do lançamento, o detalhamento será gravado, porem o campo “Inconsistente” ficara igual a “S”.

**Em que situação isso poderá acontecer?**

Para contratos que já tenham parcelas geradas sem ter o detalhamento gravado e com as seguintes características:

1º Cenário

* Quando o sistema estiver com o parâmetro **“Dividir valor de créditos financeiros das disciplinas matriculadas entre as parcelas do contrato”** marcado;
* Na matrícula da disciplina, a opção **“Considerar no cálculo de cobrança somente para parcelas com vencimento igual ou posterior a data da matricula”** estiver desmarcada;
* Para contrato que existirem parcelas com vencimentos inferior a data de matrícula da disciplina e que foram geradas ou regeradas considerando esta disciplina.

Por exemplo:

- Parcela 2 – vencimento 02/03 (o lançamento ainda não foi gerado)

- Matriculei o aluno na disciplina de Matemática no dia 10/04.

- Após a matrícula gerei o lançamento.

Conforme a parametrização mesmo a data de matrícula sendo no dia 10/04 a disciplina será cobrada na parcela 2.

2º Cenário

* Quando já existir parcela gerada e houver alteração no número de crédito ou valor do crédito.

Por exemplo:

Parcela 1 - Disciplina  D003, nº crédito 6, Valor do crédito 100,00 (lançamento gerado)

Parcela 2 - Disciplina  D003, nº crédito 7, Valor do crédito 100,00

3º Cenário

* Quando já existir parcelas geradas e for realizada uma matrícula em uma disciplina onde a data de matrícula seja inferior a data de vencimentos das parcelas já geradas.

Por exemplo:

Matriculado:

Disciplina 1 - Data de matrícula: 10/01/2018

Disciplina 2 - Data de matrícula: 10/01/2018

Considerando que o aluno antecipou a pagamento da parcela 1 a 4 no dia 10/02/2018, teremos:

Parcela 1 - valor R$ 361,00 (Baixada)

Parcela 2 - valor R$ 361,00 (Baixada)

Parcela 3 - valor R$ 361,00 (Baixada)

Parcela 4 - valor R$ 361,00 (Baixada)

Mas no dia 20/02/2018 o aluno matriculou na disciplina 3, com isso devemos cobrar o valor correspondente a disciplina para a parcela 3 e 4 que já estão quitadas.

4º Cenário

* Quando houver um cancelamento total da disciplina que o sistema identificar a existência de parcelas geradas / baixadas, o valor correspondente a disciplina é devolvido abatendo o crédito nas parcelas restantes.

Para contratos legados que não exista o detalhamento do cálculo por crédito, o sistema não conseguirá montar um detalhamento que identifique quais parcelas a disciplina foi cobrada e qual o valor a ser devolvido por parcelas.

Já nos contratos que possua detalhamento em todas as parcelas é possível identificar quais as parcelas que a disciplina foi cobrada, e com isso o sistema conseguirá detalhar os abatimentos por parcela, e identificar a origem do abatimento que neste caso é “Cancelamento total da disciplina”.

5º Cenário

* Quando houver um cenário onde o sistema estiver parametrizado para utilizar somente duas casas decimais, parametrização para divisão por crédito e o valor cobrado por disciplina resultar em uma dízima periódica, o sistema de arredondamento irá gerar  uma diferença de valor a qual o detalhamento não consegue tratar. Considerando isso, teremos um cenário de inconsistência e o resultado não será apresentado.\

Exemplo:

   Créditos: 20

   Valor do crédito: 17,87

   Total de parcelas: 18

   Valor da disciplina por parcela: (20 \* 17,87) / 18 =  19,85555555555556 (19,86)

   Total por parcela: 357,48  ( Diferença de 0.08 centavos devido ao arredondamento no valor total )

**Por que o detalhamento do cálculo não fica correto?**

As parcelas geradas anteriormente não possuem o detalhamento de cálculo da disciplinas, e dependendo do cenário o sistema não consegue realizar o rastreamento dos valores processados para a disciplina para saber por exemplo, se a disciplina foi ou não considerada em determinada parcela.

**Por que o valor do lançamento fica correto?**

Porque o sistema calcula o valor das disciplinas por contrato e não por parcela, ou seja, conforme o lançamento vai sendo gerado o sistema apenas realiza abatimentos do valor total já gerado ou baixado, garantindo que o valor total da disciplina que ainda não foi pago seja diluído nas parcelas a serem geradas.

**Sempre teremos este problema?**

Não, para os contratos em que todas as parcelas sejam geradas possuindo o detalhamento de cálculo o sistema consegue identificar qual parcela a disciplina foi cobrada e com isso conseguimos chegar no valor da disciplina por parcela.

Caso seja processado detalhamentos inconsistentes que não estão conforme o cenário relatado acima, deverá ser aberto um ticket no suporte para que possamos avaliar.

Ressaltamos que são apenas alguns cenários especifico que não será possível gerar o detalhamento, para contratos que todas as parcelas possuam detalhamento o sistema dever ser capaz de detalhar o cálculo de forma correta.

**Tem alguma maneira de corrigir essa inconsistência pelo sistema?**

Sim, em alguns casos o sistema conseguirá regerar o detalhamento, ou seja, os registros da tabela SCALCULOPARCELAPORCREDITO, sem modificar dados do lançamento ou da parcela. Para isso, a partir da versão **12.1.32**, quando ocorrer essa inconsistência, o sistema irá exibir um botão na central financeira para corrigir o detalhamento, conforme a imagem abaixo:

Vale ressaltar que essa opção não fará a correção em todos os casos, somente em casos já levantados de inconsistência que foram tratados no sistema.

Essa opção está disponibilizada nos respectivos patch das versões **12.1.32.252, 12.1.33.196 e 12.1.34.110**.

Observação

Quando o TOTVS Educacional estiver parametrizado para utilizar faixa de crédito e a faixa de crédito for por valor fixo, será gravado somente o números de créditos cobrados e não será possível ter o valor monetário para cada disciplina.

Não será gerado detalhamento do cálculo por disciplina, quando o valor da parcela for fixo.
