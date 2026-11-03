---
content_hash: b2446675d927cbdc7614f44ae7a8e6b9e29c68186e058468518958a15137985c
fetched_at: '2026-06-29T00:12:03.335503+00:00'
page_id: '906835450'
product: rm
source: tdn-rm
title: Parcial
type: documentation
url: https://tdn.totvs.com/display/LRM/Parcial
version: 5
---

## **CONTEÚDO**

1. **Parcial Complementar**
2. **Alterar Início da Parcial**
3. **Cancelar Parcial**
4. **Encerramento da Parcial**

ParcialParcial Complementar

## **01. VISÃO GERAL**

Importante!

Uma **Parcial Complementar** deve ser criada para o mesmo convênio ao qual a parcial original se refere.

O **faturamento complementar** é um procedimento utilizado no **padrão TISS (Troca de Informações na Saúde Suplementar)**, regulamentado pela ANS (Agência Nacional de Saúde Suplementar), para enviar informações adicionais ou corrigir dados de um lote já enviado anteriormente. O **faturamento complementar** é útil em situações onde houve:

1. 1. **Erros ou omissões** nos dados enviados anteriormente, que precisam ser ajustados.
   2. **Novas informações** que não estavam disponíveis no momento do envio original (exames adicionais, tratamentos complementares, etc.).
   3. **Acréscimo de dados** referentes a um atendimento já informado, como mudanças de valores cobrados, inclusão de procedimentos, ou correções de dados clínicos.

Esse processo garante que os dados trocados entre prestadores de serviços de saúde e operadoras de planos sejam atualizados e corretos, evitando problemas como recusa de pagamento ou divergências na auditoria de contas médicas.

## **02. CRIANDO UMA PARCIAL COMPLEMENTAR**

Para realizar o envio de um lote complementar, será necessário criar uma **Parcial Complementar**, como o nome sugere, é um registro adicional feito para complementar uma parcial já encerrada e faturada. Em situações excepcionais, quando é necessário realizar lançamentos posteriores, como procedimentos ou materiais, esses itens são incluídos na **Parcial Complementar**, ficando disponíveis para um eventual refaturamento.

O comportamento de uma **Parcial Complementar** é semelhante ao de uma parcial comum, mas com a diferença de que ela não altera as datas de início e fim da parcial anterior. As guias de autorização relacionadas a parcial original, serão importadas nessa nova parcial complementar.

Para criar uma **Parcial Complementar**, é necessário que a parcial de origem já esteja faturada. Selecione a parcial desejada e execute o processo **Parcial Complementar**.

Parcial Complementar criada.

Observe que nenhum lançamento é realizado nas abas de Honorários, Diárias, Taxas, Serviços ou demais abas.

O que é importado pela **Parcial Complementar** são as Autorizações da parcial original a que se refere.

Aba resumo:

Registro de atendimento , aba guia de autorização:

## **03. CANCELAR UMA PARCIAL COMPLEMENTAR**

Se for necessário cancelar a 'Parcial Complementar', basta selecionar a parcial complementar desejada e executar a rotina **Cancela Parcial.**

As validações e permissões são as mesmas de uma parcial normal, caso tenha algum item lançado não será permitido cancelar. Se a permissão for concedida, as guias geradas por essa complementar serão canceladas ou excluídas.

As datas da parcial anterior não serão alteradas.

Parcial Complementar cancelada com sucesso.

## **04. TABELAS UTILIZADAS**

* **SZPARCIALATEND**
* **SZATENDAUTORIZCAB**
* **SZATENDAUTORIZ**

Alterar Início da Parcial

## **01. VISÃO GERAL**

Esse documento tem como objetivo explicar o processo de alteração da data de início da parcial.

## **02. VALIDAÇÕES**

**Campos de preenchimento e obrigatório:  data e hora**

