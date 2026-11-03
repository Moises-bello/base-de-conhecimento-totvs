---
content_hash: afa0ed132ca22dbc2e312fe7fcf4c6c21c6feccd662f2b5763bb6eff8a2bc5cc
fetched_at: '2026-06-29T00:06:20.166006+00:00'
page_id: '221548738'
product: rm
source: tdn-rm
title: ER_PCREQ-8877_Venda
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8877_Venda
version: 155
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | Integração BackOffice RM x PDV Protheus | **IRM1** | PCREQ-7769 |
| **Requisito1** | PCREQ-8877 | **Subtarefa1** | PDR\_CP\_MOV009-100 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

 Implementação do adapter de integração via Mensagem Única TOTVS do cadastro de Cupom Fiscal com o PDV PROTHEUS, viabilizando assim o CRUD completo do cadastro por recebimento de mensagem de integração.

## Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de recebimento de Mensagens Únicas TOTVS para integração do cadastro de Cupom Fiscal, estando o adapter de envio desta mesma mensagem fora do escopo do requisito.

 

 A análise e o desenvolvimento do adapter será efetuado considerando a integração com o PDV Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cupom Fiscal | Inclusão/Alteração | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Fiscais\ Mais...\ Cupom Fiscal | - |
| Movimento | Inclusão/Alteração | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Vendas \ Faturamento\ Movimentação | - |

**Tabelas Utilizadas**

* TCUPOMFISCAL – Cupom Fiscal
* TCUPOMFISCALITM - Itens de Cupom Fiscal
* TCUPOMFISCALFIN - Pagamentos do Cupom Fiscal
* TMOV - Movimentos
* TITMMOV - Itens de Movimento

**Entidades de Integração**

* DataServer envolvido
  + MovCupomFiscalData
* Transformação
  + Id: RetailSales
  + Versão: 2.009
* SourceCode (Evento)
  + GUID: 1efe6424-027b-44af-8dd3-ef18a527d6b6

### **Regras de Integridade:**

Ao receber mensagem de Cupom Fiscal serão realizadas as seguintes ações para os campos abaixo:

**Cupom Fiscal:**

* **COO:** será utilizado o mesmo campo que o número.
* **CRO**: será obtido a partir do default do cadastro de Estação no RM, sendo assim é necessário ao cadastrar o Ponto de Venda informar este campo.
* **Redução Z:** deve ser preenchido após a integração do cupom fiscal, não sendo então integrado.
* **Acréscimo:** No Protheus o acréscimo é por cupom, com rateio para os itens. No RM esta informação será preenchido no campo VALORDESP que é a soma das despesas dos itens ou despesa aplicada ao cupom, NÃO irá incluir itens CANCELADOS. Caso não seja enviado acréscimo, será considerado como valor default o valor 0 (zero).
* **Valor Líquido:** a fórmula de cálculo para obter o valor líquido é:  VALORLIQUIDO = ( ∑ ( Preço item X Quantidade item) - Desconto + Acréscimo total ). Não deve ser considerado Itens Cancelados. Caso não seja enviado o valor líquido será considerado como valor default o valor 0 (zero).
* **Valor Recebido:** será preenchido com o mesmo valor do campo Valor Líquido.
* **Desconto:** No RM o campo que armazena esta informação é VALORDESC. Este campo é soma dos descontos dos itens ou desconto aplicado ao cupom, NÃO inclui itens CANCELADOS! Caso não seja enviado o valor líquido será considerado como valor default o valor 0 (zero). Sempre será lido o valor líquido e as despesas do valor original enviado. Mas os descontos, serão recalculados para evitar erro no arredondamento.  
  **Observação:** no Protheus o desconto pode ser por item, por cupom, ou ambos.
* **CNPJ Adquirente:** esta informação será gravada no RM somente se for enviado na mensagem.
* **Nome Adquirente:**esta informação será gravada no RM somente se for enviado na mensagem.

**Item do Cupom Fiscal:**

* **Preço unitário:**O preço unitário enviado pelo Protheus será o preço do produto.
* **Natureza da Operação:** Obtida a partir da Tributação.
* **Alíquota:**Obtida a partir da Tributação.
* **CST:**Obtida a partir da Tributação.

**Lista de Pagamentos:**

