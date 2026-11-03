---
content_hash: f851d651d32ef49318ac182f0ec16ac48670f2602c543a169cafb882eda8ab46
fetched_at: '2026-06-29T00:12:09.562275+00:00'
page_id: '948242140'
product: rm
source: tdn-rm
title: Integrações utilizando TOTVS iPaaS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=948242140
version: 16
---

DatasulvisaoGeralVisão Geral

## **O que é TOTVS iPaaS**

O TOTVS iPaaS é uma plataforma Low Code, feita para facilitar a construção e manutenção de integrações, de maneira simples e segura.

Com o TOTVS iPaaS, você controla as entregas de mensagens entre um sistema e outro, e cria códigos "De:Para" compatíveis para permitir a comunicação entre as soluções integradas.

E ainda conta com dashboards dinâmicos e total rastreabilidade, que permitem acompanhar a comunicação entre os sistemas interligados pelo TOTVS iPaaS em tempo real, permitindo identificar qualquer problema facilmente.

### Veja mais explicações sobre esta plataforma em <https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-totvs-IpaaS/>

### Documentação do Totvs iPaaS: <https://tdn.totvs.com/display/public/IPAAS/TOTVS+iPaaS>

### Ambiente (<https://ipaas.totvs.app/>)

**A partir da versão 12.1.2506 será disponibilizado novos pacotes:**

* **TOTVS Gestão Hospitalar + Linha Datasul:**Integração de Movimentação de estoque,  Emissão de Etiquetas Código de Barras, Livro de Medicamento Controlado, Montar e Desmontar KIT PRE MONTADO,  Saldo em estoque, Atualização de Preço, Fórmulas Visuais para Cadastros de: produto, unidades de medida, grupo de estoque.

**Para os diagramas do iPaaS, serão disponibilizados template com modelos de uso.**

## **EXEMPLO DE UTILIZAÇÃO**

#### **Exemplo do Diagrama de Movimentação de Estoque no Totvs iPaaS:**

**Exemplo Datasul:**

**Exemplo Protheus:**

#### **Componente Webhook:**

URL que será chamada para executar as API. O seu conteúdo é gerado automaticamente pela ferramenta.

#### **Componente Generator:**

De-Para configurado para o envio de dados ao Datasul: (Em construção):

#### **Componente TOTVS Datasul:**

#### **Componente TOTVS Protheus:**

Preenchimento da API desejada, o método (POST/GET/PUT/DELETE) e a associação de cada campo que será retornado.

#### **Componente Resposta Síncrono:**

Configurar qual item irá enviar o resultado da mensagem

preREquisitosPré Requisitos Totvs

## **Pré-requisitos no ambiente BackOffice TOTVS**

- Configuração de máscaras de produto, centro de custo, local de estoque, para utilização dos mesmos códigos do Datasul.

- Script para habilitar integração Saúde x Datasul: tabela HCPARAMETROS campo INTEGRASAUDEEMS (vide aba Script).

- Scripts para habilitar e configurar a integração com o TOTVS IPaaS (vide aba Script).

### **1 – Pré requisitos para integração via Totvs iPaaS**

Para implementar a integração Totvs Gestão Hospitalar x BackOffice Datasul via Totvs iPaas são necessários os 3 itens abaixo:

Cada item será detalhado em seu respectivo tópico.

**1.1 - Banco de dados Datasul em produção:** por exemplo, cadastros de produto, de lote, movimentação estoque, empresa, permissões de usuários, parâmetros e todo o ambiente necessário para o uso do BackOffice Datasul.

O Totvs ERP irá gravar movimentação no Datasul, e estes códigos devem ser o mesmo em ambos os sistemas.

**1.2 - Banco de dados TOTVS ERP em produção:** por exemplo, no Gestão Hospitalar: parâmetros Datasul de integração (empresa, códigos de movimento do Datasul 1.1.01, 2.1.01), tipos de movimentação utilizados. No Gestão Estoque, parâmetros gerais de movimentação de estoque e máscara de produto.

**1.3 - Ambiente contendo API Datasul públicas**, que foram implementadas para uso no Totvs iPaaS.

Necessário usuário e senha com permissão de acesso às API Datasul.

Exemplo de filtro: <https://hospital999.datasul.cloudtotvs.com.br/api/cdp/v1/unityMeasuresPublic?$filter=code> = "UN" and description = "UNIDADE"

|  |  |  |
| --- | --- | --- |
| **API DATASUL** | **ENDPOINT** | **PROCESSO NO TOTVS GESTÃO HOSPITALAR** |
| UnityMeasuresPublic | {servidor}/dts/datasul-rest/resources/prg/cdp/v1/unityMeasuresPublic | Farmácia: Cadastro de Unidade de Medidas  - Fórmula Visual SAUWKF0007 - IPAAS - Integração Unidade de Medida.TotvsWF |
| inventoryGroupsPublic | {servidor}/dts/datasul-rest/resources/prg/cep/v1/inventoryGroupsPublic | Farmácia: Cadastro de Grupo de Estoque  - Fórmula Visual SAUWKF0006 - IPAAS - Integração Grupo de Estoque.TotvsWF  <https://tdn.totvs.com/pages/releaseview.action?pageId=868240782> |
| productPublic | {servidor}/dts/datasul-rest/resources/prg/cep/v1/productPublic | Farmácia: Cadastro de Produto  - Fórmula Visual |
| itemPricePublic  (GET) | {servidor}/dts/datasul-rest/resources/prg/cep/v1/itemPricePublic | Farmácia: Preço do item.  Processo Atualização de preço  <https://tdn.totvs.com/pages/releaseview.action?pageId=870394983> |
| stockMovement  (POST) | {servidor}/dts/datasul-rest/resources/prg/cep/v1/stockMovement | Farmácia - Movimentações de Estoque, ao executar o  “Processar”, para os tipos:  Folha de Sala do Centro Cirúrgico,  Requisição Paciente,  Prescrição Médica,  Requisição a Centro de Custos,  Transferências,  Devolução para Paciente,  Devolução para Centro de Custo.    Após Processar a requisição, será criado o movimento no BackOffice Datasul e gravado o id na tabela TITMOV do RM |
| stockMovement (POST) | {servidor}/dts/datasul-rest/resources/prg/cep/v1/stockMovement | Farmácia: Montar e Desmontar KIT PRE MONTADO |
| stockMovement  (GET) | {servidor}/dts/datasul-rest/resources/prg/cep/v2/stockMovement | Farmácia: Livro de Medicamento Controlado.  Processo “Incluir itens no livro”  <https://tdn.totvs.com/pages/releaseview.action?pageId=866540460> |
| stockBalancePublic (GET) | {servidor}/dts/datasul-rest/resources/prg/cep/v3/stockBalancePublic | Farmácia: Emissão de Etiquetas Código de Barras |
| stockBalancePublic (GET) | *http://[servidor]/dts/datasul-rest/resources/prg/cep/v3/stockBalancePublic* | Farmácia: Saldo de estoque.  Ao consultar Lote na requisição paciente  <https://tdn.totvs.com/pages/viewpage.action?pageId=867797276> |

**1.4 – Diagramas no Totvs iPaaS:** através do link <https://ipaas.totvs.app/> encontramos os diagramas utilizados pelo Totvs Gestão Hospitalar para integrar com o BackOffice Datasul. Cada cliente deve possuir o seu devido cadastro conforme documentação citada anteriormente.

Necessário usuário e senha com permissão de acesso ao aplicativo Totvs iPaaS, com permissão administrador para criação dos diagramas. Obs.: um administrador existente consegue incluir novos usuários e adicioná-los como administrador.

Necessário usuário e senha com permissão de acesso às API Datasul.

Empresa = Saúde – Prestadores: é um cadastro interno de diagramas iPaaS.

Senha de rede pra logar no ipaas

Senha do usuário para acessar  a Empresa disponibilizado no Totvs iPaaS

Por exemplo, empresa Saude-Prestadores

