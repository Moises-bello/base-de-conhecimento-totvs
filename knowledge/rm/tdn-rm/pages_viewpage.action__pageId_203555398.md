---
content_hash: 75414d7e4403c4c99425be9a88760fb70b044a8428963444b7c02b5f2f5acaff
fetched_at: '2026-06-29T00:06:08.960013+00:00'
page_id: '203555398'
product: rm
source: tdn-rm
title: ER_PCREQ-7797_Integração_Produto - Item
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203555398
version: 25
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Estoque |
| **Segmento Executor** | TOTVS Construção e Projetos | | |
| **Projeto1** | Integração BackOffice RM x PDV Protheus | **IRM1** | PCREQ-7769 |
| **Requisito1** | PCREQ-7797 | **Subtarefa1** | PDR\_CP\_MOV008-10 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

 Implementação do adapter de integração via Mensagem Única TOTVS do cadastro de Produto com o PDV, viabilizando assim o CRUD completo do cadastro por envio de mensagem de integração.

## Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de envio de Mensagens Únicas TOTVS para integração do cadastro de Produto (Item), estando o adapter de recebimento desta mesma mensagem fora do escopo do requisito.

 

A análise e o desenvolvimento do adapter será efetuado considerando a integração com o PDV Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Produto | Inclusão/Alteração/Exclusão | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Estoque, Compras e Faturamento \ Produto | - |

As inclusões, alterações e exclusões de Produto/Serviço são feitos através da Linha RM, que identifica o evento em sua entidade e envia uma mensagem ao PDV Protheus. Os dados de produto que serão sincronizados pela mensagem única são :