* O status Parcial deve ser igual a Elaboração.
* Não é permitido alterar a data inicial da primeira parcial.
* A nova data deve ser diferente que a data da parcial corrente.
* A nova data deve ser inferior a data final da parcial.
* A nova data deve ser inferior a data de Alta.
* A nova data deve ser maior que a data do inicio do atendimento**.**
* A nova data dever ser maior que a data inicial da parcial anterior ativa daquela mesma unidade de faturamento.
* Não será permitido nenhuma movimentação no item de débito que já teve uma Nota Fiscal Gerada Por Item de Débito, do Gasto Particular.
* Vide item "05. Validações para múltiplas notas fiscais em Gastos Particulares" no link <https://tdn.totvs.com/x/pObAI>

## **03. EXEMPLO DE UTILIZAÇÃO**

* Deverá ser escolhida uma parcial na tela de Elaboração de Conta, em seguida clicar no menu de processo e escolher a opção de Alterar Início da Parcial.

* Será exibida na tela, um campo de texto, junto com o calendário para selecionar ou informar a data a ser alterada.

* Ao acionar o botão Executar será exibida na tela de log com o resultado do processamento pode ser com sucesso ou aviso das validações.
* Após o processamento com sucesso, a rotina deverá mover os itens de uma parcial para outra nas seguintes condições:

* + A unidade de atendimento da parcial alterada é do tipo internação
  + Com a mudança da data, se existirem lançamentos na parcial anterior que deve ser movida para a parcial que sofreu alteração na data.
  + Com a mudança da data, existirem lançamentos na parcial alterada que deve ser movida para a anterior.
  + Se houver mudança de contrato, recalcular os valores dos itens transferidos.
  + Serão alterados os vínculos com o pedido de exame.

Exemplo:

Alterar a data da parcial com o data igual ou superior a vigência

* Honorário cadastrado como exemplo

Em condições contratuais, dois contratos com vigências diferentes

Execução do processo:

Após  alteração da data inicial:

Parcial anterior recebeu a data final menos um segundo, a data inicial da parcial alterada

## **04.****TABELAS UTILIZADAS**

* SZPARCIALATEND
* SZCONTROLREPASSE
* SZATENDHONORARIO
* SZATENDDIARIAS
* SZATENDTAXASERV
* SZATENDMATMED
* SZATENDSADT
* SZLANCMMTERCEIRO
* SZATENDITEMGRATIS
* SZATENDGASTOPARTIC

Cancelar Parcial

## **01. VISÃO GERAL**

Essa rotina tem a finalidade de cancelar uma parcial.

## **02. PRÉ REQUISITOS**

Para efetuar o cancelamento, alguns critérios devem ser observados:

1. 1. **Cancelamento da primeira parcial:**  
      Não é permitido cancelar a primeira parcial, seja ela **EXTERNA** ou **INTERNA**.
   2. **Cancelamento de parciais de INTERNAÇÃO:**  
      A parcial de internação só poderá ser cancelada se:

      * For a **última parcial de internação**;
      * A parcial de internação anterior estiver em status **"em elaboração"** ou **"liberada"**, permitindo que sua **data final seja ajustada**.

      Em ambos cenários, a data final da parcial anterior será atualizada para a data final da parcial cancelada.

## **03. EXEMPLO DE UTILIZAÇÃO**

**Passos para cancelamento de parcial:**

1. **Selecionar a parcial:**  
   Na tela de **Elaboração de Conta**, escolha a parcial que deseja cancelar.
2. **Acessar o menu de processo:**  
   Clique no menu de processo e selecione a opção **"Cancelar Parcial"**.
3. **Executar o cancelamento:**  
   Ao acionar o botão **"Executar"**, o sistema exibirá uma tela de log com o resultado do processamento. Esse resultado pode indicar **sucesso** ou **avisos** relacionados às validações mencionadas anteriormente.
4. **Atualização automática:**  
   Após o processamento, a parcial que receberá os dados da parcial cancelada terá seu **resumo recalculado automaticamente** e os **repasses remanejados**.

## **04. TABELAS UTILIZADAS**

* SZPARCIALATEND
* SZATENDRESUMO
* ESTORNADO
* SZMOVIESTOQUE
