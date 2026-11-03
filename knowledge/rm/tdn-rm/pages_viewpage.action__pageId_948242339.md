---
content_hash: 1af5ce231e3c1885249d52dac1ecb72e1644112c0beb3bec1e6ae352f8e5b929
fetched_at: '2026-06-29T00:12:09.580740+00:00'
page_id: '948242339'
product: rm
source: tdn-rm
title: Integração TOTVS Gestão Hospitalar x Backoffice Datasul (middleware TOTVS iPaaS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=948242339
version: 14
---

DatasulvisaoGeralVisão Geral

## **Visão Geral**

Esta documentação tem como objetivo descrever como funciona a integração do ERP TOTVS Gestão Hospitalar com o BackOffice Datasul, utilizando a plataforma TOTVS iPaaS como middleware de comunicação.

Informações sobre o Totvs iPaaS no link <https://tdn.totvs.com/x/3AaFO>

preRequisito-totvsPré-Requisitos Totvs

## **Pré-requisitos no ambiente BackOffice TOTVS**

- Configuração de máscaras de produto, centro de custo, local de estoque, para utilização dos mesmos códigos do Datasul.

- Script para habilitar integração Saúde x Datasul: tabela HCPARAMETROS campo INTEGRASAUDEEMS (vide aba Script).

- Scripts para habilitar e configurar a integração com o TOTVS IPaaS (vide aba Script).

### **2 – Cadastros obrigatórios no TOTVS**

#### **2.1 – TOTVS Gestão Hospitalar:**

**- Menu Ambiente/Parâmetros Gestão Hospitalar:** preencher os dados do Datasul no item “Integrações/Integração BackOffice/Gestão de Estoque Compras e Faturamento/**Parâmetros E.M.S.**

O item “Parâmetros E.M.S somente ficará habilitado se existir integração com Datasul.

O campo “Estabelecimento” é o principal campo da integração, que deve existir o mesmo código no Datasul e corresponde ao campo "SiteID".

**- Menu Ambiente/Parâmetros Gestão Hospitalar:** preencher os tipos de movimentos no item “Integrações/Integração BackOffice/Gestão de Estoque Compras e Faturamento/**Tipos de Movimentação de Estoque.**

### **ATENÇÃO: os códigos de tipos de movimentos são fixos, quando integrado no Datasul.**

#### **Esta já é uma premissa existente na integração com Datasul, mesmo quando utilizava antigo EAI.**

O cadastro de tipo de movimento para integração Datasul deve seguir determinados códigos fixos.

Por exemplo, ao solicitar uma requisição para paciente, o código do tipo de movimento requisição deverá ser correspondente a 2.1.01.

2.1.01 – Saída de movimentação de estoque

1.1.01 – Entrada de movimentação de estoque

Segue abaixo a relação dos códigos para as respectivas funcionalidades:

Os Tipos de Movimentos (Totvs) que serão reconhecidos para o Datasul são:

|  |  |  |
| --- | --- | --- |
| **Código Fixo do Tipo Movimento (TOTVS)** | **Descrição** | **TransactonID no Datasul - via iPaaS** |
| 2.1.01 | Saída de estoque (requisições da mov.estoque) | stockMovementPublic (antigo InventoryTransaction) |
| 2.1.02 | Pedido | ordersPublic (antigo SalesOrder) |
| 2.1.03 | Recebimento | sem correspondente iPaaS (antigo AccountReceivableDocument) |
| 2.1.04 | Controle de Caixa inclusão | sem correspondente iPaaS (antigo TradingProcess) |
| 2.1.05 | Nota fiscal | sem correspondente iPaaS (antigo ReceiveInvoiceDocument) |
| 1.1.01 | Entrada no Estoque (devoluções mov.estoque da Farmácia) | InventoryTransaction |
| 1.1.02 | Pagamento | sem correspondente iPaaS (antigo AccountPayableDocument) |
| DEFAULT | Caso não informado nenhum | ordersPublic (antigo SalesOrder) |

### Abaixo temos um exemplo de cadastro dos tipos de movimentos para integração Datasul. Lembrando que apenas o campo CODTMV que terá seu conteúdo fixo, as demais informações devem ser aplicadas conforme cada base de dados do Cliente que a utiliza.

###### /\*Inclusão de tipos de movimento\*/ INSERT INTO TTMV (CODCOLIGADA,CODTMV, NOME) VALUES (1,'2.1.01','Saida de Estoque'); INSERT INTO TUSRTMV (CODUSUARIO,CODCOLIGADA,CODTMV,INCLUIR,ALTERAR,EXCLUIR,CANCELAR,LANCAR,                      FATURAR,ATIVAR,IMPRIMIR,ALTERARDEPOISIMP,REABRIR,CONSULTAR,COPIAR,                      CONTABILIZAR,REIMPRIMIR,ESTORNARCONTAB,INCLUIRPORFAT,ALTERARDEPOISEMAIL,EMAIL,COTAR) VALUES ('mestre','1','2.1.01','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','1','1','1');

###### INSERT INTO TTMV (CODCOLIGADA,CODTMV, NOME) VALUES (1,'2.1.02','Pedido NF'); INSERT INTO TUSRTMV (CODUSUARIO,CODCOLIGADA,CODTMV,INCLUIR,ALTERAR,EXCLUIR,CANCELAR,LANCAR,                      FATURAR,ATIVAR,IMPRIMIR,ALTERARDEPOISIMP,REABRIR,CONSULTAR,COPIAR,                      CONTABILIZAR,REIMPRIMIR,ESTORNARCONTAB,INCLUIRPORFAT,ALTERARDEPOISEMAIL,EMAIL,COTAR) VALUES ('mestre','1','2.1.02','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','1','1','1');

###### INSERT INTO TTMV (CODCOLIGADA,CODTMV, NOME) VALUES (1,'2.1.03','Titulo a Receber'); INSERT INTO TUSRTMV (CODUSUARIO,CODCOLIGADA,CODTMV,INCLUIR,ALTERAR,EXCLUIR,CANCELAR,LANCAR,                      FATURAR,ATIVAR,IMPRIMIR,ALTERARDEPOISIMP,REABRIR,CONSULTAR,COPIAR,                      CONTABILIZAR,REIMPRIMIR,ESTORNARCONTAB,INCLUIRPORFAT,ALTERARDEPOISEMAIL,EMAIL,COTAR) VALUES ('mestre','1','2.1.03','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','1','1','1');

###### INSERT INTO TTMV (CODCOLIGADA,CODTMV, NOME) VALUES (1,'1.1.01','Entrada de Estoque'); INSERT INTO TUSRTMV (CODUSUARIO,CODCOLIGADA,CODTMV,INCLUIR,ALTERAR,EXCLUIR,CANCELAR,LANCAR,                      FATURAR,ATIVAR,IMPRIMIR,ALTERARDEPOISIMP,REABRIR,CONSULTAR,COPIAR,                      CONTABILIZAR,REIMPRIMIR,ESTORNARCONTAB,INCLUIRPORFAT,ALTERARDEPOISEMAIL,EMAIL,COTAR) VALUES ('mestre','1','1.1.01','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','1','1','1');

###### INSERT INTO TTMV (CODCOLIGADA,CODTMV, NOME) VALUES (1,'1.1.02','Titulo a Pagar'); INSERT INTO TUSRTMV (CODUSUARIO,CODCOLIGADA,CODTMV,INCLUIR,ALTERAR,EXCLUIR,CANCELAR,LANCAR,                      FATURAR,ATIVAR,IMPRIMIR,ALTERARDEPOISIMP,REABRIR,CONSULTAR,COPIAR,                      CONTABILIZAR,REIMPRIMIR,ESTORNARCONTAB,INCLUIRPORFAT,ALTERARDEPOISEMAIL,EMAIL,COTAR) VALUES ('mestre','1','1.1.02','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','1','1','1');

### **2.2 – TOTVS Gestão de Estoque Compras e Faturamento**

Parâmetros a serem definidos:

#### **Máscara de Centro de Custo: necessário sua configuração na base de dados, antes que se inicie qualquer lançamento.**

### **Máscara para Local de estoque**

### **Máscara de Produto:**

### **Tipos de Movimentos:**

scriptScript de Integração

## **Script necessários para habilitar a integração com o TOTVS iPaaS**

**1 - Habilitar integração Saude x Datasul: coluna INTEGRASAUDEEMS**

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORINT) VALUES (0,  'INTEGRASAUDEEMS', '1' )