Utilizar o aplicativo igual a  

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DIAGRAMA** | **DESCRIÇÃO** | **SERVIÇO** | **RECURSO** | **TIPO DE WEBWOOK** |
| Consultar Movimentação Estoque (Datasul) | Diagrama responsável por consultar as movimentações de estoque geradas no Datasul. | TOTVS-CEP | GET - stockMovementPublic | Síncrono |
| Movimentação de Estoque (ASYNC) | Responsável em gravar a movimentação de Estoque do Totvs Gestão Hospitalar para o BackOffice Datasul (EMS), através da API stockMovementPublic | TOTVS-CEP | POST - stockMovementPublic | Assíncrono |
| Saldo de Estoque (DATASUL) | Diagrama responsável por consultar o saldo do estoque e o lote do produto no DATASUL. | TOTVS-CEP | GET -stockBalancePublic | Síncrono |
| Preço do item (DATASUL) | Recuperar o preço do produto | TOTVS-CEP | GET - itemPricePublic | Síncrono |
| Produtos (DATASUL) | Diagrama responsável pelo cadastro de Produtos no Datasul. Realiza inclusão e alteração no Datasul através de Fórmula Visual do Totvs Gestão Hospitalar | TOTVS-CEP | POST – productPublic  PUT - productPublic | Síncrono |
| Grupo de Estoque (DATASUL) | Cadastro de Grupo de Estoque via Fórmula Visual | TOTVS-CEP | POST - inventoryGroupsPublic  PUT - inventoryGroupsPublic  DELETE - inventoryGroupsPublic | Síncrono |
| Unidade de Medidas (DATASUL) | Cadastro de Unidade de Medidas via Fórmula Visual | TOTVS-CDP | POST - unityMeasuresPublic  PUT - unityMeasuresPublic  DELETE - unityMeasuresPublic | Síncrono |

### **2 – Cadastros obrigatórios no TOTVS**

#### **2.1 – TOTVS Gestão Hospitalar:**

**- Menu Ambiente/Parâmetros Gestão Hospitalar:** preencher os dados do Datasul no item “Integrações/Integração BackOffice/Gestão de Estoque Compras e Faturamento/**Parâmetros E.M.S.**

O item “Parâmetros E.M.S somente ficará habilitado se existir integração com Datasul.

O campo “Estabelecimento” é o principal campo da integração, que deve existir o mesmo código no Datasul e corresponde ao campo "SiteID".

**- Menu Ambiente/Parâmetros Gestão Hospitalar:** preencher os tipos de movimentos no item “Integrações/Integração BackOffice/Gestão de Estoque Compras e Faturamento/**Tipos de Movimentação de Estoque.**

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

/\*Inclusão de tipos de movimento\*/  
INSERT INTO TTMV (CODCOLIGADA,CODTMV, NOME) VALUES (1,'2.1.01','Saida de Estoque');  
INSERT INTO TUSRTMV (CODUSUARIO,CODCOLIGADA,CODTMV,INCLUIR,ALTERAR,EXCLUIR,CANCELAR,LANCAR,  
                     FATURAR,ATIVAR,IMPRIMIR,ALTERARDEPOISIMP,REABRIR,CONSULTAR,COPIAR,  
                     CONTABILIZAR,REIMPRIMIR,ESTORNARCONTAB,INCLUIRPORFAT,ALTERARDEPOISEMAIL,EMAIL,COTAR)  
VALUES ('mestre','1','2.1.01','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','1','1','1');

INSERT INTO TTMV (CODCOLIGADA,CODTMV, NOME) VALUES (1,'2.1.02','Pedido NF');  
INSERT INTO TUSRTMV (CODUSUARIO,CODCOLIGADA,CODTMV,INCLUIR,ALTERAR,EXCLUIR,CANCELAR,LANCAR,  
                     FATURAR,ATIVAR,IMPRIMIR,ALTERARDEPOISIMP,REABRIR,CONSULTAR,COPIAR,  
                     CONTABILIZAR,REIMPRIMIR,ESTORNARCONTAB,INCLUIRPORFAT,ALTERARDEPOISEMAIL,EMAIL,COTAR)  
VALUES ('mestre','1','2.1.02','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','1','1','1');

