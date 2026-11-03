---
content_hash: a6e65991c3ce5bd66cb1e95d2d5452b35b5ddb18fdc608bc467dd8dfddfce436
fetched_at: '2026-06-29T00:06:13.732472+00:00'
page_id: '208345689'
product: rm
source: tdn-rm
title: ER_PCREQ-7800_Vendedor - Seller
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-7800_Vendedor+-+Seller
version: 139
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Faturamento |
| **Segmento Executor** | TOTVS Construção e Projetos | | |
| **Projeto1** | Integração BackOffice RM x PDV Protheus | **IRM1** | PCREQ-7769 |
| **Requisito1** | PCREQ-7800 | **Subtarefa1** | PDR\_CP\_MOV008-33 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Implementação do adapter de integração via Mensagem Única TOTVS do cadastro de Vendedor viabilizando assim o CRUD completo do cadastro por envio de mensagem de integração no padrão de Mensageria Única TOTVS.

## Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de envio de Mensagens Únicas TOTVS para integração do cadastro de Vendedor, estando o adapter de recebimento desta mesma mensagem fora do escopo do requisito, ou seja , o cadastro de Vendedor será realizado somente no BackOffice RM e devendo todo o tratamento de comissionamento ser também gerido neste.

 

A análise e o desenvolvimento do adapter será efetuado considerando a integração do BackOffice RM com PDV Protheus, mas também viabilizará a integração com outros destinatários desde que respeitado o layout da mensagem e os campos especificado para envio. 

Visto que o PDV Protheus somente necessita de informações para lookup e o BackOffice RM quem deve efetuar todo o controle de comissionamento, somente serão enviados os dados básicos do vendedor.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Funcionários | Inclusão \ Alteração \ Exclusão | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \  Estoque, Compras e Faturamento \ Funcionários |  |

**Tabelas Utilizadas**

* TVEN – Vendedores
* TVENCOMPL – Tab.Complementar de Vendedor/Comprador
* TVENVAL – Valores por Funcionário/Filial/C.Custo

 

**Entidades de Integração** 

* DataServer de Gatilho
  + MovVenData
* Transformação
  + Id: Seller
  + Versão: 2.001
* SourceCode (Evento)
  + GUID: d772e85a-0f3f-4fbc-a387-54bf763d925d
  + Nome: Seller\_2\_001

## Regras de Integridade

**Controle de comissionamento**

Visto que todo o controle de comissionamento deverá ser efetuado no BackOffice RM não haverá integração de dados referentes a este controle na Mensagem Única enviada.

**Tipo de Vendedor**

O campo Tipo será desconsiderado para a integração, enviando assim registros referentes a todos os tipos de Vendedores do BackOffice RM (Vendedor, Comprador, Gerente e demais).

**Vendedor Padrão**

O PROTHEUS possui um parâmetro onde é informado o Código do Vendedor Padrão que será assumido na tela de atendimento no momento da Venda. Com isso é necessário que este Vendedor seja cadastrado no RM e o parâmetro ***MV\_VENDPAD***seja atualizado no Configurador do PROTHEUS (SIGACFG).

**Tamanho dos Campos**

Os campos listados na tabela abaixo possuem no Protheus tamanho máximo menor que permitido no RM e as respectivas ações de integração.

| **Campo** | **Tamanho Protheus** | ****Tamanho no** BackOffice RM** | **Ação de Integração** |
| --- | --- | --- | --- |
| Code | 6 caracteres | 16 caracteres | Caso seja enviado maior que o permitido o Protheus retornará Erro com mensagem explicativa. |
| ShortName | 25 caracteres | 80 caracteres | O RM enviará o campo NOME com tamanho cortado em 25 caracteres. |

**Compartilhamento de registros por Coligada e Filial**

Visto que o registo no BackOffice RM não considera a Filial como parte da Chave e existe a restrição na Mensagem Única TOTVS para envio do 'CompanyInternalId' completo (Coligada + Filial), é necessário que o sistema destinatário possua este cadastro exclusivo por Coligada e compartilhado por Filial.

Em resumo, o sistema de destino não deve considerar a informação de Filial enviada, pois caso no BackOffice RM este campo esteja nulo será enviada a Filial do contexto de integração, que e a primeira filial da empresa disponível na tabela De-Para.

Em relação ao Protheus deve seguir o seguinte compartilhamento:

* + Empresa:  Exclusivo
  + Unidade:   Deve ser equivalente à entidade relacionada no De-Para de integração (Empresa ou filial)
  + Filial:        Compartilhado

## Restrições e Ponto de Atenção

* Deve-se retirar a permissão do cadastro de Vendedor no Protheus, pois estas informações serão cadastradas no BackOffice RM.

## Fluxo do Processo

## Mapeamento dos Campos

* **Mensagem Seller 2.000**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **Descrição** | **RM** | | |
| **Tabela** | **Campo** | **Observação** |
| **CompanyId** | Código da empresa. | TVEN | CODCOLIGADA | Código da Coligada é obtido a partir do De-Para de Filial. |
| **BranchId** | Código da filial | TVEN | CODFILIAL |
| **CompanyInternalId** | InternalId da chave completa de empresa do produto | TVEN | CODCOLIGADA|CODFILIAL |
| **Code** | Código do Vendedor | TVEN | CODVEN |  |
| **InternalId** | InternalId de Integração | TVEN | CODCOLIGADA|CODVEN |  |
| **Name** | Nome do Vendedor | TVEN | NOME |  |
| **ShortName** | Login do Vendedor | TVEN | NOME | Conforme solicitado pela equipe Protheus, será enviado o mesmo campo NOME com a informação cortada em 25 caracteres. |
| **Active** | Registro Ativo/Inativo | TVEN | INATIVO | TVEN.INATIVO = 0: Ativo  TVEN.INATIVO = 1: Inativo |
| SellerPassword | Senha do Vendedor |  |  | Campo não utilizado na Integração. |
| SellerPhoneDDD | DDD do Vendedor |  |  | Campo não utilizado na Integração. |
| SellerPhone | Telefone do Vendedor |  |  | Campo não utilizado na Integração. |
| SellerEmail | E-mail do Vendedor |  |  | Campo não utilizado na Integração. |
| Address | Dados da localização física do vendedor |  |  | Campo não utilizado na Integração. |
| SalesChargeInformation | Informações de comissões |  |  | Campo não utilizado na Integração. |
| CustomerVendorInternalId | InternalId do Fornecedor |  |  | Campo não utilizado na Integração. |
| SalesChargeInterface | Interface a ser utilizada no fechamento da comissão |  |  | Campo não utilizado na Integração. |

* Somente os campos marcados em negrito são tratados no Adapter, sendo os demais não enviados por não haver necessidade de uso no PDV Protheus.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
