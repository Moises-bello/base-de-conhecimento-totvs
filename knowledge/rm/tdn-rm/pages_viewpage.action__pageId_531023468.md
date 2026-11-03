---
content_hash: 1aea30dbbb459dfc235b87a3ef16b308b145bb34f76484ad728616b5039054a5
fetched_at: '2026-06-29T00:10:35.632529+00:00'
page_id: '531023468'
product: rm
source: tdn-rm
title: Convênio Fat.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531023468
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Dados de faturamento**
3. **CNES**
4. **Grupos de convênio**
5. **Padrão de informações**
6. **Registro ANS**
7. **Fonte remuneração**
8. **Código singular**

## **01. VISÃO GERAL**

Cadastro de todos os Convênios do Prestador Principal. 

## **02. DADOS DE FATURAMENTO**

Anexos - Convênio - Dados de Faturamento  
Dias de Entrega  
Dias do mês que são aceitas as Faturas pelo Convênio.  
Tipo de Entrega  
Usado para informação do dia de entrega das faturas do convênio.  
Regras de Recebimento  
1º - Se a opção Dia Mês / Dia Útil for selecionada então defiremos mais os seguintes campos:  
a) – Previsão dia receb  
b) - Mês Controle: valores fixos para definição do dia previsto  
2 - Se a opção de Número de Dias após a data da Fatura for selecionada então teremos de definir o seguinte campo:  
a) Número de Dias : Definirá o número de dias que será considerado no cálculo para definição da data de recebimento.

**OBS:**

Campo destinado a realizar quaisquer observações sobre o registro inserido

## **03. CNES**

Usado para identificação do número do Cadastro Nacional de Estabelecimentos de Saúde,composto por sete dígitos, sendo os seis primeiros seqüenciais e um dígito verificador.

## **04. GRUPOS DE CONVÊNIOS**

Define em qual Grupo o Cadastro será inserido.

## **05. PADRÃO DE INFORMAÇÕES**

Padrão de Informação de Faturamento do convênio. Alguns Convênios possuem seus próprios Padrões, utilizando-os para o Faturamento Eletrônico.

## **06. REGISTRO ANS**

Código do registro junto a ANS – Agência Nacional de Saúde Suplementar – da operadora responsável pela internação. Esta informação é utilizada no arquivo de Exportação para o Ministério da Saúde - Comunicação de Internação Hospitalar – CIH.  
Tipo Faturamento (Fatura, Nota Fiscal ou Sem ônus)  
Define qual Tipo de Faturamento o Convênio utiliza.  
Fatura: Utilizado para Convênios que emitem o seu faturamento no papel ou em arquivo  
Nota Fiscal: Utilizado para Convênios Particulares do Prestador Principal.  
Sem ônus: Tipo de convênio próprio do Prestador Principal que não gera ônus.  
Quando o 'Grupo de Convênios' selecionado for "Particular", o tipo de faturamento NÃO poderá ser "Fatura". Uma mensagem informativa será exibida alertando o usuário caso ele tente fazer esta parametrização.Para Grupos de Convênios do tipo Particular, o tipo de faturamento poderá ser do tipo "Nota Fiscal" ou "Sem ônus".

## **07. FONTE REMUNERAÇÃO**

Fonte de remuneração/financiamento da Internação. Esta informação é utilizada no arquivo de Exportação para o Ministério da Saúde – Comunicação de Internação Hospitalar – CIH.

## **08. CÓDIGO SINGULAR**

Para todos os prestadores de sistemas de saúde, que utilizam padrão de faturamento Unimed - BH, o preenchimento deste campo torna-se obrigatório, para efeito de fauramento de contas.

## **09. INTEGRAÇÃO**

Clientes/Fornecedores classificados como **Cliente**, só podem ter lançamentos **A Receber**

Clientes/Fornecedores classificados como \*\* **Fornecedores**, só podem ter lançamentos \*\* **A Pagar****{**}

Clientes/Fornecedores classificados como \*\* **Ambos**, podem ter lançamentos \*\* **A Pagar e A Receber.****{**}

O Saúde manda esta informação sempre fixa (campo FCFO.PAGREC), diretamente no financeiro alterar para ambos a qualquer momento. Uma vez alterado para **ambos**, e o cliente/fornecedor tiver registros **A Pagar e A Receber** ele não pode alterar mais. As alteraçãoes realizadas no Saúde não pode alterar este campo.