INSERT INTO TTMV (CODCOLIGADA,CODTMV, NOME) VALUES (1,'2.1.03','Titulo a Receber');  
INSERT INTO TUSRTMV (CODUSUARIO,CODCOLIGADA,CODTMV,INCLUIR,ALTERAR,EXCLUIR,CANCELAR,LANCAR,  
                     FATURAR,ATIVAR,IMPRIMIR,ALTERARDEPOISIMP,REABRIR,CONSULTAR,COPIAR,  
                     CONTABILIZAR,REIMPRIMIR,ESTORNARCONTAB,INCLUIRPORFAT,ALTERARDEPOISEMAIL,EMAIL,COTAR)  
VALUES ('mestre','1','2.1.03','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','1','1','1');

INSERT INTO TTMV (CODCOLIGADA,CODTMV, NOME) VALUES (1,'1.1.01','Entrada de Estoque');  
INSERT INTO TUSRTMV (CODUSUARIO,CODCOLIGADA,CODTMV,INCLUIR,ALTERAR,EXCLUIR,CANCELAR,LANCAR,  
                     FATURAR,ATIVAR,IMPRIMIR,ALTERARDEPOISIMP,REABRIR,CONSULTAR,COPIAR,  
                     CONTABILIZAR,REIMPRIMIR,ESTORNARCONTAB,INCLUIRPORFAT,ALTERARDEPOISEMAIL,EMAIL,COTAR)  
VALUES ('mestre','1','1.1.01','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','1','1','1');

INSERT INTO TTMV (CODCOLIGADA,CODTMV, NOME) VALUES (1,'1.1.02','Titulo a Pagar');  
INSERT INTO TUSRTMV (CODUSUARIO,CODCOLIGADA,CODTMV,INCLUIR,ALTERAR,EXCLUIR,CANCELAR,LANCAR,  
                     FATURAR,ATIVAR,IMPRIMIR,ALTERARDEPOISIMP,REABRIR,CONSULTAR,COPIAR,  
                     CONTABILIZAR,REIMPRIMIR,ESTORNARCONTAB,INCLUIRPORFAT,ALTERARDEPOISEMAIL,EMAIL,COTAR)  
VALUES ('mestre','1','1.1.02','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','1','1','1');

### **2.2 – TOTVS Gestão de Estoque Compras e Faturamento**

Parâmetros a serem definidos:

#### **Máscara de Centro de Custo: necessário sua configuração na base de dados, antes que se inicie qualquer lançamento.**

### **Máscara para Local de estoque**

### **Máscara de Produto:**

### **Tipos de Movimentos:**

## **2.3 – TOTVS IPAAS (DIAGRAMAS)**

**Dica técnica para Desenvolvedores de Software:** para Diagramas que utilizam o método GET, deverá ser implementado nos sistemas, uma chamada PostAsync para que funcione a chamada à API no iPaaS. O campo TransactionType deve ser mapeado no diagrama componente Generator com o nome iniciado com letra maiúscula, ou seja transactionType vai gerar dado incorreto.

**Mensagem de retorno MethodNotAllowed:** Caso sua aplicação ou cliente utilize filtros de IP (firewall) para controle de acesso, será necessário incluir os novos endereços para garantir a continuidade do serviço. Lembrando que os IPs que já existem serão mantidos, a lista com todos IPs pode ser encontrada <https://tdn.totvs.com/x/Lm3WMg>

scriptScript de Integração

## **Script necessários para habilitar a integração com o TOTVS iPaaS**

**1 - Habilitar integração Saude x Datasul: coluna INTEGRASAUDEEMS**

INSERT INTO HCPARAMETROS  
(CODCOLIGADA, NOMECOLUNA, VALORINT)  
VALUES (0,  'INTEGRASAUDEEMS', '1' )

**2 - Habilitar a integração Totvs IPaaS com o BackOffice Datasul**

O script abaixo estará disponibilizado no conversor do release 12.1.2510 para todos os clientes (mesmo os que não utilizam integração com o Totvs IPaas).

Para ativar a integração com iPaaS, o valor do campo deve ser VALORINT = 1.

INSERT INTO HCPARAMETROS  
(CODCOLIGADA, NOMECOLUNA, VALORINT)  
VALUES (0, 'INTEGRATOTVSIPAAS', '0' )

