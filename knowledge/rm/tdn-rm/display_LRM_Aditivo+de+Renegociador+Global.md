---
content_hash: d5977edeb04e8b67620ac2c7aa704b842a057740f4c90ed15ddd0ad157d67491
fetched_at: '2026-06-29T00:09:49.160670+00:00'
page_id: '435105246'
product: rm
source: tdn-rm
title: Aditivo de Renegociador Global
type: documentation
url: https://tdn.totvs.com/display/LRM/Aditivo+de+Renegociador+Global
version: 3
---

Visando simplificar o processo de renegociação de parcelas em atraso, principalmente quando o financiamento possui Juros Pré-fixados e é preciso diferenciar quais componentes incidem nas parcelas, foi criada a funcionalidade de aditivo de Renegociador global.

Com este aditivo é possível renegociar várias parcelas de uma venda e redistribuí-las em uma ou mais parcelas futuras. Tudo isto com a facilidade de distribuir os valores em componentes correspondentes, como por exemplo Juros, Multa, etc, ou até mesmo somar tudo em um único componente do tipo principal - antes aditivo.

Uma das vantagens de se utilizar este renegociador é que os componentes e sua origem serão visualizados na parcela e na geração de boletos, melhorando assim a visibilidade e o entendimento do valor total da parcela. Tanto o comprador final quanto a incorporadora terão um melhor gerenciamento sobre a parcela do financiamento.

O funcionamento do cálculo é idêntico ao renegociador existente nos aditivos dos contratos de venda e para maior assertividade nos valores é sugerido utilizar o reajuste online, pois este calcula os valores de reajuste monetário na data informada no aditivo.

Antes de executar o aditivo é necessário cadastrar quais componentes serão utilizados para realizar a distribuição na nova parcela e o componente Principal - Antes Aditivo é obrigatório em todos os casos. O Componente de Juros é obrigatório apenas quando o financiamento tiver modelo de cálculo pré-fixado, como o PRICE, SAC e SACRE.

Caso os componentes de Juros de Mora e Multa não forem configurados nos parâmetros gerais, não serão considerados no cálculo do renegociador. Quanto aos componentes de CM, estes não serão redistribuídos, pois o Reajuste online se encarregará de atualizar esses valores nas parcelas de Destino.

**Etapa 1 - Selecione as parcelas a serem renegociadas e a data do valor líquido para o cálculo do valor renegociado.**

Esta tela é idêntica à tela de lançamentos financeiros, que está disponível no anexo do contrato de venda. Ela tem todos os lançamentos financeiros, podendo ser filtradas pela data de vencimento, número da venda, referência de lançamento, etc.  
 A partir desta tela também é possível realizar baixas, inclusão de boleto e todos os processos do módulo financeiro.   
 Para realizar o cálculo deve-se selecionar a parcela e escolher uma data para renegociação:

* **Campo data líquido**: Este campo é responsável por definir para qual data será renegociada a(s) parcela(s) selecionada(s), ao clicar no "raiozinho" no canto direito da tela, será calculado o valor líquido da parcela para a data selecionada, juntamente com o reajuste online, deságio ou multa e juros de mora.

**Etapa 2 - Selecione as parcelas que receberão os valores renegociados.**

Nesta tela serão exibidos todos os lançamentos financeiros referente à venda das parcelas que foram escolhidas no passo anterior. Ou seja, todas as parcelas que podem receber o valor renegociado. É possível também realizar baixas, inclusão de boletos, cheques e outros processos financeiros nessa etapa.  
Após selecionar as parcelas, o aditivo irá fazer o rateio do valor calculado no passo anterior entre as parcelas selecionadas.

* **Simular a Renegociação:** Ao clicar nesse botão será exibido o valor novo da parcela somado ao valor renegociado.
* **Limpar Renegociação:** Botão criado para limpar a simulação da tela, assim será possível escolher outra parcela para a simulação.

**Etapa 3 - Execução do aditivo.**

Após a execução do aditivo é gerado um log com as alterações realizadas. São exibidas as parcelas que foram alteradas juntamente com os novos componentes inclusos nas parcelas após a renegociação.

É possível verificar todo o cálculo realizado no histórico do aditivo criado que se encontra no anexo da venda. Este aditivo será criado com o tipo de alteração de valor de parcela e renegociação de contrato. Estes novos valores também podem ser consultados nos logs do plano de financiamento da venda e nos valores de integração do lançamento financeiro.

* **Observações:** Para que os componentes criados por este processo sofram reajuste posteriormente, é necessário que na criação do componente sejam marcados alguns parâmetros para indicar se esse componente compõe o valor base para o cálculo de reajuste de:
  + Reajuste de Juros de Contrato.
  + Reajuste de Correção Monetária.
* No componente do Tipo Principal, deve-se marcar os dois parâmetros.
* No componente de Juros de Contrato, caso for modelos PRICE, SAC, SACRE estes parâmetros virão marcados por default no plano de financiamento por causa do comportamento pré-fixado. Se for outro modelo, como o PADRÃO, pode se marcar de acordo com a necessidade do negócio.

Utilizando o aditivo de renegociador global, são possíveis várias configurações de financiamento, pode-se utilizar em uma mesma venda componentes de modelo Pré e pós fixados, (PRICE e PADRÃO) por exemplo. Desta maneira veja o comportamento do aditivo nas seguintes situações (Usaremos como exemplo os modelos de cálculo PRICE e PADRÃO):

**Renegociar uma parcela no modelo PADRÃO para outra parcela também do modelo PADRÃO.**

* A CM e o Juros de contrato não serão redistribuídos e serão calculados pelo Reajuste Online.
* Multa, Juros de Mora e componente Principal serão redistribuídos de acordo o valor da parcela selecionada e a data base informada.

**Renegociar uma parcela no modelo PADRÃO para uma parcela no modelo PRICE.**

* A CM e o Juros de contrato não serão redistribuídos e serão calculados pelo Reajuste Online.
* Multa, Juros de Mora e componente Principal serão redistribuídos de acordo o valor da parcela selecionada e a data base informada.

**Renegociar uma parcela no modelo PRICE para uma parcela no modelo PADRÃO.**

* A CM e o Juros de contrato não serão redistribuídos e serão calculados pelo Reajuste Online.
* Multa, Juros de Mora e componente Principal serão redistribuídos de acordo o valor da parcela selecionada e a data base informada.

**Renegociar uma parcela no modelo PRICE para outra parcela também no modelo PRICE.**

* A CM não será redistribuída e será calculada pelo Reajuste Online.
* Multa, Juros de Mora e componente Principal serão redistribuídos de acordo o valor da parcela selecionada e a data base informada. Nesse caso o Juros de Contrato também será redistribuído, pois esse valor (pré-fixado) pode ser utilizado como base para o Reajuste desta parcela posteriormente.

Veja Também

---

Para mais informações sobre como cadastrar os componentes para distribuição dos valores pelo renegociador, consulte:    
 Para mais informações sobre os aditivos a serem gerados, consulte:   
 Para as configurações disponíveis dos componentes, consulte:
