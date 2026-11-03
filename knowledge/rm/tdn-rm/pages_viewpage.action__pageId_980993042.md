---
content_hash: e37cf2aa82893b3e89d71b190fde357c5c3a2b96ed43c61e4849856575945943
fetched_at: '2026-06-29T00:12:15.544808+00:00'
page_id: '980993042'
product: rm
source: tdn-rm
title: Customização de dados no registro do boleto híbrido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=980993042
version: 11
---

Para que os dados do registro online do boleto híbrido sejam enviados de forma personalizada, é necessário:

* **Cadastro do layout**

  + Acesse a opção **“[Layout Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online)”**, disponível no menu **Movimentações Bancárias | Bancos e Agências**.
  + Cadastre os campos que farão parte do layout de envio.
* **Associação ao convênio**

  + No cadastro do convênio, configure o anexo **[Associação do Layout de Registro Online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759)**.
  + Nessa configuração, será possível:

    - Definir valores fixos para determinados campos;
    - Criar fórmulas que retornem valores customizados, conforme a necessidade.

**Configuração dos campos de layout do Registro Online do Boleto Híbrido**

Todos os campos customizados devem ser iniciados com a palavra "TBoletoHibrido".

Campos do tipo data devem ser formatado para "DD/MM/AAA" (31/12/2025)

Campos valores devem usar vírgula para o separador de decimais (99,99)

Abaixo segue como o campo deve ser cadastrado no layout de registro online, formato e valores possíveis.

**Alguns bancos possuem regras específicas para um determinado campo, [clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=864326633#TOTVSBoletoH%C3%ADbrido-Particularidadesporbancoparaconfigura%C3%A7%C3%A3odeboletonoERP) para consultar essas regras.**

Dados Principais:

* Identificador do seu número

Campo: **TBoletoHibrido.BankSlipClientNumber**

Ex: 00000123456

* Valor da transação

Campo: **TBoletoHibrido.Amount**

Ex: 10,12 (Utilizar vírgula para separador de decimais)

* Mensagem personalizada

Campo: **TBoletoHibrido.****MessageToPayer**

Ex: Efetuar o pagamento até a data de vencimento 

* Numero de dias para negativação

Campo: **TBoletoHibrido.DaysToNegativeReport**

Ex: 10

* Número de dias para protesto

Campo: **TBoletoHibrido.DaysToProtest**

Ex: 30

Dados de Vencimento

* Data de vencimento

Campo: **TBoletoHibrido.Due.DueDate**

Ex: 15/09/2025 (Formato DD/MM/AAAA)

* Até quantos dias após o vencimento a Transação pode ser paga

Campo: **TBoletoHibrido.Due.DayValidAfterDue**

Ex: 5

Dados de desconto

* Modalidade do desconto

Campo: **TBoletoHibrido.****Due.AmountDetails.Discount.Modality**

Valores possíveis: **(Verificar se o banco disponibiliza a modalidade. Caso o banco não atenda a modalidade enviada, o registro não irá ocorrer retornando erro)**

**FixedValueUntilInformedDate -** Valor Fixo até a[s] data[s] informada[s]

**PercentageUntilTheDateInformed -** Percentual até a data informada: 

* Data limite para o primeiro desconto

Campo: **TBoletoHibrido.****Due.AmountDetails.Discount.FixedDate1.Date**

Ex: 15/09/2025 (Formato DD/MM/AAAA)

* Valor do primeiro desconto

Campo: **TBoletoHibrido.****Due.AmountDetails.Discount.FixedDate1.Value**

Ex: 30,12

* Data limite para o segundo desconto

Campo: **TBoletoHibrido.****Due.AmountDetails.Discount.FixedDate2.Date**

Ex: 15/09/2025 (Formato DD/MM/AAAA)

* Valor do segundo desconto

Campo: **TBoletoHibrido.****Due.AmountDetails.Discount.FixedDate2.Value**

Ex: 30,12

* Data limite para o terceiro desconto

Campo: **TBoletoHibrido.****Due.AmountDetails.Discount.FixedDate3.Date**

Ex: 15/09/2025 (Formato DD/MM/AAAA)

* Valor do terceiro desconto

Campo: **TBoletoHibrido.****Due.AmountDetails.Discount.FixedDate3.Value**

Ex: 30,12

Dados para multa

* Valor da multa

Campo: **TBoletoHibrido.Due.AmountDetails.Fine.Value**

Ex: 0,20

* Modalidade da multa:

Campo: **TBoletoHibrido.Due.AmountDetails.Fine.Modality**

Valores possíveis: **(Verificar se o banco disponibiliza a modalidade. Caso o banco não atenda a modalidade enviada, o registro não irá ocorrer retornando erro)**

**FixedAmount -** Valor Fixo

**Percentage -** Percentual

Dados para juros: 

* Valor do juros

Campo: **TBoletoHibrido.Due.AmountDetails.Interest.Value**

Ex: 0,03

* Modalidade do juros

Campo: **TBoletoHibrido.Due.AmountDetails.Interest.Modality**

Valores possíveis: **(Verificar se o banco disponibiliza a modalidade. Caso o banco não atenda a modalidade enviada, o registro não irá ocorrer retornando erro)**

**AmountCalendarDay -** Valor (dias corridos)

**PercentagePerCalendarDay -** Percentual ao dia (dias corridos)

**PercentagePerCalendarMonth -** Percentual ao mês (dias corridos)

**PercentagePerCalendarYear -** Percentual ao ano (dias corridos)

**AmountBusinessDay -** Valor (dias úteis)

**PercentagePerBusinessDay -** Percentual ao dia (dias úteis) 

**PercentagePerBusinessMonth -** Percentual ao mês (dias úteis)

**PercentagePerBusinessYear -** Percentual ao ano (dias úteis) 

Dados para abatimento

* Valor do abatimento

Campo: **TBoletoHibrido.Due.AmountDetails.Rebate.Value**

Ex: 45,78

* Modalidade do abatimento

Campo: **TBoletoHibrido.Due.AmountDetails.Rebate.Modality**

Valores possíveis **(Verificar se o banco disponibiliza a modalidade. Caso o banco não atenda a modalidade enviada, o registro não irá ocorrer retornando erro)**

**FixedAmount -** Valor Fixo

**Percentage -** Percentual

Dados do cliente (Pagador):

* Nome

Campo: **TBoletoHibrido.Customer.Name**

Ex: Fulano de Tal da Silva

* CPF / CNPJ

Campo: **TBoletoHibrido.Customer.Ssn**

Ex: 123.456.789-00 ou 17.114.771/0001-02

* Endereço

Campo: **TBoletoHibrido.Customer.Street**

Ex: Rua do Endereço Tal

* Número do endereço

Campo: **TBoletoHibrido.Customer.AddresNumber**

Ex: Sem número

* Complemento do endereço

Campo: **TBoletoHibrido.Customer.AddresComplement**

Ex: APTO XXX

* Bairro

Campo: **TBoletoHibrido.Customer.Neighborhood**

Ex: Nova Tal (Máximo 15 caracteres)

* Cidade

Campo: **TBoletoHibrido.Customer.City**

Ex: Cidade Tal

* Estado

Campo: **TBoletoHibrido.Customer.State**

Ex: Rio de Janeiro

* CEP

Campo: **TBoletoHibrido.Customer.PostalCode**

Ex: 30465-640

* E-mail

Campo: **TBoletoHibrido.Customer.Email**

Ex: xxxxxx@yyyy.com.br

Exemplo dos campos cadastrados no anexo de Layout de Registro Online do Banco

Exemplo dos campos cadastrado na Associação de Layout de Registro Online