* **Débito/Crédito:** fixo crédito (não será trafegado).

**Cupom Fiscal - SAT / NFC-e**

Serão aplicadas as mesmas regras listadas acima para Cupom Fiscal, porém este tipo de Cupom irá criar um Movimento, ou seja, não será gerado o registro na tabela de Cupom Fiscal.

O tipo de movimento de venda que será utilizado é o definido no cadastro de Ponto de Venda. Neste tipo de movimento na etapa **Fis - Escrituração 1/2**, deve ser informado o **Tipo de Documento:**

**SAT**: **Código do Modelo 59 - CUPOM FISCAL ELETRÔNICO – SAT (CF-E-SAT).**

****NFC-e**: **Código do Modelo 65 - Nota Fiscal Eletrônica ao Consumidor Final.****

**Movimento associado ao Cupom Fiscal**

O serviço de inclusão de Cupom Fiscal também realiza a inclusão de um movimento e associa este movimento ao Cupom. Sendo assim torna-se necessário informar no cadastro de **Ponto de Venda** qual será o **Tipo de Movimento de Venda** que será utilizado. Este tipo de movimento deve possuir as seguintes configurações mínimas:

| **Etapa** | Campo | Valor | Observação |
| --- | --- | --- | --- |
| Mov - Identificação | Código | 2.X.XX | Tipo de movimento utilizado para NFC-e deve começar como 2.2.XX. |
| Edita Numeração | Edita ou Mostra |  |
| Mov - Datas 1/2 | Edição da Data de Emissão | Edita ou Mostra |  |
| Mov - Valores Financeiros 1/4 | Desconto | Marcado |  |
| Tipo de Desconto | Valor |  |
| Despesa | Marcado |  |
| Tipo de Despesa | Valor |  |
| Item - Valores Financeiros 1/2 | Utilizar Desconto | Marcado |  |
| Nome do Desconto | Desconto |  |
| Afeta Desconto do Movimento | Desmarcado |  |
| Tipo do Desconto | Valor |  |
| Utilizar Despesa | Marcado |  |
| Nome da Despesa | Despesa |  |
| Tipo de Despesa | Valor |  |
| Afeta Despesa do Movimento | Desmarcado |  |
| Fin - Condições de Pagamento | Utiliza edição de Meios de Pagamento | Marcado |  |
| Fis - Dados | Emite Cupom Fiscal | Marcado | Para Cupom Fiscal Tipo SAT este parâmetro deve ficar desmarcado. |
| Fis - Escrituração 1/2 | Código Default Tipo Documento Escrituração | Informar Código do Tipo de Documento | Para Cupom Fiscal Tipo SAT o Tipo de Documento informado deve possui Código Modelo do Documento 59 - CUPOM FISCAL ELETRÔNICO – SAT (CF-E-SAT).  Para Cupom Fiscal Tipo NFC-e o Tipo de Documento informado deve possui Código Modelo do Documento 65 - Nota Fiscal Eletrônica ao Consumidor Final. |
| Fis - NF-e | NFC-e | Informar o Tipo de Envio | Para Cupom Fiscal Tipo NFC-e este campo deve estar selecionado como Integrado por Terceiro. |

## Restrições e Ponto de Atenção

* **Cadastros necessários**  
  Para integrar o Cupom Fiscal é necessário realizar o cadastro e/ou carga inicial dos seguintes cadastros:
  + Envio de Unidade de Medida;
  + Envio de Produto / Códigos de Barras;
  + Envio de Ponto de Venda;
  + Envio de Vendedor.

* **Número do Caixa**  
  Na integração entre Protheus e RM sem mensagem única, é gravado neste campo o mesmo valor informado para o código do Ponto de Venda (F2\_PDV). Como o **Número do Caixa** do Cupom Fiscal no **RM** é do **tipo inteiro** e no **Protheus** este campo é do **tipo texto**, na integração atual via mensagem única esta informação será desconsiderada. Caso seja necessário realizar/ajustar algum relatório relacionado a esta informação, deve-se considerar do código do Ponto de Venda.
