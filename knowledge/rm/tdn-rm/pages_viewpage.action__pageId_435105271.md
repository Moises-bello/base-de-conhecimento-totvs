---
content_hash: 3afbc0cfeab963ba493bad123ebad81d9d1a31fabed68316fadbbb792ac6d281
fetched_at: '2026-06-29T00:09:49.264375+00:00'
page_id: '435105271'
product: rm
source: tdn-rm
title: Aditivo - Renegociação de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105271
version: 24
---

AditivoRenegociação ContratoRenegociação Contrato

Este tipo de aditivo permite que o usuário altere o plano de financiamento de uma determinada venda.   
Ao selecionar este tipo de Aditivo, será apresentado todas as Parcelas em aberto do plano de financiamento no link "Parcelas Renegociadas". O Sistema permite que o usuário selecione as parcelas que serão canceladas no Aditivo.

**Nota sobre Vendas Distratadas:** O sistema suporta a utilização deste Aditivo em vendas que sofreram Distrato, permitindo renegociar e alterar os valores de parcelas de devolução (natureza **A Pagar**), desde que estas não possuam baixas realizadas.

Importante!

Não cancele o Processo ***Sincronizar parcelas do aditivo com a venda***, pois o mesmo é essencial para a correta parametrização do Aditivo.

Caso esta ação seja executada, o sistema retornará à tela inicial do Aditivo e será necessário refazer toda a parametrização, até que o processo acima seja executado em sua completude.

Caso a Integração com a [Registradora de Recebíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=729222653) esteja parametrizada, verifique as **[Premissas](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora)** em relação à este tipo de Aditivo, para se executar o Processo [Integrar com Registradora](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Processos+-+Integrar+com+Registradora).

