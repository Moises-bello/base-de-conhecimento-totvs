---
content_hash: 57d41011f9ec97f8e6366ccbb608524262b1385d0425129433018e4dd51298c2
fetched_at: '2026-06-29T00:08:39.338164+00:00'
page_id: '286017154'
product: rm
source: tdn-rm
title: 752823 MATESTCNTFTOF01-358 DT Enviar Número no Fabricante do Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286017154
version: 15
---

# ENVIAR NÚMERO NO FABRICANTE DO PRODUTO / INTEGRAÇÕES SIGAMNT

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | Construção e Projetos | | |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastro de Produto/Serviços | EstPrdAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Configurador de Integrações | ConConfiguraIntegracaoAction | | Transformação | ConTransformacaoAction | | | |
| **Chamado/Ticket:** | 752823. | | |
| **Requisito/Story/Issue:** | MATESTCNTFTOF01-358/MATESTCNTFTOF01-513 | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

### Objetivo

 

Implementação do adapter de integração via Mensagem Única TOTVS para enviar a informação de Número no Fabricante do Produto RM para o Manutenção de Ativos (SigaMNT).

Ao integrar o cadastro de Produto com esta informação do número do fabricante, o usuário poderá consultar esta informação ao incluir insumos em uma Ordem de Manutenção (OS) no Manutenção de Ativos (SigaMNT).

### Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de envio de Mensagens Únicas TOTVS para integração de Produto com informação do Número no Fabricante, estando o adapter de recebimento desta mesma mensagem fora do escopo do requisito. 

A análise e o desenvolvimento do adapter será efetuado considerando a integração com o Manutenção de Ativos Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Produto | Alteração | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Produto | - |
| Configurador de Integração | Alteração | RM \ Integração \ Ferramentas \ Configurar | - |

**Regras de Integridade:**

Para a integração desta nova mensagem única de Produto serão realizadas as seguintes ações:

* Criar a mensagem única Item versão 3.007 (xsd) e adicionar o campo “ManufacturerCode”. Este campo deve ser  do tipo string.
* Neste campo será trafegada informação do campo Número no Fabricante do cadastro de Produto do RM (TPRODUTODEF.NUMNOFABRIC).
* Esta informação deverá ser gravada no campo "B1\_FABRIC" da tabela de Produtos do Protheus (SB1).
* Atualizar o Configurador de Integração do RM para contemplar esta nova versão da mensagem Item para a Integração Manutenção de Ativos x BackOffice RM.
* Atualizar o cadastro de Transformação do RM para contemplar esta nova versão da mensagem Item.
* Atualizar a Fórmula Visual de Integração da mensagem Item para considerar a versão 3.007.
* Atualizar a Fórmula Visual de Sincronização de produto para considerar a versão 3.007.

**Configurador de Integrações**

Tendo em vista que um cliente pode utilizar dois projetos de integração ativos com o BackOffice RM, será necessário realizar a seguinte atualização no Configurador de Integrações:

1. Projeto de Integração Manutenção de Ativos x BackOffice RM  
   1. Apaga a mensagem ITEM versão 2.000 caso exista;
   2. Insere a versão 3.007 da mensagem ITEM caso ainda não exista para integração Manutenção de Ativos(SigaMNT) e TOTVS PDV.
2. Projeto de Integração TOTVS PDV x BackOffice RM
   1. Apaga a mensagem ITEM versão 2.000 caso exista para a integração Manutenção de Ativos(SigaMNT).
   2. Apaga a mensagem ITEM versão 3.004 caso exista para a integração TOTVS PDV.
   3. Insere a versão 3.007 da mensagem ITEM caso ainda não exista para integração Manutenção de Ativos(SigaMNT) e TOTVS PDV.

Desta forma, a partir da versão 12.1.18 as integrações com o BackOffice RM do  TOTVS PDV e Manutenção de Ativos passam a utilizar a versão 3.007 da mensagem única ITEM.

**Ponto de atenção:**

* Não será integrado o campo Código do Fabricante do Produto.
* No RM o Número do Fabricante possui tamanho de 100 caracteres. O campo Fabricante no Protheus possue por padrão o tamanho de 20 caracteres. Caso o Número do Fabricante no RM possuir mais do que 20 caracteres, é necessário altera o tamanho do campo B1\_FABRIC no Protheus (via configurador SIGACFG) para ter o mesmo tamanho do RM.
* O envio da mensagem Item\_ 3.007 do RM para o Protheus contemplará todos os campos enviados na mensagem Item\_3.004 mais a informação da tag ManufacturerCode. Os demais campos não serão considerados neste momento.