* ******Lista de Taxas******A lista de taxas (*ListOfTaxesType*) que serão aplicadas na Venda devem ser definidas no Tipo de Movimento uma vez que estas informações são desconsideradas no recebimento da mensagem e os valores de tributação são recalculados no RM.
* **Aplicação de Desconto/Acréscimo no Movimento**Para que o Desconto e Acréscimo seja corretamente aplicada no Movimento é obrigatório que o tipo de movimento esteja parametrizado como utilizado por "**Valor**" para estas duas informações, para o Movimento e para os Itens de Movimento. Caso contrário pode haver diferenças no arredondamento e assim gerar erros na inclusão.
* ******Rateio de Desconto/Acréscimo******  
  O rateio de desconto e acréscimo dos itens é calculado sempre que existir desconto e acréscimo informado por Cupom. Como no Protheus o desconto pode ser por item, por cupom ou ambos, ao receber um Cupom o RM irá recalcular o rateio de desconto dos itens para evitar erro no arredondamento.
* ******Cupom Fiscal - SAT******  
  Esta integração está disponível a partir do release 12.1.14.
* ******Cupom Fiscal - NFC-e******  
  Esta integração está disponível a partir do release 12.1.23.

**CUPOM FISCAL ELETRÔNICO – SAT / NFC-e**

## Fluxo do Processo

## Mapeamento de Campos

**Mensagem:**RetailSales