O sistema permite a renegociação de parcelas associadas a um [Contrato de Securitização](https://tdn.totvs.com/pages/viewpage.action?pageId=518484326), para maiores detalhes sobre as regras deste processo consulte a aba Securitização de Aditivos. desta funcionalidade.

Novidade!

A partir do Patch Específico 12.1.2310.102 e dos Releases posteriores a este, é possível de se calcular o **[Valor Presente para o Price](https://tdn.totvs.com/pages/viewpage.action?pageId=795106302)** das parcelas renegociadas.

Campos a serem preenchidos:

**Negociar valores diferentes:** Permite que o novo plano ou nova parcela, tenha um valor diferente, do valor das parcelas selecionadas para serem excluídas.   
**Negociar sem multa e juros atraso:** Permite que o novo plano ou nova parcela seja renegociado sem o valor dos juros e multa.   
**Proporcionalizar:** Caso o usuário opte por Sim, os valores dos componentes da(s) nova(s) parcela(s) criada(s) serão proporcionalizados após o cancelamento das parcelas selecionadas no campo Parcelas.  
Os valores de Juros , Multa  e Correção Monetária, já existentes nas parcelas a serem canceladas são proporcionalizados de acordo com o número de novas parcelas nos componentes Antes / Ambos (CM Antes Aditivo) - Componente CM Após(CM Antes Aditivo) - Componente Juros (Juros Antes Aditivo) - Componente Juros de Mora(Tipo Encargos) - Componente Multa de Atraso (Tipo Encargos) - Componente Desconto Financiamento (Tipo Desconto).

**Obs.****1** : Os encargos financeiros serão distribuídos nos componentes correspondentes , se não preencher serão distribuídos no principal.

**Obs.****2** : Permite apenas um Componente Principal apenas Não se tem como Negociar Valores Diferentes.

Para realizar um aditivo de renegociação durante a cobrança, os valores dos componentes  estarão mantidos separados, para facilitar o controle da empresa e permitir a correta contabilização agregada.

O aditivo de renegociação para o modelo padrão deve ser preparado para isso.

A opção de aditivo deve ser incluída na tela de cobrança, junto com a opção de acordo.

Incluído o parâmetro de Aditivo / Acordo para que possa ser possível efetuar dos valores dos componentes.

Selecionar o Aditivo - Renegociação de Contrato.

Marcar o Parâmetro : Proporcionalizar - Para que possa sair os valores dos componentes separados.

Neste exemplo , foram selecionadas 2 Parcelas do Contrato vencidas com Multa e Juros.

No exemplo , a Planilha de calculo mostra 2 parcelas que serão geradas pelo Aditivo e os valores da Parcela , Juros . Multa e CM.

Após selecionar a quantidade parcela, criar uma nova condição de pagamento para o Aditivo , como mostra a figura acima de Exemplo.

No exemplo acima ,  marcando para 2 parcelas.

Ao efetivar o Aditivo , as parcelas selecionadas , são canceladas.

E ao consultas as 2 Parcelas que foram geradas pelo Aditivo , mostra os valores dos componentes sendo divididos.

**Tipo Renegociação:** Este campo possibilita a escolha do tipo de renegociação a ser realizado, são eles:

* **Padrão:** Usado quando o usuário for realizar o aditivo para excluir parcelas do Plano de Financiamento e inserir novas parcelas.
* **Inclusão:** Permite a criação de uma ou mais parcelas no plano de financiamento. Exemplo de aplicação: Será realizada uma limpeza no terreno, então neste caso será necessária a inclusão do valor a ser cobrado no plano de financiamento.
* **Cancelamento:** Realiza o cancelamento de parcelas, sem a geração de uma nova parcela.

**Comportamento resíduo:** Esse parâmetro determinar o comportamento do aditivo, quando a venda possui resíduo a ser gerado. Possui as seguintes opções:

* **Impedir cancelamento:** Ao selecionar essa opção, o aditivo vai impedir que a parcela que possui Resíduo pendente de ser gerado. Dessa forma é informado que deverá ser gerado a parcela de Resíduo antes de se efetivar o aditivo;
* **Incorporar resíduo no total a renegociar:** Ao selecionar essa opção, o aditivo vai incorporar o valor do Resíduo pendente de ser gerado, no total a renegociar.
* **Gerar Parcela de Resíduo:** Ao selecionar essa opção, o aditivo vai gerar a Parcela de Resíduo.

**Valor resíduo pendente:** Determina como determinar o valor de resíduo pendente na venda. Possui as seguintes opções:

* Parcelas em aberto;
* Parcelas em aberto e quitadas;

**Valores Renegociados:**

* **Total de parcelas selecionadas:** Exibe o somatório dos valores da parcela selecionado. Esta informação será calculada automaticamente;
* **Total renegociado:** Soma dos valores a serem gerados através do recurso de Condições de Venda. Esta informação será calculada automaticamente;
  + Para obter este valor, o sistema faz uma simulação do plano de financiamento dos grupos que foram criados no aditivo e calcula a soma dos valores das parcelas. Portanto os componentes como o encargo financeiro e entre outros serão considerados neste cálculo.
  + Se a simulação do plano retornar algum erro devido a alguma configuração inválida nas condições do plano, então o sistema irá exibir a soma dos componentes geradores de parcela.
* **Total a Renegociar:** Soma dos valores das parcelas selecionadas. Esta informação será calculada automaticamente;
* **Diferença de Renegociado por a Renegociar:** É a diferença do valor a ser gerado com o valor selecionado a ser cancelado. Esta informação será calculada automaticamente.

**Comportamento em Vendas Distratadas (Parcelas de Devolução):**

* **Total de parcelas selecionadas:** Apresenta o somatório total das parcelas de devolução selecionadas.
* **Total renegociado e Total a renegociar:** Assumem o valor absoluto e exato da operação de devolução.
* **Diferença de Renegociação:** Exibirá **R$0,00** quando o montante renegociado coincidir com as parcelas selecionadas, garantindo a integridade dos saldos para a contabilização do aditivo.

**Valores Financeiros:**

* **Total Multa de Atraso:** Soma dos valores das multas de Atraso das parcelas selecionadas. Esta informação será calculada automaticamente.
* **Total Juros de Mora:** Soma dos valores dos Juros de Mora das parcelas selecionadas. Esta informação será calculada automaticamente.
* **Total Desconto de Multa de Atraso:** Informe o valor de desconto que será dado sobre o total do valor da Multa de Atraso.
* **Total Desconto Juros de Mora:** Informe o valor de desconto que será dado sobre o total do valor de Juros de Mora.

**Valores de Resíduo:**

* **Parcelas Abertas:**

* + **Total Juros resíduo em aberta:** Exibe o total de juros de resíduo aberto na venda;
  + **Total CM resíduo em aberta:** Exibe o total de CM de resíduo aberto na venda;
  + **Total resíduo em aberta:** Exibe o total de resíduo aberto na venda;

* **Parcelas Quitadas:**

* + **Total Juros resíduo em quitada:** Exibe o total de juros de resíduo quitada na venda;
  + **Total CM resíduo em quitada:** Exibe o total de CM de resíduo quitada na venda;
  + **Total resíduo em quitada:** Exibe o total de resíduo quitada na venda;
  + **Parcelas Renegociadas:**Através desta tela, podemos selecionar as parcelas do Plano de Pagamento que serão canceladas.

**Valor Presente Price:** A partir do Patch Específico 12.1.2310.102 e dos Releases posteriores a este, é possível de se calcular o ***[Valor Presente para o Price](https://tdn.totvs.com/pages/viewpage.action?pageId=795106302)*** das parcelas renegociadas. Para saber mais sobre esta funcionalidade, clique **[aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=795106302)**.

**Plano de Financiamento:**

* **Condições de financiamento:**Através desta tela, podemos efetuar a inclusão dos novos grupos e dos componentes que irão compor, as novas condições no plano de financiamento.
* **Lançamento Financeiro:**Através dessa tela, pode ser visualizado a tela de Lançamento Financeiros criados pelo Aditivo de Renegociação. Assim como executar os processos do Lançamento Financeiro.

Para a geração das parcelas do Aditivo de Renegociação, é necessário executar o processo Gerar Plano de Financiamento Aditivo, assim como para excluir as parcelas deve ser executado o processo Excluir Plano de Financiamento Aditivo.

**Contabilização do aditivo:**Caso opte por contabilizar o aditivo, deve-se na venda preencher quais eventos contábeis são responsáveis pela contabilização inflacionária e deflacionária.  
Existe um parâmetro para que este aditivo seja contabilizado mesmo que não tenha alteração de valor, mas será importante para indicar em qual partida contábil será contabilizado (Contabilizar sempre o aditivo de renegociação).   
Os valores das parcelas selecionadas serão desfeitos na contabilização do evento deflacionário e refeitas com os valores das parcelas renegociados(novas) no evento inflacionário.   
A renegociação de contrato do tipo inclusão de parcelas, será contabilizado para o evento contábil inflacionário, já o cancelamento de parcelas será contabilizado no evento deflacionário. Já a renegociação padrão será contabilizada nos dois eventos com os valores de acordo se teve um acréscimo no plano ou um decréscimo.

Como envolve dois eventos ao mesmo tempo na contabilização do aditivo, então não será exibida a tela de pré-visualização da contabilização.

Se na efetivação tiver mais de um aditivo a ser contabilizado, então a contabilização será feita da forma antiga.false

Veja Também

---