* **Pasta Identificação:** Código do Produto, Data Cadastramento, Inativo, Nome fantasia, Tipo
* **Pasta Detalhes / Descrição:**Descrição
* **Pasta Detalhes /****Características:**Peso Bruto, Peso Líquido
* **Pasta Detalhe / Outros Dados:**Referência, Tributação Cupom Fiscal, Número  da Nomenclatura Comum do Mercosul (NCM).
* **Pasta Preço:** Serão enviados os dados do campo **Preços Selecionados:** Moeda, Data-Base, e Preço.
* **Pasta Controle de Estoque:**Controlado por lote, Unidade de Controle, Usa número de série
* **Pasta Custos:**Custo Médio / Valor, Custo unitário / Valor
* **Pasta Informações por Filial / Editar o registro da respectiva Filial:**Consignado
* **Anexos / Informações do Estoque:**Lote Econômico de Compras

Para integrar o cadastro de Produto os seguinte itens abaixo devem ser considerados:

* A configuração de compartilhamento do cadastro de Produto (Item) por Empresas e Filiais deve ser: **Exclusivo por Empresa** e **Compartilhado por Filial**.
* Serão enviados para o PROTHEUS somente os Produtos/Serviços de Último Nível.
* Produtos globais no BackOffice RM não serão considerados globais no sistema de destino, sendo enviada uma mensagem de inclusão para cada empresa a qual o produto faz parte.  
  + Caso haja ao menos uma mensagem enviada com sucesso ao PDV (SigaLoja), mesmo havendo erro nas mensagens referentes ao produto para as outras coligadas, não será apresentada mensagem de erro e a alteração/inclusão não será desfeita.
* O campo B1\_CODITE no cadastro de Produtos do PROTHEUS deve ser alterado, via apsdu, para não obrigatório e também deve-se retirar sua validação.
* O campo “Código do Produto” no PROTHEUS deve ser alterado para tamanho 30 caracteres para manter compatibilidade com o RM.

**Envio de Preços**

O RM enviará na mensagem os preços de 1 a 5  do Produto, ficando a cargo do SigaLoja a utilização destes ou de demais formas de precificação disponíveis no mesmo. Não haverá integração da Tabela de Preços da linha RM  ou da precificação no Protheus. O RM considerará como valor de venda o retornado na mensagem de Cupom Fiscal.

**Tributação ECF**

Esta informação será enviada na mensagem quando for informado a Tributação de Cupom Fiscal no cadastro de Produto. Com base no código de tributação informado no produto, o RM irá buscar as informações de Código do Tributo, Tipo de Tributação e Alíquota cadastrados na tabela Tributação ECF (TTRIBUTACAOECF) e enviar estas informações ao Protheus.

Visto que os códigos dos tributos no Protheus obrigatoriamente seguem um padrão de nomenclatura, deve-se efetuar o cadastro destes tributos no RM respeitando o mesmo código utilizado no Protheus para viabilizar a integração de registros que utilizem estes tributos.  Os códigos dos tributos devem seguir a seguinte nomenclatura:

* **Tributado ICMS**: Sempre inicia com T + alíquota do produto + 00. Exemplo: 7% = T0700, 12% = T1200, 18% = T1800.
* **Tributado ISS:** Sempre inicia com S + alíquota do produto + 00. Exemplo: 5% = S0500, 10% = S1000.
* **Não Tributado:** código fixo N1.
* **Isento:** código fixo I1.
* **Substituição Tributária:** código fixo F1.

****Nomenclatura Comum do Mercosul (**NCM)**

Quando o campo Número da Nomenclatura Comum do Mercosul (NCM) estiver preenchido ele será enviado ao Protheus na tag **FiscalClassificationCode**. Esta informação é cadastrada na pasta Outros Dados em Produto \ Detalhes \ Outros Dados. É necessário definir para este campo a Máscara nos parâmetros de Integração Fiscal.

**Fórmula Visual**

Para sincronizar o cadastro será necessário importar a fórmula visual que encontra-se disponível na pasta “Sugeridos”, interna à pasta “\_ImpExp” no ambiente instalado do sistema (“../CorporeRM/\_ImpExp/Sugeridos”). Ao importar a fórmula visual deverá ser marcado para cada fórmula o parâmetro “Importar Gatilho” na rotina de Importação de Fórmula Visual.

Caso o cliente deseje integrar somente os produtos disponíveis para venda no PDV (que possuam Tributação ECF cadastrada) o mesmo deve somente alterar as fórmulas visuais adicionando a condicional de que o campo "TRIBUTACAOECF" seja diferente de vazio ou nulo. Exemplo de expressão condicional: !string.IsNullOrEmpty(this.Fields["TRIBUTACAOECF"].AsString) .

Visando facilitar a sincronização das bases de dados RM e PDV foi desenvolvida uma atividade de fórmula visual que se responsabiliza por, a partir de alguns parâmetros, obter os dados necessários e solicitar o envio da Mensagem Única TOTVS Item\_3.004.

Basicamente é necessário informar a esta atividade somente a lista de chaves dos registros que se deseja integrar, qual a Mensagem Única a enviar e qual o objeto de negócio (DataServer) responsável por retornar as informações do registro. A partir destas informações a atividade se responsabiliza pela leitura, transformação e envio dos dados ao sistema de destino, oferecendo como retorno o Log de integração.

Todas as mensagens trafegadas também constarão no monitor da fila de integração, para posterior conferência.

**Listagem de Fórmula Visual:**

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Rotina** | **Operação** | **Fórmula Visual** |
| **Cadastro** | ``` Produto ``` | ``` Inclusão / Alteração / Exclusão ``` | ``` 02_PDV_Produto.TotvsWF ``` |
| ``` Produto ``` | ``` Carga inicial ``` | 02.Sincronização de Produto.TotvsWF |

**Tabelas Utilizadas**

* TPRODUTO - Produtos Globais.
* TPRODUTODEF - Dados dos Produtos Globais por Coligada
* TPRDLOCINFO - Informações do Estoque
* TPRDFIL - Filiais de Um Produto
* TPRDCODIGO - Código Genérico de Produtos
* TUND - Unidades de Medida
* TTRIBUTACAOECF - Tributação ECF

**Entidades de Integração**

* DataServer envolvido
  + EstPrdDataBR
* Transformação
  + Id: Item
  + Versão: 3.004
* Fluxo da mensagem
  + Saída
* Tipo de Envio:
  + Síncrono.
* Extension: 27490bfc-3d18-4e49-9eeb-b94e483baf01

## Fluxo do Processo

**Diagrama de Atividades**

Fluxo de trabalho da atividade de fórmula visual '**MovProdutoIntegradoProtheus**' utilizada no sincronismo:

## Mapeamento dos Campos

* **Mensagem Item 3.004**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **Descrição** | **RM** | | |
| **Tabela** | **Campo** | **Observação** |
| **CompanyId** | Código da coligada | TPRODUTO | CODCOLIGADA | Código da Coligada é obtido a partir do De-Para de Filial. |
| **BranchId** | Código da filial | - | - |
| **CompanyInternalId** | InternalId da filial |  |  |
| **Code** | Código do Item | TPRODUTO | CODIGOPRD | Valor texto tamanho 30 |
| **InternalId** | Chave primária do registro | TPRODUTO | CODCOLIGADA|IDPRD |  |
| **Name** | Nome do Produto | TPRODUTO | DESCRICAO |  |
| **ShorName** | Nome curto | TPRODUTO | NOMEFANTASIA |  |
| Detail | Detalhes do item |  |  | Não utilizado nesta integração. |
| **Active** | Item Ativo? | TPRODUTO | INATIVO | Quando TPRODUTO.INATIVO igual a 0 (zero) envia na tag o valor 1 - Ativo.  Quando TPRODUTO.INATIVO igual a 1 (um) envia na tag o valor 0 - Inativo. |
| StockGroupCode | Código Grupo Estoque |  |  | Não utilizado nesta integração. |
| StockGroupInternalId | InternalId da chave completa de Grupo de Estoque do produto |  |  | Não utilizado nesta integração. |
| StockGroupDescription | Descrição Grupo Estoque |  |  | Não utilizado nesta integração. |
| **UnitOfMeasureCode** | Código Unidade Medida | TPRODUTODEF | CODUNDCONTROLE | Valor texto tamanho 6 |
| **UnitOfMeasureInternalId** | InternalId da chave completa de Unidade Medida do produto | TPRODUTODEF | CODUNDCONTROLE |  |
| ObtainingType | Forma de Obtenção |  |  | Não utilizado pela linha RM |
| ComercialFamilyCode | Código Família Comercial |  |  | Não utilizado pela linha RM |
| ComercialFamilyInternalId | InternalId da chave completa de Família Comercial do produto |  |  | Não utilizado pela linha RM |
| ComercialFamilyDescription | Descrição Família Comercial |  |  | Não utilizado pela linha RM |
| **DeployDate** | Data Implantação | TPRODUTO | DTCADASTRAMENTO |  |
| ReleaseDate | Data Liberação |  |  | Não utilizado pela linha RM |
| StandardWarehouseCode | Código Depósito Padrão |  |  | Não utilizado pela linha RM |
| StandardWarehouseInternalId | InternalId da chave completa de Depósito Padrão do produto |  |  | Não utilizado pela linha RM |
| StandardWarehouseDescription | Descrição Depósito Padrão |  |  | Não utilizado pela linha RM |
| MultipleLot | Lote Múltiplo |  |  | Não utilizado pela linha RM |
| EconomicLot | Lote Econômico |  |  | Não utilizado pela linha RM |
| MinimumLot | Lote Mínimo |  |  | Não utilizado pela linha RM |
| QualityControl | Controla Qualidade |  |  | Não utilizado pela linha RM |
| **ControlType** | Tipo Controle | TPRDFIL | CONSIGNADO | Será considerada somente a informação da primeira filial, uma vez que ao incluir um produto são criados registros para todas as filiais ativas. São utilizados os campos em negrito.   Fixo 1 – Físico  Fixo 2 – Total  **Fixo 3 – Consignado**  Fixo 4 – Débito Direto  **Fixo 5 – Não Definido** |
| **Trail** | Se controla estoque por Lote | TPRODUTO | CONTROLADOPORLOTE | O valor do campo segue a lógica abaixo:  Marcado = Valor 'L' (Controlado por Lote)  Desmarcado = Valor 'N' (Não utiliza rastro) |
| **BinControl** | Se controla estoque por Nº de Série | TPRODUTO | USANUMSERIE | O valor do campo segue a lógica abaixo:  Marcado = Valor 'true' (Controla Nº de Série)  Desmarcado = Valor 'false' (Não controla Nº de Série) |
| FractionalQuantity | Quantidade Fracionada |  |  | Não utilizado pela linha RM |
| **NetWeight** | Peso Líquido | TPRODUTO | PESOLIQUIDO |  |
| **GrossWeight** | Peso Bruto | TPRODUTO | PESOBRUTO |  |
| FamilyCode | Código Família |  |  | Não utilizado pela linha RM |
| FamilyInternalId | InternalId da chave completa de Família do produto |  |  | Não utilizado pela linha RM |
| FamilyDescription | Descrição Família |  |  | Não utilizado pela linha RM |
| FamilyClassificationCode | Classificaçãio da Família de Materiais |  |  | Não utilizado pela linha RM |
| FormulaType | Tipo Fórmula |  |  | Não utilizado pela linha RM |
| PerMillion | Valor Per PPM |  |  | Não utilizado pela linha RM |
| IsScrapStockControl | Controla Estoque Refugo |  |  | Não utilizado pela linha RM |
| IsScrapFiscalPrice | Refugo ao Preço Fiscal |  |  | Não utilizado pela linha RM |
| ScrapItemCode | Código Item Refugo |  |  | Não utilizado pela linha RM |
| ScrapItemInternalId | InternalId da chave completa de Item Refugo do produto |  |  | Não utilizado pela linha RM |
| ScrapItemQuantity | Quantidade Item Refugo |  |  | Não utilizado pela linha RM |
| **Origin** | Origem da mercadoria | TPRODUTO | REFERENCIACP | Fixo 0 – Nacional  Fixo 1 - Estrangeira - Importação direta  Fixo 2 - Estrangeira - Adquirida no mercado externo |
| FiscalInformation |  |  |  | Ver FiscalInformationType |
| ListOfCustomerItemInformation |  |  |  | Ver CustomerItemInformation \ CustomerItemInformationType |
| CostCenterCode | Código do Centro de Custo |  |  | Não utilizado pela linha RM |
| CostCenterInternalId | InternalId do CostCenterCode |  |  | Não utilizado pela linha RM |
| GroupCode |  |  |  | Não utilizado pela linha RM |
| GroupInternalId | InternalId do GroupCode |  |  | Não utilizado pela linha RM |
| GroupName |  |  |  | Não utilizado pela linha RM |
| SecondUnitOfMeasureCode | Segunda Unidade de Medida Utilizada para converter a quantidade para uma segunda unidade | TPRODUTODEF | CODUNDCOMPRA |  |
| SecondUnitOfMeasureInternalId | InternalId do SecondUnitOfMeasureCode | TPRODUTODEF | CODUNDCOMPRA |  |
| MultiplicationFactorValue | Fator multiplicador da conversão para a segunda unidade de medida |  |  | Não utilizado pela linha RM |
| Values |  |  |  | Ver Values \ ValuesType |
| **ProductType** | Tipo de produto | TPRODUTO | TIPO | Fixo 01 – Ativo Imobilizado  Fixo 02 – Beneficiamento  Fixo 03 – Embalagem  Fixo 04 – Gastos Gerais  Fixo 05 – Material de Consumo  **Fixo 06 – Mercadoria:** enviado quando Tipo Produto = Produto  **Fixo 07 – Mão-De-Obra:** enviado quando Tipo Produto = Serviço  Fixo 08 – Matéria-Prima  Fixo 09 – Outros Insumos  Fixo 10 – Produto Acabado  Fixo 11 – Produto Intermediario  Fixo 12 – Produto em Processo  Fixo 13 – Produto Veiculo  Fixo 14 – Selo de Controle  Fixo 15 – SubProduto |
| Trail | Rastro por lote ou Sublote, sem rastro |  |  | Não utilizado nesta integração. |
| GovernmentCode | Código Item |  |  | Não utilizado nesta integração. |
| BinControl | Campo que identifica se o produto possui localização(Endereço/Numero de Serie) |  |  |  |
| ItemTypeCode | Código do Tipo de Produto | TPRODUTO | CODTB1FAT | Não utilizado nesta integração. |
| ItemTypeInternalId | InternalId da chave completa do Tipo de Produto | TPRODUTO | CODCOLIGADA|CODTB1FAT | Não utilizado nesta integração. |
| **ListOfGenericPrices** | Lista de Preços do Produto |  |  | Ver ListOfGenericPricesType |
| **ListOfBarCode** | Lista de Códigos de Barra |  |  | Ver ListOfBarCodeType |
| FiscalInformationType | Informações fiscais do Item |  |  | Ver FiscalInformation **\**FiscalClassificationType |
| CustomerItemInformationType | Amarração Cliente X Item |  |  | Ver ListOfCustomerItemInformation \ CustomerItemInformation |
| ****FiscalInformation \** FiscalClassificationType** | | | | Este campos não estão sendo enviados pelo RM pelos seguintes motivos:   * + BranchId - Filial: na inclusão de um novo Produto no RM é gerado na tabela TPRDFIL um registro para cada Filial ativa. Desta forma seria necessário a utilização de uma outra mensagem.   + FiscalInformation: no RM temos Dados Fiscais do Produto e Dados Fiscais por UF. Nestes dois cadastros não temos o campo Descrição. |
| FiscalClassificationCode | Código Classificação Fiscal | TPRODUTO | NCM |  |
| FiscalClassificationInternalId | InternalId do FiscalClassificationCode |  |  | Não enviado pelo RM |
| FiscalClassificationDescription | Descrição Classificação Fiscal |  |  | Não enviado pelo RM |
| **ListOfCustomerItemInformation \ CustomerItemInformation** | | | | Não utilizados nesta integração |
| CustomerCode | Código do cliente |  |  | Não utilizados nesta integração |
| CustomerInternalId | InternalId do CustomerCode |  |  | Não utilizados nesta integração |
| CustomerItemCode | Código do Item X Cliente |  |  | Não utilizados nesta integração |
| CustomerItemInternalId | InternalId do CustomerItemCode |  |  | Não utilizados nesta integração |
| **Values \ ValuesType** | | | | |
| **CostPrice** | Preço de Custo | TPRODUTODEF | PRECO1 | Os demais campos de Preço do produto são enviados na tag **ListOfGenericPrices** |
| **SalesPrice** | Preço de Venda | TPRODUTODEF | PRECO2 | Os demais campos de Preço do produto são enviados na tag **ListOfGenericPrices** |
| **AverageCostPrice** | Preço Médio de Custo | TPRODUTODEF | CUSTOMEDIO |  |
| **StandardCostPrice** | Preço Padrão | TPRODUTODEF | CUSTOUNITARIO |  |
| **BaseDate** | Data Base do Calculo dos preços | TPRODUTODEF | DATABASEPRECO1 | Os demais campos de Data-Base do Preço do produto são enviados na tag **ListOfGenericPrices** |
| PackingQuantity | Quantidade na Embalagem |  |  | Não utilizados nesta integração |
| AccountantAccountCode | Código da Conta Contábil |  |  | Não utilizados nesta integração |
| AllowsPurchase | Permite Comprar do Item |  |  | Não utilizados nesta integração |
| IsStorable | Item é Estocável (true) ou Aplicação direta (false) ? |  |  | Não utilizados nesta integração |
| LastUpdateItem | Data Última atualização do Item |  |  | Não utilizados nesta integração |
| LastPurchaseItem | Data Última Compra do Item |  |  | Não utilizados nesta integração |
| **GenericPrices \ GenericPricesType** | Preços |  |  |  |
| **PriceId** | Identificador do preço |  |  | No RM pode ser de 1 a 5 |
| **CurrencyInternalId** | Código da Moeda no Preço | TPRODUTODEF | CODMOEPRECO1 CODMOEPRECO2 CODMOEPRECO3 CODMOEPRECO4 CODMOEPRECO5 |  |
| **BaseDatePrice** | Data-base de Preço | TPRODUTODEF | DATABASEPRECO1 DATABASEPRECO2 DATABASEPRECO3 DATABASEPRECO4 DATABASEPRECO5 |  |
| **Price** | Preço | TPRODUTODEF | PRECO1 PRECO2 PRECO3 PRECO4 PRECO5 |  |
| **BarCode \** **BarCodeType** | Códigos de Barra |  |  |  |
| **Code** | Código de Barras do Produto | TPRDCODIGO | CODIGO |  |
| **InternalId** | InternalId do Código de Barras | TPRDCODIGO | CODCOLIGADA|TIPO|CODIGO |  |
| **UnifOfMeasureInternalId** | Unidade do Código do Produto | TPRDCODIGO | CODUND |  |
| **ItemQuantity** | Quantidade do Produto | TUND | FATORCONVERSAO | Tratado via extension. Busca-se o fator de conversão da unidade informada para o Códigos de barra. |
| **ECFTaxing** | Tributação de Cupom Fiscal |  |  |  |
| **Code** | Código da Tributação ECF | TPRODUTO | TRIBUTACAOECF |  |
| **Type** | Tipo da Tributação ECF | TTRIBUTACAOECF | TIPO | Informação buscada via extension quando existir Tributação Cupom Fiscal informada para o Produto, respeitando o seguinte de-para de valores:  Fixo 1 - Tributado: enviado quando Tipo = 0  Fixo 2 - Isento: enviado quando Tipo = 1  Fixo 3 - Substituição Tributaria: enviado quando Tipo = 2  Fixo 4 - Não tributado: enviado quando Tipo = 3  Fixo 5 - Outros. |
| **Aliquot** | Alíquota da Tributação ECF | TTRIBUTACAOECF | ALIQUOTA | Informação buscada via extension quando existir Tributação Cupom Fiscal informada para o Produto. |

* Somente os campos marcados em negrito são tratados no Adapter, sendo os demais não enviados na mensagem.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
