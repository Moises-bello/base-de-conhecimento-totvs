---
content_hash: 6687f3dde76c22af796948270efa7c473fa45910d810d2871bde7b8a50e1029d
fetched_at: '2026-06-29T00:09:47.705388+00:00'
page_id: '435105050'
product: rm
source: tdn-rm
title: Cadastros - Parâmetros de Integração Financeira para Aluguel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105050
version: 9
---

Os Parâmetros de Integração Financeira são responsáveis por orientar o sistema  TOTVS Incorporação durante a execução de processos que integrem parcelas  a lançamentos do sistema TOTVS Gestão Financeira,  como Filiais, Centros de Custos, Natureza Financeira dos lançamentos e até o Tipo de documento  que será criado para pagamentos e recebimentos.

**Pré-Condições:**

* Ter incluído uma
* Ter Criado uma Filial
* Ter Cadastrado um
* Ter Cadastrado as

**Incluindo um Parâmetro de Integração Financeira**

* Passo 1 - Acesse: TOTVS Incorporação/ Aluguel/ Cadastros/ Parâmetros de Integração Financeira.
* Passo 2 - Clique em Incluir. Preencha os campos conforme desejar e clique em salvar. Os campos são:
  + **Id Parâmetro:** Código Identificador  do Parâmetro de Integração
  + **Descrição:** Descrição do Parâmetro de Integração
  + **Departamento**: Código Identificador do Departamento Empresarial
  + **Centro de Custo**: Código Identificador do Centro de Custo
  + **Natureza Financeira a Pagar**: Id da Natureza Financeira a Pagar
  + **Natureza Financeira a Receber:** Id da Natureza Financeira a Pagar
  + **Tipo de Documento a Pagar:** Id Do Tipo de Documento a pagar, gerado para um  Fornecedor ou Ambos
  + **Tipo de Documento a Receber:** Id Do Tipo de Documento a pagar, gerado para um  Fornecedor ou Ambos
  + ****Tipo de Documento  a Pagar Condicional:****Define o Tipo de Documento que será utilizado para identificar os Lançamentos Financeiros de Repasse Condicional, criado ao gerar os Lançamentos Financeiros das parcelas de aluguel. Ao cadastrar o Tipo de documento deve estar com o campo [Pagar ou  Receber] com o valor "A Pagar e A Receber".
* **Utiliza Lançamentos Futuros Como Provisão:** O sistema entende como lançamentos futuros aqueles que são referentes a períodos que iniciam após 30 dias da data do sistema no momento da geração dos lançamentos.
* **Código do Tipo de Documento a Receber(Futuro):** Define o Tipo de Documento a receber para lançamentos futuros.
* **Código do Tipo de Documento a Pagar(Futuro):** Define o Tipo de Documento a pagar para lançamentos futuros.
* **Tabelas Opcionais:**
* **Histórico do Lançamento no****TOTVS Gestão Financeira:** Este campo apresenta as variáveis pré definidas (quando são selecionadas), abaixo segue a descrição de cada uma delas;  
  **Variáveis Pré-Definidas:** Quando selecionadas estas possibilitará listar informações no Histórico dos Lançamentos   
  financeiros gerados no sistema, cada variável possui sua respectiva função e contextos de uso:

  | **Variável** | **Descrição** | Contextos de uso |
  | --- | --- | --- |
  | **[CADM]** | Código do Contrato de Administração; | Incluir lançamento financeiro (Evento financeiro), Gerar lançamentos financeiros (Contrato de locação), Efetivar confissão de dívida (Confissão de dívida) |
  | **[CALG]** | Código do contrato de Locação; ***(Obs: Na confissão de dívida só será preenchido quando a confissão for gerada por contrato)*** | Incluir lançamento financeiro (Evento financeiro), Gerar lançamentos financeiros (Contrato de locação), Gerar Lançamentos (Fechamento do Condomínio Integral), Gerar lançamentos financeiros (Fechamento do Condomínio Individualizado), Efetivar confissão de dívida (Confissão de dívida) |
  | **[IMOV]** | Código do Imóvel; ***(Obs: Na confissão de dívida só será preenchido quando a confissão for gerada por contrato)*** | Incluir lançamento financeiro (Evento financeiro), Gerar lançamentos financeiros (Contrato de locação), Gerar Lançamentos (Fechamento do Condomínio Integral), Gerar lançamentos financeiros (Fechamento do Condomínio Individualizado), Efetivar confissão de dívida (Confissão de dívida) |
  | **[NUMLOC]** | Número do contrato de locação | Incluir lançamento financeiro (Evento financeiro), Gerar lançamentos financeiros (Contrato de locação), Gerar lançamentos financeiros (Fechamento do Condomínio Individualizado), Efetivar confissão de dívida (Confissão de dívida) |
  | **[IPER]** | Início do Período | Gerar lançamentos financeiros (Contrato de locação), Gerar Lançamentos (Fechamento do Condomínio Integral) |
  | **[FPER]** | Fim do Período | Gerar lançamentos financeiros (Contrato de locação), Gerar Lançamentos (Fechamento do Condomínio Integral) |
  | **[ICOMP]** | Inicio da Competência | Gerar lançamentos financeiros (Contrato de locação), Gerar Lançamentos (Fechamento do Condomínio Integral), Gerar lançamentos financeiros (Fechamento do Condomínio Individualizado) |
  | **[FCOMP]** | Fim da Competência | Gerar lançamentos financeiros (Contrato de locação), Gerar Lançamentos (Fechamento do Condomínio Integral), Gerar lançamentos financeiros (Fechamento do Condomínio Individualizado) |
  | **[DIMO]** | Descrição do Imóvel | Incluir lançamento financeiro (Evento financeiro), Gerar Lançamentos (Fechamento do Condomínio Integral), Gerar lançamentos financeiros (Fechamento do Condomínio Individualizado), Efetivar confissão de dívida (Confissão de dívida) |
  | **[COBR]** | Item de Cobrança | Gerar lançamentos financeiros (Fechamento do Condomínio Individualizado) |
* **Conta Caixa:**
* **Percentual multa de atraso / juros de mora:** Campos que permite definir o comportamento de cobrança de juros e multa por atraso nos lançamentos que serão gerados pelo Contrato de Locação. Segue os campos para essa parametrização:
* **Tipo de Juros Dia:** Permite definir como será cobrado o Juros Dia, tendo como opções por Taxa (%) ou Valor; **% de juros/mora:** Campo no qual permite definir o valor de Juros Dia dos lançamentos a serem gerados. Esse campo pode conter o valor na forma de Taxa (%) ou Valor (R$), conforme selecionado no campo "Tipo de Juros Dia"; **% multa atraso:** Campo no qual permite definir o valor da multa atraso. Esse campo sempre será preenchido com valores na forma de Taxa (%).

**Aonde o Tipo de Documento a Pagar Condicional é Utilizado:**

* Cadastro do Modelo de Contrato de Locação
* Cadastro de Contrato de Locação
* Lançamentos Financeiros  de um Contrato de Locação Vinculado a um Contrato de Administração através do Imóvel.