**Tabelas Utilizadas**

* TPRODUTODEF – Dados dos Produtos Globais por Coligada.
* HCTRANSFORMACAO – Transformação Mensagem Única TOTVS.
* HCMAPAINTEGRACAO – Tabela de mapeamento das entidades para cada Integração.

 

**Entidades de Integração**

* Transformação  
  + Identificador da Mensagem: Item
  + Versão: 3\_007
  + Tipo do Server: DataServer
  + DataServer: EstPrdDataBR
* Source Code(GUID):
* Fluxo da mensagem: Saída
* Tipo de Envio: Síncrono.
* Mandatário: BackOffice RM.

### Procedimento para Configuração

**CONFIGURAÇÃO DE INTEGRAÇÃO**

1. No **RM**, acesse **Integração/Ferramentas/Configurar**.
   1. Na janela **Assistente de Configuração de Integração** avance para a etapa **Configuração do banco de dados** e informe Usuário e Senha para conectar ao banco. Teste a conexão e avance.
   2. Na etapa **Projetos de Integração** selecione o item **Manutenção de Ativos x BackOffice RM**, avance e execute o assistente.
2. No **PROTHEUS**acesse **Configurador (SIGACFG)**, acesse **Ambiente/Schedule/Adapter E.A.I**. Crie o adapter ITEM conforme dados a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Mensagem Única:** | Sim |
| **Rotina:** | MATA010 |
| **Mensagem:** | ITEM |
| **Envia:** | Não |
| **Recebe:** | Sim |
| **Método:** | Síncrono |
| **Operação:** | 1 - Todas |
| **Canal Envio:** | 2 - EAI |
| **Versão Envio:** | 3.007 |

3. **Número do Fabricante** possuir o mesmo tamanho no **RM** e no **PROTHEUS**

* + Acesse **Configurador (SIGACFG)**, acesse **Base de Dados/Dicionário/Base de Dados**.
  + Selecione Dicionários de Dados e pesquise a tabela SB1.
  + Edite a tabela SB1 e pesquise pelo campo B1\_FABRIC
  + Edite o campo B1\_FABRIC e no campo **Tamanho** informe o valor 100.
  + Salve a alteração e atualize a base de dados com a alteração.

## Procedimento para Utilização

1. No  **Gestão de Estoque, Compras e Faturamento** cadastrar um Produto e informar o Número do Fabricante.
2. No  **Manutenção de Ativos** acessar o cadastro de Produto e verificar que a informação foi gravada no campo Fabricante da pasta Outros.

## Mapeamento dos Campos

 