**2 - Habilitar a integração Totvs IPaaS com o BackOffice Datasul**

O script abaixo estará disponibilizado no conversor do release 12.1.2510 para todos os clientes (mesmo os que não utilizam integração com o Totvs IPaas).

Para ativar a integração com iPaaS, o valor do campo deve ser VALORINT = 1.

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORINT) VALUES (0, 'INTEGRATOTVSIPAAS', '0' )

**3 - Habilitar nome da URL do iPaaS para o envio da Movimentação de Estoque (stockMovementPublic) - POST**

O Nome da Coluna é igual a TOTVSIPAAS\_STOCKMOVEMENTPUBLIC e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/21b71a4a-43d2-405f-8231-702bc91186cc/api-key/50123758-cfa4-4be1-8f15-a399509dd848>'

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORSTR) VALUES (0, 'TOTVSIPAAS\_STOCKMOVEMENTPUBLIC', exemplo\_Url )

**4 - Habilitar nome da URL do iPaaS para consulta de Saldo de Estoque Datasul  (stockBalancePublic) - GET**

O Nome da Coluna é igual a TOTVSIPAAS\_STOCKBALANCEPUBLIC e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/bf123719-26b0-4731-925c-acc91e0aa1f3/api-key/90edafcc-5214-46d3-a193-983142b44cdf>'

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORSTR) VALUES (0,  'TOTVSIPAAS\_STOCKBALANCEPUBLIC', exemplo\_Url )