1horizontal1Versão 1.001

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **Descrição** | **RM** | | |
| **Tabela** | **Campo** | **Observação** |
| **CompanyId** | Código da empresa. | TCUPOMFISCAL | CODCOLIGADA | Código da Coligada é obtido a partir do De-Para de Filial. |
| **BranchId** | Código da filial |  |  |
| **CompanyInternalId** | InternalId da chave completa de empresa do produto |  |  |
| **InternalId** | InternalId de Integração | TCUPOMFISCAL | CODCOLIGADA|PONTOVENDA|CRO|NUMERO |  |
| **SellerInternalId** | InternalId do Vendedor | TPONTOVENDA | CODVEN1 | Buscar o código do vendedor no cadastro de Estação PDV |
| ComissionPercent | Percentual da Comissão |  |  |  |
| **CustomerVendorInternalId** | InternalId do Código do Cliente | TCUPOMFISCAL | CODCOLCFO|CODCFO |  |
| TotalPrice | Valor Total da Venda |  |  |  |
| **DiscountValue** | Valor Total de Desconto | TCUPOMFISCAL | DESCONTO |  |
| **IncreaseValue** | Valor de Acréscimo | TCUPOMFISCAL | ACRESCIMO |  |
| **NetPrice** | Valor Líquido da Venda | TCUPOMFISCAL | VALORLIQUIDO e VALORRECEBIDO |  |
| CashValue | Valor Pago em Dinheiro |  |  |  |
| ChecksValue | Valor Pago em Cheques |  |  |  |
| CardsValue | Valor Pago em Cartões de Crédito |  |  |  |
| DebitValue | Valor Pago em Cartões de Débito |  |  |  |
| CovenantValue | Valor Pago com Convênio |  |  |  |
| VouchersValue | Valor Pago com Vales |  |  |  |
| FinancedValue | Valor Pago com Financiamento |  |  |  |
| OthersValue | Valor Pago com Outras Formas |  |  |  |
| InputValue | Valor de Entrada |  |  |  |
| **IssueDateDocument** | Data de Emissão da Venda | TCUPOMFISCAL | DATAEMISSAO |  |
| **DocumentCode** | Numero do Documento | TCUPOMFISCAL | NUMERO | Consistir tamanho do campo: RM: inteiro tamanho 4  PROTHEUS: string tamanho 9 |
| **SerieCode** | Serie do Documento | TPONTOVENDA | SERIE |  |
| **GrossPrice** | Valor Bruto da Venda | TCUPOMFISCAL | VALORRECEBIDO |  |
| CommodityPrice | Valor Total da Mercadoria |  |  |  |
| DiscountPercent | Percentual de Desconto da Venda |  |  |  |
| OperatorCode | Código do Operador |  |  |  |
| CurrencyRate | Taxa da Moeda |  |  |  |
| Change | Valor do Troco na Venda |  |  |  |
| StationCode | Código da Estação |  |  |  |
| DiscountPaymentTerm | Desconto Financeiro na Venda |  |  |  |
| CreditValue | Valor de Crédito da Venda |  |  |  |
| Md5 | Código Md5 NewHotel |  |  |  |
| ElectronicInvoiceComplement | Informações Complementares NFCe |  |  |  |
| **PersonalIdentification** | CPF/CGC do Cliente | TCUPOMFISCAL | CNPJCPFADQUIRENTE |  |
| **PurchaserName** | Nome do Adquirente | TCUPOMFISCAL | NOMEADQUIRENTE |  |
| **IsCanceled** | Informa se venda esta cancelada | TCUPOMFISCAL | CANCELADO |  |
| **ListOfSaleItem\ListOfSaleItemType** | Lista de Itens da Venda | | | Ver ListOfSaleItemType |
| ListOfTaxesType | Lista de Impostos da Venda | | | Não há necessidade de integrar valores de tributação pois será recalculado no RM. |
| **StationSalePointCode** | Código Ponto de Venda | TPONTOVENDA | PONTOVENDA |  |
| **StationSalePointInternalId** | InternalId do Ponto de Venda | TPONTOVENDA | CODCOLIGADA|PONTOVENDA |  |
| **SerialNumberSATEquipament** | Número de Série do equipamento SAT | TMOVFISCAL | NROSAT |  |
| **SaleType** | Tipo de venda | TCUPOMFISCAL | TIPO | Campo interno no DataServer para definir tipo do Cupom Fiscal. Possui os seguintes valores:   * V - Cupom Fiscal de Venda * S - SAT |
| **KeyAcessNFe** | Chave de acesso NFe | TMOV | CHAVEACESSONFE | Este campo será exibido no Movimento quando Código Tipo de Documento for CUPOM FISCAL ELETRÔNICO – SAT (CF-E-SAT) - Modelo 59 ou Nota Fiscal Eletrônica ao Consumidor Final - Modelo 65. |
| **ListOfSaleItemType** | Lista de Itens da Venda | | | |
| **SaleItem\SaleItemType** | Itens |  |  |  |
| **InternalId** | InternalId do Item da Venda | TCUPOMFISCALITM | CODCOLIGADA | IDCUPOM | NUMEROITEM |  |
| **ItemInternalId** | InternalId do Produto | TCUPOMFISCALITM | CODCOLIGADA|IDPRD |  |
| **ItemCode** | Código do Produto | TPRODUTO | CODIGOPRD | No RM campo tem tamanho 30 e na mensagem está definido com tamanho 15 |
| **ItemOrder** | Ordem do Item | TCUPOMFISCALITM | NUMEROITEM | No RM este campo é inteiro de tamanho 4. |
| **Quantity** | Quantidade do Item | TCUPOMFISCALITM | QUANTIDADE |  |
| **UnitPrice** | Preço Unitário do Item | TCUPOMFISCALITM | PRECOUNITARIO |  |
| **ItemPrice** | Valor do Item | TCUPOMFISCALITM | VALORLIQUIDO |  |
| DiscountPercentage | Percentual de Desconto do Item |  |  | Não utilizado no RM. |
| **DiscountAmount** | Valor do Desconto do Item | TCUPOMFISCALITM | DESCONTO |  |
| **OperationCode** | Código Fiscal de Operações e Prestações | DCFOP | CODNAT |  |
| **ListOfTaxes** | Lista de Impostos do Item | | | Ver ListOfTaxesType |
| **Increase** | Valor de Acréscimo do Item | TCUPOMFISCALITM | ACRESCIMO |  |
| Lodging | Produto é Diaria |  |  | Não utilizado no RM. |
| **IsCanceled** | Informa se o item esta cancelado | TCUPOMFISCALITM | CANCELADO |  |
| **WarehouseCode** | Código do Local de Estoque(Armazém) | TPONTOVENDA | CODLOC |  |
| **WarehouseInternalId** | Id de integração do Local de Estoque(Armazém) | TPONTOVENDA | CODCOLIGADA|CODFILIAL|CODLOC |  |
| **ECFTaxingCode** | Código da Tributação ECF | TCUPOMFISCALITM | TRIBUTACAOECF |  |
| ListOfTaxesType | Lista de Impostos da Venda | | | Não há necessidade de integrar valores de tributação pois será recalculado no RM. |
| **ListOfSaleConditionType \ SaleCondition** | Condições de Pagamento da Venda | | | ver SaleConditionType |
| **SaleConditionType** | | | | |
| AccountReceivableDocumentInternalId | InternalId do RA do cliente |  |  |  |
| **DateOfPayment** | Data de Vencimento da Parcela | TCUPOMFISCALFIN | DATAVENCIMENTO |  |
| **PaymentValue** | Valor do Pagamento | TCUPOMFISCALFIN | VALOR |  |
| **PaymentMethodCode** | Forma de Pagamento | TFORMAPAGTO | CODFORMAPAGTO | No RM o campo possui tamanho 10 e no xsd está definido como 15. |
| **PaymentMethodInternalId** | Chave de Integração de Forma de Pagamento | TCUPOMFISCALFIN | CODCOLIGADA|IDFORMAPAGTO |  |
| FinancialManagerCode | Código da Administradora Financeira |  |  | Não utilizado no RM. |
| **CardNumber** | Numeração do Cheque | TCUPOMFISCALFIN | CHEQUE | No RM o campo possui tamanho 20 caracteres. Criar consistência para quando receber valor maior que 20, uma vez que no XSD da mensagem está definido tamanho 30 caracteres. |
| SerieCheck | Série do Cheque |  |  | Não utilizado no RM |
| **BankCheck** | Banco do Cheque | TCUPOMFISCALFIN | BANCO |  |
| **AgencyCheck** | Agência Bancária do Cheque | TCUPOMFISCALFIN | AGENCIA | No RM campo possui tamanho de 20 caracteres e no XSD está definido tamanho 8 caracteres. Não teremos problemas no Recebimento, mas se for enviar esta mensagem talvez seja necessário alterar o tamanho do campo. |
| **AccountCheck** | Número da Conta do Cheque | TCUPOMFISCALFIN | CC |  |
| DocumentOfIdentification | Documento de Identidade do Cliente - Cheque |  |  | Não utilizado no RM |
| **PhoneNumber** | Telefone do Cliente - Cheque | TCUPOMFISCALFIN | TELEMITENTE |  |
| EftDate | Data do Pagamento - TEF |  |  |  |
| EftDocument | Documento de Identificação TEF |  |  |  |
| EftAutorization | Código de Autorização TEF |  |  |  |
| EftCancellationDate | Data de Cancelamento TEF |  |  |  |
| EftCancellationDocument | Número do Cancelamento TEF |  |  |  |
| EftInstitute | Código do Instituto TEF |  |  |  |
| UniqueSerialNumber | Código NSU - TEF |  |  |  |
| EftParcel | Parcelamento TEF |  |  |  |

