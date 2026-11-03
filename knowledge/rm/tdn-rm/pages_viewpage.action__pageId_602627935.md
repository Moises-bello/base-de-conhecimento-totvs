---
content_hash: 6c7e4389fb0341bb26c4f5ea2f20b444dbba5e7e9b15f44af71d103c5565a99b
fetched_at: '2026-06-29T00:10:58.004942+00:00'
page_id: '602627935'
product: rm
source: tdn-rm
title: Implantação e configuração - Integração da Natureza Financeira com outros backoffices
  (EAI)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=602627935
version: 8
---

## **1. Versões disponíveis**

* A implementação foi disponibilizada em todas as versões a partir dos patch's **12.1.29.271, 12.1.31.180 e 12.1.32.118**;
* Atualizar a versão do RM para os patch's **12.1.29.271, 12.1.31.180 ou 12.1.32.118**, conforme a versão utilizada pelo cliente;
* Executar o **R****M Atualizador.exe** para a criação do campo 'Natureza Financeira' nos parâmetros do Lançamento Financeiro na base.

## **2. Parametrização EAI 1.0**

Deverá ser atualizado o código onde é feito a inclusão das colunas CODCOLNATFINANCEIRA e CODNATFINANCEIRA:

* Em Integração | Integração | RM Conector | Mensagem Única | Integrações | Anexos | Mapeamento de entidade | ACCOUNTPAYABLEDOCUMENT 2.002:

* Editando o código de “ACCOUNTPAYABLEDOCUMENT” a partir de -+ linha 236, substituindo o código abaixo:

**parms.DataSet.Tables["PFINANCEIRO"].Columns.Add("CODCOLNATFINANCEIRA", typeof(string));**

**parms.DataSet.Tables["PFINANCEIRO"].Columns.Add("CODNATFINANCEIRA", typeof(string));**

**string natDefault = string.Empty;**

**natDefault = (string)this.ExtensionServices.GetParameter(this.DBS, "RH\_NATUREZAFINANCEIRADEFAULT",**

**RMSConvert.ToString(this.MapaIntegracao.IdIntegracao), 0);**

**//Cria a coluna IDLAN para compatibilizar com a mensageria.**

**foreach (DataRow r in parms.DataSet.Tables["PFINANCEIRO"].Rows)**

**{**

**r["IDLAN"] = r["IDFINANC"];**

**if (natDefault != string.Empty)**

**{**

**r["CODCOLNATFINANCEIRA"] = r["CODCOLIGADA"];**

**r["CODNATFINANCEIRA"] = natDefault;**

**}**

**}**

* Por este código listado abaixo:

**if (!parms.DataSet.Tables["PFINANCEIRO"].Columns.Contains("CODCOLNATFINANCEIRA"))**

**parms.DataSet.Tables["PFINANCEIRO"].Columns.Add("CODCOLNATFINANCEIRA", typeof(string));**

**if (!parms.DataSet.Tables["PFINANCEIRO"].Columns.Contains("CODNATFINANCEIRA"))**

**parms.DataSet.Tables["PFINANCEIRO"].Columns.Add("CODNATFINANCEIRA", typeof(string));**

**string natDefault = string.Empty;**

**try**

**{**

**natDefault = (string)this.ExtensionServices.GetParameter(this.DBS, "RH\_NATUREZAFINANCEIRADEFAULT",**

**RMSConvert.ToString(this.MapaIntegracao.IdIntegracao), 0);**

**}**

**catch**

**{**

**natDefault = string.Empty;**

**}**

**//Cria a coluna IDLAN para compatibilizar com a mensageria.**

**foreach (DataRow r in parms.DataSet.Tables["PFINANCEIRO"].Rows)**

**{**

**r["IDLAN"] = r["IDFINANC"];**

**if (natDefault != string.Empty)**

**{**

**r["CODCOLNATFINANCEIRA"] = r["CODCOLIGADA"];**

**r["CODNATFINANCEIRA"] = natDefault;**

**}**

**string codNatFin = RMSConvert.ToString(r["CODNATFINANCEIRA"], string.Empty);**

**if (String.IsNullOrEmpty(codNatFin))**

**throw new Exception("Natureza financeira Deve ser informada.");**

**}**

## **Atualizações e Operações no produto:**