**5 - Habilitar nome da URL do iPaaS para consulta de Preço do Item Datasul (itemPricePublic) - GET**

O Nome da Coluna é igual a TOTVSIPAAS\_ITEMPRICEPUBLIC e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/8cefcee1-a73e-4448-adf4-02044c48f378/api-key/7f22da1a-1caa-4cea-a8f3-b8c538933cb4>'

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORSTR) VALUES (0,  'TOTVSIPAAS\_ITEMPRICEPUBLIC', exemplo\_Url )

**6 - Habilitar nome da URL do iPaaS para integração do Grupo de Estoque - POST, PUT e DELETE**

O Nome da Coluna é igual a TOTVSIPAAS\_INVENTORYGROUPS e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/a33878b5-d94f-414a-af63-48f1fa5f528e/api-key/4440950e-d733-4856-843b-8d8e337b26ee>'

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORSTR) VALUES (0,  'TOTVSIPAAS\_INVENTORYGROUPS', exemplo\_Url )

**7 - Habilitar nome da URL do iPaaS para integração do Unidade de Medida - POST, PUT e DELETE**

O Nome da Coluna é igual a TOTVSIPAAS\_UNITYMEASURES e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/b2ce305c-8f52-4007-9312-748a97445ddc/api-key/d1c953f0-7fc5-4ffd-9717-8b2ef6ea06ec>'

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORSTR) VALUES (0,  'TOTVSIPAAS\_UNITYMEASURES', exemplo\_Url )

**8 - Habilitar nome da URL do iPaaS para integração do Produto - POST e PUT**

O Nome da Coluna é igual a TOTVSIPAAS\_PRODUCT e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/f4daae6b-5fb3-46c9-bb9e-048f4782197d/api-key/2dfd9868-e50c-471e-b613-794fe67bc75b>'

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORSTR) VALUES (0,  'TOTVSIPAAS\_PRODUCT', exemplo\_Url )

preRequisitoPré-Requisitos DATASUL

## **Pré Requisitos no ambiente BackOffice DATASUL:**

- Configurar base de dados Datasul para utilização de Lote de Produto.

- API devem estar configuradas para acesso por IP Público.

- API disponibilizadas para a integração:

|  |  |  |  |
| --- | --- | --- | --- |
| **API DATASUL** | **ENDPOINT** | **Tabela HCPARAMETROS (campo NOMECOLUNA) com a URL** | **Assunto no Totvs Gestão Hospitalar** |
| stockMovement(POST) | {servidor}/dts/datasul-rest/resources/prg/cep/**v1**/stockMovementExemplo:<https://hospital99.datasul.cloudtotvs.com.br/api/cep/v1/stockMovement>A API Datasul = stockMovementPublic (método POST) , é responsável por enviar a movimentação de estoque , do Gestão de Estoque Compras e Faturamento para ser gravado no BackOffice Datasul. Deverá retornar os dados do registros e a chave do campo IDMOV que será gravado no TOTVS Gestão Hospitalar, interligando ambos os registros. | TOTVSIPAAS\_STOCKMOVEMENTPUBLIC | - Movimentação de Estoque, gerado através das seguintes requisições: folha de sala, requisição de paciente, prescrição médica, requisição de centro de custo, transferências, devolução para paciente.- Montar e Desmontar KIT PRE MONTADO |
| stockMovement(GET) | {servidor}/dts/datasul-rest/resources/prg/cep/**v2**/stockMovementExemplo: <https://hospital99.datasul.cloudtotvs.com.br/api/cep/v2/stockMovement>A API Datasul = stockMovementPublic (método GET) , é responsável por consultar a movimentação de estoque no Datasul e informar ao TOTVS Gestão Hospitalar. | TOTVSIPAAS\_STOCKMOVEMENT\_GET | Livro de Medicamento Controlado |
| stockBalancePublic | {servidor}/dts/datasul-rest/resources/prg/cep/**v3**/stockBalancePublicA API Datasul = stockBalancePublic (método GET) , é responsável por consultar o saldo de um produto no Datasul e informar ao TOTVS Gestão Hospitalar. | TOTVSIPAAS\_STOCKBALANCEPUBLIC | Saldo em Estoque (lote do produto) |
| itemPricePublic | {servidor}/dts/datasul-rest/resources/prg/cep/**v1**/itemPricePublicExemplo: [https://hospital99.datasul.cloudtotvs.com.br/api/cep/v1/itemPricePublic](https://hospital99.datasul.cloudtotvs.com.br/api/cep/v1/stockMovement)A API Datasul = itemPricePublic (método GET) , é responsável por consultar o preço de um produto no Datasul e informar ao TOTVS Gestão Hospitalar. | TOTVSIPAAS\_ITEMPRICEPUBLIC | Preço do item. Processo Atualiza preço |
| productPublic | {servidor}/dts/datasul-rest/resources/prg/cep/**v1**/productPublicExemplo: [https://hospital99.datasul.cloudtotvs.com.br/api/cdp/v1/productPublic](https://hospital99.datasul.cloudtotvs.com.br/api/cep/v1/stockMovement)A API Datasul = productPublic (método GET, POST e PUT) , é responsável por cadastrar e atualizar os produtos no TOTVS Gestão Hospitalar e sincronizar com o Datasul. | TOTVSIPAAS\_PRODUCTPUBLIC | Fórmula visual para cadastro de produtoSAUWKF008 - IPAAS - Integração ProdutosWFdisponibilizada nos objetos gerenciais do Totvs Compartilhamento |
| unityMeasuresPublic | {servidor}/dts/datasul-rest/resources/prg/cdp/**v1**/unityMeasuresPublicExemplo: [https://hospital99.datasul.cloudtotvs.com.br/api/cdp/v1/unityMeasuresPublic](https://hospital99.datasul.cloudtotvs.com.br/api/cep/v1/stockMovement)A API Datasul = unityMeasuresPublic (método GET, POST, PUT e DELETE) , é responsável por cadastrar, atualizar e deletar as unidades de medidas no TOTVS Gestão Hospitalar e sincronizar com o Datasul. | TOTVSIPAAS\_INVENTORYGROUPS | Fórmula visual para cadastro de unidade de medidasSAUWKF007 - IPAAS - Integração Unidade de Medida.TotvsWFdisponibilizada nos objetos gerenciais do Totvs Compartilhamento |
| inventoryGroupsPublic | {servidor}/dts/datasul-rest/resources/prg/cep/**v1**/inventoryGroupsPublicExemplo: [https://hospital99.datasul.cloudtotvs.com.br/api/cdp/v1/iventoryGroupsPublic](https://hospital99.datasul.cloudtotvs.com.br/api/cep/v1/stockMovement)A API Datasul = inventoryGroupsPublic (método GET, POST, PUT e DELETE) , é responsável por cadastrar, atualizar e deletar grupo de estoque no TOTVS Gestão Hospitalar e sincronizar com o Datasul. | TOTVSIPAAS\_UNITYMEASURES | Fórmula visual para cadastro de grupo de estoqueSAUWKF006 - IPAAS - Integração Grupo de Estoque.TotvsWFdisponibilizada nos objetos gerenciais do Totvs Compartilhamento |
|  |  |  |  |

totvsIpaasTotvs iPaaS - Diagramas

## **Diagramas do TOTVS iPaaS para Integração com Datasul**

**Dica técnica para Desenvolvedores de Software:** para Diagramas que utilizam o método GET, deverá ser implementado nos sistemas, uma chamada PostAsync para que funcione a chamada à API no iPaaS. O campo TransactionType deve ser mapeado no diagrama componente Generator com o nome iniciado com letra maiúscula, ou seja transactionType vai gerar dado incorreto.

**Mensagem de retorno MethodNotAllowed:** Caso sua aplicação ou cliente utilize filtros de IP (firewall) para controle de acesso, será necessário incluir os novos endereços para garantir a continuidade do serviço. Lembrando que os IP que já existem serão mantidos, a lista com todos IP pode ser encontrada <https://tdn.totvs.com/x/Lm3WMg>

|  |  |  |
| --- | --- | --- |
| **NOME DO DIAGRAMA** | **DESCRIÇÃO DO DIAGRAMA** | **Uso no Totvs Gestão Hospitalar** |
| Consultar Movimentação Estoque (DATASUL) | Diagrama responsável por consultar as movimentações de estoque geradas no Datasul, ao executar processos da Farmácia no Totvs Gestão Hospitalar:Livro de medicamentos Controlados,Folha de Sala do Centro Cirúrgico, Requisição Paciente, Prescrição Médica, Requisição a Centro de Custos, Transferências, Devolução para Paciente, Devolução para Centro de Custo | Consultas aos movimentos gerados no Datasul ao executar os processos do Totvs Gestão Hospitalar:Folha de Sala do Centro Cirúrgico, Requisição Paciente, Prescrição Médica, Requisição a Centro de Custos, Transferências, Devolução para Paciente, Devolução para Centro de Custo, Livro de medicamentos controlados |
| Gravar Movimentação de Estoque (DATASUL) | Diagrama responsável por gravar as movimentações de estoque geradas pela Farmácia do Totvs Gestão Hospitalar, inserindo no DATASUL.Movimentações estas da Folha de Sala do Centro Cirúrgico, Requisição Paciente, Prescrição Médica, Requisição a Centro de Custos, Transferências, Devolução para Paciente, Devolução para Centro de Custo. | Inserir movimentação de estoque gerado no Totvs Gestão Hospitalar e gravado no DATASUL.Processos executados no Totvs Gestão Hospitalar:Folha de Sala do Centro Cirúrgico, Requisição Paciente, Prescrição Médica, Requisição a Centro de Custos, Transferências, Devolução para Paciente, Devolução para Centro de Custo, Livro de medicamentos controlados |
| Saldo de Estoque (DATASUL) | Diagrama responsável por consultar o saldo do estoque e o lote do produto no DATASUL. | Utilizado pelo Totvs Gestão Hospitalar: ao pesquisar um lote na requisição de paciente, ao pesquisar o saldo na inclusão de livro de medicamentos controlados. |
| Produtos (DATASUL) | Diagrama responsável pelo cadastro de Produtos no Datasul. Realiza inclusão e alteração no Datasul. | Utilizado em Fórmulas Visuais do Totvs Gestão Hospitalar. |
| Unidade de Medidas (DATASUL) | Diagrama responsável pelo cadastro de Unidades de Medidas no Datasul. Realiza inclusão, alteração e exclusão no Datasul. | Utilizado em Fórmulas Visuais do Totvs Gestão Hospitalar. |
| Grupo de Estoque (DATASUL) | Diagrama responsável pelo cadastro de Grupo de estoque no Datasul. Realiza inclusão, alteração e exclusão no Datasul. | Utilizado em Fórmulas Visuais do Totvs Gestão Hospitalar. |
| Preço do Item (DATASUL) | Diagrama responsável em consultar o preço do produto no Datasul. | Utilizado no processo “Atualiza preço” do Totvs Gestão Hospitalar |
