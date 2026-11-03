---
content_hash: 3a8223a6f25b36bb7f5be082486cac63c317635b35b2f31b8073ddfdf488c41f
fetched_at: '2026-06-29T00:12:13.945265+00:00'
page_id: '961008258'
product: rm
source: tdn-rm
title: Integração TOTVS Gestão Hospitalar x Backoffice Protheus (middleware TOTVS
  iPaaS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=961008258
version: 5
---

ProtheusvisaoGeralVisão Geral

## **Visão Geral**

Esta documentação tem como objetivo descrever como funciona a integração do ERP TOTVS Gestão Hospitalar com o BackOffice Protheus, utilizando a plataforma TOTVS iPaaS como middleware de comunicação.

Informações sobre o Totvs iPaaS no link <https://tdn.totvs.com/x/3AaFO>

preRequisito-totvsPré-Requisitos Totvs

## **Pré-requisitos no ambiente BackOffice TOTVS RM**

- Importação das Fórmulas Visuais dos cadastros através do TOTVS Compartilhamento.

- Script para habilitar integração Saúde x Protheus: tabela HCPARAMETROS campo INTEGRASAUDEEMS (vide aba Script).

- Scripts para habilitar e configurar a integração com o TOTVS IPaaS (vide aba Script).

### **2 – Cadastros obrigatórios no TOTVS**

#### **2.1 – TOTVS Serviços Globais:**

**- Menu Administração/Cadastros/Coligadas:** preencher o campo "Código Externo" com o código da Empresa do Protheus.

Esse campo é o principal campo da integração, que deve existir o mesmo código no Protheus e corresponde ao campo "CompanyID".

scriptScript de Integração

## **Script necessários para habilitar a integração com o TOTVS iPaaS**

**1 - Habilitar integração Saude x Protheus: coluna INTEGRASAUDEEMS**

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORINT) VALUES (0,  'INTEGRASAUDEEMS', '1' )

**2 - Habilitar a integração Totvs IPaaS com o BackOffice Protheus**

O script abaixo estará disponibilizado no conversor do release 12.1.2510 para todos os clientes (mesmo os que não utilizam integração com o Totvs IPaas).

Para ativar a integração com iPaaS, o valor do campo deve ser VALORINT = 1.

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORINT) VALUES (0, 'INTEGRATOTVSIPAAS', '0' )

**3 - Habilitar nome da URL do iPaaS para o envio do Cadastro de Centros de Custo (CostCenter) - POST, PUT e DELETE**

O Nome da Coluna é igual a TOTVSIPAAS\_COSTCENTER e a coluna VALORSTR deverá conter a URL específica do diagrama padrão de integração ou o diagrana do cliente em caso de customizações.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/21b71a4a-43d2-405f-8231-702bc91186cc/api-key/50123758-cfa4-4be1-8f15-a399509dd848>'

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORSTR) VALUES (0, 'TOTVSIPAAS\_COSTCENTER', exemplo\_Url )

**4 - Habilitar nome da URL do iPaaS para o envio do Cadatros de Cliente/Fornecedor (CustomerVendor) - POST, PUT e DELETE**

O Nome da Coluna é igual a TOTVSIPAAS\_CUSTOMERVENDOR e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/bf123719-26b0-4731-925c-acc91e0aa1f3/api-key/90edafcc-5214-46d3-a193-983142b44cdf>'

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORSTR) VALUES (0,  'TOTVSIPAAS\_CUSTOMERVENDOR ', exemplo\_Url )

**5 - Habilitar nome da URL do iPaaS para integração do Unidade de Medida (UnitOfMeasure) - POST, PUT e DELETE**

O Nome da Coluna é igual a TOTVSIPAAS\_UNITYMEASURES e a coluna VALORSTR deverá conter a URL específica do diagrama de cada Cliente.

Exemplo de uma URL do webhook - exemplo\_Url =  '<https://api-ipaas.totvs.app/sync-hook/api/v1/integrations/b2ce305c-8f52-4007-9312-748a97445ddc/api-key/d1c953f0-7fc5-4ffd-9717-8b2ef6ea06ec>'

###### INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORSTR) VALUES (0,  'TOTVSIPAAS\_UNITYMEASURES', exemplo\_Url )

preRequisitoPré-Requisitos Protheus

## **Pré Requisitos no ambiente BackOffice PROTHEUS:**

- API devem estar configuradas para acesso por IP Público.

- API disponibilizadas para a integração:

|  |  |  |  |
| --- | --- | --- | --- |
| **Mensagem** | **Descrição** | **Parametrização (TOTVS Gestão Hospitalar)** | **OBS (TOTVS Gestão Hospitalar)** |
| CostCenter(POST, PUT, DELETE) | {servidor}/api/ctb/v1/costcentersA API Protheus = CostCenter, é responsável pelo cadastro dos centros de custo no Protheus a partir do cadastro feito no TOTVS Gestão Hospitalar. | TOTVSIPAAS\_COSTCENTER | Fórmula visual para cadastro de centro de custoSAUWKF005 - IPAAS - Integração Cadastro de Centro de Custos.TotvsWFDisponibilizada nos objetos gerenciais do Totvs Compartilhamento |
| CustomerVendor(POST, PUT, DELETE) | {servidor}/api/crm/v1/customerVendorA API Protheus = CustomerVendor, é responsável pelo cadastro dos Clientes/Fornecedores no Protheus a partir do cadastro feito no TOTVS Gestão Hospitalar. | TOTVSIPAAS\_CUSTOMERVENDOR | Fórmula visual para cadastro de cliente/fornecedor no backoffice refrentes ao cadastro de Prestadores (Fornecedor) e Convênios/Pacientes (Cliente).SAUWKF008 - IPAAS - Integração Cadastro de Cliente/Fornecedor (Prestador/Convênio).TotvsWFDisponibilizada nos objetos gerenciais do Totvs Compartilhamento |
| UnitOfMeasure(POST, PUT, DELETE) | {servidor}/api/supply/v2/UnitOfMeasuresA API Protheus = UnitOfMeasure, é responsável pelo cadastro dos unidades de medida no Protheus a partir do cadastro feito no TOTVS Gestão Hospitalar. | TOTVSIPAAS\_UNITYMEASURES | Fórmula visual para cadastro de unidade de medidasSAUWKF007 - IPAAS - Integração Unidade de Medida.TotvsWFDisponibilizada nos objetos gerenciais do Totvs Compartilhamento |

totvsFVFórmulas Visuais - TOTVS Gestão Hospitalar

## **Fórmulas Visuais - TOTVS Gestão Hospitalar**

Nessa integração as Fórmular Visuais são utilizadas como gatilho para que o sistema integre os cadastros com o Protheus.

Essas fórmulas visuais são disponibilizadas no [TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento) e para seu uso essas deverão ser configuradas no sistema conforme orientações abaixo:

|  |  |  |  |
| --- | --- | --- | --- |
| **FÓRMULA VISUAL** | **DESCRIÇÃO** | **GATILHO** | **DATASERVER** |
| SAUWKF005 - IPAAS - Integração Cadastro de Centro de Custos | FV responsável pelo cadastro de Centros de Custo - (Inclusão, Alteração e Remoção) | Após Salvar o Registro | CtbCCustoData |
| SAUWKF008 - IPAAS - Integração Cadastro de Cliente/Fornecedor (Prestador/Convênio) | FV responsável pelo cadastro de Cliente/Fornecedor no Protheus e referente aos cadastros de Responsável Financeiro do Paciente / Convênio (Cliente) e  cadastro de Prestdores (Fornecedor) - (Inclusão, Alteração e Remoção) | Após Salvar o Registro | SauCadGeralConvDataSauCadGeralData |
| SAUWKF007 - IPAAS - Integração Unidade de Medida | FV responsável pelo cadastro de Unidades de Medida - (Inclusão, Alteração e Remoção) | Após Salvar o Registro | EstUndData |

totvsIpaasTotvs iPaaS - Diagramas

## **Diagramas do TOTVS iPaaS para Integração com Protheus**

**Mensagem de retorno MethodNotAllowed:** Caso sua aplicação ou cliente utilize filtros de IP (firewall) para controle de acesso, será necessário incluir os novos endereços para garantir a continuidade do serviço. Lembrando que os IP que já existem serão mantidos, a lista com todos IP pode ser encontrada <https://tdn.totvs.com/x/Lm3WMg>

|  |  |  |
| --- | --- | --- |
| **NOME DO DIAGRAMA** | **DESCRIÇÃO DO DIAGRAMA** | **Uso no Totvs Gestão Hospitalar** |
| Centro de Custo (Protheus) | Diagrama responsável pela integração do cadastro de Centros de Custo no Protheus. Realiza inclusão, alteração e exclusão. | Utilizado em Fórmulas Visuais do Totvs Gestão Hospitalar. |
| Cliente/Fornecedor (Protheus) | Diagrama responsável pela integração do cadastro de Cliente/Fornecedor no Protheus. Realiza inclusão, alteração e exclusão. | Utilizado em Fórmulas Visuais do Totvs Gestão Hospitalar.Processos executados no Totvs Gestão Hospitalar:  * Responsável Financeiro pelo Paciente / Convênio : Cliente * Prestadores :  Fornecedor |
| Unidades de Medida | Diagrama responsável pela integração do cadastro de Unidades de Medidas no Protheus. Realiza inclusão, alteração e exclusão. | Utilizado em Fórmulas Visuais do Totvs Gestão Hospitalar. |