* **Mensagem Item 3.007**

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **Descrição** | **RM** | | |
| **Tabela** | **Campo** | **Observação** |
| **CompanyId** | Código da coligada | TPRODUTO | CODCOLIGADA | Código da Coligada é obtido a partir do De-Para de Filial. |
| **BranchId** | Código da filial | - | - |
| **CompanyInternalId** | InternalId da filial |  |  |
| BranchInternalId | InternalId do Estabelecimento/Filial | - | - | Não utilizado nesta integração. |
| **Code** | Código do Item | TPRODUTO | CODIGOPRD | Valor texto tamanho 30 |
| **InternalId** | Chave primária do registro | TPRODUTO | CODCOLIGADA|IDPRD |  |
| **Name** | Nome do Produto | TPRODUTO | DESCRICAO |  |
| **ShorName** | Nome curto | TPRODUTO | NOMEFANTASIA |  |
| Detail | Detalhes do item |  |  | Não utilizado nesta integração. |
| **Active** | Item Ativo? | TPRODUTO | INATIVO | Quando TPRODUTO.INATIVO igual a 0 (zero) envia na tag o valor 1 - Ativo.  Quando TPRODUTO.INATIVO igual a 1 (um) envia na tag o valor 0 - Inativo. |
| StockGroupCode | Código Grupo Estoque |  |  | Não utilizado nesta integração. |
| StockGroupInternalId | InternalId da chave completa de Grupo de Estoque do produto |  |  | Não utilizado nesta integração. |
| StockGroupDescription | Descrição Grupo Estoque |  |  | Não utilizado nesta integração. |
| **UnitOfMeasureCode** | Código Unidade Medida | TPRODUTODEF | CODUNDCONTROLE | Valor texto tamanho 6 |
| **UnitOfMeasureInternalId** | InternalId da chave completa de Unidade Medida do produto | TPRODUTODEF | CODUNDCONTROLE |  |
| ObtainingType | Forma de Obtenção |  |  | Não utilizado pela linha RM |
| **DeployDate** | Data Implantação | TPRODUTO | DTCADASTRAMENTO |  |
| ReleaseDate | Data Liberação |  |  | Não utilizado pela linha RM |
| StandardWarehouseCode | Código Depósito Padrão |  |  | Não utilizado pela linha RM |
| StandardWarehouseInternalId | InternalId da chave completa de Depósito Padrão do produto |  |  | Não utilizado pela linha RM |
| StandardWarehouseDescription | Descrição Depósito Padrão |  |  | Não utilizado pela linha RM |
| MultipleLot | Lote Múltiplo |  |  | Não utilizado pela linha RM |
| EconomicLot | Lote Econômico |  |  | Não utilizado pela linha RM |
| MinimumLot | Lote Mínimo |  |  | Não utilizado pela linha RM |
| QualityControl | Controla Qualidade |  |  | Não utilizado pela linha RM |
| **ControlType** | Tipo Controle | TPRDFIL | CONSIGNADO | Será considerada somente a informação da primeira filial, uma vez que ao incluir um produto são criados registros para todas as filiais ativas. São utilizados os campos em negrito.  Fixo 1 – Físico  Fixo 2 – Total  **Fixo 3 – Consignado**  Fixo 4 – Débito Direto  **Fixo 5 – Não Definido** |
| **StockControlType** | Tipo Controle Estoque | TPRODUTODEF | USANUMSERIE ou CONTROLADOPORLOTE | São utilizados os campos em negrito.  Fixo 1 – Serial  **Fixo 2 – Número Série (**TPRODUTODEF.USANUMSERIE: Indica se utiliza número de série**)**  **Fixo 3 – Lote (**TPRODUTODEF.CONTROLADOPORLOTE: Controlado por lote.**)**  Fixo 4 – Referência  Fixo 5 – Não Definido |
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
| ListOfComercialFamilyItem | Lista de códigos de famílias(categorias) com produto |  |  | Ver ComercialFamilyItemType |
| GroupCode |  |  |  | Não utilizado pela linha RM |
| GroupInternalId | InternalId do GroupCode |  |  | Não utilizado pela linha RM |
| GroupName |  |  |  | Não utilizado pela linha RM |
| SecondUnitOfMeasureCode | Segunda Unidade de Medida Utilizada para converter a quantidade para uma segunda unidade | TPRODUTODEF | CODUNDCOMPRA |  |
| SecondUnitOfMeasureInternalId | InternalId do SecondUnitOfMeasureCode | TPRODUTODEF | CODUNDCOMPRA |  |
| MultiplicationFactorValue | Fator multiplicador da conversão para a segunda unidade de medida |  |  | Não utilizado pela linha RM |
| Values |  |  |  | Ver Values \ ValuesType |
| **ProductType** | Tipo de produto | TPRODUTO | TIPO | Fixo 01 – Ativo Imobilizado  Fixo 02 – Beneficiamento  Fixo 03 – Embalagem  Fixo 04 – Gastos Gerais  Fixo 05 – Material de Consumo  **Fixo 06 – Mercadoria:** enviado quando Tipo Produto = Produto  **Fixo 07 – Mão-De-Obra:**enviado quando Tipo Produto = Serviço  Fixo 08 – Matéria-Prima  Fixo 09 – Outros Insumos  Fixo 10 – Produto Acabado  Fixo 11 – Produto Intermediario  Fixo 12 – Produto em Processo  Fixo 13 – Produto Veiculo  Fixo 14 – Selo de Controle  Fixo 15 – SubProduto  Fixo 16 – Insumo Agrícola  Fixo 18 – Produtos Industriais  Fixo 19 – Insumo Industriais  Fixo 20 – Serviço  Fixo 21 – Genérico  Fixo 22 – Produzido  Fixo 23 – Comprado  Fixo 24 – Fantasma  Fixo 25 – Beneficiado  Fixo 26 – Final |
| **Trail** | Rastro por lote ou Sublote, sem rastro | TPRODUTO | CONTROLADOPORLOTE | O valor do campo segue a lógica abaixo:  Se controla estoque por Lote Marcado = Valor 'L' (Controlado por Lote)  Se controla estoque por Lote Desmarcado = Valor 'N' (Não utiliza rastro) |
| **BinControl** | Campo que identifica se o produto possui localização(Endereço/Numero de Serie) | TPRODUTO | USANUMSERIE | O valor do campo segue a lógica abaixo:  Se controla estoque por Nº de Série Marcado = Valor 'true' (Controla Nº de Série)  Se controla estoque por Nº de Série Desmarcado = Valor 'false' (Não controla Nº de Série) |
| GovernmentCode | Código Item |  |  | Não utilizado nesta integração. |
| ItemTypeCode | Código do Tipo de Produto | TPRODUTO | CODTB1FAT | Não utilizado nesta integração. |
| ItemTypeInternalId | InternalId da chave completa do Tipo de Produto | TPRODUTO | CODCOLIGADA|CODTB1FAT | Não utilizado nesta integração. |
| **ListOfGenericPrices** | Lista de Preços do Produto |  |  | Ver ListOfGenericPricesType |
| **ListOfBarCode** | Lista de Códigos de Barra |  |  | Ver ListOfBarCodeType |
| FiscalInformationType | Informações fiscais do Item |  |  | Ver FiscalInformation**\**FiscalClassificationType |
| CustomerItemInformationType | Amarração Cliente X Item |  |  | Ver ListOfCustomerItemInformation \ CustomerItemInformation |
| **FiscalInformationType** | | | | Informações fiscais do Item |
| ****FiscalInformation \**FiscalClassificationType** | | | | Este campos não estão sendo enviados pelo RM pelos seguintes motivos:   * + BranchId - Filial: na inclusão de um novo Produto no RM é gerado na tabela TPRDFIL um registro para cada Filial ativa. Desta forma seria necessário a utilização de uma outra mensagem.   + FiscalInformation: no RM temos Dados Fiscais do Produto e Dados Fiscais por UF. Nestes dois cadastros não temos o campo Descrição. |
| FiscalClassificationCode | Código Classificação Fiscal | TPRODUTO | NCM |  |
| FiscalClassificationInternalId | InternalId do FiscalClassificationCode |  |  | Não enviado pelo RM |
| FiscalClassificationDescription | Descrição Classificação Fiscal |  |  | Não enviado pelo RM |
| PisRetaining | Indica se retém PIS |  |  | Não enviado pelo RM |
| PisAliquot | Alíquota de PIS |  |  | Não enviado pelo RM |
| CofinsRetaining | Indica se retém COFINS |  |  | Não enviado pelo RM |
| CofinsAliquot | Alíquota de COFINS |  |  | Não enviado pelo RM |
| CsllRetaining | Indica se retém CSLL |  |  | Não enviado pelo RM |
| CsllAliquot | Alíquota de CSLL |  |  | Não enviado pelo RM |
| IrrfIncidence | Indica se tem incidência de IRRF |  |  | Não enviado pelo RM |
| IssAliquot | Alíquota de ISS |  |  | Não enviado pelo RM |
| IssServiceCode | Código de Serviço do ISS |  |  | Não enviado pelo RM |
| MunicipalTaxCode | Código de Tributação Municipal |  |  | Não enviado pelo RM |
| TaxSubstitutionCode | Código Especificador da Substituição Tributária (CEST) |  |  | Não enviado pelo RM |
| **ListOfCustomerItemInformation \ CustomerItemInformation** | | | | Não utilizados nesta integração |
| CustomerCode | Código do cliente |  |  | Não utilizados nesta integração |
| CustomerInternalId | InternalId do CustomerCode |  |  | Não utilizados nesta integração |
| GovernmentalInformation | CNPJ/CPF e Inscrição estadual do cliente/fornecedor |  |  | Não utilizados nesta integração |
| CustomerItemCode | Código do Item X Cliente |  |  | Não utilizados nesta integração |
| CustomerItemInternalId | InternalId do CustomerItemCode |  |  | Não utilizados nesta integração |
| **Values \ ValuesType** | | | | |
| **CostPrice** | Preço de Custo | TPRODUTODEF | PRECO1 | Os demais campos de Preço do produto são enviados na tag **ListOfGenericPrices** |
| **SalesPrice** | Preço de Venda | TPRODUTODEF | PRECO2 | Os demais campos de Preço do produto são enviados na tag **ListOfGenericPrices** |
| **AverageCostPrice** | Preço Médio de Custo | TPRODUTODEF | CUSTOMEDIO |  |
| **StandardCostPrice** | Preço Padrão | TPRODUTODEF | CUSTOUNITARIO |  |
| **BaseDate** | Data Base do Calculo dos preços | TPRODUTODEF | DATABASEPRECO1 | Os demais campos de Data-Base do Preço do produto são enviados na tag **ListOfGenericPrices** |
| PackingQuantity | Quantidade na Embalagem |  |  | Não utilizados nesta integração |
| AccountantAccountCode | Código da Conta Contábil |  |  | Não utilizados nesta integração |
| AllowsPurchase | Permite Comprar do Item |  |  | Não utilizados nesta integração |
| IsStorable | Item é Estocável (true) ou Aplicação direta (false) ? |  |  | Não utilizados nesta integração |
| LastUpdateItem | Data Última atualização do Item |  |  | Não utilizados nesta integração |
| LastPurchaseItem | Data Última Compra do Item |  |  | Não utilizados nesta integração |
| **GenericPrices \ GenericPricesType** | Preços | | | |
| **PriceId** | Identificador do preço |  |  | No RM pode ser de 1 a 5 |
| **CurrencyInternalId** | Código da Moeda no Preço | TPRODUTODEF | CODMOEPRECO1 CODMOEPRECO2 CODMOEPRECO3 CODMOEPRECO4 CODMOEPRECO5 |  |
| **BaseDatePrice** | Data-base de Preço | TPRODUTODEF | DATABASEPRECO1 DATABASEPRECO2 DATABASEPRECO3 DATABASEPRECO4 DATABASEPRECO5 |  |
| **Price** | Preço | TPRODUTODEF | PRECO1 PRECO2 PRECO3 PRECO4 PRECO5 |  |
| **BarCode \****BarCodeType** | Códigos de Barra | | | |
| **Code** | Código de Barras do Produto | TPRDCODIGO | CODIGO |  |
| **InternalId** | InternalId do Código de Barras | TPRDCODIGO | CODCOLIGADA|TIPO|CODIGO |  |
| **UnifOfMeasureInternalId** | Unidade do Código do Produto | TPRDCODIGO | CODUND |  |
| **ItemQuantity** | Quantidade do Produto | TUND | FATORCONVERSAO | Tratado via extension. Busca-se o fator de conversão da unidade informada para o Códigos de barra. |
| **ECFTaxing** | Tributação de Cupom Fiscal | | | |
| **Code** | Código da Tributação ECF | TPRODUTO | TRIBUTACAOECF |  |
| **Type** | Tipo da Tributação ECF | TTRIBUTACAOECF | TIPO | Informação buscada via extension quando existir Tributação Cupom Fiscal informada para o Produto, respeitando o seguinte de-para de valores:  Fixo 1 - Tributado: enviado quando Tipo = 0  Fixo 2 - Isento: enviado quando Tipo = 1  Fixo 3 - Substituição Tributaria: enviado quando Tipo = 2  Fixo 4 - Não tributado: enviado quando Tipo = 3  Fixo 5 - Outros. |
| **Aliquot** | Alíquota da Tributação ECF | TTRIBUTACAOECF | ALIQUOTA | Informação buscada via extension quando existir Tributação Cupom Fiscal informada para o Produto. |
| **ManufacturerCode** | Número no Fabricante | TPRODUTODEF | NUMNOFABRIC |  |
| **ComercialFamilyItemType** | Amarração famílias(categorias) pertencentes ao produto | | | |
| ComercialFamilyCode | Código Família Comercial |  |  | Não utilizado pela linha RM |
| ComercialFamilyInternalId | InternalId da chave completa de Família Comercial do produto |  |  | Não utilizado pela linha RM |
| ComercialFamilyDescription | Descrição Família Comercial |  |  | Não utilizado pela linha RM |

 

* Somente os campos marcados em negrito são tratados no Adapter, sendo os demais não enviados na mensagem.
