---
content_hash: b8328cb6f2a0ace3ccb37590ebdbd2efde3f94a8bb311ad3154b3526f249a2e5
fetched_at: '2026-06-29T00:05:54.035386+00:00'
page_id: '1073766180'
product: rm
source: tdn-rm
title: Integração - Configuração RM x RD Station
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1073766180
version: 7
---

Este documento descreve as etapas necessárias para realizar a integração com RD Station Marketing utilizando ambientes staging do SmartLink e a plataforma IpaaS no ecossistema TOTVS.

Integracaoconfig\_smartlinkConfiguração SmartLink

## **1. Configuração do Banco de Dados (API de Staging)**

Para apontar o ambiente para o servidor de staging do SmartLink, é necessário ajustar os parâmetros diretamente na base de dados. 

**1.1. Atualização do Endpoint**

Execute o script abaixo na base de dados para atualizar a URL do endpoint para o ambiente de homologação: 

sql1Atualiza ParâmetroInfo

**Nota:** A ausência do termo "staging" na URL indica que o parâmetro apontará para a API de produção

**1.2. Consulta de Verificação**

Para validar se o parâmetro foi gravado corretamente, execute o comando de seleção:

sqlConsulta Parâmetro

# **2. Configurações Globais do Sistema**

**2.1. Definição do Tipo de Ambiente**

1. Acesse o módulo **Serviços Globais**.
2. Garanta que o campo **Tipo de Ambiente** esteja configurado explicitamente como **"Homologação"**.

**2.2. Configuração do License Server**

O correto funcionamento do IpaaS depende obrigatoriamente de uma licença válida. Atualmente, o servidor dedicado a essa homologação deve ser parametrizado da seguinte forma: 

1. Acesse a tela de **Parâmetros Globais**.
2. Vá até a aba **License Server**.
3. Preencha os campos conforme as especificações abaixo:

| Campo | Valor |
| --- | --- |
| Endereço IP | 10.171.32.220 |
| Porta | 5555 |

Importante

Após salvar as alterações, é mandatório **reiniciar o host** para que as novas configurações entrem em vigor

# **3. Ativação e Configuração do SmartLink**

**3.1. Criação do Ambiente e Credenciais**

1. Navegue pelo menu: **Integração > Totvs App > Ativação Smartlink**.
2. No configurador, preencha o **Nome do Ambiente** seguindo a nomenclatura recomendada:
   * **Padrão de Nome:** `{TipoBanco}-{NomeDaMaquina}-{NomeDaBase}`
   * **Exemplo prático:** `sql-BHN050104633-ImbModeloR1212510_SmartLink_IpaaS`
3. Selecione a opção para **Criar novo ambiente e gerar credenciais**.

**3.2. Diagnóstico e Sincronização**

Após a criação, o ambiente passará por um processo automático que pode levar alguns minutos. 

1. Acesse a tela **Diagnóstico Smartlink**.
2. Na aba **Integração** e certifique-se de que o campo **Status do ambiente** mudou para **"Integrado"**.
3. Na tabela de *Servidores executando*, verifique se os seguintes serviços estão listados com o status **Ativo**:
   * Credential Helper
   * Behavior Sharing

provisionamento\_ipaasProvisionamento IpaaS

# **1. Provisionamento do Ambiente IpaaS**

Após a ativação do SmartLink, pode seguir para solicitar o provisionamento do IpaaS utilizando o assistente do TCGI

**1.1. Verificação de Requisitos**

1. Acesse o assistente pelo caminho: **Construção > Gestão de Imóveis > Utilitários > Configuração Integração RD Station Marketing > Processos > Assistente Configuração RD Station Marketing**.
2. Na primeira tela (*Passo 1 de 3 - Verificação de Requisitos*), certifique-se de que o sistema exibe o ícone verde com a mensagem **"Smartlink ativo"**.
3. Clique em **Avançar**.

**1.2. Workaround Obrigatório: Provisionamento Direto via API**

Atenção Crítica

Através do fluxo normal do sistema, o assistente depende de um serviço de segundo plano que ainda está sendo desenvolvido pela equipe de *framework* (lib). **Portanto, NÃO execute o processo pelo assistente do ERP por enquanto.** Para que o provisionamento funcione, você deve realizar uma requisição HTTP manual, utilizando ferramentas como Postman.