* Deverá configurar no RM a natureza financeira para cada tipo de lançamento financeiro em Folha de Pagamento | Encargos | Financeiro | Cadastro Financeiros | Parâmetros | Parâmetros:

* Caso não tenha a ‘Natureza Financeira’ já cadastrada no Protheus, poderá ser criada em TOTVS SmartClient | SIGAFIN | Financeiro | Contas a Pagar | Contas a Pagar - selecione em ‘Outras Opções’ | Editar | clicar na lupa de ‘Natureza’, com isso o sistema irá abrir a lista de ‘Natureza’ e clicar em ‘Incluir’:

* Caso não tenha o mapeamento da ‘Natureza Financeira’ cadastrada no Protheus, poderá ser criado em TOTVS SmartClient | SIGACFG | Configurador | Ambiente | Schedule | De  / para de Mensagem - selecione a opção de ‘Incluir’ e cadastre o DE/ PARA conforme abaixo:

* Depois de efetuar o cadastro da ‘Natureza Financeira’ tanto no ‘RM’ quanto no ‘Protheus’ ir para RM | Folha de Pagamento | Encargos | Financeiro | Geração dos Lançamentos - gerar o Lançamento Financeiro:

**Observação: Caso tenha lançamentos financeiros gerados antes das alterações da ‘Natureza Financeira’ que deseje integrar, será necessário gerá-los novamente para preenchimento do campo ‘Natureza Financeira’ no envio para o protheus.**

* Em RM | Folha de Pagamento | Encargos | Financeiro | Lançamentos | Lançamentos (RM Labore) - selecione o lançamento que deseja integrar, clique em ‘Processos | Integração financeira com outros backoffices e execute o processo:

* Poderá conferir  a ‘Natureza Financeira’ em RM | Integrações | Mensagem Única | Fila de mensagens únicas:

* Poderá conferir  o lançamento no PROTHEUS, basta acessar TOTVS SmartClient |SIGAFIN|Financeiro| Contas a Pagar | Contas a Pagar:

## **3. Parametrização EAI 2.0**

**Observação: No EAI 2.0, não há a necessidade de atualização do source code do adapter, pois a alteração é realizada no código-fonte e já está disponível nas versões.**

## **Atualizações e Operações no produto:**

* Deverá configurar no RM a natureza financeira para cada tipo de lançamento financeiro em Folha de Pagamento | Encargos | Financeiro | Cadastro Financeiros | Parâmetros | Parâmetros:

* Caso não tenha a ‘Natureza Financeira’ já cadastrada no Protheus, poderá ser criada em TOTVS SmartClient | SIGAFIN | Financeiro | Contas a Pagar | Contas a Pagar - selecione em ‘Outras Opções’ | Editar | clicar na lupa de ‘Natureza’, com isso o sistema irá abrir a lista de ‘Natureza’ e clicar em ‘Incluir’:

* Caso não tenha o mapeamento da ‘Natureza Financeira’ cadastrada no Protheus, poderá ser criado em TOTVS SmartClient | SIGACFG | Configurador | Ambiente | Schedule | De  / para de Mensagem - selecione a opção de ‘Incluir’ e cadastre o DE/ PARA conforme abaixo:

* Depois de efetuar o cadastro da ‘Natureza Financeira’ tanto no ‘RM’ quanto no ‘Protheus’ ir para RM | Folha de Pagamento | Encargos | Financeiro | Geração dos Lançamentos - gerar o Lançamento Financeiro:

**Observação: Caso tenha lançamentos financeiros gerados antes das alterações da ‘Natureza Financeira’ que deseje integrar, será necessário gerá-los novamente para preenchimento do campo ‘Natureza Financeira’ no envio para o protheus.**

* Em RM | Folha de Pagamento | Encargos | Financeiro | Lançamentos | Lançamentos (RM Labore) - selecione o lançamento que deseja integrar, clique em ‘Processos | Integração financeira com outros backoffices e execute o processo:

* Poderá conferir  a ‘Natureza Financeira’ em RM | Integrações | Mensagem Única | Fila de mensagens únicas:

* Poderá conferir  o lançamento no PROTHEUS, basta acessar TOTVS SmartClient |SIGAFIN|Financeiro| Contas a Pagar | Contas a Pagar:

## **ASSUNTOS RELACIONADOS**

**[EAI 2.0](https://tdn.totvs.com/pages/viewpage.action?pageId=269063776)**
