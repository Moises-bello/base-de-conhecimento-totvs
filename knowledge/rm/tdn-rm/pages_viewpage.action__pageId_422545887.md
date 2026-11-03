---
content_hash: 8c5b588ff4d36a86e56e6104cc001ccd87b22624be17560a55debc6be61e3b77
fetched_at: '2026-06-29T00:09:21.728473+00:00'
page_id: '422545887'
product: rm
source: tdn-rm
title: Controle de Créditos Fiscais (Registro 1100, 1500, 1300 e 1700)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545887
version: 3
---

**Introdução**

O objetivo desse documento é oferecer uma visão geral do cadastro dos créditos fiscais de tributo e controle de valores retidos na fonte. Esses dados serão selecionados na geração dos registros 1100, 1500, 1300 e 1700 do EFD PIS COFINS  
    
 **Créditos Fiscais**

**Cadastro de Créditos Fiscais de Tributos**

Acessado pelo TOTVS Gestão Fiscal, através do menu Obrigações Principais | Apuração PIS/COFINS | opção Controle de Créditos Fiscais do Tributo. Os campos existentes são: Tributo (somente PIS ou COFINS), Mês e Ano do Crédito, Origem do Crédito, Tipo do Crédito, Valor do Crédito Apurado, Valor do Crédito Extemporâneo Apurado e Saldo Remanescente do Crédito. O Saldo Remanescente terá inicialmente a soma dos dois valores de crédito e será decrescido à medida que as compensações do crédito forem criadas.

Os créditos podem ser cadastrados manualmente ou geradas com base nos lançamentos fiscais do período considerado. Para esse fim, foi criado o processo "Geração de Créditos Fiscais de Tributos". Os valores serão originados da soma do valor do tributo dos itens dos lançamentos fiscais de entrada das filiais de mesmo CNPJ da filial corrente, para o mês e ano informados na tela do processo, agrupados pelo Tipo Crédito. Somente serão considerados os tributos cujo *Tipo do Tributo* seja PIS ou COFINS. Caso o lançamento tenha status "Normal" o valor será armazenado no campo *Valor do Crédito Apurado*, se "Extemporâneo" no campo *Valor do Crédito Extemporâneo Apurado*.

**Cadastro de Compensação do Crédito**

A compensação do crédito fiscal gerado deve ser criada via anexo Compensação de Créditos Fiscais de Tributos onde são informados os campos de Mês e Ano da compensação, que deve ser igual ou posterior ao crédito, Tipo da Compensação e o Valor. Após a inclusão/alteração do registro de compensação o campo Saldo Remanescente do Crédito é atualizado. O somatório do valor de todas as compensações não pode ser superior ao total do crédito vinculado.

**Movimento/Lançamentos Fiscais**

Para a geração dos registros de créditos fiscais via processo é necessário que seja preenchido no item do lançamento fiscal o campo de nome Tipo Crédito, a ser preenchido com os valores permitidos para o campo *Código do Tipo do Crédito* (COD\_CRED) do layout do EFD PIS/COFINS. Para ter a informação na nota (movimento) basta preencher o campo de mesmo nome e tipo no item do movimento que o mesmo será escriturado para o item do lançamento fiscal.  Para registrar uma nota como "Extemporâneo" é necessário marcar o flag de mesmo nome no movimento, informar os campos *Data de Entrada/Saída* e *Data de Emissão* com os valores reais da entrada/saída e emissão, sendo a data de emissão diferente da data do movimento, e preencher o campo *Data Lançamento*.

**Valores Retidos**

**Cadastro de Créditos Retidos na Fonte**

Acessado pelo RM Liber através do menu Cadastros/Tabelas Auxiliares/Obrigações Federais/Apuração PIS-COFINS/Controle de Créditos Fiscais de Tributos Retido. Os campos existentes são: Tributo (somente PIS ou COFINS), Mês e Ano, Natureza da Retenção, Valor Total da Retenção, Valor da Retenção da Restituição, Valor da Retenção da Compensação, Valor da Retenção Deduzida e Saldo da Retenção. O Saldo terá inicialmente a soma dos da retenção e será decrescido à medida que as compensações forem criadas.

Os créditos podem ser cadastrados manualmente ou geradas com base nos lançamentos financeiros do período considerado. Para esse fim, foi criado o processo "Geração de Valores Retidos na Fonte". Para PIS e COFINS retidos os valores serão originados da soma do valor do tributo dos lançamentos financeiros a receber das filiais de mesmo CNPJ da filial corrente, para o mês e ano informados na tela do processo (o filtro será feito pelo campo *Data da Baixa*), agrupados pela *Natureza da Retenção* (campo complementar do Cliente/Fornecedor). Somente serão considerados os tributos cujo *Tipo do Tributo* seja PIS RF ou COFINS RF. No caso das Contribuições Sociais Retidas na Fonte os valores serão originados da soma da base de cálculo do tributo dos lançamentos financeiros aplicado a alíquota de 0,65% para PIS e 3,00% para COFINS, sendo gerado um registro de crédito para cada tributo.

**Cadastro de Compensação do Crédito Retido**

A compensação do crédito fiscal gerado deve ser criada via anexo Compensação de Créditos Fiscais Retidos onde são informados os campos de Mês e Ano da compensação, que deve ser igual ou posterior ao crédito, Tipo da Compensação e o Valor. Após a inclusão/alteração do registro de compensação o campo Saldo da Retenção é atualizado. O somatório do valor de todas as compensações não pode ser superior ao total do crédito vinculado.

**Cliente/Fornecedor**

Para a geração dos registros de créditos fiscais via processo é necessário que seja criado no Cliente/Fornecedor o campo complementar com os seguintes dados:

|  |  |
| --- | --- |
| **Nome** | INDNATRET |
| **Tipo** | Alfanumérico |
| **Tamanho** | 5 |

Deve ser preenchido com os valores permitidos para o campo *Identificador de Natureza da Retenção na Fonte* (IND\_NAT\_RET) do layout do EFD PIS/COFINS.