Isso é apenas para ambiente staging, em produção o fluxo do sistema funciona corretamente

**Detalhes da Requisição API:**

* Método: POST
* URL: <https://api-ipaas.staging.totvs.app/provisioning-worker/api/v1/custom/provision>
* Headers:
  + x-api-key: ea2ca33f-7676-4109-8d75-6ccaf9f5b50b

**Corpo da Requisição (JSON Body):**

Os dados fixos abaixo referem-se à utilização atrelada ao License Server `10.171.32.220:5555`:

jsBody

* **tenantId:** Deve ser copiado exatamente como consta na sua tela de **Diagnóstico SmartLink**.
* **totvsId:** Deve ser enviado em branco (`""`).
* **requestUser:** Substitua pelo seu e-mail corporativo.

**1.3. Seleção de Coligadas (Em produção esse fluxo funciona corretamente)**

No assistente do sistema (*Passo 2 de 3*), é possível visualizar a listagem de coligadas. 

Quando a lib liberar o serviço oficial, a orientação será selecionar as coligadas desejadas para a sincronização automática com o RD Station e clicar em **Executar**.

**2. Validação Final e Acesso**

* Após o envio com sucesso do provisionamento via API, um e-mail de ativação será disparado para o usuário administrador cadastrado da empresa.
* Como a plataforma permite apenas **um único usuário administrador**, você precisará:
  + Utilizar as credenciais do administrador atual: `cep.app@totvs.com.br`
  + Credenciais em "<https://docs.google.com/document/d/181XyuMIyM3jWNaMbfj_krSSaqNRO8K9xJ8PkKLMJ5M0/edit>"
* Ao receber a confirmação por e-mail, realize o login na interface do IpaaS com a conta administradora para realizar os testes finais e atestar o sucesso da integração.
  + <https://ipaas.staging.totvs.app/>

diagrama\_ipaasConfiguração Diagramas IpaaS

## **1. Visão Geral**

Esta documentação descreve a implementação da mensagem de integração entre o sistema **TOTVS Gestão de Imóveis (RM)** e o **RD Marketing (RD Station)** através da plataforma iPaaS. O objetivo principal desta funcionalidade é permitir a ativação (habilitação) e desativação da integração de forma estruturada.

A arquitetura foi projetada para receber inicialmente um único parâmetro de envio, porém possui uma estrutura extensível que permite a evolução para novos parâmetros futuramente, conforme a necessidade do negócio.

## **2. Configurações do SmartLink Hook (iPaaS)**

No ambiente do iPaaS, foram estabelecidas audiências específicas para o correto direcionamento e recebimento das mensagens e eventos correspondentes.

| Fluxo / Funcionalidade | Identificador da Audiência (Audience) |
| --- | --- |
| **Recebimento de Eventos** | rmgestaodeimoveisposvendaipaasrdstationaudience |
| **Envio de Integração (Habilitar/Desabilitar)** | rmimbposvendardmarketingintegrationaudience |

## **3. Especificações da Mensagem de Envio**

Para o gatilho de ativação ou desativação, o ecossistema iPaaS deve ser configurado utilizando um tipo de mensagem específico.

* **Tipo de Mensagem:** RMImbRDMarketingIntegrationEvent

### **3.1. Estrutura do Corpo do JSON (Payload de Envio)**

O objeto de envio contém a propriedade booleana responsável por indicar se a integração deve ser interrompida/desabilitada:

{  
  "RDMarketingIntegrationDisabled": true  
}

## **4. Especificações da Mensagem de Resposta (Retorno)**

Após o processamento da solicitação, o fluxo retorna uma mensagem de confirmação detalhando o sucesso da operação, o ID de correlação e o status atual da integração.

### **4.1. Estrutura do Corpo do JSON (Payload de Resposta)**

{  
  "CorrelationId": "4384c74e-f921-4858-89fe-46360430ee8c",  
  "Success": true,  
  "RDMarketingIntegrationDisabled": true,  
  "Message": "A integração RM x RD Marketing foi Desabilitada."  
}

## **5. Próximos Passos e Validação**

Para a continuidade do processo de homologação e detalhamento de regras de negócio adicionais, faz-se necessária a validação junto aos responsáveis técnicos da área.