* Somente os campos marcados em negrito são tratados no Adapter.
2Versão 2.007

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **Descrição** | **RM** | | |
| **Tabela** | **Campo** | **Observação** |
| **CompanyId** | Código da empresa. | TCUPOMFISCAL | CODCOLIGADA | Código da Coligada é obtido a partir do De-Para de Filial. |
| **BranchId** | Código da filial |  |  |
| **CompanyInternalId** | InternalId da chave completa de empresa do produto |  |  |
| **InternalId** | InternalId de Integração | TCUPOMFISCAL | CODCOLIGADA|PONTOVENDA|CRO|NUMERO |  |
| **SellerInternalId** | InternalId do Vendedor | TPONTOVENDA | CODVEN1 | Buscar o código do vendedor no cadastro de Estação PDV |
| ComissionPercent | Percentual da Comissão |  |  |  |
| **CustomerVendorInternalId** | InternalId do Código do Cliente | TCUPOMFISCAL | CODCOLCFO|CODCFO |  |
| TotalPrice | Valor Total da Venda |  |  |  |
| **DiscountValue** | Valor Total de Desconto | TCUPOMFISCAL | DESCONTO |  |
| **IncreaseValue** | Valor de Acréscimo | TCUPOMFISCAL | ACRESCIMO |  |
| **NetPrice** | Valor Líquido da Venda | TCUPOMFISCAL | VALORLIQUIDO e VALORRECEBIDO |  |
| CashValue | Valor Pago em Dinheiro |  |  |  |
| ChecksValue | Valor Pago em Cheques |  |  |  |
| CardsValue | Valor Pago em Cartões de Crédito |  |  |  |
| DebitValue | Valor Pago em Cartões de Débito |  |  |  |
| CovenantValue | Valor Pago com Convênio |  |  |  |
| VouchersValue | Valor Pago com Vales |  |  |  |
| FinancedValue | Valor Pago com Financiamento |  |  |  |
| OthersValue | Valor Pago com Outras Formas |  |  |  |
| InputValue | Valor de Entrada |  |  |  |
| **IssueDateDocument** | Data de Emissão da Venda | TCUPOMFISCAL | DATAEMISSAO |  |
| **DocumentCode** | Numero do Documento | TCUPOMFISCAL | NUMERO | Consistir tamanho do campo: RM: inteiro tamanho 4  PROTHEUS: string tamanho 9 |
| **SerieCode** | Serie do Documento | TPONTOVENDA | SERIE |  |
| **GrossPrice** | Valor Bruto da Venda | TCUPOMFISCAL | VALORRECEBIDO |  |
| CommodityPrice | Valor Total da Mercadoria |  |  |  |
| DiscountPercent | Percentual de Desconto da Venda |  |  |  |
| OperatorCode | Código do Operador |  |  |  |
| CurrencyRate | Taxa da Moeda |  |  |  |
| Change | Valor do Troco na Venda |  |  |  |
| StationCode | Código da Estação |  |  |  |
| DiscountPaymentTerm | Desconto Financeiro na Venda |  |  |  |
| CreditValue | Valor de Crédito da Venda |  |  |  |
| **KindOfDocument** | Tipo do Documento | TCUPOMFISCAL | TIPO | Campo interno no DataServer para definir tipo do Cupom Fiscal. Possui os seguintes valores:   * CF - Cupom Fiscal de Venda * SATCE - SAT * NFCE - NFC-e |
| Md5 | Código Md5 NewHotel |  |  |  |
| ElectronicInvoiceComplement | Informações Complementares NFCe |  |  |  |
| **PersonalIdentification** | CPF/CGC do Cliente | TCUPOMFISCAL | CNPJCPFADQUIRENTE |  |
| **PurchaserName** | Nome do Adquirente | TCUPOMFISCAL | NOMEADQUIRENTE |  |
| **IsCanceled** | Informa se venda esta cancelada | TCUPOMFISCAL | CANCELADO |  |
| **ListOfSaleItem\ListOfSaleItemType** | Lista de Itens da Venda | | | Ver ListOfSaleItemType |
| ListOfTaxesType | Lista de Impostos da Venda | | | Não há necessidade de integrar valores de tributação pois será recalculado no RM. |
| **StationSalePointCode** | Código Ponto de Venda | TPONTOVENDA | PONTOVENDA |  |
| **StationSalePointInternalId** | InternalId do Ponto de Venda | TPONTOVENDA | CODCOLIGADA|PONTOVENDA |  |
| **SerialNumberSATEquipament** | Número de Série do equipamento SAT | TMOVFISCAL | NROSAT |  |
| **SaleType** | Tipo de venda | TCUPOMFISCAL | TIPO | Campo interno no DataServer para definir tipo do Cupom Fiscal. Possui os seguintes valores:   * V - Cupom Fiscal de Venda * S - SAT |
| **KeyAcessNFe** | Chave de acesso NFe | TMOV | CHAVEACESSONFE | Este campo será exibido no Movimento quando Código Tipo de Documento for CUPOM FISCAL ELETRÔNICO – SAT (CF-E-SAT) - Modelo 59 ou Nota Fiscal Eletrônica ao Consumidor Final - Modelo 65. |
| **ListOfSaleItemType** | Lista de Itens da Venda | | | |
| **SaleItem\SaleItemType** | Itens |  |  |  |
| **InternalId** | InternalId do Item da Venda | TCUPOMFISCALITM | CODCOLIGADA | IDCUPOM | NUMEROITEM |  |
| **ItemInternalId** | InternalId do Produto | TCUPOMFISCALITM | CODCOLIGADA|IDPRD |  |
| **ItemCode** | Código do Produto | TPRODUTO | CODIGOPRD | No RM campo tem tamanho 30 e na mensagem está definido com tamanho 15 |
| **ItemOrder** | Ordem do Item | TCUPOMFISCALITM | NUMEROITEM | No RM este campo é inteiro de tamanho 4. |
| **Quantity** | Quantidade do Item | TCUPOMFISCALITM | QUANTIDADE |  |
| **ItemTablePrice** | Preço Unitário do Item | TCUPOMFISCALITM | PRECOUNITARIO |  |
| **ItemPrice** | Valor do Item | TCUPOMFISCALITM | VALORLIQUIDO |  |
| DiscountPercentage | Percentual de Desconto do Item |  |  | Não utilizado no RM. |
| **DiscountAmount** | Valor do Desconto do Item | TCUPOMFISCALITM | DESCONTO |  |
| **OperationCode** | Código Fiscal de Operações e Prestações | DCFOP | CODNAT |  |
| **ListOfTaxes** | Lista de Impostos do Item | | | Ver ListOfTaxesType |
| **Increase** | Valor de Acréscimo do Item | TCUPOMFISCALITM | ACRESCIMO |  |
| Lodging | Produto é Diaria |  |  | Não utilizado no RM. |
| **IsCanceled** | Informa se o item esta cancelado | TCUPOMFISCALITM | CANCELADO |  |
| **WarehouseCode** | Código do Local de Estoque(Armazém) | TPONTOVENDA | CODLOC |  |
| **WarehouseInternalId** | Id de integração do Local de Estoque(Armazém) | TPONTOVENDA | CODCOLIGADA|CODFILIAL|CODLOC |  |
| **ECFTaxingCode** | Código da Tributação ECF | TCUPOMFISCALITM | TRIBUTACAOECF |  |
| ListOfTaxesType | Lista de Impostos da Venda | | | Não há necessidade de integrar valores de tributação pois será recalculado no RM. |
| **ListOfSaleConditionType \ SaleCondition** | Condições de Pagamento da Venda | | | ver SaleConditionType |
| **SaleConditionType** | | | | |
| AccountReceivableDocumentInternalId | InternalId do RA do cliente |  |  |  |
| **DateOfPayment** | Data de Vencimento da Parcela | TCUPOMFISCALFIN | DATAVENCIMENTO |  |
| **PaymentValue** | Valor do Pagamento | TCUPOMFISCALFIN | VALOR |  |
| **PaymentMethodCode** | Forma de Pagamento | TFORMAPAGTO | CODFORMAPAGTO | No RM o campo possui tamanho 10 e no xsd está definido como 15. |
| **PaymentMethodInternalId** | Chave de Integração de Forma de Pagamento | TCUPOMFISCALFIN | CODCOLIGADA|IDFORMAPAGTO |  |
| FinancialManagerCode | Código da Administradora Financeira |  |  | Não utilizado no RM. |
| **CardNumber** | Numeração do Cheque | TCUPOMFISCALFIN | CHEQUE | No RM o campo possui tamanho 20 caracteres. Criar consistência para quando receber valor maior que 20, uma vez que no XSD da mensagem está definido tamanho 30 caracteres. |
| SerieCheck | Série do Cheque |  |  | Não utilizado no RM |
| **BankCheck** | Banco do Cheque | TCUPOMFISCALFIN | BANCO |  |
| **AgencyCheck** | Agência Bancária do Cheque | TCUPOMFISCALFIN | AGENCIA | No RM campo possui tamanho de 20 caracteres e no XSD está definido tamanho 8 caracteres. Não teremos problemas no Recebimento, mas se for enviar esta mensagem talvez seja necessário alterar o tamanho do campo. |
| **AccountCheck** | Número da Conta do Cheque | TCUPOMFISCALFIN | CC |  |
| DocumentOfIdentification | Documento de Identidade do Cliente - Cheque |  |  | Não utilizado no RM |
| **PhoneNumber** | Telefone do Cliente - Cheque | TCUPOMFISCALFIN | TELEMITENTE |  |
| EftDate | Data do Pagamento - TEF |  |  |  |
| EftDocument | Documento de Identificação TEF |  |  |  |
| EftAutorization | Código de Autorização TEF |  |  |  |
| EftCancellationDate | Data de Cancelamento TEF |  |  |  |
| EftCancellationDocument | Número do Cancelamento TEF |  |  |  |
| EftInstitute | Código do Instituto TEF |  |  |  |
| UniqueSerialNumber | Código NSU - TEF |  |  |  |
| EftParcel | Parcelamento TEF |  |  |  |

* Somente os campos marcados em negrito são tratados no Adapter.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
