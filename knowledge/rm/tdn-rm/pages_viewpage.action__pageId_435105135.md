---
content_hash: 1e2d80fbeb8cede658b4ca1f99cd7e1c96153571d8a63a5a893d39963a156788
fetched_at: '2026-06-29T00:09:48.368161+00:00'
page_id: '435105135'
product: rm
source: tdn-rm
title: Cadastros - Modelo de Contrato de Locação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105135
version: 5
---

O cadastro de Modelo de Contrato permite ao cliente criar modelos  para facilitar a inclusão de contratos, evitando erros  e agilizando o preenchimento destes contratos de locação. Existe no Cadastro de Contrato de Locação um campo de preenchimento obrigatório, qual permite que o modelo de contrato seja vinculado, preenchendo automaticamente alguns outros campos com um valor padrão.

**Pré-Condições:**

* Ter incluído a [Regra de Vencimento](http://tdn.totvs.com/display/LRM/Regra+de+Vencimento "Regra de Vencimento")
* Ter incluído o [Parâmetro da Integração Financeira](http://tdn.totvs.com/pages/viewpage.action?pageId=435105050)
* Ter incluído o [Tipo de Evento Financeiro](http://tdn.totvs.com/display/LRM/Tipo+Evento+Financeiro "Tipo Evento Financeiro")
* Ter incluído um [Tipo de Contrato de Locação](http://tdn.totvs.com/pages/viewpage.action?pageId=435105420 "Tipo de Contrato Locação")
* Ter incluído um Índice.
* Ter incluído uma Fórmula de Reajuste.
* Ter incluído as Fórmulas Rescisórias.
* Ter incluído um registro RM Reports com [Tipo] 1000, 1016 e 1017.

**Incluindo um Modelo de Contrato de Locação**

* **Passo 1 -** Acesse: TOTVS RM/ Projeto/ Incorporação/ Aluguel/ Cadastros/ Modelo de Contrato
* **Passo 2 -** Clique em [Incluir].
* **Passo 3 -** Será exibido o formulário de cadastro de modelos de Contrato.Preencha os campos conforme o modelo desejado. Os campos são:

**Aba Identificação**

* **Código Modelo de Contrato**
* **Descrição do Modelo de Contrato**
* **Código da Regra de Vencimento:** A Regra de Vencimento definirá como o sistema criará os lançamentos financeiros para as parcelas do Contrato de Locação.

* + **Dia Fixo:** Se a regra de vencimento for definida como dia fixo, o sistema gerará a primeira parcela  com data de vencimento igual ao valor informado ao campo  **[1º Vencimento Em**] do contrato de locação qual o Modelo de Contrato de Locação foi vinculado e o restante das parcelas conforme  o dia fixo estabelecido na Regra de Vencimento.
  + **Dia Útil:** Se a regra de vencimento for definida como dia útil, o sistema gerará  a primeira parcela e o restante  com vencimento igual  ao dia útil estabelecido, ignorando a data informada ao campo  **[1º Vencimento Em]** do contrato de locação qual o Modelo de Contrato de Locação foi vinculado.

* **Tipo de pagamento**
* **Parâmetro de Integração financeira**
* **Tipo de evento financeiro**
* **Tipo de locação**
* **Bloqueia Taxas:** Este campo define se no contrato de locação os campos de informação de taxas vão ficar bloqueados ou não

**Aba Dados do Reajuste**

* Período de Reajuste

* + Periodicidade do Contrato de Locação
  + Data Base do Reajuste

* Reajuste por Índice

* + Índice
  + Defasagem Cotação
  + Valor do Índice Informado nas Cotações
  + Índice mensal ou índice acumulado

* Cálculo Pro-Rata-Dia
* Configuração Pró-Rata-dia

* + Rateio de Índice
  + Aplicação de Índice

* Capitalizado
* Reajuste por Fórmula

* + Fórmula de Reajuste

**Aba Dados da Rescisão**

* Informações para cálculos rescisórios por parte do Locatário

* + Tipo de Evento Financeiro
  + Taxa Rescisória
  + Fórmula Rescisória

* Informações para cálculos rescisórios por parte do Locatário

* + Taxa Rescisória
  + Fórmula Rescisória

**Aba Relatórios**

* Relatório default de "Contrato de Locação": neste campo serão listados apenas relatórios do tipo "1000 - Contrato de Locação".
* Relatório default de "Lista de Encerramento do Contrato": neste campo serão listados apenas relatórios do tipo "1016 - Lista de verificação de encerramento".
* Relatório default de "Encerramento/Rescisão": neste campo serão listados apenas relatórios do tipo "1017 - Encerramento/Rescisão do Contrato".
