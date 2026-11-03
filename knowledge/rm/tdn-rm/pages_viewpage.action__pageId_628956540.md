---
content_hash: 075571c4cd24ca1f590479f30cc2ba8eede55fd5ae1b1a24143ee3d14c2a3d21
fetched_at: '2026-06-29T00:11:05.294093+00:00'
page_id: '628956540'
product: rm
source: tdn-rm
title: Geração do Movimento de Fatura
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628956540
version: 13
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Gerando o movimento de fatura**
3. **Formas de Agrupamento**
4. **Gerando o movimento de fatura para **Hemocomponentes****
5. **Excluindo o movimento de fatura**
6. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O movimento de fatura consiste no envio dos dados financeiros da fatura para o BackOffice integrado.

Quando integrado com o BackOffice RM, o movimento pode gerar o lançamento financeiro e o contábil.

## **02. GERANDO O MOVIMENTO DE FATURA**

* Acesse o menu Faturamento > Particular e Convênios > Faturamento para Convênios

### **1. Selecionar a fatura**

* Selecione a fatura com o status Faturada
* Execute o processo Gerar Movimento de Fatura

### 2. Tipo de movimento

* O tipo de movimento a ser gerado será preenchido de acordo com o parâmetro abaixo.

### 3. Condição de Pagamento

A condição de pagamento já vem carregada, quando se é definido um valor default, no tipo de movimento.

Mas é possível alterar o valor.

### 4. Natureza Financeira

A natureza financeira só é utilizada na integração com o BackOffice Protheus

## **03. FORMAS DE AGRUPAMENTO**

O agrupamento dos gastos da fatura, pode ser parametrizado de 3 formas:

### 1.Descrição única

Esta opção é habilitada quando o parâmetro em *Opções | Parâmetros | Parâmetros Gerais | Faturamento / Utilizar sempre discriminação única na NF*  estiver selecionado e se houver algum produto parametrizado para utilização na descrição única em *Opções | Parâmetros | Integração RM Nucleus | Aba geral / Pedido NF/Recibo Paciente.*

### *2.  Por grupo de gasto*

O agrupamento dos gastos por grupo de gastos é realizado quando:

* a parametrização do item*"Agrupamento de todos lançamentos em uma única descrição"*desmarcada
* a parametrização "Geração de movimento agrupado por grupo de gasto" estiver marcada
* e o parâmetro em *Cadastros | Faturamento | Grupos de Gasto / Agrupa Nota Fiscal* estiver marcado

### *3.  Por codificação*

O agrupamento dos gastos por codificação é realizado quando o convênio referente à fatura possuir produtos associados em *Cadastros | Faturamento | Condições Contratuais com Convênios / Padrão de Faturamento e Codificação*

Para essa parametrização ser executada é necessário que os parâmetros dos itens *"Agrupamento de todos lançamentos em uma única descrição"* e "Geração de movimento agrupado por grupo de gasto" estejam desmarcados.

## **04. GERANDO MOVIMENTO DE FATURA PARA HEMOCOMPONENTES**

No **TOTVS Gestão Hospitalar**, acesse o menu **Cadastros /  Condições Contratuais com Convênios**.

1. Selecione o convênio e acesse a aba **Faturamento Hemocomponentes**.
2. Marque a opção **Fatura de Hemocomponentes** e selecione o tipo de faturamento desejado.

3. Crie um atendimento para este convênio e, conforme a parametrização realizada, lance os itens na conta. Caso a conta seja dos tipos 1 ou 2, se entende que essa conta deverá conter Hemocomponentes. Os Hemocomponentes serão entendidos como pacotes pelo sistema (RM Saúde), portanto, no cadastro da taxa ou serviço, o campo “pacote”, deverá estar marcado.

4. A partir deste momento, esta conta é considerada uma conta do tipo “pacote” ou seja, todos os itens que não sejam pacotes, lançados nesta conta, constarão como pertencentes a algum pacote.

5. Caso seja necessário que o Item seja considerado como um “**Item Avulso**”, clique com o botão direito sobre ele e clique na opção Incluir Item na cobrança de pacote. O Item  passará a ter o campo “**INCLUIDOPACOTE” = T**, em sua respectiva tabela.

6. Encerre a conta do paciente.

7. Acesse o menu **Faturamento / Fatura para Convênios** e crie uma nova remessa para o convênio utilizado.

8. Para gerar de movimento de fatura, contendo esta conta recém encerrada.

* Selecione a fatura com o status Faturada
* Execute o processo Gerar Movimento de Fatura do SUS

## **05. EXCLUINDO O MOVIMENTO DE FATURA**

Através desse processo, será possível excluir o movimento de fatura .

* Selecione a fatura com o status Faturada e que tenha identificador do movimento.
* Execute o processo Excluir Movimento de Fatura.

## **06. TABELAS UTILIZADAS**

* SZFATURACONVENIO
* SZFATURAITEMMOV

Tabelas  do Faturamento de Hemocomponentes :

* SZFATURAHEMOCOMP: Tabela Pai, onde estarão as informações referentes à fatura recém-criada, como a soma do valor de todos os itens, informações sobre o convenio, unidade, etc.
* SZFATURAHEMOCOMPPCT: Tabela onde serão armazenados os dados referentes aos pacotes, onde constarão as informações como Descrição, quantidade, valor, valor total, entre outras.
* SZFATURAHEMOCOMPITEM: Tabela onde serão armazenados os dados referentes aos itens.