**3 - Habilitar nome da URL do iPaaS para o envio da Movimentação de Estoque (stockMovementPublic) - POST**

O Nome da Coluna é igual a TOTVSIPAAS\_STOCKMOVEMENTPUBLIC e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/21b71a4a-43d2-405f-8231-702bc91186cc/api-key/50123758-cfa4-4be1-8f15-a399509dd848>'

INSERT INTO HCPARAMETROS  
(CODCOLIGADA, NOMECOLUNA, VALORSTR)  
VALUES (0, 'TOTVSIPAAS\_STOCKMOVEMENTPUBLIC', exemplo\_Url )

**4 - Habilitar nome da URL do iPaaS para consulta de Saldo de Estoque Datasul  (stockBalancePublic) - GET**

O Nome da Coluna é igual a TOTVSIPAAS\_STOCKBALANCEPUBLIC e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/bf123719-26b0-4731-925c-acc91e0aa1f3/api-key/90edafcc-5214-46d3-a193-983142b44cdf>'

INSERT INTO HCPARAMETROS  
(CODCOLIGADA, NOMECOLUNA, VALORSTR)  
VALUES (0,  'TOTVSIPAAS\_STOCKBALANCEPUBLIC', exemplo\_Url )

**5 - Habilitar nome da URL do iPaaS para consulta de Preço do Item Datasul (itemPricePublic) - GET**

O Nome da Coluna é igual a TOTVSIPAAS\_ITEMPRICEPUBLIC e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/8cefcee1-a73e-4448-adf4-02044c48f378/api-key/7f22da1a-1caa-4cea-a8f3-b8c538933cb4>'

INSERT INTO HCPARAMETROS  
(CODCOLIGADA, NOMECOLUNA, VALORSTR)  
VALUES (0,  'TOTVSIPAAS\_ITEMPRICEPUBLIC', exemplo\_Url )

**6 - Habilitar nome da URL do iPaaS para integração do Grupo de Estoque - POST, PUT e DELETE**

O Nome da Coluna é igual a TOTVSIPAAS\_INVENTORYGROUPS e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/a33878b5-d94f-414a-af63-48f1fa5f528e/api-key/4440950e-d733-4856-843b-8d8e337b26ee>'

INSERT INTO HCPARAMETROS  
(CODCOLIGADA, NOMECOLUNA, VALORSTR)  
VALUES (0,  'TOTVSIPAAS\_INVENTORYGROUPS', exemplo\_Url )

**7 - Habilitar nome da URL do iPaaS para integração do Unidade de Medida - POST, PUT e DELETE**

O Nome da Coluna é igual a TOTVSIPAAS\_UNITYMEASURES e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/b2ce305c-8f52-4007-9312-748a97445ddc/api-key/d1c953f0-7fc5-4ffd-9717-8b2ef6ea06ec>'

INSERT INTO HCPARAMETROS  
(CODCOLIGADA, NOMECOLUNA, VALORSTR)  
VALUES (0,  'TOTVSIPAAS\_UNITYMEASURES', exemplo\_Url )

**8 - Habilitar nome da URL do iPaaS para integração do Produto - POST e PUT**

O Nome da Coluna é igual a TOTVSIPAAS\_PRODUCT e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/f4daae6b-5fb3-46c9-bb9e-048f4782197d/api-key/2dfd9868-e50c-471e-b613-794fe67bc75b>'

INSERT INTO HCPARAMETROS  
(CODCOLIGADA, NOMECOLUNA, VALORSTR)  
VALUES (0,  'TOTVSIPAAS\_PRODUCT', exemplo\_Url )

dicaTecnicaDicas Técnicas para construção no Totvs IPASS

**Treinamento Totvs IPAAS:****<https://academy.fluig.com/local/fluig_search/?q=ipaas>**

**OU**

**Na Universidade Totvs**

**TOTVS iPaaS Primeiros passos: <https://unit.edusense.app/#/player/2375?lesson_id=33366>**

**TOTVS iPaaS Intermediario: <https://unit.edusense.app/#/player/2607?lesson_id=35886>**
